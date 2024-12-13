def play(player1, player2, num_games, verbose=False):
    results = {"player1_wins": 0, "player2_wins": 0, "ties": 0}
    player1_history = []
    player2_history = []

    for _ in range(num_games):
        player1_move = player1(player2_history[-1] if player2_history else '', player2_history)
        player2_move = player2(player1_history[-1] if player1_history else '', player1_history)

        player1_history.append(player1_move)
        player2_history.append(player2_move)

        if player1_move == player2_move:
            results["ties"] += 1
        elif (player1_move == "R" and player2_move == "S") or \
             (player1_move == "P" and player2_move == "R") or \
             (player1_move == "S" and player2_move == "P"):
            results["player1_wins"] += 1
        else:
            results["player2_wins"] += 1

        if verbose:
            print(f"Player 1: {player1_move} | Player 2: {player2_move}")

    return results