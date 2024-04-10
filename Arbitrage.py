liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}
from itertools import permutations

fee = 0.003
tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]

def getAmount(amountIn, reserveIn, reserveOut):
    amountInWithFee = (1-fee)*amountIn
    numerator = amountInWithFee*reserveOut
    denominator = reserveIn + amountInWithFee
    return numerator/denominator 

def sort_token(token0, token1):
    if token0 < token1:
        return (token0, token1), 1
    return (token1, token0), 0


def find_path_greedy(startToken, amount):
    remaing_token = tokens.copy()
    path = [startToken]

    balance = amount
    token_from = startToken
    while len(remaing_token) != 0:
        next_token = None
        next_best_amount = 0
        for token in remaing_token:
            if token == startToken and len(path) <= 3:
                continue
            token_address, token_indices = sort_token(token_from, token)
            liquidity_with_address = liquidity[token_address]
            tmp_amountOut = getAmount(balance, liquidity_with_address[1-token_indices], liquidity_with_address[token_indices])
            if tmp_amountOut > next_best_amount:
                next_token, next_best_amount  = token, tmp_amountOut
                
        # Update the variables
        remaing_token.remove(next_token)
        path.append(next_token)
        token_from = next_token
        balance = next_best_amount
        if next_token == startToken:
            break
    print("{}, tokenB balance={:.6f}".format("->".join(path), balance))
    return path ,balance


def cal_path_amountOut(path, amountIn):
    balance = amountIn
    for token_idx in range(1, len(path)):
        token_from, token_to = path[token_idx-1], path[token_idx]
        token_address, token_indices = sort_token(token_from, token_to)
        liquidity_with_address = liquidity[token_address]
        balance = getAmount(balance, liquidity_with_address[1-token_indices], liquidity_with_address[token_indices])
    return balance

def find_all_path(start_token):
    all_path = []
    remain_tokens =  tokens.copy()
    remain_tokens.remove(start_token)
    for k in range(1, 5):
        for path in list(permutations(remain_tokens, k)):
            path_list = list(path)
            path_list.append(start_token)
            path_list.insert(0, start_token)
            all_path.append(path_list)

    return all_path

#Exhaustive method
def find_path_exhaustive(start_token, amount):
    all_path = find_all_path(start_token)
    best_balance = 0
    best_path = None
    for path in all_path:
        balance = cal_path_amountOut(path, amount )
        if balance > best_balance:
            best_balance, best_path = balance, path

    print("{}, tokenB balance={:.6f}".format("->".join(best_path), best_balance))



if __name__ == "__main__":
    start_token = "tokenB"
    # Greedy mehtod
    # path , balance =find_path_greedy("tokenB", 5)
    # exhaustive method
    find_path_exhaustive(start_token, 5)
