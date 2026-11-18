"""Exact finite-module probe checks; named fields occur only in the verifier."""
import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb, gcd
from pathlib import Path


def proj_count(p,d):
    return (p**d-1)//(p-1)


def support(x):
    return tuple(i for i,a in enumerate(x) if a)


def span(vs,p,d):
    ans={(0,)*d}
    for v in vs:
        if v in ans:
            continue
        ans={tuple((x[i]+c*v[i])%p for i in range(d)) for x in ans for c in range(p)}
    return frozenset(ans)


def normalized(x,p):
    pivot=next(c for c in x if c)
    return tuple((a*pow(pivot,-1,p))%p for a in x)


def projective(p,d):
    return sorted({normalized(v,p) for v in product(range(p),repeat=d) if any(v)})


def subspaces(p,d,r):
    if r==0:
        return {frozenset({(0,)*d})}
    points=projective(p,d)
    seen=set()
    for reps in combinations(points,r):
        vs=span(reps,p,d)
        if len(vs)==p**r:
            seen.add(vs)
    return seen


def sums(p,q):
    n=p*q
    units={i for i in range(n) if gcd(i,n)==1}
    c={0}|units
    twice={(x-y)%n for x in c for y in c}
    three={(x+y)%n for x in twice for y in c}
    assert twice==set(range(n))-({q} if p==2 else set())
    assert three==set(range(n))
    for z in range(n):
        expected=(p-1-int(z%p!=0))*(q-1-int(z%q!=0))
        assert sum((x+z)%n in units for x in units)==expected
    return dict(primes=[p,q],unit_count=len(units),unary=len(c),
                binary=len(twice),ternary=len(three),minimal_full_arity=3 if p==2 else 2)


def core(u,v,p,q,d):
    left=defaultdict(set);right=defaultdict(set)
    for x in u: left[support(x)].add(x)
    for y in v: right[support(y)].add(y)
    both=left.keys()&right.keys()
    return (span([x for s in both for x in left[s]],p,d),
            span([x for s in both for x in right[s]],q,d))


def shortened(u,v):
    d=len(next(iter(u))); indices=set(range(d))
    while True:
        a=frozenset(x for x in u if set(support(x))<=indices)
        b=frozenset(x for x in v if set(support(x))<=indices)
        active=set().union(*(set(support(x)) for x in a))&set().union(*(set(support(x)) for x in b))
        if active==indices: return a,b
        indices=active


def classify(p,q,d):
    n=p*q
    c={i for i in range(n) if i==0 or gcd(i,n)==1}
    probes=list(product(sorted(c),repeat=d))
    tested=[(tuple(i%p for i in x),tuple(i%q for i in x)) for x in probes]
    spacesp=set().union(*(subspaces(p,d,r) for r in range(d+1)))
    spacesq=set().union(*(subspaces(q,d,r) for r in range(d+1)))
    by_answers={};by_core={};equal_count=0
    for u,v in product(spacesp,spacesq):
        answers=tuple(i for i,(a,b) in enumerate(tested) if a in u and b in v)
        actual=core(u,v,p,q,d)
        assert by_answers.setdefault(answers,actual)==actual
        assert by_core.setdefault(actual,answers)==answers
        assert core(*actual,p,q,d)==actual
        if min(p,q)>d+1:
            assert shortened(u,v)==actual
        if (u,v)==actual:equal_count+=1
    return dict(primes=[p,q],dimension=d,submodules=len(spacesp)*len(spacesq),
                clean_queries=len(probes),observable_cores=len(by_core),
                already_equal_to_core=equal_count)


def blocking(p,d,r):
    pts=projective(p,d)
    flats=subspaces(p,d,r)
    masks=[sum(1<<i for i,x in enumerate(pts) if x in flat) for flat in flats]
    t=proj_count(p,d-r+1)
    witness=sum(1<<i for i,x in enumerate(pts) if not any(x[d-r+1:]))
    assert witness.bit_count()==t and all(witness&m for m in masks)
    # All smaller hitting sets extend to one of size t-1. Check that last size.
    tested=0
    for S in combinations(range(len(pts)),t-1):
        mask=sum(1<<i for i in S)
        assert any(not mask&m for m in masks)
        tested+=1
    assert tested==comb(len(pts),t-1)
    return dict(prime=p,dimension=d,promised_rank=r,projective_points=len(pts),
                flats=len(masks),minimum=t,all_smaller_boundary_sets_checked=tested)


def public_minimal_cyclic(n,d):
    # Purely extensional enumeration from public n,d. This slow reflection is
    # outside the scalar-clean phase. No prime-coordinate decomposition here.
    vectors=list(product(range(n),repeat=d))
    cyclic={frozenset(tuple(k*z%n for z in v) for k in range(n)) for v in vectors if any(v)}
    atoms=[line for line in cyclic if not any(other<line for other in cyclic)]
    return [min(x for x in line if any(x)) for line in atoms]


def minimax(n,p,q,d,k):
    reps=public_minimal_cyclic(n,d)
    total=proj_count(p,d)+proj_count(q,d)
    assert len(reps)==total
    truth=[]
    for prime,other in ((p,q),(q,p)):
        for x in projective(prime,d):
            line=span([x],prime,d)
            good={i for i,v in enumerate(reps) if not any(z%other for z in v)
                  and tuple(z%prime for z in v) in line}
            assert len(good)==1
            truth.append(next(iter(good)))
    assert sorted(truth)==list(range(total))
    error=Fraction(total-k,2*total-k)
    all_subsets=list(combinations(range(total),k))
    for marked in truth:
        miss=Fraction(sum(marked not in s for s in all_subsets),len(all_subsets))
        assert miss*(1-error)==error
    return dict(public_n=n,dimension=d,one_sided_lines=total,query_budget=k,
                subsets=len(all_subsets),two_sided_minimax_error=str(error),
                one_sided_false_negative=str(Fraction(total-k,total)))


def fixtures():
    # Exact public parent kernel as an oracle for fixed tiny public modulus.
    n=15;d=2
    vectors=list(product(range(n),repeat=d))
    kernel={x for x in vectors if (x[0]+x[1])%n==0 and (x[0]+4*x[1])%n==0}
    c=[x for x in vectors if all(a==0 or gcd(a,n)==1 for a in x)]
    assert kernel=={(0,0),(5,10),(10,5)}
    assert set(c)&kernel=={(0,0)}
    x=(1,2); y=(11,7)
    assert x in c and y in c and x!=y
    assert tuple((a-b)%n for a,b in zip(x,y)) in kernel
    p,q,d=3,5,4
    u=span([(1,1,1,0),(0,1,2,1)],p,d)
    v=span([(1,)*d],q,d)
    assert all(len(support(z))==3 for z in u if any(z))
    assert len(core(u,v,p,q,d)[0])==len(core(u,v,p,q,d)[1])==1
    assert shortened(u,v)==(u,v)
    return dict(public_parent_n=n,full_kernel=sorted(kernel),
                normalized_pair=[x,y],unary_hits_including_zero=1,
                small_field_mask_counterexample=dict(primes=[p,q],dimension=d,
                    crt_ranks=[2,1],visible_ranks=[0,0]))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--verify',type=Path)
    args=ap.parse_args()
    result=dict(arity=[sums(p,q) for p,q in [(2,3),(2,5),(2,7),(3,5),(3,7),(3,11),(5,7)]],
                clean_core=[classify(p,q,2) for p,q in [(2,3),(3,5),(5,7)]],
                blocking=[blocking(*s) for s in [(2,4,2),(2,4,3),(3,3,2),(5,3,2)]],
                exact_randomized=[minimax(6,2,3,2,2),minimax(15,3,5,2,3)],examples=fixtures())
    out=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.verify:
        assert out==args.verify.read_text()
        print('PASS',sha256(out.encode()).hexdigest())
    else:
        print(out,end='')


if __name__=='__main__':
    main()
