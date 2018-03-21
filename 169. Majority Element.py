## O(nlogn)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1 
        return self.majority(nums,lo,hi)
        
    def majority(self,nums,lo,hi):
        if lo == hi:
            return nums[lo]            ##dc算法在思考的时候想一想最小的分割情况，最后剩一个返回
        
        mid = (lo+hi) / 2
        
        left = self.majority(nums,lo,mid)   ##dc算法在思考的时候想一想最小的分割情况，返回的最后一个左边
        right = self.majority(nums,mid+1,hi)  ##dc算法在思考的时候想一想最小的分割情况，返回的最后一个右边总共两个元素，为最小问题的情况
        
        if left == right:
            return left
        
        else:
            left_count = sum(1 for i in range(lo,hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo,hi+1) if nums[i] == right)
            
        return left if left_count > right_count else right      ##最终return给上一个子问题，然后再重复

    ##此题其实也可以用hash做，时间复杂度为O(n),空间复杂度为O(n)
