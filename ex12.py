'''12 - Faça um algoritmo que leia o valor de um produto 
e determine o valor que deve ser pago, conforme a escolha da forma de pagamento
 pelo comprador e imprima na tela o valor final do produto a ser pago. 
 Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.

 Tabela de Código de Condições de Pagamento

 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto

 2 - À Vista no cartão de crédito, recebe 10% de desconto

 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros

 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%'''
produto = float(input('Digite o valor do produto: ')) 
forma_pagamento = int(input('Digite a forma de pagamento: '))

desconto = produto * 0.15
desconto_cartao = produto * 0.10
juros = produto * 0.10  

if forma_pagamento == 1:
    valor_final = produto - (produto * 0.15)
    print(f'O valor final do produto é de R$ {valor_final:.2f}')
elif forma_pagamento == 2:
    valor_final = produto - (produto * 0.10)
    print(f'O valor final do produto é de R$ {valor_final:.2f}')
elif forma_pagamento == 3:
    valor_final = print(" O produto será preço normal sem juros no cartão em duas vezes!")
elif forma_pagamento == 4:
    valor_final = produto + (produto * 0.10)
    print(f'Pode pagar parcelado em três veze no cartão e o valor final do produto é de R$ {valor_final:.2f}')
else:
    print('Forma de pagamento inválida, digie uma opção válida!')
    
   
