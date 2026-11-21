#!/usr/bin/env python3
"""Exact local Farey residual certificate for frozen BRC16943/EC49FVS.
Only standard-library integer arithmetic and Fraction are used.
"""
from fractions import Fraction as F
from math import gcd

p=11
U,Gamma=F(4822040484,8132285009),F(141024,1653649)
red=lambda x:(x.numerator*pow(x.denominator,-1,p))%p
u,g,inv=red(U),red(Gamma),pow(637,-1,p)
rows=[]
for z in range(p):
    la,lb=(637-3*z)*inv%p,u*(1+g*z)%p
    a,b=(1-(1-z)*la)%p,(1-(1-z)*lb)%p
    rows.append((z,a,b,la,lb))
c,d=-3*inv%p,u*g%p
pat={(h%10,n%10) for h in range(1,11) for n in range(1,11)
     if all((pow(a,h,p)*pow(la,n,p)-pow(b,h,p)*pow(lb,n,p))*pow((la-lb)%p,-1,p)%p
            for z,a,b,la,lb in rows if z!=3)
     and (pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p)%p}
assert len(pat)==44 and (1,1) not in pat
cert=lambda h,n:(h%10,n%10) in pat and (9*h+10*n)%11!=0

def direct(h,n):
    for z,a,b,la,lb in rows:
        if z==3:
            v=pow(la,n-1,p)*pow(a,h-1,p)*(n*a-h*(1-z)*la)%p
        else:
            v=(pow(a,h,p)*pow(la,n,p)-pow(b,h,p)*pow(lb,n,p))*pow((la-lb)%p,-1,p)%p
        if v==0:return False
    return (pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p)%p!=0
assert all(cert(h,n)==direct(h,n) for h in range(1,111) for n in range(1,111))
print('PROJECTIVE 12100/12100 PASS')

sets={
    'half-left':{m for m in range(110) if cert(m,m+1)},
    'half-right':{m for m in range(110) if cert(m+1,m)},
    'zero-end':{n for n in range(110) if cert(1,n)},
    'one-end':{h for h in range(110) if cert(h,1)},
}
def max_cyclic_step(S):
    v=sorted(S)
    return max([b-a for a,b in zip(v,v[1:])]+[v[0]+110-v[-1]])
for key,expected in [('half-left',(80,3)),('half-right',(80,3)),
                     ('zero-end',(50,5)),('one-end',(50,6))]:
    actual=(len(sets[key]),max_cyclic_step(sets[key]))
    assert actual==expected,(key,actual)
    print('RESIDUE',key,'count',actual[0],'maximum-cyclic-step',actual[1])

def nearest(H):
    top=(H-1)//2
    ml=max(m for m in range(1,top+1) if cert(m,m+1))
    mr=max(m for m in range(1,top+1) if cert(m+1,m))
    nl=max(n for n in range(1,H) if cert(1,n))
    hh=max(h for h in range(1,H) if cert(h,1))
    ql,qr,q0,q1=2*ml+1,2*mr+1,nl+1,hh+1
    assert H-5<=min(ql,qr)<=H and H-4<=q0<=H and H-5<=q1<=H
    assert 2*ql>H and 2*qr>H and 2*q0>H and 2*q1>H
    half_gap=F(1,2*ql)+F(1,2*qr)
    assert F(1,H)<=half_gap<=F(1,H-5)
    return ql,qr,q0,q1,half_gap

for H in range(11,1001):
    ql,qr,q0,q1,half_gap=nearest(H)
    if H<=180:
        vals=[F(h,d) for d in range(2,H+1) for h in range(1,d)
              if gcd(h,d)==1 and cert(h,d-h)]
        assert min(vals)==F(1,q0)
        assert max(vals)==1-F(1,q1)
        assert max(x for x in vals if x<F(1,2))==F(ql-1,2*ql)
        assert min(x for x in vals if x>F(1,2))==F(qr+1,2*qr)
print('ALL HEIGHTS 11..1000 LOCAL THEOREM PASS; DIRECT 11..180 PASS')

def farey_global_max(H):
    a,b,c,d=0,1,1,H
    la,lb=0,1
    best_n,best_d=0,1
    witness=None
    ncert=0
    while True:
        ok=(c==1 and d==1) or cert(c,d-c)
        if ok:
            ncert+=1
            dn=c*lb-la*d
            dd=d*lb
            if dn*best_d>best_n*dd:
                best_n,best_d=dn,dd
                witness=(la,lb,c,d)
            la,lb=c,d
        if c==1 and d==1:break
        k=(H+b)//d
        a,b,c,d=c,d,k*c-a,k*d-b
    return ncert,F(H*best_n,best_d),witness

for H in (128,256,512,1024,2048,4096,8192):
    ncert,gap,w=farey_global_max(H)
    print('EXACT_FAREY',H,'certified_plus_one=',ncert,
          'H_times_global_max_gap=',gap,'witness=',f'{w[0]}/{w[1]}->{w[2]}/{w[3]}')
print('UNIVERSAL GLOBAL C=1+o(1) REMAINS A CONJECTURE, NOT A THEOREM')
print('ALL PASS')
