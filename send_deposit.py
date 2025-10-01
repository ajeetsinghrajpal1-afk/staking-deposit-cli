
import os
from web3 import Web3
import json

ETH_NODE_URL = os.environ.get('ETH_NODE_URL', 'https://worldchain-mainnet.g.alchemy.com/v2/LuDq4FkmeHfsQ3lwsAteW')
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

# Provided validator data
pubkey = bytes.fromhex('80000001677f23a227dfed6f61b132d114be83b8ad0aa5f3c5d1d77e6ee0bf5f73b0af750cc34e8f2dae73c21dc36f4a')
# Withdrawal credentials for new address 0x06EE840642a33367ee59fCA237F270d5119d1356
withdrawal_credentials = bytes.fromhex('01000000000000000000000006ee840642a33367ee59fca237f270d5119d1356')
signature = bytes.fromhex('aeb1fe4450903bc9371ace92cd0ffb2b1af17ccc3fab60649eb5e934582381d961f43bef9a430d346e4f280e45a404c710f92e6022381230a8d424138538bae1f60ca64b3c2f1759ddf0883ef6460599a351cfd40e3a7e4cb2c0857cad221275')
deposit_data_root = bytes.fromhex('fca4e92e73f96d11cd907eeb51ff8f149a2f69318c5177520ea4c10b9708be6c')

w3 = Web3(Web3.HTTPProvider(ETH_NODE_URL))
contract = w3.eth.contract(address=DEPOSIT_CONTRACT_ADDRESS, abi=DEPOSIT_CONTRACT_ABI)

private_key = os.environ.get('ETH_PRIVATE_KEY')
if not private_key:
        print('Please set ETH_PRIVATE_KEY in your environment.')
        exit(1)
account = w3.eth.account.from_key(private_key)
print(f'Account address: {account.address}')
balance = w3.eth.get_balance(account.address)
print(f'Account balance: {w3.from_wei(balance, "ether")} ETH')

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
