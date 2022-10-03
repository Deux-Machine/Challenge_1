print('¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.')

#No se permiten el uso de listas, era innecesesario ya que no hay acceso a datos almacenados.
#Las listas normales o multidimensionales se usan para almacenar datos y ese es el caso del reto 2
ratings = []
percentages = [] #Importante cuidar la ortografia en las variables ya facilita la lectura del codigo
final_ratings = []
percentage = 0 #Variable no usada, codigo "basura"
sum_percentages = 0 #Importante cuidar la ortografia en las variables ya facilita la lectura del codigo
final_rating = 0

#para la suma solo era necesario un contador i
#Los print deben ser tal cual como se solictan en el documento.
student_name = input('Ingrese el nombre del estudiante: ')
subject = input('Ingrese el nombre de la materia: ')

#El ciclo while esta muy bien diseñado, aun cuando no es la estructura limpia que se propone es funcional y elimina lienas de codigo inecesarias.
#IMPORTANTE: usar comentarios (estos) para que la lectura del codigo sea mas facil, hace parte de Buenas Practicas de programacion.
while sum(percentages) < 100:
    student_rating = float(input('Ingrese la nota obtenida: '))
    percentage_rating = float(input('Ingrese el porcentaje de la nota: '))
    sum_percentages = sum(percentages) + percentage_rating

    #Cuando el porcentaje es superior a 100 se debera eliminar la ultima nota y porcentaje agregado para rectificar este dato.
    if sum_percentages > 100:
        print('El porcentaje evaluado de una materia no puede ser mayor a 100')
        print(percentage) #No retorna valores, intento 1
        percentage_rating = int(input('Ingrese el porcentaje de la nota: '))
        print(percentage) #No retorna valores, intento 2
    ratings.append(student_rating)
    percentages.append(percentage_rating)
    if sum(percentages) < 100:
        #No es la impresion correcta, se requiere un eval para determinar si es S o N
        print(f'Faltan notas por añadir, solo llevas el {sum(percentages)}%')

#No se requier iterar ya que no es necesario el almacenamiento, dentro del codigo no hay acceso a datos almacenados.
for x in range(0, len(ratings)):
    final_rating = ratings[x] * percentages[x]
    final_ratings.append(final_rating)

total_final_ratings = sum(final_ratings)/100

if total_final_ratings >= 3.5:
    #Muy funcional para el llamado en la impresion pero no es correcto a la estrctura del codigo, pero se acepta.
    approved = True
else:
    approved = False

#Fata capitalizar el nombre y la materia
print(f'El estudiante {student_name} cursó la materia {subject} y obtuvo {total_final_ratings} resultando en {"Aprobado" if approved else "Reprobado"}')
#Se revisan las listas y  se almacenan los datos de forma correcta. MUY BIEN
print(ratings)
print(percentages)
print(final_ratings)
