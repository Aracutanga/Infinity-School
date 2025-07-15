soma=0
quantidade_de_numeros =0

while True:
    numero=int(input("Por favor, digite um numero inteiro: "))
    if numero == 0:
        break
    quantidade_de_numeros+=1
    soma+=numero


if quantidade_de_numeros > 0:
    media=soma/quantidade_de_numeros

else:
    media=0


print(f"A quantidade de números digitados até chegar no número 0 foi {quantidade_de_numeros} . A soma foi igual a {soma}. E a média igual a {media}")