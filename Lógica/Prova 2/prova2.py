# Escreva um programa em python que pergunte ao usuário a velocidade de um carro.
#  Caso ultrapasse 80 km/h, exiba uma mensagem 
# dizendo que o usuário foi multado e o valor da multa, 
# cobrando R$20,00 por cada km que exceder 80 km/h

v=float(input("Por favor, digite a velocidade do carro (em km/h): "))
m=(v-80)*20
if(v> 80.0):{
    print(f"Infelizmente, o condutor foi multado, pois estava a uma velocidade de {v}km/h em uma pista com limite de 80km/h. O valor da multa será de {m} reais (20 reais por cada Km/h excedido do limite da pista)")
}
    
else:{
    print("O condutor estava dentro do limite de velocidade.")
}

