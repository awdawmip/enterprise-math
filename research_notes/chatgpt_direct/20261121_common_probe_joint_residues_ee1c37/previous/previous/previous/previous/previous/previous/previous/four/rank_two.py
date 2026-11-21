"""Exhaust two projected twelve-point templates for each type of rank-two map."""
from functools import lru_cache
from itertools import product
import json

POINTS = list(product(range(5),repeat=4))
PAIRINGS = ((0,1,2,3),(0,2,1,3),(0,3,1,2))
TYPES = (((1,0),(0,1),(1,1),(1,2)),
         ((1,0),(1,0),(0,1),(1,1)),
         ((1,0),(1,0),(1,0),(0,1)),
         ((1,0),(1,0),(0,1),(0,1)),
         ((1,0),(0,1),(1,1),(0,0)),
         ((1,0),(1,0),(0,1),(0,0)),
         ((1,0),(0,1),(0,0),(0,0)))

@lru_cache(None)
def capacity(a):
    if max(a)==1:
        return 1
    values=[]
    for b in product(*(range(1,x) if x>1 else [1] for x in a)):
        c=tuple(x-y if x>1 else 1 for x,y in zip(a,b))
        values.append(capacity(tuple(sorted(b)))+capacity(tuple(sorted(c))))
    return max(values)

def only_maximal_split():
    pairs=set()
    for b in product(range(1,5),repeat=4):
        c=tuple(5-u for u in b)
        if capacity(tuple(sorted(b)))+capacity(tuple(sorted(c)))==12:
            pairs.add(tuple(sorted(b)))
    assert pairs=={(1,1,4,4)}
    assert capacity((5,5,5,5))==12

def centered_templates():
    for pairing in PAIRINGS:
        for offsets in product(range(1,5),repeat=4):
            points=[]
            for i,j in enumerate(pairing):
                partner=pairing[i^1]
                for v in range(1,5):
                    if v==offsets[j]:
                        continue
                    p=[0]*4
                    p[j]=v
                    p[partner]=offsets[partner]
                    points.append(tuple(p))
            yield points

def classify(cols):
    projections=[[sum(p[j]*cols[j][i]for j in range(4))%5 for i in range(2)] for p in POINTS]
    def cell(p):
        a,b,c,d=p
        return projections[((5*a+b)*5+c)*5+d]
    shifts=[[1<<(5*((a+x)%5)+(b+y)%5) for a,b in product(range(5),repeat=2)]
            for x,y in product(range(5),repeat=2)]
    masks=set()
    for g in centered_templates():
        image={5*a+b for a,b in map(cell,g)}
        if len(image)==12:
            masks.update(sum(sh[i]for i in image)for sh in shifts)
    allpoints=(1<<25)-1
    disjoint=sum(allpoints^m^(1<<p) in masks for m in masks for p in range(25) if not (m>>p)&1)
    assert disjoint==0
    # Find a pair of full image sets with one shared point. If present, this
    # establishes sharpness within this type without classifying submaximal sets.
    pair=None
    for x in sorted(masks):
        outside=[i for i in range(25) if not (x>>i)&1]
        for q in range(25):
            if not (x>>q)&1:
                continue
            for j,a in enumerate(outside):
                for b in outside[j+1:]:
                    y=(allpoints^x)^(1<<a)^(1<<b)^(1<<q)
                    if y in masks:
                        pair=[sorted(i for i in range(25) if (z>>i)&1) for z in (x,y)]
                        break
                if pair: break
            if pair: break
        if pair: break
    witnesses=[]
    if pair:
        representatives={tuple(cell(p)):p for p in POINTS}
        for required in pair:
            target=sum(1<<q for q in required)
            for shape in centered_templates():
                image={5*a+b for a,b in map(cell,shape)}
                if len(image)<12:
                    continue
                hits=[j for j,sh in enumerate(shifts) if sum(sh[q] for q in image)==target]
                if hits:
                    shift=representatives[divmod(hits[0],5)]
                    group=[tuple((x+y)%5 for x,y in zip(p,shift)) for p in shape]
                    assert sorted(5*a+b for a,b in map(cell,group))==required
                    witnesses.append([POINTS.index(p) for p in group])
                    break
        assert len(witnesses)==2
    return dict(columns=cols,twelve_point_images=len(masks),disjoint_full_pairs=disjoint//2,
                pair_reaching_twenty_three=pair,lifts_of_pair=witnesses)

if __name__=='__main__':
    only_maximal_split()
    print(json.dumps([classify(cols)for cols in TYPES],indent=2))
