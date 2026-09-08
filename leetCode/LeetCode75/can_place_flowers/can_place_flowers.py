"""
You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 
means not empty, and an integer n, return true if n new flowers can be
planted in the flowerbed without violating the no-adjacent-flowers 
rule and false otherwise.
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        #Hay un regla que no te deja plantar las flores si hay un huego entre las 2
        
        numero_longitud_lista = len(flowerbed)
        guecos_disponibles = 0
        
        for i in range(numero_longitud_lista):
            if flowerbed[i] == 0 and not i == 0 and not i == numero_longitud_lista - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    guecos_disponibles += 1
                    flowerbed[i] = 1
            elif numero_longitud_lista == 1 and flowerbed[i] == 0:
                return 1 >= n 
            elif flowerbed[i] == 0 and i == 0:
                if numero_longitud_lista > 1:
                    if flowerbed[i + 1] == 0:
                        guecos_disponibles += 1
                        flowerbed[i] = 1
            elif flowerbed[i] == 0 and i == numero_longitud_lista - 1:
                if flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    guecos_disponibles += 1
            
                    
        return guecos_disponibles >= n
        