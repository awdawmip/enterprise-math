#!/usr/bin/env python3
"""EC49DS: exact signed-X6 10-step history-feature certificate (stdlib)."""
import json
from fractions import Fraction
D=(-2,0,0,0,0,0)
Z={(1,0,0,0,0,0),(0,1,0,0,0,0),(0,0,1,0,0,0),
   (0,0,0,1,0,0),(0,1,0,0,1,0),(0,0,1,0,0,1)}

def obs(w):
    d=[0]*6;p=[0]*6;a=b=last=0
    for s in w:
        j=abs(s)-1;d[j]+=1 if s>0 else -1
        if s>0:p[j]+=1
        a=int(a or (last==1 and s==2));b=int(b or (last==2 and s==1))
        last=s if s in (1,2) else 0
    z=(int(not a and not b),int(not a and b),int(a and not b),
       int(a and b),int(not a and last==1),int(not b and last==2))
    return tuple(d),tuple(p),z

def comps(n,k):
    if k==1:yield (n,)
    else:
        for i in range(n+1):
            for t in comps(n-i,k-1):yield (i,)+t

def reach(p):
    q=tuple(c+(2 if j==0 else 0) for j,c in enumerate(p))
    states={(p,q,0,0,0):()}
    for _ in range(10):
        nxt={}
        for (v,q,a,b,last),w in states.items():
            for j in range(6):
                for s in (j+1,-j-1):
                    vv=list(v);qq=list(q)
                    if s>0:
                        if not vv[j]:continue
                        vv[j]-=1
                    else:
                        if not qq[j]:continue
                        qq[j]-=1
                    aa=int(a or (last==1 and s==2));bb=int(b or (last==2 and s==1))
                    ll=s if s in (1,2) else 0
                    nxt.setdefault((tuple(vv),tuple(qq),aa,bb,ll),w+(s,))
        states=nxt
    out={}
    for w in states.values():
        d,pp,z=obs(w)
        assert d==D and pp==p and len(w)==10
        out.setdefault(z,w)
    return out

def wt(p,x):
    v=1
    for n,a in zip(p,x):v*=a**n
    return v

def rank(rows):
    basis={}
    for row in rows:
        v=[Fraction(a) for a in row]
        for j,b in sorted(basis.items()):
            t=v[j]
            if t:v=[a-t*c for a,c in zip(v,b)]
        j=next((i for i,a in enumerate(v) if a),None)
        if j is not None:
            t=v[j];basis[j]=[a/t for a in v]
    return len(basis)

C={(1,3,0,0,0,0),(2,2,0,0,0,0),(3,1,0,0,0,0)}
for j in range(2,6):
    for a,b in ((1,2),(2,1)):
        p=[0]*6;p[0]=a;p[1]=b;p[j]=1;C.add(tuple(p))
C=sorted(C)
H={(p,z):w for p in comps(4,6) for z,w in reach(p).items()}
assert len(H)==333 and len(C)==11 and all((p,z) in H for p in C for z in Z)

def checked(x,y):
    g=rank([(wt(p,x),wt(p,y),1) for p in C])
    m=rank([tuple(wt(p,x)*a for a in z)+tuple(wt(p,y)*a for a in z)+z for p,z in H])
    assert (g==3)==(m==18)
    return (g,m)

T=[
 ('generic',(2,3,1,4,5,6),(3,5,7,4,6,9),18),
 ('y1_eq_y2',(2,3,1,4,5,6),(7,7,11,7,7,7),18),
 ('y_constant',(2,3,1,4,5,6),(7,)*6,12),
 ('x1_eq_x2',(2,2,4,5,6,7),(3,5,3,5,3,5),18),
 ('x_constant',(2,)*6,(3,5,3,5,3,5),12),
 ('front_proportional',(2,3,1,4,5,6),(4,6,2,8,11,12),18),
 ('proportional',(2,3,1,4,5,6),(4,6,2,8,10,12),12),
 ('equal_core_noncollinear',(2,2,1,2,3,4),(3,3,2,4,6,8),18),
 ('equal_core_collinear',(2,2,1,2,3,4),(5,5,3,5,7,9),17),
 ('all_equal',(2,)*6,(3,)*6,6)]
out=[]
for name,x,y,expected in T:
    g,r=checked(x,y)
    assert r==expected
    out.append({'case':name,'rank_G11':g,'rank_M333':r})
print(json.dumps({'status':'PASS','positive_count_vectors':126,'reachable_states':len(H),
 'core_count_vectors':len(C),'verified_core_native_words':len(C)*len(Z),'cases':out,
 'core_witnesses':[{'p':p,'z':z,'w':H[p,z]} for p in C for z in sorted(Z)]},sort_keys=True))
