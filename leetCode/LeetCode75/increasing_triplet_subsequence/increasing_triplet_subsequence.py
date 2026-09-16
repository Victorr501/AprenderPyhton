class Solution(object):
    """
    Given an integer array nums, return true if there exists a triple of 
    indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
    If no such indices exists, return false.
    """
    
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # l_c_n = [0 for i in range(3)]
        
        
        # for i in range(len(nums)):
        #     if l_c_n[0] == 0 or ((l_c_n[0] < nums[i] and l_c_n[1] > nums[i])and l_c_n[1] == 0) :
        #         l_c_n[0] = i
        #         continue
        #     if l_c_n[1] == 0 or ((l_c_n[1] < nums[i] and l_c_n[2] > nums[i] )and l_c_n[2] == 0):
        #         l_c_n[1] = i
        #         continue
        #     if l_c_n[2] == 0 or l_c_n[2] < nums[i]:
        #         l_c_n[2] = i
                            
            
        # return l_c_n
        
        # if nums[l_c_n[0]] < nums[l_c_n[1]] < nums[l_c_n[2]]:
        #      return True
        # else:
        #      return False
        
        # Iniciamos a infintio para que pueda meter cualquier numero
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
            
        return False