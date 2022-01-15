from brownie import OurToken, accounts
from scripts.utils import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def deploy():
    account = get_account()
    token = OurToken.deploy(initial_supply, {"from": account})
    print(token.name())


def main():
    deploy()
