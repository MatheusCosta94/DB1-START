#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre


#Vetor numbers
numbers = []

#Pedir Número inteiro
numbers.append(int(input("Digite um numero inteiro: ")))
#Pedir Número Real
numbers.append(float(input("Digite um numero real: ")))
#Entregar soma
print(f"A soma dos números {numbers} é: {sum(numbers)}")
