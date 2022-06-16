# Data-Structures-And-Algorithms
Practice Data Structures And Algorithms

## Kadane's Algorithm
Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.
* Example 1:
```
Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
```
* Solution:
```
class Solution:
    # find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        maxarr = arr[0]
        su = arr[0]
        for i in range(1,N):
            su = max(arr[i], su + arr[i])
            maxarr = max(maxarr,su)
        return maxarr
```

## Minimum number of jumps
Given an array of N integers arr[] where each element represents the max number of steps that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.
* Example 1:
```
Input:
N = 11 
arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} 
Output: 3 
Explanation: 
First jump from 1st element to 2nd 
element with value 3. Now, from here 
we jump to 5th element with value 9, 
and from here we will jump to the last.
```
* Solution:
```
class Solution:
    def minJumps(self, arr, n):
        maxend = 0
        currend= 0
        jump = 0
        if n == 1:
           return 0
        for i in range(n):
            maxend = max(maxend, i+arr[i])
            if maxend >= n-1:
                return jump+1
            elif i == maxend:
                return -1
            elif i==currend:
                jump+=1
                currend=maxend
        return jump
```

## Missing number in array
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.
* Example 1:
```
Input:
N = 5
A[] = {1,2,3,5}
Output: 4
```
* Solution:
```
class Solution:
    def MissingNumber(self,array,n):
        # return first element of differences of sets
        return list(set([i for i in range(1, n+1)]) - set(array))[0]
```       

## Smallest distinct window
Given a string 's'. The task is to find the smallest window length that contains all the characters of the given string at least one time.
For eg. A = aabcbcdbca, then the result would be 4 as of the smallest window will be dbca.
* Example 1:
```
Input : "AABBBCBBAC"
Output : 3
Explanation : Sub-string -> "BAC"
```
* Example 2:
```
Input : "AABBBCBBAC"
Output : 3
Explanation : Sub-string -> "BAC"
```
* Solution:
```
import numpy as np

class Solution:
    def findSubString(self, str):
        v1,v2={},{}
        for a in str:
            if a not in v1:
                v1[a]=0
            v1[a]+=1
        i,j,res,n=0,0,1e5+1,len(str)
        while j<n:
            if str[j] not in v2:
                v2[str[j]]=0
            v2[str[j]]+=1
            if (len(v2)==len(v1)): # means all characters has been counted at least once
                while len(v2)==len(v1):
                    v2[str[i]]-=1
                    if v2[str[i]]==0:
                        del v2[str[i]]
                    i+=1
                res=min(res,2+j-i)
            j+=1
        return res
```

## Trapping Rain Water 
Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
* Example 1:
```
Input:
N = 6
arr[] = {3,0,0,2,0,4}
Output:
10
```
![TrappingRainWater](https://github.com/GreyFrenchKnight/Data-Structures-And-Algorithms/blob/f39ebfb10bc73b8dcd36dbef4f5a52e218312481/Images/Trapping%20Rain%20Water.png)

* Solution:
```
class Solution:
    def trappingWater(self, arr,n):
        totalResult = 0
        # find all combinations of leftHeightLimitation --- rightHeightLimitation
        # not only from indexes 0 to n - 1
        leftIndex = 0
        rightIndex = leftIndex + 1
        while rightIndex < n:
            leftHeightLimitation = arr[leftIndex]
            if leftHeightLimitation == max(arr[leftIndex: n]):
                # if left is max, look for next right max
                if leftIndex == n - 2:
                    # when reaching end of array
                    rightIndex = n - 1
                else:
                    rightIndex = leftIndex + 1 + arr[leftIndex + 1: n].index(max(arr[leftIndex + 1: n]))
                rightHeightLimitation = arr[rightIndex]
            else:    
                # if left is not max, look for next upper right
                rightHeightLimitation = arr[rightIndex]
                while leftHeightLimitation > rightHeightLimitation and rightIndex < n - 1:
                    rightIndex = rightIndex + 1
                    rightHeightLimitation = arr[rightIndex]

            localArr = arr[leftIndex:rightIndex + 1]
            localMinHeightLimitation = min(leftHeightLimitation, rightHeightLimitation)

            difference = list(map(lambda h: localMinHeightLimitation - h if h < localMinHeightLimitation else 0, localArr))
            result = sum(difference[1:-1])
            totalResult = totalResult + result
            
            leftIndex = rightIndex
            rightIndex = leftIndex + 1
        
        return totalResult
```

# Template

## Title
Desc
* Example 1:
```
example
```
* Solution:
```
code
```