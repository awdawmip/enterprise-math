from fractions import Fraction as F
from itertools import product

r=(F(1,2),F(1),F(3,2))
w=(F(1,2),F(1,2))
K=((F(1,4),F(1,2),F(1,4)),(F(5,16),F(6,16),F(5,16)))
assert all(sum(v)==1 and sum(a*b for a,b in zip(r,v))==1 and all(a>0 for a in v) for v in K)
delta = sum((abs(a-b) for a,b in zip(*K)), F(0))/2
assert delta==F(1,8)

# First actions: 0 STOP/P, 1 STOP/Q, 2 CONTINUE.
# Terminal labels: 0 P, 1 Q for each (source, likelihood-ratio key).
def calc(first, terminal):
    c=[int(a==2) for a in first]
    sc=sum(w[h]*c[h] for h in range(2))
    early_P=sum(w[h]*int(first[h]==0) for h in range(2))
    early_Q=sum(w[h]*int(first[h]==1) for h in range(2))
    muF=[sum((w[h]*c[h]*K[h][j] for h in range(2)), F(0)) for j in range(3)]
    barK=[sum((w[h]*K[h][j] for h in range(2)), F(0)) for j in range(3)]
    muL=[sc*barK[j] for j in range(3)]
    f=[]
    for j in range(3):
        x=sum((w[h]*c[h]*K[h][j]*int(terminal[h][j]==0) for h in range(2)),F(0))
        f.append(x/muF[j] if muF[j] else F(0))
    efQ=early_P + sum((muF[j]*f[j] for j in range(3)),F(0))
    elQ=early_P + sum((muL[j]*f[j] for j in range(3)),F(0))
    efP=early_Q + sum((r[j]*muF[j]*(1-f[j]) for j in range(3)),F(0))
    elP=early_Q + sum((r[j]*muL[j]*(1-f[j]) for j in range(3)),F(0))
    tfQ=F(1)+sc
    tlQ=F(1)+sc
    tfP=F(1)+sum((r[j]*muF[j] for j in range(3)),F(0))
    tlP=F(1)+sum((r[j]*muL[j] for j in range(3)),F(0))
    D=[muF[j]-muL[j] for j in range(3)]
    expectedD=[w[0]*w[1]*(c[0]-c[1])*(K[0][j]-K[1][j]) for j in range(3)]
    assert D==expectedD
    assert sum(D)==sum((r[j]*D[j] for j in range(3)),F(0))==0
    assert efQ-elQ==sum((D[j]*f[j] for j in range(3)),F(0))
    assert efP-elP==-sum((r[j]*D[j]*f[j] for j in range(3)),F(0))
    assert (tfQ,tfP)==(tlQ,tlP)
    tv=sum((abs(z) for z in D),F(0))/2
    assert tv==w[0]*w[1]*abs(c[0]-c[1])*delta
    assert abs(efQ-elQ)<=tv and abs(efP-elP)<=max(r)*tv
    return (efP,efQ,tfP,tfQ),(elP,elQ,tlP,tlQ),tv

count=0;nonzero=0
for first in product(range(3),repeat=2):
    for labels in product(range(2),repeat=6):
        terminal=(labels[:3],labels[3:])
        a,b,tv=calc(first,terminal)
        count+=1
        nonzero+=bool(a!=b)
assert count==576
example=calc((2,0),((1,0,1),(0,0,0)))
assert example[0]==(F(1,4),F(3,4),F(3,2),F(3,2))
assert example[1]==(F(9,32),F(23,32),F(3,2),F(3,2))
assert example[2]==F(1,32)
print('PASS_EXACT_R5_TWO_SOURCE_KERNEL_GATE_COVARIANCE')
print('model=K_A(1/4,1/2,1/4);K_B(5/16,6/16,5/16);r=(1/2,1,3/2);w=(1/2,1/2)')
print('Q_TV_KERNEL_DIAMETER=',delta)
print('FULL_DETERMINISTIC_POLICIES=',count)
print('NONZERO_CANONICAL_O4_RESIDUALS=',nonzero)
print('EXAMPLE_FULL_O4=',example[0])
print('EXAMPLE_LR_O4=',example[1])
print('EXAMPLE_TERMINAL_Q_TV=',example[2])
print('EXAMPLE_O4_FULL_MINUS_LR=',tuple(x-y for x,y in zip(example[0],example[1])))
