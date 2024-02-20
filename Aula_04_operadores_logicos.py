# Operadores lógicos
# Esses operadores são usados para combinar expressões booleanas e avaliar condições 
# mais complexas em Python.

# and: Retorna True se ambas as expressões forem verdadeiras.
# or: Retorna True se pelo menos uma das expressões for verdadeira.
# not: Inverte o valor de verdade de uma expressão, retornando True se a expressão for falsa e False se a 
# expressão for verdadeira.

# Participar do evento
idade = 28
altura = 1.67

resultado = (idade >= 18) and (altura >= 1.65)
msg = f'Pode participar do evento?: {resultado}'

print(msg)

# Alarme
porta = 'f'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg = f'Alarme disparado? {alarme}'
print(msg)

# Requisitos compras
tem_dinheiro = False
tem_dinheiro = not tem_dinheiro

msg = f'Tem dinheiro? {tem_dinheiro}'
print(msg)