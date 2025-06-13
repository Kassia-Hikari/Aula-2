numeros = []
par=[]

for numero in range(10):
    n = int(input(f"Insira o {numero+1}º número: "))
    if n % 2 == 0:
        par.append(n)
    numeros.append(n)

print("Ordem crescente:", sorted(numeros))
print("Ordem decrescente:", sorted(numeros, reverse=True))
print("Números pares:", par)