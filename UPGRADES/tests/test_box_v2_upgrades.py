from scripts.helpful_scripts import get_account, encode_function_data, upgrade
from brownie import Box, ProxyAdmin, TransparentUpgradeableProxy, Contract, BoxV2, exceptions
import pytest

def test_proxy_upgrades():
    account= get_account()
    box=Box.deploy({'from':account})
    proxy_admin= ProxyAdmin.deploy({'from':account})
    box_encoded_initializer_function = encode_function_data()
    proxy=TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {'from':account}
    )
    box_v2=BoxV2.deploy({'from':account})
    proxy_box=Contract.from_abi('BoxV2',proxy.address,BoxV2.abi)
    with pytest.raises(exceptions.VirtualMachineError):
        proxy_box.increment({'from':account})
    
    upgrade(account,proxy,box_v2,proxy_admin_contract=proxy_admin)
    proxy_box.increment({'from':account})
    assert proxy_box.retrieve()==1
    