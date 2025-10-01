import asyncio
import os
import sys


# For not importing staking_deposit here
DEFAULT_VALIDATOR_KEYS_FOLDER_NAME = 'validator_keys'


async def main(argv):
    # Use deposit.sh as the CLI entry point
    my_folder_path = os.path.join(os.getcwd(), 'TESTING_TEMP_FOLDER')
    if not os.path.exists(my_folder_path):
        os.mkdir(my_folder_path)

    cmd_args = [
        'bash', 'deposit.sh',
        '--language', 'english',
        '--non_interactive',
        'new-mnemonic',
        '--num_validators', '1',
        '--mnemonic_language', 'english',
        '--chain', 'mainnet',
        '--keystore_password', 'MyPassword',
        '--folder', my_folder_path,
    ]
    proc = await asyncio.create_subprocess_exec(
        *cmd_args,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    proc = await asyncio.create_subprocess_shell(
        ' '.join(cmd_args),
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    seed_phrase = ''
    parsing = False
    found_mnemonic_msg = False
    async for out in proc.stdout:
        output = out.decode('utf-8').strip()
        if found_mnemonic_msg and output:
            seed_phrase = output
            break
        if 'This is your mnemonic' in output or 'Your mnemonic' in output:
            found_mnemonic_msg = True
        print(output)

    async for out in proc.stderr:
        output = out.decode('utf-8').strip()
        print(f'[stderr] {output}')

    assert len(seed_phrase.split()) >= 12

    # Check files
    validator_keys_folder_path = os.path.join(my_folder_path, DEFAULT_VALIDATOR_KEYS_FOLDER_NAME)
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
