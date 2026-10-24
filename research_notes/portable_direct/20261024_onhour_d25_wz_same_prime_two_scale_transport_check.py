"""D25 author-side exact fixed-p WZ rank transport, not native benchmark."""
from fractions import Fraction
from math import factorial, isqrt

def primes_upto(N):
    return [p for p in range(2,N+1) if all(p%d for d in range(2,isqrt(p)+1))]
def P(k,n):
    return (27*n**4+(324*k+180)*n**3+(1836*k*k+1746*k+429)*n*n
            +(4320*k**3+5940*k*k+2706*k+412)*n+3456*k**4+6336*k**3+4128*k*k+1184*k+128)
def gpair(k,n):
    return (4*n*P(k,n),9*(n+2*k+1)*(n+4*k+1)*(n+4*k+2)*(n+4*k+3)*(6*n+12*k+1))
def strip(x,p):
    assert x>0
    v=0
    while x%p==0:x//=p;v+=1
    return v,x
def valmod(pair,p,M):
    v,u=pair
    assert v>=0
    return 0 if v>=3 else p**v*u%M
def stream(r,N,p):
    M=p**3
    assert 6*r<p
    A=factorial(6*r)*pow(3**(6*r)*factorial(2*r)**3,-1,M)%M
    v=0;u=1;out=[]
    for j in range(N+1):
        vL,L=strip(6*j+12*r+1,p)
        out.append((v+vL,A*u*L%M))
        if j==N:break
        num=(4*r+2*j+1)*(3*j+1)*(3*j+2)
        den=36*(j+1)*(2*r+j+1)*(4*r+j+1)
        vn,un=strip(num,p);vd,ud=strip(den,p)
        v+=vn-vd
        assert v>=0
        u=u*un*pow(ud,-1,M)%M
    return out
def exactS(r):
    A=Fraction(factorial(6*r),3**(6*r)*factorial(2*r)**3)
    rho=Fraction(1);s=Fraction(0)
    for n in range(4*r+1):
        s+=A*(6*n+12*r+1)*rho
        if n<4*r:
            rho*=Fraction((4*r+2*n+1)*(3*n+1)*(3*n+2),
                         36*(n+1)*(2*r+n+1)*(4*r+n+1))
    return s
def vfrac(x,p):
    a,b=x.numerator,x.denominator
    if a==0:return 9999
    v=0
    while a%p==0:a//=p;v+=1
    while b%p==0:b//=p;v-=1
    return v
def fmod(x,p,n):
    a,b=x.numerator,x.denominator
    while a%p==b%p==0:a//=p;b//=p
    assert b%p
    return a*pow(b,-1,p**n)%(p**n)

steps=early=late=prime_count=0
third211=[]
for p in primes_upto(1000):
    if p%6!=1:continue
    m=(p-1)//6;lo=(m+1)//2;hi=(3*m-4)//4
    if lo>=m:continue
    prime_count+=1;M=p**3
    for k in range(lo,m):
        steps+=1;N=4*k+1
        old=stream(k,N,p);new=stream(k+1,N+3,p)
        gn,gd=gpair(k,N);vn,un=strip(gn,p);vd,ud=strip(gd,p)
        vg=vn-vd;ug=un*pow(ud,-1,M)%M
        v,u=old[N];five=[(v+vg,u*ug%M)]+new[N:N+4]
        assert len(five)==5 and all(z[0]>=1 for z in five)
        delta=(sum(valmod(z,p,M) for z in new[:N+4])
               -sum(valmod(z,p,M) for z in old[:N]))%M
        rhs=sum(valmod(z,p,M) for z in five)%M
        assert delta==rhs and delta%p==0,(p,k)
        if k<=hi:
            early+=1
            assert all(z[0]>=2 for z in five)
            assert delta%(p*p)==0
            if p==211:third211.append(delta//(p*p)%p)
        else:late+=1
assert (steps,early,late,prime_count)==(3027,1471,1556,79)
assert third211==[109,148,89,22,3,49,191,116]
p=37
s3,s4,s5=(exactS(r) for r in (3,4,5))
assert vfrac(s4-s3,p)==2 and fmod(s4-s3,p,3)==36*p*p
assert vfrac(s5-s4,p)==1 and fmod(s5-s4,p,2)==19*p
p=211;M=p**3
s18=sum(valmod(z,p,M) for z in stream(18,72,p))%M
s26=sum(valmod(z,p,M) for z in stream(26,104,p))%M
assert (s26-s18)%M==94*p*p
print("PASS p transport 3027, p² plateau 1471, p=37 sharpness, p=211 eight-step 94")
