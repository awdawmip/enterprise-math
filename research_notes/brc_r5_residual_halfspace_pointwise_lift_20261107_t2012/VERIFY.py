#!/usr/bin/env python3
"""Exact-rational verification for R5 nonnegative-residual same-time history erasure.
No external packages, no sampling used as the proof of all-real result.
"""
from fractions import Fraction as Q
from itertools import product

K = Q(247, 1620)
LR = [Q(1,10),Q(1,2),Q(3,4),Q(1),Q(5,4),Q(3,2),Q(19,10)]

def masses(x):
    g,a,b,u,v,w,z = x
    c0=Q(13,40)*a+Q(1,80)*b
    c1=Q(1,10)*a+Q(9,40)*b
    c2=Q(3,40)*a+Q(21,80)*b
    return (
        Q(509,900)*u+Q(47,180)*z+Q(67,162)*(v-z)+Q(1,100)*w,
        c0-u,
        (g-a)/2,
        1-g+c1-v+Q(191,450)*(u+w)+Q(43,90)*z+Q(14,81)*(v-z),
        (g-b)/2,
        c2-w,
        Q(1,100)*u+Q(47,180)*z+Q(67,162)*(v-z)+Q(509,900)*w,
    )

def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+Q(3,8)*a+Q(5,8)*b+Q(1,2)*u+v+Q(3,2)*w,
            1+g+(a+b)/2+u+v+w)

def legal(x):
    g,a,b,u,v,w,z=x
    c0=Q(13,40)*a+Q(1,80)*b
    c2=Q(3,40)*a+Q(21,80)*b
    return (0<=a<=g<=1 and 0<=b<=g<=1 and 0<=u<=c0 and 0<=w<=c2
            and 0<=z<=a/10 and 0<=v-z<=Q(9,40)*b)

def residual(x):
    g,a,b,u,v,w,z=x
    return 9*b*z-4*a*(v-z)

def lift(x, declarations):
    assert legal(x) and residual(x)>=0
    g,a,b,u,v,w,z=x
    denom=4*a+9*b
    new_z=Q(0) if denom==0 else 4*a*v/denom
    y=(g,a,b,u,v,w,new_z)
    assert legal(y) and residual(y)==0
    old_m, new_m=masses(x), masses(y)
    delta=K*(z-new_z)
    assert delta>=0
    assert all(old_m[j]==new_m[j] for j in [1,2,4,5])
    assert new_m[0]==old_m[0]+delta
    assert new_m[6]==old_m[6]+delta
    assert new_m[3]==old_m[3]-2*delta
    assert times(y)==times(x)
    e=list(declarations)
    for j in (0,6):
        if new_m[j]>0:
            e[j]=(old_m[j]*declarations[j]+delta*declarations[3])/new_m[j]
        else:
            assert old_m[j]==delta==0
    assert all(0<=d<=1 for d in e)
    return y, tuple(e), delta

def observe(x,d):
    ms=masses(x)
    e_q=sum(m*di for m,di in zip(ms,d))
    e_p=1-sum(r*m*di for r,m,di in zip(LR,ms,d))
    return e_p,e_q,*times(x)

# Exact symbolic transfer coefficient check (common Q and P mass balance)
assert Q(47,180)-Q(67,162)==-K
assert Q(43,90)-Q(14,81)==2*K
assert LR[0]+LR[6]==2*LR[3]
assert 4*Q(1,10)==Q(2,5) and 9*Q(1,10)==Q(9,10)

# Explicit history-dependent corner with R=9/10 and a nontrivial declaration map.
x=(Q(1),Q(1),Q(1),Q(0),Q(1,10),Q(0),Q(1,10))
d=(Q(1),Q(0),Q(0),Q(0),Q(0),Q(0),Q(1))
y,e,delta=lift(x,d)
assert residual(x)==Q(9,10)
assert delta==Q(247,23400)
assert y==(Q(1),Q(1),Q(1),Q(0),Q(1,10),Q(0),Q(2,65))
assert e[0]==e[6]==Q(611,858)
assert observe(x,d)==observe(y,e)==(Q(853,900),Q(47,900),Q(31,10),Q(31,10))
print('CORNER_R',residual(x),'DELTA',delta,'SEEDLESS_Z',y[-1],
      'DECLARATION_LOW_HIGH',e[0],'W',observe(y,e))

# Verify every binary full declaration for this exact corner.
for ds in product((Q(0),Q(1)),repeat=7):
    yy,ee,dd=lift(x,ds)
    assert observe(x,ds)==observe(yy,ee)
print('EXACT_CORNER_2_POWER_7_DECLARATIONS',2**7)

# A rational parametric grid checks legal bounds, endpoint degeneracies, and label map.
count=0
for g in (Q(0),Q(1,2),Q(1)):
  for af in (Q(0),Q(1,3),Q(1)):
   for bf in (Q(0),Q(2,3),Q(1)):
    a,b=g*af,g*bf
    c0=Q(13,40)*a+Q(1,80)*b
    c2=Q(3,40)*a+Q(21,80)*b
    for et,om in ((Q(0),Q(1)),(Q(1,2),Q(1,3)),(Q(1),Q(0))):
     for thetaA,thetaB in ((Q(0),Q(0)),(Q(1,3),Q(0)),(Q(1,2),Q(1,4)),(Q(1),Q(1,3)),(Q(1),Q(1))):
      zz=thetaA*a/10
      vv=zz+thetaB*Q(9,40)*b
      xx=(g,a,b,et*c0,vv,om*c2,zz)
      assert legal(xx) and residual(xx)>=0
      ds=(Q(0),Q(1,7),Q(2,7),Q(3,7),Q(4,7),Q(5,7),Q(1))
      yy,ee,dd=lift(xx,ds)
      assert observe(xx,ds)==observe(yy,ee)
      mx=masses(xx);my=masses(yy)
      assert all(m>=0 for m in mx+my)
      assert sum(mx)==sum(my)==1
      assert sum(r*m for r,m in zip(LR,mx))==sum(r*m for r,m in zip(LR,my))==1
      count+=1
print('EXACT_PARAMETRIC_GRID_LEGAL_CASES',count)

# Negative-residual fixed-flow sufficient-label test.
# If new_m0=M0-D and new_m6=M6-D, with D>0, formulas below
# give a valid direct lifting whenever both corrected labels are in [0,1].
def reverse_lift_if_admissible(x,d):
    assert legal(x) and residual(x)<0
    g,a,b,u,v,w,z=x
    new_z=4*a*v/(4*a+9*b)
    y=(g,a,b,u,v,w,new_z)
    m,n=masses(x),masses(y)
    D=K*(new_z-z)
    e=list(d)
    for j in (0,6):
        if not (n[j]>0): return None
        e[j]=(m[j]*d[j]-D*d[3])/n[j]
    if not all(Q(0)<=dj<=Q(1) for dj in e): return None
    return y,tuple(e),D

xneg=(Q(1),Q(1),Q(1),Q(0),Q(9,40),Q(0),Q(0))
assert residual(xneg)==-Q(9,10)
for d_const in (Q(0),Q(1,3),Q(1)):
    dd=(d_const,)*7
    rr=reverse_lift_if_admissible(xneg,dd)
    assert rr is not None and observe(xneg,dd)==observe(rr[0],rr[1])
assert reverse_lift_if_admissible(xneg,(Q(0),Q(0),Q(0),Q(1),Q(0),Q(0),Q(0))) is None
print('NEGATIVE_RESIDUAL_SAME_FLOW_SUFFICIENT_LABEL_TEST', 'PASS')
print('PASS_R5_NONNEGATIVE_HISTORY_RESIDUAL_ALL_REAL_EXACT_LIFT')
