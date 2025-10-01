#!/bin/bash

# Path to your BLS-to-execution-change message JSON
CHANGE_FILE="bls_to_execution_change-8499.json"

# Beacon node REST API endpoint (default for Prysm is http://localhost:3500)
BEACON_API="http://localhost:3500/eth/v1/beacon/pool/bls_to_execution_changes"

# Submit the BLS-to-execution-change message
curl -X POST \
  -H "Content-Type: application/json" \
  --data @$CHANGE_FILE \
  $BEACON_API

echo "Submitted BLS-to-execution-change for validator 8499 to beacon node REST API."
