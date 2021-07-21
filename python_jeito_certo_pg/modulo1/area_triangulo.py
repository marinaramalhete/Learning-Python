# Cálculo da área do triângulo segundo a fórmula de Heron
# e obedecendo a condição de existência de um triângulo.


import math

a = float(input('Digite o valor do primeiro lado do triângulo: '))
b = float(input('Digite o valor do segundo lado do triângulo: '))
c = float(input('Digite o valor do terceiro lado do triângulo: '))

# Condição de existência: um de seus lados deve ser maior que o
# valor absoluto (módulo) da diferença dos outros dois lados e
# menor que a soma dos outros dois lados
def condicao_existencia(a, b, c):
    if (
        (abs(b - c) < a)
        and (a < (b + c))
        and (abs(a - c) < b)
        and (b < (a + c))
        and (abs(a - b) < c)
        and (c < (a + b))
        ):
        return True
    else:
        print('Condição de existência do triângulo não satisfeita.')

# Fórmula de Heron
def formula_heron(a, b, c):
    while condicao_existencia(a, b, c) == True:
        p = (a + b + c)/2
        area = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
        return (f'A área do triângulo é {area}')

print(formula_heron(a, b, c))