class Solution(object):
    def reverseVowels(self,s):
        """
        :type s: str
        :rtype: str
        """
        
        vocales = "aeiouAEIOU"
        s_lista = list(s)
        izquierda = 0
        derecha = len(s_lista) - 1

        while izquierda < derecha:
            if s_lista[izquierda] not in vocales:
                izquierda += 1
            elif s_lista[derecha] not in vocales:
                derecha -= 1
            else:
                s_lista[izquierda], s_lista[derecha] = s_lista[derecha], s_lista[izquierda]
                izquierda += 1
                derecha -= 1
                
        return "".join(s_lista)
        
        