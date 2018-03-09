##python

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k%n                                    
        nums[:] = nums[n-k:]+nums[:n-k] 
 ##must use nums[:] instead of nums, in python, the slice just change the memory pointing,so the extra memory consuming just
 ##O(1)
