from fractions import Fraction as F
from itertools import product, combinations
from math import gcd
from functools import reduce

r=(F(1,2),F(1),F(3,2))
qrows=((F(1,4),F(1,2),F(1,4)),(F(1,3),)*3)
prows=tuple(tuple(x*y for x,y in zip(r,row)) for row in qrows)
assert all(sum(q)==sum(p)==1 and min(q+p)>0 for q,p in zip(qrows,prows))
assert all(prows[h][j]/qrows[h][j]==r[j] for h in (0,1) for j in range(3))
assert qrows[0]!=qrows[1]
q={(h,j):qrows[h][j]/2 for h in (0,1) for j in range(3)}
p={(h,j):prows[h][j]/2 for h in (0,1) for j in range(3)}
Q=[sum(q[h,j] for h in (0,1)) for j in range(3)]
P=[sum(p[h,j] for h in (0,1)) for j in range(3)]
assert Q==[F(7,24),F(5,12),F(7,24)]

def history(root,acts,terminal):
    if root!='C':return (F(root=='Q'),F(root=='P'),F(0))
    a=b=F(0);t=F(1)
    for h,act in enumerate(acts):
        if act=='P':b+=F(1,2)
        elif act=='Q':a+=F(1,2)
        else:
            t+=F(1,2)
            for j in range(3):
                if terminal[3*h+j]=='Q':a+=p[h,j]
                else:b+=q[h,j]
    return a,b,t

def lr(root,act,terminal):
    if root!='C':return (F(root=='Q'),F(root=='P'),F(0))
    if act!='C':return (F(act=='Q'),F(act=='P'),F(1))
    return (sum((P[j] for j in range(3) if terminal[j]=='Q'),F(0)),
            sum((Q[j] for j in range(3) if terminal[j]=='P'),F(0)),F(2))

H={history(rt,ac,te) for rt in 'PQC' for ac in product('PQC',repeat=2)
   for te in product('PQ',repeat=6)}
T={lr(rt,ac,te) for rt in 'PQC' for ac in 'PQC' for te in product('PQ',repeat=3)}
assert len(H)==85 and len(T)==12
vec=sorted(tuple(int(48*x) for x in v) for v in T)
allhist=[tuple(int(48*x) for x in v) for v in H]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
facets=set()
for a,b,c in combinations(vec,3):
    n=cross(tuple(y-x for x,y in zip(a,b)),tuple(y-x for x,y in zip(a,c)))
    if n==(0,0,0):continue
    d=dot(n,a)
    signs=[dot(n,v)-d for v in vec]
    if min(signs)<0<max(signs) or min(signs)==max(signs)==0:continue
    if min(signs)<0:n=tuple(-x for x in n);d=-d
    g=reduce(gcd,(*map(abs,n),abs(d)))
    facets.add(tuple(x//g for x in n)+(d//g,))
expected={(-96,-96,7,-4608),(-2,-3,0,-144),(-2,-1,0,-96),
          (0,0,-1,-96),(2,1,0,48),(2,3,0,96),(96,96,7,4608)}
assert facets==expected
assert all(dot(f[:3],v)>=f[3] for f in facets for v in allhist)

w=history('C',('C','P'),('Q','P','P','P','P','P'))
compressed=(F(1,2)*P[0]*F(6,7),
            F(1,2)+F(1,2)*(1-Q[0]*F(6,7)),F(3,2))
assert w==compressed==(F(1,16),F(7,8),F(3,2))
assert tuple(q[0,j]-F(1,2)*Q[j] for j in range(3))==(F(-1,48),F(1,24),F(-1,48))

def bellman(A,B,C,D):
    g=C+D; fn=lambda x:min(A*x,B);m=fn(F(1))
    fs=[sum((row[j]*fn(r[j]) for j in range(3)),F(0)) for row in qrows]
    full=min(m,g+sum((min(m,g+fs[h])/2 for h in (0,1)),F(0)))
    quotient=min(m,g+min(m,g+sum(fs,F(0))/2))
    return full,quotient
for weights in product((-2,-1,0,1,2),repeat=4):
    a,b=bellman(*map(F,weights));assert a==b,(weights,a,b)
print('POSITIVE LR-MINIMAL NONLUMPABLE MODEL: PASS')
print('1728 full deterministic tables, 85 distinct observer vectors: PASS')
print('72 LR deterministic tables, 12 distinct observer vectors: PASS')
print('7 exact 3D convex-hull facets, all 85 vectors contained: PASS')
print('625 signed real-linear integer-coefficient cross-checks: PASS')
print('Witness O=(1/16,7/8,3/2,3/2), nonzero Q defect=(-1/48,1/24,-1/48): PASS')
print('Universal quantifier requires accompanying analytical support and convexity proof.')
