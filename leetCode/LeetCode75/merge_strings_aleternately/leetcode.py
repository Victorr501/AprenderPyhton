"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
"""
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        numero_caracteres_word1 = len(word1)
        numero_caracteres_word2 = len(word2)
        
        is_word1_longer = len(word1) > len(word2)
        
        newWord = ""
        
        if is_word1_longer:
            for i in range(numero_caracteres_word1):
                newWord += word1[i]
                if numero_caracteres_word2 > i:
                    newWord += word2[i]
        else:
            for i in range(numero_caracteres_word2):
                if numero_caracteres_word1 > i:
                    newWord += word1[i]
                newWord += word2[i]
                    
        return newWord
    
