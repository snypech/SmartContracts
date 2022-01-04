from types import SimpleNamespace
from brownie import accounts, SimpleStorage


def deploy_simple_storage():
    # work with ganachicli accounts
    account = accounts[0]
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


def main():
    deploy_simple_storage()
