"""Exact six-bit certificate for four independent five-symbol services."""
from itertools import product
from collections import Counter

THREE_D_CLASSES = [
 [1,2,3,9,14,24,40,65,90,115],
 [4,29,54,95,96,97,98,109,114,119],
 [16,27,30,33,34,37,47,66,91,116],
 [6,28,38,43,48,55,57,59,81,106],
 [7,32,52,67,72,85,86,88,89,107],
 [20,21,22,49,74,99,103,108,113,118],
 [5,10,15,45,70,76,77,78,79,120],
 [8,13,18,23,25,50,75,101,102,104],
 [11,26,41,46,61,80,82,83,84,111],
 [12,35,36,39,53,58,68,73,87,112],
 [17,42,51,56,60,63,64,71,92,117],
 [19,44,69,94,100,105,110,121,122,123],
]
STAR_COLOR = [
 [0,3,3,0,0],
 [3,0,2,1,2],
 [3,1,0,2,1],
 [1,0,1,2,3],
 [2,2,0,1,3],
]
def laminar(group):
    n=len(group[0])
    blocks=[frozenset(i for i,w in enumerate(group) if w[k]==v)
            for k in range(n) for v in range(5)]
    return all(not(a&b) or a<=b or b<=a for a in blocks for b in blocks)
def run():
    universe=set(range(125))
    diagonal={31*v for v in range(5)}
    occupied=set()
    for j,cls in enumerate(THREE_D_CLASSES):
        group=[(z//25,(z//5)%5,z%5) for z in cls]
        assert len(cls)==10 and len(set(cls))==10
        assert laminar(group),f'bad 3D group {j}'
        assert occupied.isdisjoint(cls),f'overlap in group {j}'
        occupied.update(cls)
    assert occupied==universe-diagonal
    for k in range(4):
        pts=[(u,v)for u,v in product(range(5),repeat=2)if STAR_COLOR[u][v]==k]
        assert laminar(pts),f'bad grid color {k}'
    labels={z:j for j,cls in enumerate(THREE_D_CLASSES)for z in cls}
    groups={k:[] for k in range(64)}
    for t,x,y,z in product(range(5),repeat=4):
        v=25*x+5*y+z
        if v in diagonal:
            msg=60+STAR_COLOR[t][x]
        else:
            msg=12*t+labels[v]
        groups[msg].append((t,x,y,z))
    assert all(groups.values()) and sum(map(len,groups.values()))==625
    assert all(laminar(g) for g in groups.values())
    histogram=dict(sorted(Counter(map(len,groups.values())).items()))
    assert histogram=={6:3,7:1,10:60},histogram
    print('PASS messages=64 histories=625 all_laminar=True',
          'message_size_histogram=',histogram,'bits=6')
    return groups
if __name__=='__main__': run()
