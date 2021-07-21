# Operação de multiplicação

tamanho = int(input("Digite o tamanho da sequência de números: "))
produto = 1
for _ in range(tamanho):
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto *= valor
print("O produto dos valores digitados é: ", produto)
