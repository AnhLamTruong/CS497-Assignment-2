from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      maxCount = 0
      index = -1  # sentinels
      for i in range(len(nums)):
  
          count = 0
          for j in range(len(nums)):
  
              if(nums[i] == nums[j]):
                  count += 1
  
          # update maxCount if count of
          # current element is greater
          if(count > maxCount):
  
              maxCount = count
              index = i
  
      # if maxCount is greater than n/2
      # return the corresponding element
      if (maxCount > len(nums)//2):
          return nums[index]
  
      else:
          print("No Majority Element")
          
arr = [1, 1, 2, 1, 3, 5, 1]
n = len(arr)
# Function calling
print(Solution.majorityElement(Solution,arr))