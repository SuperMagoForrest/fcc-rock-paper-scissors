# RPS.py

def player(prev_play, opponent_history=[]):
    # Salva lo storico delle mosse dell'avversario
    if prev_play != "":
        opponent_history.append(prev_play)

    # Predizione basata su pattern matching (ultimi 3 moves)
    guess = "R"
    n = 3  # lunghezza del pattern
    if len(opponent_history) > n:
        pattern = opponent_history[-n:]
        counts = {"R": 0, "P": 0, "S": 0}

        for i in range(len(opponent_history) - n):
            if opponent_history[i:i+n] == pattern:
                next_move = opponent_history[i+n]
                counts[next_move] += 1

        if counts:
            guess = max(counts, key=counts.get)

    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[guess]
