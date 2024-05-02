'''2 - Faça um algoritmo para receber um número qualquer e imprimir na tela
 se o número é par ou ímpar, positivo ou negativo.'''
num = float(input('Digite um número: '))

if num % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')

print("=-" * 10)

if num > 0:
    print('O número é positivo')
else:
    print('O número é negativo')

