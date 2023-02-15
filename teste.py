# x = 0
# while True:
#     x = x + 1
    
#     if x <= 10:
#         print('teste')
#     else:
#         break
# print('terminou')


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]

# l1.extend(l2)

# print(l1)

# lista = ['lista1', 'lista2', 'lista']

# for enu, v in enumerate(lista):
#     print(enu, v)


# x = 10
# y = 'Rafael'

# x, y = y, x

# print(x)


# user_login = True

# msg= "usuario logado" if user_login else 'deslogado'

# print(msg)

"""
idade_user = "17"

se_idade = (idade_user >= 18 and idade_user.isnumeric())
msg = "maior de idade" if se_idade else "menor de idade"

print(msg)
"""
"""
for a, d in enumerate(range(10, 1, -1)):
    print(a, d)
"""

cpf_digitado = input("Digite o CPf: ")

cpf_tratado_digitado = ''.join(filter(str.isalnum, cpf_digitado)) # remove string(caracteres não numericos)
cpf_tratado = ''.join(filter(str.isalnum, cpf_digitado)) # remove string(caracteres não numericos)
soma_digitos = 0

# calcula os 10 primeiros digitos do cpf
for n, valor in enumerate(range(10, 1, -1)):
    valor_cpf = int(cpf_tratado[n])
    calcula_numeros = valor_cpf * valor
    soma_digitos += int(calcula_numeros)

# print(soma_digitos)
# calcula o resto do calcula dos 10 primeiros digitos
resto_calculo_digito_1 = 11 - (int(soma_digitos) % 11)
verifica_calculo_digito_1 = resto_calculo_digito_1 if resto_calculo_digito_1 <= 9 else 0

cpf_tratado = str(cpf_tratado[0:9]) + str(verifica_calculo_digito_1)
soma_digitos = 0

# calcula os 11 primeiros digitos do cpf
for n, valor in enumerate(range(11, 1, -1)):
    valor_cpf = int(cpf_tratado[n])
    calcula_numeros = valor_cpf * valor
    soma_digitos += int(calcula_numeros)

# calcula o resto do calcula dos 10 primeiros digitos
resto_calculo_digito_2 = 11 - (int(soma_digitos) % 11)

cpf_tratado = str(cpf_tratado) + str(resto_calculo_digito_2)

# verifica cpf digitado
msg = "cpf valido" if cpf_tratado == cpf_tratado_digitado else "CPF invalido"
print(msg)