# Módulo que abriga as funções referentes a escolhas do Jogador e da Máquina

from random import randint

from functions.validation import *

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
    
    if user_input == '0' or user_input == '1' or user_input == '2':
        return int(user_input)
    
    while(input_validator == False or (user_input != '0' or user_input != '1' or user_input != '2')):
        print('Escolha o número de uma das opções acima!')
        user_input = input('Qual número você escolhe?')
        input_validator = user_input.isnumeric()
        while (input_validator == True):
            if user_input == '0' or user_input == '1' or user_input == '2':
                
                return int(user_input)
                
            else:
                print('Escolha o número de uma das opções acima!')
                user_input = input('Qual número você escolhe?')
                input_validator = user_input.isnumeric()
    
    
'''
computer_choice Function
Usada para retornar a opção escolhida aleatoriamente pelo computador

return int
'''
def computer_choice(content):

    computer_chose = randint(0, len(content)-1)
    return computer_chose

