import random

def player(prev_play, opponent_history=[]):
    if opponent_history is None:
        opponent_history = []
    opponent_history.append(prev_play)

    if prev_play == '':
        return random.choice(['R', 'P', 'S'])

    # Estrategia básica para predecir el próximo movimiento
    most_common = max(set(opponent_history), key=opponent_history.count)
    if most_common == 'R':
        return 'P'
    elif most_common == 'P':
        return 'S'
    elif most_common == 'S':
        return 'R'

    return random.choice(['R', 'P', 'S'])


def always_rock(*args):
    return 'R'


def repeat_opponent_move(last_move, opponent_history=[]):
    if last_move == '':
        return 'R'
    return last_move


def cyclical_bot(last_move, opponent_history=[]):
    moves = ['R', 'P', 'S']
    if last_move == '':
        return 'R'
    return moves[(moves.index(last_move) + 1) % 3]


def random_bot(*args):
    return random.choice(['R', 'P', 'S'])