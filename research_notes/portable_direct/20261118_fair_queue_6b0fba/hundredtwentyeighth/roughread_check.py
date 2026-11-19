"""Exact arithmetic for the squarefree cosine readout. Requires python-flint."""
import hashlib
import importlib.util
import json
from fractions import Fraction
from itertools import combinations
from math import gcd
from pathlib import Path

from flint import fmpz_mat, fmpz_poly

X = fmpz_poly([0, 1])


def native_source():
    path = Path(__file__).resolve().parents[1] / "hundredeighth" / "rough_check.py"
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest == SOURCE_SHA
    spec = importlib.util.spec_from_file_location("original_rough", path)
    src = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(src)
    return src


def factors(k):
    primes = []
    d = 2
    while d*d <= k:
        if k % d == 0:
            primes.append(d)
            while k % d == 0:
                k //= d
        d += 1
    if k > 1:
        primes.append(k)
    return primes


def phi(k):
    result = k
    for p in factors(k):
        result = result // p * (p-1)
    return result


def unit_columns(T):
    # Integer cyclotomic coordinates of 2cos(n*pi/(2T)); the native complex
    # power basis contains the real order as a direct summand.
    cyclo = fmpz_poly.cyclotomic(4*T)
    powers = [(X**i - X**(2*T-i)) % cyclo for i in range(T)]
    odds = list(range(1, T, 2))
    return [powers[i] + (powers[2*i] if 2*i < T else 0) for i in odds]


def matrix(cols, degree):
    return fmpz_mat([[int(col[i]) for col in cols] for i in range(degree)])


def smith(T, squarefree_only=False):
    cols = unit_columns(T)
    if squarefree_only:
        cols = [v for j, v in enumerate(cols) if all((2*j+1) % (p*p) for p in factors(2*j+1))]
    diag = matrix(cols, phi(4*T)).snf()
    invariants = [int(diag[i, i]) for i in range(min(diag.nrows(), diag.ncols())) if diag[i, i]]
    if not squarefree_only:
        assert invariants == [1] * min((T-1)//2, phi(T))
    return [T, len(cols), len(invariants), sorted(set(invariants))]


def quarter_certificate(P, B):
    # Each block uses the first d samples of a recurrence with polynomial D.
    D = (X**P-1) // fmpz_poly.cyclotomic(P)
    d = D.degree()
    zero = [0] * d
    w = fmpz_poly([1])
    rows = []
    for j in range(P):
        h = [int(w[i]) for i in range(d)]
        angle = 8*(B*j+1)
        k = P*B
        if angle in (k,3*k,5*k,7*k):
            row = zero+zero+h
        elif angle < k or angle > 7*k:
            row = [-i for i in h]+zero+h
        elif angle < 3*k:
            row = zero+[-i for i in h]+h
        elif angle < 5*k:
            row = h+zero+h
        else:
            row = zero+h+h
        rows.append(row)
        w = (X*w) % D
    # Compute a literal integral combination of the original rows giving 2*A[0].
    H, U = fmpz_mat(rows).hnf(transform=True)
    rem = [Fraction(2)] + [Fraction(0)] * (3*d-1)
    combination = [0] * P
    rank = 0
    for i, row0 in enumerate(H.tolist()):
        row = list(map(int, row0))
        pivot = next((k for k,v in enumerate(row) if v), None)
        if pivot is None:
            continue
        rank += 1
        coeff = rem[pivot] / row[pivot]
        assert coeff.denominator == 1
        rem = [v - coeff*r for v, r in zip(rem, row)]
        for j in range(P):
            combination[j] += int(coeff)*int(U[i,j])
    assert not any(rem)
    assert [sum(combination[j]*rows[j][i] for j in range(P)) for i in range(3*d)] == [2]+[0]*(3*d-1)
    return dict(P=P, B=B, degree=d, rank=rank, combination=combination)


def real_prefix_checks(src, T, y, skip):
    window = [p for p in src.primes_until(T) if p > y and p not in skip]
    buckets, _ = src.source_events(T, y, window)
    mod = fmpz_poly.cyclotomic(4*T)
    raw = fmpz_poly()
    weights = [0] * T
    contents = []
    decoded = 0
    cols = unit_columns(T)
    deg = mod.degree()
    if T % 2 and phi(T) >= (T-1)//2:
        # Exact row operations construct an integral left inverse independent of the input.
        H,U = matrix(cols, deg).hnf(transform=True)
        n = len(cols)
        assert all(H[i,j] == (i==j) for i in range(n) for j in range(n))
        inverse = fmpz_mat(U.tolist()[:n])
    for p in [1]+window:
        for n, sign in buckets[p]:
            weights[n] = sign
            raw += sign*(X**n-X**(2*T-n))
        reduced = raw % mod
        content = abs(int(reduced.content()))
        contents.append(content)
        assert content > 0
        assert reduced == sum((v*weights[2*j+1] for j,v in enumerate(cols)), fmpz_poly())
        if T % 2 and phi(T) >= (T-1)//2:
            values = inverse * fmpz_mat([[int(reduced[i])] for i in range(deg)])
            assert [int(values[i,0]) for i in range(n_odd(T))] == weights[1::2]
            decoded += n_odd(T)
            assert content == 1
    return dict(T=T, y=y, skipped=sorted(skip), prefixes=len(contents), contents=sorted(set(contents)),
                decoded_odd_labels=decoded)


def n_odd(T):
    return T//2


def first_squarefree_kernel():
    exceptions = [T for T in range(3,316,2) if (T-1)//2 > phi(T)]
    assert exceptions == [105,165,195,315]
    T = 315
    labels = [s for s in range(1,T,2) if all(s % (p*p) for p in factors(s))]
    cols = unit_columns(T)
    M = matrix([cols[(s-1)//2] for s in labels], phi(4*T))
    N,n = M.nullspace()
    assert n == 1
    v = [int(N[i,0]) for i in range(len(labels))]
    g = gcd(*v) * (-1 if v[0] > 0 else 1)
    v = [i//g for i in v]
    assert v[0] == -7 and max(map(abs,v)) == 32 and v[labels.index(199)] == 32
    assert (M*fmpz_mat([[i] for i in v])).is_zero()
    sub = matrix([cols[(s-1)//2] for s in labels[1:]], phi(4*T)).snf()
    values = [int(sub[i,i]) for i in range(len(labels)-1)]
    assert values == [1]*127+[14]
    return dict(exceptions=exceptions, relation=[[s,i] for s,i in zip(labels,v) if i],
                anchored_tail_last_invariant=14)


def mixed_square_witness(T, primes, external):
    q = 4*T
    assert set(factors(T)) - {2} == set(primes)
    M = 1
    steps = []
    for p, ell in zip(primes, external):
        s = q//p
        assert q % ell and M % ell
        # Earliest external divisor in any nonempty subset wins.
        b = M * ((-pow(s*M,-1,ell**2)) % ell**2)
        M *= ell**2
        if b > M//2:
            b -= M
        steps.append(b*s)
    rows = []
    for size in range(1, len(steps)+1):
        for ids in combinations(range(len(steps)), size):
            r = 1 + sum(steps[i] for i in ids)
            ell = external[ids[0]]
            assert abs(r) <= T and r % (ell*ell) == 0
            rows.append([r,ell])
    return dict(T=T, odd_primes=primes, steps=steps, forced_zeros=rows)


def main():
    src = native_source()
    odd_tests = [smith(T) for T in [*range(3,76,2), 85, 105, 115, 165, 195, 231]]
    source_cases = [real_prefix_checks(src,t,y,skip) for t,y,skip in
                    [(15,2,{7}), (45,3,{7,11}), (77,2,{5,13}), (105,3,{5,13}),
                     (70,2,{7}), (110,3,{7,13}), (130,2,{7}), (140,3,{7,17}),
                     (154,3,{7}), (210,2,{11,13})]]
    crt = [mixed_square_witness(2*467*479,[467,479],[3,5]),
           mixed_square_witness(2*1009*1013*100003,[1009,1013,100003],[3,5,7])]
    fold = []
    for a in [21,22,81,82]:
        w = 2**a
        r = 1 if a % 60 == 21 else 2
        freq = [10*w+r,12*w+r,8*w-r]
        assert [v % d for v,d in zip(freq,[9,25,9])] == [0,0,0]
        fold.append(dict(T=15*w, r=r, frequencies=freq))
    return {"source_sha256":SOURCE_SHA, "smith_T_columns_rank_factors":odd_tests,
            "squarefree_restricted_examples":[smith(T,True) for T in (105,165,195,231,315)],
            "first_kernel":first_squarefree_kernel(),
            "actual_prefixes":source_cases, "quarter_row_combinations":[quarter_certificate(P,B)
                   for P in (35,55,65) for B in (8,16)], "crt_cubes":crt, "folded_examples":fold}


SOURCE_SHA = "a7736400305d6c3edecae4be0119ce9758ec7f2c08762fcb908357b5d0de2172"
if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
