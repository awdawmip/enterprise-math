"""Exact A3 state, common-H, quotient and support-probe certificates."""
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from pathlib import Path
import json


FROZEN = "28f3000ea052b78b7b7ec3ba34c3d880ed98666b61eef2888d1890cd11e61b04"


def partitions(carrier, maps):
    remaining=set(carrier)
    out=[]
    while remaining:
        first=min(remaining)
        seen={first}
        stack=[first]
        while stack:
            x=stack.pop()
            for g in maps:
                y=g[x]
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        remaining-=seen
        out.append(seen)
    return out


def fixed_counts(partition):
    return dict(sorted(Counter(map(len,partition)).items()))


def weight_polynomial(parts):
    coeff=[1]
    for orbit in parts:
        n=len(orbit)
        ext=coeff+[0]*n
        for i,v in enumerate(coeff):
            ext[i+n]+=v
        coeff=ext
    return coeff


def restricted_counts(parts, pins, a):
    free=0
    for orbit in parts:
        values={pins[v] for v in orbit if v in pins}
        if len(values)>1:
            return 0
        free+=not values
    return a**free


def frozencase(m):
    b=m.ball(2)
    h={x:m.r_act(m.SWAP12,x) for x in b}
    g=m.SWAP23
    u={x:m.prefix_move(3,2,g,x) for x in b}
    l={x:m.prefix_move(2,2,g,x) for x in b}
    k={u[x]:l[x] for x in b}
    hk={x:h[k[x]] for x in b}
    partitions3=[partitions(b,[k]),partitions(b,[hk]),partitions(b,[k,h])]
    assert [len(c) for c in partitions3]==[77,41,39]
    f,mixed,both=[weight_polynomial(p) for p in partitions3]
    orbit_counts=[v+w-s for v,w,s in zip(f,mixed,both)]
    brute=[]
    for size in range(4):
        raw=global_h=0
        for s in combinations(b,size):
            z=frozenset(s)
            upper=frozenset(u[x] for x in z)
            lower=frozenset(l[x] for x in z)
            raw+=lower==upper
            global_h+=lower==upper or lower==frozenset(h[x] for x in upper)
        assert (raw,global_h)==(f[size],orbit_counts[size])
        brute.append([size,raw,global_h])
    p=(1,-1,0,0)
    pointers={r:m.r_act(m.inverse(g),m.anchor(r)) for r in (2,3)}
    assert all(m.r_act(g,ptr)==m.anchor(r) for r,ptr in pointers.items())
    assert u[p]==p and l[p]==(-1,0,1,0) and h[p]==p
    # Mark the frozen interior position and force its displaced mate to background.
    pins={p:1,l[p]:0}
    constrained=[restricted_counts(pt,pins,2) for pt in partitions3]
    return dict(marked_paths=[u[p],l[p]],pointers=pointers,
                block_cycle_lengths=[fixed_counts(pt) for pt in partitions3],
                unrestricted_binary_orbit_equality=str(Fraction(2**77+2**41-2**39,2**85)),
                low_weight_exact=brute,pinned_binary_orbit_equality_count=
                str(constrained[0]+constrained[1]-constrained[2]))


def local_test(m,n,d):
    q=n-d+1
    witness1=(1,0,-1,0)
    firstpair={(1,-1,0,0),(1,1,-1,-1)}
    def rigid(r):
        return (r,1,-1,-r)
    if n==1:
        return {(1,-1,0,0)}
    if d==1:
        return {witness1,rigid(n)}
    if q==1:
        return firstpair|{rigid(2)}
    return {witness1,rigid(q),rigid(q+1)}


def probe_test(m):
    gset=m.G
    identity=m.E
    h=m.SWAP12
    resid={identity,h}
    cent={g for g in gset if m.compose(g,h)==m.compose(h,g)}
    assert len(cent)==4
    census=Counter()
    for n in range(1,7):
        all_probe={(1,-1,0,0),(1,1,-1,-1)}|{(r,1,-1,-r) for r in range(2,n+1)}
        if n==1:
            all_probe={(1,-1,0,0)}
        for d in range(1,n+1):
            q=n-d+1
            probe=local_test(m,n,d)
            assert len(probe)==(1 if n==1 else (2 if d==1 else 3))
            for points in [probe,all_probe]:
                upper={g:frozenset(m.prefix_move(n+1,d,g,x) for x in points) for g in gset}
                lower={g:frozenset(m.prefix_move(n,d,g,x) for x in points) for g in gset}
                for gu,gl in product(gset,repeat=2):
                    a,b=upper[gu],lower[gl]
                    matches=b==a or b==frozenset(m.r_act(h,x) for x in a)
                    if n==1:
                        formula=gl in resid
                    elif d==1:
                        formula=gl==identity
                    elif q==1:
                        formula=gl in resid and gu==identity
                    else:
                        formula=gl==gu==identity
                    assert matches==formula
                    if points is probe:
                        census["actual_path_pairs"]+=1
                        census["equal_common_H"]+=matches
                        census["commuting_on_quotient"]+=bool(matches and gu in cent and gl in cent)
    return dict(census)


def group_closure(m,generators):
    known={m.E}
    stack=[m.E]
    while stack:
        a=stack.pop()
        for b in generators:
            s=m.compose(a,b)
            if s not in known:
                known.add(s)
                stack.append(s)
    return known


def repairs(m):
    sizes=Counter()
    for g in m.G:
        conjugates=set()
        t=m.SWAP12
        while t not in conjugates:
            conjugates.add(t)
            t=m.compose(m.compose(g,t),m.inverse(g))
        normal=group_closure(m,conjugates)
        difference=group_closure(m,[m.compose(t,m.SWAP12) for t in conjugates])
        assert difference=={t for t in normal if m.parity(t)==1}
        sizes[len(normal)]+=1
    assert dict(sizes)=={2:4,4:4,6:8,24:8}
    b=m.ball(2)
    g=m.SWAP23
    p={x:m.prefix_move(2,1,g,x) for x in b}
    h={x:m.r_act(m.SWAP12,x) for x in b}
    k={p[x]:p[h[x]] for x in b}
    delta={x:k[h[x]] for x in b}
    assert [len(partitions(b,maps)) for maps in ([h],[delta],[h,k])]==[45,41,23]
    # Independent six-point restriction: check every binary state and all iterations.
    seed=(2,1,-1,-2)
    support=next(o for o in partitions(b,[p,h]) if seed in o)
    assert len(support)==6
    checked=0
    for bits in product(range(2),repeat=len(support)):
        z=frozenset(x for x,bit in zip(sorted(support),bits) if bit)
        hz=frozenset(h[x] for x in z)
        eq=lambda a,b:b==a or b==frozenset(h[x] for x in a)
        assert (eq(z,hz) and eq({p[x] for x in z},{p[x] for x in hz}))==(
            hz==z or frozenset(delta[x] for x in z)==z)
        checked+=1
    return dict(normal_closure_size_hist=dict(sizes),n2_d1_counts=[45,41,23],
                restricted_binary_states=checked)


def shell_fixed(m):
    cases=0
    for r in range(1,8):
        shell=m.shell(r)
        for g in m.G:
            typ=sorted(map(len,partitions(range(4),[dict(enumerate(g))])))
            expect=16*r*r+2 if typ==[1,1,1,1] else (2*(r%3==0) if typ==[1,3] else 2)
            assert sum(m.r_act(g,x)==x for x in shell)==expect
            cases+=1
    return cases


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",required=True,type=Path)
    parser.add_argument("--json",type=Path)
    args=parser.parse_args()
    path=args.repo/"scripts/check_a3_recursive_shell_alignment_tomography.py"
    assert sha256(path.read_bytes()).hexdigest()==FROZEN
    spec=spec_from_file_location("frozen_a3_shell",path)
    m=module_from_spec(spec)
    spec.loader.exec_module(m)
    result=dict(frozen_checker_sha256=FROZEN,original_case=frozencase(m),probes=probe_test(m),
                repairs=repairs(m),fixed_point_checks=shell_fixed(m))
    data=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.json: args.json.write_text(data)
    else: print(data,end="")


if __name__=="__main__":
    main()
