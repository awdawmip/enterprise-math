"""R181 — source-presence observer quotient and minimum rational affine dimension.

Exact reference implementation; pure Python 3, no third-party dependencies.
Native enterprise_math module execution remains a separate integration test.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import json
import random


def bitmask(word, targets):
    """A word is a tuple of complete (branch_id, source_id, signed_X6_path) atoms."""
    loc = {t: i for i, t in enumerate(targets)}
    result = 0
    for branch_id, source_id, path in word:
        if source_id in loc:
            result |= 1 << loc[source_id]
    return result


def affine(mask, k):
    """Diagonal affine action (a_i,b_i), x_i -> a_i*x_i+b_i."""
    return tuple((F(1-((mask>>i)&1)), F((mask>>i)&1)) for i in range(k))


def then(first, later):
    return tuple((b[0]*a[0], b[0]*a[1]+b[1]) for a,b in zip(first,later))


def evaluate(action, x):
    return tuple(a*y+b for (a,b), y in zip(action,x))


def normalize(terms):
    counts=defaultdict(int)
    for w,action,n in terms:
        assert isinstance(w,F) and w>0
        assert isinstance(n,int) and n>=0
        if n:
            counts[w,action]+=n
    return tuple(sorted((w,a,n) for (w,a),n in counts.items()))


def push(terms, targets):
    k=len(targets)
    return normalize((w,affine(bitmask(word,targets),k),n) for w,word,n in terms)


def fine_then(A,B):
    return [(w*v,a+b,c*d) for w,a,c in A for v,b,d in B]


def coarse_then(A,B):
    return normalize((w*v,then(a,b),c*d) for w,a,c in A for v,b,d in B)


def test():
    targets=(0,2**65+17,991,2**128+99)
    k=len(targets)
    steps=tuple((i,s) for i in range(6) for s in (-1,1))
    atoms=tuple((branch,source,tuple(steps[t] for t in path))
        for branch in (0,1,2**65+3)
        for source in (*targets,7)
        for path in ((),(0,),(0,1),(5,3,10)))
    rng=random.Random(181)
    masks=range(1<<k)

    def witness(mask):
        return tuple((0,targets[j],()) for j in range(k) if (mask>>j)&1)

    assert {bitmask(witness(m),targets) for m in masks} == set(masks)
    assert len({affine(m,k) for m in masks}) == 1<<k
    for a,b in product(masks,repeat=2):
        assert then(affine(a,k),affine(b,k)) == affine(a|b,k)
        for x in ((F(0),)*k,(F(1,2),)*k,tuple(F(i-1,3) for i in range(k))):
            assert evaluate(affine(a,k),x) == tuple(F(1) if ((a>>j)&1) else x[j] for j in range(k))

    # Characters chi_A(S) are 1 exactly when S is disjoint from A.
    # Comparing full set with full-minus-singleton requires the singleton character.
    full=(1<<k)-1
    needed=[]
    for j in range(k):
        chars=[A for A in masks if int((full&A)==0) != int(((full^(1<<j))&A)==0)]
        assert chars == [1<<j]
        needed.append(chars[0])
    assert len(set(needed))==k

    for _ in range(1200):
        a=tuple(rng.choice(atoms) for t in range(rng.randrange(5)))
        b=tuple(rng.choice(atoms) for t in range(rng.randrange(5)))
        c=tuple(rng.choice(atoms) for t in range(rng.randrange(5)))
        assert bitmask(a+b,targets) == (bitmask(a,targets)|bitmask(b,targets))
        assert bitmask(c+a+b,targets) == (bitmask(c,targets)|bitmask(a,targets)|bitmask(b,targets))

    weights=(F(1,3),F(3,7),F(2,5),F(1))
    for _ in range(360):
        A=[(rng.choice(weights),tuple(rng.choice(atoms) for t in range(rng.randrange(4))),rng.randint(1,3))
           for z in range(1+rng.randrange(4))]
        B=[(rng.choice(weights),tuple(rng.choice(atoms) for t in range(rng.randrange(4))),rng.randint(1,3))
           for z in range(1+rng.randrange(4))]
        assert push(A+B,targets) == normalize(push(A,targets)+push(B,targets))
        assert push(fine_then(A,B),targets) == coarse_then(push(A,targets),push(B,targets))

    primes=(2,3,5,7)
    def scale(counts):
        x=1
        for p,c in zip(primes,counts):
            x*=p**c
        return x
    vectors=list(product(range(4),repeat=k))
    assert len({scale(c) for c in vectors})==len(vectors)==256
    for _ in range(250):
        a=tuple(rng.randrange(4) for i in range(k))
        b=tuple(rng.randrange(4) for i in range(k))
        assert scale(tuple(x+y for x,y in zip(a,b)))==scale(a)*scale(b)

    return {
       "schema":"R181_SOURCE_PRESENCE_QUERY_QUOTIENT_V1",
       "reference":"complete R180 typed atom histories and exact positive rational histogram",
       "selectors":list(map(str,targets)),"k":k,"masks":1<<k,
       "optimal_affine_dimension":k,
       "exhaustive_affine_mask_compositions":(1<<k)**2,
       "necessary_singleton_characters":needed,
       "seeded_context_checks":1200,
       "exact_positive_histogram_pair_checks":360,
       "prime_count_vector_injections_in_box_0_to_3":256,
       "prime_scaling_composition_checks":250,
       "native_package_executed":False,
       "result":"R181_EXACT_REFERENCE_PASS"
    }


if __name__ == "__main__":
    print(json.dumps(test(),indent=2,sort_keys=True))
