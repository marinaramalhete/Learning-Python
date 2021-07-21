# Escreva um programa que recebe um número inteiro do usuário
# e responde se esse número é par ou não.
# Obs.: um número é dito par se ele é divisível por 2.


num = int(input('Digite um número inteiro: '))

if (num % 2 == 0):
    print('O número é par!')
else:
    print('O número é ímpar!')

# Utilizando funções

# def num_par(num):
#     if (num % 2 ==0):
#         return True
#     else:
#         return False

# if num_par(num):
#     print(f'{num} é par!')
# else:
#     print(f'{num} é ímpar!')