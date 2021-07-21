l = int(input("Digite a largura do retângulo:"))
alt = int(input("Digite a altura do retângulo:"))
tralha = "#"

def retangulo(tralha, l, alt):
    LC = tralha * l
    LCC = tralha + ("#" * (l - 2)) + tralha if l > 2 else LC
    if alt >= 1:
        print(LC)
    for _ in range(alt - 2):
        print(LCC)
    if alt >= 2:
        print(LC)
retangulo(tralha, l, alt)
