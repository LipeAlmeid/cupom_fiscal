# Exercício Faculdade - Crie um cupom fiscal 


produtos = {123: 'Camisa estampada',
        124: 'Camisa social manga longa',
        125: 'Calça Jeans'}

venda = [(123, 3, 25.55),
        (124, 2, 79.99),
        (125, 1, 99.99)]

item = 0
valor_total = 0
print("-" * 46)
print('C U P O M  F I S C A L'.center(45, ' '))
print("ITEM CÓDIGO DESCRIÇÃO" 
      " QTD.UN.VL_UNIT(R$) ST VL")
print("-" * 46)
                    
for indice in range(0, len(venda)):
    subtotal = 0 
    item += 1
    produto = produtos.get(venda[indice][0])
    quantidade = venda [indice][1]
    valor = venda[indice][2]
    subtotal += quantidade * valor 
    valor_total += subtotal
 
    print(f'{str(item).ljust(4)}'
          f'{str(venda[indice][0]).ljust(8)}'
          f'{produto.ljust(25)}'
          f'{str(quantidade).rjust(3)} UN X'
          f'{str(valor).rjust(10)}'
          f'{str(subtotal).rjust(10)}')

print("-" * 46)
print('TOTAL R$'
      f'{str(valor_total).rjust(37)}')