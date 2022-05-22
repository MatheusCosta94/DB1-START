# Escreva um programa que some todos os itens de uma lista.
#Vetor numbers
numbers = []

#Repetir a possibilidade de inserir números de acordo com o pedido do usuário
for i in range(int(input("Vamos fazer uma soma? Quantos números você quer que eu some?: "))):
    numbers.append(int(input("Digite um número: ")))

#Entregar Soma
print(f"A soma de {numbers} é: {sum(numbers)}")
