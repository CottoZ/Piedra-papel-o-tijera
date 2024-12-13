from RPS import player, always_rock, repeat_opponent_move, cyclical_bot, random_bot
from RPS_game import play

# Definir los bots
opponents = {
    "Always Rock": always_rock,
    "Repeat Opponent Move": repeat_opponent_move,
    "Cyclical Bot": cyclical_bot,
    "Random Bot": random_bot,
}

# Número de partidas por oponente
num_games = 1000

# Jugar contra cada oponente
for name, bot in opponents.items():
    print(f"Playing against: {name}")
    result = play(player, bot, num_games)
    print(result)
    print("-" * 40)