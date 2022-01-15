from scripts.deploy_lottery import deploy_lottery
from scripts.utils import LOCAL_BLOCKCHAIN_ENVIRONMENTS, fund_with_link, get_account
from brownie import network, accounts, Lottery
from brownie.network.gas.strategies import GasNowStrategy
import pytest
from scripts.utils import LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy_lottery import deploy_lottery
import time

gas_strategy = GasNowStrategy("fast")


def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    # lottery = Lottery[-1]
    account = get_account()
    network.gas_limit("auto")
    # lottery.startLottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee() + 10000})
    lottery.enter({"from": account, "value": lottery.getEntranceFee() + 10000})
    fund_with_link(lottery)
    lottery.endLottery({"from": account})
    time.sleep(180)
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0
