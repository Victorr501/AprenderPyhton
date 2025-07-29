#Pedirle al usaurio que diga cualquier texto reay y:
# - calcular cuanto tardaía en decir esa frase
# - ¿Cuantas palabras dijo?

frase = input("Decime una frase y te calculo uanto tardarias si tuvieras que decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

print(f"Dijiste {cantidad_de_palabras} palabras, y tardaías {cantidad_de_palabras / 2 } segundos en decirlo")

#Si se tarda más de 1 minutos:
# - decirle: "para flaco tampoco te pedí un textamento"

if cantidad_de_palabras > 120:
    print("Pará flaco tampoco te pedi un testamento")

#Dalto habla un 30% más rapido: 
#¿Cuanto tardaría él en decirlo?
print(f"Dalto lo diria en {cantidad_de_palabras / 2 * 0.7} segundos")