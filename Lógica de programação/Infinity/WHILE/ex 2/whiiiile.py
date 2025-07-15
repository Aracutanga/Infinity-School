
# p=str.lower("Parar")
s=0

while True:
    numero=int(input("Digite seu número: "))
    s+=numero
    print(f"A soma é igual a: {s}")
    print("Digite 'parar' para sair do programa, ou qualquer outra tecla para continuar.")
    ans=input("Digite sua opção: ")
    if ans.lower()=="parar":
        print(f"O programa será fechado. Sua soma final foi {s}. Até mais.")
        break
    else:
        print(f"Vamos continuar! Sua soma até agora é {s} Digite o próximo número: ")

