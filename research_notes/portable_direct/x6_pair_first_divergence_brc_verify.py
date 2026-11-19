#!/usr/bin/env python3
"""First distinguishing word depth for signed-X6 two-source Boolean BRC languages."""
import json
from collections import Counter
from itertools import combinations
from x6_full_signed_port_r14_brc_verify import grid_ball, two_language, norm, lattice_ball_count

def verify_dim(d,H):
    near=list(grid_ball(d,H))
    far=[(H+1,)+(0,)*(d-1),(0,H+1)+(0,)*(d-2), (-(H+2),)+(0,)*(d-1)]
    states=near+far
    languages={x:[two_language(x,h) for h in range(H+1)] for x in states}
    counts=Counter()
    for x,y in combinations(states,2):
        actual=next((h for h in range(H+1) if languages[x][h]!=languages[y][h]),None)
        predicted=min(norm(x),norm(y)) if (x!=y and min(norm(x),norm(y))<=H) else None
        assert actual==predicted,(d,H,x,y,actual,predicted)
        counts[str(actual) if actual is not None else '>H']+=1
    return {'dimension':d,'horizon':H,'near_vectors':len(near),'far_representatives':len(far),
            'unordered_distinct_vector_pairs_tested':sum(counts.values()),
            'first_difference_depth_histogram':dict(sorted(counts.items())),
            'full_ball_class_count':lattice_ball_count(d,H)}

def main():
    result={'schema':'EM_X6_R14B_FIRST_DIFFERENCE_TYPED_BRC_V1','status':'PASS',
    'theorem':'For distinct nonzero signed-unit-step relative displacements d,d2, minimum successful-language distinguishing word length equals min(||d||_1,||d2||_1).',
    'tests':[verify_dim(2,3),verify_dim(6,2)],
    'X6_new_classes_by_h_1_6':[lattice_ball_count(6,h)-lattice_ball_count(6,h-1) for h in range(1,7)],
    'scope':'conditional vacancy-only fully signed six-Port-source-labelled Boolean BRC support; no native physical admission'}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
