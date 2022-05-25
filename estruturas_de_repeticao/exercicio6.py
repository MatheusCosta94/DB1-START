#Faça um Programa que leia três números e mostre o maior deles.


#Vetor numbers
numbers = []

for i in range(2):
#Pedir Número inteiro
    numbers.append(int(input("Digite um numero: ")))

#Entregar maior
print(f"O maior dos números {numbers} é: {max(numbers)}")
