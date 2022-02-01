from brownie import AdvancedCollectible, network, accounts
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)
import pytest
import time
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible_integration():

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for integration testing")
    advanced_collectilbe, ctx = deploy_and_create()
    time.sleep(180)
    assert advanced_collectilbe.tokenCounter() == 1
