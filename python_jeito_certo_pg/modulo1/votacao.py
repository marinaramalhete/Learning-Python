# Reescreva o programa que avalia a obrigatoriedade 
# do voto de outra forma, mas mantendo as 3 
# respostas corretas (obrigatório, facultativo, proibido).

idade = int(input('Digite sua idade: '))

def voto(x):
    if (x >= 18 and x <=70):
        print(f'Com {x} anos, seu voto é obrigatório!')
    elif (x >= 16):
        print(f'Com {x} anos, seu voto é facultativo!')
    else:
        print(f'Com {x} anos, você não pode votar!')    

voto(idade)
