# Verificar se tem caracteres duplicados em strings

def verifica_duplicados(palavra):
    verificados = []
    for p in palavra:
        if p in verificados:
            return True
        verificados.append(p)
    return False

print(verifica_duplicados("marina"))