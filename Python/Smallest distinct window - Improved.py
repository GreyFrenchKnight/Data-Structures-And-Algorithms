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
    
input = "AABBBCBBAC"

print(Solution().findSubString(input))