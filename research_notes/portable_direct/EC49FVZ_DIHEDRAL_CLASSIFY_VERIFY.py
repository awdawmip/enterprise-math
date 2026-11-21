#!/usr/bin/env python3
"""EC49FVZ exact finite dihedral classification (frozen BRC16943 predicate)."""
from collections import Counter
from fractions import Fraction
from math import gcd

p = 11
U = Fraction(4822040484, 8132285009)
G = Fraction(141024, 1653649)
def residue11(x):
    return x.numerator * pow(x.denominator, -1, p) % p
u, gamma, inv637 = residue11(U), residue11(G), pow(637, -1, p)
rows = []
for z in range(p):
    la, lb = (637 - 3*z)*inv637 % p, u*(1 + gamma*z) % p
    aa, bb = (1 - (1-z)*la) % p, (1 - (1-z)*lb) % p
    rows.append((z, aa, bb, la, lb))
c, d = -3*inv637 % p, u*gamma % p
P10 = {(h,n) for h in range(10) for n in range(10)
       if all((pow(aa,h,p)*pow(la,n,p)-pow(bb,h,p)*pow(lb,n,p))
              * pow((la-lb)%p,-1,p) % p
              for z,aa,bb,la,lb in rows if z!=3)
       and (pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p)%p}
assert len(P10) == 44

def certificate(h,n):
    return (h%10,n%10) in P10 and (9*h+10*n)%11 != 0

def direct(h,n):
    for z,aa,bb,la,lb in rows:
        if z==3:
            val=pow(la,n-1,p)*pow(aa,h-1,p)*(n*aa-h*(1-z)*la)%p
        else:
            val=(pow(aa,h,p)*pow(la,n,p)-pow(bb,h,p)*pow(lb,n,p))*pow((la-lb)%p,-1,p)%p
        if not val:
            return False
    return (pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p)%p != 0
assert all(certificate(h,n)==direct(h,n) for h in range(1,111) for n in range(1,111))
assert {((-h)%10,(-n)%10) for h,n in P10} == P10
print('PROJECTIVE_DIRECT 12100/12100; P10=44; SIGN_SYMMETRY PASS')

def egcd(a,b):
    if b==0:
        return abs(a), 1 if a>=0 else -1, 0
    g,x,y=egcd(b,a%b)
    return g,y,x-(a//b)*y

def base_mod(a,b,m):
    # (b-a)h - a*n = -1 (mod m); primitive direction guaranteed.
    g,x,y=egcd(b-a,-a)
    d,s,_=egcd(g,m)
    assert d==1
    h,n=(-s*x)%m,(-s*y)%m
    assert ((b-a)*h-a*n+1)%m==0
    return h,n

def reflective(W):
    return W in W[::-1]*2

def word10(a,b):
    h,n=base_mod(a,b,10)
    return bytes(int(((h+a*t)%10,(n+(b-a)*t)%10) in P10)
                 for t in range(10))

rows10=[]
for b in range(10):
    for a in range(10):
        if gcd(gcd(a,b),10)!=1:
            continue
        word=word10(a,b)
        yes=reflective(word)
        criterion=(b%2==0 and (a%5==0 or (2*a-b)%5==0))
        assert yes==criterion, (a,b,word)
        rows10.append((a,b,sum(word),yes))
assert len(rows10)==72
winners=sorted((a,b) for a,b,wt,yes in rows10 if yes)
assert winners==[(1,2),(3,6),(5,2),(5,4),(5,6),(5,8),(7,4),(9,8)]
assert Counter(wt for a,b,wt,yes in rows10)==Counter({4:12,5:24,6:24,7:8,8:4})
print('MOD10_PRIMITIVE_DIRECTIONS 72; REFLECTIVE 8; NONREFLECTIVE 64; ALL CRITERION PASS')
print('EIGHT_SYMMETRIC_CLASSES',winners)
for a,b in winners:
    uword=word10(a,b)
    assert sum(all(uword[t]==uword[(z-t)%10] for t in range(10)) for z in range(10))==1
    assert all(any(uword[t]!=uword[(t+k)%10] for t in range(10)) for k in (1,2,5))
print('POSITIVE_MOD10_WORDS: EACH ONE REFLECTION CENTER; MINIMAL PERIOD 10 PASS')

# The mod-11 factor is either constant true or all but one of 11 positions;
# compare every primitive residue direction to the exact full 110-cell mask.
tested=positive=0
for b in range(110):
    for a in range(110):
        if gcd(gcd(a,b),110)!=1:
            continue
        h,n=base_mod(a,b,110)
        W=bytes(int(certificate(h+a*t,n+(b-a)*t)) for t in range(110))
        p10=word10(a,b)
        v11=bytes(int((9*(h+a*t)+10*(n+(b-a)*t))%11!=0) for t in range(11))
        assert all(W[t]==p10[t%10]*v11[t%11] for t in range(110))
        assert sum(v11) in (10,11)
        expected=bool(b%2==0 and (a%5==0 or (2*a-b)%5==0))
        assert reflective(W)==expected
        tested+=1
        positive+=expected
assert (tested,positive)==(8640,960)
print('MOD110_PRIMITIVE_DIRECTIONS 8640; TRANSLATABLE 960; NONTRANSLATABLE 7680; CRT PASS')

# Independent denominator-set construction for reduced rational anchors.
# The plus-mask is the reflected minus-mask. A delay is an integer shift in q.
def exact_denominator_masks(a,b):
    T=110*b
    R={s:{q%T for q in range(1,T+1) if (a*q+s)%b==0 and
          certificate((a*q+s)//b,q-(a*q+s)//b)} for s in (-1,1)}
    return T,R
families=0
for b in range(2,31):
    for a in range(1,b):
        if gcd(a,b)>1: continue
        T,R=exact_denominator_masks(a,b)
        assert R[1]=={-q%T for q in R[-1]}
        q0=pow(a,-1,b)
        h0,n0=(a*q0-1)//b,q0-(a*q0-1)//b
        W=bytes(int(certificate(h0+a*t,n0+(b-a)*t)) for t in range(110))
        centers=[z for z in range(110) if all(W[t]==W[(z-t)%110] for t in range(110))]
        shifts={(-2*q0-b*z)%T for z in centers}
        assert all({(q+shift)%T for q in R[-1]}==R[1] for shift in shifts)
        assert bool(shifts)==(b%2==0 and (a%5==0 or (2*a-b)%5==0))
        shift_candidates=[d for d in range(T) if d%b==(-2*q0)%b]
        brute={d for d in shift_candidates if {(q+d)%T for q in R[-1]}==R[1]}
        assert brute==shifts
        if shifts:
            assert len(shifts)==(11 if (a+b)%11==0 else 1)
            expected_period=(10 if (a+b)%11==0 else 110)
            assert all(any(W[t]!=W[(t+k)%110] for t in range(110))
                       for k in range(1,expected_period))
            assert all(W[t]==W[(t+expected_period)%110] for t in range(110))
        families+=1
assert families==277
print('DIRECT_RATIONAL_ANCHORS b<=30:',families,'; ALL DENOMINATOR SHIFT SETS EXACT')
for a,b in [(1,2),(1,7),(1,12),(3,16),(5,16)]:
    q0=pow(a,-1,b)
    h0=(a*q0-1)//b; n0=q0-h0
    W=bytes(int(certificate(h0+a*t,n0+(b-a)*t)) for t in range(110))
    centers=[z for z in range(110) if all(W[t]==W[(z-t)%110] for t in range(110))]
    shifts=sorted({(-2*q0-b*z)%(110*b) for z in centers})
    print('ANCHOR',f'{a}/{b}','CENTERS',centers,'SHIFTS',shifts)
T,R=exact_denominator_masks(5,6)
assert len({d for d in range(T) if R[1]=={(q+d)%T for q in R[-1]}})==11
print('FIVE_SIXTHS: 11 VALID DELAYS; PERIOD 10b PASS')
assert 168 in [(-2*1-2*z)%220 for z in range(110) if z==25]
print('ALL PASS')
