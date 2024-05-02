''' 11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, 
calcule a média das nota obtidas, imprima na tela o nome do aluno e 
se o aluno foi aprovado ou reprovado. 
Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.'''

nome = input('Digite o nome do aluno: ')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4 

if media >= 7:
    print(f'O aluno {nome} foi aprovado com a média {media: .2f}')

else:
    print(f'O aluno {nome} foi reprovado com a média {media}')