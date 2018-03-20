class Solution(object):
    def maxSubArrayhelp(self, nums,l,r):
        """
        :type nums: List[int]
        :rtype: int
        """
        if l > r:
            return -2147483647
        
        mid = (r+l)/2
        
        l_max_sum = 0
        suml = 0
        for i in range(mid-1,l-1,-1):
            suml += nums[i]
            l_max_sum = max(suml,l_max_sum)
        
        r_max_sum = 0
        sumr = 0
        for i in range(mid+1,r+1,1):
            sumr += nums[i]
            r_max_sum = max(sumr, r_max_sum)
        
        leftans = self.maxSubArrayhelp(nums,l,mid-1)
        rightans = self.maxSubArrayhelp(nums,mid+1,r)
        
        return max(l_max_sum+r_max_sum+nums[mid],max(leftans,rightans))
    
    def maxSubArray(self,nums):
        return self.maxSubArrayhelp(nums,0,len(nums)-1)
        
