"""Check the Gaussian trace order in the full, unweighted integral Veronese lattice."""
from math import fsum, isqrt, lgamma, log, prod
import json


def primes(n):
    return [p for p in range(2,n+1) if all(p%i for i in range(2,isqrt(p)+1))]


def valuation(a,p):
    assert a
    v=0
    while a%p==0:
        a//=p
        v+=1
    return v


def vp_factorial(k,p):
    total=0
    while k:
        k//=p
        total+=k
    return total


def predicted(d,p):
    k,r=divmod(d,p+1)
    if p==2:
        return (k+1)//2 + vp_factorial(k,2)
    if p%4==1:
        return 0
    if r==0 and k%2:
        k-=1
    return k+vp_factorial(k,p)


def mixed_differences(d):
    # Row Δ_x^a Δ_y^b v_d(0,0), obtained directly from finite differences.
    # Index a+b=d gives (d-j)! j! times the j-th coordinate unit.
    diff=[]
    for e in range(d+1):
        samples=[x**e for x in range(d+1)]
        coeff=[]
        while samples:
            coeff.append(samples[0])
            samples=[b-a for a,b in zip(samples,samples[1:])]
        diff.append(coeff)
    return [[diff[d-j][a]*diff[j][b] for j in range(d+1)]
            for a in range(d+1) for b in range(d-a+1) if a+b or d==0]


def pivot(rows,p):
    # A nonzero entry with least p-adic valuation. Look for a unit first.
    found=None
    for i,row in enumerate(rows):
        for j,x in enumerate(row):
            if x%p:
                return i,j,0
            if x:
                v=valuation(x,p)
                if found is None or v<found[2]:
                    found=i,j,v
    return found


def local_order(matrix,w,p,precision):
    # Smith elimination in Z/p^precision. Column operations act on w too.
    modulus=p**precision
    rows=[[x%modulus for x in row] for row in matrix]
    target=[x%modulus for x in w]
    exponent=0
    while target:
        location=pivot(rows,p)
        if location is None:
            for x in target:
                if x:exponent=max(exponent,precision-valuation(x,p))
            return exponent
        i,j,v=location
        pivot_row=rows.pop(i)
        pivot_row[0],pivot_row[j]=pivot_row[j],pivot_row[0]
        target[0],target[j]=target[j],target[0]
        ideal=p**v
        inv=pow(pivot_row[0]//ideal,-1,modulus)
        row=[(x*inv)%modulus for x in pivot_row]
        assert row[0]==ideal
        if target[0]:
            exponent=max(exponent,v-valuation(target[0],p))
        coefficients=[x//ideal for x in row[1:]]
        target=[(x-target[0]*c)%modulus for x,c in zip(target[1:],coefficients)]
        current=[]
        for other in rows:
            other[0],other[j]=other[j],other[0]
            first=other[0]
            reduced=[(x-first*c)%modulus for x,c in zip(other[1:],coefficients)]
            if any(reduced):
                current.append(reduced)
        rows=current
    return exponent


def gaussian_mul(u,v):
    return u[0]*v[0]-u[1]*v[1], u[0]*v[1]+u[1]*v[0]


def kernel_at_i(p,k):
    value=(1,0)
    for t in range(k*p):
        value=gaussian_mul(value,(-t,1))
    for t in range(k):
        value=gaussian_mul(value,(1,-p*t))
    return value


def growth_samples():
    limit=1_000_000
    sieve=bytearray([1])*(limit+1)
    sieve[:2]=bytes(2)
    for p in range(2,isqrt(limit)+1):
        if sieve[p]:
            sieve[p*p::p]=bytes((limit-p*p)//p+1)
    ps=[p for p in range(2,limit+1) if sieve[p]]
    out=[]
    for d in (1_000,10_000,100_000,1_000_000):
        log_order=fsum(predicted(d,p)*log(p) for p in ps if p<=d)
        out.append(dict(d=d,twice_log_order_minus_log_factorial_over_d=(2*log_order-lgamma(d+1))/d))
    return out


def main():
    scans=[]
    for d in [*range(0,29),30,32,36,40,48,56]:
        w=[[1,0,-1,0][j%4] for j in range(d+1)]
        matrix=mixed_differences(d)
        actual={}
        for p in primes(d):
            h=local_order(matrix,w,p,vp_factorial(d,p))
            assert h==predicted(d,p),(d,p,h,predicted(d,p))
            if h:actual[p]=h
        scans.append(dict(d=d,full_grid_order=prod(p**v for p,v in actual.items()),exponents=actual))
    ramified=[]
    for k in range(33):
        a,b=kernel_at_i(2,k)
        assert a and valuation(a,2)==k//2
        ramified.append(k//2)
    inert=[]
    for p in [3,7,11,19]:
        for k in [1,3,5,7,p,p*p]:
            a,b=kernel_at_i(p,k)
            assert b%p and a%(p**(1+valuation(k,p)))==0
            inert.append([p,k,1+valuation(k,p)])
    print(json.dumps(dict(exact_full_lattice=scans,formula_growth_samples=growth_samples(),ramified_real_valuations_k0_to32=ramified,
                          inert_exception_checks=inert),sort_keys=True,indent=2))
if __name__=="__main__":
    main()
