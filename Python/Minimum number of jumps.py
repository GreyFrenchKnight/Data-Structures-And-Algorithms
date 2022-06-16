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
 
N = 11
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, ]

print(Solution().minJumps(arr, N))