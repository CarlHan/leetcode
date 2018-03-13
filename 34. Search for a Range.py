class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        elif len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        else:
            count = []
            right = len(nums)-1
            left = 0
            result = self.binary_search(left,right,nums,target)
            if result == -1:
                return [-1,-1]
            ## 下面从当前index向两边寻找边界点，lc，rc,似乎这个搜索好像事件复杂度也是线性的………………O(n)
            else:
                lc = rc = result
                while lc >= 0 and nums[lc] == target:
                    lc -= 1 
                lc = lc + 1 
                while rc <= (len(nums)-1) and nums[rc] == target:
                    rc += 1
                rc = rc -1
            return [lc,rc]
                    
            
    
    def binary_search(self,left,right,nums,target):   ##O(logn)
        
        if left > right:
            return -1
        
        mid = (left + (right-left)/2)
        
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            return self.binary_search(mid+1,right,nums,target)
        if target < nums[mid]:
            return self.binary_search(left,mid-1,nums,target)
