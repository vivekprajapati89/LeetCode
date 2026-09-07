class Solution:
    def twoSum(self,n,target):
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if n[i] + n[j] == target:
                    return [i,j]


            
            
        