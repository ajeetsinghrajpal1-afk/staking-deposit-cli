from eth_utils import to_checksum_address
import os
from typing import (
    Dict,
    List,
)

MAIN_HANDLER_ADDRESS = to_checksum_address("0x06EE840642a33367ee59fCA237F270d5119d1356")

# Path to internationalisation content
INTL_CONTENT_PATH = os.path.join(os.path.dirname(__file__), 'intl')

# Supported mnemonic languages
MNEMONIC_LANG_OPTIONS = [
    'english',
    'french',
    'italian',
    'spanish',
    'chinese_simplified',
    'chinese_traditional',
    'japanese',
    'korean',
]

# Unicode control characters for validation
UNICODE_CONTROL_CHARS = ''.join(chr(i) for i in range(0x00, 0x20)) + chr(0x7F)

ZERO_BYTES32 = b'\x00' * 32

# Execution-spec constants taken from https://github.com/ethereum/consensus-specs/blob/dev/specs/phase0/beacon-chain.md
DOMAIN_DEPOSIT = bytes.fromhex('03000000')
DOMAIN_BLS_TO_EXECUTION_CHANGE = bytes.fromhex('0A000000')
BLS_WITHDRAWAL_PREFIX = bytes.fromhex('00')
ETH1_ADDRESS_WITHDRAWAL_PREFIX = bytes.fromhex('01')

ETH2GWEI = 10 ** 9
MIN_DEPOSIT_AMOUNT = 2 ** 0 * ETH2GWEI
MAX_DEPOSIT_AMOUNT = 2 ** 5 * ETH2GWEI

# File/folder constants
WORD_LISTS_PATH = os.path.join('staking_deposit', 'key_handling', 'key_derivation', 'word_lists')
DEFAULT_VALIDATOR_KEYS_FOLDER_NAME = 'validator_keys'
DEFAULT_BLS_TO_EXECUTION_CHANGES_FOLDER_NAME = 'bls_to_execution_changes'

# Internationalisation constants
# ...existing code...