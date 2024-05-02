'''6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.'''

valor = float(input('Digite o valor: '))
reajuste = valor * 0.05
print(f'O reajuste de 5% é: {reajuste}')

valor_reajuste = valor + reajuste

print(f'O valor com reajuste de 5% é: {valor_reajuste}')