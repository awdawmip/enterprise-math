"""Finite group checks and exact finite-field reductions for the marked P11 point."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import isqrt, prod
import json

A = 233**2
B = 119**2
H = (194089, 69872040)
CUTOFF = 1000000


def primes(bound):
    sieve = bytearray(b'\x01') * (bound + 1)
    sieve[:2] = bytes(2)
    for p in range(2, isqrt(bound) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((bound-p*p)//p + 1)
    return [p for p in range(2, bound+1) if sieve[p]]


def sign(n, p):
    a = pow(n % p, (p-1)//2, p)
    return -1 if a == p-1 else a


def local(q):
    size = q*(q-1)**2*(q+1)
    good = q*size - q**3 + q + 1
    return Fraction(good,q*size), Fraction(1,good)


def check_affine(q):
    size = good = signed = 0
    for a,b,c,d in product(range(q), repeat=4):
        det = (a*d-b*c) % q
        if not det:
            continue
        cols = ((1-a,-c), (-b,1-d))
        image = {((x*cols[0][0]+y*cols[1][0])%q,(x*cols[0][1]+y*cols[1][1])%q)
                 for x,y in product(range(q),repeat=2)}
        for t in product(range(q), repeat=2):
            size += 1
            ok = len(image)==q*q or (len(image)==q and t not in image)
            if ok:
                good += 1
                signed += sign(det,q)
    s,c = local(q)
    assert Fraction(good,size)==s and Fraction(signed,good)==c
    return dict(total=size,passed=good,signed_passed=signed)


def check_two():
    # Full 16 sign patterns; row (a,b) of (Frob-1)/2 in the T0,TP basis.
    data = [0]*4
    for a,b,u,v in product(range(2), repeat=4):
        if (a or b) and v:
            aa = (-1)**(a+b)
            bb = (-1)**v
            data = [x+y for x,y in zip(data,(1,aa,bb,aa*bb))]
    assert data == [6,-2,-6,2]
    return data


def group_law(s,t,p):
    if s is None: return t
    if t is None: return s
    x,y=s; z,w=t
    if x==z:
        if (y+w)%p==0: return None
        slope=(3*x*x-2*(A+B)*x+A*B)*pow(2*y,-1,p)%p
    else:
        slope=(w-y)*pow(z-x,-1,p)%p
    xx=(slope*slope+A+B-x-z)%p
    return xx,(slope*(x-xx)-y)%p


def times(k,s,p):
    result=None
    while k:
        if k&1: result=group_law(result,s,p)
        s=group_law(s,s,p)
        k//=2
    return result


def check_curve(ps, limit):
    counts=Counter()
    samples=[]
    for p in ps:
        if p>limit: break
        if (2*A*B*(A-B))%p==0: continue
        squares=bytearray(p)
        for y in range(p): squares[y*y%p]+=1
        order=1+sum(squares[x*(x-A)*(x-B)%p] for x in range(p))
        point=H[0]%p,H[1]%p
        assert (point[1]**2-point[0]*(point[0]-A)*(point[0]-B))%p==0
        factors=[]; n=order
        for q in ps:
            if q*q>n: break
            if n%q==0:
                factors.append(q)
                while n%q==0: n//=q
        if n>1: factors.append(n)
        h=order
        for q in factors:
            while h%q==0 and times(h//q,point,p) is None: h//=q
        index=order//h
        two_good=(sign(-1,p)==-1 or sign(627,p)==-1) and sign(3961,p)==-1
        assert times(h,point,p) is None and index%2==0 and (index%4==2)==two_good
        counts['good_reductions']+=1
        counts['v2_index_one']+=int(two_good)
        counts['index_two']+=int(index==2)
        if p not in (3,11,19):
            assert sign(-627,p)==prod(sign(p,q) for q in (3,11,19))
        if p not in (17,233):
            assert sign(3961,p)==sign(p,17)*sign(p,233)
        if len(samples)<12 or p in (4001,4441):
            samples.append([p,order,h,index])
    return dict(bound=limit,counts=dict(counts),examples_p_group_point_index=samples)


def euler_bracket(ps):
    # Directed integer rounding at every multiplication. The final tail is analytic.
    scale=10**32
    lower=upper=scale
    for q in ps:
        if q==2: continue
        s,_=local(q)
        n,d=s.numerator,s.denominator
        lower=lower*n//d
        upper=(upper*n+d-1)//d
    c1=prod(local(q)[1] for q in (3,11,19))
    c2=prod(local(q)[1] for q in (17,233))
    factor=Fraction(3,8)*(1-c1/3)*(1-c2)
    lo=Fraction(lower,scale)*factor*(1-Fraction(1,CUTOFF-1))
    hi=Fraction(upper,scale)*factor
    decimals=10**12
    return dict(prime_cutoff=CUTOFF,odd_primes=len(ps)-1,
                odd_character_products=[str(c1),str(c2)],correction=str(factor/Fraction(3,8)),
                outward_decimal_numerators=[lo.numerator*decimals//lo.denominator,
                    -(-hi.numerator*decimals//hi.denominator)],decimal_denominator=decimals)


if __name__ == '__main__':
    ps=primes(CUTOFF)
    result=dict(odd_affine={q:check_affine(q) for q in (3,5,7)},two_signed_sums=check_two(),
                finite_field=check_curve(ps,5000),haar_bracket=euler_bracket(ps))
    print(json.dumps(result,sort_keys=True,indent=2))
