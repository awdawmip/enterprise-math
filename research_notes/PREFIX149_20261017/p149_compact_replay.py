"""Standalone PREFIX-149 dense-edge no-go certificate; Python 3, exact integers.
Does not import inherited PREFIX-143–148 certificates. All output counts are exact.
"""
from itertools import product, combinations
from collections import Counter

v3 = [p for p in product(range(9), repeat=3) if sum(p) == 8]
b3 = [p for p in v3 if sum(x>0 for x in p)<=2]
f3 = [p for p in v3 if min(p)>0]
t3 = [p for p in product(range(17), repeat=3) if sum(p)==16]
assert (len(v3),len(b3),len(f3),len(t3))==(45,24,21,153)
idx3={p:i for i,p in enumerate(t3)}
def m3(A,B):
    result=0
    for a in A:
        for b in B:
            result|=1<<idx3[tuple(x+y for x,y in zip(a,b))]
    return result
all3=(1<<153)-1
face_bins={}
edge3=[p for p in b3 if sum(x>0 for x in p)==2]
for r in (0,1,2):
    bins=Counter()
    for rem in combinations(edge3,r):
        B=tuple(p for p in b3 if p not in rem)
        base=m3(B,B)
        if base==all3: k=0
        elif any((base|m3((f,),B)|m3((f,),(f,)))==all3 for f in f3): k=1
        elif any((base|m3((f,g),B)|m3((f,g),(f,g)))==all3 for f,g in combinations(f3,2)): k=2
        else: k=3  # means >=3, not exactly 3
        assert k>=r
        bins[k]+=1
    face_bins[r]=dict(sorted(bins.items()))
assert face_bins=={0:{0:1},1:{1:6,2:9,3:6},2:{2:24,3:186}}
print('FACET',face_bins)

ED=tuple(combinations(range(4),2))
def splits(n):
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                yield (a,b,c,n-a-b-c)
def pairs(e,h,t):
    return (e[0]*e[5]+e[1]*e[4]+e[2]*e[3]
            +sum(e[k]*(h[i]+h[j]) for k,(i,j) in enumerate(ED))
            +sum(h[i]*h[j] for i,j in ED)+sum(h)
            +t*(53-t)+t*(t+1)//2)
support={}
for D in (0,1,2):
    for t in range(8+D):
        htot=7+D-t; high=0
        for ds in product(range(D+1),repeat=6):
            if sum(ds)!=D: continue
            e=[7-d for d in ds]
            for h in splits(htot): high=max(high,pairs(e,h,t))
        support[D,t]=high
assert (max(support[0,t] for t in range(6)),
        max(support[1,t] for t in range(5)),
        max(support[2,t] for t in range(4)))==(447,438,430)
print('SUPPORT_LOWT', {D:max(support[D,t] for t in range((6,5,4)[D])) for D in (0,1,2)})

v4=[p for p in product(range(9),repeat=4) if sum(p)==8]
core=[p for p in v4 if sum(x>0 for x in p)<=2]
edge=[p for p in core if sum(x>0 for x in p)==2]
face=[p for p in v4 if sum(x>0 for x in p)==3]
full=[p for p in v4 if min(p)>0]
t4=[p for p in product(range(1,17),repeat=4) if sum(p)==16]
assert (len(v4),len(core),len(edge),len(face),len(full),len(t4))==(165,46,42,84,35,455)
idx4={p:i for i,p in enumerate(t4)}
def m4(A,B):
    res=0
    for a in A:
        for b in B:
            k=idx4.get(tuple(x+y for x,y in zip(a,b)))
            if k is not None: res|=1<<k
    return res
result={}
for D in (0,1,2):
    cmax=fmax=umax=0; tested=0
    for rem in combinations(edge,D):
        B=tuple(p for p in core if p not in rem)
        baseline=m4(B,B);c=baseline.bit_count()
        f=max((m4((q,),B)&~baseline).bit_count() for q in face)
        u=max((m4((q,),B)&~baseline).bit_count() for q in full)
        cmax=max(cmax,c);fmax=max(fmax,f);umax=max(umax,u)
        tested+=1
    result[D]=(cmax,fmax,umax,tested)
assert result=={0:(127,17,40,1),1:(122,18,40,42),2:(118,19,40,861)}
print('RELAX_COMPONENTS',result)
for D,ts in ((0,(6,7)),(1,(5,6)),(2,(4,5))):
    C,F,U,_=result[D]
    for t in ts:
        h=7+D-t
        cap=C+h*F+h*(h-1)//2+t*(U+h)+t*(t+1)//2
        assert cap<455
        print('REMAINING',D,t,h,'UPPER',cap)
print('P149_SELF_CONTAINED_UNCONDITIONAL_PASS')
