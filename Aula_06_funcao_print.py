# A função print() em Python é usada para exibir mensagens ou valores na saída padrão, 
# geralmente o console. Ela aceita múltiplos argumentos separados por vírgula e os 
# imprime em sequência, convertendo-os para strings, se necessário. É uma ferramenta 
# essencial para depuração, feedback do usuário e comunicação de resultados durante a 
# execução de um programa.


print('Olá pessoal!\nTudo bem com vocês?') # "\n" salta uma linha
print('Olá', end=' ') # ", end=' '" permanece na mesma linha
print('mundo!')

nome = 'Maria'
idade = 28
msg_formatada = 'O nome dela é {0} e ela tem {1} anos.' .format(nome,idade)

print(msg_formatada)

nome = "Alice"
idade = 30
altura = 1.65

# Utilizando f-string para formatar a string
mensagem = f"Olá, meu nome é {nome}, eu tenho {idade} anos e minha altura é {altura} metros."
print(mensagem)
# ou
print(f"Olá, meu nome é {nome}, eu tenho {idade} anos e minha altura é {altura} metros.")

# Expressões
a = 10
b = 20
resultado = a + b

print(f'A soma de {a} + {b} é {resultado}')

# Floats
valor = 125.3653565
print(f'O valor é R$ {valor}')

# Arredondar as casas decimais
print(f'O valor é R$ {valor:.2f}') # ".2f"= "duas casas flutuantes"

# Em Python, os "escapes" na função print() são caracteres especiais que começam com 
# uma barra invertida () e indicam ações específicas durante a impressão de texto. 
# Alguns exemplos comuns incluem:

# \n: Nova linha.
# \t: Tabulação horizontal.
# \\: Barra invertida.
# \' ou \": Aspas simples ou duplas.
# \uXXXX ou \UXXXXXXXX: Sequências Unicode para caracteres especiais.

print(f'O valor é \"{valor:.2f}\"')

nome = 'João'
idade = 32

print(f'Nome: {nome}\tIdade:{idade}')
print('Data: 20\\02\\2024')