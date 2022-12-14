# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input('Enter X (true or false): '))
y = bool(input('Enter Y (true or false): '))
z = bool(input('Enter Z (true or false): '))


result = bool((not (x or y or z)) == (not x and not y and not z))
print('')
print(f'Result of the statement is {result}')


# X	     Y	     Z	  ¬(X⋁Y⋁Z) ¬X⋀¬Y⋀¬Z result
# true	true	true	false	false	true
# true	true	false	false	false	true
# true	false	true	false	false	true
# true	false	false	false	false	true
# false	true	true	false	false	true
# false	true	false	false	false	true
# false	false	true	false	false	true
# false	false	false	true	true	true

