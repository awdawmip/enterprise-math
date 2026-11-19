"""Finite rings, square classes and exact weight distributions. Python standard library."""
from collections import Counter
from fractions import Fraction
from functools import cache
from math import comb, gcd, isqrt, prod
import argparse
import json
from pathlib import Path


K = (1, 2, 4, 8, 16)
ROWS = [(k,j,(2*j+1)**2+16*k) for k in K for j in range(k)]
FULL = (1 << len(K))-1


@cache
def factors(n):
    f = []
    d = 2
    while d*d <= n:
        e = 0
        while n % d == 0:
            e += 1
            n //= d
        if e:
            f.append((d,e))
        d += 1
    if n>1:
        f.append((n,1))
    return tuple(f)


def space_closure(gens):
    span = {0}
    for x in gens:
        span |= {v^x for v in span}
    return frozenset(span)


def relation_space():
    primes = sorted({p for _,_,a in ROWS for p,e in factors(a) if e%2})
    pivots, dependencies = {}, []
    for i,(_,_,a) in enumerate(ROWS):
        v = sum(1<<primes.index(p) for p,e in factors(a) if e%2)
        expression = 1<<i
        while v:
            j = v.bit_length()-1
            if j not in pivots:
                pivots[j] = (v,expression)
                break
            w,y = pivots[j]
            v ^= w
            expression ^= y
        if not v:
            dependencies.append(expression)
    assert len(primes)==29 and len(pivots)==27 and len(dependencies)==4
    D = space_closure(dependencies)
    subspaces = {frozenset({0})}
    for x in sorted(D):
        subspaces |= {U | frozenset(y^x for y in U) for U in subspaces}
    assert len(subspaces)==67
    info = []
    for U in subspaces:
        supp = 0
        for w in U:
            supp |= w
        info.append((len(U).bit_length()-1,supp))
    return dependencies,sorted(info)


def pmul(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out


def linpow(c,n):
    return [comb(n,i)*c**(n-i) for i in range(n+1)]


def total_weight_counts(Q,subspaces):
    a = [Q-1,0,1]
    b = [(Q-1)*(Q-2),2*(Q-1),0,Q-1,0,1]
    simple = pmul(pmul(linpow(Q-1,24),a),b)
    dual = [0]*32
    for dim,mask in subspaces:
        s = mask.bit_count()
        poly = pmul(linpow(-1,s),linpow(Q-1,31-s))
        weight = prod(Q-2**i for i in range(dim))
        for i,c in enumerate(poly):
            dual[i] += weight*c
    assert dual == [v*Q**4 for v in simple]
    assert sum(simple)==Q**27 and sum(i*c for i,c in enumerate(simple))==31*Q**26
    var=Fraction(sum(i*i*c for i,c in enumerate(simple)),Q**27)-Fraction(31,Q)**2
    assert var==Fraction(39*(Q-1),Q**2)
    return simple


def get_intersection(Q,requested,subspaces):
    rowmask = sum(1<<i for i,(k,_,_) in enumerate(ROWS) if requested & (1<<K.index(k)))
    n = rowmask.bit_count()
    summation=0
    for dim,support in subspaces:
        if support & ~rowmask:
            continue
        s = support.bit_count()
        summation += prod(Q-2**i for i in range(dim))*(-1)**s*(Q-1)**(n-s)
    return Fraction(summation,Q**n)


def pgf(Q,t):
    x,y,z,v,w = t
    a,b,c = x*v*w,y,w
    coupled = a*b*c+(Q-1)*(a+b+c)+(Q-1)*(Q-2)
    return Fraction((Q-1+z)**4*(Q-1+v)**6*(Q-1+w)**14*(Q-1+y*v)*coupled,Q**27)


def law(Q,subspaces):
    intersections = {}
    for J in range(FULL+1):
        t = [int(not J&(1<<i)) for i in range(5)]
        independent = get_intersection(Q,J,subspaces)
        assert independent==pgf(Q,t)
        intersections[J] = independent
    exact={}
    for I in range(FULL+1):
        density = sum((-1)**((J^I).bit_count())*d for J,d in intersections.items() if J&I==I)
        assert density>=0
        exact[''.join(str(int(bool(I&(1<<i)))) for i in range(5))] = str(density)
    assert sum(Fraction(x) for x in exact.values())==1
    assert Fraction(exact['11111'])==Fraction((Q-1)**26*(Q-2),Q**27)
    return dict(r=Q.bit_length()-1,Q=Q,saturation_profile_by_k_1_2_4_8_16=exact,
                positive_profiles=sum(x!='0' for x in exact.values()),
                total_rows_weight_counts_over_Q_power_27=total_weight_counts(Q,subspaces))


def roots_mod_power(n,p,e):
    v,u = 0,n
    while v<e and u%p==0:
        v += 1
        u //= p
    if v==e:
        return p**(e//2)
    if v%2 or pow(u,(p-1)//2,p)!=1:
        return 0
    return 2*p**(v//2)


def fibers(M,k):
    assert M%2 and M-2*k>=3 and gcd(M,2*k)==1
    return [prod(roots_mod_power((2*j+1)**2+16*k,p,e) for p,e in factors(M)) for j in range(k)]


def direct_fibers(M,k):
    s = M-2*k
    inv_two = pow(2,-1,M)
    ys = [(x*inv_two % M, -x*inv_two % M) for x in range(1,2*k,2)]
    outside = {v for pair in ys for v in pair}
    assert outside==set(range(s//2+1,M-s//2))
    actual = Counter()
    for a in range(1,M):
        if gcd(a,M)==1:
            t = (-s*a-pow(2*a,-1,M)) % M
            if t in outside:
                actual[t] += 1
    assert all(actual[u]==actual[v] for u,v in ys)
    result = [actual[u] for u,_ in ys]
    assert result==fibers(M,k)
    return result


def metrics(M, direct=False):
    out = {}
    for k in K:
        ns = direct_fibers(M,k) if direct else fibers(M,k)
        out[str(k)] = dict(number_of_rows_with_roots=sum(n>0 for n in ns),
                           outside_inputs=2*sum(ns),outside_outputs=2*sum(n>0 for n in ns),
                           row_root_counts_per_output=ns)
    return out


def sqrt_prime(n,p):
    if pow(n,(p-1)//2,p)!=1:
        raise ArithmeticError('expected nonzero square')
    d,e = p-1,0
    while d%2==0:
        d//=2
        e+=1
    z = next(h for h in range(2,p) if pow(h,(p-1)//2,p)==p-1)
    c,r,t = pow(z,d,p),pow(n,(d+1)//2,p),pow(n,d,p)
    while t!=1:
        j=next(j for j in range(1,e) if pow(t,2**j,p)==1)
        b=pow(c,2**(e-j-1),p)
        r,t,c,e = r*b%p,t*b*b%p,b*b%p,j
    return r


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out',type=Path)
    out = parser.parse_args().out
    rel,subs=relation_space()
    profiles = [law(Q,subs) for Q in (2,4,8,16)]
    assert profiles[0]['total_rows_weight_counts_over_Q_power_27'][:3]==[0,2,48]
    direct_cases=0
    for M in range(5,402,2):
        for k in K:
            if M-2*k>=3:
                direct_fibers(M,k)
                direct_cases+=1
    p=1599326581
    assert factors(p)==((p,1),)
    prime=metrics(p)
    assert sum(v['outside_inputs'] for v in prime.values())==4
    s=p-4
    root=sqrt_prime(41,p)
    roots={}
    for y in ((3*pow(2,-1,p))%p,(-3*pow(2,-1,p))%p):
        roots[y]=sorted(((-2*y+d)*pow(4*s,-1,p))%p for d in (root,-root))
        assert all((-s*a-pow(2*a,-1,p))%p==y for a in roots[y])
    small=[(p,metrics(p)) for p in (151,571)]
    M=151*571
    mixed=metrics(M,True)
    assert all(x['outside_outputs']==0 for x in mixed.values())
    ram=[p for p in sorted({p for _,_,v in ROWS for p,_ in factors(v)}) if p>=35]
    bad={q:sum(v['outside_inputs'] for v in metrics(q,True).values()) for q in ram}
    assert min(bad.values())==38
    result=dict(group_order=list(K),row_count=len(ROWS),rank=27,relation_dim=4,
                relation_label_generators=[[(k,j) for i,(k,j,_) in enumerate(ROWS) if m&(1<<i)] for m in rel],
                subspace_count_by_dim=dict(sorted(Counter(d for d,_ in subs).items())),
                joint_laws=profiles,
                direct_ring_checks=dict(odd_moduli_inclusive=[5,401],condition='all k with M-2k >= 3',parameter_pairs=direct_cases),
                minimal_prime_score_example=dict(prime=p,by_k=prime,outside_fibers_k2=roots),
                ramified_primes_ge_35_total_outside_input_counts=bad,
                all_saturation_semiprime=dict(modulus=M,prime_components=small,by_k=mixed),
                nonunit_discriminant_checks=dict(k1_N17_p17_and_p17squared=[direct_fibers(n,1)[0] for n in (17,289)],
                                                k8_j2_N153_at_171_513=[direct_fibers(n,8)[2] for n in (171,513)]))
    dump=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if out:
        out.write_text(dump)
    else:
        print(dump,end='')


if __name__=='__main__':
    main()
