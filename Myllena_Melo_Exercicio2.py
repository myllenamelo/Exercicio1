valor = float (input('Insira o valor da parcela: '))
taxa = float (input('Insira a taxa: '))
tempo = float (input('Insira o número de dias '))

prestacao = (valor + (valor*(taxa/100)*tempo))

print ("O valor da prestação em atraso é: R$",prestacao)