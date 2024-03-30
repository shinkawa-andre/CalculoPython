# Este codigo só funciona com expressoes simples
# **********************************************

from sympy import *

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

cal = input('O que você quer calcular (i - integral), (d - derivada): ')

if cal == 'i' or cal == 'I':
    inte = input('Digite a expressão (EX: cos(x)): ')
    result = integrate(inte, x)
    print(f'O Resultado é: {result}')

if cal == 'd' or cal == 'D':
    der = input('Digite a expressão (EX: cos(x)): ')
    result = diff(der, x)
    print(f'O Resultado é: {result}')