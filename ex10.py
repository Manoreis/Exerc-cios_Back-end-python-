'''10 - Faça um algoritmo que leia três notas obtidas por um aluno, e 
imprima na tela a média das notas.'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print(f'A média das notas é: {media: .2f}')