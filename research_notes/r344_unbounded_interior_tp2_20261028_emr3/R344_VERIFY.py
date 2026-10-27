#!/usr/bin/env python3
"""R344 exact certificate for infinitely long BRC Newton interior TP2 corank strips.

Default: consume the faithful full exact R331 Newton-coefficient JSON.
Alternative --rebuild: reconstruct that input from the original signed 12-term
K/J BRC recurrence (slow, intended for independent full reproducibility).
No floating point; all arithmetic is Python int or Fraction.

Dependency: R330 rational extraction identity proving deg(H_r)<=r and
D_{r+u,u}=5^u H_r(u). This script does not independently prove that identity.
"""
import argparse
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path

EXPECTED_R331_SHA = '81c190fa50e22dc8479cb337a374706ae300a877fc9c74aa7a9033c49d96cf09'


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def add(a, b):
    z = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        z[i] += v
    for i, v in enumerate(b):
        z[i] += v
    return z


def mul(a, b):
    z = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        if v:
            for j, w in enumerate(b):
                if w:
                    z[i + j] += v * w
    return z


def monomial(n, coefficient, shift):
    return [0] * shift + [coefficient * binom(n, j) for j in range(n + 1)]


def K(i):
    d = (-binom(4, i) + binom(2, i-1),
         binom(5, i-1) - binom(5, i-2),
         binom(7, i-2), -binom(9, i-3))
    out = [0]
    for j, v in enumerate(d, 1):
        if v:
            out = add(out, monomial(i + 1 - j, -v, i - 1))
    return out


def J(s):
    out = [0]
    for v, n in ((-binom(3, s-1), s),
                 (-binom(6, s-1), s-1),
                 (binom(8, s-2), s-2)):
        if v:
            out = add(out, monomial(n, v, s))
    return out


def rebuild_newton(max_r):
    # Max H index is max_r+1. Its interpolation uses s<=3*(max_r+1).
    rmax = max_r + 1
    B = [[1, 1]]
    kernels = [None] + [K(i) for i in range(1, 13)]
    for s in range(1, 3*rmax + 1):
        row = J(s)
        for i in range(1, min(12, s) + 1):
            row = add(row, mul(kernels[i], B[s-i]))
        B.append(row)
    cases = []
    for r in range(rmax + 1):
        values = []
        for u in range(r + 1):
            q = r + u
            D = sum((-1)**(u-v) * binom(u, v) * 2**(q-v) * B[q+v][q]
                    for v in range(u+1))
            values.append(Fraction(D, 5**u))
        coefficients = []
        while values:
            coefficients.append(values[0])
            values = [values[j+1] - values[j] for j in range(len(values)-1)]
        cases.append(coefficients)
    return cases


def load_newton(file):
    source = json.loads(Path(file).read_text(encoding='utf-8'))
    cases = source['cases']
    assert all(c['r'] == i for i, c in enumerate(cases)), 'r case ordering incomplete'
    return [[Fraction(v) for v in c['newton_coefficients']] for c in cases]


def reconstruct_values(forward_coeffs, count):
    # Δ^j L(0) coefficients become L(n), by Δ^j L(n+1)=Δ^j L(n)+Δ^{j+1} L(n).
    diffs = forward_coeffs.copy()
    out = []
    for _ in range(count):
        out.append(diffs[0])
        for j in range(len(diffs)-1):
            diffs[j] += diffs[j+1]
    return out


def cert(cases, max_r=255):
    assert max_r >= 1
    assert len(cases) >= max_r + 2
    signed = hashlib.sha256()
    for r, row in enumerate(cases):
        assert len(row) == r + 1
        assert row[-1] == 6**r, ('top H coefficient mismatch', r)
        for k, v in enumerate(row):
            assert v > 0, ('R331 input contains nonpositive coefficient', r, k)
            signed.update(f'{r},{k},{v.numerator}/{v.denominator}\n'.encode())
    # Input must be the complete R331 0..256 exact coefficient sequence, not a forged fragment.
    assert len(cases) == 257, ('full R331 input expected', len(cases))
    input_sha = signed.hexdigest()
    assert input_sha == EXPECTED_R331_SHA, ('full R331 digest mismatch', input_sha)

    count = 2*max_r + 4
    rows = []
    for r, row in enumerate(cases):
        L = [t * 5**r for t in row]
        assert all(x.denominator == 1 for x in L), ('nonintegral 5^r H Newton coefficient', r)
        rows.append(reconstruct_values([int(x) for x in L], count))

    digest = hashlib.sha256()
    r_digests = []
    total = 0
    samples = {}
    for r in range(1, max_r + 1):
        # Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1)
        # Degree<=2*r follows from the R330 H polynomial degree bounds.
        values = [rows[r][v+1]*rows[r][v+2]
                  - rows[r-1][v+2]*rows[r+1][v+1]
                  for v in range(2*r+1)]
        d = values.copy()
        inner_sha = hashlib.sha256()
        first = None
        for i in range(2*r+1):
            z = d[0]
            assert z > 0, ('R344 Q forward coeff nonpositive', r, i, z)
            if first is None:
                first = z
            s = f'{r},{i},{z}\n'.encode()
            digest.update(s)
            inner_sha.update(s)
            d = [d[j+1]-d[j] for j in range(len(d)-1)]
            total += 1
        # Exact leading coefficient: Δ^{2r} Q = 30^{2r} Catalan(r).
        cat = comb(2*r, r)//(r+1)
        assert z == 30**(2*r) * cat, ('top Q Catalan identity', r)
        r_digests.append({'r': r, 'positive_count': 2*r+1, 'sha256': inner_sha.hexdigest()})
        if r in (1, 2, 3, 4, 5, 17, 64, 128, 255):
            samples[str(r)] = {'Q_r_0': str(first), 'delta_2r_Q_r_0': str(z)}
    assert total == max_r * (max_r + 2)
    return {
        'schema': 'ENTERPRISE_MATH_R344_INTERIOR_TP2_UNBOUNDED_CORANK_V1',
        'result': 'EXACT_FINITE_COEFFICIENT_CERTIFICATE_PASS',
        'mathematical_scope': 'BRC signed 12-term auxiliary model, not native X6 dynamics',
        'inherited_required_lemma': 'R330 exact rational extraction D_{r+u,u}=5^u H_r(u), deg H_r<=r',
        'source': 'R331 full 0..256 rational Newton coefficients; R331 source reconstruction available',
        'input_newton_sha256': input_sha,
        'r_interval': [1, max_r],
        'k_condition': 'k>=1, q=r+k, 1<=r<=255',
        'exact_positive_newton_coefficients_for_shifted_minor': total,
        'sha256_lines_r_i_Qdelta_decimal_newline': digest.hexdigest(),
        'each_r_sha256': r_digests,
        'samples': samples,
        'independent_top_coefficient_check': 'Delta^(2r) Q_r(0) = 30^(2r) Catalan(r) for every 1<=r<=max_r',
        'nonadjacent_corollary': 'D[q,k]D[p,l]-D[q,l]D[p,k]>0 for all 1<=k<l<=q<p and p-k<=256',
        'input_arithmetic': 'exact Fraction; Q and deltas exact integer',
        'claims_not_made': ['Global unbounded interior TP2', 'all r>=1', 'independent R330 degree lemma review', 'native Source acceptance', 'X6 dynamics transfer'],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='full R331_INTERPOLATION_EVIDENCE_256.json')
    parser.add_argument('--rebuild', action='store_true', help='independently recompute full input from signed K/J recurrence')
    parser.add_argument('--max-r', type=int, default=255)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    if not args.rebuild and not args.input:
        parser.error('specify --input FILE or --rebuild')
    data = rebuild_newton(args.max_r) if args.rebuild else load_newton(args.input)
    out = cert(data, args.max_r)
    Path(args.out).write_text(json.dumps(out, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print('PASS', out['r_interval'], out['exact_positive_newton_coefficients_for_shifted_minor'], out['sha256_lines_r_i_Qdelta_decimal_newline'], flush=True)


if __name__=='__main__':
    main()
