"""R749SMC: exact source history quotient for finite Walsh-character public controllers."""
from fractions import Fraction as Q
from itertools import product
from math import prod
import json

def xor_rank(vectors):
    basis=[]
    for v in vectors:
        x=v
        for b in basis:x=min(x,x^b)
        if x:
            basis.append(x)
            basis.sort(reverse=True)
    return len(basis)

def character(mask,z):
    return prod(z[i] for i in range(len(z)) if mask&(1<<i))

def row_rank(M):
    if not M:return 0
    a=[list(map(Q,row)) for row in M]
    r=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        v=a[r][j]
        for t in range(j,len(a[0])):a[r][t]/=v
        for i in range(r+1,len(a)):
            k=a[i][j]
            for t in range(j,len(a[0])):a[i][t]-=k*a[r][t]
        r+=1
        if r==len(a):break
    return r

def check(d,vectors):
    h=len(vectors)
    Z=list(product((-1,1),repeat=d))
    A=list(product((-1,1),repeat=h))
    M=[[prod(Q(2+a[i]*character(vectors[i],z),4) for i in range(h)) for z in Z] for a in A]
    r=xor_rank(vectors)
    assert row_rank(M)==2**r
    assert all(sum(row[j] for row in M)==1 for j in range(len(Z)))
    def fiber(z):return tuple(character(v,z) for v in vectors)
    assert len(set(map(fiber,Z)))==2**r
    for i,z in enumerate(Z):
        for j,z2 in enumerate(Z):
            identical=all(row[i]==row[j] for row in M)
            assert identical==(fiber(z)==fiber(z2))
    for subset in range(1<<h):
        v=0
        for i in range(h):
            if subset>>i&1:v^=vectors[i]
        for j,z in enumerate(Z):
            lhs=sum(M[k][j]*prod(a[i] for i in range(h) if subset>>i&1) for k,a in enumerate(A))
            rhs=Q(character(v,z),2**subset.bit_count())
            assert lhs==rhs
    return r

counts={}
for d,maxh in [(1,3),(2,3),(3,3)]:
    count=0;rs=set()
    for h in range(maxh+1):
        for vec in product(range(1<<d),repeat=h):
            r=check(d,vec)
            rs.add(r);count+=1
    counts[str(d)]={"sequences_checked":count,"ranks_observed":sorted(rs)}

for d in (4,5):
    cases=[(),(0,),(1,),(1,1),(1,2),(1,2,3),(1,2,4),(1,2,4,8),
           (1,2,4,8,16)[:d],(3,5,6,3),(0,1,0,2)]
    for case in cases:
        assert all(v<(1<<d) for v in case)
        check(d,case)
    counts[str(d)]={"sequences_checked":len(cases),"tested_rank_deficiency":True}
print(json.dumps({"status":"PASS","arithmetic":"Fraction","exact_formula":"rank=2^rank_GF2(v_i)",
  "point_equivalence":"equal all declared signed-Walsh characters",
  "quotient_fiber_size":"2^(d-r)","cases":counts,"native_event_permission":False},sort_keys=True))
