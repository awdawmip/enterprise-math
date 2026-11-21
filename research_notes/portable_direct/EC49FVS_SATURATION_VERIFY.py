from fractions import Fraction as Q
from math import gcd,lcm
from functools import reduce
from collections import defaultdict
p=11
U,Gamma=Q(4822040484,8132285009),Q(141024,1653649)
red=lambda x: (x.numerator*pow(x.denominator,-1,p))%p
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
assert len(pat)==44

def direct(h,n):
    for z,a,b,la,lb in rows:
        if z==3:
            v=(pow(la,n-1,p)*pow(a,h-1,p)*(n*a-h*(1-z)*la))%p
        else:
            v=((pow(a,h,p)*pow(la,n,p)-pow(b,h,p)*pow(lb,n,p))
                *pow((la-lb)%p,-1,p))%p
        if v==0: return False
    return (pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p)%p != 0

cert=lambda h,n: (h%10,n%10) in pat and (9*h+10*n)%11 !=0
assert all(cert(h,n)==direct(h,n) for h in range(1,111) for n in range(1,111))
print('12100 independent direct projective checks PASS',flush=True)
L=84915883381329
C=2*L
M=14080*C
rs=[r for r in range(1,129,2) if L%r==0]
menu=[(r,e) for r in rs for e in range((r-1).bit_length(),8)]
assert len(menu)==65
print('MENU',rs, menu,flush=True)

def layer(j,r,e,level):
    step=C*2**e//(2**level*r)
    assert C*2**e%(2**level*r)==0
    assert M%step==0 and M//step%lcm(110,2*r)==0
    n=(r*pow(2,j+level-e,110))%110
    return {step*h for h in range(1,M//step) if gcd(h,2*r)==1 and cert(h,n-h)}

def gap(points):
    a=sorted(points)
    return max(a[0]+M-a[-1],max(v-u for u,v in zip(a,a[1:])))

expected={}
for j in range(14,34):
    current=set()
    adds=defaultdict(set)
    for r,e in menu:
        current.update(layer(j,r,e,0))
        t=Q(2*r,2**e)
        adds[t].update(layer(j,r,e,1))
    upper=Q(0)
    witness=None
    stages=[]
    for t in sorted(adds):
        if t<=1:
            current.update(adds[t]);continue
        g=Q(gap(current),C)
        stages.append((str(t),str(g),len(current)))
        if t*g>upper:
            upper=t*g
            witness=(upper,g,t)
        current.update(adds[t])
    assert len(current)>0
    print('j=',j,'worst=',str(upper),'gap=',str(witness[1]),'cutoff=',str(witness[2]),'points=',len(current),flush=True)
    expected[j]=witness
print('overall max',max(v[0] for v in expected.values()),flush=True)

assert expected[14][0]==Q(160,63) and expected[15][0]==Q(1365,506)
assert all(expected[j][0]==expected[j+2][0] for j in range(14,32))
assert max(v[0] for v in expected.values())==Q(1365,506)
print('20 exponent classes, 65-layer stagewise optimum and witnesses PASS',flush=True)

# Independent finite-height enumeration with literal denominator and reduced numerator.
CAND=Q(1365,506)
for j in range(8,12):
    k=2**j
    heights=sorted({k, 11*k//8-1, 11*k//8, 91*k//64-1, 91*k//64, 2*k-1})
    for H in heights:
        pts={0,C*k}
        for level in (0,1):
            for r,e in menu:
                den=(2**level)*r*2**(j-e)
                if den>H: continue
                step=C*k//den
                assert C*k%den==0
                pts.update(step*h for h in range(1,den)
                           if gcd(h,den)==1 and cert(h,den-h))
        a=sorted(pts)
        maxgap=max(b-a for a,b in zip(a,a[1:]))
        assert Q(maxgap*H,C*k)<=CAND,(j,H,Q(maxgap*H,C*k))
    print('independent direct fraction validation PASS: j',j,'heights',len(heights),flush=True)
print('THEOREM H>=256 interval length >1365/(506H) implies 11-adic-certified phase',flush=True)
print('ALL PASS',flush=True)
