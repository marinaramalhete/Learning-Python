# Linha X Coluna

altura = 5
for linha in range(1, altura + 1):
    print("*", end = "")
    for _ in range(2, altura):
        if linha in [1, altura]:
            print("*", end = "")
        else:
            print(end = " ")
    print("*")
