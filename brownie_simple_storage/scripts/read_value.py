from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]#last deployment
    print(simple_storage.getFavoriteNumber())


def main():
    read_contract()
