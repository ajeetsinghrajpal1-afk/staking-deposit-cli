"""
Unified staking deposit CLI script.
All deposit and withdrawal operations use the registered address:
0x06EE840642a33367ee59fCA237F270d5119d1356
"""
import os
import json
from typing import Any, Sequence
from eth_typing import HexAddress
from web3 import Web3

# Registered ETH withdrawal address for all operations
REGISTERED_ETH_WITHDRAWAL_ADDRESS = "0x06EE840642a33367ee59fCA237F270d5119d1356"

# Example deposit contract details (update as needed)
DEPOSIT_CONTRACT_ADDRESS = '0x00000000219ab540356cBB839Cbe05303d7705Fa'
DEPOSIT_CONTRACT_ABI = [
    {
        "inputs": [
            {"internalType": "bytes", "name": "pubkey", "type": "bytes"},
            {"internalType": "bytes", "name": "withdrawal_credentials", "type": "bytes"},
            {"internalType": "bytes", "name": "signature", "type": "bytes"},
            {"internalType": "bytes32", "name": "deposit_data_root", "type": "bytes32"}
        ],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]

# Example: deposit transaction function

def broadcast_deposit(pubkey, signature, deposit_data_root, eth_node_url, private_key):
    withdrawal_credentials = bytes.fromhex('01000000000000000000000006ee840642a33367ee59fca237f270d5119d1356')
    w3 = Web3(Web3.HTTPProvider(eth_node_url))
    contract = w3.eth.contract(address=DEPOSIT_CONTRACT_ADDRESS, abi=DEPOSIT_CONTRACT_ABI)
    account = w3.eth.account.from_key(private_key)
    tx = contract.functions.deposit(
        pubkey,
        withdrawal_credentials,
        signature,
        deposit_data_root
    ).build_transaction({
        'from': account.address,
        'value': w3.to_wei(32, 'ether'),
        'gas': 200000,
        'nonce': w3.eth.get_transaction_count(account.address)
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f'Transaction sent: {tx_hash.hex()}')

# Example: key generation and BLS-to-execution-change logic would also enforce REGISTERED_ETH_WITHDRAWAL_ADDRESS
# Add additional unified logic as needed for your workflow

if __name__ == "__main__":
    print("Unified staking deposit CLI. All operations use:", REGISTERED_ETH_WITHDRAWAL_ADDRESS)
    # Add CLI argument parsing and workflow as needed
    # This script is a template for merging all logic into one place
