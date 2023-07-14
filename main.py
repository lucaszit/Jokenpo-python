from random import randint

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
user_choice Function
Usada para retornar a escolha do jogador

return int
'''    
def user_choice(options):
    
    for index,option in enumerate(options):
        print(f'{index} = {option}')


    user_input = input('Qual número você escolhe?')
    
    # Validação do user_input para permitir apenas os números informados
    # TODO: Transformar esse bloco em uma função de validação
    input_validator = user_input.isnumeric()
    while(input_validator == False):
        print('Escolha o número de uma das opções acima!')
        user_input = input('Qual número você escolhe?')
        input_validator = user_input.isnumeric()
        while (input_validator == True):
            if user_input == '0' or user_input == '1' or user_input == '2':
                int_user_input = int(user_input)
                break
            else:
                print('Escolha o número de uma das opções acima!')
                user_input = input('Qual número você escolhe?')
                input_validator = user_input.isnumeric()
                
                
    return int_user_input
    
    
'''
computer_choice Function
Usada para retornar a opção escolhida aleatoriamente pelo computador

return int
'''
def computer_choice(content):

    computer_chose = randint(0, len(content)-1)
    return computer_chose


'''
validate_results Function
Usada para validar qual opção é a vencedora

return string
'''
def validate_results(choices, player, computer):

    if player == computer:
        return 'Ocorreu um empate!'
    
    elif (player == 0 and computer == len(choices)-1) or ( player > computer and not(player == len(choices)-1 and computer == 0)):
        return 'Jogador Venceu!'
    else: 
        return 'Jogador Perdeu'


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
    

# Chamada da função que dá inicio ao jogo e encadeia todas as outras funções
continue_play()