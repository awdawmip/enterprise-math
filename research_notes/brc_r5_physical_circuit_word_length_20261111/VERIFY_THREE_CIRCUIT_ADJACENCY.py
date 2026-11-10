#!/usr/bin/env python3
"""Exact two-pivot 14 -> 15 -> 15 vertices and a length-three tangent ray.
Frozen R5 scientific inputs: GK a01383f825ef9d43b4b754254303298c64041568;
EM 86149263e38c22292c9def1e0f69092efa1be77e.
All matrices and arithmetic are exact SymPy rationals.
"""
from sympy import Matrix, Rational as Q

R = (2, 10, 15, 20, 25, 30, 38)
r = [Q(z, 20) for z in R]
D = [(i,j) for j in (0,1,2,3,5,6) for i in range(7)
     if j not in (0,6) or i == j]
C = Matrix.hstack(*(Matrix([int(i==k) for k in range(7)]
       + [int(j==k) for k in range(7)]
       + [r[i] if j==k else 0 for k in range(7)]) for i,j in D))
M = {
(0,0):'219346331/10192753200',(0,1):'18669495/951323632',
(1,1):'1898238/8493961',(5,1):'3733899/475661816',
(2,2):'196521/2426846',(0,3):'8057361/237830908',
(2,3):'1544855/16987922',(3,3):'377644447/2548188300',
(4,3):'1544855/16987922',(5,3):'26530335/475661816',
(6,3):'196521/67951688',(0,5):'196521/9707384',
(6,5):'1375647/19414768',(6,6):'451274777/3397584400'
}
x = Matrix([Q(M[a]) if a in M else Q(0) for a in D])
assert C.rank()==15

def supp(v):
    return [i for i,z in enumerate(v) if z>0]

def pivot_at(v,insert_arcs,weights):
    p=supp(v)
    z=[i for i,q in enumerate(v) if q==0]
    pi=list(C[:,p].T.rref()[1])
    assert len(pi)==len(p)
    insert=[D.index(e) for e in insert_arcs]
    assert all(i in z for i in insert)
    old=-C[pi,p].inv()*sum((C[pi,idx]*w for idx,w in zip(insert,weights)),
                            Matrix.zeros(len(p),1))
    d=Matrix.zeros(30,1)
    for idx,w in zip(insert,weights):d[idx]=w
    for idx,w in zip(p,old):d[idx]=w
    assert C*d==Matrix.zeros(21,1)
    assert all(d[k]>=0 for k in z)
    t=min(v[k]/(-d[k]) for k in p if d[k]<0)
    out=v+t*d
    assert min(out)>=0 and C*out==C*v
    assert C[:,supp(out)].rank()==len(supp(out))
    return out,d,t

def H(j,k,a,b,c):
    vec=Matrix.zeros(30,1)
    for i,w in ((a,r[b]-r[c]),(b,r[c]-r[a]),(c,r[a]-r[b])):
        vec[D.index((i,j))]=w
        vec[D.index((i,k))]=-w
    assert C*vec==Matrix.zeros(21,1)
    assert sum(1 if w else 0 for w in vec)==6
    return vec

assert C[:,supp(x)].rank()==len(supp(x))==14
V,d1,t1=pivot_at(x,[(1,2),(4,2)],[Q(1,2),Q(1,4)])
assert len(supp(V))==15
W,d,t2=pivot_at(V,[(3,5)],[Q(1)])
assert len(supp(W))==15
assert sum(1 if u else 0 for u in d)==14
cert=-Q(1,2)*H(1,3,0,1,5)-Q(7,5)*H(2,3,1,2,4)-Q(5,9)*H(3,5,0,3,6)
assert d==cert
union=sorted(set(supp(V))|set(supp(W)))
assert len(union)==16 and C[:,union].rank()==15
assert len(union)-C[:,union].rank()==1
# Any sum of two six-support circuits has support <= 12.
assert sum(1 if u else 0 for u in d)>12
print('OBSERVER_RANK',C.rank())
print('START_VERTEX_SUPPORT',len(supp(x)),'START_RANK',C[:,supp(x)].rank())
print('FIRST_INSERTED_ARCS',[(1,2),(4,2)],'WEIGHTS',(Q(1,2),Q(1,4)),'STEP',t1)
print('INTERMEDIATE_VERTEX_SUPPORT',len(supp(V)),'RANK',C[:,supp(V)].rank())
print('SECOND_INSERTED_ARC',(3,5),'STEP',t2)
print('FINAL_VERTEX_SUPPORT',len(supp(W)),'RANK',C[:,supp(W)].rank())
print('ADJACENCY_UNION_SUPPORT',len(union),'UNION_RANK',C[:,union].rank(),
      'FACE_DIM',len(union)-C[:,union].rank())
print('TANGENT_DIRECTION_SUPPORT',sum(1 if u else 0 for u in d))
print('EXACT_THREE_CIRCUIT_IDENTITY',
      '-1/2 H(1,3;0,1,5) -7/5 H(2,3;1,2,4) -5/9 H(3,5;0,3,6)')
print('EXACT_MINIMUM_K23_WORD_LENGTH',3)
print('INTERMEDIATE_POSITIVE_ARCS',[(D[i],str(V[i])) for i in supp(V)])
print('EDGE_DIRECTION_NONZERO',[(D[i],str(d[i])) for i in range(len(D)) if d[i]])
print('PASS_EXACT_R5_ADJACENT_EDGE_RAY_WORD_LENGTH_THREE')
