#!/usr/bin/env python3
"""R762CB finite verifier: the 729 coherent conditional C3 sign-gates.
Original sign, named-Port, Link and branch histories remain typed; this checks
only aggregate based-return counts and terminal signed holonomy in the model.
"""
from itertools import product, permutations
from collections import Counter, defaultdict
from math import factorial
import json

BASE=(0,1,2)
AXES=range(6)
H=(None,0,3)             # excluded; closed with 0 or 3 enabled Ports
M=(None,0,1,2,3,4,5,6,7) # excluded; closed with 3-bit enabled Port mask

def popcount(m): return m.bit_count()

def histogram(h1,h2,m1,m2):
    n=[0,0,0,0]
    for k in (h1,h2):
        if k is not None: n[k]+=1
    for mask in (m1,m2):
        if mask is not None: n[popcount(mask)]+=3
    return tuple(n)

def b(k,m):
    if k==0: return int(m==0)
    if k==1: numerator=3**m+3*(-1)**m; denominator=4
    elif k==2: numerator=6**m+4+5*(-2)**m; denominator=10
    elif k==3: numerator=9**m+5*3**m+9*(-1)**m+5*(-3)**m; denominator=20
    else: raise ValueError(k)
    assert numerator%denominator==0
    return numerator//denominator

def exact_dynamic_counts(k, max_m=8):
    dp={BASE:1}; counts=[]
    for m in range(max_m+1):
        counts.append(sum(count for frame,count in dp.items() if set(frame)==set(BASE)))
        nxt=defaultdict(int)
        for frame,count in dp.items():
            outside=set(AXES)-set(frame)
            for port in range(k):
                for entering in outside:
                    new=frame[:port]+(entering,)+frame[port+1:]
                    nxt[new]+=count
        dp=nxt
    return counts

for k in range(4):
    observed=exact_dynamic_counts(k)
    assert observed==[b(k,m) for m in range(len(observed))],(k,observed)

laws=Counter(histogram(*x) for x in product(H,H,M,M))
assert sum(laws.values())==729
assert len(laws)==90

def value(n,m): return sum(n[k]*b(k,m) for k in range(4))

def rank_det(matrix):
    # exact 4x4 Leibniz determinant
    total=0
    for p in permutations(range(4)):
        inversions=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        a=(-1)**inversions
        for i in range(4): a*=matrix[i][p[i]]
        total+=a
    return total

matrix=[[b(k,m) for k in range(4)] for m in (0,2,3,4)]
assert matrix==[[1,1,1,1],[0,3,6,9],[0,6,18,36],[0,21,138,369]]
assert rank_det(matrix)==324
signature={(value(n,0),value(n,4)): n for n in laws}
assert len(signature)==len(laws)==90
# Proves identification from exactly two fixed-length count probes (0,4).
assert len({value(n,0) for n in laws})==9
assert len({value(n,4) for n in laws})==30
assert tuple(value((1,3,3,1),m) for m in range(9)) == (8,0,36,108,846,5418,41580,324576,2664810)

# All-length terminal-signature observer, NOT complete event history.
repair_counts=Counter()
repair_bits=Counter()
for n,weight in laws.items():
    signatures=sum(n[k]*factorial(k) for k in range(4))
    repair_counts[signatures]+=weight
    bits=0 if signatures<=1 else (signatures-1).bit_length()
    repair_bits[bits]+=weight
assert min(repair_counts)==0 and max(repair_counts)==48
assert repair_counts[0]==1 and repair_counts[48]==1
assert dict(sorted(repair_bits.items()))=={0:3,1:1,2:24,3:100,4:357,5:221,6:23}
assert sum(n*(n-1)//2 for n in laws.values())==5013
assert Counter(laws.values())==Counter({1:9,2:18,4:9,6:18,9:6,12:18,18:9,36:3})

out={
    "schema":"R762CB_CONDITIONAL_RETURN_SPECTRA_V1",
    "model":"X6 signed ordered three-Port, sign-only C3-covariant coherent closure/gate",
    "source_dependency":"R762CA@7530269499c7f799e65cb20b50a0f5c698b4b1c7; R762BY/R762BV based-return laws",
    "coherent_policies":sum(laws.values()),
    "distinct_return_spectra":len(laws),
    "class_size_distribution":dict(sorted(Counter(laws.values()).items())),
    "same_spectrum_unordered_policy_pairs":5013,
    "return_count_matrix_m_0_2_3_4":matrix,
    "return_count_matrix_determinant":rank_det(matrix),
    "single_probe_distinct_counts_m0":9,
    "single_probe_distinct_counts_m4":30,
    "two_probe_m0_m4_distinct_signatures":len(signature),
    "sign_positive_gate_return_count_m0_to_8":[value((1,3,3,1),m) for m in range(9)],
    "terminal_signature_min":min(repair_counts),
    "terminal_signature_max":max(repair_counts),
    "terminal_repair_bit_distribution":dict(sorted(repair_bits.items())),
    "closed_form":"N(m)=n0*[m=0]+n1*(3^m+3*(-1)^m)/4+n2*(6^m+4+5*(-2)^m)/10+n3*(9^m+5*3^m+9*(-1)^m+5*(-3)^m)/20",
    "census_polynomial":"(1+u0+u3)^2(1+u0^3+3u1^3+3u2^3+u3^3)^2",
    "checks":"exact integer enumeration of 729 policies; independent finite frame DP at m=0..8; exact determinant and pair injectivity",
    "independent_review":"NOT_REVIEWED",
    "native_TRIADIC_CLOSURE_E_licensing":"OPEN"
}
print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
