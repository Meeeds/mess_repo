#!/usr/bin/env python
import json
import sys

handicap_moves = ["",
                  "",
                  ";B[pd];W[];B[dp]",
                  ";B[pd];W[];B[dp];W[];B[pp]",
                  ";B[pd];W[];B[dp];W[];B[pp];W[];B[dd]",
                  ";B[pd];W[];B[dp];W[];B[pp];W[];B[dd];W[];B[jj]",
                  ";B[pd];W[];B[dp];W[];B[pp];W[];B[dd];W[];B[dj];W[];B[pj]",
                  ";B[pd];W[];B[dp];W[];B[pp];W[];B[dd];W[];B[dj];W[];B[pj];W[];B[jj]",
                  ";B[pd];W[];B[dp];W[];B[pp];W[];B[dd];W[];B[dj];W[];B[pj];W[];B[jd];W[];B[jp]",
                  ";B[pd];W[];B[dp];W[];B[pp];W[];B[dd];W[];B[dj];W[];B[pj];W[];B[jd];W[];B[jp];W[];B[jj]",
                  ]


data = json.loads(open(sys.argv[1], encoding="utf8").read())
moves = data["gamedata"]["moves"]
out_file = open(sys.argv[1][:-3]+"sgf", 'w')

print("(", file=out_file)


handicap = (data["handicap"] > 1)

if handicap == False:
    black = True
else:
    black = False
    print(';KM[0.5]', file=out_file)
    print(handicap_moves[data["handicap"]], file=out_file)


for move in moves:
    move = chr(97+move[0])+chr(97+move[1])
    if black:
        print(';B['+move+']', file=out_file)
        black = False
    else:
        print(';W['+move+']', file=out_file)
        black = True


print(")", file=out_file)
