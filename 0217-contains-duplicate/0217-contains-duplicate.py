class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 

        dupli = set()
        for num in nums :
            if num in dupli:
                return True 
            dupli.add(num) 
        return False     