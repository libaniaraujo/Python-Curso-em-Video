# Custo da viagem

'''distância = float(input('Qual a distância de sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:preço = distância * 0.45
print('E o preço de sua passagem será de R${:.2f}'.format(preço))'''

distância = float(input('Qual a distância de sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distância))
preço = distância * 0.50 if distância<= 200 else distância * 0.45
print('E o preço de sua passagem será de R${:.2f}'.format(preço))