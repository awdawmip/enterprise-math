#!/usr/bin/env python3
"""BRC N4/S23 six-witness 8/15 theorem: exact Fraction certificate.

Run: python VERIFY.py. No optimizer or floating-point theorem input.
"""
from fractions import Fraction as F
from itertools import combinations
import json

M20=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
     (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
A=(0,0,0,1,1,1); B=(2,2,3,2,2,4); C=(5,6,7,8,9,10)
GROUP=(0,0,1,2,2,3)
BASE=('34 24 34 24','34 23 34 34','34 34 34 23',
      '24 24 12 12','12 12 24 34','12 13 23 24',
      '23 34 12 13','24 34 12 14')

def prepared(z):
    f=[]
    for x in range(6):
        a,b,c=z[A[x]],z[B[x]],z[C[x]]
        f.append((a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c)))
    return tuple(tuple(sum((F(M20[i][x],20)*f[x][t] for x in range(6)),F(0))
                       for t in range(4)) for i in range(6))

def decoded(d):
    return tuple(tuple(sum((F(M20[i][x],20)*d[GROUP[x]][t] for x in range(6)),F(0))
                       for t in range(4)) for i in range(6))

def pair_decoder(s):
    rows=[]
    for pair in s.split():
        row=[F(0)]*4
        for atom in pair:row[int(atom)-1]+=F(1,2)
        rows.append(tuple(row))
    return tuple(rows)

def tv(p,q):return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2

def loss(p,q):return max(tv(x,y) for x,y in zip(p,q))

def O(s,t):return (s,t,F(0),F(0),F(0),F(0),F(1),F(1),F(1),F(0),F(1))
def N(s,t):return (s,t,F(0),F(0),F(0),F(1),F(0),F(0),F(0),F(0),F(0))

controls={
    'W':(F(1),F(0),F(0),F(0),F(1),F(0),F(0),F(0),F(0),F(0),F(0)),
    'J':(F(1),F(1,3),F(0),F(0),F(0),F(0),F(0),F(0),F(0),F(1),F(0)),
    'A':O(F(1,7),F(1)),
    'B':O(F(1),F(1,7)),
    'C':N(F(1,7),F(1)),
    'X':O(F(1),F(1,15))
}
P={k:prepared(v) for k,v in controls.items()}
D9=((F(9,14),F(0),F(5,14),F(0)),
    (F(9,14),F(0),F(0),F(5,14)),
    (F(1,2),F(0),F(0),F(1,2)),
    (F(1,2),F(1,2),F(0),F(0)))
D10=((F(41,63),F(0),F(22,63),F(0)),
     (F(41,63),F(0),F(22,63),F(0)),
     (F(29,45),F(0),F(29,315),F(83,315)),
     (F(31,63),F(0),F(22,63),F(10,63)))

def triple_certificate(names):
    """Maximal disjoint-event triple lower bound across all six original rows."""
    candidates=[]
    for i in range(6):
        src=[P[k][i] for k in names]
        owner=[max(range(3),key=lambda j:src[j][t]) for t in range(4)]
        events=tuple(''.join(str(t+1) for t in range(4) if owner[t]==j) or '-' for j in range(3))
        total=sum((max(src[j][t] for j in range(3)) for t in range(4)),F(0))
        candidates.append(((total-1)/3,i+1,events,total))
    return max(candidates,key=lambda v:v[0])

def main():
    r=F(8,15)
    for z in controls.values():
        assert len(z)==11 and all(0<=x<=1 for x in z)
    for v in P.values():
        assert len(v)==6 and all(len(row)==4 and sum(row)==1 and min(row)>=0 for row in v)
    fixed=[decoded(pair_decoder(s)) for s in BASE]
    for d in (D9,D10):
        assert len(d)==4 and all(sum(row)==1 and min(row)>=0 for row in d)
    qall=fixed+[decoded(D9),decoded(D10)]
    fixed_min={k:min(loss(p,q) for q in fixed) for k,p in P.items()}
    assert fixed_min=={'W':F(1),'J':F(2,3),'A':F(4,7),'B':F(4,7),'C':F(4,7),'X':r}
    risks={k:[loss(p,q) for q in qall] for k,p in P.items()}
    assert all(min(row)<=r for row in risks.values())
    assert max(min(row) for row in risks.values())==r
    assert all(min(risks[k][8:])<=F(32,63) for k in ('W','J','A','B','C'))
    assert risks['X'][4]==r
    names=tuple(P)
    triples={tuple(c):triple_certificate(c) for c in combinations(names,3)}
    assert len(triples)==20
    # At r'<8/15, every witness must use label 9 or 10.
    # Check all 2^5 unordered assignments (fix X to color zero).
    color_obstructions=[]
    for mask in range(1<<5):
        colors={name:(mask>>i)&1 for i,name in enumerate(names[:5])}
        colors['X']=0
        prohibited=[(c,v) for c,v in triples.items()
                    if len({colors[k] for k in c})==1 and v[0]>=r]
        assert prohibited,(mask,colors)
        chosen=min(prohibited,key=lambda x:(x[0],x[1][1]))
        color_obstructions.append(''.join(chosen[0]))
    # Smaller human-checkable obstruction family (W with any two except B,X,
    # together with JAC, ACX, JCX, JAX).
    needed=('WJA','WJB','WJC','WJX','WAB','WAC','WAX','WBC','WCX',
            'JAC','ACX','JCX','JAX')
    assert all(triples[tuple(s)][0]>=r for s in needed)
    assert triple_certificate(('J','A','X'))[0]==r
    assert triple_certificate(('J','C','X'))[0]==r
    result={
       'result':'PASS_BRC_N4_S23_SIX_WITNESS_EXACT_8_15_20261102',
       'scientific_input_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
       'theorem':'real stochastic two-free-decoder six-witness minimax',
       'radius':str(r),
       'witnesses':list(names),
       'new_witness_controls':[str(v) for v in controls['X']],
       'new_witness_prepared':[[str(z) for z in row] for row in P['X']],
       'fixed_eight_min':{k:str(v) for k,v in fixed_min.items()},
       'bank_risk':{k:str(min(v)) for k,v in risks.items()},
       'X_decoder5_six_row_TV':[str(tv(a,b)) for a,b in zip(P['X'],qall[4])],
       'triple_dual_certificates':[{'triple':''.join(c),'row':v[1],
                                    'events':list(v[2]),'sum':str(v[3]),
                                    'lower':str(v[0])} for c,v in triples.items()],
       'forbidden_core':list(needed),
       'two_colorings_checked':len(color_obstructions),
       'all_32_colorings_have_a_forbidden_triple':True,
       'coverage':'six original positive-mix prepared distributions; four stops; all 20 triples; 32 colorings; real stochastic decoders',
       'review_status':'author computation only; not independent review or native admission'
    }
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=='__main__':main()
