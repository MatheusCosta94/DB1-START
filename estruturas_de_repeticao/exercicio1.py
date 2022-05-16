#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

#Perguntar Ganho por hora
ganhoporhora = int(input("Quanto você ganha por hora: "))

#Se valor informado for 0 ou menor que 0 solicita novamente que o usuário digite um valor válido
while ganhoporhora <= 0:

    ganhoporhora = int(input("Quanto você ganha por hora deve ser maior que 0, informe novamente Quanto você ganha por hora: "))

horastrabalhas = int(input("Quantas horas você trabalhou neste mês: "))

#Se valor informado for 0 ou menor que 0 solicita novamente que o usuário digite um valor válido
while horastrabalhas <= 0:

    horastrabalhas = int(input("Quantas horas você trabalhou neste mês deve ser maior que 0, informe novamente Quantas horas você trabalhou neste mês: "))

#Totalizar salário ao final do código multiplicando ganho por horas e horas trabalhadas no mês
print ("Seu salário este mês é de:",ganhoporhora * horastrabalhas)
