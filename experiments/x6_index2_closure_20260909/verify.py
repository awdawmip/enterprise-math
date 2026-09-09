#!/usr/bin/env python3
"""Exact finite checks for the X6 index-2 closure research note.

From an EM checkout:
    python experiments/x6_index2_closure_20260909/verify.py --output results.json

Uses the existing finite_symmetry implementation; no new toolbox family.
All classification/count checks are integer or finite-set computations.
The general number-theoretic theorem is proved/cited in the note, not inferred
from finite samples.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
try:
    from enterprise_math.finite_symmetry import orbit_partition, global_fixed_points
except ImportError as exc:
    raise SystemExit(
        "Run in an EM checkout, or set PYTHONPATH to the supplied source_excerpt "
        "for local reproduction. Do not substitute a new symmetry engine."
    ) from exc

D = 6
Matrix = tuple[tuple[int, ...], ...]
Pair = tuple[int, int]

def eye() -> Matrix:
    return tuple(tuple(int(i == j) for j in range(D)) for i in range(D))

def trn(a: Matrix) -> Matrix:
    return tuple(zip(*a))

def mul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(sum(x*y for x, y in zip(row, col))
                       for col in zip(*b)) for row in a)

def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(x+y for x, y in zip(r, s)) for r, s in zip(a, b))

def scale(k: int, a: Matrix) -> Matrix:
    return tuple(tuple(k*x for x in r) for r in a)

def gram(a: Matrix) -> Matrix:
    return mul(trn(a), a)

def trace(a: Matrix) -> int:
    return sum(a[i][i] for i in range(D))

def delta(a: Matrix) -> int:
    g = gram(a)
    return D*sum(x*x for row in g for x in row) - trace(g)**2

def defect(a: Matrix) -> Matrix:
    g = gram(a)
    return add(scale(D, g), scale(-trace(g), eye()))

def determinant(a: Matrix) -> int:
    # Bareiss elimination: exact, no floating determinant tolerances.
    b = [list(r) for r in a]
    sign, previous = 1, 1
    for k in range(D-1):
        pivot = next((i for i in range(k,D) if b[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            b[k], b[pivot] = b[pivot], b[k]
            sign = -sign
        v = b[k][k]
        for i in range(k+1,D):
            for j in range(k+1,D):
                numerator = b[i][j]*v - b[i][k]*b[k][j]
                assert numerator % previous == 0
                b[i][j] = numerator // previous
        for i in range(k+1,D):
            b[i][k] = 0
        previous = v
    return sign*b[-1][-1]

def pair_gate(pair: Pair) -> Matrix:
    i,j = pair
    a = [list(r) for r in eye()]
    a[i][i], a[i][j], a[j][i], a[j][j] = 1,1,1,-1
    return tuple(map(tuple,a))

def matchings(items: tuple[int,...]):
    if not items:
        yield ()
        return
    a = items[0]
    for b in items[1:]:
        for rest in matchings(tuple(x for x in items[1:] if x != b)):
            yield tuple(sorted(((a,b),)+rest))

def mask(pair: Pair) -> int:
    return sum(1 << i for i in pair)

def span(vectors) -> frozenset[int]:
    result = {0}
    for v in vectors:
        result |= {x ^ v for x in tuple(result)}
    return frozenset(result)

def relabel(v: int, p: tuple[int,...]) -> int:
    return sum(1 << p[i] for i in range(D) if v & (1 << i))

def orthogonal_line_census(q: int):
    assert q in (2,3)
    vectors = []
    for support in combinations(range(D),q):
        for signs in product((-1,1),repeat=q-1):
            v = [0]*D
            v[support[0]] = 1
            for i,s in zip(support[1:],signs):
                v[i] = s
            vectors.append(tuple(v))
    adjacency = [0]*len(vectors)
    for i,j in combinations(range(len(vectors)),2):
        if sum(x*y for x,y in zip(vectors[i],vectors[j])) == 0:
            adjacency[i] |= 1 << j
            adjacency[j] |= 1 << i
    sizes = Counter()
    frames = []
    def visit(chosen: tuple[int,...], candidates: int):
        sizes[len(chosen)] += 1
        if len(chosen) == D:
            frames.append(chosen)
        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            i = bit.bit_length()-1
            visit(chosen+(i,), candidates & adjacency[i])
    visit((),(1 << len(vectors))-1)
    return vectors,dict(sorted(sizes.items())),frames

def run() -> dict:
    pairs = tuple(combinations(range(D),2))
    gates = {p:pair_gate(p) for p in pairs}
    ms = tuple(sorted(set(matchings(tuple(range(D))))))
    assert len(ms) == 15
    for a in gates.values():
        assert abs(determinant(a)) == 2 and delta(a) == 8

    # Execute the existing T7 symmetry implementation, complete S6 action.
    branch_masks = tuple(range(1,1 << D))
    actions = {p:{v:relabel(v,p) for v in branch_masks}
               for p in permutations(range(D))}
    orbits = orbit_partition(branch_masks, actions)
    assert sorted(map(len,orbits)) == [1,6,6,15,15,20]
    assert global_fixed_points(branch_masks,actions) == frozenset({63})
    minimal_masks = tuple(mask(p) for p in pairs)
    restricted = {p:{v:action[v] for v in minimal_masks}
                  for p,action in actions.items()}
    assert global_fixed_points(minimal_masks,restricted) == frozenset()

    duals = tuple(span(mask(p) for p in m) for m in ms)
    assert len(set(duals)) == 15 and all(len(w)==8 for w in duals)
    incidence = {v:sum(v in w for w in duals) for v in branch_masks}
    table = []
    for w in range(1,7):
        vs = [v for v in branch_masks if v.bit_count()==w]
        counts = {incidence[v] for v in vs}
        assert len(counts)==1
        n = counts.pop()
        table.append({"weight":w,"branches":len(vs),
                      "terminal_lattices_per_branch":n,
                      "flags_per_branch":3*n})
    assert [r["terminal_lattices_per_branch"] for r in table] == [0,3,0,3,0,15]
    flags = set()
    for index,w in enumerate(duals):
        for v in w-{0}:
            planes = {span((v,u)) for u in w-span((v,))}
            assert len(planes)==3
            for plane in planes:
                flags.add((index,v,tuple(sorted(plane))))
    assert len(flags)==315
    assert sum(incidence[v] > 0 for v in branch_masks)==31

    # Right products give actual nested image-lattice chains.
    histogram = Counter()
    closed = []
    for triple in product(pairs,repeat=3):
        a = eye()
        for p in triple:
            a = mul(a,gates[p])
        d = delta(a)
        histogram[d] += 1
        disjoint = len({i for p in triple for i in p}) == D
        assert (d==0) == disjoint
        if d==0:
            assert gram(a) == scale(2,eye())
            assert abs(determinant(a)) == 8
            closed.append(triple)
    assert len(closed)==90
    assert dict(sorted(histogram.items())) == {
        0:90,29:1080,56:990,129:720,152:240,233:240,392:15}

    # Independent exhaustive norm-2 / norm-3 frame census.
    _,q2,q2frames = orthogonal_line_census(2)
    _,q3,q3frames = orthogonal_line_census(3)
    assert q2[6]==15 and len(q2frames)==15
    assert max(q3)==4 and not q3frames

    # Complete inventory of five-round pair-balanced schedules.
    factorizations = tuple(fs for fs in combinations(ms,5)
        if len({p for m in fs for p in m})==15)
    assert len(factorizations)==6
    epochs = []
    a = eye()
    for k,m in enumerate(factorizations[0],1):
        for p in m:
            a = mul(a,gates[p])
        assert gram(a)==scale(2**k,eye())
        assert abs(determinant(a))==2**(3*k)
        epochs.append({"epoch":k,"index":2**(3*k),
                       "gram_scalar":2**k,"delta":delta(a)})

    # T6 exact future-observation failure. Left composition is explicitly
    # declared here; it is NOT the nested-chain update convention above.
    a = gates[(0,1)]
    p = tuple(tuple(int(j==[2,3,0,1,4,5][i]) for j in range(D)) for i in range(D))
    a2 = mul(p,a)
    assert gram(a2)==gram(a)
    assert delta(mul(a,a))==72
    assert delta(mul(a,a2))==8
    u = [list(r) for r in eye()]
    u[2][3] = 1
    u = tuple(map(tuple,u))
    assert determinant(u)==1
    assert delta(mul(a,u))==21  # Same image lattice, different basis.

    # Integer, oriented Gram-defect composition law for every gate pair.
    for left,right in product(gates.values(),repeat=2):
        inner = mul(mul(trn(right),defect(left)),right)
        lhs = scale(D,defect(mul(left,right)))
        rhs = add(add(scale(trace(gram(left)),defect(right)),
                      scale(D,inner)),scale(-trace(inner),eye()))
        assert lhs==rhs

    return {
        "status":"ALL_EXACT_FINITE_CHECKS_PASSED_NOT_FORMAL_PROOF_OR_ADMISSION",
        "source_snapshot":"cf224163a9fe5ea4f3ac6d8dd5e13f1b771daf44",
        "symmetry_reuse":{
            "source":"src/enterprise_math/finite_symmetry.py",
            "git_blob":"ae96a32cb6b6fdd974bd9f44fb28a1b643c9b8a2",
            "functions":["orbit_partition","global_fixed_points"],
            "resolution":"REUSE_EXECUTED",
            "local_run_note":"Exact fetched function/dependency excerpt; EM uses its complete upstream module."
        },
        "branches":63,"admissible_first_branches":31,
        "terminal_lattices":15,"nested_index2_flags":315,
        "branch_weight_table":table,
        "pair_triples_tested":3375,"pair_triples_closed":90,
        "delta_histogram":dict(sorted(histogram.items())),
        "uniform_pair_word_probability":str(Fraction(90,3375)),
        "uniform_nested_sublattice_probability":str(Fraction(315,63**3)),
        "q2_orthogonal_line_subset_counts":q2,
        "q3_orthogonal_line_subset_counts":q3,
        "five_matching_factorizations":6,
        "one_pair_balanced_schedule_1based":[
            [[i+1,j+1] for i,j in m] for m in factorizations[0]],
        "epoch_checks":epochs,
        "same_gram_future_delta_witness":[72,8],
        "same_lattice_basis_delta_witness":[8,21],
        "defect_composition_pairs_checked":225
    }

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding="utf-8")
    print(text,end="")

if __name__=="__main__":
    main()
