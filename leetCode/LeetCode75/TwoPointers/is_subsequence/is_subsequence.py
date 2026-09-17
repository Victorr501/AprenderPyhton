class Solution(object):
    """
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters 
    ithout disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
    """
    
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        puntero_s = 0
        puntero_t = 0
        
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        
        while puntero_t < len(t) and puntero_s < len(s):
            if s[puntero_s] == t[puntero_t] and puntero_s < len(s):
                puntero_s += 1
            puntero_t += 1
            
            
        return puntero_s == len(s)
        # if puntero_s == len(s):
        #     return True
        # return False
