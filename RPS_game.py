# RPS_game.py
import random

def play(player1, player2, num_games, verbose=False):
    p1 = ""
    p2 = ""
    p1_score = 0
    p2_score = 0
    for i in range(num_games):
        p1 = player1(p2)
        p2 = player2(p1)

        if p1 == p2:
            winner = "Tie"
        elif (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
            winner = "Player 1"
            p1_score += 1
        else:
            winner = "Player 2"
            p2_score += 1

        if verbose:
            print(f"Game {i+1}: Player 1: {p1}  Player 2: {p2}  Winner: {winner}")

    return {"Player 1": p1_score, "Player 2": p2_score}


def quincy(prev_play, opponent_history=[]):
    if prev_play == "":
        opponent_history.clear()
    quincy_play = ["R", "P", "S", "R", "P"]
    return quincy_play[len(opponent_history) % len(quincy_play)]


def abbey(prev_play, opponent_history=[]):
    if prev_play == "":
        opponent_history.clear()
    if len(opponent_history) == 0:
        guess = "P"
    else:
        last = opponent_history[-1]
        if last == "P":
            guess = "S"
        elif last == "R":
            guess = "P"
        else:
            guess = "R"
    opponent_history.append(prev_play)
    return guess


def kris(prev_play):
    if prev_play == "":
        return "R"
    return prev_play


def mrugesh(prev_play, opponent_history=[]):
    if prev_play == "":
        opponent_history.clear()
    opponent_history.append(prev_play)
    if len(opponent_history) < 2:
        return "S"
    else:
        last_two = opponent_history[-2:]
        if last_two == ["R", "R"]:
            return "P"
        elif last_two == ["S", "S"]:
            return "R"
        elif last_two == ["P", "P"]:
            return "S"
        else:
            return "R"
