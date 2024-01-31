'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un
nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario
su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''

nombre_alumno = input('Ingresa tu nombre: ').upper() # nombre en mayusculas
sexo_alumno = input('Ingresao tu sexo (escribe la letra M si es masculino o F si es femenimo): ').upper() # seco en mayusculas

if((nombre_alumno[0] < "M" and sexo_alumno == 'F') or (nombre_alumno[0] > "N" and sexo_alumno == 'M')):
    print('Pertenece al grupo A')
else:
    print('Pretenece al grupo B')