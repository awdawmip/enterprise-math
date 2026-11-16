#!/usr/bin/env python3
"""R613: full-aggregate original signed BRC D(q,0) initial-response certificate.
Frozen scientific input: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f,
research_notes/r388_signed_k3_corank16_20261029_emr3/r388_exact.py, theta=0.
No isolated history selections; all twelve original signed K_i and original J_s.
"""
from math import comb
from itertools import product
from hashlib import sha256
from pathlib import Path
import json

N = 12

def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def add(p, q):
    z = [0] * max(len(p), len(q))
    for j, a in enumerate(p): z[j] += a
    for j, a in enumerate(q): z[j] += a
    return tuple(z)

def mul(p, q):
    z = [0] * (len(p) + len(q) - 1)
    for j, a in enumerate(p):
        for k, b in enumerate(q): z[j + k] += a * b
    return tuple(z)

def mono(n, value, shift):
    return tuple([0] * shift + [value * C(n, j) for j in range(n + 1)]) if n >= 0 else (0,)

def K(i):
    ds = (-C(4, i) + C(2, i-1), C(5, i-1) - C(5, i-2),
          C(7, i-2), -C(9, i-3))
    out = (0,)
    for j, a in enumerate(ds, 1):
        if a: out = add(out, mono(i+1-j, -a, i-1))
    return out

def J(s):
    out = (0,)
    for a, n in ((-C(3, s-1), s), (-C(6, s-1), s-1), (C(8, s-2), s-2)):
        if a: out = add(out, mono(n, a, s))
    return out

def coeff(p, j):
    return p[j] if 0 <= j < len(p) else 0

def convolution_state(input_poly, kernels, forced=True):
    result = [tuple(input_poly)]
    for s in range(1, N + 1):
        b = J(s) if forced else (0,)
        for i in range(1, min(s, 12) + 1): b = add(b, mul(kernels[i-1], result[s-i]))
        result.append(b)
    return result

def d0(seq, q):
    return (2**q) * coeff(seq[q], q)

def main():
    kernels = [K(i) for i in range(1, 13)]
    assert kernels[0] == (2, 3)
    assert kernels[1] == (0, -1, 4, 4)
    assert all(coeff(kernels[i], 0) == 0 for i in range(1, 12))
    assert coeff(kernels[2], 2) == -8  # frozen theta=0
    R = convolution_state((1,), kernels, forced=False)
    assert [coeff(x, 0) for x in R] == [2**q for q in range(N+1)]
    base = convolution_state((1, 1), kernels, forced=True)
    D02 = [d0(base, q) for q in range(5)]
    assert D02[:3] == [1, 6, 32], D02
    # Response matrix M_{qj} = D(q,0; B0=t^j)-D(q,0; B0=0).
    M = [[2**q * coeff(R[q], q-j) if j <= q else 0
          for j in range(N+1)] for q in range(N+1)]
    assert all(M[q][q] == 4**q for q in range(N+1))
    assert all(M[q][j] == 0 for q in range(N+1) for j in range(q+1, N+1))
    assert sum(q*2 for q in range(N+1)) == N*(N+1)
    assert [M[q][:q+1] for q in range(3)] == [[1], [6,4], [52,44,16]]
    sample = (1,-2,3)
    sample_response = [sum(M[q][j]*sample[j] for j in range(q+1)) for q in range(3)]
    assert sample_response == [1,-2,12]
    assert (-1 - 6*1) % 4 != 0  # false candidate y=(1,-1,12) at q=1
    # Exhaustive test: all degree <= 4 integer inputs with coefficients -1,0,1.
    checked = 0
    for vec in product((-1, 0, 1), repeat=5):
        p = tuple(vec)
        variant = convolution_state(add((1, 1), p), kernels, forced=True)
        delta = [d0(variant, q) - d0(base, q) for q in range(N+1)]
        predicted = [sum(M[q][j] * p[j] for j in range(5)) for q in range(N+1)]
        assert delta == predicted
        recovered = []
        for q in range(5):
            numerator = delta[q] - sum(M[q][j]*recovered[j] for j in range(q))
            assert numerator % 4**q == 0
            recovered.append(numerator // 4**q)
        assert tuple(recovered) == p
        if any(p):
            first = next(j for j, v in enumerate(p) if v)
            assert all(delta[q] == 0 for q in range(first))
            assert delta[first] == 4**first * p[first]
        checked += 1
    # Finite-horizon kernel: t^(d+1) is invisible through q=d, visible at q=d+1.
    for d in range(N):
        p = (0,)*(d+1) + (1,)
        variant = convolution_state(add((1,1), p), kernels, forced=True)
        delta = [d0(variant, q)-d0(base,q) for q in range(d+2)]
        assert delta[:d+1] == [0]*(d+1)
        assert delta[d+1] == 4**(d+1)
    record = {
      'schema': 'R613_SIGNED_BRC_WHOLE_AGGREGATE_D0_LATTICE_V1',
      'scientific_pin': 'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
      'input': 'all 12 original signed K_i; original J_s; theta=0; varying B0 in Z[t]',
      'N': N, 'K1': list(kernels[0]), 'K2': list(kernels[1]),
      'response_constant_terms': [coeff(x,0) for x in R],
      'd0_baseline_first_five': D02,
      'diagonal_M_0_to_N': [M[q][q] for q in range(N+1)],
      'M_first_three_rows': [M[q][:q+1] for q in range(3)],
      'example_input_p0_2': list(sample),
      'example_delta_D0_2': sample_response,
      'integer_image_exclusion_prefix': [1,-1,12],
      'index_for_horizon_N': str(2**(N*(N+1))),
      'exhaustive_degree4_inputs_coefficients_minus1_0_1': checked,
      'finite_horizon_kernel_checks': N,
      'arithmetic_semantics': 'Python arbitrary precision integers; exact exhaustive declared input grid',
      'claim_scope': 'whole aggregate deterministic signed K/J->B->D polynomial recurrence, varying B0; fixed R462 initial B0 remains (1+t)',
      'terminal_marker': 'R613_EXACT_WHOLE_STATE_D0_OBSERVER_PASS'
    }
    content = json.dumps(record, sort_keys=True, ensure_ascii=False, indent=2)+'\n'
    pth=Path(__file__).with_name('R613_EVIDENCE.json')
    pth.write_text(content, encoding='utf-8')
    print(record['terminal_marker'])
    print('input_grid',checked,'kernel_checks',N,'index',record['index_for_horizon_N'])
    print('evidence_sha256',sha256(content.encode()).hexdigest())

if __name__ == '__main__': main()
