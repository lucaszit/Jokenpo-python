# Módulo que abriga funções de validação

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
