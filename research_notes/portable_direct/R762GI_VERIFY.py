#!/usr/bin/env python3
"""R762GI — exact signed K4 STAR semidirect BRC certificate; standard library only."""
from collections import Counter
import json

STARS = ((0,1,2),(0,3,4),(1,3,5),(2,4,5))
I = tuple(range(6))
Z = (0,)*6
EVENTS = tuple((j,s) for j in range(4) for s in (1,-1))

def compose(p,q):
    return tuple(p[q[i]] for i in range(6))

def act(p,v):
    out=[0]*6
    for i,a in enumerate(v):
        out[p[i]]=a
    return tuple(out)

def invp(p):
    return tuple(p.index(i) for i in range(6))

def mul(A,B):
    x,p=A; y,q=B
    py=act(p,y)
    return tuple(a+b for a,b in zip(x,py)), compose(p,q)

def inverse(A):
    x,p=A; q=invp(p)
    return tuple(-a for a in act(q,x)),q

def make_event(j,s):
    a,b,c=STARS[j]; g=list(I)
    if s==1: g[a],g[b],g[c]=b,c,a
    else: g[a],g[b],g[c]=c,a,b
    return tuple(s*int(i in STARS[j]) for i in range(6)),tuple(g)

GENERATORS={ev:make_event(*ev) for ev in EVENTS}

def evaluate(word):
    u=(Z,I)
    for ev in word:
        u=mul(u,GENERATORS[ev])
    return u

def half_words(n):
    counts={(Z,I):1}
    witnesses={(Z,I):()}
    for _ in range(n):
        nxt=Counter()
        nw={}
        for u,weight in counts.items():
            for ev in EVENTS:
                v=mul(u,GENERATORS[ev])
                nxt[v]+=weight
                if v not in nw:
                    nw[v]=witnesses[u]+(ev,)
        counts=dict(nxt)
        witnesses=nw
    assert sum(counts.values())==8**n
    return counts,witnesses

def convolution(A,B,k):
    ac,aw=A; bc,bw=B
    target=(tuple([k]*6),I)
    value=0
    witness=None
    for u,c in ac.items():
        v=mul(inverse(u),target)
        d=bc.get(v,0)
        if d:
            value+=c*d
            if witness is None:
                witness=aw[u]+bw[v]
    if witness is not None:
        assert evaluate(witness)==target
    return value,witness

def main():
    for j in range(4):
        assert mul(GENERATORS[j,1],GENERATORS[j,-1])==(Z,I)
    halves={t:half_words(t) for t in range(6)}
    assert [len(halves[t][0]) for t in range(6)]==[1,8,57,400,2769,18592]
    expected={
        0:{"0":1},
        2:{"0":8},
        4:{"0":120},
        6:{"0":2192},
        8:{"-4":8,"0":44312,"4":8},
        10:{"-4":560,"-3":320,"-1":40,"0":955232,
            "1":40,"3":320,"4":560},
    }
    rows=[]
    for m in range(0,11,2):
        a=m//2
        counts={}
        for k in range(-m//2,m//2+1):
            num,_=convolution(halves[a],halves[a],k)
            if num: counts[str(k)]=num
        assert counts==expected[m],(m,counts)
        rows.append({"m":m,"all_words":8**m,
                     "half_distinct_states":len(halves[a][0]),
                     "joint_diagonal_counts":counts})
    num4,w4=convolution(halves[4],halves[4],4)
    num1,w1=convolution(halves[5],halves[5],1)
    assert num4==8 and len(w4)==8 and all(s==1 for j,s in w4)
    assert num1==40 and len(w1)==10
    assert evaluate(w4)==((4,)*6,I)
    assert evaluate(w1)==((1,)*6,I)
    inv1=tuple((j,-s) for j,s in reversed(w1))
    assert evaluate(inv1)==((-1,)*6,I)
    # Independent direct signed-X6 coordinate accumulation on the unit-depth witness:
    x=[0]*6
    p=I
    for j,s in w1:
        for axis in STARS[j]:
            x[p[axis]]+=s
        p=compose(p,GENERATORS[j,s][1])
    assert tuple(x)==(1,)*6 and p==I
    print(json.dumps({
       "schema":"R762GI_EXACT_SEMIDIRECT_BRC_EVIDENCE_V1",
       "model":"CANDIDATE_SIGNED_K4_STAR_SEMIDIRECT_AFFINE_ACTION",
       "frozen_task":"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
       "stars":STARS,
       "generator_count":8,
       "counts_by_depth":rows,
       "first_nonzero_joint_return_length":8,
       "first_nonzero_depth_magnitude":4,
       "shortest_unit_depth_length":10,
       "holonomy":"Z",
       "witness_depth_plus4":[list(e) for e in w4],
       "witness_depth_plus1":[list(e) for e in w1],
       "witness_depth_minus1":[list(e) for e in inv1],
       "probability_m8_nonzero":"16/16777216",
       "probability_m10_nonzero":"1840/1073741824",
       "author_verification":"PASS",
       "independent_review":"NOT_REVIEWED",
       "native_TRIADIC_CLOSURE_E_permission":"UNVERIFIED"
    },ensure_ascii=False,sort_keys=True,indent=2))

if __name__=="__main__":
    main()
