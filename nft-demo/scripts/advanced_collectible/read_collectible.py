from brownie import AdvancedCollectible
from scripts.helpful_scripts import fund_with_link, get_account


def main():
    # account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    ncoll = advanced_collectible.tokenCounter()
    print(f"Number of collectibles is {ncoll}")
    for col in range(ncoll):
        print(f"breed for tokenid= {col} is {advanced_collectible.tokenIdToBreed(col)}")
