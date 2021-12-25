# Tratando vários valores

núm = cont = soma = 0
núm = int(input('Digite um número [888 para parar]: '))
while núm != 888:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [888 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))