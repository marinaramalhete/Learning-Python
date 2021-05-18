# Na vida real, ambos os jogadores escolhem ao mesmo tempo, mostrando suas mãos.
# Ainda não sabemos como fazer isso, então nosso programa vai funcionar da seguinte maneira:
# I. Ao executar o programa, ele deve escrever o nome do jogo e pedir que o jogador 1 faça sua escolha.
# II. O programa aguarda o jogador 1 digitar sua escolha e pressionar *Enter*
# III. O programa pede que o jogador 2 digite sua escolha
# IV. O programa aguarda o jogador 2 digitar sua escolha e pressionar *Enter*
# V. O programa analisa as 2 escolhas e declara o campeão ou um empate

# Regras:
# I. Pedra vence Tesoura.
# II. Tesoura vence Papel.
# III. Papel vence Pedra.
# IV. Quando ambos são iguais, temos um empate.

print('Bem vinde ao jogo Pedra, Papel e Tesoura :D')
escolha_1 = input('Jogador 1, escolha Pedra, Papel ou Tesoura e pressione ENTER: ').lower()
escolha_2 = input('Jogador 2, escolha Pedra, Papel ou Tesoura e pressione ENTER: ').lower()

def game(escolha_1, escolha_2):    
    while escolha_1 and escolha_2 is not None:
        if ((escolha_1 == "tesoura") and (escolha_2 == 'pedra') or (escolha_1 == "pedra") and (escolha_2 == 'tesoura')):
            return("Pedra vence Tesoura!")
        if ((escolha_1 == "tesoura") and (escolha_1 == 'papel') or (escolha_1 == "papel") and (escolha_2 == 'tesoura')):
            return("Tesoura vence Papel!")
        if ((escolha_1 == "papel") and (escolha_2 == 'pedra') or (escolha_1 == "pedra") and (escolha_2 == 'papel')):
            return("Papel vence Pedra!")
        if escolha_1 == escolha_2:
            return("Ambos jogadores fizeram a mesma escolha! Temos um empate! --'")            

print(game(escolha_1, escolha_2))
