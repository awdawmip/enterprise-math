"""Exact finite signed-triad observation checks for the anchored six-axis chart."""
import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from math import gcd
from pathlib import Path
import subprocess
import sys

N = 6
AXES = range(N)
TRIADS = tuple(combinations(AXES, 3))
IDENTITY = tuple(AXES)
J = (-1, -1, -1, 1, 1, 1)
PLUS = (1,) * N
CHECKER_HASH = "d523bd64fca6dbbb32fa94bbd1fbc6909a8f4ff289ed3f26786ffd373d9d9c06"


def view(triad, signs=(1, 1, 1)):
    return tuple(triad), tuple(signs)


def framed(p, eps, triad):
    return view([p[i] for i in triad], [eps[i] for i in triad])


def read(z, v):
    axes, signs = v
    y = [e*z[i] for i, e in zip(axes, signs)]
    return tuple(t-min(y) for t in y)


def contrasts(z, views, modulus):
    out = []
    for v in views:
        y = read(z, v)
        out.extend((y[j]-y[0]) % modulus for j in (1, 2))
    return tuple(out)


def edges(views):
    # y_j-y_0, multiplied by eps_j, has coefficients +1 and -sigma.
    for axes, signs in views:
        for j in (1, 2):
            yield axes[0], axes[j], signs[0]*signs[j]


def signature(views):
    adj = [[] for _ in AXES]
    for i, j, s in edges(views):
        adj[i].append((j, s))
        adj[j].append((i, s))
    phase = [0]*N
    balanced = unbalanced = 0
    for root in AXES:
        if phase[root]:
            continue
        phase[root] = 1
        todo = [root]
        consistent = True
        while todo:
            i = todo.pop()
            for j, sign in adj[i]:
                expected = phase[i]*sign
                if phase[j]:
                    consistent &= phase[j] == expected
                else:
                    phase[j] = expected
                    todo.append(j)
        if consistent:
            balanced += 1
        else:
            unbalanced += 1
    return balanced, unbalanced


def determinant(matrix):
    if not matrix:
        return 1
    if len(matrix) == 1:
        return matrix[0][0]
    return sum((-1)**i*v*determinant([row[:i]+row[i+1:] for row in matrix[1:]])
               for i, v in enumerate(matrix[0]) if v)


def minor_smith(views):
    matrix = []
    for i, j, sign in edges(views):
        row = [0]*N
        row[i], row[j] = -sign, 1
        matrix.append(row)
    last = 1
    factors = []
    for order in range(1, min(len(matrix), N)+1):
        divisor = 0
        for rows in combinations(matrix, order):
            for cols in combinations(AXES, order):
                sub = [[r[c] for c in cols] for r in rows]
                divisor = gcd(divisor, determinant(sub))
        if not divisor:
            break
        factors.append(divisor//last)
        last = divisor
    return factors


def circuit_tests():
    selected = [view((0,1,2)), view((2,3,4)), framed(IDENTITY, J, (0,4,5))]
    independent = [view((0,1,2)), view((0,1,2), (1,1,-1)),
                   view((3,4,5)), view((3,4,5), (1,1,-1))]
    disconnected = [view((0,1,2)), view((3,4,5))]
    z = (3, -2, 5, 7, -1, 4)
    results = {}
    for name, menu in [('three_fr_with_J123', selected), ('two_unbalanced', independent),
                       ('two_balanced', disconnected), ('no_views', [])]:
        b, u = signature(menu)
        smith = minor_smith(menu)
        assert smith == [1]*(N-b-u)+[2]*u
        probes = {}
        for q in (2, 3, 4, 5, 6):
            hist = Counter(contrasts(vals, menu, q) for vals in product(range(q), repeat=N))
            f = q**b*gcd(2,q)**u
            assert set(hist.values()) == {f}
            probes[str(q)] = {'distinct_reports': len(hist), 'states_per_report': f}
        results[name] = {'b': b, 'u': u, 'nonzero_smith_invariants': smith, 'modular': probes}
    z0 = (0,)*N
    diag = (1,)*N
    assert all(read(z0,view(t)) == read(diag,view(t)) for t in TRIADS)
    assert read(diag,selected[-1]) == (0,2,2)
    assert [read(z, v) for v in selected] == [(5,0,7),(6,8,0),(0,2,7)]
    for q in (2,4,6,8,10):
        assert contrasts(z0,selected,q) == contrasts((q//2,)*N,selected,q)
    return results, {'signed_chart_state':z, 'integer_readouts':[read(z,v) for v in selected],
                     'JD_axis_1_5_6':read(diag,selected[-1])}


def exact_designs():
    menus = [view(t,(1,)+s) for t in TRIADS for s in product((1,-1),repeat=2)]
    good = set()
    binary = set()
    support_shapes = Counter()
    for ids in combinations(range(len(menus)),3):
        vs = [menus[i] for i in ids]
        b, u = signature(vs)
        if b+u == 1:
            binary.add(ids)
        if (b,u) != (0,1):
            continue
        good.add(ids)
        supp = [set(t) for t,_ in vs]
        shape = tuple(sorted(len(a & b) for a,b in combinations(supp,2)))
        support_shapes[shape] += 1
    four = Counter()
    witness = None
    for i,j,k in sorted(good):
        for ell in range(k+1,len(menus)):
            if not all(triple in good for triple in ((i,j,ell),(i,k,ell),(j,k,ell))):
                continue
            views = [menus[h] for h in (i,j,k,ell)]
            degree = Counter(a for t,_ in views for a in t)
            assert set(degree.values()) == {2} and len(degree)==6
            multiplicity = max(len(set(a[0])&set(b[0])) for a,b in combinations(views,2))
            four['K4' if multiplicity==1 else 'opposite_doubles'] += 1
            if witness is None:
                witness = [{'axes_one_based':[i+1 for i in t],'signs':s} for t,s in views]
    assert len(good)==15360 and four=={'K4':960,'opposite_doubles':2880}
    assert support_shapes == {(0,1,2):5760,(1,1,2):5760,(1,1,1):3840}
    four_binary = sum(all(triple in binary for triple in ((i,j,ell),(i,k,ell),(j,k,ell)))
                      for i,j,k in binary for ell in range(k+1,len(menus)))
    assert (len(binary),four_binary) == (30720,19200)
    six = [view(tuple((i+j)%N for j in range(3)),(1,1,-1)) for i in AXES]
    assert all(signature(keep)==(0,1) for keep in combinations(six,4))
    # An impulse in any of six axes differs on exactly three of these six readouts.
    zero = (0,)*N
    for axis in AXES:
        impulse = tuple(int(i==axis) for i in AXES)
        assert sum(read(impulse,v)!=read(zero,v) for v in six)==3
    return {'binary_three_complete_with_formal_signs':len(binary),
            'binary_four_single_erasure_complete_with_formal_signs':four_binary,
            'cyclic_six_two_erasure_subsets_checked':15,'cyclic_six_min_distance':3,
            'normalized_views':len(menus), 'three_checked':82160, 'three_complete':len(good),
            'three_by_sorted_intersection_sizes':{str(k):v for k,v in sorted(support_shapes.items())},
            'single_erasure_complete_four':dict(sorted(four.items())),
            'single_erasure_total':sum(four.values()), 'single_erasure_witness':witness}


def source_action_checks():
    z = (0,2,-1,3,1,-2)
    count = 0
    safe = 0
    for p in permutations(AXES):
        if sum(p[i]>p[j] for i,j in combinations(AXES,2))%2:
            continue
        for eps in product((-1,1),repeat=N):
            gz = tuple(e*z[i] for e,i in zip(eps,p))
            t = TRIADS[count%len(TRIADS)]
            assert read(z,framed(p,eps,t)) == read(gz,view(t))
            count += 1
            safe += len(set(eps))==1
    assert (count,safe) == (23040,720)
    return {'frames':count,'whole_relative_uniform_sign':safe}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint-checker',type=Path,
                    help='Optionally verify and replay the pinned upstream checker from its original file.')
    args=ap.parse_args()
    if args.checkpoint_checker is not None:
        assert sha256(args.checkpoint_checker.read_bytes()).hexdigest()==CHECKER_HASH
        proc=subprocess.run([sys.executable,str(args.checkpoint_checker)],capture_output=True,text=True,check=True)
        assert proc.stdout.strip()=='frame-group 23040 observer-safe 720 unsafe 22320'
    finite, witness = circuit_tests()
    out={'finite_and_smith':finite,'source_example':witness,
         'designs':exact_designs(),'frame_action':source_action_checks(),
         'source_checker_sha256':CHECKER_HASH}
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
