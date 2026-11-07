"""Exact low-dimensional face-stationary tests and R5 scalar-gate spotcheck."""
from fractions import Fraction as Q
from itertools import combinations
import sympy as s

R=s.Rational
def critical_face_values(n, inequalities, equalities, H, c, d=0):
    """a*x<=b, a*x==b; exact small-dimension face enumeration."""
    xs=s.symbols('x:'+str(n)); X=s.Matrix(xs)
    H=s.Matrix(H); c=s.Matrix(c)
    f=(X.T*H*X)[0]/2+(c.T*X)[0]+R(d)
    found=[]
    for k in range(min(n,len(inequalities))+1):
      for chosen in combinations(inequalities,k):
        active=list(equalities)+list(chosen)
        A=s.Matrix([a for a,b in active]) if active else s.zeros(0,n)
        b=s.Matrix([v for a,v in active]) if active else s.zeros(0,1)
        if A.row_join(b).rank()!=A.rank(): continue
        tangent=A.nullspace()
        stationary=[(tuple((t.T*H)[0,:]),-(t.T*c)[0]) for t in tangent]
        eqs=active+stationary
        E=s.Matrix([a for a,b in eqs]) if eqs else s.zeros(0,n)
        y=s.Matrix([b for a,b in eqs]) if eqs else s.zeros(0,1)
        if E.row_join(y).rank()!=E.rank(): continue
        for t in range(min(n,len(inequalities))+1):
          for pin in combinations(inequalities,t):
            all_eq=eqs+list(pin)
            C=s.Matrix([a for a,b in all_eq]) if all_eq else s.zeros(0,n)
            z=s.Matrix([v for a,v in all_eq]) if all_eq else s.zeros(0,1)
            if C.rank()!=n or C.row_join(z).rank()!=n: continue
            sol=C.gauss_jordan_solve(z)[0]
            if all(s.Matrix(a).dot(sol)<=v for a,v in inequalities) and all(s.Matrix(a).dot(sol)==v for a,v in equalities):
                found.append((s.factor(f.subs(dict(zip(xs,sol)))),tuple(sol)))
    assert found
    return min(v for v,p in found),max(v for v,p in found),len(found)

examples=[
 ('triangle-indefinite',2,[((-1,0),0),((0,-1),0),((1,1),1)],[],[[0,1],[1,0]],[0,0],-R(1,8),-R(1,8),R(1,8)),
 ('square-interior-min',2,[((-1,0),0),((0,-1),0),((1,0),1),((0,1),1)],[],[[2,0],[0,2]],[-R(2,3),-R(4,5)],R(1,9)+R(4,25)-R(1,8),-R(1,8),R(4,9)+R(9,25)-R(1,8)),
 ('line-relative-face',2,[((-1,0),0),((0,-1),0)], [((1,1),1)],[[0,1],[1,0]],[0,0],0,R(0),R(1,4)),
 ('quadratic-irrational-zero',1,[((-1,),0),((1,),1)],[],[[2]],[0],-R(1,2),-R(1,2),R(1,2))
]
for label,n,ineq,eq,H,c,d,low,high in examples:
    a,b,count=critical_face_values(n,ineq,eq,H,c,d)
    assert (a,b)==(low,high),(label,a,b,low,high)
    print(label,'min',a,'max',b,'candidate_count',count)

alpha=Q(47,180); beta=Q(67,162); delta=beta-alpha
A=Q(1,10); B=Q(9,40); X=(A+B)/2
low=max(alpha*X,beta*X-delta*A)
high=min(beta*X,alpha*X+delta*B)
shared=alpha*A/2+beta*B/2
F=lambda J:(A+B)*J-X*(alpha*A+beta*B)
assert low<shared<high
assert F(low)==-Q(3211,1296000) and F(high)==Q(3211,1296000) and F(shared)==0
W=(Q(1),Q(0),Q(253,80),Q(253,80))
for J in (low,shared,high):
    V0=Q(1,2)*Q(13,20)+Q(1,2)*Q(1,40)
    V1=A+B
    V2=Q(1,2)*Q(3,20)+Q(1,2)*Q(21,40)
    masses={Q(1,10):J,Q(1,2):V0,Q(1):V1-2*J,Q(3,2):V2,Q(19,10):J}
    assert all(m>=0 for m in masses.values())
    assert sum(masses.values())==1
    assert sum(r*m for r,m in masses.items())==1
    assert W==(Q(1),Q(0),Q(253,80),Q(253,80))
print('R5_extreme_J',low,high,'F',F(low),F(high),'LR_J',shared,'W',W)
print('PASS_EXACT_R5_RATIONAL_QUADRATIC_FACE_STATIONARITY')
