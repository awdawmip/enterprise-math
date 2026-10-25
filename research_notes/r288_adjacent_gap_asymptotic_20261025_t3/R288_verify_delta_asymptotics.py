"""Exact finite crosschecks for R288 fixed-offset BRC adjacent-fiber gaps.

Mathematical asymptotic positivity comes from the accompanying analytic proof,
not from extrapolating these finite integer calculations.
"""
from collections import defaultdict
import json

N = 320
J = N // 2 + 8
M = 20
TRANSITIONS = (
    ((2, -1, -1), (2, 1, -1)),
    ((0, -1, -1), (0, 1, -1)),
    ((1, 1, 1), (2, 1, -1)),
)

def mul(a, b, n=J):
    out = [0] * (n+1)
    for i, ai in enumerate(a[:n+1]):
        if not ai:
            continue
        for j, bj in enumerate(b[:n+1-i]):
            if bj:
                out[i+j] += ai*bj
    return out

# w=u/x, where y*w^2-(1+2*y^2-y^3)*w+1=0, w(0)=1.
w = [0]*(J+1)
w[0] = 1
for n in range(1,J+1):
    w[n] = sum(w[i]*w[n-1-i] for i in range(n)) \
           - (2*w[n-2] if n>=2 else 0) \
           + (w[n-3] if n>=3 else 0)
assert w[:5] == [1,1,0,0,1], w[:5]
assert all(v >= 0 for v in w)

powers = [[1] + [0]*J]
for m in range(M+3):
    powers.append(mul(powers[-1], w))

def delta_by_algebra(eps, m):
    if eps == 1:
        base = powers[m+1]
        subtract = mul(base, w)
        # w^(m+1) * (1-y+y^2-y*w)
        A = [base[j] - (base[j-1] if j>=1 else 0)
             + (base[j-2] if j>=2 else 0)
             - (subtract[j-1] if j>=1 else 0) for j in range(J+1)]
    else:
        base = powers[m-1]
        subtract = mul(base,w)
        A = [base[j] - (subtract[j-1] if j>=1 else 0) for j in range(J+1)]
    # Division by 1+y as a formal series.
    d = []
    prev = 0
    for aj in A:
        cur = aj - prev
        d.append(cur)
        prev = cur
    return d

algebra = {(eps,m): delta_by_algebra(eps,m) for eps in (1,-1)
           for m in range(1 if eps==1 else 2,M+1)}

states = {(0,1,0,False):1}
compared = 0
observed_last_negative = {}
for n in range(N+1):
    P = defaultdict(int)
    for (q,eps,k,z),count in states.items():
        if q == 0:
            P[(eps,k)] += count
    for (eps,m), coeff in algebra.items():
        if n>=m+2 and (n-m)%2 == 0:
            j=(n-m-2)//2
            gap = P[(eps,-m)]-P[(eps,-m-2)]
            assert gap == coeff[j], (n,eps,m,j,gap,coeff[j])
            compared += 1
            if gap < 0:
                observed_last_negative[f'{eps}:{m}'] = n
    next_states=defaultdict(int)
    for (q,eps,k,z),count in states.items():
        for b,(nq,eta,c) in enumerate(TRANSITIONS[q]):
            if z and b==0:
                continue
            next_states[(nq,eta*eps,eta*k+c,b==0)]+=count
    states=next_states

# Additional independent radical identity: D=a^2-4*y, v=(a-sqrt D)/2,
# (1-u^2)/sqrt D = u/x. Tested in Q(y)[w]/(y*w^2-a*w+1)
# via exact symbolic polynomial reduction at a sample of finite degrees:
# s=a-2*y*w; (1-y*w^2) = s*w by the polynomial relation.
a_coeff = [0]*(J+1)
a_coeff[0] = 1
a_coeff[2] = 2
a_coeff[3] = -1
s_coeff = [a_coeff[j] - (2*w[j-1] if j>=1 else 0)
           for j in range(J+1)]
ww = mul(w,w)
sw = mul(s_coeff,w)
for j in range(J+1):
    expected = int(j==0) - (ww[j-1] if j>=1 else 0)
    assert sw[j] == expected, (j,sw[j],expected)
identity_checks = J+1

res={
  'schema':'EM_R288_ALGEBRAIC_ADJACENT_GAP_V1',
  'source_model':'ordered positive BRC raw words with no adjacent zero and final q=0',
  'arithmetic':'unbounded Python integers',
  'checked_lengths_inclusive':[0,N],
  'offsets_plus_inclusive':[1,M],
  'offsets_minus_inclusive':[2,M],
  'exact_gap_coefficient_checks':compared,
  'quadratic_radical_cancellation_degree_checks':identity_checks,
  'formal_w_first_12':w[:12],
  'observed_last_negative_by_offset':observed_last_negative,
  'theorem_scope':'Fixed-m eventual sign classification proven analytically; full-length positivity for m=13,14,+ and m=11,12,- remains open',
  'status':'PASS'
}
print(json.dumps(res,indent=2,ensure_ascii=False,sort_keys=True))
