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

In the Uniswap V2 protocol, when liquidity is initially added to a liquidity pool (i.e., through the mint function), a minimum liquidity amount is subtracted. This minimum liquidity serves several purposes, primarily related to ensuring the stability and efficiency of the liquidity pool. Here are some rationales behind this design:

1. **Preventing "Dust" Liquidity:** By subtracting a minimum liquidity amount, Uniswap V2 prevents extremely small liquidity additions that could be considered negligible or "dust." Such tiny liquidity additions can create inefficiencies in the system and may not provide meaningful liquidity depth to the pool. Setting a minimum liquidity threshold ensures that liquidity providers contribute a sufficient amount of liquidity to make a meaningful impact on the pool's efficiency.

2. **Maintaining Pool Stability:** Liquidity pools need to maintain a certain level of liquidity to ensure stable pricing and efficient trading. Subtracting a minimum liquidity amount helps maintain this stability by ensuring that liquidity providers add a reasonable amount of liquidity to the pool. Insufficient liquidity can lead to increased slippage and price volatility, negatively impacting the trading experience for users.

3. **Incentivizing Participation:** Setting a minimum liquidity requirement incentivizes liquidity providers to contribute a significant amount of liquidity to the pool. By requiring a minimum contribution, liquidity providers are encouraged to commit a meaningful stake, which aligns their incentives with the long-term health and stability of the liquidity pool. This helps attract more committed and serious liquidity providers to the platform.

4. **Reducing Gas Costs:** Handling extremely small liquidity additions can be inefficient in terms of gas costs, both for the liquidity provider and the network as a whole. By setting a minimum liquidity requirement, Uniswap V2 reduces the frequency of small transactions, which can help optimize gas usage and reduce congestion on the Ethereum network.

Overall, the rationale behind subtracting a minimum liquidity amount upon initial minting in Uniswap V2 is to promote stability, efficiency, and meaningful participation in liquidity provision, while also optimizing gas usage and network resources.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

The rationale behind subtracting a minimum liquidity amount upon initial minting in the mint function of the UniswapV2Pair contract is to address the first minter problem and defend against **the inflation attack**. This attack vector involves malicious actors attempting to manipulate the price by owning the entire supply of LP (Liquidity Provider) tokens.

To prevent this, Uniswap V2 employs a defense mechanism by burning a portion of the initial liquidity tokens (MINIMUM_LIQUIDITY tokens) during the minting process. By doing so, it ensures that no single entity can monopolize the LP token supply, thereby safeguarding against potential price manipulation.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

In Uniswap V2, the `mint` function in the `UniswapV2Pair` contract is responsible for adding liquidity to a liquidity pool. When depositing tokens into the pool, whether it's not the first time (i.e., adding more liquidity) or initially, the liquidity is obtained using a specific formula. This formula ensures that the liquidity provider receives a proportionate share of the pool's assets in exchange for the tokens deposited.

The intention behind using a specific formula, known as the constant product formula or the "x * y = k" invariant formula, is to maintain the balance of the assets in the liquidity pool. In other words, it ensures that the product of the quantities of the two assets in the pool remains constant before and after the addition of liquidity. This constant product formula is fundamental to how Uniswap V2 operates.

Here's a brief explanation of the intention behind using the constant product formula:

1. **Maintaining Asset Balance:** By using the constant product formula, Uniswap V2 ensures that the balance of assets in the liquidity pool remains stable. This is achieved by adjusting the quantities of the two assets whenever liquidity is added or removed from the pool.

2. **Determining Price:** The constant product formula also serves to determine the price of the assets relative to each other within the liquidity pool. Traders can rely on this price to execute trades with minimal slippage, as it reflects the current supply and demand dynamics of the assets.

3. **Fair Distribution of Liquidity Provider Shares:** When liquidity is added to the pool, the liquidity provider receives a proportionate share of the pool's assets in exchange for the tokens deposited. This ensures a fair distribution of ownership and incentives among liquidity providers.

4. **Efficient Trading:** The constant product formula enables efficient and automated market making on Uniswap V2. It allows traders to execute trades directly against the liquidity pool, without relying on order books or centralized intermediaries.

Overall, the intention behind using a specific formula, such as the constant product formula, in the `mint` function of the UniswapV2Pair contract is to maintain the balance of assets in the liquidity pool, determine asset prices, ensure fair distribution of liquidity provider shares, and facilitate efficient trading on the platform.

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
