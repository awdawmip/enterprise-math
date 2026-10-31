"""R435: exact signed BRC source and all order<=3 minor checks; order4 spot audit."""
from math import comb,gcd
from functools import reduce
from random import Random
from itertools import permutations
import json
from pathlib import Path
R=19
N=R-2
def coefficient(q,r,s):
    return sum(comb(2*s,q-2*j)*comb(r-s,j)
               for j in range(r-s+1) if 0<=q-2*j<=2*s)
def H(r,s):
    return comb(r+s,2*s)*(coefficient(r,r,s)-coefficient(r-1,r,s)) if 2<=s<=r else 0
def cat(k):
    return comb(2*k,k)//(k+1) if k>=0 else 0
def Hc(r,s):
    if not 2<=s<=r:return 0
    k=r//2
    if r%2:
        d=sum(comb(s-1,2*t)*4**t*cat(k-t) for t in range((s-1)//2+1))
    else:
        d=sum(comb(s-1,2*t+1)*2*4**t*cat(k-1-t) for t in range((s-2)//2+1))
    return comb(r+s,2*s)*d
def at(a,j):
    return a[j] if 0<=j<len(a) else 0
def det2(m):return m[0][0]*m[1][1]-m[0][1]*m[1][0]
def det3(m):
    x,y,z=m
    return x[0]*(y[1]*z[2]-y[2]*z[1])-x[1]*(y[0]*z[2]-y[2]*z[0])+x[2]*(y[0]*z[1]-y[1]*z[0])
def det4(m):
    return sum((-1 if j%2 else 1)*m[0][j]*det3([[m[i][q] for q in range(4) if q!=j] for i in range(1,4)]) for j in range(4))
def det5(m):
    res=0
    for p in permutations(range(5)):
        term=1;inversions=0
        for i in range(5):
            term*=m[i][p[i]]
            inversions+=sum(p[i]>p[j] for j in range(i+1,5))
        res+=-term if inversions%2 else term
    return res
raw=[H(R,R-h) for h in range(N+1)]
assert all(v>0 for v in raw)
assert all(H(R,s)==Hc(R,s) for s in range(2,R+1))
g=reduce(gcd,raw)
assert g==2
a=[v//g for v in raw]
assert max(a)<2**44
counts={}
for h in (1,2,3):
    pos=zero=neg=0
    def row_gen(prefix):
        if len(prefix)==h:
            yield tuple(prefix)
        else:
            for delta in range(1,N+1):
                yield from row_gen(prefix+[prefix[-1]+delta])
    def col_gen(rows,prefix):
        t=len(prefix)
        if t==h:
            yield tuple(prefix)
        else:
            lo=max(rows[t],prefix[-1]+1 if prefix else 0)
            for v in range(lo,rows[t]+N+1):
                yield from col_gen(rows,prefix+[v])
    for rows in row_gen([0]):
        for cols in col_gen(rows,[]):
            m=[[at(a,cols[j]-rows[i]) for j in range(h)] for i in range(h)]
            d=(m[0][0] if h==1 else det2(m) if h==2 else det3(m))
            assert d>0,(rows,cols,d)
            pos+=d>0;zero+=d==0;neg+=d<0
    counts[str(h)]={'positive':pos,'zero':zero,'negative':neg,'total':pos+zero+neg}
rng=Random(435019)
spot=0
for _ in range(30000):
    u=[0]
    for i in range(3):
        u.append(u[-1]+rng.randint(1,N))
    v=[u[i]+rng.randint(0,N) for i in range(4)]
    if any(v[i]>=v[i+1] for i in range(3)):
        continue
    assert det4([[at(a,v[j]-u[i])for j in range(4)]for i in range(4)])>0
    spot+=1
a4=[H(4,4-h)for h in range(3)]
a6=[H(6,6-h)for h in range(5)]
assert det3([[at(a4,1+j-i)for j in range(3)]for i in range(3)])==-1568
assert det4([[at(a6,c-i)for c in [1,4,5,6]]for i in [0,1,2,3]])==-4117994496
sval={s:H(R,s) for s in range(2,8)}
E19=det5([[sval.get(3+i-j,0)for j in range(5)]for i in range(5)])
assert E19==-1072490571380901349955734874221287438418464
evidence={'r':R,'gcd':g,'normalized_coefficients':[str(v)for v in a],
          'original_signed_catalan_checks':18,'lower_counts':counts,
          'exact_order4_spot_checks':spot,'negative_r19_order5':str(E19),
          'numeric_model':'Python arbitrary precision integers'}
Path(__file__).with_name('R435_EVIDENCE_LOWER.json').write_text(json.dumps(evidence,indent=2)+'\n')
print('R435_LOWER_EXACT_PASS',counts,'spot4',spot,'gcd',g,'pf5_E19',E19)
