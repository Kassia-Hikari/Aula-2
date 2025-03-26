n1 = float(input('Digite um numero a ser calculado'))
n2 = float(input('Digite um segundo numero para a operação'))
op = int(input('Digite uma operação entre: 1-soma, 2- subtração, 3- divisao, 4- multiplicação '))
if op == 1:
    print(n1+n2)
elif op == 2:
    print(n1-n2)
elif op == 3:
    print(n1/n2)
elif op == 4:
    print(n1*n2)
else:
    print('digite um numero de operação valida')