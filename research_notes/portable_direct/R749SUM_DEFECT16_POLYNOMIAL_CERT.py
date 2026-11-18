#!/usr/bin/env python3
"""Exact polynomial / inequality certificate for R749SUM; no external packages.

The full finite M<=10000 domain is a REUSED immutable R749SUK C++17 certificate,
not rerun by this checker. Its provenance is recorded in the companion note.
"""
import json

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def add(a,b):
    return trim([ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b))) ])

def neg(a): return [-v for v in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return trim(out)
def powp(a,n):
    out=[1]
    for _ in range(n): out=mul(out,a)
    return out

T=[0,1]; t2=mul(T,T); m=sub(t2,[1]); mt=sub(m,T)
W=mul(m,powp(mt,2))
p2=sub(mul([27],W),powp(sub(sub(mul([3],m),mul([2],T)),[1]),3))
p6=sub(mul([17],W),mul(add(mul([16],t2),[1]),powp(add(m,mul([2],T)),2)))
p7=sub(mul([2],powp(mt,2)),mul(add(t2,[1]),m))
assert p2==[37,42,-42,-28,18], p2
assert p6==[-18,-30,16,128,-67,-98,1], p6
assert p7==[3,4,-2,-4,1], p7

# Exhaust a moderate regression range of the exact rational inequality;
# the proof for all t>=99 is via positive polynomial decomposition in the note.
checks=0
for t in range(99,257):
    m=t*t-1; W=m*(m-t)**2
    assert 27*W>(3*m-2*t-1)**3
    assert 17*W>(16*t*t+1)*(t*t+2*t-1)**2
    for delta in range(2*t+1):
        M=m+delta; S=3*delta+2*t
        # Bound from the exact deficit and determinant identities.
        assert (S*S+4)*M*M < 68*W
        checks+=1
for t in range(5,501):
    m=t*t-1; W=m*(m-t)**2
    assert (4*t*t+4)*m*m < 8*W  # square subsequence: |Q|<2

result={
    'record':'R749SUM', 'status':'PASS',
    'arithmetics':'exact_integer_polynomial_and_rational_cross_multiplication',
    'polynomial_identities_checked':3,
    'complete_tail_regression_t':'99..256',
    'all_delta_tail_regression_cases':checks,
    'square_subsequence_regression_t':'5..500',
    'analytic_infinite_threshold_t':99,
    'analytic_infinite_threshold_M':9800,
    'new_all_M_optimal_absolute_Q_bound':16,
    'finite_cert_reused':'R749SUK_Q_FIBER_UNIFORM_BOUND_CERT.cpp at 0b292a4181f3729b2bda282cf35e6df2166531e5; previous PASS M=2..10000',
    'finite_cert_rerun_this_round':False,
    'scope':'auxiliary_labeled_two_Port_WBRC_threshold_maximizers; no_native_X6_admission'
}
print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
