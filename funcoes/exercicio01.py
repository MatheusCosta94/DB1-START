# Escreva um programa que execute uma função que encontre o maior número de uma lista passada por parâmetro

# Criar Lista
numbers = []


# Inserir números na lista contida na função inserirnúmeros
def inserirnúmeros():
    for i in range(cont):
        maior = ()
        numbers.append(int(input('Digite um número: ')))

# Lógica para encontrar o maior da lista
def encontremaior():
    maior = (0)
    for i in range(cont):
        if numbers[i] > maior:
            maior = (numbers[i])
        if numbers[i] < maior:
            maior = (maior)
    return maior

# Retornar valores
def imprimir():
    print(f'Sua lista é composta por {numbers}')
    position = int(input('Sabendo que a primeira posição equivale a 0, Qual posição você quer retornar?'))
    print(f'Na posição {position} está o número {numbers[position]}, e o maior é o número {resultmaior}')


cont = int(input('Quantos números você quer guardar?: '))

# Indicar funções
inserirnúmeros()
resultmaior = encontremaior()
imprimir()
