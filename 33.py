
palavras = []
for i in range(10):
    palavra = input(f"Digite a palavra {i+1}: ")
    palavras.append(palavra)


vogais = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

palavras_vogal = [p for p in palavras if p.startswith(vogais)]

print("\nLista original:")
print(palavras)
print("\nPalavras que começam com vogal:")
print(palavras_vogal)
