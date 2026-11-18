"""Exact finite diagnostics for translated power observations."""
import argparse
from collections import Counter
from itertools import combinations
from hashlib import sha1,sha256
import json
from math import ceil, gcd, prod
from pathlib import Path
import sys
import zipfile


def factors(n):
    ds = []
    p = 2
    while p*p <= n:
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        if k:
            ds.append((p,k))
        p += 1
    if n > 1:
        ds.append((n,1))
    return ds


def prime_period(p,k,r):
    if p != 2:
        return p**k
    if k <= min(2**r,r+2):
        return 2
    return 2**max(2,k-r)


def power_fibers(p,k,r):
    q = p**k
    e = 2**r
    h = (k+e-1)//e
    hist = Counter({p**(k-h): 1})
    for j in range(h):
        b = k-e*j
        phi = (p-1)*p**(b-1)
        if p != 2:
            torsion = gcd(e,phi)
        elif b == 1:
            torsion = 1
        else:
            torsion = 2*gcd(e, 2**(b-2))
        hist[p**((e-1)*j)*torsion] += phi//torsion
    actual = Counter(Counter(pow(x,e,q) for x in range(q)).values())
    assert hist == actual
    return len(actual),sum(hist.values())


def signatures(table,shifts):
    n=len(table)
    return [tuple(table[(x+h)%n] for h in shifts) for x in range(n)]


def equivalent(partition,predicted):
    return len(set(zip(partition,predicted))) == len(set(partition)) == len(set(predicted))


def two_adic(q,k,r):
    e = 2**r
    table = [pow(x,e,q) for x in range(q)]
    period = prime_period(2,k,r)
    cases = 1 if period == 2 else (4 if k <= e and k > r+2 else 2)
    keys = [x%period for x in range(q)]
    assert equivalent(signatures(table, range(cases)),keys)
    if cases == 4:
        adaptive = [(table[x],table[(x+2)%q]) if x%2 else
                    (table[x],table[(x+1)%q],table[(x+3)%q]) for x in range(q)]
        assert equivalent(adaptive, keys)
        # Exact optimum: parity of first output is known, all even inputs give zero.
        for h in range(q):
            assert not equivalent([table[(x+h)%q] for x in range(0,q,2)],keys[::2])
    return cases


def field_probes(p,r):
    e = 2**r
    roots = [a for a in range(1,p) if pow(a,e,p)==1]
    dset = {pow(a-1,-1,p) for a in roots if a!=1}
    table = [pow(x,e,p) for x in range(p)]
    masks = set()
    for x,y in combinations(range(p),2):
        actual = {h for h in range(p) if table[(x+h)%p] == table[(y+h)%p]}
        assert actual == {(-x+(y-x)*d)%p for d in dset}
        masks.add(sum(1 << h for h in actual))
    if len(roots)==p-1:
        ans=tuple(range(p-1))
        assert len(masks)==p*(p-1)//2
    else:
        # Any two distinct probes normalize affinely to 0,1.
        covered=[m for m in masks if m&3==3]
        for size in range(2,len(roots)+1):
            ans=None
            for extra in combinations(range(2,p),size-2):
                w=3+sum(1<<h for h in extra)
                if all(w&m!=w for m in covered):
                    ans=(0,1,*extra)
                    break
            if ans is not None:
                break
    assert len(set(signatures(table,ans))) == p
    good_second = [h for h in range(p) if len({table[(x+h)%p] for x in roots})==len(roots)]
    # All nonzero first-output fibers are dilations of the roots of unity.
    assert bool(good_second) or p <= 1+len(roots)*(len(roots)-1)*(len(roots)-2)//2
    if len(roots)==4:
        assert bool(good_second)==(p>13)
    return {'p':p,'r':r,'roots':len(roots),'least_fixed_probes':len(ans),'example':ans,
            'second_shift_separates_first_unit_fiber':good_second[:1]}


def odd_lifts(p,k,r):
    q,e=p**k,2**r
    table=[pow(x,e,q) for x in range(q)]
    g=gcd(e,p-1)
    two=Counter(signatures(table,[0,1]))
    ordered=sum(c*(c-1) for c in two.values())
    assert ordered==(g-1)*(g-2)
    assert len(set(signatures(table,[0,1,p])))==q
    both=[(table[x],table[(x+(1 if table[x]%p==0 else p))%q]) for x in range(q)]
    assert len(set(both))==q
    return ordered


def repository_checks(repo):
    from enterprise_math import partial_operation_quotient as po
    from enterprise_math import composition_safe_collapse as cc
    from enterprise_math.brc_transport import Affine
    checked=0
    for n in (8,16,25,48,64,81,96):
        for r in (1,2,3):
            e=2**r
            states=list(range(n))
            add={x:(x+1)%n for x in states}
            power={x:pow(x,e,n) for x in states}
            # Current observation is the prospective block h=0. Translations
            # are unobserved until the probe, and arbitrary words may follow.
            stable=po.stable_partial_family_partition(states,{'add':add,'power':power},power)
            period=prod(prime_period(p,k,r) for p,k in factors(n))
            model={x:x%period for x in states}
            assert po.partitions_equivalent(states,stable,model)
            assert cc.fiber_constancy_witness(states,model,power) is None
            checked+=1
    assert Affine(((1,),),(1,)).then(Affine(((1,),),(2,))).apply((2,))==(5,)
    here=repo/'research_inputs/fermat_residual_20261004/source_archive.zip'
    assert sha256(here.read_bytes()).hexdigest()=='7d2002193d3cb5ef79d699354a86ab0d0082a853623290c89abbdb818b3fb7dd'
    with zipfile.ZipFile(here) as archive:
        for line in archive.read('MANIFEST.sha256').decode().splitlines():
            digest,member=line.split()
            assert sha256(archive.read(member)).hexdigest()==digest
    hashes={}
    for name in ['partial_operation_quotient','composition_safe_collapse','brc_transport']:
        b=(repo/'src/enterprise_math'/(name+'.py')).read_bytes()
        hashes[name]=sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    return {'future_partition_comparisons':checked,'source_git_blobs':hashes}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,default=Path('/workspace/enterprise-math'))
    p.add_argument('--verify',type=Path)
    args=p.parse_args()
    repo=args.repo.resolve()
    sys.path.insert(0,str(repo/'src'))
    count=0
    for n in range(2,145):
        for r in range(1,6):
            e=2**r
            period=prod(prime_period(p,k,r) for p,k in factors(n))
            power=[pow(x,e,n) for x in range(n)]
            assert equivalent(signatures(power,range(n)),[x%period for x in range(n)])
            count+=1
    clipped=0
    for p,k in [(2,1),(2,4),(2,6),(3,3),(5,2),(7,2)]:
        q=p**k
        for r in range(1,5):
            e=2**r
            def value(x):
                a=0
                while a<k and x%p==0:
                    a+=1
                    x//=p
                return min(k,e*a)
            h=(k+e-1)//e
            assert equivalent(signatures([value(x) for x in range(q)],range(q)),[x%(p**h) for x in range(q)])
            clipped+=1
    fiber_tests=0
    for p,bound in [(2,9),(3,6),(5,4),(7,3)]:
        for k in range(1,bound+1):
            for r in range(1,6):
                power_fibers(p,k,r)
                fiber_tests+=1
    powers2=Counter(two_adic(2**k,k,r) for k in range(1,10) for r in range(1,6))
    lifts={str((p,k,r)):odd_lifts(p,k,r) for p,k in [(3,3),(5,2),(5,3),(7,2),(13,2),(17,2)] for r in (1,2,3,4)}
    fields=[field_probes(p,r) for p in (3,5,7,13,17,29,41) for r in (1,2,3,4)]
    assert (2*2+1)%25 == 5 and (7*7+1)%25==0
    result={'full_period_tables':count,'valuation_tables':clipped,'unshifted_prime_power_fiber_histograms':fiber_tests,
            'two_adic_optimum_counts':dict(powers2),'odd_two_probe_ordered_collisions':lifts,
            'finite_field_optima':fields,'original_tool_checks':repository_checks(repo)}
    if args.verify:
        assert json.loads(json.dumps(result))==json.loads(args.verify.read_text())
        print('PASS')
    else:
        print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
