n1 = float(input("number #1: "))
n2 = float(input("number #2: "))
n3 = n1+n2
print(n3)


p1 = float(input("Escreva nota do primeiro bimestre: "))
p2 = float(input("Escreva nota do segundo bimestre: "))
p3 = float(input("Escreva nota do treceiro bimestre: "))
p4 = float(input("Escreva nota do quarto bimestre: "))

mp = (p1 +p2 + p3 + p4)/ 4
print(mp)


m = float(input("Escreva o comprimento em cm: "))/100
print(f"{m}m")


lado1 = float(input("Escreva o comprimento do lado1: "))
lado2 = float(input("Escreva o comprimento do lado2: "))
area_quadrado = lado1*lado2
print(f"{area_quadrado}m^2")
print(f"{area_quadrado*2}m^2")

income = float(input("Escreva seu salário por hora: "))
hours = float(input("Escreva o número de horas trabalhadas por semana: "))
weekly_income = income*hours
print(f"{weekly_income} reais por semana")
monthly_income = weekly_income*4
print(f"Equivalente a aproximadamente {monthly_income} reais por mês")
