#!/usr/bin/env python3
"""PREFIX-949 exact Q19 nonzero adjacent-core resonance census.

Two independently organized integer-only counters: direct odd-a scan and
periodic congruence-class floor counting. No earlier sorted W_k inputs.
"""
import json

L, U, STATE_N, MAX_BIT = 262145, 524287, 1 << 32, 18


def count_direct(m, v):
    k, ell, h = (1 << m)-1, (1 << m)+1, 1 << v
    high = min(U, (STATE_N-1)//ell)
    if L+h > high:
        return 0
    count = 0
    for a in range(L+h, high+1, 2):
        if not (k*a >> v & 1) and (ell*a >> (m+v) & 1):
            b = a-h
            assert L <= b <= U and b % 2 == 1
            # Actual two named XOR equalities, not only symbolic bit signs.
            assert ((k*a ^ (1 << v)) - (1 << (m+v))) == k*b
            assert ((ell*a ^ (1 << (m+v))) - (1 << v)) == ell*b
            count += 1
    return count


def count_residues(m, v):
    k, ell, h = (1 << m)-1, (1 << m)+1, 1 << v
    low, high = L+h, min(U, (STATE_N-1)//ell)
    if low > high:
        return 0
    period = 1 << (m+v+1)
    total = 0
    for residue in range(1, period, 2):
        if not (k*residue >> v & 1) and (ell*residue >> (m+v) & 1):
            total += (high-residue)//period - (low-1-residue)//period
    return total


def signed_term_spectrum(jmax):
    terms = {(1 << i) - s*(1 << j)
             for i in range(jmax+1) for j in range(jmax+1)
             for s in (-1, +1)}
    found = []
    for k in range(7, 200, 2):
        ell = k+2
        compatible = any(c and (ell*c) % k == 0 and (ell*c)//k in terms
                         for c in terms)
        if compatible:
            found.append(k)
    expected = [(1 << m)-1 for m in range(3, jmax+1) if (1 << m)-1 < 200]
    assert found == expected, (jmax, found, expected)
    return found


def run():
    rows = []
    assert signed_term_spectrum(MAX_BIT) == [7, 15, 31, 63, 127]
    for m in range(3, 15):
        by_v = {}
        for v in range(1, MAX_BIT-m+1):
            n1 = count_direct(m, v)
            n2 = count_residues(m, v)
            assert n1 == n2, (m, v, n1, n2)
            by_v[str(v)] = n1
        rows.append({"m": m, "k": (1 << m)-1, "next_core": (1 << m)+1,
                     "total_distinct_resonant_offdiag_pairs": sum(by_v.values()),
                     "by_v": by_v, "both_exact_counters_agree": True})
    assert [row["total_distinct_resonant_offdiag_pairs"] for row in rows] == [
        485798,456313,424864,392657,360193,327553,294784,
        262144,229376,196608,163760,0]
    result = {
        "schema": "PREFIX949_R6_SPARSE_RESONANCE_Q19_V1",
        "scientific_input_pin": "f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "domain": {"odd_moduli_inclusive": [L,U], "bit_indices_inclusive": [0,MAX_BIT],
                   "state_endpoint_upper_exclusive": STATE_N,
                   "adjacent_odd_core_m_inclusive": [3,14]},
        "method": "exact direct odd-a scan and independent residue-floor counter",
        "rows": rows, "all_assertions_passed": True,
        "formal_review": False, "admitted": False}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    run()
