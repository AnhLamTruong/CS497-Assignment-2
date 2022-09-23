from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # set up the right close to the elements x that specified the
        l, r= 0, len(arr)-k
        while l<r:
            m=(l+r)//2
            #distance between elements x to the left from the mid point
            #> distance between elements x to the right          
            if x-arr[m]>arr[m+k]-x:
                #move to left positions to the mid point 
                l=m+1
            else:
                #move to the right positions to the mid point
                r = m
        return arr[l:l+k]
    
#Driver code
arr1 =[1,2,3,4,5] 
k1=4 
x1=3

arr2=[1,2,3,4,5]
k2=4
x2=-1

arr3=[1,2,4,7,9]
k3=4
x3=8

print(Solution.findClosestElements(Solution, arr1, k1, x1))
print(Solution.findClosestElements(Solution, arr2, k2, x2))
print(Solution.findClosestElements(Solution, arr3, k3, x3))


