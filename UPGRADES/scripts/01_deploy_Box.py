from scripts.helpful_scripts import get_account, encode_function_data
from brownie import Box, network,ProxyAdmin, Contract, TransparentUpgradeableProxy

def main():
    account=get_account()
    print(f'deploying to {network.show_active()}')
    box = Box.deploy({'from':account})
    proxy_admin=ProxyAdmin.deploy({'from':account})
    # If we want an intializer function we can add
    # `initializer=box.store, 1`
    # to simulate the initializer being the `store` function
    # with a `newValue` of 1
    box_encoded_initializer_function = encode_function_data()
    # box_encoded_initializer_function = encode_function_data(initializer=box.store, 1)
    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        # account.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {"from": account, "gas_limit": 1000000},
    )
    print(f"Proxy deployed to {proxy} ! You can now upgrade it to BoxV2!")
    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    tx=proxy_box.store(1,{'from':account})
    tx.wait(1)
    print(f"Here is the initial value in the Box: {proxy_box.retrieve()}")

