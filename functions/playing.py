# Módulo que abriga as funções referentes a inicio e continuação do jogo

from functions.choices import *
from functions.validation import *

'''
continue_play Function
Usada para verificar se o jogador deseja jogar novamente

return void
'''
def continue_play():

    play_again = ''
    
    while play_again.lower() != 'n':
        
        start_play()
        
        print('')
        print ('Você quer jogar novamente? ')
        play_again = input('Escreva \'s\' para sim ou \'n\' para não: ')


'''
start_play Function
Usada para iniciar o jogo e mostrar as opções escolhidas e o vencedor

return void
'''
def start_play():
    
    print('---------------------------------')
    print('Bem vindo ao Pedra, Papel e Tesoura!')
    print('---------------------------------')

    # Opções que serão escolhidas pelo jogador e pelo computador
    options_list = ['Pedra', 'Papel' , 'Tesoura']
    player_result = user_choice(options_list)
    computer_result = computer_choice(options_list)
    
    # Representação visual da escolha de cada um
    print('')
    print(f'Escolha do jogador: {options_list[player_result]}')
    print(f'Escolha do computador: {options_list[computer_result]}')

    # Verifica o resultado e diz quem foi o vencedor
    results = validate_results(options_list, player_result, computer_result)
    
    print('')
    return print (f'\n{results}')