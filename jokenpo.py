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
        print('EMPATE')
    
    elif jogador == 1:
        print('Jogador vence')
    
    elif jogador == 2:
        print('computador venceu')
    
    else:
        print('Jogada invalida')

if computador == 1:#se o computador jogou papel
    if jogador == 1:
        print('EMPATE')
    
    elif jogador == 1:
        print('Jogador Venceu')
    
    else:
        print('Jogada invalida')

if computador ==2: #se o computador jogou tesoura
    if jogador == 2:
        print('Empate')
    
    elif jogador == 2:
        print('Jogador Venceu')
    
    else:
        print('Jogada Invalida')



