"""Degree-two seed fibers; exact arithmetic in the six original coefficient axes."""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from fractions import Fraction as F
from math import comb, factorial, gcd, isqrt
import json


ONE = (1,0,0,0,0,0)
ZERO = (0,)*6


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def reduce7(a):
    return tuple(t-a[6] for t in a[:6])


def mul(a,b):
    v = [0]*7
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                v[(i+j)%7] += x*y
    return reduce7(v)


def sigma(a,j):
    v = [0]*7
    for i,x in enumerate(a):
        v[i*j%7] = x
    return reduce7(v)


def power(a,n):
    out = ONE
    while n:
        if n&1:
            out = mul(out,a)
        a = mul(a,a)
        n //= 2
    return out


@lru_cache(None)
def hilbert90(v):
    # The ratio v/conjugate(v) classifies F-lines without a chosen p-adic label.
    norm = mul(v,sigma(v,6))
    conjugates = mul(sigma(norm,2),sigma(norm,3))
    full = mul(norm,conjugates)
    assert full[0]>0 and full[1:]==(0,)*5
    numer = mul(mul(v,v),conjugates)
    den = full[0]
    g = gcd(den,*numer)
    return (den//g,)+tuple(a//g for a in numer)


def columns(a):
    return [sigma_shift(a,j) for j in range(6)]


def sigma_shift(a,j):
    v = [0]*7
    for i,x in enumerate(a):
        v[(i+j)%7] = x
    return reduce7(v)


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def finite_tag(v,rho,p):
    a,b = 0,0
    for term in reversed(v):
        a,b = (term-b)%p, (a+rho*b)%p
    assert a or b
    return a*pow(b,-1,p)%p if b else -1


def isprime(p):
    return p>=2 and all(p%j for j in range(2,isqrt(p)+1))


def block(n,conj,r):
    p = n**3-n*n-2*n+1
    assert p%7==6 and isprime(p)
    zeta = (0,1,0,0,0,0)
    gens = [add((n,0,0,0,0,0),add(sigma(zeta,j),sigma(zeta,7-j))) for j in (1,2,3)]
    g = power(gens[conj],r)
    b,c = (a for j,a in enumerate(gens) if j!=conj)
    adj = power(mul(b,c),r)
    assert mul(g,adj)==(p**r,0,0,0,0,0)
    vroot = (1,3,2)[conj]
    trace = [2,-n]
    for _ in range(vroot-1):
        trace.append(-n*trace[-1]-trace[-2])
    root = trace[vroot]%p
    assert (root**3+root**2-2*root-1)%p==0
    assert pow((root*root-4)%p,(p-1)//2,p)==p-1
    bounds = []
    for row in zip(*columns(adj)):
        bnd = 0
        while 42**3*(bnd+1)**6*p**(4*r)<dot(row,row)**3*p:
            bnd+=1
        bounds.append(bnd)
    mod,rat = Counter(),Counter()
    tagmap = {}
    valid = 0
    for v in product(*(range(-j,j+1) for j in bounds)):
        if next((a for a in v if a),0)<=0:
            continue
        x = mul(g,v)
        if 42**3*dot(x,x)**3>=p**(2*r+1):
            continue
        valid += 1
        assert gcd(*v)==gcd(*x)
        if gcd(*x)!=1:
            continue
        finite = finite_tag(v,root,p)
        actual = hilbert90(v)
        assert tagmap.setdefault(actual,finite)==finite
        mod[finite]+=1
        rat[actual]+=1
    assert len(set(tagmap.values()))==len(tagmap)
    assert Counter(mod.values())==Counter(rat.values())
    freq = Counter(mod.values())
    nr = sum(freq.values())
    total = sum(mod.values())
    second = sum(v*v for v in mod.values())
    pairs = sum(comb(v,2) for v in rat.values())
    assert second==total+2*pairs and nr==len(mod)
    # Cross-check each actual rational pair against the full finite line classes.
    freq[0]=p+1-nr
    return dict(n=n,p=p,r=r,conjugate=conj+1,finite_root=root,
                unfiltered_pairs_mod_sign=valid, primitive_pairs_mod_sign=total,
                seed_denominator=p+1, multiplicities=dict(sorted(freq.items())),
                second_numerator=second, unordered_collision_numerator=pairs)


def cubic_at(x):
    return x**3+x*x-2*x-1


def abs_root(a,b):
    a,b=F(a),F(b)
    side=cubic_at(a)>0
    assert side!=(cubic_at(b)>0)
    for _ in range(55):
        c=(a+b)/2
        if (cubic_at(c)>0)==side:
            a=c
        else:
            b=c
    return (a,b) if a>0 else (-b,-a)


def log_bounds(x):
    # Only positive arguments >= 1 enter.
    t=(x-1)/(x+1)
    assert 0<=t<1
    poly=2*sum(t**(2*k+1)/(2*k+1) for k in range(24))
    return poly,poly+2*t**49/(49*(1-t*t))


def invtan(q):
    # Lower partial sum has an even number of alternating terms.
    lo=sum(F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(14))
    return lo, lo+F(1,29*q**29)


def constants():
    x,y,z=(abs_root(*a) for a in [(1,2),(-1,0),(-2,-1)])
    x=(log_bounds(x[0])[0],log_bounds(x[1])[1])
    y=(log_bounds(1/y[1])[0],log_bounds(1/y[0])[1])
    z=(log_bounds(z[0])[0],log_bounds(z[1])[1])
    reg=(y[0]**2-x[1]*z[1],y[1]**2-x[0]*z[0])
    a,b=invtan(5),invtan(239)
    pi=(16*a[0]-4*b[1],16*a[1]-4*b[0])
    n=1800
    zeta=sum(F(1,i**3) for i in range(1,n+1))
    zl,zu=zeta+F(1,2*(n+1)**2),zeta+F(1,2*n*n)
    gr=F(0)
    for n in range(51):
        closed=sum(factorial(2*n)//(factorial(a)*factorial(b)*factorial(n-a-b))**2
                   for a in range(n+1) for b in range(n+1-a))
        gr+=F(closed,4*64**n)
    gu=gr+F(4,7)*F(9,16)**51
    den=10**18
    k=isqrt(7*den*den)
    lo=49*F(k,den)*reg[0]*gr/(3*pi[1]*zu**2)
    hi=49*F(k+1,den)*reg[1]*gu/(3*pi[0]*zl**2)
    def encoded(low,high,scale=10**10):
        return [int(low*scale),-((-high*scale)//1),scale]
    assert F(14099289,10**7)<lo<hi<F(14099290,10**7)
    return dict(interval_format='[floor lower, ceil upper, denominator]', C_star=encoded(lo,hi),
                C_star_over_42_cubed=encoded(lo/42**3,hi/42**3,10**14),
                Green_at_4=encoded(gr,gu,10**12), regulator=encoded(*reg,scale=10**12),
                walk_terms_n='0 through 50', zeta3_summands=1800)


def main():
    rows=[]
    for n,levels in [(43,(0,1,7,16)),(85,(0,1,3)),(129,(0,1,3)),(220,(0,1,3))]:
        for level in levels:
            case=[block(n,j,level) for j in range(3)]
            assert case[0]['multiplicities']==case[1]['multiplicities']==case[2]['multiplicities']
            rows.extend(case)
    extra=next(n for n in range(530,650) if (n**3-n*n-2*n+1)%7==6
               and isprime(n**3-n*n-2*n+1))
    rows.append(block(extra,0,0))
    print(json.dumps(dict(
        parameters='kappa=1/sqrt(42), strict native six-coordinate ball; uniform unfiltered projective seed',
        fixed_product_lock_denominators=[7,364,14,7],
        lock_product=7*364*14*7,constants=constants(),blocks=rows),indent=2))


if __name__=='__main__':
    main()
