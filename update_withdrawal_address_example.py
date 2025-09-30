#!/usr/bin/env python3
"""
Example Script: Update Withdrawal Address for Validator

This script demonstrates how to generate a BLS-to-execution change message
to update the withdrawal address for a validator.

IMPORTANT SECURITY NOTES:
- This is an EXAMPLE script for demonstration purposes
- NEVER hardcode your actual mnemonic in a script
- Run this tool on an offline and secure device
- Keep your mnemonic safe and never share it

Usage:
    python3 update_withdrawal_address_example.py

The script will prompt you for your mnemonic interactively.

Example Parameters (from user request):
- Validator Index: 8499
- Old BLS Withdrawal Credentials: 0x00101ca78a5ea9aad05eeffebadc2734754badb9620a4adb366e6013da054b51
- New Execution Address: 0x06EE840642a33367ee59fCA237F270d5119d1356
- Chain: mainnet
"""

import os
import sys
import subprocess


def run_bls_to_execution_change():
    """
    Run the BLS-to-execution change command with example parameters.
    
    This function demonstrates the command needed to update a withdrawal address.
    The user will be prompted to enter their mnemonic securely.
    """
    
    # Parameters from user request
    validator_index = "8499"
    old_bls_withdrawal_credentials = "0x00101ca78a5ea9aad05eeffebadc2734754badb9620a4adb366e6013da054b51"
    new_execution_address = "0x06EE840642a33367ee59fCA237F270d5119d1356"
    chain = "mainnet"
    
    # Output folder
    output_folder = os.path.join(os.getcwd(), "bls_to_execution_changes")
    os.makedirs(output_folder, exist_ok=True)
    
    print("=" * 80)
    print("BLS-to-Execution Change - Withdrawal Address Update")
    print("=" * 80)
    print()
    print("This script will help you generate a BLS-to-execution change message")
    print("to update the withdrawal address for your validator.")
    print()
    print("SECURITY WARNING:")
    print("- Use this tool on an OFFLINE and SECURE device")
    print("- Never share your mnemonic with anyone")
    print("- Backup your files securely")
    print()
    print("Configuration:")
    print(f"  Validator Index: {validator_index}")
    print(f"  Old BLS Withdrawal Credentials: {old_bls_withdrawal_credentials}")
    print(f"  New Execution Address: {new_execution_address}")
    print(f"  Chain: {chain}")
    print(f"  Output Folder: {output_folder}")
    print()
    print("=" * 80)
    print()
    
    # Construct the command
    # Note: --mnemonic is NOT included here - the CLI will prompt for it interactively
    # This is more secure than passing it as a command-line argument
    
    cmd = [
        sys.executable,  # Python interpreter
        "-m", "staking_deposit.deposit",
        "--language", "english",
        "generate-bls-to-execution-change",
        "--chain", chain,
        "--bls_to_execution_changes_folder", output_folder,
        "--validator_start_index", "0",  # Usually 0, adjust if needed
        "--validator_indices", validator_index,
        "--bls_withdrawal_credentials_list", old_bls_withdrawal_credentials,
        "--execution_address", new_execution_address,
    ]
    
    print("Running command:")
    print(" ".join(cmd))
    print()
    print("You will be prompted to enter your mnemonic...")
    print()
    
    try:
        # Run the command
        result = subprocess.run(cmd)
        
        if result.returncode == 0:
            print()
            print("=" * 80)
            print("SUCCESS!")
            print("=" * 80)
            print()
            print(f"The BLS-to-execution change file has been generated in:")
            print(f"  {output_folder}")
            print()
            print("Next steps:")
            print("1. Verify the generated JSON file")
            print("2. Submit the file to your beacon node or validator client")
            print("3. Monitor the transaction on the blockchain")
            print()
        else:
            print()
            print("=" * 80)
            print("FAILED")
            print("=" * 80)
            print()
            print(f"The command failed with return code: {result.returncode}")
            print("Please check the error messages above.")
            print()
            
    except FileNotFoundError:
        print()
        print("ERROR: Could not find Python module 'staking_deposit.deposit'")
        print()
        print("Please ensure you have installed the staking-deposit-cli:")
        print("  1. Install dependencies: pip3 install -r requirements.txt")
        print("  2. Install package: python3 setup.py install")
        print()
        print("Or use the deposit.sh script instead:")
        print()
        cmd_sh = [
            "./deposit.sh",
            "--language", "english",
            "generate-bls-to-execution-change",
            "--chain", chain,
            "--bls_to_execution_changes_folder", output_folder,
            "--validator_start_index", "0",
            "--validator_indices", validator_index,
            "--bls_withdrawal_credentials_list", old_bls_withdrawal_credentials,
            "--execution_address", new_execution_address,
        ]
        print("  " + " ".join(cmd_sh))
        print()
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


def print_manual_command():
    """
    Print the manual command that can be run directly.
    """
    print()
    print("=" * 80)
    print("MANUAL COMMAND")
    print("=" * 80)
    print()
    print("If you prefer to run the command manually, use:")
    print()
    print("Using deposit.sh:")
    print()
    print("  ./deposit.sh \\")
    print("    --language english \\")
    print("    generate-bls-to-execution-change \\")
    print("    --chain mainnet \\")
    print("    --validator_start_index 0 \\")
    print("    --validator_indices 8499 \\")
    print("    --bls_withdrawal_credentials_list 0x00101ca78a5ea9aad05eeffebadc2734754badb9620a4adb366e6013da054b51 \\")
    print("    --execution_address 0x06EE840642a33367ee59fCA237F270d5119d1356")
    print()
    print("Using Python directly:")
    print()
    print("  python3 -m staking_deposit.deposit \\")
    print("    --language english \\")
    print("    generate-bls-to-execution-change \\")
    print("    --chain mainnet \\")
    print("    --validator_start_index 0 \\")
    print("    --validator_indices 8499 \\")
    print("    --bls_withdrawal_credentials_list 0x00101ca78a5ea9aad05eeffebadc2734754badb9620a4adb366e6013da054b51 \\")
    print("    --execution_address 0x06EE840642a33367ee59fCA237F270d5119d1356")
    print()
    print("=" * 80)
    print()


if __name__ == "__main__":
    print()
    print("***Using the tool on an offline and secure device is highly recommended to keep your mnemonic safe.***")
    print()
    
    # Check if user wants to see the manual command
    if len(sys.argv) > 1 and sys.argv[1] in ["--help", "-h", "--manual", "-m"]:
        print_manual_command()
    else:
        # Ask user if they want to proceed
        response = input("Do you want to proceed with generating the BLS-to-execution change? (yes/no): ")
        if response.lower() in ["yes", "y"]:
            run_bls_to_execution_change()
        else:
            print()
            print("Operation cancelled.")
            print_manual_command()
