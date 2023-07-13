from random import randint

'''
continue_play Function
Usada para verificar se o jogador deseja jogar novamente

return void
'''
def continue_play():

    play_again = ''
    
    while play_again.lower() != 'n':
        play()
        
        print ('Você quer jogar novamente? ')
        play_again = input('Escreva \'s\' para sim ou \'n\' para não: ')


'''
user_choice Function
Usada para retornar a escolha do jogador

return int
'''    
def user_choice(options):
    
    for index,option in enumerate(options):
        print(f'{index} = {option}')

    user_input = int(input('Qual número você escolhe?'))
    user_input_validator = user_choice_validator(user_input)
    
    return user_input_validator

'''
user_choice_validator Function
Usada pra validar se o número escolhido pelo jogador está entre os números permitidos

return int
'''
def user_choice_validator(user_option):
    
     while user_option != 1 or 2 or 3:
        
        print('Opção não permitida!')
        print('Escolha uma das opções apresentadas!')
        
        user_choice(user_option)
        

'''
computer_choice Function
Usada para retornar a opção escolhida aleatoriamente pelo computador

return int
'''
def computer_choice(content):

    computer_chose = randint(0,len(content)-1)
    
    return computer_chose

'''
validate_results Function
Usada para validar qual opção é a vencedora

return string
'''
def validate_results(choices, player, computer):

    if player == computer:
        return print('Ocorreu um empate!')
    
    elif (player == 0 and computer == len(choices)-1) or ( player > computer and not(player == len(choices)-1 and computer == 0)):
        return print('Jogador Venceu!')
    
    return print('Jogador Perdeu')

'''
play Function
Usada para iniciar o jogo e mostrar as opções escolhidas e o vencedor

return void
'''
def play():
    print('''
    ---------------------------------
    Bem vindo ao Pedra, Papel e Tesoura! - Escolha uma opção
    ---------------------------------
    ''')

    # Opções que serão escolhidas pelo jogador e pelo computador
    options_list = ['Pedra', 'Papel' , 'Tesoura']
    player_result = user_choice(options_list)
    computer_result = computer_choice(options_list)
    
    # Representação visual da escolha de cada um
    print(f'Escolha do jogador: {options_list[player_result]}')
    print(f'Escolha do computador: {options_list[computer_result]}')

    # Verifica o resultado e diz quem foi o vencedor
    results = validate_results(options_list, player_result, computer_result)
    
    print (f'\n{results}')
    
    
continue_play()