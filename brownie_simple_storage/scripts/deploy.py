from brownie import accounts


def deploy_simple_storage():
    # work with ganachicli accounts
    # account = accounts[0]
    # print(account)
    account = accounts.load("secondacc-brownie")
    print(account)


def main():
    deploy_simple_storage()
