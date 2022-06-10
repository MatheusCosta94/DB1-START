# Escreva um programa que execute uma função que
# some todos os itens de uma lista passada por
# parâmetro

# Criar Lista
numbers = []


# Inserir números na lista contida na função inserirnúmeros
def inserirnúmeros():
    for i in range(cont):
        somatotal = ()
        numbers.append(int(input('Digite um número: ')))

# Lógica para somar um número da lista por vez
def somartorio():
    somafinal = (0)
    for i in range(cont):
            somafinal = somafinal + numbers[i]
    return somafinal

# Retornar valores
def imprimir():
    print(f'Sua lista é composta por {numbers}')
    print(f'Somando todos os números da lista o resultado é: {totalfinal}')


cont = int(input('Quantos números você quer guardar?: '))

# Indicar funções
inserirnúmeros()
totalfinal = somartorio()
imprimir()
