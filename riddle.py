from math import isqrt
import sys

global_set = set()

# Find the factors of a number
def factors(n):
    result = set()
    for i in range(1, isqrt(n) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    result.remove(n)
    return frozenset(result)

# Define the game state
def game_state(gamecards, my_cards, oponent_cards):
    #print(f"    game_state({gamecards}, {my_cards}, {oponent_cards})")
    # If no cards left, return the difference of the scores
    if len(gamecards)==0:
        difference = sum(my_cards) - sum(oponent_cards)
        results = "WIN"
        if difference <= 0 :
            results = "LOST"
            return
        #if ((2 in my_cards and 6 in my_cards) or (10 in my_cards and 2 in my_cards) or (10 in my_cards and 6 in my_cards)):
        if (2 in my_cards or 10 in my_cards or 6 in my_cards):
            global_set.add(frozenset(my_cards))
            #print(f"{results} {difference} my_cards:{my_cards} oponent_cards:{oponent_cards}")
        #sys.exit()
        return 

    # Compute the result of the game for each possible card I can pick
    for card in gamecards:
        a = factors(card)
        if len(a.intersection(gamecards)) == 0:
            #print(f"cannot pick {card} with {gamecards}")
            continue
        else:
            new_gamecards= frozenset(set(gamecards) - {card}-a)
            new_my_cards = my_cards + [card]
            new_oponent_cards = oponent_cards.union(a)
            game_state(new_gamecards, new_my_cards, new_oponent_cards)
    
    new_gamecards={}
    new_oponent_cards = oponent_cards.union(gamecards)
    game_state(new_gamecards, my_cards, new_oponent_cards)


# Initialize the game
gamecards = frozenset(range(1, 24))
game_state(gamecards, [], set())
for s in global_set:
    print(s)