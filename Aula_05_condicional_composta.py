# Condicionais
# condicionais são estruturas de controle de fluxo que permitem executar determinados 
# blocos de código com base na avaliação de uma expressão booleana. As principais 
# condicionais são:

# if: Executa um bloco de código se a condição for verdadeira.
# elif: Utilizado para verificar múltiplas condições alternativas após um if.
# else: Define um bloco de código a ser executado se nenhuma das condições 
# anteriores for verdadeira.

# Operador ternário if-else: Uma forma compacta de escrever uma condicional em uma única 
# linha.

nota1 = nota2 = 0
media = 0.0

# Receber a nota pelo usuário:
nota1 = (float(input('Insira a nota 1: ')))
nota2 = (float(input('Insira a nota 2: ')))

# Calcular a média aritimética
media = (nota1 + nota2) / 2

# Condicional
if media >= 6:
    print(f'Parabens! \nO aluno foi aprovado com a média: {media}')
elif media > 4:
    print(f'Ainda há chances! \nO aluno está de recuperação com média: {media}')
else:
    print(f'Que pena! \nO aluno foi reprovado com média: {media}')