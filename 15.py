x=int(input("Quantos numeros deseja inserir? "))
cont=0
soma=0
while cont < x:
    z=int(input("Digite algum numero: "))
    soma = (soma + z)
    cont+=1
    
media = soma/x
print(media)