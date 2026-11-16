#!/usr/bin/env python3
"""R650: exact signed PF10 two-cell observer quotient and 19-rank certificate."""
from itertools import combinations, product
from fractions import Fraction
import json

PORTS=range(4)
CELLS=('x','y')
PAIRS=tuple(combinations(PORTS,2))
TRIADS=tuple(combinations(range(6),3))
MATCHINGS=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
def code(s,m):
    z=set(s)
    if any((a in z)+(b in z)!=1 for a,b in m):return 0
    return 1 if sum(b in z for a,b in m)%2==0 else -1
C={s:tuple(code(s,m) for m in MATCHINGS) for s in TRIADS}
NEI={s:tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
assert len(set(C.values()))==20

def fresh():
    return {c:{'M':[[0]*4 for _ in PORTS],'ri':[0]*4,'ro':[0]*4} for c in CELLS}
def signed(L):
    result={}
    for c in CELLS:
        m=L[c]['M'];om=tuple(m[i][j]-m[j][i] for i,j in PAIRS)
        d=tuple(L[c]['ri'][i]-L[c]['ro'][i] for i in PORTS)
        result[c]=(om,d)
    return result
def full_u_om(L,c):
    m=L[c]['M'];u=tuple(sum(m[i])-sum(m[j][i] for j in PORTS)+L[c]['ri'][i]-L[c]['ro'][i] for i in PORTS)
    o=tuple(tuple(m[i][j]-m[j][i] for j in PORTS) for i in PORTS)
    return u,o
def compressed19(r):
    return r['x'][0]+r['y'][0]+r['x'][1]+r['y'][1][:3]
def decode19(z):
    assert len(z)==19
    dx=z[12:16];dy3=z[16:19]
    return {'x':(z[:6],dx),'y':(z[6:12],dy3+(-sum(dx)-sum(dy3),))}
def from_reduced(om,d):
    o=[[0]*4 for _ in PORTS]
    for (i,j),v in zip(PAIRS,om):o[i][j]=v;o[j][i]=-v
    return tuple(sum(o[i])+d[i] for i in PORTS),tuple(map(tuple,o))
def score(s,t,u,o):
    return sum(u[i]*C[t][i] for i in PORTS)+sum(C[s][i]*o[i][j]*C[t][j] for i in PORTS for j in PORTS)
def update(L,r,e):
    typ,c,a,other,b=e
    if typ=='P':L[c]['M'][a][b]+=1
    else:L[c]['ro'][a]+=1;L[other]['ri'][b]+=1
    if typ=='P':
        i,j=sorted((a,b));sgn=1 if a==i else -1
        v=list(r[c][0]);v[PAIRS.index((i,j))]+=sgn;r[c]=(tuple(v),r[c][1])
    else:
        dc=list(r[c][1]);do=list(r[other][1]);dc[a]-=1;do[b]+=1
        r[c]=(r[c][0],tuple(dc));r[other]=(r[other][0],tuple(do))
def rank(A):
    A=[[Fraction(z) for z in row] for row in A]
    i=0
    for j in range(len(A[0])):
        k=next((k for k in range(i,len(A)) if A[k][j]),None)
        if k is None:continue
        A[i],A[k]=A[k],A[i]
        v=A[i][j];A[i]=[z/v for z in A[i]]
        for h in range(i+1,len(A)):
            v=A[h][j]
            if v:A[h]=[a-v*b for a,b in zip(A[h],A[i])]
        i+=1
        if i==len(A):break
    return i
EV=[]
for c in CELLS:
    for a,b in PAIRS:EV.append(('P',c,a,None,b))
for c,other in (('x','y'),('y','x')):
    for a in PORTS:
        for b in PORTS:EV.append(('T',c,a,other,b))
cols=[]
for e in EV:
    L=fresh();r={c:((0,)*6,(0,)*4) for c in CELLS};update(L,r,e)
    cols.append(list(r['x'][0]+r['y'][0]+r['x'][1]+r['y'][1]))
assert len(cols)==44
R=rank(list(zip(*cols)))
assert R==19
ALPH=(('P','x',0,None,1),('P','x',1,None,0),('P','y',2,None,3),
      ('T','x',0,'y',1),('T','y',2,'x',3),('P','x',3,None,2))
words=steps=scores=0
for n in range(5):
    for word in product(ALPH,repeat=n):
        words+=1;L=fresh();r={c:((0,)*6,(0,)*4) for c in CELLS}
        for e in word:
            update(L,r,e);steps+=1
            for c in CELLS:
                assert r[c]==signed(L)[c]
                assert decode19(compressed19(r))==r
                u,o=full_u_om(L,c)
                assert (u,o)==from_reduced(*r[c])
                for s in TRIADS:
                    for t in NEI[s]:
                        assert score(s,t,u,o)==score(s,t,*from_reduced(*r[c]))
                        scores+=1
            assert sum(sum(full_u_om(L,c)[0]) for c in CELLS)==0
assert words==1555
print(json.dumps({'marker':'R650_SIGNED_PF10_19_COORDINATE_FUTURE_QUOTIENT_PASS',
 'source':'V29/V27/V17@b62110008321d9147212cb89f2627ff613c2550d',
 'science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
 'linear_observer_rank':R,'primitive_generator_count':len(EV),
 'compressed_integer_coordinate_count':19,'reconstruction':'delta_y[3]=-sum(delta_x)-sum(delta_y[0:3])',
 'event_words':words,'event_updates':steps,'score_equalities':scores,
 'expected_rank':12+7, 'global_transfer_boundary_sum':0,
 'coverage':'all length 0..4 words over declared six event labels; every 20 triad and nine neighbor scores at every prefix; exact integers',
 'status':'author-side exact auxiliary model; formal CLAIM/independent Driver not asserted'},indent=2))
