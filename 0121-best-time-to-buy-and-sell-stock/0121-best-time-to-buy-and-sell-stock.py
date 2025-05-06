class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min=min(prices)
        min=prices[0]
        res=0
        for i in range(len(prices)):
            if min<prices[i]:
                res=max(res, prices[i]-min)
            else:
                min=prices[i]
        return res
        