import re
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      hashing=set()
      result=[]
      for i in range(0,len(nums1)):
        hashing.add(nums1[i])
      print("Intersection:")
      for i in range(0,len(nums2)):
        if nums2[i] in hashing:
          print (nums2[i])
          if nums2[i] not in result:
            result.append(nums2[i])
      return result
arr1 = [4,9,5]
arr2 = [9,4,9,8,4]
print(Solution.intersection(Solution,arr1,arr2))