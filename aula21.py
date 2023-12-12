# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

entrada = input('Digite (E) para ENTRAR ou (S) para SAIR: ')
if entrada == 'E':
    print('Você entrou no sistema.')
elif entrada == 'S':
    print('Você saiu do sistema.')
else:         
    print('Você não digitou nem "E" nem "S"')


    
