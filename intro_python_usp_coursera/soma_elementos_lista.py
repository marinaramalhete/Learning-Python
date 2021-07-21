# Dada determinada lista, soma dos elementos

def soma_elementos(list):
    soma = 0
    for i in list:
        soma = soma + i
    return soma

lista = [1,2,3,4,5,6]
print(soma_elementos(lista))

# n = int(input("Digite um número inteiro: "))
# soma = 0
# while (n > 0):
#     resto = n % 10
#     n //= 10
#     soma += resto
# print(soma)