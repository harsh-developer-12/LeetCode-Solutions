class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = 0 
        sum = 0 
        mx = float('-inf')
        for r in range (len(nums)):
            sum+=nums[r]      # sum = first val --> second val --> ...
            if r - l + 1 == k:
                if sum >mx :
                    mx =sum 
                sum -= nums[l] 
                l += 1 
        return (mx /k)            