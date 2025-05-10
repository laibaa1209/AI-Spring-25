def alpha_beta(cards, left, right, is_max, alpha, beta):
    if left > right:
        return 0

    if is_max:
        pick_left = cards[left] + alpha_beta(cards, left + 1, right, False, alpha, beta)
        pick_right = cards[right] + alpha_beta(cards, left, right - 1, False, alpha, beta)
        best = max(pick_left, pick_right)
        alpha = max(alpha, best)
        return best
    else:
        pick_left = alpha_beta(cards, left + 1, right, True, alpha, beta)
        pick_right = alpha_beta(cards, left, right - 1, True, alpha, beta)
        best = min(pick_left, pick_right)
        beta = min(beta, best)
        return best

def find_best_move(cards):
    left_score = cards[0] + alpha_beta(cards, 1, len(cards) - 1, False, float('-inf'), float('inf'))
    right_score = cards[-1] + alpha_beta(cards, 0, len(cards) - 2, False, float('-inf'), float('inf'))
    return 0 if left_score >= right_score else -1

def play_game(cards):
    max_score = 0
    min_score = 0
    turn = 'Max'

    print(f"Initial Cards: {cards}")

    while cards:
        if turn == 'Max':
            index = find_best_move(cards)
            if index == 0:
                pick = cards.pop(0)
            else:
                pick = cards.pop()
            max_score += pick
            print(f"Max picks {pick}, Remaining Cards: {cards}")
            turn = 'Min'
        else:
            if cards[0] <= cards[-1]:
                pick = cards.pop(0)
            else:
                pick = cards.pop()
            min_score += pick
            print(f"Min picks {pick}, Remaining Cards: {cards}")
            turn = 'Max'

    print(f"Final Scores - Max: {max_score}, Min: {min_score}")
    if max_score > min_score:
        print("Winner: Max")
    elif max_score < min_score:
        print("Winner: Min")
    else:
        print("It's a tie!")

if __name__ == '__main__':
    cards = [4, 10, 6, 2, 9, 5]
    play_game(cards)
