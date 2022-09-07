from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        #Initializr the current sum and minimum length
        curr_sum= 0
        min_len=len(nums)+1
        
        
        start=0
        end=0
        #Loops throught the array
        while(end<len(nums)):
          
          ##Keep adding the array numbers
          #while curr_sum<=to k
          while(curr_sum<=k and end<len(nums)):
            curr_sum+=nums[end]
            end+=1
          
          #If curr_sum >= than x
          while(curr_sum >= k and start<len(nums)):
            #Update the minimum length
            if (end-start<min_len):
              min_len=end-start
            
            #remove the starting elements
            curr_sum-=nums[start]
            start+=1
        if(min_len==len(nums)+1):
          return -1;
        return min_len

arr1 = [1, 4, 45, 6, 10, 19]
x = 51
print(Solution.shortestSubarray(Solution,arr1,x))
arr2 = [1]
x1 = 1
print(Solution.shortestSubarray(Solution,arr1,x))
arr3 = [1,2]
x2 = 4
print(Solution.shortestSubarray(Solution,arr1,x))
arr4 = [2,-1,2]
x3 = 3
print(Solution.shortestSubarray(Solution,arr1,x))