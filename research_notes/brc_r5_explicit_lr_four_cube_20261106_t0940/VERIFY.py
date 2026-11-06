from fractions import Fraction as Q
from itertools import product

F = Q
# Full strictly positive conditional Q kernels from frozen R5 auxiliary model.
q3 = ((F(13,20),F(1,5),F(3,20)),
      (F(1,40),F(9,20),F(21,40)))
r1 = (F(3,4),F(5,4))
r3 = (F(1,2),F(1),F(3,2))
C = (F(1,2), F(1,4), F(1,4), F(27,640), F(13,320), F(27,640))
H = F(1,148)

def capacities(u0,u1):
    return tuple((u0*q3[0][j]+u1*q3[1][j])/2 for j in range(3))

def time(x):
    g,u0,u1,x0,x1,x2=x
    return (F(1)+g+(3*u0+5*u1)/8+x0/2+x1+3*x2/2,
            F(1)+g+(u0+u1)/2+x0+x1+x2)

def witness(Ep, Eq, Tp, Tq):
    a,b=Tp-F(15,8),Tq-F(15,8)
    c,d=Ep-F(1,2),Eq-F(1,2)
    g=F(1,2)+3*b-2*a
    x2=F(27,640)+2*(a-b)
    x=(g,F(1,4),F(1,4),F(27,640),F(13,320),x2)
    v=capacities(x[1],x[2])
    assert x[1] <=g<=1 and x[2]<=g and all(F(0)<=xx<=vv for xx,vv in zip(x[3:],v))
    t_root=F(1,2)+(-4*c-3*d)/(1-g)
    t_s0=F(1,2)+8*(c+d)/(g-F(1,4))
    assert 0<=t_root<=1 and 0<=t_s0<=1
    # All other time-/likelihood-key declarations select P with probability 1/2.
    # The first two keys have P masses (1-g), 3(g-u0)/8, and Q masses (1-g),(g-u0)/2.
    ep=F(1,2)-(1-g)*(t_root-F(1,2))-F(3,8)*(g-F(1,4))*(t_s0-F(1,2))
    eq=F(1,2)+(1-g)*(t_root-F(1,2))+F(1,2)*(g-F(1,4))*(t_s0-F(1,2))
    assert (ep,eq)==(Ep,Eq) and time(x)==(Tp,Tq)
    return x,t_root,t_s0

assert C[3:]==tuple(v/2 for v in capacities(C[1],C[2]))
assert time(C)==(F(15,8),F(15,8))
assert all(sum(q3[i][j]*r3[j] for j in range(3))==r1[i] for i in range(2))
assert all(sum(row)==1 for row in q3)
assert F(4,148) <=F(27,640)
assert F(16,148)/(F(1,4)-F(5,148))==F(1,2)
checks=0; corner_checks=0; boundary_t0=False
for vals in product((-1,0,1),repeat=4):
    ep=F(1,2)+H*vals[0];eq=F(1,2)+H*vals[1]
    tp=F(15,8)+H*vals[2];tq=F(15,8)+H*vals[3]
    x,t0,t1=witness(ep,eq,tp,tq)
    checks+=1
for vals in product((-1,1),repeat=4):
    ep=F(1,2)+H*vals[0];eq=F(1,2)+H*vals[1]
    tp=F(15,8)+H*vals[2];tq=F(15,8)+H*vals[3]
    x,tr,ts=witness(ep,eq,tp,tq)
    if ts in (F(0),F(1)):boundary_t0=True
    corner_checks+=1
assert boundary_t0
# At any radius h>1/148 sufficiently close, the same fixed controller fails on
# the joint target (+h,+h,+h,-h): time forces g=1/2-5h and t_s0>1.
h=F(1,147)
g=F(1,2)-5*h
assert F(0)<g-F(1,4)
assert F(1,2)+16*h/(g-F(1,4))>1
print('center=(1/2,1/2,15/8,15/8), box_radius=1/148')
print('exact_grid_targets=',checks,'exact_corners=',corner_checks)
print('terminal Q moment checks=2; exact optimality witness for the stated controller=1')
print('PASS_EXACT_R5_QUANTIFIED_FOUR_DIMENSIONAL_LR_BOX')
