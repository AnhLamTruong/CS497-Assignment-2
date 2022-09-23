from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n= len(arr)
        l=0
        r=1
        p=q=0
        while l<r:
          m=(l+r)/2
          maxF=0
          cnt=0
          j=1
          for i in range(n-1):
            while j<n and arr[i]/arr[j]>m:
              j+=1
            if j==n:
              break
            cnt+=n-j
            if((arr[i]/arr[j])>maxF):
              p=arr[i]
              q=arr[j]
              maxF=p/q
print(Solution.kthSmallestPrimeFraction(Solution,[1,2,3,5],k=3))
print(Solution.kthSmallestPrimeFraction(Solution,[1,7],k=1))