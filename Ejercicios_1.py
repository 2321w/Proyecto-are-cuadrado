#Diferencia en porcentajes entre curso actual y el más rapido, el más lento de otros cursos

#Diferencia en porcentajes entre curso actual y el más rapido, el más lento de otros cursos

Curso_actual=1.5
Promedio=4
Mínimo=2.5
Máximo=7
#Duración de videos sin editar
duración_sin_editar_video_actual=3.5
duración_sin_editar_videos_promedio=5

porcentaje_de_material_inservible_reducido_curso_actual=100-Curso_actual*1000//duración_sin_editar_video_actual/10
porcentaje_de_material_inservible_reducido_cursos_promedio=100-Promedio/duración_sin_editar_videos_promedio*100

#Diferencia en porcentajes entre curso actual y el más rapido, el más lento de otros cursos
diferencia_con_min=100-Curso_actual/Mínimo*100
diferencia_con_max=100-Curso_actual*1000//Máximo/10
diferencia_con_el_promedio=100-Curso_actual/Promedio*100


print(f"El curso de dura un {diferencia_con_min} % menos que el más rapido")
print(f"El curso actual dura un {diferencia_con_max} % menos que el maximo de videos")
print(f"El curso actual dura un {diferencia_con_el_promedio}% menos que el promedio de videos")
print("-----------------------------------------------------------------------------------------------")

print(f"El procentaje de reducción de video es {porcentaje_de_material_inservible_reducido_curso_actual}% en el curso actual")
print(f"El porcentaje de reducción de videos en el promedio es {porcentaje_de_material_inservible_reducido_cursos_promedio} ")
print("------------------------------------------------------------------------------------------------")
#Cuanto equivale 10 horas del curso actual a cuanto equivale en horas de otro curso
print(f"Ver 10 horas de este curso equivalen a ver {Promedio*1000//Curso_actual/100}% horas de otros cursos")
