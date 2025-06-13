ValorCompra = float(input('Digite o valor total da compra: '))
resposta = str(input('Escolha as opções de gorgeta A - 10%  B - 15%  C - 20%: '))
gorjeta = 0
if resposta == 'A' or 'a':
    gorjeta = ValorCompra * 0.10
elif resposta == 'B' or 'b':
    gorjeta = ValorCompra * 0.15
elif resposta == 'C' or 'c':
    gorjeta = ValorCompra * 0.2
print(f'O valor da gorjeta será: {gorjeta}')