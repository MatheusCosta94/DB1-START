# Escreva um programa que retorne o maior e o menor número de uma lista.
lista = []
numbers = int(input('Quantos números você quer inserir na Lista?'))
print (f'Ok, Então digite {numbers} números a medida que o sistema for solicitando!')

while len(lista) < numbers:
    incluir = int(input('Digite um número: '))
    lista.append(incluir)

menor = min(lista)
maior = max(lista)

print (f'O menor número da lista é {menor} e o maior é {maior}')
