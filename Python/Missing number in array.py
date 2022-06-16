class Solution:
    def MissingNumber(self,array,n):
        # code here
        # return first element of differences of sets
        return list(set([i for i in range(1, n+1)]) - set(array))[0]
        
N = 5
arr = [1,2,3,5]

print(Solution().MissingNumber(arr, N))