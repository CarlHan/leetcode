##此题可以用多种排序的方法先把数组order好，然后查询所在位置的元素
##时间复杂度主要集中在排序上，O(nlgon)

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        return nums[len(nums)-k]
        
 ##python内建的排序函数，根据实际情况会采用最有效的排序方法，可以借此复习几种不同的排序方式以及时间复杂度，此处是快排，O(nlogn)
 
 还可以用堆排序的方法，首先把nums数组转为堆数据结构，然后extract，时间复杂度也是O(nlogn)
 
 class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        
        for num in nums:                              ##O(nlogn),注意这里内建的堆是按root为最小来建的树
            heapq.heappush(heap,num)
        
        for _ in range(len(nums)-k):                  ##O((n-k)logn)
            heapq.heappop(heap)
        
        return heapq.heappop(heap)
        
        ##O(nlogn)
