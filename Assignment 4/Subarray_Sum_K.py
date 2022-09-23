from typing import List
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n, ans = len(nums), float('inf')
        nums.append(0)
        s = deque([-1])
        for i in range(n):
            nums[i] += nums[i-1]
            while s and ans + s[0] <= i: 
              s.popleft()
            while s and nums[s[0]] + k <= nums[i]: 
              ans = i - s.popleft()
            while s and nums[s[-1]] >= nums[i]: 
              s.pop()
            s.append(i)
        return ans if ans != float('inf') else -1

nums1=[2,-1,2]
k1=3
nums2=[1,-1,2,4,5,6,3,31,13,4]
k2=17

print(Solution.shortestSubarray(Solution,nums1,k1))
print(Solution.shortestSubarray(Solution,nums2,k2))