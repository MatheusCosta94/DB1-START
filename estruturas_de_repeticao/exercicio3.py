#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

#Vetor numbers
notas = []

#Repetir a possibilidade de inserir notas de acordo com o pedido do usuário
for i in range(int(input("Vamos descobrir sua média atual? quantos bimestres você já tem nota?: "))):
    notas.append(float(input("Digite a nota: ")))

#Entregar Média
print(f"A sua média das notas {notas} é: {sum(notas)/len(notas)}")
