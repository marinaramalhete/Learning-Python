# Faça um programa que recebe uma lista de números reais e exibe sua média


num = input("Digite uma lista de números reais (separados por espaços):\n")
lista = num.split()
lista_num = []
for x in lista:
    n = float(x)
    lista_num.append(n)

def media(lista_num):
        soma = sum(lista_num)
        return soma/len(lista_num)

print(f'A média dos elementos inseridos na lista é {media(lista_num)}')