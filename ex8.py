'''8 - Faça um algoritmo que leia três valores inteiros diferentes e 
imprima na tela os valores em ordem decrescente e decrescente'''

valor1 = int(input("Digite o nº: "))
valor2 = int(input("Digite o nº: "))
valor3 = int(input("Digite o nº: "))

ordemCrescente = sorted([valor1, valor2, valor3])
ordemDecrescente = sorted([valor1, valor2, valor3], reverse=True)

print(f'Os valores digitados em ordem crescente são: {ordemCrescente}')
print(f'Os valores digitados em ordem decrescente são: {ordemDecrescente}')