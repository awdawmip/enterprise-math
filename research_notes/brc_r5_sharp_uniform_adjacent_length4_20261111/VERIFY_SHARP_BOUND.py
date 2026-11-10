#!/usr/bin/env python3
"""Exact R5 sharp adjacent-ray bound check. Frozen GK/EM science pins unchanged."""
from itertools import combinations
from sympy import Matrix, Rational as Q, zeros
J=(1,2,3,5)
r=[Q(z,20) for z in (2,10,15,20,25,30,38)]
D=[(i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j]
C=Matrix.hstack(*(Matrix([int(i==q) for q in range(7)]+[int(j==q) for q in range(7)]+[r[i] if j==q else 0 for q in range(7)]) for i,j in D))
assert len(D)==30 and C.rank()==15
def H(j,k,a,b,c):
    h=zeros(30,1)
    for i,v in ((a,r[b]-r[c]),(b,r[c]-r[a]),(c,r[a]-r[b])):
        h[D.index((i,j))]=v
        h[D.index((i,k))]=-v
    return h
n=0
for j,k in combinations(J,2):
    for a,b,c in combinations(range(7),3):
        h=H(j,k,a,b,c)
        assert C*h==zeros(21,1) and sum(bool(v) for v in h)==6
        n+=1
assert n==210
for k in (2,3,4):
    for ports in combinations(J,k):
        cols=[t for t,(_,j) in enumerate(D) if j in ports]
        assert C[:,cols].rank()==2*k+5
    N=2*k+6
    bound=(1 if k==2 else N-(N+k-1)//k-2*(k-1))
    assert bound<=4
    print('ACTIVE_SOURCE_PORTS',k,'MAX_CIRCUIT_ARCS',N,'UPPER_WORD_LENGTH',bound)
Vraw={
(0,0):'219346331/10192753200',(0,1):'7271277/135903376',
(1,1):'29907399/169879220',(5,1):'7271277/339758440',
(1,2):'8057361/169879220',(2,2):'9236487/679516880',
(4,2):'11594739/679516880',(6,2):'196521/67951688',
(2,3):'107583593/679516880',(3,3):'377644447/2548188300',
(4,3):'50199461/679516880',(5,3):'14346033/339758440',
(0,5):'196521/9707384',(6,5):'1375647/19414768',
(6,6):'451274777/3397584400'}
Draw={
(0,1):'1/2',(1,1):'-7/10',(5,1):'1/5',
(1,2):'7/10',(2,2):'-2/5',(4,2):'-4/5',(6,2):'1/2',
(2,3):'2/5',(3,3):'-1',(4,3):'4/5',(5,3):'-1/5',
(0,5):'-1/2',(3,5):'1',(6,5):'-1/2'}
V=Matrix([Q(Vraw.get(a,'0')) for a in D])
d=Matrix([Q(Draw.get(a,'0')) for a in D])
assert C*d==zeros(21,1) and sum(bool(v) for v in d)==14
cert=(-Q(1,2)*H(1,2,0,1,5)+Q(5,9)*H(5,2,0,3,6)
      +2*H(2,3,2,3,4)-Q(2,5)*H(2,3,2,4,5))
assert cert==d
supp=lambda v:[i for i,z in enumerate(v) if z>0]
assert len(supp(V))==C[:,supp(V)].rank()==15 and min(V)>=0
step=min(V[i]/(-d[i]) for i in range(30) if d[i]<0)
assert step==Q(11594739,543613504)
W=V+step*d
U=sorted(set(supp(V))|set(supp(W)))
assert min(W)>=0 and C*V==C*W
assert len(supp(W))==C[:,supp(W)].rank()==15
assert len(U)==16 and C[:,U].rank()==15
def row(j,v):
    return {i:v[D.index((i,j))] for i in range(7)
            if (i,j) in D and v[D.index((i,j))]!=0}
assert [len(row(j,d)) for j in J]==[3,4,4,3]
# Exhaust all three-atom incidence possibilities: lows 1,5 each occur once.
for a,b in ((2,3),(3,2)):
    rem=d.copy()
    for low,hi in ((1,a),(5,b)):
        for i,z in row(low,d).items():
            rem[D.index((i,low))]-=z
            rem[D.index((i,hi))]+=z
    assert not row(1,rem) and not row(5,rem)
    assert row(2,rem)=={i:-z for i,z in row(3,rem).items()}
    assert len(row(2,rem))==5 # one six-edge atom has only 3 targets
print('DICT_ATOMS',n,'EDGE_ENDPOINT_SUPPORTS',len(supp(V)),len(supp(W)))
print('SHARP_EDGE_UNION',len(U),'UNION_RANK',C[:,U].rank())
print('SHARP_EDGE_MINIMUM_WORD_LENGTH',4)
print('PASS_EXACT_R5_SHARP_UNIFORM_ADJACENT_LENGTH_FOUR')
