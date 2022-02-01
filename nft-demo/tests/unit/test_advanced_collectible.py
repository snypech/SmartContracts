from brownie import AdvancedCollectible, network, accounts
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)
import pytest
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible():

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    advanced_collectilbe, ctx = deploy_and_create()
    requestId = ctx.events["requestedCollectible"]["requestId"]
    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, advanced_collectilbe.address, {"from": get_account()}
    )
    assert advanced_collectilbe.tokenCounter() == 1
    assert advanced_collectilbe.tokenIdToBreed(0) == random_number % 3
