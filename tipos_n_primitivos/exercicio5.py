# Escreva um programa que conte quantas string tenham tamanho maior que 2 e o primeiro e último caracteres sejam iguais. 
#(Exemplo de lista: ['abc','xyz','aba','1221']


from collections import Counter
lista = []

contad = int(input('Vamos fazer uma lista de strings, quantas palavras você quer incluri na lista:'))

for i in range(contad):
    frase = input(f'Digite a palavra {i}:')
    lista.append(frase)

contador = (0)
for i in range(contad):
    separar_strings = list(lista[i])
    if len(lista[i]) > 2 and separar_strings[0] == separar_strings[-1]:
        contador += 1
print(contador)
