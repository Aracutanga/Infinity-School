# while True:
#     print("Looping infinito")

# contador = 0
# while (contador < 5):
#     print(contador)
#     contador += 1

# numero_screto = 42
# tentativa = 0

# while tentativa != numero_screto:
#     tentativa=int(input("Tente adivinhar o número secreto"))

# print("Parabéns! Você adivinhou o número secreto!")

# n = 0
# while(n<=10):
#     print(n)
#     n+=2

# n_s = 11
# t=0
# while t!=11:
#     t=int(input("Tente adivinhar o número secreto: "))
#     if(t>50):{
#         print("Opa, tá muuito frio. Talvez vc devesse tentar um n menor?")
#     }
#     elif(t<-1):{
#         print("Vamos tentar só com números inteiros ;)")
# }
        
# print("Parabéns! Você acertou o número secreto!")

# s=0
# l=10
# while True:
#     n=int(input("Digite um número: "))
#     s+=n

#     if s>=l:
#         break

# print(f"A soma ultrapassou o limite de {l}. A soma final: {s}")

# n_secreto=42
# t_max=6
# t=0

# while t!=n_secreto and t_max>0:
#     t=int(input("Tente adivinhar o número secreto: "))
#     t_max-=1
#     if t!=n_secreto:
#         print(f"Tentativas restantes: {t_max}")

# if t==n_secreto:
#     print("Parabéns! Você acertou o número secreto.")
    
# else:
#     print(f"Suas tentativas acabaram. O número secreto era: {n_secreto}")

# Crie um programa que solicite ao usuário adivinhar um
# número entre 1 e 100, dando dicas se a tentativa é muito alta,
# muito baixa ou correta. Adicione um limite de tentativas.

# n_secreto=42
# t_max=6
# t=0

# while t!=n_secreto and t_max>0:
#     t=int(input("Tente adivinhar o número secreto (entre 1 e 100): "))
#     t_max-=1
#     if t!=n_secreto and t>100:
#         print(f"Tá frio. Tentativas restantes: {t_max}")
#     elif t!=n_secreto and t<100:
#         print(f"No no no, só números positivos. Tentativas restantes: {t_max}")

# if t==n_secreto:
#     print("Parabéns! Você acertou o número secreto.")
    
# else:
#     print(f"Suas tentativas acabaram. O número secreto era: {n_secreto}")

# Crie um programa que solicite ao usuário que digite números
# inteiros. O programa deve continuar solicitando números até
# que a soma dos números pares digitados seja maior que 50.
# Ao atingir ou ultrapassar esse limite, o programa deve exibir a
# soma total e encerrar.
# Dica:
# Use um loop while para continuar solicitando números até
# que a condição seja atendida.
# Mantenha uma variável para rastrear a soma dos números
# pares.
# Utilize a instrução break para sair do loop quando a
# condição for atendida.
# Exiba a soma total ao final.


# s=0
# numero_par=0
# while True:
#     numero=int(input("Digite um número inteiro: "))
#     if(numero%2==0):
#         s+=numero

#     if s>=50:
#         break

# print(f"A soma final: {s}")

x=0

while x>=0:

    print('Olá mundo!')