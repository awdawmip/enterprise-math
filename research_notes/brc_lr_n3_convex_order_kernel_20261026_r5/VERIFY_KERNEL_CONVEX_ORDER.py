#!/usr/bin/env python3
"""Author-level exact rational checks for an N=3 LR-dependent terminal kernel.
Finite coefficient grids test a theorem but are not its universal proof.
"""
from fractions import Fraction as F
from itertools import product

R=(F(1,2),F(1),F(3,2))
Y=(F(1,4),F(2))
Q1={'a':F(1,2),'b':F(1,2)}
ALPHA={'a':F(1,4),'b':F(1,3)}
Q2={h:(v,1-2*v,v) for h,v in ALPHA.items()}
P2={h:tuple(r*q for r,q in zip(R,Q2[h])) for h in ALPHA}
# Fixed final LR endpoints with an LR-dependent, mean-preserving Q kernel.
Q3={r:((Y[1]-r)/(Y[1]-Y[0]),(r-Y[0])/(Y[1]-Y[0])) for r in R}
P3={r:tuple(y*q/r for y,q in zip(Y,Q3[r])) for r in R}
QBAR=tuple(sum(Q1[h]*Q2[h][i] for h in Q1) for i in range(3))
assert sum(Q1.values())==1 and Q2['a']!=Q2['b']
assert QBAR==(F(7,24),F(5,12),F(7,24))
for h in Q1:
    assert sum(Q2[h])==sum(P2[h])==1
    assert all(x>0 for x in Q2[h]+P2[h])
for r in R:
    assert all(q>0 for q in Q3[r]+P3[r])
    assert sum(Q3[r])==sum(P3[r])==1
    assert sum(y*q for y,q in zip(Y,Q3[r]))==r
assert tuple(Q3[r][1] for r in R)==(F(1,7),F(3,7),F(5,7))
assert tuple(P3[r][1] for r in R)==(F(4,7),F(6,7),F(20,21))

# Piecewise-linear call prices need checking only at union of terminal-LR knots.
for theta in (F(0),)+Y:
    calls=tuple(sum(q*max(F(0),y-theta) for y,q in zip(Y,Q3[r])) for r in R)
    assert 2*calls[1]==calls[0]+calls[2],(theta,calls)

def support(A,B,C,D):
    def H(r):return min(A*r,B)
    def phi(r):
        return min(H(r), C*r+D+sum(q*H(y) for q,y in zip(Q3[r],Y)))
    gamma=C+D
    m=H(F(1))
    f={h:sum(q*phi(r) for q,r in zip(Q2[h],R)) for h in Q1}
    full=min(m,gamma+sum(Q1[h]*min(m,gamma+f[h]) for h in Q1))
    pooled=sum(q*phi(r) for q,r in zip(QBAR,R))
    compressed=min(m,gamma+min(m,gamma+pooled))
    midgap=2*phi(R[1])-phi(R[0])-phi(R[2])
    d=tuple(m-f[h] for h in Q1)
    assert midgap>=0 and min(d)>=0 and (d[0]+d[1])/2<=2*min(d)
    return full,compressed

def observe(compressed):
    ep=eq=tp=tq=F(0)
    def walk(t,h,r,y,p,q):
        nonlocal ep,eq,tp,tq
        if t==0: acts={'C':F(1)}
        elif compressed:
            if t==1:acts={'P':F(1,2),'C':F(1,2)}
            elif t==2:acts={'P':F(1,7),'C':F(6,7)} if r==R[2] else {'P':F(1)}
            else:acts={'Q':F(1)} if y==Y[0] else {'P':F(1)}
        else:
            if t==1:acts={'C':F(1)} if h=='a' else {'P':F(1)}
            elif t==2:acts={'C':F(1)} if h=='a' and r==R[2] else {'P':F(1)}
            else:acts={'Q':F(1)} if y==Y[0] else {'P':F(1)}
        assert sum(acts.values())==1
        for action,w in acts.items():
            pp,qq=p*w,q*w
            if action=='P':eq+=qq
            elif action=='Q':ep+=pp
            else:
                assert t<3
                tp+=pp;tq+=qq
                if t==0:
                    for hh in Q1:walk(1,hh,None,None,pp*Q1[hh],qq*Q1[hh])
                elif t==1:
                    for i,rr in enumerate(R):walk(2,h,rr,None,pp*P2[h][i],qq*Q2[h][i])
                else:
                    for j,yy in enumerate(Y):walk(3,h,r,yy,pp*P3[r][j],qq*Q3[r][j])
    walk(0,None,None,None,F(1),F(1))
    return ep,eq,tp,tq

raw=observe(False)
compressed=observe(True)
assert raw==compressed==(F(1,112),F(27,28),F(27,16),F(13,8)),(raw,compressed)
n=0
for coeffs in product(range(-4,5),repeat=4):
    u,v=support(*(F(k) for k in coeffs))
    assert u==v,(coeffs,u,v)
    n+=1
print('MODEL=STRICT_POSITIVE_RATIONAL_N3, FIRST_LR=1, R=(1/2,1,3/2), TERMINAL_Y=(1/4,2)')
print('TIME1_Q_STRONG_LR_LUMPABILITY=FALSE')
print('FINAL_Q_HIGH_BY_R='+','.join(str(Q3[r][1]) for r in R))
print('FINAL_P_HIGH_BY_R='+','.join(str(P3[r][1]) for r in R))
print('FINITE_SUPPORT_CALL_PRICE_CONVEXITY=EQUALITY_AT_ALL_KNOTS')
print('EXACT_FULL_OBSERVER='+','.join(str(x) for x in raw))
print('EXACT_LR_ONLY_OBSERVER='+','.join(str(x) for x in compressed))
print('SIGNED_COEFFICIENT_GRID_POINTS='+str(n))
print('BELLMAN_EQUALITY_ALL_GRID_POINTS=PASS')
print('UNIVERSAL_REAL_COEFFICIENT_PROOF=SEPARATE_ALGEBRAIC_ARGUMENT')
