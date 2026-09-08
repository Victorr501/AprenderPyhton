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
        
        for i in range(min(largo_de_str1, largo_de_str2), 0, -1):
            if largo_de_str1 % i == 0 and largo_de_str2 % i == 0:
                if str1[:i] * (largo_de_str1 // i) == str1 and str2[:i] * (largo_de_str2 // i) == str2:
                    if str1[:i] == str2[:i]:
                        return str1[:i]
        return ""