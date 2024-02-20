# Operadores de comparação:
# Eles comparam dois valores e retornam True se a comparação for verdadeira e 
# False caso contrário.
# == Igual a
# != Diferente de
# > Maior que
# >= Maior ou igual a
# < Menor que
# <= Menor ou igual a

x = y = z = v = False
n1 = n2 = 0

print('Digite um número: ')
n1 = int(input())
n2 = int(input('Digite outro número: \n'))

x = n1 == n2
print(f'{n1} e {n2} são iguais? {x} \n')

z = n1 > n2
print(str(n1) + ' é maior que' + str(n2) + '? ' + str(z) + '\n')

y = n1 != n2
print(n1, 'é diferente de', n2, '?', y )

v = n1 < n2
print(f'{n1} é menor que {n2}? {v} \n')
