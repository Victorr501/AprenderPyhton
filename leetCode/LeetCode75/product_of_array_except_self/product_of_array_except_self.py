import math

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        longitud_nums = len(nums)
        numeros_devueltos = [0 for i in range(longitud_nums)]
        multiplicacion_izquierda_a_derecha = [0 for i in range(longitud_nums)]
        resultado_derecha_a_izquierda = 1
        resultado_izquierda_a_derecha = 1
        
        for i in range(longitud_nums):
            if i == 0:
                multiplicacion_izquierda_a_derecha[i] = resultado_izquierda_a_derecha
                continue
            resultado_izquierda_a_derecha *= nums[i-1]
            multiplicacion_izquierda_a_derecha[i] = resultado_izquierda_a_derecha
            
        for i in range(longitud_nums -1,-1, -1):
            if i == longitud_nums - 1:
                numeros_devueltos[i] = multiplicacion_izquierda_a_derecha[i]
                continue
            resultado_derecha_a_izquierda *= nums[i + 1]
            numeros_devueltos[i] = resultado_derecha_a_izquierda * multiplicacion_izquierda_a_derecha[i]
        
        
            
        return numeros_devueltos