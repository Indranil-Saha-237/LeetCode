#0121. Best Time to Buy and Sell Stock
#Runtime=21ms
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minVal=float('inf')
        profit=0

        for i in prices:
            if i <minVal:
                minVal=i
            elif i-minVal>profit:
                profit= i-minVal
        return profit



        
        