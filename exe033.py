# Maior e menor valores

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < c:
    menor = c
# Verificando quem é o maior valor:
maior =  a
if b > a and b > c:
    maior = b
if c > a and c > c:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))