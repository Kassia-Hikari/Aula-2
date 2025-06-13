vogais="aeiouAEIOU"
numero_vogais=0
palavra=input("Digite uma palavra: ")

for letra in palavra:
    if letra in vogais:
        numero_vogais += 1
        
if numero_vogais > 0:
    print(f"A palavra '{palavra}' tem {numero_vogais} vogais.")
else:
    print("Não há vogais na palavra.")