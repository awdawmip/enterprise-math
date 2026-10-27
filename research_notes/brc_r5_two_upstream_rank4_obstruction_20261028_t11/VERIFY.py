"""Exact, restricted-policy BRC likelihood-ratio collision witness (six strictly positive leaves)."""
from fractions import Fraction as F
from itertools import product

def q(a,b=1): return F(a,b)

# (time-one branch, time-two outcome, time-three class, P mass, Q mass, terminal R)
leaves = [
    ('A','C','low',q(1,24),q(1,12),q(1,2)),
    ('A','C','high',q(1,8),q(1,12),q(3,2)),
    ('A','L','-',q(1,12),q(1,3),q(1,4)),
    ('B','C','low',q(1,32),q(1,8),q(1,4)),
    ('B','C','high',q(7,32),q(1,8),q(7,4)),
    ('B','H','-',q(1,2),q(1,4),q(2)),
]
assert sum(z[3] for z in leaves)==sum(z[4] for z in leaves)==1
assert all(p>0 and qv>0 and p==qv*r for _,_,_,p,qv,r in leaves)
for g,r in [('A',q(1,2)),('B',q(3,2))]:
    P=sum(z[3] for z in leaves if z[0]==g)
    Q=sum(z[4] for z in leaves if z[0]==g)
    assert P==r*Q
assert sum(z[3] for z in leaves if z[0]=='A' and z[1]=='C')==q(1,6)
assert sum(z[3] for z in leaves if z[0]=='B' and z[1]=='C')==q(1,4)

def obs(xA,xB,yA,yB):
    result=[q(0),q(0),q(0),q(0)]
    for g,g2,term,p,qv,r in leaves:
        x=xA if g=='A' else xB
        y=yA if g=='A' else yB
        if x==0: tau=1; decision='P'
        elif g2!='C' or y==0: tau=2; decision='P'
        else: tau=3; decision='Q' if term=='low' else 'P'
        if decision=='Q': result[0]+=p
        if decision=='P': result[1]+=qv
        result[2]+=p*tau;result[3]+=qv*tau
    return tuple(result)

def add(*vectors):return tuple(map(sum,zip(*vectors)))
def neg(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(t*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))

def determinant(M):
    A=[list(row) for row in M];ans=q(1);n=len(A)
    for c in range(n):
        j=next((i for i in range(c,n) if A[i][c]),None)
        if j is None:return q(0)
        if j!=c:A[c],A[j]=A[j],A[c];ans=-ans
        pivot=A[c][c];ans*=pivot
        for i in range(c+1,n):
            factor=A[i][c]/pivot
            for k in range(c,n):A[i][k]-=factor*A[c][k]
    return ans

def inverse_map(M,b):
    A=[list(row)+[bv] for row,bv in zip(M,b)];n=len(A)
    for c in range(n):
        pivot=next(i for i in range(c,n) if A[i][c])
        A[c],A[pivot]=A[pivot],A[c]
        t=A[c][c];A[c]=[v/t for v in A[c]]
        for i in range(n):
            if i!=c:
                t=A[i][c];A[i]=[a-t*b for a,b in zip(A[i],A[c])]
    return tuple(row[-1] for row in A)

O0=obs(0,0,0,0)
UA=neg(obs(1,0,0,0),O0)
UB=neg(obs(0,1,0,0),O0)
VA=neg(obs(1,0,1,0),obs(1,0,0,0))
VB=neg(obs(0,1,0,1),obs(0,1,0,0))
M=[tuple(v[i] for v in (UA,UB,VA,VB)) for i in range(4)]
det=determinant(M)
assert O0==(q(0),q(1),q(1),q(1))
assert (UA,UB,VA,VB)==(
    (q(0),q(0),q(1,4),q(1,2)),
    (q(0),q(0),q(3,4),q(1,2)),
    (q(1,24),-q(1,12),q(1,6),q(1,6)),
    (q(1,32),-q(1,8),q(1,4),q(1,4)),
)
assert det==q(1,1536)
# Multi-affine identity verifies the decision-tree formula at all 16 vertices.
for a,b,ya,yb in product((0,1),repeat=4):
    rhs=add(O0,mul(UA,a),mul(UB,b),mul(VA,a*ya),mul(VB,b*yb))
    assert obs(a,b,ya,yb)==rhs

lr=[obs(a,b,y,y) for a,b,y in product((0,1),repeat=3)]
full=[obs(a,b,ya,yb) for a,b,ya,yb in product((0,1),repeat=4)]
lam=(-80,-32,0,-2)
assert tuple(dot(lam,v) for v in (UA,UB,VA,VB))==(-1,-1,-1,1)
min_lr=min(map(lambda v:dot(lam,v),lr))
min_full=min(map(lambda v:dot(lam,v),full))
assert min_lr==-36 and min_full==-37 and min_lr-min_full==1
full_witness=obs(1,1,1,0)
assert dot(lam,full_witness)==-37

T=mul(add(obs(1,0,1,0),obs(0,1,0,0)),q(1,2))
assert T==(q(1,48),q(23,24),q(19,12),q(19,12))
coeff=inverse_map(M,neg(T,O0))
assert coeff==(q(1,2),q(1,2),q(1,2),q(0))
assert q(1,2)*q(1)!=q(0) # x_A*y=1/2 forces y=1, contradicting x_B*y=0.

def fmt(v):return '('+', '.join(map(str,v))+')'
print('Leaves:',len(leaves),'all P/Q positive, normalized, exact likelihood ratios')
print('O0:',fmt(O0))
print('UA:',fmt(UA),' UB:',fmt(UB))
print('VA:',fmt(VA),' VB:',fmt(VB))
print('det[UA UB VA VB]:',det)
print('dual lambda:',fmt(lam),' coefficients:',fmt(tuple(dot(lam,v) for v in (UA,UB,VA,VB))))
print('restricted deterministic full/LR policy tables:',len(full),len(lr))
print('min J_full / min J_LR:',min_full,min_lr,'exact separation:',min_lr-min_full)
print('full support witness:',fmt(full_witness))
print('LR midpoint T:',fmt(T),'coordinate inverse:',fmt(coeff))
print('ALL EXACT CHECKS PASSED')
