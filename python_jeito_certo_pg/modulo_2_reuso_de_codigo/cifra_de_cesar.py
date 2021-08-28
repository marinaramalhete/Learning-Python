# Criptografia com Cifra de César

# sem iterar
def cifra_cesar(chave, letra):
    print(ord(letra))
    return chr(ord(letra) + chave)

entrada = 'a'
resposta = cifra_cesar(3, entrada)
print(f'A cifra de {entrada} é {resposta}')