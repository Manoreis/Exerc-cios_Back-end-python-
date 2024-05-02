'''3 - Faça um algoritmo que leia dois valores inteiros A e B, 
se os valores de A e B forem iguais, deverá somar os dois valores, 
caso contrário devera multiplicar A por B. 
Ao final de qualquer um dos cálculos deve-se 
atribuir o resultado a uma variável C e imprimir seu valor na tela.'''

numA = int(input('Digite um número: '))
numB = int(input('Digite outro número: '))

if numA == numB:
    C = numA + numB
    print(f'Os numeros digitados são iguais e a soma dos dois números é {C}')
else:
    C = numA * numB
    print(f'Os numeros digitados são diferentes e multiplicação dos dois números é {C}')


