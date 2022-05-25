#Faça um Programa que peça dois números e imprima o maior deles.


#Vetor numbers
numbers = []

#Pedir Número inteiro
numbers.append(int(input("Digite um numero: ")))
#Pedir Número inteiro
numbers.append(int(input("Digite outro número: ")))
#Entregar maior
print(f"O maior dos números {numbers} é: {max(numbers)}")
