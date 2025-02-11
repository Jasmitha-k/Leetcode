class Solution(object):
    def getSneakyNumbers(self, nums):
        arr=[]
        for i in nums:
            if nums.count(i)==2 and i not in arr:
                arr.append(i)
        return arr
                
        