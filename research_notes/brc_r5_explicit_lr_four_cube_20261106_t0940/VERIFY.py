from fractions import Fraction as Q
from itertools import product
F = Q
q3 = ((F(13,20),F(1,5),F(3,20)),
      (F(1,40),F(9,20),F(21,40)))
r1=(F(3,4),F(5,4))
r3=(F(1,2),F(1),F(3,2))
alpha,beta=F(47,180),F(67,162)
C=(F(1,2),F(1,4),F(1,4),F(27,640),F(13,320),F(27,640))
H=F(1,148)

def capacities(u0,u1):
    return tuple((u0*q3[0][j]+u1*q3[1][j])/2 for j in range(3))

def time(x):
    g,u0,u1,x0,x1,x2=x
    return (F(1)+g+(3*u0+5*u1)/8+x0/2+x1+3*x2/2,
            F(1)+g+(u0+u1)/2+x0+x1+x2)

def stopped_mass(x):
    g,u0,u1,x0,x1,x2=x
    V=capacities(u0,u1)
    A,B=u0/10,9*u1/40
    J=x1*(alpha*A+beta*B)/(A+B)
    m={r:F(0) for r in (F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))}
    m[F(1)]+=1-g
    for i,u in enumerate((u0,u1)):m[r1[i]]+=(g-u)/2
    for j in range(3):m[r3[j]]+=V[j]-x[j+3]
    m[F(1,10)]+=(509*x0+9*x2)/900+J
    m[F(1)]+=F(382,900)*(x0+x2)+x1-2*J
    m[F(19,10)]+=(9*x0+509*x2)/900+J
    assert all(0<=mass for mass in m.values())
    assert sum(m.values())==1 and sum(r*mass for r,mass in m.items())==1
    return m

def witness(Ep,Eq,Tp,Tq):
    a,b=Tp-F(15,8),Tq-F(15,8)
    c,d=Ep-F(1,2),Eq-F(1,2)
    g=F(1,2)+3*b-2*a
    x=(g,F(1,4),F(1,4),F(27,640),F(13,320),F(27,640)+2*(a-b))
    caps=capacities(x[1],x[2])
    assert x[1]<=g<=1 and x[2]<=g and all(0<=z<=v for z,v in zip(x[3:],caps))
    m=stopped_mass(x)
    # Share t_1 at *every* stopped key with LR 1 (root, time-3, terminal),
    # rather than changing only the root declaration.
    t1=F(1,2)+(-4*c-3*d)/m[F(1)]
    t34=F(1,2)+8*(c+d)/(g-F(1,4))
    t={r:F(1,2) for r in m};t[F(1)]=t1;t[F(3,4)]=t34
    assert all(0<=v<=1 for v in t.values())
    ep=1-sum(r*m[r]*t[r] for r in m)
    eq=sum(m[r]*t[r] for r in m)
    assert (ep,eq)==(Ep,Eq) and time(x)==(Tp,Tq)
    return x,t

assert C[3:]==tuple(v/2 for v in capacities(C[1],C[2]))
assert time(C)==(F(15,8),F(15,8))
assert all(sum(q3[i][j]*r3[j] for j in range(3))==r1[i] for i in range(2))
assert all(sum(row)==1 for row in q3)
assert F(4,148)<F(27,640)
assert F(16,148)/(F(1,4)-F(5,148))==F(1,2)
checks=0;corners=0;boundary34=False
for vals in product((-1,0,1),repeat=4):
    W=(F(1,2)+H*vals[0],F(1,2)+H*vals[1],F(15,8)+H*vals[2],F(15,8)+H*vals[3])
    witness(*W);checks+=1
for vals in product((-1,1),repeat=4):
    W=(F(1,2)+H*vals[0],F(1,2)+H*vals[1],F(15,8)+H*vals[2],F(15,8)+H*vals[3])
    x,t=witness(*W)
    if t[F(3,4)] in (F(0),F(1)):boundary34=True
    corners+=1
assert boundary34
h=F(1,147)
g=F(1,2)-5*h
assert g>F(1,4) and F(1,2)+16*h/(g-F(1,4))>1
print('center=(1/2,1/2,15/8,15/8), box_radius=1/148')
print('exact_grid_targets=',checks,'exact_corners=',corners)
print('all seven stopped LR-key masses checked, including shared ratio-1 declaration')
print('terminal Q moment checks=2; exact sharpness witness for the stated controller=1')
print('PASS_EXACT_R5_QUANTIFIED_FOUR_DIMENSIONAL_LR_BOX_FULL_KEY_SHARING')
