class Solution(object):
    """
    Given an array of characters chars, compress it using the following algorithm:

    Begin with an empty string s. For each group of consecutive repeating characters in chars:

    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.
    The compressed string s should not be returned separately, but instead, be stored in the input 
    character array chars. Note that group lengths that are 10 or longer will be split into 
    multiple characters in chars.

    After you are done modifying the input array, return the new length of the array.

    You must write an algorithm that uses only constant extra space.

    Note: The characters in the array beyond the returned length do not matter and should be ignored.
    """
    
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        i = 0
        write = 0
        
        while i < len(chars):
            letra_actual = chars[i]
            contador = 0
            
            while i < len(chars) and chars[i] == letra_actual:
                contador += 1
                i += 1
            
            chars[write] = letra_actual
            write += 1

            if contador > 1:
                for digito in str(contador):
                    chars[write] = digito
                    write += 1
            
        return write
        
            
                    
            