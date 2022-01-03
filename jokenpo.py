'''Game Jokenpo'''
from random import randint
from time import sleep #importar o modulo time para cadenciar o nome Jokenpo

itens = ('Pedra', 'Papel', 'Tesoura') #definit os itens
computador = randint(0, 2)
#apresentar as opcoes:
print('''Suas opcoes:
[0] pedra
[1]papel
[2]tesoura''')
#Ojogador faz a jogada
jogador = int(input('Qual e a sua jogada?: '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('JOGADA INVÁLIDA. Tente novamente!')
#usar o sleep para cadenciar a apresentação do nome do jogo, e no final
print('JO')
sleep(1)
print('Ken')
sleep(1)
print('po')
sleep(2)
# criamos uma linha para separar os dados na saída do código.
print('-=' * 11)
#mostrar na tela os resultados das jogadas, utilizamos as f strings.
#Em seguida apresentar novamente a linda de separação.
print(f'Computador jogo:{itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('-=' * 11)
#montar estruturas condicionais para apresentar os resultados
if computador == 0:#se o computador jogou pedra
    if jogador == 0:
        print('EMPATOU')
    elif jogador ==1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')  
    else:
        print('JOGADA INVALIDA')

elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('EMPATOU')
    elif jogador ==1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')  
    else:
        print('JOGADA INVALIDA')

elif computador == 2:# computador jogo tesoura
    if jogador == 0:
        print('EMPATOU')
    elif jogador ==1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')  
    else:
        print('JOGADA INVALIDA')



