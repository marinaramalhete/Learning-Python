# Final - COH_PIAH

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = {}
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = {}
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma_mod = 0
    if type(as_b[0]) is list:
        lista_Sab = []
        for lin in range(len(as_b)):
            for col in range(len(as_b[lin])):
                soma_mod += abs(as_a[col] - as_b[lin][col])
            Sab = soma_mod / 6
            lista_Sab.append(Sab)
        return lista_Sab
    else:
        for i in range(len(as_b)):
            soma_mod += abs(as_a[i] - as_b[i])
        Sab = soma_mod / 6
        return Sab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    if type(texto) != list:
        aux = texto
        texto = []
        texto.append(aux)
    for i in texto:
        sentencas = []
        sentencas = separa_sentencas(str(i))
        frases = []
        num_tot_sentencas = 0
        soma_cat_sentencas = 0
        for i in range(len(sentencas)):
            frase_i = separa_frases(str(sentencas[i]))
            frases.append(frase_i)
            num_tot_sentencas += 1
            soma_cat_sentencas += len(sentencas[i])
        palavras = []
        num_tot_frases = 0
        soma_cat_frases = 0
        for frase in frases:
            for col in range(len(frase)):
                palavra_i = separa_palavras(str(frase[col]))
                palavras.append(palavra_i)
                num_tot_frases += 1
                soma_cat_frases += len(str(frase[col]))
        mtrx_para_lista = []  # transform.. palavras de matriz para lista
        for palavra in palavras:
            for col in range(len(palavra)):
                mtrx_para_lista.append(palavra[col])
        palavras = mtrx_para_lista[:]
        soma_comp_palavras = 0
        num_tot_palavras = 0
        for lin in range(len(palavras)):
            for col in range(len(palavras[lin])):
                soma_comp_palavras += len(str(palavras[lin][col]))
            num_tot_palavras += 1
        matriz_ass_input = [tam_m_pal(soma_comp_palavras, num_tot_palavras)]
        matriz_ass_input.append(type_token(palavras, num_tot_palavras))
        matriz_ass_input.append(h_lego(palavras, num_tot_palavras))
        matriz_ass_input.append(tam_m_sent(soma_cat_sentencas, num_tot_sentencas))
        matriz_ass_input.append(compx_med(num_tot_frases, num_tot_sentencas))
        matriz_ass_input.append(tam_m_frase(soma_cat_frases, num_tot_frases))
    return matriz_ass_input


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    aux_ass_com = (ass_comparadas[:])
    aux_ass_com.sort()
    for indice in range(len(ass_comparadas)):
        if aux_ass_com[0] == ass_comparadas[indice]:
            copiah = indice
    return copiah - 1


def main():
    lista_texto = []
    lista_sentencas = []
    lista_frases = []
    lista_palavras = []
    lista_assinatura = []
    lista_pal_unicas = 0
    lista_pal_diferentes = []
    #lista_assinatura = le_assinatura()
    lista_texto = le_textos()
    for s in range(len(lista_texto)):
        lista_sentencas = separa_sentencas(lista_texto[s])
    for f in range(len(lista_sentencas)):
        lista_frases = separa_frases(str(lista_sentencas[f]))
    for p in range(len(lista_frases)):
        lista_palavras = separa_palavras(str(lista_frases[p]))
    lista_pal_unicas = n_palavras_unicas(str(lista_palavras))


    print(lista_sentencas)
    print(lista_frases)
    print(lista_palavras)
    print('Palavras Unicas: ', lista_pal_unicas)


main()