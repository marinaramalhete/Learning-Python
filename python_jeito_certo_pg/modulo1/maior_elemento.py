# Faça um programa que recebe uma lista de números reais
# e exibe o seu maior elemento.


num = input("Digite uma lista de números reais (separados por espaços):\n")
lista = num.split()
lista_num = []
for x in lista:
    n = float(x)
    lista_num.append(n)

maior = lista_num[0]
for n in lista_num:
    if n > maior:
        maior = n

print(f'O maior número é {maior}')

# outra maneira:
print(max(lista_num))