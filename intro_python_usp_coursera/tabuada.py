coluna = 1
for linha in range(1, 11):
    while coluna <= 10:
        print (linha * coluna, end = "\t")
        coluna += 1
    print ()
    coluna = 1