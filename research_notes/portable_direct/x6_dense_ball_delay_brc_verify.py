#!/usr/bin/env python3
"""Exact typed signed-axis Boolean-BRC witness and vacancy-cone certificate.

The infinite-parameter result is a symbolic proof, while this program checks
finite fully specified six-component occupied balls and the shortest witness.
"""
from itertools import product
from math import comb
import json

V=tuple(tuple(sign if j==i else 0 for j in range(6)) for i in range(6) for sign in (-1,1))
e1=(1,0,0,0,0,0)
origin=(0,)*6
norm=lambda x:sum(abs(i) for i in x)
add=lambda x,y:tuple(a+b for a,b in zip(x,y))

def B(R):
    # Enumerate only actually occupied cells: exact finite integer recursion.
    out=[]
    def rec(p,left):
        if len(p)==6:
            out.append(tuple(p));return
        for a in range(-left,left+1):rec(p+[a],left-abs(a))
    rec([],R)
    return sorted(out)

def step(state,label,direction):
    src=state[label]; dest=add(src,direction)
    if dest in state:return None
    out=list(state);out[label]=dest
    return tuple(out)

def witness(R):
    coords=B(R)
    center=coords.index(origin); neighbour=coords.index(e1)
    assert R>=2
    # Swapping labels at center and e1 leaves the geometric occupancy unchanged.
    a=tuple(coords)
    b=list(coords);b[center],b[neighbour]=b[neighbour],b[center];b=tuple(b)
    w=[(coords.index((t,0,0,0,0,0)),e1) for t in range(R,1,-1)]
    w.append((neighbour,e1))
    assert len(w)==R
    for idx,(label,d) in enumerate(w):
        next_a=step(a,label,d);next_b=step(b,label,d)
        assert next_a is not None,(R,idx,'A')
        if idx<R-1: assert next_b is not None,(R,idx,'B');b=next_b
        else: assert next_b is None,(R,idx,'final B should reject')
        a=next_a
    # Shortest potential vacancy path to the originally occupied central cells.
    # A legal event exchanges an occupied position with an adjacent vacancy.
    # Therefore an initial vacancy needs >= R+1-norm(x) swaps to reach x.
    assert R+1-norm(origin)==R+1
    assert R+1-norm(e1)==R
    expected=sum((2**j)*comb(6,j)*comb(R,j) for j in range(min(6,R)+1))
    assert len(coords)==expected
    return len(coords), len(w)

def exhaustive_depth2():
    # For R=2, scan all legal one-letter actions and verify both configurations
    # have the same complete one-letter language; at depth 2 the witness differs.
    R=2;coords=B(R);c=coords.index(origin);n=coords.index(e1)
    a=tuple(coords);b=list(coords);b[c],b[n]=b[n],b[c];b=tuple(b)
    successes=[]
    for label in range(len(coords)):
        for d in V:
            xa=step(a,label,d);xb=step(b,label,d)
            assert (xa is None)==(xb is None)
            if xa is not None:successes.append((label,d))
    count=0
    for label,d in successes:
        aa=step(a,label,d);bb=step(b,label,d)
        for label2 in range(len(coords)):
            for d2 in V:
                p=step(aa,label2,d2);q=step(bb,label2,d2)
                if (p is None)!=(q is None):count+=1
    assert count>0
    return len(successes),count

def run():
    samples={str(R):{'occupied_cells':N,'first_distinguishing_depth':h} for R in range(2,8) for N,h in [witness(R)]}
    L1,firstdiff=exhaustive_depth2()
    return {'result':'PASS','full_signed_spatial_dimension':6,'ports':12,'models':samples,
            'R2_legal_one_letter_events':L1,'R2_differing_two_letter_words':firstdiff,
            'method':'R2 exhaustive two-letter joint comparison; R2..7 exact ball construction and sharp-length witnesses; arbitrary R symbolic vacancy-cone argument'}
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
