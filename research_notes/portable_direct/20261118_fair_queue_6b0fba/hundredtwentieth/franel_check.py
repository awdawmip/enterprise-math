"""Simultaneous mod-p-squared Franel queries at the native two indices."""
import argparse
from hashlib import sha256
from math import comb, isqrt
from fractions import Fraction
from functools import lru_cache
import json
try:
    from flint import fmpz as Integer
except ImportError:
    Integer = int


def primes(limit):
    table=bytearray(b'\x01')*(limit+1)
    table[:2]=b'\x00\x00'
    for k in range(2,isqrt(limit)+1):
        if table[k]:
            table[k*k::k]=b'\x00'*((limit-k*k)//k+1)
    return [p for p in range(5,limit+1) if table[p] and p%24 in (5,23)]


def compose(b,a):
    e,f,g,h,s=b
    x,y,z,w,t=a
    return (e*x+f*z,e*y+f*w,g*x+h*z,g*y+h*w,s*t)


def block_product(start,stop):
    a,b,c,d,t=map(Integer,(1,0,0,1,1))
    for i in range(start,stop):
        h=(i+1)**2
        f=7*i*i+7*i+2
        g=8*i*i
        a,b,c,d,t=f*a+g*c,f*b+g*d,h*a,h*b,h*t
    return a,b,c,d,t


def native_answers(limit,block):
    ps=primes(limit)
    queries={}
    for p in ps:
        for slot,i in enumerate(((p-2)//3,(p-1)//2)):
            queries.setdefault(i,[]).append((p,slot))
    stop=max(queries)+1
    ids=range(0,stop,block)
    moduli=[Integer(1) for _ in ids]
    for i,qs in queries.items():
        for p,slot in qs:
            moduli[i//block]*=p*p
    mats=[block_product(x,min(x+block,stop)) for x in ids]
    tree=[(moduli,mats)]
    while len(moduli)>1:
        nm=[]; nt=[]
        for j in range(0,len(moduli),2):
            if j+1==len(moduli):
                nm.append(moduli[j]);nt.append(mats[j])
            else:
                nm.append(moduli[j]*moduli[j+1]);nt.append(compose(mats[j+1],mats[j]))
        tree.append((nm,nt))
        moduli,mats=nm,nt
    answers={p:[None,None] for p in ps}
    def descend(level,j,state):
        m=tree[level][0][j]
        if m==1:return
        x,y,u=(a%m for a in state)
        if level:
            descend(level-1,2*j,(x,y,u))
            if 2*j+1<len(tree[level-1][0]):
                q=tree[level-1][0][2*j+1]
                if q>1:
                    a,b,c,d,t=tree[level-1][1][2*j]
                    x,y,u=x%q,y%q,u%q
                    descend(level-1,2*j+1,((a%q*x+b%q*y)%q,(c%q*x+d%q*y)%q,(t%q*u)%q))
            return
        for i in range(j*block,min((j+1)*block,stop)):
            for p,slot in queries.get(i,()):
                q=p*p
                answers[p][slot]=int(x%q)*pow(int(u%q),-1,q)%q
            h=(i+1)**2
            x,y,u=((7*i*i+7*i+2)*x+8*i*i*y)%m,h*x%m,h*u%m
    descend(len(tree)-1,0,(Integer(1),Integer(0),Integer(1)))
    return answers


def binomial_certificate(p):
    assert all(p%i for i in range(2,isqrt(p)+1))
    m=(p-1)//2
    n=(p-2)//3
    mod=p*p
    fac=[1]
    for j in range(1,m+1): fac.append(fac[-1]*j%mod)
    inv=[0]*(m+1)
    back=pow(fac[-1],-1,mod)
    for j in range(m,0,-1):
        inv[j]=fac[j-1]*back%mod
        back=back*j%mod
    rows=[]
    for a in (n,n+1,m):
        val=s=1
        for j in range(1,a+1):
            val=val*(a+1-j)*inv[j]%mod
            s=(s+pow(val,3,mod))%mod
        assert val==1
        rows.append({"index":a,"F_mod_p_square":s,"F_mod_p":s%p,"first_quotient_if_zero":None if s%p else s//p,"whipple_quotient_if_zero":None if s%p else pow(2,-a,p)*(s//p)%p})
    return {"p":p,"rows":rows}

def factors(n):
    divisors = []
    trial = 2
    while trial * trial <= n:
        if n % trial == 0:
            exp = 0
            while n % trial == 0:
                n //= trial
                exp += 1
            divisors.append((trial, exp))
        trial = 3 if trial == 2 else trial + 2
    if n > 1:
        divisors.append((n, 1))
    return divisors


def valuation_profile(p):
    n, m = (p - 2) // 3, (p - 1) // 2
    modulus = p * p
    x, y, denominator = 1, 0, 1
    roots = {}
    for i in range(m + 2):
        if x % p == 0:
            value = x * pow(denominator, -1, modulus) % modulus
            assert value != 0, "The fixture contains a higher zero"
            roots[i] = value // p
        h = (i + 1) ** 2
        x, y = ((7*i*i + 7*i + 2)*x + 8*i*i*y) % modulus, h*x % modulus
        denominator = denominator * h % modulus

    @lru_cache(None)
    def shadow(v):
        if v <= 2:
            return 0
        divs = factors(v)
        if divs == [(v, 1)]:
            j = (v + 1) // 2
            return shadow(j) + int(j in roots) - int(j - 1 in roots)
        return sum(exp * shadow(q) for q, exp in divs)

    k = (p + 1) // 6
    r = min(roots)
    max_prime = max(t for v in (k, 4*k-1) for t,_ in factors(v))
    bound = (max_prime + 1) // 2
    defects = []
    for i in (n, n+1, m):
        numerator, divisor = shadow(i), shadow(2*i-1)
        degree = int(i in roots) - int(i-1 in roots) + numerator - divisor
        defects.append(dict(index=i, boundary_factors=factors(2*i-1),
                            shadow_of_index=numerator, shadow_of_boundary=divisor,
                            valuation=degree))
    from_scale = defects[1]['valuation'] + int(n in roots) - int(n+1 in roots) - int(m in roots)
    from_shadow = shadow(k) - shadow(4*k-1) - int(m in roots)
    assert from_scale == from_shadow
    if r > bound:
        assert from_shadow == -1
    return dict(roots_and_quotients=sorted(roots.items()), rank=r,
                rank_boundaries=[factors(2*r-1),factors(2*r+1)],
                k_factors=factors(k), four_k_minus_one_factors=factors(4*k-1),
                largest_possible_shadow_index=bound, defects=defects, terminal_valuation=from_scale)


def quartic_jet(p):
    m = (p - 1) // 2
    degree = (p - 1) // 4
    k = (degree - 1) // 2
    assert degree == 2*k + 1
    # Homogenize the quartic sum with D_i = (2^i i!)^4.
    partial, top, den, central_num, central_den = 1, 1, 1, 1, 1
    for i in range(1, k + 1):
        odd, even = 2*i-1, 2*i
        central_num = central_num * odd % p
        central_den = central_den * even % p
        c = pow(even, 4, p)
        top = top * pow(odd, 4, p) % p
        partial = (partial*c + (4*i+1)*top) % p
        den = den*c % p
    a = central_num * pow(central_den, -1, p) % p
    s = partial * pow(den, -1, p) % p
    integral = s * pow(2*degree**2*a*a, -1, p) % p
    quotient = -3*pow(2, m-1, p)*integral % p
    return dict(legendre_degree=degree, terms=k+1,
                quartic_sum=s, midpoint_quotient=quotient)


def integral_checks():
    result = []
    prev, curr = [Fraction(1)], [Fraction(0), Fraction(1)]
    for d in range(1, 26):
        if d % 2:
            val = sum(a*b/(i+j) for i,a in enumerate(curr) for j,b in enumerate(curr)
                      if i+j and a and b)
            k = (d-1)//2
            term = lambda j: Fraction(comb(2*j,j), 4**j)
            quartic = sum((4*j+1)*term(j)**4 for j in range(k+1))
            assert val == quartic / (2*d*d*term(k)**2)
            result.append(str(val))
        shifted = [Fraction(0)] + [Fraction((2*d+1)*a, d+1) for a in curr]
        for i,a in enumerate(prev):
            shifted[i] -= Fraction(d*a, d+1)
        prev, curr = curr, shifted
    return result

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--limit',type=int,default=1200000)
    parser.add_argument('--block',type=int,default=128)
    args=parser.parse_args()
    if args.limit < 5 or args.block < 1:
        parser.error("limit must be at least 5 and block must be positive")
    a=native_answers(args.limit,args.block)
    digest=sha256()
    hits=[]; mid=[]; small=[]
    for p,(x,y) in a.items():
        assert y%p==0
        digest.update(f'{p} {x} {y}\n'.encode())
        if x%p==0: hits.append([p,x//p,y//p])
        if y==0: mid.append([p,x])
        if p<251:
            fn=lambda n:sum(comb(n,k)**3 for k in range(n+1))
            assert x==fn((p-2)//3)%(p*p) and y==fn((p-1)//2)%(p*p)
            assert quartic_jet(p)['midpoint_quotient'] == y//p
            small.append([p,x,y])
    witnesses = []
    for p, first, midpoint in hits:
        case = binomial_certificate(p)
        assert case['rows'][0]['first_quotient_if_zero'] == first
        assert case['rows'][2]['first_quotient_if_zero'] == midpoint
        case['quartic'] = quartic_jet(p)
        assert case['quartic']['midpoint_quotient'] == midpoint
        if p in (536111, 663983):
            case['row_visibility'] = valuation_profile(p)
            assert case['row_visibility']['rank'] == (p-2)//3
        witnesses.append(case)
    high_range = {}
    for p in (4349, 19157):
        if p > args.limit:
            continue
        example = valuation_profile(p)
        r = example['rank']
        assert example['largest_possible_shadow_index'] < r < (p+1)//6
        assert example['rank_boundaries'] == [[(2*r-1,1)],[(2*r+1,1)]]
        high_range[p] = example
    print(json.dumps(dict(high_range=high_range, witnesses=witnesses, rational_integrals=integral_checks(), limit=args.limit,sector=[5,23],prime_count=len(a),diagonal_hits=hits,midpoint_zeros=mid,sha256_serialized_triples=digest.hexdigest(),direct_binomial=small),sort_keys=True,indent=2))

if __name__=='__main__':main()
