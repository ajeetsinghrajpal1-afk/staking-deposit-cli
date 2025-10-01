#!/bin/bash

# Mnemonic for all validators
MNEMONIC="talent chest scrub rail similar boss fatigue grief place model dress add"
# New withdrawal address
NEW_ADDRESS="0x06EE840642a33367ee59fCA237F270d5119d1356"
# Chain
CHAIN="mainnet"
# Output folder
OUT_FOLDER="bls_to_execution_changes"

# Create output folder if it doesn't exist
mkdir -p "$OUT_FOLDER"

# Range of validator indices (edit as needed)
START=8499
END=8528

# Build comma-separated list of indices
INDICES=$(seq -s, $START $END)

# Run the CLI to generate BLS-to-execution-change for all indices
python3 -m staking_deposit.cli.generate_bls_to_execution_change \
  --validator_indices "$INDICES" \
  --execution_address "$NEW_ADDRESS" \
  --mnemonic "$MNEMONIC" \
  --chain "$CHAIN" \
  --folder "$OUT_FOLDER"

echo "BLS-to-execution-change messages generated for indices $INDICES in $OUT_FOLDER/"
