#Faça um Programa que peça dois números e imprima o maior deles.


#Vetor numbers
numbers = []

for i in range(2):
#Pedir Número inteiro
    numbers.append(int(input("Digite um numero: ")))

#Entregar maior
print(f"O maior dos números {numbers} é: {max(numbers)}")
