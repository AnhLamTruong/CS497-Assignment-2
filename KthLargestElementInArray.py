class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort();
        return nums[len(nums)-k]
      
#Driver Code
arr=[3,2,1,5,6,4]
k=2

print(Solution.findKthLargest(Solution,arr,k))