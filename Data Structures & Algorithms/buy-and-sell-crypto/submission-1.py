class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j=0
        n=0
        temp=0
        for i in range(len(prices)):
            j=i+1
            while j!=len(prices):
                if prices[j]>prices[i]:
                    temp=prices[j]-prices[i]
                    if n<temp:
                        n=temp
                j+=1
        return n
        
                
        