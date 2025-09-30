# Quick Start: Update Withdrawal Address for Validator 8499

This repository includes helper scripts and documentation for updating the withdrawal address for validator 8499.

## Files Included

1. **`run_withdrawal_address_update.sh`** - Interactive shell script (recommended for most users)
2. **`update_withdrawal_address_example.py`** - Python helper script with detailed output
3. **`WITHDRAWAL_ADDRESS_UPDATE_GUIDE.md`** - Comprehensive guide with all options and troubleshooting

## Quick Start

### Option 1: Using the Shell Script (Easiest)

```bash
./run_withdrawal_address_update.sh
```

This script will:
- Show you the parameters that will be used
- Ask for confirmation
- Prompt you for your mnemonic securely
- Generate the BLS-to-execution change file
- Show you the next steps

### Option 2: Using the Python Script

```bash
python3 update_withdrawal_address_example.py
```

Or to see the manual command:

```bash
python3 update_withdrawal_address_example.py --help
```

### Option 3: Manual Command

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

## Configuration Details

| Parameter | Value |
|-----------|-------|
| **Validator Index** | 8499 |
| **Old BLS Withdrawal Credentials** | `0x00101ca78a5ea9aad05eeffebadc2734754badb9620a4adb366e6013da054b51` |
| **New Execution Address** | `0x06EE840642a33367ee59fCA237F270d5119d1356` |
| **Network** | Mainnet |

## Security Warnings ⚠️

- **NEVER share your mnemonic** with anyone
- **Use an OFFLINE and SECURE device** to run these commands
- **Backup all generated files** securely
- **Verify the new address** multiple times before submitting
- **This operation is irreversible** once submitted to the blockchain

## Prerequisites

Before running any of these scripts:

1. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   python3 setup.py install
   ```

2. **Have your mnemonic ready** - You'll need the 24-word recovery phrase used when creating the validator

3. **Verify the parameters** - Double-check that the validator index and addresses are correct

## What Happens

1. The script will prompt you for your mnemonic (it won't be displayed as you type)
2. It validates that your mnemonic matches the old BLS withdrawal credentials
3. It generates a signed JSON file with the change message
4. You then submit this file to the Ethereum network via your beacon node

## Output

After successful execution, you'll find a file like:

```
bls_to_execution_changes/bls_to_execution_change-<timestamp>.json
```

## Next Steps

After generating the file:

1. **Verify the JSON file contents**
2. **Submit to your beacon node** (see guide for specific commands per client)
3. **Monitor on block explorer** - https://beaconcha.in/validator/8499

## For More Help

See the comprehensive guide: **[WITHDRAWAL_ADDRESS_UPDATE_GUIDE.md](WITHDRAWAL_ADDRESS_UPDATE_GUIDE.md)**

This guide includes:
- Detailed step-by-step instructions
- All submission methods
- Troubleshooting tips
- Verification steps
- Additional resources

## Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'Crypto'"**
```bash
pip3 install pycryptodome
```

**"Mnemonic does not match withdrawal credentials"**
- Verify you're using the correct mnemonic
- Check the validator_start_index (usually 0)

**Command not found: ./deposit.sh**
```bash
chmod +x deposit.sh
chmod +x run_withdrawal_address_update.sh
```

For more troubleshooting, see [WITHDRAWAL_ADDRESS_UPDATE_GUIDE.md](WITHDRAWAL_ADDRESS_UPDATE_GUIDE.md).
