from fractions import Fraction as F
from math import factorial

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): c[i+j]+=u*v
    return c

def integ(a): return sum((v/F(i+1) for i,v in enumerate(a)),F(0))
phi=[F(1,2),-1,F(3,2)]
weights=[[0,1,-1],[0,1],[0,1,-2,1]] # I,U,B
# Nonnegative weights w and w*phi; degree-23/24 Taylor integral brackets.
weights += [mul(w,phi) for w in weights]
coeff=[]
for w in weights:
    a=[]; p=[F(1)]
    for k in range(25):
        a.append((-1)**k*integ(mul(w,p))/factorial(k));p=mul(p,phi)
    coeff.append(a)
def horner(a,s):
    z=F(0)
    for v in reversed(a):z=z*s+v
    return z

def plus(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return plus(a,neg(b))
def prod(a,b):
    t=[x*y for x in a for y in b];return min(t),max(t)
def scale(a,t):return prod(a,(t,t))
def limits(s,derivative=False):
    vals=[(horner(a[:-1],s),horner(a,s)) for a in coeff[:(6 if derivative else 3)]]
    I,U,B=vals[:3];J=sub(U,scale(B,s))
    L=sub(scale(prod(I,I),28*s),scale(prod(I,J),12))
    if not derivative:return L
    Ip,Up,Bp=map(neg,vals[3:]);Jp=sub(sub(Up,B),scale(Bp,s))
    Lp=sub(plus(scale(prod(I,I),28),scale(prod(I,Ip),56*s)),scale(plus(prod(Ip,J),prod(I,Jp)),12))
    return L,Lp

# Exact node bound verification; all decimals are rationals.
for S,K,Perr,prodmax,verr,jerr,vmax,jmax,berr,bmax,Gmax,gmax,amax,aerr,p1err,errmax in [
    (F(4),61,65,F('1.064'),14,210,F('.18'),F('2.7'),17,F('.183'),6,F('2.3'),F('.092'),8,530,2100),
    (F(3,2),11,12,F('1.012'),4,28,F('.17'),F('1.3'),F('5.3'),F('.172'),F('1.2'),F('.42'),F('.087'),F('2.4'),97,300)]:
    h=F(1,1024); d=1/h
    # absolute log difference of paired numerator/denominator (not two independent Taylor errors)
    assert 2*S + 3*S*S*(1+2*h)/(1-3*S*h) < K
    assert F(K)/(1-K*h)<Perr and 1+Perr*h<prodmax
    den=1-S*h*(1+h)/2
    Tmax=S*(1+h/2)/den
    Terr=(S/2+S*S*(1+h)/2)/den
    assert (1/F(6)+h*(1+h)**2)*prodmax < vmax
    assert F(Perr,6)+(1+h)**2*prodmax+(1+S/2)/2 < verr
    assert (1+h)*(F(1,2)+h)*(1+Tmax)*prodmax < jmax
    assert (1+h)/2*(1+S)*Perr+(1+h)/2*Terr*prodmax+(1+h)*(1+Tmax)*prodmax+(1+3*S+2*S*(1+S))/2+1 < jerr
    assert verr+jmax<=berr and vmax+h*jmax<bmax
    assert ((F(3,2)*S/(1-S*h))+(1+2*h)*S*S/(1-S*h)**2)/(2*(2-S*h*h/(1-S*h)))<Gmax
    assert Gmax*(vmax+bmax)<gmax
    assert (vmax+bmax)/4+h*h*gmax<amax and (verr+berr)/4+h*gmax<aerr
    e0max=F('.14')
    assert prodmax*(2+3*h)/(2*(2-2*S*h-S*h*h))*(2+S*h+2*S*h*h)/(8-4*S*h-2*S*h*h)<e0max
    assert 24*S+3*S*S*(3+h)**2 < p1err
    assert 48+h*(72*S+h*p1err)<49 and 96+32*S*h*(1+h)<97
    terms=[24*(aerr*jmax+F(jerr,12)),p1err*amax*bmax+72*S*(aerr*bmax+F(berr)/12),32*S*amax**2+32*S*aerr*(amax+F(1,12)),96*amax*gmax,49*e0max*bmax,97*(2*amax*S*(vmax+bmax)+S*S*h*h*(vmax+bmax)**2)]
    total=sum(terms); assert total<errmax
    print('S',S,'error bound ceiling',-(-total.numerator//total.denominator),'claimed',errmax)

# Grid certificate: |L'| <= 12 and |L''| <= 24 on [0,4], from integral bounds in KA.
# Every s in either closed exterior interval lies within 1/2000 of its grid.
neg_count=pos_count=0
for i in range(4001):
    if 750<i<1250:continue
    lo,hi=limits(F(i,1000))
    if i<=750: assert hi < -F(1,10);neg_count+=1
    else: assert lo > F(1,10);pos_count+=1
for i in range(150,251):
    _,(lo,hi)=limits(F(i,200),True)
    assert lo>F(1,4)
assert F(1,10)-F(12,2000)==F(47,500)
assert F(1,4)-F(24,400)==F(19,100)
assert F(2100,25000)<F(47,500)
assert F(1200,25000)<F(19,100)-F(14,100)
print('grid',neg_count,pos_count,'derivative',101,'PASS; d>=25000, Fdprime>0.14 on [0.75,1.25]')
