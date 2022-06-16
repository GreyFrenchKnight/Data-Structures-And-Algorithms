import numpy as np

class Solution:
    def findSubString(self, str):
        # Your code goes here
        chars = [char for char in str]
        uniques = np.unique(chars)

        # find the smallest window length that contains
        # all the characters of the given 
        # string at least one time
        smallestWindow = str
        for startingIndex in range(0, len(str) + 1 - len(uniques)):
            for endingIndex in range(startingIndex + len(uniques), len(str) + 1):
                window = chars[startingIndex:endingIndex]

                if len(window) >= len(smallestWindow):
                    # no need to keep looking with this startingIndex
                    break
                
                has_all = all([char in window for char in uniques])
                
                if has_all and len(window) < len(smallestWindow):
                    # all uniques contained in window and smallestWindow
                    smallestWindow = window
                    # no need to keep looking with this startingIndex
                    break
                    
        return len(smallestWindow)
    
input = "AABBBCBBAC"

print(Solution().findSubString(input))