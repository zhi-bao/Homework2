# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
```
tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.129889
```

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution


Slippage in Automated Market Makers (AMMs) refers to the difference between the expected price of a trade and the actual price at which the trade is executed. This difference occurs because AMMs, like Uniswap V2, rely on constant product formulas to determine token prices based on supply and demand within liquidity pools. When a trade is executed, especially for a large amount, it can significantly impact the token price due to the limited liquidity available at that specific price point.

Uniswap V2 address this issue by setting **slippage tolerance**. 

In Uniswap V2's Router 02 contract, when using functions like swapTokensForExactTokens, the slippage tolerance is handled programmatically through the amountInMax parameter. This parameter specifies the maximum amount of input tokens (token A) that you are willing to trade to get the desired output tokens (token B).

The slippage tolerance is indirectly controlled by setting the appropriate amountInMax value. This value determines how much slippage (price impact) you are willing to accept during the trade. The higher the amountInMax, the more slippage you might encounter, but it also increases the likelihood of your trade getting executed successfully, especially in volatile markets.

Here's a brief explanation of the parameters in the swapTokensForExactTokens function:

amountOut: The exact amount of output tokens (token B) you want to receive in the trade.
amountInMax: The maximum amount of input tokens (token A) you are willing to provide for the trade, considering slippage.
path: An array specifying the token swap path, e.g., [tokenA, tokenB].
to: The address that will receive the output tokens.
deadline: The timestamp by which the transaction must be executed, after which it expires.
By adjusting the amountInMax parameter, you can control the slippage tolerance programmatically when executing a swap transaction using the Uniswap V2 Router 02 contract.


## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

The rationale behind subtracting a minimum liquidity amount upon initial minting in the mint function of the UniswapV2Pair contract is to address the first minter problem and defend against **the inflation attack**. This attack vector involves malicious actors attempting to manipulate the price by owning the entire supply of LP (Liquidity Provider) tokens.

To prevent this, Uniswap V2 employs a defense mechanism by burning a portion of the initial liquidity tokens (MINIMUM_LIQUIDITY tokens) during the minting process. By doing so, it ensures that no single entity can monopolize the LP token supply, thereby safeguarding against potential price manipulation.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

The intention behind the specific formula used in the minting function of the UniswapV2Pair contract, as outlined in the Uniswap whitepaper, is to ensure that the value of a liquidity pool share remains relatively stable and independent of the initial deposit ratio. This formula also prevents situations where the value of a liquidity pool share could grow excessively over time, making it unfeasible for small liquidity providers to participate.


## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

A sandwich attack is a type of front-running attack commonly seen in decentralized finance (DeFi) platforms, particularly in automated market maker (AMM) protocols like Uniswap. In a sandwich attack, a malicious actor exploits the predictability of blockchain transactions to manipulate the price of an asset during a swap.

Here's how a sandwich attack typically unfolds:
1. **Observation**: The attacker monitors the mempool (the pool of unconfirmed transactions) for pending transactions involving a specific token pair.

2. **Front-Running**: When they identify a large buy or sell order about to be executed, the attacker quickly submits their own transactions to the mempool.

3. **Sandwich**: The attacker's transactions are strategically placed before and after the target transaction. The initial transaction is typically designed to influence the price in a favorable direction for the attacker, while the subsequent transaction is used to capitalize on the changed price.

4. **Profit**: By executing trades at manipulated prices, the attacker can profit from the price movement caused by their own transactions, often at the expense of the original trader.

Impact:
- **Slippage**: The presence of sandwich attacks can lead to increased slippage for traders, meaning they may receive less of their desired token or pay more than expected due to the manipulated price.
- **Finaical Losses**: Initiating swaps may suffer financial losses if their transactions are sandwiched between those of the attacker, especially if they are unaware of the manipulation.
