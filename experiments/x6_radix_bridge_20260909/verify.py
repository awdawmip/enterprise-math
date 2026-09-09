#!/usr/bin/env python3
"""Exact, task-scoped radix bridge regression; no network and no new tool family.

In the EM repository run this file directly. For a detached source bundle supply
--source-root with the three pinned dependencies below. An independent proof is
in the accompanying research note; these checks do not constitute admission.
"""
from __future__ import annotations
import argparse
from collections import Counter
from functools import lru_cache
import hashlib
import importlib.util
from itertools import product
import json
from math import prod
from pathlib import Path
import random
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

D = 6
SOURCE = '6cf0edabb2b1d5551ba30e8efc27044363d9ed1f'
DEPENDENCIES = {
 'walk': ('experiments/x6_native_growth_20260909/verify.py', '01db1ef95bc120491e36653c45c88f6728e602f5'),
 'lattice': ('experiments/x6_coherent_arithmetic_20260909/verify.py', 'f4f46d080719adc2e59bc31c0d24d16c01dcd2a2'),
 't6': ('src/enterprise_math/composition_safe_collapse.py', '384d166f642fb65c53fc7f2431f43dc99880693a'),
}

def load_exact(root: Path, name: str):
    relative, expected = DEPENDENCIES[name]
    path = root/relative
    raw = path.read_bytes()
    actual = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if actual != expected:
        raise ValueError(f'Pinned dependency differs: {relative}; {actual}')
    spec = importlib.util.spec_from_file_location('x6_radix_reuse_'+name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def native_sum(a, b):
    return tuple(x+y for x,y in zip(a,b))


def coset_key_factory(a):
    det = int(a.det())
    adj = a.adjugate()
    coefficients = [[int(adj[i,j]) for j in range(D)] for i in range(D)]
    modulus = abs(det)
    def key(z):
        return tuple(sum(c*v for c,v in zip(row,z)) % modulus for row in coefficients)
    return key


def digits(h):
    """Standard rectangular representatives for an upper-triangular column HNF."""
    if h != hermite_normal_form(h):
        raise ValueError('Column HNF required')
    return tuple(product(*(range(int(h[i,i])) for i in range(h.rows))))


def reduce_hnf(z, h):
    """Exact z = digit + H*carry, by upper-triangular integer division."""
    r = sp.Matrix(z)
    c = sp.zeros(h.rows,1)
    for j in reversed(range(h.rows)):
        c[j] = int(r[j]) // int(h[j,j])
        r -= c[j]*h[:,j]
    assert all(0 <= r[j] < h[j,j] for j in range(h.rows))
    assert r+h*c == sp.Matrix(z)
    return sp.ImmutableMatrix(r), sp.ImmutableMatrix(c)


def verify(root):
    walk, old, t6 = (load_exact(root, name) for name in ('walk','lattice','t6'))
    eye = sp.eye(D)
    @lru_cache(None)
    def alternating_local(p, k):
        if k < 0 or not sp.isprime(p):
            raise ValueError('Prime and nonnegative exponent required')
        cycles, stage = divmod(k,6)
        if p == 2 or p % 4 == 1:
            b = sp.Matrix(old.gaussian_block(p))
            blocks = []
            for j in range(3):
                # B on the first pass, its conjugate on the second pass.
                blocks.append((p*sp.eye(2)) if stage >= j+4 else (b if stage >= j+1 else sp.eye(2)))
            a = p**cycles * sp.diag(*blocks)
        else:
            a = p**cycles * sp.diag(*(p if j<stage else 1 for j in range(D)))
        assert abs(a.det()) == p**k
        return sp.ImmutableMatrix(a)
    @lru_cache(None)
    def alt_basis(n):
        if n < 1: raise ValueError('Positive index required')
        a = sp.ImmutableMatrix(eye)
        for p,k in sorted(sp.factorint(n).items()):
            a = old.intersect(a, alternating_local(int(p),int(k)))
        assert abs(a.det()) == n
        return sp.ImmutableMatrix(hermite_normal_form(a))

    # First four Cells already forbid the fixed-frame, ordered base-2 law.
    pts = [walk.point(k) for k in range(4)]
    assert pts == [(0,0,0,0,0,0),(1,0,0,0,0,0),(1,-1,0,0,0,0),(0,-1,0,0,0,0)]
    assert pts[3] != native_sum(pts[1],pts[2])
    base2_defect = tuple(pts[3][i]-pts[1][i]-pts[2][i] for i in range(D))
    assert base2_defect == (-2,0,0,0,0,0)

    # Quotient support/repair census: no rounding or floating point coordinates.
    census=[]
    for n in range(1,97):
        key = coset_key_factory(old.basis(n))
        counts=Counter(key(walk.point(k)) for k in range(n))
        census.append({'index':n,'support':len(counts),'minimum_replacements':n-len(counts)})
    key3=coset_key_factory(old.basis(3))
    dom=tuple(range(3)); coarse={k:key3(walk.point(k)) for k in dom}
    q={k:sum(x*x for x in walk.point(k)) for k in dom}
    witness=t6.fiber_constancy_witness(dom,coarse,q)
    assert witness == (1,2) and not t6.descends_through(dom,coarse,q)
    assert t6.class_count(t6.coarsest_one_step_repair(dom,coarse,q)) == 3

    # Scale-5 cube and the frozen, one-chirality Gaussian lattice.
    n=5**6; key=coset_key_factory(old.basis(n))
    cube_counts=Counter(key(z) for z in product(range(-2,3),repeat=D))
    assert len(cube_counts)==21**3==9261
    hist=dict(sorted(Counter(cube_counts.values()).items()))
    assert hist == {1:4913,2:3468,4:816,8:64}
    assert sum(k*v for k,v in hist.items())==n
    assert n-len(cube_counts)==6364
    cube_vector=tuple(int(x) for x in old.basis(n)[:,0])
    assert cube_vector==(-3,4,0,0,0,0)
    left=(1,-2,0,0,0,0); right=(-2,2,0,0,0,0)
    assert tuple(y-x for x,y in zip(left,right))==cube_vector
    assert key(left)==key(right)

    # A genuinely changed local chain repairs every sixth-power box milestone.
    local_checks=0
    primes=(2,3,5,7,11,13,17,19,29)
    for p in primes:
        for k in range(18):
            b=alternating_local(p,k).inv()*alternating_local(p,k+1)
            assert old.integral(b) and abs(b.det())==p
            local_checks+=1
        for r in range(4):
            assert alternating_local(p,6*r)==p**r*eye
        if p == 2 or p%4 == 1:
            a=alternating_local(p,3)
            assert a.T*a==p*eye
        else:
            assert alternating_local(p,6)==p*eye
    cubes=[]
    for s in range(1,26):
        a=alt_basis(s**6)
        assert a==s*eye
        cubes.append(s)
    assert alt_basis(5**6) != hermite_normal_form(old.basis(5**6))
    # Conjugation does not remove the first non-cube obstruction.
    assert alt_basis(3)==hermite_normal_form(old.basis(3))
    assert len({coset_key_factory(alt_basis(3))(walk.point(k)) for k in range(3)})==2
    intersection_checks=0
    for n in range(1,13):
        for m in range(1,13):
            assert old.intersect(alt_basis(n),alt_basis(m))==alt_basis(int(sp.ilcm(n,m)))
            intersection_checks+=1

    # Every ordered n*m quotient has an exact relative radix, not necessarily S_nm.
    radix_pairs=0; radix_states=0; nonzero_carries=0; carry_example=None
    for n in range(1,13):
        for m in range(1,13):
            a=alt_basis(n); target=alt_basis(n*m)
            rel=a.inv()*target
            assert old.integral(rel) and abs(rel.det())==m
            hrel=hermite_normal_form(sp.Matrix(D,D,[int(x) for x in rel]))
            output=set()
            for u in digits(a):
                for v in digits(hrel):
                    z=sp.Matrix(u)+a*sp.Matrix(v)
                    d,c=reduce_hnf(z,target)
                    output.add(tuple(d)); radix_states+=1
                    if any(c):
                        nonzero_carries+=1
                        if carry_example is None:
                            carry_example={'n':n,'m':m,'u':list(u),'v':list(v),'raw':list(map(int,z)),
                                           'digit':list(map(int,d)),'carry':list(map(int,c))}
            assert len(output)==n*m and output==set(digits(target))
            radix_pairs+=1

    # A relative quotient is not generally the absolute same-index quotient.
    # On the first Gaussian stage, reuse of the absolute 2 digit collides at 4.
    a2=alt_basis(2); a4=alt_basis(4)
    d2=digits(a2); abs_outputs=Counter(tuple(reduce_hnf(sp.Matrix(u)+a2*sp.Matrix(v),a4)[0])
                                     for u in d2 for v in d2)
    assert len(abs_outputs)==2 # the properly relative choice gives 4

    # Exact additive cocycle. Dropping carries is not a native-coordinate identity.
    rng=random.Random(6090904); cocycles=0
    for n in range(2,18):
        h=alt_basis(n); dn=digits(h)
        for _ in range(20):
            a,b,c=(sp.Matrix(rng.choice(dn)) for __ in range(3))
            ab,kab=reduce_hnf(a+b,h); bc,kbc=reduce_hnf(b+c,h)
            d1,k1=reduce_hnf(ab+c,h); d2,k2=reduce_hnf(a+bc,h)
            assert d1==d2 and kab+k1==kbc+k2
            cocycles+=1

    # Non-affine rank radix is an exact set bijection; not claimed to be spatially linear.
    rank_cases=0; associativity_cases=0
    for n in range(1,25):
        for m in range(1,25):
            image={walk.point(a+n*b) for a in range(n) for b in range(m)}
            assert len(image)==n*m
            assert image=={walk.point(k) for k in range(n*m)}
            rank_cases+=1
    for n,m,l in product(range(1,7),repeat=3):
        for _ in range(5):
            a,b,c=rng.randrange(n),rng.randrange(m),rng.randrange(l)
            assert walk.point(a+n*(b+m*c))==walk.point((a+n*b)+n*m*c)
            associativity_cases+=1
    return {
      'status':'PASS_EXACT_TASK_REGRESSION_NOT_FORMAL_PROOF_OR_ADMISSION',
      'source_snapshot':SOURCE,'arithmetic':'integer/rational','sympy_version':sp.__version__,
      'ordered_base2_first_four_cells':[list(x) for x in pts], 'ordered_base2_defect':list(base2_defect),
      'prefix_quotient_census':census,
      'cube5':{'cells':15625,'support':9261,'minimum_replacements':6364,
               'total_variation_from_uniform':'6364/15625','multiplicity_histogram':hist,
               'collision_pair':[list(left),list(right)]},
      'conjugate_chain_local_checks':local_checks,'scalar_cube_sides_checked':cubes,
      'intersection_checks':intersection_checks,'relative_radix_pairs':radix_pairs,
      'relative_radix_states':radix_states,'nonzero_radix_carries':nonzero_carries,
      'first_nonzero_radix_carry':carry_example,
      'incorrect_absolute_2x2_support':len(abs_outputs), 'correct_relative_2x2_support':4,
      'carry_cocycle_cases':cocycles, 'rank_radix_pairs':rank_cases,
      'rank_associativity_cases':associativity_cases,
      't6_witness_at_index3':list(witness),'reuse':DEPENDENCIES,
      'not_claimed':['ordinary arithmetic changed','all prefixes are lattice digit sets',
        'same ordered enumeration is affine in every base','one-chirality chain unchanged',
        'rank radix is an intrinsic spatial dilation','independent review or Foundation admission']}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=verify(args.source_root)
    text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text,encoding='utf-8')
    print(text)
if __name__=='__main__':main()
