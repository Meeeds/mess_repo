import sys
# let's fill from lvl 4 because before it does not makes much sens


def compute_proba(race, level, total_pieces, a, dissmiss, dissmissName):
    if dissmiss is not None:
        single_proba = sum([ a[i][level]/100.0 * race[i] for i in range(0,4) ] ) / sum( [ a[i][level]/100.0 * (total_pieces[i] - dissmiss[i] ) for i in range(0,4) ] )
    else:
        single_proba = sum([ a[i][level]/100.0 * race[i] for i in range(0,4) ] ) / sum( [ a[i][level]/100.0 * total_pieces[i] for i in range(0,4) ] )

    #print(f"{name} for level {level+1} 1p proba is {single_proba:.2%} {dissmissName}")
    fiveP_proba = 1-(1-single_proba)**5
    return fiveP_proba

def display_proba(name, race, level, total_pieces, a, dissmiss, dissmissName):
    c_proba = compute_proba(race, level, total_pieces, a, dissmiss, dissmissName)
    print(f"{name} for level {level+1} 5p proba is {c_proba:.2%} {dissmissName}")


global_probabilities_pieces = [[100, 70, 60, 45, 35, 30, 30, 24, 22, 20],
                               [0,   30, 35, 40, 40, 33, 30, 30, 25, 22],
                               [0,   0,   5, 15, 23, 30, 30, 28, 25, 25],
                               [0,   0,   0, 0,   2, 7, 10, 17, 25, 28],
                               [0,   0,   0, 0,   0, 0, 0, 1, 3, 5]]
a = global_probabilities_pieces

#total_pieces
total_pieces = [19.0,19.0,17.0,15.0]


#races
goblin = [3,1,0,2]
elves = [3,3,3,0]
trolls = [3,1,1,0]
goblin = [3,1,0,2]
orcs = [1,2,0,1]
undead = [3,1,2,2]
races = {"elves" : elves, "trolls" : trolls, "goblin" : goblin, "orcs" : orcs} 

#type
warriors = [3,3,2,2]
knights = [2,2,1,2]
assassin = [2,3,3,1]
hunters = [2,2,1,3]
#types = { "warriors" : warriors, "knights" : knights, "assassin" : assassin}
types = { "knights" : knights, "assassin" : assassin, "hunters" : hunters, "warriors" : warriors}


#3rd category

all_dict = {**types, **races}


for level in range(0,10):
    if ( sum ([a[i][level] for i in range(0,4)]) != 100):
        print(f"proba not equal to 100 : {level+1}")
    else:
        print(f"proba equal to 100 : {level+1}")



# print proba of piece per level for warriors
for name, race in all_dict.items():
    for level in range(3, 7):

        #display_proba(name, race, level, total_pieces, global_probabilities_pieces, None, "")
        #display_proba(name, race, level, total_pieces, global_probabilities_pieces, warriors, "with dissmiss assasin")
        #display_proba(name, race, level, total_pieces, global_probabilities_pieces, assassin, "with dissmiss warriors")
        #display_proba(name, race, level, total_pieces, global_probabilities_pieces, elves, "with dissmiss elves")
        # display_proba(name, race, level, total_pieces, global_probabilities_pieces, test, "with dissmiss test")

        base_proba = compute_proba(race, level, total_pieces, global_probabilities_pieces, None, "")
        best_proba = [0.0]
        for dissmiss_name, dissmiss_race in all_dict.items():
            if dissmiss_name == name:
                continue
            current_proba = compute_proba(race, level, total_pieces, global_probabilities_pieces, dissmiss_race, f"with dissmiss {dissmiss_name}") 
            if current_proba > best_proba[0] : 
                   best_proba = [current_proba, dissmiss_name, dissmiss_race]

        display_proba(name, race, level, total_pieces, global_probabilities_pieces, None, "")
        display_proba(name, race, level, total_pieces, global_probabilities_pieces, best_proba[2], f"with dissmiss {best_proba[1]}") 
    print()


        
#print(sys.argv[1])


