''' 9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, 
leia o seu peso e sua altura e imprima na tela sua condição 


de acordo com a tabela abaixo:

Fórmula do IMC = peso / (altura) ²

Tabela Condições IMC

 Abaixo de 18,5   | Abaixo do peso          

 Entre 18,6 e 24,9 | Peso ideal (parabéns)  

 Entre 25,0 e 29,9 | Levemente acima do peso

 Entre 30,0 e 34,9 | Obesidade grau I 

 Entre 35,0 e 39,9 | Obesidade grau II (severa)

 Maior ou igual a 40 | Obesidade grau III (mórbida)'''

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))                   

imc = peso / altura 
print(f'Seu IMC é {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.6 and imc <= 24.9:
    print('Peso ideal (parabéns)')
elif imc >= 25.0 and imc <= 29.9:
    print('Levemente acima do peso')
elif imc >= 30.0 and imc <= 34.9:
    print('Obesidade grau I')
elif imc >= 35.0 and imc <= 39.9:
    print('Obesidade grau II (severa)')
elif imc >= 40:
    print('Obesidade grau III (mórbida)')
else:
    print('Digite um valor válido')


