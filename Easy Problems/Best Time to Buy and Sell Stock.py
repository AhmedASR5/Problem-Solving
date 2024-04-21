class Solution(object):
    def maxProfit(self, prices):

        left = 0
        right = 1
        profit = 0
        best_profit = 0

        while right < len(prices):

            if prices[left] < prices [right]:
                profit = prices[right] - prices [left] 
                best_profit = max(best_profit,profit)

            else:
                 left = right

            right +=1        
           
        return best_profit





