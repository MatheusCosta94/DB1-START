#Faça um Programa que leia três números e mostre-os em ordem decrescente.
#Vetor numbers
prices = []

for i in range(int(input("Quantos produtos você quer analisar?: "))):
#Pedir Número inteiro
    prices.append(float(input(f"Digite o preço do produto: ")))
    
#Classificar e ordenadar de forma decrescente
prices.sort(reverse = True)

#Indicar menor
print(prices)
