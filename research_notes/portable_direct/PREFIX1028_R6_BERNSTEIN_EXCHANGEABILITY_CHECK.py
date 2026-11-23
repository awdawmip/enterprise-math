#!/usr/bin/env python3
"""PREFIX-1028: exact Stage46 BRC/Laurent contrast, zero-index extension
and finite coherent Bernstein distributions. Only the frozen published
integer A6 recurrence and exact signed-port contrast are used.
No native-update, physical-residual, pi or trigonometric computation.
"""
import hashlib
import json
import math
import sys
from fractions import Fraction


def collisions(n):
    A = [1, 6, 66]
    for r in range(2, n + 3):
        numerator = (2*(2*r+1)*(14*r**4+28*r**3+28*r**2+14*r+3)*A[r]
            -4*r**3*(196*r**2+59)*A[r-1]
            +1152*(2*r-1)*r*r*(r-1)**2*A[r-2])
        denominator = (r+1)**5
        assert numerator % denominator == 0
        A.append(numerator // denominator)
    assert A[:8] == [1,6,66,996,18306,384156,8848236,218040696]
    return A


def mass_difference(m, A):
    value = (Fraction(-72*(72*m*m+163*m+80), 5*(m+1))*A[m+1]
       + Fraction(2*(144*m**3+1135*m*m+2367*m+1310),5*(m+1)*(m+2))*A[m+2]
       - Fraction(2*(m+8)*(2*m+5),5*(m+2))*A[m+3])
    assert value.denominator == 1
    return value.numerator


def falling(m, d):
    x = 1
    for j in range(d):
        x *= m-j
    return x


def audit(N=1200):
    A = collisions(N)
    a = [mass_difference(m,A) for m in range(N+1)]
    assert a[0] == 2412
    assert a[1:10] == [25620,386028,7124592,149251656,3398043852,
                        81969197100,2063490736128,53703289713528,
                        1436011181064216]
    baselines = {"240": "ba12049d9510eabf3abef8326249de88d7edcfdf88f1d990d2539a51bae8afc8",
        "1200": "b626fc2e4e12db5ce219ab6f5e69f0c0344f38d6fe63d189a768a935d888439e"}
    selected = sorted(set([0,1,2,10,100,240,N]))
    diagonal = {n:{} for n in selected}
    stream_all = hashlib.sha256()
    stream_original = hashlib.sha256()
    row = a[:]
    for k in range(N+1):
        assert all(v > 0 for v in row), k
        for m,v in enumerate(row):
            stream_all.update(f"{m},{k},{v}\n".encode('ascii'))
            if m>=1:
                stream_original.update(f"{m},{k},{v}\n".encode('ascii'))
            s=m+k
            if s in diagonal:
                diagonal[s][m] = v
        row = [36*row[i]-row[i+1] for i in range(len(row)-1)]
    full_hash = stream_all.hexdigest()
    old_hash = stream_original.hexdigest()
    if str(N) in baselines:
        assert old_hash == baselines[str(N)]
    checks = {}
    for n, data in diagonal.items():
        assert len(data) == n+1
        w = [math.comb(n,m)*data[m] for m in range(n+1)]
        assert sum(w) == a[0]*36**n

        for d in range(min(n,3)+1):
            observed = sum(w[m]*falling(m,d) for m in range(n+1))
            expected = falling(n,d)*a[d]*36**(n-d)
            assert observed == expected, (n,d)
        checks[str(n)]={"normalization":"PASS", "factorial_moments_d_0_to_3":"PASS"}

    return {
        "schema":"PREFIX1028_R6_ZERO_INDEX_BERNSTEIN_CERT_V1",
        "scientific_pin":"awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json",
        "observer":"Stage46 candidate signed BRC W=J12-6I, frozen X6 Cell-port-grade joint mass, Link {0,e1}, exactly one negative outgoing step",
        "N":N,
        "strictly_positive_pairs_m_ge_0":(N+1)*(N+2)//2,
        "new_zero_row_pairs":N+1,
        "a_0":str(a[0]),
        "original_m_ge_1_witness_sha256":old_hash,
        "new_m_ge_0_witness_sha256":full_hash,
        "stream_format":"ASCII m,k,E\\n; ascending k then ascending m; 0<=m, 0<=k, m+k<=N",
        "finite_exchangeable_distribution_p_N_m":"binom(N,m)*E(m,N-m)/(2412*36^N)",
        "moment_bound":"0<=integral(y^d d sigma_N)-a_d<=2412*36^d*d*(d-1)/(2N), 0<=d<=N, N>0",
        "selected_invariant_checks":checks,
        "mathematical_status":"FINITE_EXACT_INTEGER_CHECKED; SYMBOLIC_IDENTITY_AUTHOR_PROOF; NOT_REVIEWED"
    }

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv)>1 else 1200
    cert = audit(N)
    print('PASS', cert['strictly_positive_pairs_m_ge_0'], cert['new_m_ge_0_witness_sha256'])
    if len(sys.argv)>2:
        with open(sys.argv[2],'w',encoding='utf8') as f:
            json.dump(cert,f,ensure_ascii=False,indent=2)
            f.write('\n')
