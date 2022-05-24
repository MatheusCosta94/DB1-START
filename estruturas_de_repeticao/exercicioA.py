#Tabuada
numerotabuada = int(input('Vamos fazer a tabua de um numero, diga um número: '))
multiplicador = 1
while multiplicador <= 10:
    print('{0} X {1} = {2}'.format(multiplicador, numerotabuada, (multiplicador*numerotabuada)))
    multiplicador = multiplicador + 1
