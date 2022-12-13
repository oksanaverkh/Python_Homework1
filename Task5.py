# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Enter coordinates for point A:')
x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
print('')
print('Enter coordinates for point B:')
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
print('')

distance = round(((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))**0.5, 2)

print(f'Distance between points A ({x1},{y1}) and B ({x2},{y2}) = {distance}')