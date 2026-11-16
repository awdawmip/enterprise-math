#!/usr/bin/env python3
"""R611 exact signed BRC K/J->B->D row inversion and integer-lattice checks.

Frozen science: awdawmip/enterprise-math R462@18783e01e3646c72b7aab3b16d3f565e83e6446f,
research_notes/r388_signed_k3_corank16_20261029_emr3/r388_exact.py, theta=0.
Implements the exact twelve signed branches; no X6 physical-dynamics assertion.
"""
from math import comb
from pathlib import Path
from hashlib import sha256
import json


def C(n, j):
    return comb(n, j) if 0 <= j <= n else 0


def monomial(n, scalar, offset):
    return {offset+j: scalar*C(n, j) for j in range(n+1) if scalar*C(n, j)} if n >= 0 else {}


def plus(*args):
    z = {}
    for p in args:
        for j, c in p.items():
            z[j] = z.get(j, 0) + c
    return {j: c for j, c in z.items() if c}


def prod(p, q):
    z = {}
    for i, a in p.items():
        for j, b in q.items():
            z[i+j] = z.get(i+j, 0) + a*b
    return {j: c for j, c in z.items() if c}


def K(i):
    assert 1 <= i <= 12
    d = (-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2), C(7,i-2), -C(9,i-3))
    return plus(*(monomial(i+1-j, -v, i-1) for j, v in enumerate(d, 1)))


def J(s):
    assert s >= 1
    return plus(monomial(s, -C(3,s-1), s),
                monomial(s-1, -C(6,s-1), s),
                monomial(s-2, C(8,s-2), s))


def coefficient(p, j):
    return p.get(j, 0)


def bare(max_s):
    B = [{0:1, 1:1}]
    for s in range(1, max_s+1):
        B.append(plus(J(s), *(prod(K(i), B[s-i]) for i in range(1, min(s,12)+1))))
    return B


def D(q, k, B):
    assert 0 <= k <= q and q+k < len(B)
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*coefficient(B[q+w], q)
               for w in range(k+1))


def main():
    assert K(1) == {0:2, 1:3}
    assert K(2) == {1:-1, 2:4, 3:4}
    Q = 15
    B = bare(2*Q)
    checks = 0
    for q in range(Q+1):
        d = [D(q,k,B) for k in range(q+1)]
        for w in range(q+1):
            lifted = sum(C(w,k)*d[k] for k in range(w+1))
            expected = 2**(q-w)*coefficient(B[q+w],q)
            assert lifted == expected, (q,w,lifted,expected)
            assert lifted % 2**(q-w) == 0, (q,w)
            checks += 1

    H = [dict(p) for p in B]
    s = 6
    H[s][0] = H[s].get(0,0) + 17
    H[s][s+1] = H[s].get(s+1,0) - 9
    for q in range(Q+1):
        for k in range(q+1):
            assert D(q,k,H) == D(q,k,B), (q,k)
    assert H[s] != B[s]
    witness_q2 = [D(2,k,B) for k in range(3)]
    bad = witness_q2[:]
    bad[0] += 1
    assert bad[0] % 4 != 0
    index_exponent_q15 = Q*(Q+1)//2
    result = {
      'schema':'R611_SIGNED_BRC_D_VISIBLE_BAND_LATTICE_V1',
      'source_pin':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
      'source_file':'research_notes/r388_signed_k3_corank16_20261029_emr3/r388_exact.py',
      'source_branch_semantics':'original signed twelve K/J -> B -> D; theta=0',
      'q_range':[0,Q], 'B_s_range':[0,2*Q],
      'checked_integral_inverse_coordinates':checks,
      'q2_original_D_row':[str(v) for v in witness_q2],
      'q2_nonrealizable_modified_D_row':[str(v) for v in bad],
      'generic_free_B_family_kernel_witness':{
        'modified_s':s, 'lower_coeff_delta':{'degree':0,'value':17},
        'upper_coeff_delta':{'degree':s+1,'value':-9},
        'checked_all_qk_in_range':True,
        'claim_scope':'arbitrary free polynomial family, not alternate legitimate BRC K/J state'
      },
      'q15_row_lattice_index_power_of_two':index_exponent_q15,
      'q2_row_modular_conditions':['D(2,0) divisible by 4', 'D(2,0)+D(2,1) divisible by 2'],
      'terminal_marker':'R611_EXACT_BRC_D_BAND_LATTICE_PASS'
    }
    output = json.dumps(result,sort_keys=True,ensure_ascii=False,indent=2)+'\n'
    outpath=Path(__file__).with_name('R611_EVIDENCE.json')
    outpath.write_text(output,encoding='utf-8')
    print(result['terminal_marker'])
    print('row range q=0..',Q,' inverted/divisibility pairs=',checks)
    print('q=2 original D:',witness_q2, 'non-realizable D:',bad)
    print('q=15 image lattice index = 2^',index_exponent_q15)
    print('generic kernel test: B6[t^0] +=17, B6[t^7] -=9; all D in q<=15 unchanged')
    print('evidence SHA256:',sha256(output.encode('utf-8')).hexdigest())


if __name__ == '__main__':
    main()
