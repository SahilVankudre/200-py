# 2. Best Time to Buy and Sell Stock (I/II/with cooldown/with fee)

def maxProfit_I(prices):

    if not prices:
        return 0

    n = 0
    min_price = prices[n]
    max_profit = 0

    for price in prices:
        # Update minimum price seen so far
        min_price = min(min_price, price)

        # Calculate profit if we sell today
        profit = price - min_price

        # Update maximum profit
        max_profit = max(max_profit, profit)

        n += 1

    return max_profit

def maxProfit_II(prices):

    max_pro = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_pro += prices[i] - prices[i-1]

    return max_pro

price = [1, 7, 2, 3, 6, 7, 6, 7]
print(maxProfit_II(price))