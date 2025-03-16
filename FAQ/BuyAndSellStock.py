'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
'''

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]: # check if current price is higher than previous price
            profit += prices[i] - prices[i-1]
    return profit

# Test cases for the maximum profit problem
test_cases = [
    ([7,1,5,3,6,4], 7),  # Standard case with multiple transactions
    ([1,2,3,4,5], 4),  # Increasing prices, buy at the start, sell at the end
    ([7,6,4,3,1], 0),  # Decreasing prices, no profit possible
    ([1,2,3,1,2,3,1,2,3], 6),  # Multiple cycles of buying and selling
    ([2,1,4,5,2,9,7], 11),  # Mixed pattern of rise and fall
    ([3,3,3,3,3], 0),  # Constant price, no profit possible
    ([1,100,1,100,1], 198),  # Large fluctuations, buy low sell high repeatedly
    ([2,3,2,3,2,3,2], 3),  # Small fluctuations, minimal profit each step
    ([5,1,6,4,3,7,2,8], 15), 
    ([10], 0),  # Only one price, no transactions possible
    ([], 0),  # Empty list, no transactions possible
]

# Run assertions
for prices, expected in test_cases:
    result = maxProfit(prices)  # Replace with your function
    assert result == expected, f"Failed: Expected {expected}, got {result} for input {prices}"
    print(f"Test passed for input: {prices} -> Output: {result}")

print("All test cases passed successfully!")