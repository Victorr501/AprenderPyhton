animales = ["perro", "gato", "loros", "cocodrilo"]

for animal in animales:
    print(animal)
    print(f"el animal es: {animal}")

print("hola mundo")

numeros = [1,2,3,4]

for animal, numero in zip(animales, numeros):
    print(numero)
    print(animal)
    
for num in range(5,10):
    print(num) 
    
for num, i in enumerate(numeros):
    print(num)
    print(i)
else:
    print("Se ha terminado el bucle")