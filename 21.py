
n = int(input('Digite um numero para saber se é um numero primo ou não: '))

for i in range(2, n):
    if n % i == 0:
        print("Não é primo")
        break
else:
        print("É primo")
