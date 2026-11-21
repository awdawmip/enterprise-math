#!/usr/bin/env python3
"""EC49FVM: exact mod-11 projective obstruction and dyadic mesh audit.
Frozen observer inputs: BRC16943, EC49FVJ/FVL; not a native BRC computation.
"""
from fractions import Fraction
from math import gcd

P=11
U=Fraction(4822040484,8132285009)
GAMMA=Fraction(141024,1653649)

def mod(q):
    assert q.denominator % P
    return q.numerator * pow(q.denominator, -1, P) % P

u, g = mod(U), mod(GAMMA)
inv637 = pow(637, -1, P)
c, d = mod(Fraction(-3,637)), u*g % P
rows=[]
for z in range(P):
    la=(637-3*z)*inv637 % P
    lb=u*(1+g*z) % P
    a=(1-(1-z)*la) % P
    b=(1-(1-z)*lb) % P
    rows.append((z,a,b,la,lb))
sing=[r for r in rows if r[3]==r[4]]
assert sing==[(3,10,10,10,10)]
sz,sa,sb,sla,slb=sing[0]
hcoef, ncoef = (-(1-sz)*sla)%P, sa%P
assert (hcoef,ncoef)==(9,10)

def projective_nonzero(h,n):
    assert h>0 and n>0
    for z,a,b,la,lb in rows:
        if z==sz:
            val=(pow(sla,n-1,P)*pow(sa,h-1,P)
                 *(n*sa-h*(1-sz)*sla))%P
        else:
            val=((pow(a,h,P)*pow(la,n,P)-pow(b,h,P)*pow(lb,n,P))
                 *pow((la-lb)%P,-1,P))%P
        if val==0: return False
    val=((pow(c,h+n,P)-pow(d,h+n,P))*pow((c-d)%P,-1,P))%P
    return val!=0

patterns={(a,b) for a in range(10) for b in range(10)
          if all(
              (((pow(A,a or 10,P)*pow(LA,b or 10,P)-pow(B,a or 10,P)*pow(LB,b or 10,P))
                 *pow((LA-LB)%P,-1,P))%P)!=0
              for z,A,B,LA,LB in rows if z!=sz)
          and ((pow(c,(a or 10)+(b or 10),P)-pow(d,(a or 10)+(b or 10),P))
               *pow((c-d)%P,-1,P))%P !=0}
assert len(patterns)==44

def valid(h,n):
    return ((h%10,n%10) in patterns) and (hcoef*h+ncoef*n)%P!=0

period_rows=[]
for j in range(1,21):
    k_mod=pow(2,j,110)
    allowed=[h for h in range(1,110,2) if valid(h,k_mod-h)]
    assert len(allowed)==20
    gaps=[b-a for a,b in zip(allowed,allowed[1:])]+[allowed[0]+110-allowed[-1]]
    assert max(gaps)==10
    k=2**(j+20)
    for h in range(1,110,2):
        assert valid(h,k-h)==projective_nonzero(h,k-h)
    period_rows.append((j,k_mod,len(allowed),max(gaps),allowed[0],allowed[-1]))

assert pow(2,20,55)==1
for j in range(1,21):
    for h in range(1,110,2):
        assert valid(h,pow(2,j,110)-h)==valid(h,pow(2,j+20,110)-h)

for j in range(7,19):
    k=2**j
    selected=[h for h in range(1,k,2) if valid(h,k-h)]
    gaps=[selected[0]]+[b-a for a,b in zip(selected,selected[1:])]+[k-selected[-1]]
    assert max(gaps)<=10
    assert all(gcd(h,k)==1 for h in selected)
    if j<=10: print('dyadic',j,'k',k,'certified',len(selected),'max_gap',max(gaps))

for j in [7,8,9,10,12]:
    k=2**j
    for lo,hi in [(Fraction(0),Fraction(1)),(Fraction(1,3),Fraction(2,3)),
                  (Fraction(1,13),Fraction(2,13))]:
        actual=sum(1 for h in range(1,k,2) if lo*k<=h<hi*k and valid(h,k-h))
        predicted=Fraction(2,11)*k*(hi-lo)
        assert abs(actual-predicted)<=20

print('period table j,kmod110,count,maxgap,first,last:')
for row in period_rows: print(','.join(map(str,row)))
print('ALL PASS — 20/20 exact projective classes; dyadic covering gap 10/k; O(1/H) certificate mesh')
