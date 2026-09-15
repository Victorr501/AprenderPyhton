class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        guardar_string = []
        palabra = []
        respuesta = ""

        for i in s:
            if i == " ":
                if not palabra:
                    pass
                if len(palabra) > 0:
                    guardar_string.append(palabra[:])
                    del palabra[:]
            elif i != " ":
                palabra.append(i)
        
        if s[-1] != " ":
            guardar_string.append(palabra[:])
            
        
        for i in range(len(guardar_string) -1, -1, -1):
            if i == 0:
                respuesta += "".join(guardar_string[i])
            if i > 0:
                respuesta += "".join(guardar_string[i]) + " "   
                
        return respuesta

    # def reverseWords(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
        
    #     palabras = s.split() # Corta la frase por los epacio automátcamente y elimina los sobrantes
    #     return " ".join(reversed(palabras)) # Les da la buelta y " ".join() las vuelve a unir con un espacio
        
                
        
        
        
                