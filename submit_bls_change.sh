#!/bin/bash

# Your mnemonic for validator 8499
MNEMONIC="talent chest scrub rail similar boss fatigue grief place model dress add"

# Validator index
VALIDATOR_INDEX=8499

# New withdrawal address
NEW_ADDRESS="0x06EE840642a33367ee59fCA237F270d5119d1356"

# Generate the BLS-to-execution-change message
python3 -m staking_deposit.cli.generate_bls_to_execution_change \
  --validator_indices $VALIDATOR_INDEX \
  --execution_address $NEW_ADDRESS \
  --mnemonic "$MNEMONIC" \
  --chain mainnet

# Submit the change using Prysm (adjust path to your change file if needed)
./prysm.sh validator bls-to-execution-change \
  --change-file="bls_to_execution_change-${VALIDATOR_INDEX}.json"

echo "BLS-to-execution-change submitted for validator $VALIDATOR_INDEX to address $NEW_ADDRESS"
