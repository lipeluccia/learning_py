# Elas são como contêineres que contêm valores, como números, texto ou objetos, 
# e podem ser alteradas durante a execução do programa. As variáveis têm um nome 
# único que as identifica e um valor associado que pode ser modificado conforme 
# necessário.

nome_completo = 'Felipe Luccia de Lima' 
idade = 28
altura = 1.67
casado = True

#Função print (imprimir a tela)

print(nome_completo)

# Função type (tipo ou classe)
# podem ser str ou caracteres, int ou números inteiros, float ou valor real, 
# bool ou boleano (lógico), complex ou números complexos.

print(type(nome_completo))
print(type(idade))
print(type(altura))
print(type(casado))
print(type(1 + 2j))

# Função isinstance() usada para verificar se um objeto é uma instância de uma 
# classe específica. Ela retorna True se o objeto for uma instância da classe 
# fornecida e False caso contrário.

a = 10
b = 'sol'
c = True

print(isinstance(a,int))
print(isinstance(b,str))
print(isinstance(c,float))
print(isinstance(c, (bool,float)))

#Reatribuição de valores de variável. Anteriormente a = 10, caso seja dado um
# novo valor para a variável, ela terá o novo valor a partir da novo código

a = 20
print(a)

# Operações com variaveis

a = 10
b = 20
r = a * b

print(r)

# Função input() é usada para receber dados digitados pelo usuário durante a 
# execução do programa. Ela exibe uma mensagem opcional para solicitar a entrada 
# do usuário e retorna o que foi digitado como uma string.

nome = input('Digite seu nome e depois dê enter: ')
print(nome)

# Casting - refere-se à conversão explícita de um tipo de dado para outro. 
# Isso é feito usando funções como int(), float(), str(), entre outras, para 
# alterar o tipo de dado de uma variável conforme necessário.

num1 = int(input('Digite um número inteiro:\n'))
num2 = float(input('Digite aqui um número com casas decimais. \n (use ponto em vez de virgula)\n'))

print(num1, type(num1))
print(num2, type(num2))
