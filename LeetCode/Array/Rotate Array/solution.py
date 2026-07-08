from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums)) == 1 or len(nums)==k:
            return
        
        while k>len(nums):
            k=k-len(nums)
            
        newIndex = -1
        aList = []
        
        for i in range(len(nums)):
            aList.append(-1)
            
        for i in range(len(nums)):
            newIndex = k+i
            if newIndex > len(nums)-1:
                newIndex-= len(nums)
            aList[newIndex] = nums[i]
                
        nums[:] = aList[:]