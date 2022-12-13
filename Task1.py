# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

weekday = int(input(f'Enter a weekday number: '))

if weekday >= 1 and weekday <= 7:
    if weekday == 6 or weekday == 7:
        print('YES, weekday is a weekend')
    else:
         print('NO, weekday is NOT a weekend')
else: 
    print('ERROR!')