import random

game_options = ['Pedra', 'Papel', 'Tesoura']

player = input('Escolha entre Pedra, Papel ou Tesoura: ').lower()
machine = random.choice(game_options).lower()

if player == machine:
    print(f'Ocorreu um empate pois o jogador e a máquina escolheram {player}')
elif player == 'pedra' and machine == 'tesoura':
    print(f'O jogador venceu, pois {player} vence de {machine}')
elif player == 'pedra' and machine == 'papel':
    print(f'O jogador perdeu, pois {player} perde de {machine}')
elif player == 'papel' and machine == 'pedra':
    print(f'O jogador venceu, pois {player} vence de {machine}')
elif player == 'papel' and machine == 'tesoura':
    print(f'O jogador perdeu, pois {player} perde de {machine}')
elif player == 'tesoura' and machine == 'papel':
    print(f'O jogador venceu, pois {player} vence de {machine}')
elif player == 'tesoura' and machine == 'pedra':
    print(f'O jogador perdeu, pois {player} perde de {machine}')
