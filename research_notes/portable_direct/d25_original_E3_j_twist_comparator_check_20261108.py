#!/usr/bin/env python3
"""D25 original E3 CM j-fiber/twist discriminator.
Exact standard-library author-side arithmetic, NOT native H0/B0.
"""
import math

H0 = 14670139392
H1728 = 1728**2 - 4834944 * 1728 + H0
JC = 2417472
JS = 1707264

def primes(n):
    sieve = [True]*(n+1)
    sieve[:2] = [False,False]
    for x in range(2, math.isqrt(n)+1):
        if sieve[x]:
            for y in range(x*x,n+1,x):
                sieve[y] = False
    return [p for p in range(n+1) if sieve[p]]

def add(a,b,p): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def neg(a,p): return ((-a[0])%p,(-a[1])%p)
def sub(a,b,p): return add(a,neg(b,p),p)
def mul(a,b,p): return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def scale(a,v,p): return (a[0]*v%p,a[1]*v%p)
def inv(a,p):
    norm = (a[0]*a[0]-2*a[1]*a[1])%p
    assert norm != 0
    return scale((a[0],-a[1]),pow(norm,-1,p),p)
def quotient(a,b,p): return mul(a,inv(b,p),p)
def power(a,n,p):
    out = (1,0)
    for _ in range(n): out = mul(out,a,p)
    return out

def curve_j(p):
    one=(1,0)
    s=(0,1)
    t=scale(sub((2,0),s,p),pow(4,-1,p),p)
    c=scale(t,pow(27,-1,p),p)
    c4=sub(one,scale(c,24,p),p)
    delta=mul(power(c,3,p),sub(one,scale(c,27,p),p),p)
    return quotient(power(c4,3,p),delta,p)

assert H1728==6318342144
assert H0==2**12*3**6*17**3
assert H1728==2**14*3**6*23**2
assert JS==2**8*3**3*13*19
ps=[p for p in primes(2000) if p%24 in (13,19)]
assert len(ps)==77
for p in ps:
    assert pow(2,(p-1)//2,p)==p-1
    assert H0%p and H1728%p
    actual=curve_j(p)
    expected=(JC%p,JS%p)
    assert actual==expected,(p,actual,expected)
    assert actual != (0,0) and actual != (1728%p,0)
    assert (actual[1]==0)==(p in (13,19))
    assert (p in (13,19))==(JS%p==0)
    hval=sub(sub(power(actual,2,p),scale(actual,4834944,p),p),(-H0,0),p)
    assert hval==(0,0),(p,hval)

for p in (13,19,373):
    print(f'p={p}, original_j={curve_j(p)}, j_1728={1728%p}, conjugate_difference_coefficient={2*JS%p}, H0_mod_p={H0%p}, H1728_mod_p={H1728%p}')
print('PASSED:',len(ps),'exact target primes <=2000; original E3 j and Hilbert polynomial, nonexceptional j, only p13/p19 coalescence')

# Exact original-curve geometric comparison at two coalescence primes.
for p in (13,19):
    j=JC%p
    den=(1728-j)%p
    a=(3*j*pow(den,-1,p))%p
    b=(2*j*pow(den,-1,p))%p
    def character(x):
        if x==0: return 0
        return 1 if pow(x,(p-1)//2,p)==1 else -1
    ap=-sum(character((x*x*x+a*x+b)%p) for x in range(p))
    assert ap==0
    c=scale(sub((2,0),(0,1),p),pow(108,-1,p),p)
    c4=sub((1,0),scale(c,24,p),p)
    c6=add(sub((-1,0),scale(c,-36,p),p),scale(power(c,2,p),-216,p),p)
    c4ref=(-48*a)%p
    c6ref=(-864*b)%p
    d=mul(mul(c6,(c4ref,0),p),inv(mul(c4,(c6ref,0),p),p),p)
    dnorm=(d[0]*d[0]-2*d[1]*d[1])%p
    assert pow(dnorm,(p-1)//2,p)==p-1,(p,d,dnorm)
    def chi2(v):
        norm=(v[0]*v[0]-2*v[1]*v[1])%p
        return character(norm)
    total=0
    for xx in range(p):
        for yy in range(p):
            x=(xx,yy)
            disc=add(power(add(x,c,p),2,p),scale(power(x,3,p),4,p),p)
            total+=chi2(disc)
    actual_count=p*p+1+total
    assert actual_count==(p-1)**2
    assert (p+1)**2+actual_count==2*(p*p+1)
    print(f'p={p}, E_ref:y^2=x^3+{a}x+{b}, a_p={ap}, twist_d={d}, norm_d={dnorm} (nonsquare), E_ref(Fp2)={(p+1)**2}, original_E3(Fp2)={actual_count}')
