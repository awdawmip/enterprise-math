#!/usr/bin/env python3
"""EC49FVY, exact reflection/orthogonality and non-delay witness; BRC16943."""
from collections import Counter
from fractions import Fraction as Q
from math import gcd

P = 11
U = Q(4822040484, 8132285009)
G = Q(141024, 1653649)
def mod11(x):
    return x.numerator * pow(x.denominator, -1, P) % P
u, gamma, inv = mod11(U), mod11(G), pow(637, -1, P)
rows = []
for z in range(P):
    la, lb = (637-3*z)*inv % P, u*(1+gamma*z) % P
    aa, bb = (1-(1-z)*la) % P, (1-(1-z)*lb) % P
    rows.append((z,aa,bb,la,lb))
c, d = -3*inv % P, u*gamma % P
P10 = {(h,n) for h in range(10) for n in range(10)
       if all((pow(aa,h,P)*pow(la,n,P)-pow(bb,h,P)*pow(lb,n,P))
              * pow((la-lb)%P,-1,P) % P
              for z,aa,bb,la,lb in rows if z != 3)
       and (pow(c,h+n,P)-pow(d,h+n,P))*pow((c-d)%P,-1,P) % P}
assert len(P10) == 44
assert {((-h)%10,(-n)%10) for h,n in P10} == P10

def cert(h,n):
    return (h%10,n%10) in P10 and (9*h+10*n)%11 != 0

def direct(h,n):
    for z,aa,bb,la,lb in rows:
        if z == 3:
            value = pow(la,n-1,P)*pow(aa,h-1,P)*(n*aa-h*(1-z)*la)%P
        else:
            value = (pow(aa,h,P)*pow(la,n,P)-pow(bb,h,P)*pow(lb,n,P)) * pow((la-lb)%P,-1,P)%P
        if value == 0:
            return False
    return (pow(c,h+n,P)-pow(d,h+n,P))*pow((c-d)%P,-1,P)%P != 0
assert all(cert(h,n) == direct(h,n) for h in range(1,111) for n in range(1,111))
print('PROJECTIVE 12100/12100; P10=44; SIGN_REVERSAL PASS')

def get_sets(a,b):
    assert 0 < a < b and gcd(a,b) == 1
    T = 110*b
    sets = {}
    for s in (-1,+1):
        sets[s] = {q % T for q in range(1,T+1) if (a*q+s)%b==0
                   and cert((a*q+s)//b, q-(a*q+s)//b)}
    return T, sets

def deficits(R,T):
    return [next(t for t in range(T) if (H-t)%T in R) for H in range(T)]

def gaps(R,T):
    q = sorted(R)
    return [(q[(i+1)%len(q)]-q[i])%T for i in range(len(q))]

families = 0
for b in range(2,13):
    for a in range(1,b):
        if gcd(a,b)!=1:
            continue
        T, R = get_sets(a,b)
        assert R[+1] == {(-q)%T for q in R[-1]}
        l,r = deficits(R[-1],T),deficits(R[+1],T)
        assert Counter(l) == Counter(r)
        assert sum(r) == sum(l)
        mean = Q(sum(l),T)
        cov = sum(((Q(x)-mean)*(Q(y)-mean) for x,y in zip(l,r)),Q())/T
        variance = sum(((Q(x)-mean)**2 for x in l),Q())/T
        assert sum((Q(y-x,2) for x,y in zip(l,r)),Q()) == 0
        assert (variance-variance)/4 == 0
        assert sum(((Q(x+y,2)-mean)*Q(y-x,2) for x,y in zip(l,r)),Q()) == 0
        families += 1
assert families == 45
print('GENERAL REFLECTION/MARGINAL/ORTHOGONALITY: 45 REDUCED ANCHORS b<=12 PASS')

a,b = 1,7
T,R = get_sets(a,b)
assert not cert(a,b-a)
assert T == 770 and len(R[-1]) == len(R[+1]) == 60
cyc = gaps(R[-1],T)
assert max(cyc) == 42
ordered = Counter((cyc[i],cyc[(i+1)%len(cyc)]) for i in range(len(cyc)))
assert (ordered[(14,7)],ordered[(7,14)]) == (10,2)
assert not any({(q+shift)%T for q in R[-1]}==R[+1] for shift in range(T))
l,r = deficits(R[-1],T), deficits(R[+1],T)
assert max(l)==max(r)==41
assert next(t for t in range(1,T+1) if T%t==0
            and all((l[i],r[i])==(l[(i+t)%T],r[(i+t)%T]) for i in range(T)))==T
m = Q(sum(l),T)
A = [Q(y-x,2) for x,y in zip(l,r)]
varA = sum((v*v for v in A),Q())/T
assert (m,varA)==(Q(494,55),Q(9531,220))
print('ANCHOR 1/7: 770 PERIOD; 60 EACH; MAX_GAP=42; PAIR_GAPS (14,7)=10, (7,14)=2; NO SHIFT PASS')
print('ANCHOR 1/7: MEAN_DEFICIT',m,'VAR(A)',varA,'JOINT_STATES',len(Counter(zip(l,r))))

for H in (113,137,177,231,331):
    left=right=None
    for q in range(2,H+1):
        for h in range(1,q):
            if gcd(h,q)!=1 or not cert(h,q-h):
                continue
            x=Q(h,q)
            if x<Q(a,b) and (left is None or left<x):left=x
            if x>Q(a,b) and (right is None or x<right):right=x
    qL,qR=H-l[H%T],H-r[H%T]
    assert left==Q(a*qL-1,b*qL) and right==Q(a*qR+1,b*qR)
    rho,A_H=Q(l[H%T]+r[H%T],2),Q(r[H%T]-l[H%T],2)
    L,Rr=Q(a,b)-left,right-Q(a,b)
    assert L+Rr == Q(2,b*H)+Q(2*rho,b*H*H)+Q(l[H%T]**2,H*H*(H-l[H%T])*b)+Q(r[H%T]**2,H*H*(H-r[H%T])*b)
    assert b*H*H*(Rr-L)/2 == A_H*Q(H*H,qL*qR)
    print('INDEPENDENT_FAREY',H,'nearest',str(left),str(right),'rho',rho,'A',A_H,'PASS')
print('ALL PASS')
