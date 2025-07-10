#Diferencia en porcentajes entre curso actual y el más rapido, el más lento de otros cursos

Curso_actual=1.5
Promedio=4
Mínimo=2.5
Máximo=7

diferencia_con_min=100-Curso_actual/Mínimo*100
diferencia_con_max=100-Curso_actual*1000//Máximo/10
diferencia_con_el_promedio=100-Curso_actual/Promedio*100


print(f"El curso de dura un {diferencia_con_min} % menos que el más rapido")
print(f"El curso actual dura un {diferencia_con_max} % menos que el maximo de videos")
print(f"El curso actual dura un {diferencia_con_el_promedio}% menos que el promedio de videos")
