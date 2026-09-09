#!/usr/bin/env python3
"""Exact X6 face-snake experiment. A domain construction, not a native law.

Run: python verify.py --reuse /path/to/composition_safe_collapse.py --limit 262144
No network I/O. The optional --output stores a reproducible JSON report.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
from itertools import islice, product
import json
from math import prod
from pathlib import Path
import random
from typing import Iterator, Sequence

D = 6
SOURCE = 'd40aa672623d6fc82af4cbb60964e6a628267e62'
REUSE_BLOB = '384d166f642fb65c53fc7f2431f43dc99880693a'
START_BITS = ((1,1,1,1,1,1),(0,1,1,1,1,0),
              (1,1,0,1,0,1),(0,1,0,1,0,0))
ROUND_DIRS = ((1,-1,-1,-1,-1,-1),(-1,1,1,1,1,1),
              (1,-1,1,-1,1,-1),(-1,1,-1,1,-1,1))
Point = tuple[int, ...]


def snake_point(k: int, lengths: Sequence[int]) -> tuple[int, ...]:
    """Mixed-radix reflected snake; axis 0 is fastest."""
    if any(a < 1 for a in lengths) or not 0 <= k < prod(lengths):
        raise ValueError('bad local index or side length')
    if not lengths:
        return ()
    block = prod(lengths[:-1])
    digit, rem = divmod(k, block)
    if digit % 2:
        rem = block - 1 - rem
    return snake_point(rem, lengths[:-1]) + (digit,)


def snake_rank(u: Sequence[int], lengths: Sequence[int]) -> int:
    if len(u) != len(lengths) or any(not 0 <= b < a for b,a in zip(u,lengths)):
        raise ValueError('bad local point')
    if not lengths:
        return 0
    block = prod(lengths[:-1])
    rem = snake_rank(u[:-1], lengths[:-1])
    return u[-1]*block + (block-1-rem if u[-1] % 2 else rem)


def corners_after_face(bits: list[int], lengths: Sequence[int], axis: int) -> list[int]:
    out = bits.copy()
    odd = 1
    for j in reversed([(axis+t)%D for t in range(1,D)]):
        out[j] ^= odd
        odd *= lengths[j] % 2
    return out


def box_before_round(r: int) -> tuple[list[int],list[int],list[int]]:
    if r < 0:
        raise ValueError('negative round')
    a = r//2
    lo, hi = [-a]*D, [a]*D
    if r % 2:
        for i, sign in enumerate(ROUND_DIRS[(r-1)%4]):
            if sign == 1: hi[i] += 1
            else: lo[i] -= 1
    return lo, hi, list(START_BITS[r%4])


def sixth_root_floor(n: int) -> int:
    if n < 0: raise ValueError('negative integer')
    low, high = 0, 1 << ((n.bit_length()+5)//6)
    while low+1 < high:
        mid = (low+high)//2
        if mid**6 <= n: low = mid
        else: high = mid
    return high if high**6 <= n else low


def point(k: int) -> Point:
    """Random access to the one fixed infinite face-snake enumeration."""
    if isinstance(k,bool) or not isinstance(k,int) or k < 0:
        raise ValueError('index must be a nonnegative integer')
    if k == 0: return (0,)*D
    s = sixth_root_floor(k)
    lo,hi,bits = box_before_round(s-1)
    for i in range(D):
        lengths = [hi[j]-lo[j]+1 for j in range(D)]
        before = prod(lengths)
        order = [(i+t)%D for t in range(1,D)]
        count = prod(lengths[j] for j in order)
        start = [hi[j] if bits[j] else lo[j] for j in range(D)]
        start[i] += 1 if bits[i] else -1
        if k < before+count:
            u = snake_point(k-before,[lengths[j] for j in order])
            for j,b in zip(order,u):
                start[j] += -b if bits[j] else b
            return tuple(start)
        if bits[i]: hi[i] += 1
        else: lo[i] -= 1
        bits = corners_after_face(bits,lengths,i)
    raise AssertionError('face interval missing')


def rank(z: Sequence[int]) -> int:
    """Inverse enumeration. Uses bounded integer searches, not a visited set."""
    if len(z)!=D or any(isinstance(v,bool) or not isinstance(v,int) for v in z):
        raise ValueError('point must have six integer coordinates')
    if all(v==0 for v in z): return 0
    low,high = 1, 2*max(map(abs,z))+1
    def inside(s: int) -> bool:
        a,b,_ = box_before_round(s-1)
        return all(a[j]<=z[j]<=b[j] for j in range(D))
    while low<high:
        mid=(low+high)//2
        if inside(mid): high=mid
        else: low=mid+1
    s=low-1
    lo,hi,bits=box_before_round(s-1)
    for i in range(D):
        lengths=[hi[j]-lo[j]+1 for j in range(D)]
        before=prod(lengths)
        start=[hi[j] if bits[j] else lo[j] for j in range(D)]
        start[i]+=1 if bits[i] else -1
        if bits[i]: hi[i]+=1
        else: lo[i]-=1
        if all(lo[j]<=z[j]<=hi[j] for j in range(D)):
            order=[(i+t)%D for t in range(1,D)]
            u=[start[j]-z[j] if bits[j] else z[j]-start[j] for j in order]
            return before+snake_rank(u,[lengths[j] for j in order])
        bits=corners_after_face(bits,lengths,i)
    raise AssertionError('point face missing')


def stream() -> Iterator[Point]:
    """Independent streaming construction, avoiding the closed-form round table."""
    lo,hi,bits=[0]*D,[0]*D,[1]*D
    yield (0,)*D
    while True:
        for i in range(D):
            lengths=[hi[j]-lo[j]+1 for j in range(D)]
            start=[hi[j] if bits[j] else lo[j] for j in range(D)]
            start[i]+=1 if bits[i] else -1
            order=[(i+t)%D for t in range(1,D)]
            for k in range(prod(lengths[j] for j in order)):
                u=snake_point(k,[lengths[j] for j in order])
                z=start.copy()
                for j,b in zip(order,u): z[j]+=-b if bits[j] else b
                yield tuple(z)
            if bits[i]: hi[i]+=1
            else: lo[i]-=1
            bits=corners_after_face(bits,lengths,i)


def axis_counts_to_cube(side: int) -> list[int]:
    lengths=[1]*D; counts=[0]*D
    for _ in range(side-1):
        for i in range(D):
            order=[(i+t)%D for t in range(1,D)]
            counts[i]+=1  # entering the new face
            outer=1
            for j in reversed(order):
                counts[j]+=(lengths[j]-1)*outer
                outer*=lengths[j]
            lengths[i]+=1
    assert sum(counts)==side**6-1
    return counts


def load_reuse(path: Path):
    data=path.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if blob!=REUSE_BLOB: raise ValueError('reuse source is not the pinned module')
    spec=importlib.util.spec_from_file_location('em_collapse',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify(reuse: Path, limit: int) -> dict:
    if limit < 46656: raise ValueError('limit must cover the 6^6 CRT milestone')
    mod=load_reuse(reuse)
    # Exhaustive local boxes establish the parity/endpoint implementation audit.
    local_cases=0
    for d in range(1,6):
        for dims in product(range(1,4), repeat=d):
            pts=[snake_point(k,dims) for k in range(prod(dims))]
            assert len(set(pts))==prod(dims)
            for k,u in enumerate(pts): assert snake_rank(u,dims)==k
            assert all(sum(abs(a-b) for a,b in zip(u,v))==1 for u,v in zip(pts,pts[1:]))
            local_cases+=1
    lo,hi,bits=[0]*D,[0]*D,[1]*D
    for r in range(12):
        assert (lo,hi,bits)==box_before_round(r)
        directions=[]
        for i in range(D):
            lengths=[hi[j]-lo[j]+1 for j in range(D)]
            directions.append(1 if bits[i] else -1)
            if bits[i]: hi[i]+=1
            else: lo[i]-=1
            bits=corners_after_face(bits,lengths,i)
        assert tuple(directions)==ROUND_DIRS[r%4]
    seen=set(); previous=None; plus=[0]*D; minus=[0]*D
    cube_rows=[]; crt=Counter(); axial_mod6=Counter(); inward=0
    rng=random.Random(6090903)
    selected=set(rng.randrange(limit) for _ in range(4000))|set(range(1000))
    for k,z in enumerate(islice(stream(),limit)):
        assert z not in seen; seen.add(z)
        if k in selected:
            assert point(k)==z
            assert rank(z)==k
        if previous is not None:
            dif=[z[i]-previous[i] for i in range(D)]
            assert sum(map(abs,dif))==1
            j=next(i for i,a in enumerate(dif) if a)
            (plus if dif[j]>0 else minus)[j]+=1
            inward+=sum(a*a for a in z)<sum(a*a for a in previous)
            assert 2*inward==k-sum(map(abs,z))
        previous=z
        if k<6**6:
            axial_mod6[tuple(a%6 for a in z)]+=1
            crt[(sum(z)%2,z[0]%3)]+=1
        n=k+1;s=sixth_root_floor(n)
        if s**6==n:
            lo,hi,_=box_before_round(s-1)
            assert all(tuple(v) in seen for v in product(*(range(lo[i],hi[i]+1) for i in range(D))))
            assert [plus[i]+minus[i] for i in range(D)]==axis_counts_to_cube(s)
            cube_rows.append({'side':s,'count':n,'lower':lo,'upper':hi,'axis_steps':[plus[i]+minus[i] for i in range(D)]})
    assert len(axial_mod6)==6**6 and set(axial_mod6.values())=={1}
    assert len(crt)==6 and set(crt.values())=={6**5}
    # Check exact uniform spatial coupling, locality and memory repair.
    coupling_checks=0
    for n in range(1,151):
        columns=[Fraction(0)]*(n+1); moving=Fraction(0)
        for i in range(n):
            a,b=Fraction(n-i,n*(n+1)),Fraction(i+1,n*(n+1))
            assert a+b==Fraction(1,n)
            columns[i]+=a; columns[i+1]+=b
            assert sum(abs(v-w) for v,w in zip(point(i),point(i+1)))==1
            moving+=b
        assert columns==[Fraction(1,n+1)]*(n+1) and moving==Fraction(1,2)
        coupling_checks+=1
    H=40
    cuts=sorted({Fraction(k,n) for n in range(1,H+1) for k in range(n+1)})
    theta=[(a+b)/2 for a,b in zip(cuts,cuts[1:])]
    domain=tuple(range(len(theta)))
    coarse={i:point(int(3*t)) for i,t in enumerate(theta)}
    observed={i:point(int(4*t)) for i,t in enumerate(theta)}
    witness=mod.fiber_constancy_witness(domain,coarse,observed)
    assert witness is not None
    part={i:() for i in domain}
    for n in range(1,H+1):
        ob={i:point(int(n*t)) for i,t in enumerate(theta)}
        part=mod.coarsest_one_step_repair(domain,part,ob)
    assert mod.class_count(part)==len(theta)==490
    # Floor history repair maps to actual Cell positions without changing laws.
    posterior={(Fraction(0),Fraction(1)):Fraction(1)}
    for n in range(1,31):
        nxt={}; spatial=Counter()
        for (a,b),weight in posterior.items():
            # This is the retained interval at layer n; its current rank is fixed.
            i=int(n*((a+b)/2))
            for j in (i,i+1):
                c=max(a,Fraction(j,n+1)); e=min(b,Fraction(j+1,n+1))
                if c<e:
                    w=weight*(e-c)/(b-a)
                    assert w==e-c
                    nxt[c,e]=nxt.get((c,e),Fraction(0))+w
                    spatial[point(j)]+=w
        assert set(spatial.values())=={Fraction(1,n+1)} and len(spatial)==n+1
        posterior=nxt
    # Random-access beyond enumeration range: exact round trips and adjacency.
    big=[]
    for bits_n in (40,80,160,320):
        for _ in range(20):
            k=rng.getrandbits(bits_n)
            z=point(k)
            assert rank(z)==k
            assert sum(abs(a-b) for a,b in zip(z,point(k+1)))==1
        big.append(bits_n)
    # Rectangular radix bridge, explicitly sZ^6 rather than the prime-selected L(s^6).
    radix_pairs=0
    for a in range(1,13):
        for b in range(1,13):
            vals={u+a*v for u in range(a) for v in range(b)}
            assert vals==set(range(a*b))
            radix_pairs+=1
    radix_six_axis_cases=0
    for _ in range(1000):
        a,b,c=[rng.randrange(1,1000) for _ in range(3)]
        u=[rng.randrange(a) for _ in range(D)]
        v=[rng.randrange(b) for _ in range(D)]
        w=[rng.randrange(c) for _ in range(D)]
        combined=[u[j]+a*v[j] for j in range(D)]
        assert [x%a for x in combined]==u
        assert [x//a for x in combined]==v
        assert [u[j]+a*(v[j]+b*w[j]) for j in range(D)]==[combined[j]+a*b*w[j] for j in range(D)]
        radix_six_axis_cases+=1
    # Purely moving marks cannot map one uniform path prefix to the next:
    # the bipartite signed mean would have to change sign, which it does not.
    for n in range(1,151):
        old=Fraction(n%2,n); new=Fraction((n+1)%2,n+1)
        assert new!=-old
    phase_rows=[]
    for t in (Fraction(1,5),Fraction(2,5),Fraction(4,5)):
        j2=int(2*t);j3=int(3*t)
        j5=int(5*t);j6=int(6*t)
        assert 0<=j5-j2-j3<=1
        assert 0<=j6-2*j3<2
        phase_rows.append({'theta':str(t),'ranks_2_3_5_6':[j2,j3,j5,j6]})
    return {
      'status':'PASS_EXACT_FINITE_REGRESSION_NOT_FORMAL_PROOF_OR_ADMISSION',
      'source_snapshot':SOURCE,'dimension':D,
      'enumerated_distinct_cells':limit,'native_edges_checked':limit-1,
      'random_access_prefix_roundtrips':len(selected),'local_snake_boxes':local_cases,
      'four_round_controller_verified_rounds':12,'complete_cubes':cube_rows,
      'uniform_native_couplings_checked':coupling_checks,
      'mean_native_squared_marked_step':'1/2',
      'crt_side6_full_residue_vectors':len(axial_mod6),'crt_pair_counts':[crt[k] for k in sorted(crt)],
      'posterior_interval_horizon':31,'posterior_state_count':len(posterior),
      't6_history_horizon':H,'t6_history_classes':mod.class_count(part),
      't6_current_cell_not_future_safe_witness_phases':[str(theta[i]) for i in witness],
      'large_index_bit_lengths':big,'large_index_roundtrips':80,
      'asymptotic_axis_fractions_side1000':[str(Fraction(c,1000**6-1)) for c in axis_counts_to_cube(1000)],
      'phase_arithmetic_examples':phase_rows,
      'rectangular_radix_pairs':radix_pairs,'six_axis_radix_associativity_cases':radix_six_axis_cases,
      'no_wait_uniform_mark_obstructions':150,
      'reuse':{'source':'src/enterprise_math/composition_safe_collapse.py','blob':REUSE_BLOB,'state':'REUSE_EXECUTED'},
      'boundaries':['chosen enumeration, not unique dynamics','waits permitted for marked Cell, not for enumeration edges',
         'residue uniformity is fixed-modulus occupancy, not changing-modulus equivariant successor',
         'floor refinement does not replace canonical quotient maps','no integer-index multiplication action on occupied sets',
         'no Foundation promotion or independent review']}


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--reuse',type=Path,required=True)
    ap.add_argument('--limit',type=int,default=262144)
    ap.add_argument('--output',type=Path)
    ns=ap.parse_args()
    result=verify(ns.reuse,ns.limit)
    text=json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    if ns.output: ns.output.write_text(text,encoding='utf-8')
    print(text)
if __name__=='__main__': main()
