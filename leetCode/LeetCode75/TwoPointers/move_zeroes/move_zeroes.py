class Solution(object):
    """
    Given an integer array nums, move all 0's to the end of it while maintaining the 
    relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.
    """
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        j = 0
        k = 0
        
        while i - j < len(nums):
            if nums[i - j] == 0:
                del nums[i - j]
                j += 1
            i += 1
               
        while k < j:
            nums.append(0)
            k += 1
    
        