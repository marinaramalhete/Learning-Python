# Escreva um programa que recebe um número inteiro do usuário 
# e responde se esse número é par ou não. 
# Um número é dito par se ele é divisível por 2.

num = int(input('Digite um número inteiro: '))

if (num % 2 == 0):
    print('O número é par! :)')
else:
    print('O número não é par! :(')
