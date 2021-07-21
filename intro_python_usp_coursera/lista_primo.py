def éPrimo(x):
    fator = 2
    if x == 2:
        return True

    while x % fator != 0 and fator <= x/2:
        fator += 1
    return x % fator != 0


limite = int(input("Limite máximo: "))
for n in range(2, limite):
    if éPrimo(n):
        print (n, end=", ")
lista1 = ["rosa", "verde", "azul"]
lista1[:]
