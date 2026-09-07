"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        largo_de_str1 = len(str1)
        largo_de_str2 = len(str2)
        
        a_de_volver = ""
        
        multiplicador = largo_de_str1 // largo_de_str2
        
        if not largo_de_str2 * multiplicador == largo_de_str1:
            return ""
        
        for i in range(multiplicador):
            if largo_de_str2 > i:
                is_igual = str1[i] == str2[i]
                if is_igual:
                    a_de_volver += str1[i]
        
                     
                
        return a_de_volver