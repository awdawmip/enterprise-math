#!/usr/bin/env python3
"""Self-contained author-side exact N29 certificate recomputation.
Only Python stdlib. Auxiliary four-label BRC, not native X6 physics.
Produces verified counts and exceptions WITHOUT a precomputed TSV or JSON.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import comb
N=29

def trim(x):
    while len(x)>1 and x[-1]==0:x.pop()
    return tuple(x)

def Nmass(c):
    x,y,u,v=c
    out=[0]*(x+1)
    def add(f,a,b):
        for j in range(x+1):out[j]+=f*comb(x,j)*a**(x-j)*b**j
    add(2**(u+v),1,1)
    out[0]+=2**(x+v)
    add(2**u,2,1)
    add(2**y,2,-1)
    if x==0:out[0]-=1
    if y==0:add(-3,1,1)
    if u==0:add(-2,1,-1)
    if v==0:out[0]-=2
    return trim(out)

def D(c,a):
    old=Nmass(c);newc=list(c);newc[a]+=1;new=Nmass(newc)
    p=[0]*max(len(old),len(new))
    for k,x in enumerate(old):p[k]-=3*x
    for k,x in enumerate(new):p[k]+=x
    return trim(p)

def interval_min(p,l=F(),r=F(1)):
    # Exact monomial substitution z=l+(r-l)*w, Bernstein lift to degree N.
    shifted=[sum((F(p[j])*comb(j,k)*l**(j-k)*(r-l)**k
                  for j in range(k,len(p))),F()) for k in range(len(p))]
    return min(sum((shifted[j]*F(comb(k,j),comb(N,j))
                    for j in range(min(k,len(shifted)-1)+1)),F()) for k in range(N+1))

def vecs(total):
    for x in range(total+1):
      for y in range(total-x+1):
       for u in range(total-x-y+1):yield x,y,u,total-x-y-u

def multiplicity(c):
    r=1;m=sum(c)
    for t in c:r*=comb(m,t);m-=t
    return r

def inc(w,t):
    c=[0,0,0,0]
    for x in w[:t-1]:c[int(x)]+=1
    return D(c,int(w[t-1]))

def delta(w,t):
    c=[0,0,0,0]
    for x in w[:t]:c[int(x)]+=1
    return Nmass(c)

def evaluate(p,z):return sum((F(x)*z**k for k,x in enumerate(p)),F())

classes=defaultdict(int);frozen=0;nonfrozen=0;vectors=0
for c in vecs(N-1):
    mult=multiplicity(c)
    if all(c):frozen+=4*mult;continue
    for a in range(4):
        vectors+=1;classes[D(c,a)]+=mult;nonfrozen+=mult
assert vectors==6280==8*((N-1)**2+1)
assert len(classes)==4270
assert frozen==287864353914883296
assert nonfrozen==366022236828448==16*3**28-24*2**28+16
assert frozen+nonfrozen==4**N
negative=[];exception=[]
for p,n in classes.items():
    m=interval_min([-x for x in p])
    if m>0:negative.append((p,n,m))
    else:exception.append((p,n))
assert len(negative)==4268
assert min(row[2] for row in negative)==49146
assert sum(row[1] for row in negative)==366022236828419
assert sorted(n for p,n in exception)==[1,28]

E=D((28,0,0,0),0);Z=D((27,0,1,0),0)
assert set(p for p,n in exception)=={E,Z}
assert evaluate(E,F())<0<evaluate(E,F(1))
assert evaluate(Z,F())<0<evaluate(Z,F(1))
EE=F(499993,500000);ZZ=F(4999999999999,5000000000000)
assert interval_min([-x for x in E],F(),EE)>0
assert interval_min([-x for x in Z],F(),ZZ)>0
assert sum(x*y<0 for x,y in zip([a for a in reversed(Z) if a],[a for a in reversed(Z) if a][1:]))==1
for t in range(2,N):assert interval_min(inc('0'*N,t),EE,F(1))>0
for k in range(1,N):
    w='0'*(k-1)+'2'+'0'*(N-k)
    for t in range(2,N):
        sign=-1 if k>=4 and t==k else 1
        assert interval_min([sign*x for x in inc(w,t)],ZZ,F(1))>0,(k,t)
    if k>=4:
        small=delta(w,k-1);large=delta(w,N)
        gap=[0]*max(len(small),len(large))
        for j,x in enumerate(small):gap[j]+=3**(N-k+1)*x
        for j,x in enumerate(large):gap[j]-=x
        assert interval_min(gap,ZZ,F(1))>0
lo,hi=ZZ,F(1)
for _ in range(240):
    md=(lo+hi)/2
    if evaluate(Z,md)>0:hi=md
    else:lo=md
s=10**40
left=F(lo.numerator*s//lo.denominator,s);right=left+F(1,s)
assert evaluate(Z,left)<0<evaluate(Z,right)
print('N29_STANDALONE_EXACT_PASS', {'total':4**N,'frozen':frozen,'nonfrozen':nonfrozen,'count_action_classes':vectors,'polynomials':len(classes),'strict_negative':len(negative),'exceptional_words':sum(n for p,n in exception),'bernstein_min':49146,'positive_gain_words':25})
print('Z29_UNIQUE_POSITIVE_ROOT_BRACKET',left,right)
print('ALL_N_Z1_PULSE_THEOREM: for every n>=4, p=0002 + 0^(n-4), R_n=1/81-1/3^n; the proof is elementary, not this finite script.')
