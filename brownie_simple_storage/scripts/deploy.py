from types import SimpleNamespace
from brownie import accounts, SimpleStorage, network, config


def deploy_simple_storage():
    # work with ganachicli accounts
    account = get_account()
    # print(account)
    # account = accounts.load("secondacc-brownie")
    # print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.getFavoriteNumber()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    stored_value = simple_storage.getFavoriteNumber()
    print(stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        # return accounts.add(config["wallets"]["from_key"])
        return accounts.load("secondacc-brownie")


def main():
    deploy_simple_storage()
