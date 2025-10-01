import asyncio
import os
import sys


# For not importing staking_deposit here
DEFAULT_VALIDATOR_KEYS_FOLDER_NAME = 'bls_to_execution_changes'


async def main(argv):
    # Use deposit.sh as the CLI entry point
    my_folder_path = os.path.join(os.getcwd(), 'TESTING_TEMP_FOLDER')
    if not os.path.exists(my_folder_path):
        os.mkdir(my_folder_path)

    # Step 1: Generate a valid mnemonic using the CLI
    gen_mnemonic_cmd = 'bash deposit.sh --language english --non_interactive new-mnemonic --num_validators 1 --mnemonic_language english --chain mainnet --keystore_password MyPassword --folder {}'
    proc_mnemonic = await asyncio.create_subprocess_shell(
        gen_mnemonic_cmd.format(my_folder_path),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    mnemonic = ''
    found_mnemonic_msg = False
    async for out in proc_mnemonic.stdout:
        output = out.decode('utf-8').strip()
        if found_mnemonic_msg and output:
            mnemonic = output
            break
        if 'This is your mnemonic' in output or 'Your mnemonic' in output:
            found_mnemonic_msg = True
    await proc_mnemonic.wait()
    assert len(mnemonic.split()) >= 12

    # Step 2: Use the valid mnemonic for bls-to-execution-change
    run_script_cmd = 'bash deposit.sh'
    cmd_args = [
        '--language', 'english',
        '--non_interactive',
        'generate-bls-to-execution-change',
        '--bls_to_execution_changes_folder', my_folder_path,
        '--chain', 'mainnet',
        '--mnemonic', f'"{mnemonic}"',
        '--bls_withdrawal_credentials_list', '0x00bd0b5a34de5fb17df08410b5e615dda87caf4fb72d0aac91ce5e52fc6aa8de',
        '--validator_start_index', '0',
        '--validator_indices', '1',
        '--execution_address', '0x3434343434343434343434343434343434343434',
    ]
    proc = await asyncio.create_subprocess_shell(
        ' '.join([run_script_cmd] + cmd_args),
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    seed_phrase = mnemonic
    async for out in proc.stdout:
        output = out.decode('utf-8').rstrip()
        print(output)

    async for out in proc.stderr:
        output = out.decode('utf-8').rstrip()
        print(f'[stderr] {output}')

    assert len(seed_phrase) > 0

    # Check files
    validator_keys_folder_path = os.path.join(my_folder_path, DEFAULT_VALIDATOR_KEYS_FOLDER_NAME)
    _, _, key_files = next(os.walk(validator_keys_folder_path))

    # Clean up
    for root, dirs, files in os.walk(my_folder_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(my_folder_path)


if os.name == 'nt':  # Windows
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(sys.argv))
else:
    asyncio.run(main(sys.argv))
