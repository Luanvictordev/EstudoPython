nome = "Luiz Otávio"
altura = 1.80
peso = 95
imc = peso / (altura**2)

# Luiz otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura.'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

# anotação:
# .2f faz com que tenha 2 casas decimais.

print(linha_1)
print(linha_2)
print(linha_3)