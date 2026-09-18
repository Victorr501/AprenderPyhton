class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        
        izquierda = 0
        derecha = len(nums) -1
        conjuntos = 0
        
        while izquierda < derecha :
            suma = nums[izquierda] + nums[derecha]
            if suma == k:
                izquierda += 1
                derecha -= 1
                conjuntos += 1
            elif suma < k:
                izquierda += 1
            elif suma > k:
                derecha -= 1
        
   
        
        return conjuntos
            