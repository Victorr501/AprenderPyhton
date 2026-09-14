class Solution(object):
    # def reverseWords(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """

    #     new_string = ""
    #     guardar_palabra = []
    #     ahi_palabra = False
    #     anterior_es_espacio = False
    #     palabra_que_es = 0
        
    #     for i in range(len(s) - 1, -1, -1):
    #         if s[i] != " ":
    #             if anterior_es_espacio:
    #                 if not guardar_palabra:
    #                     ahi_palabra = False
                        
    #             if ahi_palabra and palabra_que_es == 0 :
    #                 palabra = "".join(guardar_palabra)
    #                 new_string += palabra + " "
    #                 guardar_palabra.clear()
    #                 palabra_que_es += 1
    #             elif ahi_palabra and palabra_que_es != 0:
    #                 palabra = "".join(guardar_palabra)
    #                 new_string += palabra
    #                 guardar_palabra.clear()
    #                 palabra_que_es += 1
    #             guardar_palabra.insert(0, s[i])
    #         elif s[i] == " ":
    #             anterior_es_espacio = True
                
    #     return new_string

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        palabras = s.split() # Corta la frase por los epacio automátcamente y elimina los sobrantes
        return " ".join(reversed(palabras)) # Les da la buelta y " ".join() las vuelve a unir con un espacio
        
                
        
        
        
                