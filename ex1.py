'''1 - Faça um algoritmo que leia os valores de A, B, C e em seguida 
imprima na tela a soma entre A e B é mostre se a soma é menor que C.'''

A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))
C = int(input('Digite o valor de C: ')) 

soma = A + B

if soma < C:
    print("=-=-" * 12)
    print(f'A soma de {A} + {B} é {soma}  e menor que {C}')
else:
    print(f'A soma de {A} + {B} é {soma} e é maior que {C}')
