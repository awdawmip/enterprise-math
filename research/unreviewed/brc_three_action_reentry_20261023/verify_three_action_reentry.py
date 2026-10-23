#!/usr/bin/env python3
"""Exact auxiliary BRC three-action reentry audit. Standard library only.
16-state integer occupancy, independent pair formula, polynomial arithmetic.
This is author-side evidence, not a native X6 or admission certificate.
"""
from fractions import Fraction as Q
from itertools import product
import json

GOOD=(0b0011,0b0110,0b1010,0b1100)
PAIRS=((0,1),(1,2),(1,3),(2,3))
BASE={0:(0,2,0,1), 2:(1,1,0,1)}
W=(0,3,2,0,2,0)

def masks(word,actions):
    state=(1,)+(0,)*15
    prev_d=S=M=prev_r=0
    rows=[]
    for t,action in enumerate(word,1):
        nxt=[0]*16
        for mask,c in enumerate(state):
            if c:
                for i,v in enumerate(actions[action]):
                    if v:nxt[mask|(1<<i)]+=c*v
        state=tuple(nxt)
        d=sum(state[m] for m in GOOD)
        inc=d-3*prev_d
        S=3*S+max(inc,0)
        M=max(3*M,d)
        r=S-M
        rows.append((t,action,Q(d,3**t),Q(inc,3**t),
                     Q(M,3**t),Q(r,3**t),Q(r-3*prev_r,3**t)))
        prev_d,prev_r=d,r
    return rows

def independent_pairs(word,actions):
    total=Q(0)
    for i,j in PAIRS:
        pair=si=sj=Q(1)
        for a in word:
            qi,qj=Q(actions[a][i],3),Q(actions[a][j],3)
            pair*=qi+qj
            si*=qi
            sj*=qj
        total+=pair-si-sj
    return total

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return tuple(c)

def mult(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return tuple(c)

def polynomial(word):
    u={0:((0,),(1,1),(1,-1),(1,)),
       2:((1,),(1,),(0,),(1,)),
       3:((0,),(0,),(0,),(3,))}
    out=(0,)
    for i,j in PAIRS:
        pair=si=sj=(1,)
        for a in word:
            x,y=u[a][i],u[a][j]
            pair=mult(pair,add(x,y))
            si=mult(si,x)
            sj=mult(sj,y)
        out=add(out,add(pair,tuple(-x for x in add(si,sj))))
    while len(out)>1 and out[-1]==0:out=out[:-1]
    return out

def main():
    counts={}
    checks=0
    witness_counts={}
    for label in range(4):
        actions={**BASE,3:tuple(3 if i==label else 0 for i in range(4))}
        bylen={}
        for n in range(1,7):
            hits=[]
            for w in product((0,2,3),repeat=n):
                rows=masks(w,actions)
                assert rows[-1][2]==independent_pairs(w,actions)
                checks+=1
                gains=[r[0] for r in rows if r[-1]>0]
                if gains and gains!=list(range(gains[0],gains[-1]+1)):
                    hits.append(''.join(map(str,w)))
            bylen[n]=hits
        counts[label]={str(k):len(v) for k,v in bylen.items()}
        witness_counts[label]=bylen[6]
    assert checks==4368
    assert all(counts[j][str(k)]==0 for j in range(4) for k in range(1,6))
    assert all(counts[j]['6']==0 for j in range(3))
    assert counts[3]['6']==6
    actions={**BASE,3:(0,0,0,3)}
    rows=masks(W,actions)
    assert [(r[0],r[-1]) for r in rows if r[-1]>0]==[(4,Q(2,27)),(6,Q(2,243))]
    polys=[polynomial(W[:t]) for t in range(1,7)]
    assert polys==[(0,),(6,),(12,3),(30,12,9),(54,36,15),(114,108,90,9)]
    param_checks=0
    for z in (Q(0),Q(1,3),Q(2,3),Q(9,10),Q(947,1000),Q(948,1000),Q(1)):
        probs={0:(Q(0),(1+z)/3,(1-z)/3,Q(1,3)),
               2:(Q(1,3),Q(1,3),Q(0),Q(1,3)),
               3:(Q(0),Q(0),Q(0),Q(1))}
        for t in range(1,7):
            value=Q(0)
            for i,j in PAIRS:
                pair=si=sj=Q(1)
                for a in W[:t]:
                    qi,qj=probs[a][i],probs[a][j]
                    pair*=qi+qj;si*=qi;sj*=qj
                value+=pair-si-sj
            assert value==sum(Q(c)*z**i for i,c in enumerate(polys[t-1]))/3**t
            param_checks+=1
    result=dict(status='AUTHOR_UNREVIEWED',witness='032020',
                gain_times=[4,6],gain_sizes=['2/27','2/243'],
                count_by_added_deterministic_label=counts,
                n6_witnesses_label3=witness_counts[3],
                independent_occupancy_crosschecks=checks,
                exact_polynomial_coefficients_low_to_high=polys,
                polynomial_fraction_crosschecks=param_checks,
                native_x6_bridge=False,formal_claim=False)
    print(json.dumps(result,sort_keys=True,indent=2))
if __name__=='__main__':main()
