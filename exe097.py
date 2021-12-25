# Um print especial

# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
# uma mensagem com tamanho adaptável.

def escreva(msg):
    tam = len(msg)
    print('~' * tam)
    print(f'{msg}')
    print('~' * tam)

# Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')