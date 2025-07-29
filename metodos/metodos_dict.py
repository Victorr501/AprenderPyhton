dicionario = {
    "nombre":'lucas',
    "apellido":'dalto',
    "subs": 10000
}

claves = dicionario.get("nombre")

#elimina todo del diccionario
#dicionario.clear()

#eliminando un elemento del dicionario

dicionario.pop("apellido", "subs")

#obteniendo un elemento dict_items iterable
dicionario_iterable = dicionario.items()

print(dicionario_iterable)

