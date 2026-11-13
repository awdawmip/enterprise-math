#!/usr/bin/env python3
"""R749SMY: exact Fraction certificate for the B disjoint-edge (1/3,1/3) fiber."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import json

C=(1,2,4,8,15)
B=tuple(x for x in range(1,16) if x not in C)
t=s=F(1,3)

def chi(mask,x):
    return 1 if (mask&x).bit_count()%2 == 0 else -1

def solve(A,b):
    n=len(b)
    rows=[[F(x) for x in row]+[F(rhs)] for row,rhs in zip(A,b)]
    for j in range(n):
        piv=next((k for k in range(j,n) if rows[k][j]),None)
        if piv is None: return None
        rows[j],rows[piv]=rows[piv],rows[j]
        d=rows[j][j]
        rows[j]=[x/d for x in rows[j]]
        for k in range(n):
            if k != j and rows[k][j]:
                d=rows[k][j]
                rows[k]=[x-d*y for x,y in zip(rows[k],rows[j])]
    return tuple(row[-1] for row in rows)

def source(z):
    return tuple((1+t*chi(3,x)+s*chi(12,x)
        +sum(z[i]*chi(C[i],x) for i in range(5)))/16 for x in range(16))

def moment(p,mask):
    return sum(p[x]*chi(mask,x) for x in range(16))

def tv(p,q):
    return sum(abs(x-y) for x,y in zip(p,q))/2

vertices=set()
nonsingular=feasible=0
for support in combinations(range(16),5):
    A=[[chi(mask,x) for mask in C] for x in support]
    rhs=[-1-t*chi(3,x)-s*chi(12,x) for x in support]
    z=solve(A,rhs)
    if z is None: continue
    nonsingular+=1
    p=source(z)
    if min(p)<0: continue
    feasible+=1
    assert sum(p)==1 and all(moment(p,k)==({3:t,12:s}.get(k,F(0))) for k in B)
    vertices.add(p)
assert (nonsingular,feasible,len(vertices))==(3008,312,37)

def group(x):
    A,D=chi(3,x),chi(12,x)
    return 0 if (A,D)==(1,1) else (1 if (A,D)==(1,-1) else
           (2 if (A,D)==(-1,1) else 3))

def decoder(a,b):
    classes=(a,b,b,1-a-2*b)
    assert min(classes)>=0 and sum(classes)==1
    return tuple(classes[group(x)]/4 for x in range(16))

q=decoder(F(128,225),F(46,225))
qc=decoder(F(4,9),F(2,9))
assert (moment(q,3),moment(q,12))==(F(41,75),F(41,75))
assert (moment(qc,3),moment(qc,12))==(t,s)
assert all(moment(qc,k)==0 for k in B if k not in (3,12))
hu=Counter(str(tv(q,p)) for p in vertices)
hc=Counter(str(tv(qc,p)) for p in vertices)
assert hu==Counter({'353/900':16,'92/225':9,'1/3':8,'67/300':4})
assert hc==Counter({'3/8':16,'1/3':12,'4/9':5,'1/4':4})
assert max(tv(q,p) for p in vertices)==F(92,225)
assert max(tv(qc,p) for p in vertices)==F(4,9)

def witness(assign):
    p=tuple(F(assign.get(i,0)) for i in range(16))
    assert sum(p)==1 and all(moment(p,k)==({3:t,12:s}.get(k,F(0))) for k in B)
    assert p in vertices
    return p

wA=witness({4:F(1,12),7:F(1,12),8:F(1,12),11:F(1,12),
            12:F(1,6),13:F(1,6),14:F(1,6),15:F(1,6)})
wB=witness({3:F(1,9),5:F(1,36),6:F(1,36),7:F(1,9),
            9:F(1,36),10:F(1,36),11:F(1,9),12:F(1,9),
            13:F(1,9),14:F(1,9),15:F(2,9)})
wC=witness({0:F(1,6),3:F(1,6),5:F(1,12),6:F(1,12),
            9:F(1,12),10:F(1,12),12:F(1,6),15:F(1,6)})
SA=(4,7,8,11,12,13,14,15)
SB=(5,6,7,9,10,11,13,14,15)
SC=(0,3,5,6,9,10,12,15)
assert [sum(w[x] for x in S) for w,S in ((wA,SA),(wB,SB),(wC,SC))]==[1,F(7,9),1]
# Symmetrized decoder: class masses (a,b,b,c), c=1-a-2b.
# Lower bounds are 1-a/2-3b/2, -2/9+3a/4+b, and 2b.
# Weights 12/25,8/25,5/25 cancel the a and b coefficients.
assert F(12,25)+F(8,25)+F(5,25)==1
assert -F(12,25)/2+F(8,25)*F(3,4)==0
assert -F(12,25)*F(3,2)+F(8,25)+2*F(5,25)==0
assert F(12,25)-F(8,25)*F(2,9)==F(92,225)
# Calibration requires a+b=2/3: radius >= max(2/3-b,2b).
assert F(2,3)-F(2,9)==2*F(2,9)==F(4,9)

result={
    'schema':'R749SMY_TWO_DISJOINT_MOMENTS_POINT_CERTIFICATE_V1',
    'status':'PASS','frozen_science_commit':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'model':'F2^4, B ten retained Walsh characters, m_3=m_12=1/3, other B moments zero',
    'support_sets_checked':4368,'nonsingular_bases':nonsingular,
    'feasible_bases':feasible,'distinct_vertices':len(vertices),
    'unrestricted_minimax_TV':'92/225','calibrated_minimax_TV':'4/9',
    'calibration_penalty':'8/225',
    'unrestricted_decoder_class_masses':['128/225','46/225','46/225','1/45'],
    'calibrated_decoder_class_masses':['4/9','2/9','2/9','1/9'],
    'unrestricted_histogram':dict(sorted(hu.items())),
    'calibrated_histogram':dict(sorted(hc.items())),
    'lower_witness_event_masses':['1','7/9','1'],
    'lower_certificate_weights':['12/25','8/25','5/25'],
    'arithmetic':'exact Fraction and exhaustive 5-active-set vertex enumeration; no float or external solver',
    'scope':'one exact rational interior fiber only; no full t,s square or native V29/V39 claim'
}
print(json.dumps(result,indent=2,ensure_ascii=False))
