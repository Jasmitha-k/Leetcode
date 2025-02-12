class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        c=-1
        x=nums.count(target)
        for i in range(len(nums)):
            if nums[i]==target:
                c=i
                break
        if c==-1:
            return [-1,-1]
        else:
            return [c,x+c-1]
        
        