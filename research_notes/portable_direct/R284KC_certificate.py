from fractions import Fraction as F
from math import factorial

def envelope(S,real=False):
    h=F(1,600); r=(2+2*h)*S*h
    Q=(2+2*h)*S*S*(1+2*h)/(1-r)
    K=max(2*S,Q) if real else 2*S+Q
    assert K*h<1
    Perr=K/(1-K*h); M=1+Perr*h
    den=F(1) if real else 1-S*h*(1+h)/2
    Tmax=S*(1+h/2)/den
    Terr=(S/2+S*S*(1+h)/2)/den
    vmax=(F(1,6)+h*(1+h)**2)*M
    verr=Perr/6+(1+h)**2*M+(1+S/2)/2
    W=max(1,S-1) if real else 1+S
    Wt=max(1,Tmax-1) if real else 1+Tmax
    Jder=W+S/2+2*S*W
    Jw=(1+h)*(F(1,2)+h)*Wt
    Xw=(1+h)/2*W
    Aw=(1+h)*Wt
    if real:
        Jw=min(Jw,(1+h)*(F(1,2)+h)+S*(F(1,12)+h*(1+h)*(2+h)/6)+S*h/2*(F(1,6)+h*(1+h)/2))
        Xw=min(Xw,(1+h)/2+S/12)
        Aw=min(Aw,(1+h)*(1+S*(2+h)/6+S*h/4))
    jmax=Jw*M
    jerr=Xw*Perr+(1+h)/2*Terr*M+Aw*M+Jder/2+1
    berr=verr+jmax; bmax=vmax+h*jmax
    Gmax=((F(3,2)*S/(1-S*h))+(1+2*h)*S*S/(1-S*h)**2)/(2*(2-S*h*h/(1-S*h)))
    gmax=Gmax*(vmax+bmax)
    amax=(vmax+bmax)/4+h*h*gmax; aerr=(verr+berr)/4+h*gmax
    e0max=M*(2+3*h)/(2*(2-2*S*h-S*h*h))*(2+S*h+2*S*h*h)/(8-4*S*h-2*S*h*h)
    p1err=24*S+3*S*S*(3+h)**2
    Pmax=48+h*(72*S+h*p1err); Tbound=96+32*S*h*(1+h)
    return sum([24*(aerr*jmax+jerr/12),p1err*amax*bmax+72*S*(aerr*bmax+berr/12),32*S*amax**2+32*S*aerr*(amax+F(1,12)),96*amax*gmax,Pmax*e0max*bmax,Tbound*(2*amax*S*(vmax+bmax)+S*S*h*h*(vmax+bmax)**2)])

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): c[i+j]+=u*v
    return c

def integ(a): return sum((v/F(i+1) for i,v in enumerate(a)),F(0))
psi=[F(1,6),-1,F(3,2)]
weights=[[0,1,-1],[0,1],[0,1,-2,1]]
weights += [mul(w,psi) for w in weights]
coeff=[]
for w in weights:
    a=[]; p=[F(1)]
    for k in range(17):
        a.append((-1)**k*integ(mul(w,p))/factorial(k));p=mul(p,psi)
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
def limits(s):
    vals=[(horner(a[:-1],s),horner(a,s)) for a in coeff]
    I,U,B=vals[:3];J=sub(U,scale(B,s))
    L=sub(scale(prod(I,I),28*s),scale(prod(I,J),12))
    Ip,Up,Bp=map(neg,vals[3:]);Jp=sub(sub(Up,B),scale(Bp,s))
    Lp=sub(plus(scale(prod(I,I),28),scale(prod(I,Ip),56*s)),scale(plus(prod(Ip,J),prod(I,Jp)),12))
    return L,Lp
# Lipschitz bounds of shifted limit: psi in [0,2/3].
I0,I1,I2=F(1,6),F(1,9),F(2,27)
J0,J1,J2=F(5,6),F(23,36),F(13,27)
assert 28*I0**2+224*I0*I1+12*(I1*J0+I0*J1)<8
assert 112*I0*I1+224*(I1**2+I0*I2)+12*(I2*J0+2*I1*J1+I0*J2)<12
# All closed intervals covered by nearest grid node at distance <= 1/800.
vals={i:limits(F(i,400)) for i in range(1601)}
blocks=[(0,300,-1)]+[(i,i+50,1) for i in range(500,1600,50)]
for i,j,sgn in blocks:
    margin=min((vals[k][0][0] if sgn==1 else -vals[k][0][1]) for k in range(i,j+1))-F(8,800)
    E=envelope(F(j,400),True)
    assert margin>0 and E<520*margin
margin=min(vals[k][1][0] for k in range(300,501))-F(12,800)
assert margin>F(743,1000)
assert envelope(F(2))/F(3,4)<440
assert F(743,1000)-F(440,600)>F(9,1000)
assert envelope(F(5,4),True)<91
assert F(91)/(F(743,1000)*F(3,4)*F(9,10))<182
print('1601 exact rational grid nodes; 23 exterior blocks PASS; E/margin < 520')
print('scaled limit derivative > 743/1000; complex error derivative < 440/d')
print('d>=600: scaled exact derivative > 9/1000; local value error < 91/d; q error < 182*d')
