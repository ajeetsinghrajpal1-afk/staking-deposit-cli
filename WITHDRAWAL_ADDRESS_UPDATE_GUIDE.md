# Guide: Updating Withdrawal Address for Validator 8499

This guide provides step-by-step instructions for generating a BLS-to-execution change message to update the withdrawal address for your validator.

## Overview

**Validator Index:** 8499  
**Old BLS Withdrawal Credentials:** `0x00101ca78a5ea9aad05eeffebadc2734754badb9620a4adb366e6013da054b51`  
**New Execution Address:** `0x06EE840642a33367ee59fCA237F270d5119d1356`  
**Network:** Mainnet

## ⚠️ Important Security Warnings

- **NEVER share your mnemonic** with anyone or store it in plain text files
- **Use an OFFLINE and SECURE device** to generate the change message
- **Backup all files securely** before proceeding
- **Verify the new address** multiple times before submitting
- **This operation is irreversible** once submitted to the blockchain

## Prerequisites

1. **Python 3.12+** installed on your system
2. **Your mnemonic phrase** from when you created the validator
3. **The staking-deposit-cli** installed (this repository)

## Installation

If you haven't installed the dependencies yet:

```bash
# Install Python dependencies
pip3 install -r requirements.txt

# Install the package
python3 setup.py install
```

## Option 1: Using the Helper Script (Recommended)

We've created a helper script that makes it easy to run the command with your specific parameters.

### Steps:

1. **Navigate to the repository directory:**
   ```bash
   cd /path/to/staking-deposit-cli
   ```

2. **Run the helper script:**
   ```bash
   python3 update_withdrawal_address_example.py
   ```

3. **Follow the prompts:**
   - You will be asked if you want to proceed
   - Enter "yes" to continue
   - You will then be prompted to enter your mnemonic securely
   - The script will generate the BLS-to-execution change file

4. **Verify the output:**
   - The generated file will be in the `bls_to_execution_changes` folder
   - Review the JSON file to ensure all parameters are correct

### View Manual Command Only

To see the command without running it:

```bash
python3 update_withdrawal_address_example.py --help
```

## Option 2: Using deposit.sh Directly

If you prefer to run the command manually:

```bash
./deposit.sh \
  --language english \
  generate-bls-to-execution-change \
  --chain mainnet \
  --validator_start_index 0 \
  --validator_indices 8499 \
  --bls_withdrawal_credentials_list 0x00101ca78a5ea9aad05eeffebadc2734754badb9620a4adb366e6013da054b51 \
  --execution_address 0x06EE840642a33367ee59fCA237F270d5119d1356
```

## Option 3: Using Python Module Directly

```bash
python3 -m staking_deposit.deposit \
  --language english \
  generate-bls-to-execution-change \
  --chain mainnet \
  --validator_start_index 0 \
  --validator_indices 8499 \
  --bls_withdrawal_credentials_list 0x00101ca78a5ea9aad05eeffebadc2734754badb9620a4adb366e6013da054b51 \
  --execution_address 0x06EE840642a33367ee59fCA237F270d5119d1356
```

## What Happens When You Run The Command

1. **Language Selection:** The CLI will confirm you're using English
2. **Mnemonic Input:** You'll be prompted to enter your 24-word mnemonic phrase
   - Type carefully and verify each word
   - The mnemonic is NOT displayed as you type (for security)
3. **Validation:** The CLI validates that:
   - The mnemonic matches the old BLS withdrawal credentials
   - The new execution address is valid
   - All parameters are correct
4. **File Generation:** A JSON file is created with the signed message
   - Filename format: `bls_to_execution_change-<timestamp>.json`
   - Location: `bls_to_execution_changes/` folder

## Output Files

After successful execution, you will find:

```
bls_to_execution_changes/
└── bls_to_execution_change-<timestamp>.json
```

This JSON file contains the signed BLS-to-execution change message that needs to be broadcast to the Ethereum network.

## Next Steps: Submitting the Change

After generating the file, you need to submit it to the Ethereum network. You have several options:

### Method 1: Using Your Beacon Node

If you're running your own beacon node (e.g., Lighthouse, Prysm, Teku, Nimbus):

```bash
# Example for Lighthouse
lighthouse account validator bls-to-execution-change \
  --file bls_to_execution_changes/bls_to_execution_change-*.json

# Example for Prysm
prism validator bls-to-execution-change \
  --path bls_to_execution_changes/bls_to_execution_change-*.json

# Example for Teku
teku voluntary-exit --bls-to-execution-changes-file bls_to_execution_changes/bls_to_execution_change-*.json
```

Consult your beacon node's documentation for the exact command.

### Method 2: Using Ethereum Launchpad

1. Visit https://launchpad.ethereum.org/
2. Navigate to the "Withdrawal Credentials" section
3. Upload your `bls_to_execution_change-*.json` file
4. Follow the on-screen instructions

### Method 3: Using BeaconScan or Block Explorer

Some block explorers provide a UI for submitting BLS-to-execution changes:

1. Visit https://beaconcha.in/ or similar
2. Navigate to your validator page
3. Look for "Update Withdrawal Credentials" option
4. Upload your JSON file

## Verification

After submitting:

1. **Check on a block explorer:**
   - Visit https://beaconcha.in/validator/8499
   - Look for the withdrawal credentials update
   - Verify the new address matches: `0x06EE840642a33367ee59fCA237F270d5119d1356`

2. **Wait for inclusion:**
   - The change may take several epochs to be processed
   - Monitor your validator status

3. **Confirm the update:**
   - Once processed, your withdrawal credentials should change from:
     - Old: `0x00101ca78a5ea9aad05eeffebadc2734754badb9620a4adb366e6013da054b51`
     - New: `0x0106ee840642a33367ee59fca237f270d5119d1356000000000000000000000000` (Note: the `01` prefix indicates execution layer withdrawal)

## Troubleshooting

### "ModuleNotFoundError: No module named 'Crypto'"

Install pycryptodome:
```bash
pip3 install pycryptodome
```

### "Mnemonic does not match withdrawal credentials"

- Verify you're using the correct mnemonic
- Check that the `validator_start_index` is correct (usually 0)
- Ensure the BLS withdrawal credentials are correct

### "Invalid execution address"

- Verify the address format (should start with 0x and be 42 characters total)
- Check for typos
- Ensure it's a valid Ethereum address with correct checksum

### Command not found: ./deposit.sh

Make sure you're in the repository root directory and the file is executable:
```bash
chmod +x deposit.sh
```

## Additional Resources

- [Ethereum Staking Launchpad](https://launchpad.ethereum.org/)
- [EIP-2334: BLS12-381 Key Derivation](https://eips.ethereum.org/EIPS/eip-2334)
- [Withdrawal Credentials FAQ](https://launchpad.ethereum.org/faq#keys)
- [BeaconScan Validator Explorer](https://beaconcha.in/)

## Support

For issues with the staking-deposit-cli:
- GitHub Issues: https://github.com/ethereum/staking-deposit-cli/issues
- Documentation: https://github.com/ethereum/staking-deposit-cli

---

**Remember:** This is a critical operation. Take your time, verify everything twice, and keep backups of all files!
