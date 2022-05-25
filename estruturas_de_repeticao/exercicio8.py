#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre #pelo mais barato

#Vetor numbers
prices = []

for i in range(int(input("Quantos produtos você quer analisar?: "))):
#Pedir Número inteiro
    prices.append(float(input(f"Digite o preço do produto: ")))

#Indicar menor
print(f"O mais barato dos produtos {prices} é: {min(prices)}")
