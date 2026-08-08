class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        if len(nums2) > len(nums1):
            nums2 , nums1 = nums1 , nums2
        for i in nums1:
            if i in nums2: 
               intersection.append(i)
               nums2.remove(i) 
        return intersection



       