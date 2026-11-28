#!/usr/bin/env python3
"""Exact 11/17 finite-field certificates and their CRT residue-pair union.

Recomputes local tables from pinned rational constants. Uses only Python stdlib.
"""
from collections import Counter
from fractions import Fraction
from math import gcd

U = Fraction(4822040484,8132285009)
GAMMA = Fraction(141024,1653649)

def analyze(p):
    def red(q):
        return q.numerator*pow(q.denominator,-1,p)%p
    u,g=red(U),red(GAMMA)
    inv637=pow(637,-1,p)
    rows=[]
    for x in range(p):
        L=(637-3*x)*inv637%p
        M=u*(1+g*x)%p
        a=(1-(1-x)*L)%p
        b=(1-(1-x)*M)%p
        rows.append((x,a,b,L,M))
    singular=[r for r in rows if r[3]==r[4]]
    assert len(singular)==1 and singular[0][1]==singular[0][3]!=0
    sx=singular[0][0]
    c,d=red(Fraction(-3,637)),u*g%p
    assert c!=d
    def vals(h,n):
        out=[]
        for x,a,b,L,M in rows:
            if L!=M:
                q=(pow(a,h,p)*pow(L,n,p)-pow(b,h,p)*pow(M,n,p))*pow((L-M)%p,-1,p)%p
            else:
                q=pow(L,n-1,p)*pow(a,h-1,p)*(n*a-h*(1-x)*L)%p
            out.append(q)
        out.append((pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p)%p)
        return out
    patterns=set()
    table={}
    for hr in range(p-1):
        good=[]
        for nr in range(p-1):
            h,n=hr or p-1,nr or p-1
            if all(v for i,v in enumerate(vals(h,n)) if i!=sx):
                patterns.add((hr,nr))
                good.append(nr)
        table[hr]=good
    modulus=p*(p-1)
    class_counts=Counter()
    class_count=0
    for h in range(1,modulus+1):
        for n in range(1,modulus+1):
            predicted=((h%(p-1),n%(p-1)) in patterns
                       and (n-(1-sx)*h)%p!=0)
            observed=all(vals(h,n))
            assert predicted==observed,(p,h,n,predicted,observed)
            if observed:
                class_counts[(h%2,n%2)]+=1
                class_count+=1
    return dict(p=p,singular=singular[0],slopes=(c,d),
                patterns=patterns,table=table,modulus=modulus,
                counts=class_counts,class_count=class_count)

r11=analyze(11)
r17=analyze(17)
assert r11['singular']==(3,10,10,10,10)
assert r17['singular']==(4,8,8,8,8)
assert (len(r11['patterns']),r11['class_count'])==(44,4840)
assert (len(r17['patterns']),r17['class_count'])==(96,26112)
assert r11['counts']==Counter({(1,0):1760,(0,1):1760,(1,1):880,(0,0):440})
assert r17['counts']==Counter({(1,1):10880,(1,0):6528,(0,1):6528,(0,0):2176})

M=14960
assert M%110==M%272==0 and gcd(110,272)==2
A=r11['class_count']*(M//110)**2
B=r17['class_count']*(M//272)**2
I=sum(r11['counts'][v]*r17['counts'][v] for v in
      [(0,0),(0,1),(1,0),(1,1)])
union=A+B-I
assert (A,B,I,union)==(89520640,78988800,33510400,134999040)
assert Fraction(union,M*M)==Fraction(564,935)

print('p=11: 44 mod-10 patterns; 4840 mod-110 pairs')
print('p=17: 96 mod-16 patterns; 26112 mod-272 pairs')
for h in range(16):
    print('p17 h mod 16 =',h,'n mod 16 =',r17['table'][h])
print('parity 11:',dict(sorted(r11['counts'].items())))
print('parity 17:',dict(sorted(r17['counts'].items())))
print('CRT joint modulus:',M)
print('p11 certified lifts:',A,'p17 certified lifts:',B,'intersection:',I)
print('union:',union,'of',M*M,'fraction:',Fraction(union,M*M))
print('ALL PASS')
