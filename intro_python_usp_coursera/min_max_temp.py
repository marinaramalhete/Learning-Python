# Temperaturas mínimas e máximas

def MinMax(temperaturas):
        print("A menor temperatura do mes foi: "), minima(temperaturas), "C."
        print("A maior temperatura do mes foi: "), maxima(temperaturas), "C."

def minima(temps):
        min = temps[0]
        for i in range(1, len(temps)):
                if temps[i] < min:
                    min = temps[i]
        return min

def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array", temp)
        print("Valor esperado :", valor_esperado, ". Valor calculado: ", valor_calculado)

def testa_minima():
    print("Iniciando os testes")
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0, 0])
    teste_pontual([-15, -12, 2, 20, 30])
    print("Finalizando os testes")
