### Top K Frequent Elements

I use the map to solve this problem. Firstly, I put the number in the from a list to number frequency.
Something like this:
|1:4|
|2:3|
|3:3|
|4:2|
Then I put values in the number frequency to the frequency list.
|4:[1]|
|3:[2],[3]|
|2:[4]|
Therefore, I just return the hightest keys in the frequency list.
The time complexity of this method is O(m+n)

### Find K Closest Elements

I used Binary Search to find the closest element in the array given, and to find the crossover point.Once we find index of crossover point, we can print k closest elements in O(k) time. Therefore,
Our Solution is to find k elements in O(Logn + k) time.

### Shortest Subarray with Sum at least K

I used a deque to store possible indices with an increasing sum.
Time Complexity : O(N), since we are doing at most two operation for each element in array, adding to deque and removing from deque, and we haven N elements. So at most 2\*N operations, so O(N).
