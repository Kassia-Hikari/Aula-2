numeros = input("Digite números separados por espaço: ").split()
numeros = [int(num) for num in numeros]

cont_numeros = 0
while cont_numeros < len(numeros):
    x = cont_numeros + 1  
    while x < len(numeros):
        if numeros[cont_numeros] > numeros[x]:
            numeros[cont_numeros], numeros[x] = numeros[x], numeros[cont_numeros]
        x += 1
    cont_numeros += 1

print("Ordem crescente: ", numeros)