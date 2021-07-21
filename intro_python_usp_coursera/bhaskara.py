# Fórmula de bhaskara

import math

def delta(a, b, c):
    return (b ** 2 - 4 * a * c)

def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    if delta(a, b, c) == 0:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        print("A única raíz é: ", raiz1)
    elif delta < 0:
        print("Esta equação não possui raízes rais.")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A primeira raíz é: ", raiz1)
        print("A segunda raiz é: ", raiz2)
