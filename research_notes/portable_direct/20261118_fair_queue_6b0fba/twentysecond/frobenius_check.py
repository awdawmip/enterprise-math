"""Finite cyclic carrier audit and exact ramified cyclotomic fibres; Python standard library."""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product
from math import comb, gcd, isqrt, prod
from random import Random
import json


def divisors(n):
    return [j for j in range(1,n+1) if n%j==0]


def valuation(n,p):
    v=0
    while n%p==0:
        n//=p
        v+=1
    return v


def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))


def quotient(f,g):
    f=list(f)
    q=[0]*(len(f)-len(g)+1)
    for j in reversed(range(len(q))):
        q[j]=f[j+len(g)-1]
        for i,c in enumerate(g):
            f[j+i]-=q[j]*c
    assert not any(f)
    return q


@lru_cache(None)
def phi_poly(n):
    f=[-1]+[0]*(n-1)+[1]
    for d in divisors(n)[:-1]:
        f=quotient(f,phi_poly(d))
    return tuple(f)


@lru_cache(None)
def nonzero_phi(n):
    return [(j,c) for j,c in enumerate(phi_poly(n)[:-1]) if c]


def residue(f,d,m):
    g=phi_poly(d)
    deg=len(g)-1
    f=list(f)
    for i in reversed(range(deg,len(f))):
        c=f[i]
        if c:
            for j,b in nonzero_phi(d):
                q=i-deg+j
                f[q]=(f[q]-c*b)%m
    return tuple(f[:deg])


def fold(f,r,m):
    return tuple(sum(f[j::r])%m for j in range(r))


def mul(a,b,m):
    """Carry-free integer encoding of an ordinary coefficient convolution."""
    r=len(a)
    stride=max(1,((r*(m-1)**2).bit_length()+7)//8)
    def pack(v):
        return int.from_bytes(b''.join(c.to_bytes(stride,'little') for c in v),'little')
    u=pack(a); v=u if a is b else pack(b)
    s=(u*v).to_bytes(2*r*stride,'little')
    def coeff(j):
        return int.from_bytes(s[stride*j:stride*(j+1)],'little')
    return tuple((coeff(i)+coeff(i+r))%m for i in range(r))


def naive(a,b,m):
    r=len(a)
    out=[0]*r
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[(i+j)%r]+=x*y
    return tuple(c%m for c in out)


def power(f,e,m,op=mul):
    f=tuple(f)
    a=(1,)+(0,)*(len(f)-1)
    while e:
        if e&1:
            a=op(a,f,m)
        e//=2
        if e:
            f=op(f,f,m)
    return a


def seed(r,t):
    if r==1:
        return (t+1,)
    return (t,1)+(0,)*(r-2)


def observed(f,m):
    return tuple(x for d in divisors(len(f)) for x in residue(f,d,m))


def order(p,n):
    if n==1:
        return 1
    k,v=1,p%n
    while v!=1:
        k+=1
        v=v*p%n
    return k


def fiber_histogram(p,r,exp):
    """Product of local fiber-size histograms, counting observation values."""
    a=valuation(r,p)
    n=r//p**a; v=valuation(exp,p); c=exp//p**v
    h=p**max(0,a-v)
    s=(1 if a==0 else (p-1)*p**(a-1))
    t=(s+p**min(a,v)-1)//p**min(a,v)
    hist=Counter({1:1})
    for d in divisors(n):
        e=order(p,d); q=p**e
        roots=(q-1)//gcd(c,q-1)
        zero_fiber=1+roots*sum(q**(h-j*c-1) for j in range((t+c-1)//c,(h-1)//c+1))
        nz_obs=roots*sum(q**(t-j*c-1) for j in range((t-1)//c+1))
        local=Counter({zero_fiber:1})
        local[q**(h-t)]+=nz_obs
        for _ in range((len(phi_poly(d))-1)//e):
            new=Counter()
            for size,nobs in hist.items():
                for b,count in local.items():
                    new[size*b]+=nobs*count
            hist=new
    return dict(sorted(hist.items()))


def small_checks():
    cases=[]
    for p,r,exponents in [(2,4,[2,6]),(2,8,[2,4,6]),(2,12,[6,10]),
                          (3,3,[3,6]),(3,6,[3,15]),(3,9,[3,6,15]),
                          (5,5,[5,15])]:
        for n in exponents:
            positions=defaultdict(set)
            for f in product(range(p),repeat=r):
                state=power(f,n,p,op=naive)
                positions[observed(state,p)].add(state)
            actual=Counter(map(len,positions.values()))
            assert actual==fiber_histogram(p,r,n)
            cases.append({"p":p,"width":r,"exponent":n,"input_seeds":p**r,
                          "observation_values_by_fiber_size":dict(sorted(actual.items()))})
    for p in [2,3,5,7,11]:
        for n in [p,2*p,p*p,3*p*p]:
            for r in [2,3,4,5,6,8,9,10,12,16,18,25,27,36,49]:
                found={}
                for t in range(p):
                    state=power(seed(r,t),n,p)
                    obs=observed(state,p)
                    assert obs not in found or found[obs]==state
                    found[obs]=state
    return cases


def proper_hit(vals,n):
    return any(1<gcd(a,n)<n for a in vals)


def classify(n,r):
    f=power(seed(r,1),n,n)
    assert all(f[j]==f[(n-j)%r] for j in range(r))
    fine=proper_hit(f,n)
    div=any(proper_hit(fold(f,d,n),n) for d in divisors(r)[:-1])
    cyc=proper_hit(observed(f,n),n)
    return fine,fine or div,fine or div or cyc


def rho_counts(n,cap):
    # Same deterministic finite Floyd control for every N.
    x=y=2
    for i in range(1,cap//3+1):
        x=(x*x+1)%n
        y=(y*y+1)%n
        y=(y*y+1)%n
        d=gcd(abs(x-y),n)
        if d>1:
            return int(d<n),3*i,i
    return 0,3*(cap//3),cap//3


def fermat_counts(n):
    x=isqrt(n)
    x+=int(x*x<n)
    count=0
    while True:
        gap=x*x-n; y=isqrt(gap); count+=1
        if y*y==gap:
            return count
        x+=1


def hypergeom(M,n,x):
    """Inclusive exact equal-tail 95% confidence set for the population count."""
    if M==n: return [x,x]
    den=comb(M,n)
    def prob(k,left):
        lo=max(0,n-(M-k))
        hi=min(k,n)
        lo,hi=(lo,min(hi,x)) if left else (max(lo,x),hi)
        return 40*sum(comb(k,j)*comb(M-k,n-j) for j in range(lo,hi+1))>=den
    def first(test):
        a,b=0,M+1
        while a<b:
            k=(a+b)//2
            if test(k): b=k
            else: a=k+1
        return a
    return [first(lambda k:prob(k,False)),first(lambda k:not prob(k,True))-1]


def benchmark():
    widths=[12,24,48,96,120,192,240]
    rng=Random(20260909)
    bands=[]
    for B in [32,64,128,256,512,1024]:
        ps=[p for p in range(B,2*B) if prime(p)]
        pair_by_n={p*q:(p,q) for p,q in combinations(ps,2)}
        population=sorted(pair_by_n)
        inputs=sorted(rng.sample(population,min(48,len(population))))
        cols=[]
        for r in widths:
            counts=[0]*3
            for n in inputs:
                hits=classify(n,r)
                counts=[a+b for a,b in zip(counts,hits)]
            slots=r+sum(divisors(r))
            fixed=10**8
            null_floor=0
            for n in inputs:
                p,q=pair_by_n[n]  # Used only for the separate theoretical control.
                denominator=n**slots
                null_floor+=fixed*(denominator-(n-p-q+2)**slots)//denominator
            cols.append({"matched_slot_null_expected_hits_scaled_1e8_lower":null_floor,
                         "matched_slot_null_expected_hits_scaled_1e8_upper":null_floor+len(inputs),
                         "width":r,"fine_divisor_combined":counts,
                         "combined_population_95_counts":hypergeom(len(population),len(inputs),counts[2]),
                         "dense_schoolbook_modmul":sum(r*r*(n.bit_length()-1+n.bit_count()) for n in inputs),
                         "physically_packed_integer_products":sum(n.bit_length()-1+n.bit_count() for n in inputs),
                         "all_coordinate_gcd_slots_per_input":r+sum(divisors(r))})
        cap=12**2  # conservative, smaller than a single width-12 fine power
        rho=[rho_counts(n,cap) for n in inputs]
        bands.append({"prime_interval":[B,2*B],"population_pairs":len(population),"sampled_pairs":len(inputs),
                      "inputs":inputs,"by_width":cols,"rho_cap_modmul":cap,
                      "rho_hit_modmul_gcd_totals":[sum(c[k] for c in rho) for k in range(3)],
                      "fermat_integer_square_tests":sum(fermat_counts(n) for n in inputs)})
    return bands


def full_carrier_kernel():
    cases=[]
    for p,e,r in [(2,1,4),(2,2,4),(2,3,4),(3,2,3),(2,2,6),(3,1,6),(5,2,2)]:
        a=valuation(r,p)
        expected=p**(r//p**a*sum(p**(a-k) for k in range(1,min(e,a)+1)))
        m=p**e
        actual=sum(not any(observed(f,m)) for f in product(range(m),repeat=r))
        assert expected==actual
        cases.append({"coefficient_modulus":m,"width":r,"whole_carrier_kernel":actual})
    return cases


def mixed_characteristic_binomials():
    for e in range(2,13):
        n=2*3**e
        x=power(seed(9,0),n,n,op=naive)
        y=power(seed(9,4),n,n,op=naive)
        gap=tuple((b-a)%n for a,b in zip(x,y))
        assert gap==tuple(4*3**(e-1) if j%3==0 else 0 for j in range(9))
        assert x!=y and observed(x,n)==observed(y,n)
    return {"N":"2*3^e","width":9,"checked_exponents":list(range(2,13)),
            "translations":[0,4],"different_indices":[0,3,6],"difference":"4*3^(e-1)"}


def original_96():
    # Frozen summary, 2026-11-17, SHA-256 585fc2f2...81185070.
    expected={(12,2):(10,12,14),(12,3):(12,15,15),
              (18,2):(16,16,16),(18,3):(12,15,15),
              (24,2):(16,16,16),(24,3):(12,15,15)}
    tally=defaultdict(lambda:[0,0,0])
    for p,g in product([11,13,17,19],[6,12,18,24]):
        q=next(i for i in range(p+g,p+g+100) if prime(i))
        n=p*q
        for r,arity in product([12,18,24],[2,3]):
            f=power((1,)*arity+(0,)*(r-arity),n,n)
            f_ok=proper_hit(f,n)
            d_ok=f_ok or any(proper_hit(fold(f,d,n),n) for d in divisors(r)[:-1])
            c_ok=d_ok or proper_hit(observed(f,n),n)
            tally[r,arity]=[a+b for a,b in zip(tally[r,arity],(f_ok,d_ok,c_ok))]
    assert all(tuple(counts)==expected[k] for k,counts in tally.items())
    return [{"R":r,"terms":a,"fine_divisor_union":v} for (r,a),v in sorted(tally.items())]


def historical_and_examples():
    checks=0
    for p,q in [(23,31),(37,43),(101,127)]:
        n=p*q
        for r in [6,8,12,15,24]:
            for t in [1,3,7]:
                f=power(seed(r,t),n,n)
                assert f==power(seed(r,t),n,n,op=naive)
                for d in divisors(r):
                    # The two methods start with independently projected seeds.
                    assert fold(f,d,n)==power(tuple(u%n for u in seed(d,t)),n,n,op=naive)
                    assert residue(f,d,n)==residue(fold(f,d,n),d,n)
                    checks+=1
    p,q,r,t=23,31,8,3
    f=power(seed(r,t),p*q,p*q)
    assert f==(704,148,251,4,145,287,393,519)
    assert not proper_hit(f,p*q) and gcd(fold(f,4,p*q)[2],p*q)==23
    first=power((1,0,0,0),6,6)
    # Construct the mixed-CRT witness directly as 1+3(X-1)=4+3X.
    mixed=power((4,3,0,0),6,6)
    assert first!=mixed and observed(first,6)==observed(mixed,6)
    tri=[power(tuple(int(i in support) for i in range(8)),6,6)
         for support in [(0,1,2),(0,3,6)]]
    assert tri[0]!=tri[1] and observed(tri[0],6)==observed(tri[1],6)
    return {"N6_R8_three_named_steps":{"exponent_sets":[[0,1,2],[0,3,6]],
                "different_fine":tri,"common_cyclotomic":observed(tri[0],6)},
            "divisor_identities_and_cyclotomic_commuting_squares":checks,
            "independent_fine_powers":45,"width8_known_fine":f,"hit":23,
            "N6_R4": {"seeds":[[1,0,0,0],[4,3,0,0]],"outputs":[first,mixed],
                      "common_cyclotomic":observed(first,6)}}


if __name__=="__main__":
    print(json.dumps({"mixed_characteristic_binomials":mixed_characteristic_binomials(),
                      "original_96":original_96(),"whole_carrier_kernels":full_carrier_kernel(),
                      "exact_carriers":historical_and_examples(),"local_exhaustions":small_checks(),
                      "translated_binomial_checks":5*4*15,"public_benchmark":benchmark()},indent=2))
