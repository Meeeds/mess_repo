import copy, sys
from collections import defaultdict

best_strat_lost = defaultdict(int)
best_strat_full = defaultdict(list)

def play_game(cards, turns, total_lost, history, recursion, id):
    # base case: less than 2 cards left or no turns left
    # print("  "*recursion+f"play_game_{id}({cards}, {turns}, {total_lost}, {history})")
    if turns == 0:
        if cards > 2: # player must rest if they have any cards left
            history[2].append(f'rest {cards- 1}')
            play_game(cards- 1, (cards - 1) // 2, total_lost + 1, history,recursion+1,"a")
        else:
            if history[1] == best_strat_lost[history[0]]:
                best_strat_full[history[0]].append(history[2])
            elif history[1] > best_strat_lost[history[0]]:
                best_strat_lost[history[0]]=history[1]
                best_strat_full[history[0]]=[history[2]]
            print("  "*recursion,history)
            return
    else:
        for i in range(0,turns*2+1): # suppose we can lose all cards at maximum
            # make the choice and continue the game$
            new_history = copy.deepcopy(history)
            new_history[0]+=turns
            new_history[1]+=i
            new_history[2].append(f"{i}, {turns} turns")
            play_game(cards - i, 0, total_lost + i, new_history,recursion+1,"b")

# start the game with 11 cards and 5 turns, 0 total lost cards
number_of_cards=int(sys.argv[1])
play_game(number_of_cards, number_of_cards//2, 0, [0,0,[]], 0,"f")

print('best_strat_lost ' , dict(best_strat_lost))
for key, value in best_strat_full.items():
    if len(value)==1:
        print(f"{key} turns with {best_strat_lost[key]} lost cards: {value[0]} ")
    else:
        for s in value:
            print(f"  {key} turns with {best_strat_lost[key]} lost cards: {s}")

