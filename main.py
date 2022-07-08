import base

cnpj1 = input('Digite um CNPJ: ')
if base.valida(cnpj1):
    print(f'{cnpj1} é valido.')
else:
    print(f'{cnpj1} é invalido.')

# AQUI SAO GERADOS 100 CNPJ ALEATORIOS
'''for i in range(100):
    novo_cnpj = base.gera()
    formatado = base.formata(novo_cnpj)
    print(formatado)'''
