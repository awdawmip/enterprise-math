"""Exact Fraction regression checks for R5 sharper seedless-LR four-cube."""
from fractions import Fraction as F
from itertools import product
q3=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
r1=(F(3,4),F(5,4));r3=(F(1,2),F(1),F(3,2))
alpha,beta=F(47,180),F(67,162)
R=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
M0=F(3761,96000)
H=9*M0/(40+F(9,25))
C=(F(1,2),F(1,4),F(1,4),F(27,640),F(13,320),F(27,640))

def capacities(u0,u1):
    return tuple((u0*q3[0][j]+u1*q3[1][j])/2 for j in range(3))

def time(x):
    g,u0,u1,x0,x1,x2=x
    return (1+g+(3*u0+5*u1)/8+x0/2+x1+3*x2/2,
            1+g+(u0+u1)/2+x0+x1+x2)

def mass(x):
    g,u0,u1,x0,x1,x2=x
    A,B=u0/10,9*u1/40
    J=x1*(alpha*A+beta*B)/(A+B) if A+B else F(0)
    V=capacities(u0,u1)
    m={r:F(0) for r in R}
    m[F(1)]+=1-g
    for i,u in enumerate((u0,u1)):m[r1[i]]+=(g-u)/2
    for j in range(3):m[r3[j]]+=V[j]-x[j+3]
    m[F(1,10)]+=(509*x0+9*x2)/900+J
    m[F(1)]+=F(382,900)*(x0+x2)+x1-2*J
    m[F(19,10)]+=(9*x0+509*x2)/900+J
    assert min(m.values())>=0
    assert sum(m.values())==1 and sum(r*v for r,v in m.items())==1
    return m

def witness(Ep,Eq,Tp,Tq):
    a,b=Tp-F(15,8),Tq-F(15,8)
    c,d=Ep-F(1,2),Eq-F(1,2)
    g=F(1,2)+3*b-2*a
    x=(g,F(1,4),F(1,4),F(27,640),F(13,320),F(27,640)+2*(a-b))
    assert x[1]<=g<=1 and x[2]<=g
    assert all(0<=v<=cap for v,cap in zip(x[3:],capacities(x[1],x[2])))
    m=mass(x)
    assert m[F(1,10)]==M0+(a-b)/50
    s=10*(c+d)/(9*m[F(1,10)])
    r=-(10*c+d)/(9*m[F(1)])
    t={v:F(1,2) for v in R}
    t[F(1,10)]+=s;t[F(1)]+=r
    assert all(0<=p<=1 for p in t.values())
    ep=1-sum(key*m[key]*t[key] for key in R)
    eq=sum(m[key]*t[key] for key in R)
    assert (ep,eq)==(Ep,Eq) and time(x)==(Tp,Tq)
    return x,m,t

assert all(sum(row)==1 for row in q3)
assert all(sum(q3[i][j]*r3[j] for j in range(3))==r1[i] for i in (0,1))
assert capacities(C[1],C[2])==(F(27,320),F(13,160),F(27,320))
assert time(C)==(F(15,8),F(15,8)) and mass(C)[F(1,10)]==M0
assert H==F(11283,1291520) and F(1,148)<H<F(27,2560)
assert H<F(1,20) and H<F(9,134)
assert 40*H==9*(M0-H/25)
checks=0
for vals in product((-2,-1,0,1,2),repeat=4):
    ds=[H*F(v,2) for v in vals]
    witness(F(1,2)+ds[0],F(1,2)+ds[1],F(15,8)+ds[2],F(15,8)+ds[3])
    checks+=1
corners=0;sat=False
for vals in product((-1,1),repeat=4):
    ds=[H*v for v in vals]
    x,m,t=witness(F(1,2)+ds[0],F(1,2)+ds[1],F(15,8)+ds[2],F(15,8)+ds[3])
    corners+=1
    if t[F(1,10)] in (F(0),F(1)):sat=True
assert corners==16 and sat
higher=F(1,114)
a,b,c,d=-higher,higher,higher,higher
x=(F(1,2)+3*b-2*a,F(1,4),F(1,4),F(27,640),F(13,320),F(27,640)+2*(a-b))
assert all(0<=u<=v for u,v in zip(x[3:],capacities(x[1],x[2])))
assert 10*(c+d)/(9*mass(x)[F(1,10)])>F(1,2)
print('radius=',H,'approx=',float(H))
print('previous_radius=',F(1,148),'exact_improvement_factor=',H/F(1,148))
print('ratio_1_10_center_stopped_Q_mass=',M0)
print('exact_5^4_grid_targets=',checks,'exact_corners=',corners)
print('corner_declaration_probability_1_attained=',sat)
print('fixed_controller_sharpness_witness_radius=1/114')
print('PASS_EXACT_R5_SHARPER_FOUR_CUBE_RATIO_ONE_TENTH_KEY')
