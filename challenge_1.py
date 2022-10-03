print('¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.')

ratings = []
percentages = []
final_ratings = []
percentage = 0
sum_percentages = 0
final_rating = 0
student_name = input('Ingrese el nombre del estudiante: ')
subject = input('Ingrese el nombre de la materia: ')
while sum(percentages) < 100:
    student_rating = float(input('Ingrese la nota obtenida: '))
    percentage_rating = float(input('Ingrese el porcentaje de la nota: '))
    sum_percentages = sum(percentages) + percentage_rating
    if sum_percentages > 100:
        print('El porcentaje evaluado de una materia no puede ser mayor a 100')
        percentage_rating = int(input('Ingrese el porcentaje de la nota: '))

    ratings.append(student_rating)
    percentages.append(percentage_rating)
    if sum(percentages) < 100:
        print(f'Faltan notas por añadir, solo llevas el {sum(percentages)}%')

for x in range(0, len(ratings)):
    final_rating = ratings[x] * percentages[x]
    final_ratings.append(final_rating)

total_final_ratings = sum(final_ratings)/100

if total_final_ratings >= 3.5:
    approved = True
else:
    approved = False

print(f'El estudiante {student_name} cursó la materia {subject} y obtuvo {total_final_ratings} resultando en {"Aprobado" if approved else "Reprobado"}')
