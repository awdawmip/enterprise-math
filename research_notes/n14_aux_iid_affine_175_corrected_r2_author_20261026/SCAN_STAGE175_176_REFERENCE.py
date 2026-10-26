#!/usr/bin/env python3
"""Stage175 corrected tangent and Stage176 exact first-gap ray scans.
Checks two finite Bellman piecewise-affine calculations; no primal Stage176.
"""
from functools import lru_cache
from fractions import Fraction as F

N=14
P=(F(1,8),F(1,24),F(5,6))
T=(8,2,0)
Z=(14,0,0)
B=(6,3,3)
A=('P','Q','C')

def ell(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return s[0]+1,s[1]+int(i==0),s[2]+int(i==1)
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def scale(k,x):return tuple(k*a for a in x)

def scan(K0,L0,choosers,dK,dL):
    @lru_cache(None)
    def bell0(s):
        v=[K0*ell(s),L0]
        if s[0]<N:
            v.append(1+sum((P[i]*bell0(child(s,i))[0] for i in range(3)),F(0)))
        m=min(v)
        return m,tuple(a for a,x in zip(A,v) if x==m)
    @lru_cache(None)
    def affine(s):
        options={'P':(F(0),ell(s),F(0)),'Q':(F(0),F(0),F(1))}
        if s[0]<N:
            v=(F(1),F(0),F(0))
            for i in range(3):v=add(v,scale(P[i],affine(child(s,i))[0]))
            options['C']=v
        w=bell0(s)[1]
        chosen=choosers.get(s,w[0])
        assert chosen in w
        return options[chosen],options,chosen
    steps=[]
    zero=[]
    for n in range(N+1):
        for a in range(n+1):
            for b in range(n-a+1):
                s=(n,a,b)
                base,options,selected=affine(s)
                assert base[0]+K0*base[1]+L0*base[2]==bell0(s)[0]
                for action,v in options.items():
                    if action==selected:continue
                    gap=(v[0]-base[0])+K0*(v[1]-base[1])+L0*(v[2]-base[2])
                    deriv=(v[1]-base[1])*dK+(v[2]-base[2])*dL
                    assert gap>=0
                    if gap==0:
                        assert deriv>=0
                        zero.append((s,action,deriv))
                    elif deriv<0:steps.append((-gap/deriv,s,action))
    steps.sort()
    step=steps[0][0]
    K=K0+step*dK
    L=L0+step*dL
    @lru_cache(None)
    def bell(s):
        options=[K*ell(s),L]
        if s[0]<N:
            options.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0)))
        v=min(options)
        return v,tuple(a for a,x in zip(A,options) if x==v),options
    ties={}
    strict=[]
    for n in range(N+1):
        for a in range(n+1):
            for b in range(n-a+1):
                s=(n,a,b)
                v,w,options=bell(s)
                if len(w)>1:ties[s]=w
                strict.extend(x-v for x in options if x>v)
    assert len(strict)==1238 and len(ties)==2
    return (K,L,bell((0,0,0))[0],step,ties,min(strict),len(steps),zero,affine)

K0=L0=F(16044588,70019)
# Derive the unique affine tangent keeping T's P/continue equality.
_,_,_,_,_,_,_,_,aff0=scan(K0,L0,{T:'P',Z:'Q'},F(-1),-F(169640,99621))
a=aff0(T)[1]
diff=tuple(a['P'][i]-a['C'][i] for i in range(3))
assert diff==(F(-148561,124416),F(21205,1679616),F(-11069,1492992))
rho=-diff[1]/diff[2]
assert rho==F(169640,99621)
first=scan(K0,L0,{T:'P',Z:'Q'},F(-1),-rho)
K1,L1,H1,e1,ties1,gap1,num1,zero1,_=first
assert (K1,L1,H1)==(
    F(41521222013193063,181934251842254),
    F(20701458469704504,90967125921127),
    F(53122292194902540973485450586445,311451660365537449574670532608))
assert e1==F(11785669755441343155,12738854379742782826)
assert ties1=={B:('Q','C'),T:('P','C')}
assert gap1==F(152464420746873000396113,3337744988485269306998784)
assert num1==760
second=scan(K1,L1,{T:'P',B:'Q'},F(-1),-rho)
K2,L2,H2,e2,ties2,gap2,num2,zero2,_=second
assert (K2,L2,H2)==(
    F(1696807920718753587,7487608294325270),
    F(168348947995801752,748760829432527),
    F(1733492029996286794626721771839535,10254377114019668494551279992832))
assert e2==F(546791690132072466208602234228,340563103278980896037851489645)
assert ties2=={(4,1,2):('Q','C'),T:('P','C')}
assert gap2==F(152464420746873000396113,4292712684503529027010560)
assert num2==759
print('STAGE175_CORRECTED_RAY_AND_STAGE176_DUAL_ONLY_PASS')
