1. Swap eth for weth

Use weth interface to get token contract

2. Deposit weth into aave
3. Borrow some asset with ETH collateral
    1. Sell that borrowed asset (Short selling)
4. Repay everything back


#Testing:

Integration test: kovan

Unit Test: Mainnet fork (Use mokcs when working with oracles)

get_weth: get contract from interface