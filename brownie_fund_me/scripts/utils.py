from brownie import network, accounts


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        # return accounts.add(config["wallets"]["from_key"])
        return accounts.load("secondacc-brownie")
