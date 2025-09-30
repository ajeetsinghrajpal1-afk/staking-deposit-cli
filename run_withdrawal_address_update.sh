#!/bin/bash
#
# Quick Start Script: Update Withdrawal Address for Validator 8499
#
# This script runs the BLS-to-execution change command with the pre-filled
# parameters for updating the withdrawal address.
#
# SECURITY WARNINGS:
# - Run this on an OFFLINE and SECURE device only
# - You will be prompted for your mnemonic - never share it
# - Verify all parameters before proceeding
#
# Parameters:
# - Validator Index: 8499
# - Old BLS Withdrawal Credentials: 0x00101ca78a5ea9aad05eeffebadc2734754badb9620a4adb366e6013da054b51
# - New Execution Address: 0x06EE840642a33367ee59fCA237F270d5119d1356
# - Chain: mainnet
#

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
VALIDATOR_INDEX="8499"
OLD_BLS_WITHDRAWAL_CREDENTIALS="0x00101ca78a5ea9aad05eeffebadc2734754badb9620a4adb366e6013da054b51"
NEW_EXECUTION_ADDRESS="0x06EE840642a33367ee59fCA237F270d5119d1356"
CHAIN="mainnet"
VALIDATOR_START_INDEX="0"
OUTPUT_FOLDER="./bls_to_execution_changes"

# Banner
echo ""
echo "================================================================================"
echo "         BLS-to-Execution Change - Withdrawal Address Update                  "
echo "================================================================================"
echo ""
echo "${YELLOW}⚠️  SECURITY WARNING ⚠️${NC}"
echo ""
echo "- Use this tool on an OFFLINE and SECURE device"
echo "- Never share your mnemonic with anyone"
echo "- Backup your files securely"
echo ""
echo "================================================================================"
echo ""
echo "Configuration:"
echo "  Validator Index:                ${GREEN}${VALIDATOR_INDEX}${NC}"
echo "  Old BLS Withdrawal Credentials: ${YELLOW}${OLD_BLS_WITHDRAWAL_CREDENTIALS}${NC}"
echo "  New Execution Address:          ${GREEN}${NEW_EXECUTION_ADDRESS}${NC}"
echo "  Chain:                          ${CHAIN}"
echo "  Output Folder:                  ${OUTPUT_FOLDER}"
echo ""
echo "================================================================================"
echo ""

# Ask for confirmation
read -p "Do you want to proceed? (yes/no): " CONFIRM
if [ "$CONFIRM" != "yes" ] && [ "$CONFIRM" != "y" ]; then
    echo ""
    echo "${RED}Operation cancelled.${NC}"
    echo ""
    echo "To run manually, use:"
    echo ""
    echo "  ./deposit.sh \\"
    echo "    --language english \\"
    echo "    generate-bls-to-execution-change \\"
    echo "    --chain ${CHAIN} \\"
    echo "    --validator_start_index ${VALIDATOR_START_INDEX} \\"
    echo "    --validator_indices ${VALIDATOR_INDEX} \\"
    echo "    --bls_withdrawal_credentials_list ${OLD_BLS_WITHDRAWAL_CREDENTIALS} \\"
    echo "    --execution_address ${NEW_EXECUTION_ADDRESS}"
    echo ""
    exit 0
fi

echo ""
echo "Proceeding with withdrawal address update..."
echo ""

# Create output folder if it doesn't exist
mkdir -p "$OUTPUT_FOLDER"

# Check if deposit.sh exists
if [ ! -f "./deposit.sh" ]; then
    echo "${RED}ERROR: deposit.sh not found!${NC}"
    echo "Please run this script from the staking-deposit-cli repository root."
    exit 1
fi

# Make deposit.sh executable if needed
chmod +x ./deposit.sh

# Run the command
echo "Running BLS-to-execution change command..."
echo "You will be prompted for your mnemonic..."
echo ""

./deposit.sh \
  --language english \
  generate-bls-to-execution-change \
  --chain "$CHAIN" \
  --bls_to_execution_changes_folder "$OUTPUT_FOLDER" \
  --validator_start_index "$VALIDATOR_START_INDEX" \
  --validator_indices "$VALIDATOR_INDEX" \
  --bls_withdrawal_credentials_list "$OLD_BLS_WITHDRAWAL_CREDENTIALS" \
  --execution_address "$NEW_EXECUTION_ADDRESS"

EXIT_CODE=$?

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo "================================================================================"
    echo "${GREEN}✓ SUCCESS!${NC}"
    echo "================================================================================"
    echo ""
    echo "The BLS-to-execution change file has been generated in:"
    echo "  ${GREEN}${OUTPUT_FOLDER}/${NC}"
    echo ""
    echo "Next steps:"
    echo "  1. Verify the generated JSON file"
    echo "  2. Submit the file to your beacon node or validator client"
    echo "  3. Monitor the transaction on https://beaconcha.in/validator/${VALIDATOR_INDEX}"
    echo ""
    echo "For detailed instructions, see: WITHDRAWAL_ADDRESS_UPDATE_GUIDE.md"
    echo ""
else
    echo "================================================================================"
    echo "${RED}✗ FAILED${NC}"
    echo "================================================================================"
    echo ""
    echo "The command failed with exit code: $EXIT_CODE"
    echo "Please check the error messages above."
    echo ""
    echo "For help, see: WITHDRAWAL_ADDRESS_UPDATE_GUIDE.md"
    echo ""
fi

exit $EXIT_CODE
