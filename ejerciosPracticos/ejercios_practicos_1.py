#Cuanta diferencia en porecentaje entre el curso actual y:
# - el más rapidod de otros curos
# - el más lento de otros curos
# - el promdeio de los cursos

otros_crursos_min = 2.5
otros_crursos_max = 7
otros_crursos_promedio = 4

dalto_curso = 1.5

#Diferencias de duración

diferencia_con_min = 100 - dalto_curso / otros_crursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_crursos_max / 100
diferencia_con_promedio = 100 - dalto_curso / otros_crursos_promedio * 100

print(f"El curos de dalto dura un {diferencia_con_min}% menos que el más rapido")
print(f"El curso de dalto dura un {diferencia_con_max}% menos que el más lento")
print(f"El curso de dalto duro un {diferencia_con_promedio}% menos que el promedio")

print("-------------------------")


#Procesntaje de material inservible qe se reduce en:
# - el prmedio de los cursos
# - el curso actual (este curos)
crudo_promedio = 5
crudo_dalto = 3.5

tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto /10
tiempo_vacio_promedio = 100 - otros_crursos_promedio * 1000 // crudo_promedio / 10

print(f"El crudo que elimina dalto es de {tiempo_vacio_dalto}%")
print(f"El crudo que eliminan el promedio es de {tiempo_vacio_promedio}%")

print("-------------------------")

#ver 10 horas de este curso a cuantas de otros cursos equivale? ¿y al reves?

print(f"Ver 10 horas de este curso equivale a ver {otros_crursos_promedio * 1000 // dalto_curso / 100} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivale a ver {dalto_curso * 1000 // otros_crursos_promedio / 100} horas de este curso")