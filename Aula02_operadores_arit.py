# Os operadores aritméticos em Python são símbolos matemáticos que são usados 
# para realizar operações como adição (+), subtração (-), multiplicação (*), 
# divisão (/), divisão inteira (//), módulo (%) e exponenciação (**). Eles são 
# usados para manipular números em expressões matemáticas dentro de programas Python.

# A ordem de precedência dos operadores em Python segue a seguinte hierarquia, da 
# mais alta para a mais baixa:

# Parênteses ()
# Exponenciação **
# Multiplicação *, Divisão /, Divisão inteira //, Módulo %
# Adição +, Subtração -

a = b = c = 0

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = a * b
print('O resultado do cáculo é:', c)

x = 2
y = 3
z = 4

adicao = x + y
print(f'{x} + {y} é : {adicao}')
subtracao = z - x
print(f'{z} - {x} é: {subtracao}')
multiplicacao = x * z
print(f'{x} x {z} é: {multiplicacao}')
divisao = z / x
print(f'{z} / {x} é {int(divisao)}')
expo = z ** y
print(f'{z} elevado a {y} é: {expo}')

