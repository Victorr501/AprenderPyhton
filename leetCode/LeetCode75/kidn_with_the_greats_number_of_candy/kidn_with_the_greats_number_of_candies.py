"""
There are n kids with candies. You are given an integer array candies, where each candies[i] 
represents the number of candies the ith kid has, and an integer extraCandies, 
denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, 
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        numero_macxio = max(candies)
        numero_largo_array = len(candies)
        resultado = []
        
        for i in range(numero_largo_array):
            numero_anterior = candies[i]
            candies[i] = numero_anterior + extraCandies
        
        for i in range(numero_largo_array):
            if candies[i] >= numero_macxio:
                resultado.append(True)
            else:
                resultado.append(False)
                
        return resultado
        