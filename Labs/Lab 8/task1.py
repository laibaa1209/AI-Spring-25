def task1_card_probabilities():
    total_cards = 52
    red_cards = 26  # Hearts and Diamonds
    hearts = 13
    diamonds = 13

    # Face cards: J, Q, K of each suit = 3 * 4 = 12 total
    face_cards = 12
    diamond_face_cards = 3  # J♦, Q♦, K♦
    spade_face_cards = 3    # J♠, Q♠, K♠
    queen_cards = 4         # One in each suit

    # (a) Probability of drawing a red card
    p_red = red_cards / total_cards

    # (b) Given that it's red, probability it's a heart
    p_heart_given_red = hearts / red_cards

    # (c) Given that it's a face card, probability it's a diamond
    p_diamond_given_face = diamond_face_cards / face_cards

    # (d) Given that it's a face card, probability it's a spade or a queen
    spade_or_queen = len(set(["J♠", "Q♠", "K♠", "Q♦", "Q♣", "Q♥"]) & 
                         set(["J♠", "Q♠", "K♠", "J♦", "Q♦", "K♦", "J♥", "Q♥", "K♥", "J♣", "Q♣", "K♣"]))
    p_spade_or_queen_given_face = spade_or_queen / face_cards

    print(f"(a) P(Red card) = {p_red:.2f}")
    print(f"(b) P(Heart | Red) = {p_heart_given_red:.2f}")
    print(f"(c) P(Diamond | Face card) = {p_diamond_given_face:.2f}")
    print(f"(d) P(Spade or Queen | Face card) = {p_spade_or_queen_given_face:.2f}")

task1_card_probabilities()
