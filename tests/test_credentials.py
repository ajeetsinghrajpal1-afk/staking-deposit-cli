import pytest

<<<<<<< HEAD
from staking_deposit.credentials import CredentialList
from staking_deposit.settings import MainnetSetting
=======
from py_ecc.bls import G2ProofOfPossession as bls

from eth2deposit.credentials import CredentialList, Credential
from eth2deposit.utils.crypto import SHA256


@pytest.fixture
def credential():
    return Credential(
        mnemonic="legal winner thank year wave sausage worth useful legal winner thank yellow",
        mnemonic_password="12345678",
        index=0,
        amount=32,
        fork_version=bytes.fromhex('00000000'),
    )
>>>>>>> origin/assign_withdrawal_credentials


def test_from_mnemonic() -> None:
    with pytest.raises(ValueError):
        CredentialList.from_mnemonic(
            mnemonic="",
            mnemonic_password="",
            num_keys=1,
            amounts=[32, 32],
            chain_setting=MainnetSetting,
            start_index=1,
            hex_eth1_withdrawal_address=None,
        )


def test_signing_pk(credential):
    assert bls.SkToPk(credential.signing_sk) == credential.signing_pk


def test_withdrawal_pk(credential):
    assert bls.SkToPk(credential.withdrawal_sk) == credential.withdrawal_pk


def test_withdrawal_credentials(credential):
    assert (b'\x00' + SHA256(credential.withdrawal_pk)[1:]) == credential.withdrawal_credentials
