import numpy

# let's fill from lvl 4 because before it does not makes much sens


global_probabilities_pieces = [[100, 70, 60, 45, 35, 30, 30, 24, 22, 20],
                               [0, 30, 35, 40, 40, 33, 30, 30, 25, 22],
                               [0, 0, 5, 15, 23, 30, 30, 28, 25, 25],
                               [0, 0, 0, 0, 2, 7, 10, 17, 25, 28],
                               [0, 0, 0, 0, 0, 0, 0, 1, 3, 5]]
a = global_probabilities_pieces

#total_pieces
total_pieces = [19.0,19.0,17.0,15.0]


#races
elves = [3,3,3,0]
trolls = [3,1,1,0]
goblin = [3,1,0,2]
orcs = [1,2,0,1]
undead = []
races = {"elves" : elves, "trolls" : trolls, "goblin" : goblin, "orcs" : orcs} 

#type
warriors = [3,3,2,2]
knights = [2,2,1,2]
assassin = [2,3,3,1]
#types = { "warriors" : warriors, "knights" : knights, "assassin" : assassin}
types = { "warriors" : warriors, "knights" : knights, "assassin" : assassin}


#3rd category


for level in range(0,10):
    if ( sum ([a[i][level] for i in range(0,4)]) != 100):
        print(f"proba not equal to 100 : {level+1}")
    else:
        print(f"proba equal to 100 : {level+1}")



# print proba of piece per level for warriors
for name, race in types.items():
    for level in range(0, 7):
        single_proba = sum([ a[i][level]/100.0 * race[i] for i in range(0,4) ] ) / sum( [ a[i][level]/100.0 * total_pieces[i] for i in range(0,4) ] )

        print(f"{name} for level {level+1} proba is {single_proba:.3f}")



