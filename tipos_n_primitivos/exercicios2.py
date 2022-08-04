# Escreva um programa que multiplique todos os itens de uma lista.
lista = []
numbers = int(input('Quantos números você quer inserir na Lista?'))
print (f'Ok, Então digite {numbers} números a medida que o sistema for solicitando!')

while len(lista) < numbers:
    incluir = int(input('Digite um número: '))
    lista.append(incluir)
    
print (f'Você formou uma lista composta por {lista}')
print ('Que tal fazer uma tabuada com esse números?')
