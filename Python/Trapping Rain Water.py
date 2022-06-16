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
        
N = 3
arr = [6,9,9]
# output 0

N = 9
arr = [7,4,0,9,3,5,0,0,6]
# output 26

N = 9
arr = [5,1,2,3,7,1,2,0,8]
# output 27

N = 7 
arr = [8,8,2,4,5,5,1]
# output 4

print(Solution().MissingNumber(arr, N))