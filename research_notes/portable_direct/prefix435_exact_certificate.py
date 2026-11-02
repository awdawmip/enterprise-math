"""PREFIX-435 nine-channel tomography: exact Fraction-only certificate."""
from fractions import Fraction as Q
F = lambda a=0,b=0: (Q(a),Q(b))
def mul(x,y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def phase(k): return (F(1),F(0,1),F(-1),F(0,-1))[k%4]
def square(x): return mul(x,conj(x))[0]
def coeff(c):
    r=[square(x) for x in c]
    for i,j in ((0,1),(0,2),(1,2)):
        z=mul(c[i],conj(c[j]));r.extend((2*z[0],-2*z[1]))
    return r
def rankdet(a):
    a=[list(x) for x in a];p=0;d=Q(1)
    for j in range(len(a[0])):
        k=next((k for k in range(p,len(a)) if a[k][j]),None)
        if k is None: continue
        if k!=p: a[p],a[k]=a[k],a[p];d=-d
        t=a[p][j];d*=t;a[p]=[x/t for x in a[p]]
        for k in range(p+1,len(a)):
            s=a[k][j]
            if s: a[k]=[x-s*y for x,y in zip(a[k],a[p])]
        p+=1
    return p,d if p==len(a) else Q(0)
def intensity(c,x):
    t=F()
    for a,b in zip(c,x):t=add(t,mul(a,b))
    return square(t)
A=F(Q(11,4),Q(15,8)); B=F(Q(5,4),Q(9,4))
Z=F(); O=F(1)
base=[(Z,O,Z),(O,O,Z),(Z,Z,O),(O,Z,O),(A,A,B)]
tags=((0,1),(1,0),(1,1),(1,2))
added=[(A,mul(A,phase(a)),mul(B,phase(b))) for a,b in tags]
assert rankdet([coeff(c) for c in base])[0]==5
r,d=rankdet([coeff(c) for c in base+added])
assert r==9 and d==Q(1001129928661,65536)
v=F(Q(1,2000),-Q(123,490000))
yplus=[intensity(c,(O,F(0,1),v)) for c in base+added]
yminus=[intensity(c,(O,F(0,-1),v)) for c in base+added]
assert yplus[:5]==yminus[:5] and yplus[5:]!=yminus[5:]
print('PASS_PREFIX435_EXACT_FRACTION_TOMOGRAPHY')
print('base_rank=5 augmented_rank=9 determinant=',d)
print('tags=',tags,'original_collision_repaired=True')
