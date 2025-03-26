idade = int(input('Digite sua idade'))
if idade <12 and idade >0:
    print('Criança Feliz')
elif idade >12 and idade <17:
    print('Adolescente Rebelde')
elif idade >=18 and idade <59:
    print('Adulto Triste')
elif idade >=60:
    print('Idoso NSS')
else:
    print('Baby Reborn')