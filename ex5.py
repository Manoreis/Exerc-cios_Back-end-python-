'''5 - Faça um algoritmo que leia o valor do salário mínimo
e o valor do salário bruto de um usuário, calcule quantos salários mínimos esse 
usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).'''
salario_minimo = float(input('Digite o valor do salário mínimo: '))
salario_bruto = float(input('Digite o valor do salário bruto: '))

salario_minimo_ganho = salario_bruto / salario_minimo

print(f'O usuário ganha {salario_minimo_ganho:.2f} salários mínimos')