class Solution:
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        maxarr = arr[0]
        su = arr[0]
        for i in range(1,N):
            su = max(arr[i], su + arr[i])
            maxarr = max(maxarr,su)
        return maxarr
        
N = 5
arr = [1,2,3,-2,5]

print(Solution().maxSubArraySum(arr, N))