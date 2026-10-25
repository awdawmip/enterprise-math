#!/usr/bin/env python3
"""R284: exact BRC central-gap syzygy: six-edge DP vs algebraic ODE.
Only ordered positive-count auxiliary BRC paths; no P000 native computation.
Run: python3 R284_verify_gap_syzygy.py
"""
from collections import defaultdict
from hashlib import sha256
from json import dumps
from pathlib import Path

MAX_DP_N = 320
MAX_ALG_M = 1600
EDGES = {
    (0, 0): (2, -1, -1), (0, 1): (2, +1, -1),
    (1, 0): (0, -1, -1), (1, 1): (0, +1, -1),
    (2, 0): (1, -1, -1), (2, 1): (2, +1, -1),
}

def at(xs, i):
    return xs[i] if 0 <= i < len(xs) else 0

def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out

# h(y)=1-3y+y^2, q(y)=1+y+y^2.
# g(y)=sqrt(h/q), g(0)=1, satisfies
# (1-2y-y^2-2y^3+y^4)g' = 2(y^2-1)g.
g = [1]
for n in range(MAX_ALG_M + 2):
    top = ((2*n - 2)*at(g, n) + (n - 1)*at(g, n-1)
           + (2*n - 2)*at(g, n-2) - (n - 3)*at(g, n-3))
    assert top % (n+1) == 0, (n, top)
    g.append(top // (n+1))
assert g[:10] == [1, -2, 0, 0, -2, -2, -4, -10, -20, -44]

# K(y) = [(y-1) P7(y) - P8(y)*g(y)] / [2y(1+y)].
P7 = [-1, 1, -8, 4, -6, 11, -6, 1]
P8 = [1, -2, 1, -8, 6, -3, 7, -5, 1]
A = poly_mul([-1, 1], P7)
K = []
for m in range(MAX_ALG_M + 1):
    j = m+1
    numerator = at(A,j) - sum(p*at(g,j-i) for i,p in enumerate(P8))
    assert numerator % 2 == 0, (m,numerator)
    K.append(numerator//2 - at(K,m-1))
assert K[:12] == [1,1,-2,-3,1,2,-2,-3,-2,-6,-13,-24]

# p(y)=1-y-2y^3+y^4; E(x)=x^8 K(x^2), O(x)=x^5 p(x^2)K(x^2).
p = [1,-1,0,-2,1]
PK = [sum(v*at(K,j-i) for i,v in enumerate(p)) for j in range(MAX_ALG_M+1)]

# Completely separate positive integer count of original ordered source words.
dp = {(0,2,+1,0):1}  # previous=2 means no source bit yet
checked_dp_levels = 0
checked_even, checked_odd = 0,0
samples={}
for n in range(MAX_DP_N + 1):
    clean0=defaultdict(int)
    for (q,previous,eps,k),count in dp.items():
        if q==0:
            clean0[(eps,k)]+=count
    if n%2==0 and n>=8:
        e=clean0[(+1,-4)]-clean0[(-1,-4)]
        assert e==K[(n-8)//2],('even',n,e,K[(n-8)//2])
        checked_even+=1
    if n%2==1 and n>=5:
        o=clean0[(-1,-3)]-clean0[(+1,-5)]
        assert o==PK[(n-5)//2],('odd',n,o,PK[(n-5)//2])
        checked_odd+=1
    if n in (8,40,73,74,79,80,81,82,100,101,150,151,319,320):
        samples[str(n)]={'plus_minus4':str(clean0[(+1,-4)]),
                         'minus_minus4':str(clean0[(-1,-4)]),
                         'minus_minus3':str(clean0[(-1,-3)]),
                         'plus_minus5':str(clean0[(+1,-5)])}
    checked_dp_levels+=1
    next_dp=defaultdict(int)
    for (q,previous,eps,k),count in dp.items():
        for bit in (0,1):
            if previous==0 and bit==0:
                continue
            q2,eta,b=EDGES[(q,bit)]
            next_dp[(q2,bit,eps*eta,eta*k+b)]+=count
    dp=next_dp

# Independent entire integer tail through 3208 even / 3205 odd.
nonpositive_even=[8+2*i for i,v in enumerate(K) if v<=0]
nonpositive_odd=[5+2*i for i,v in enumerate(PK) if v<=0]
assert max(nonpositive_even)==80, max(nonpositive_even)
assert max(nonpositive_odd)==73, max(nonpositive_odd)
# Exact syzygy: x^3 O(x)=p(x^2)E(x); the current arrays realize it coefficientwise.
for j in range(5,MAX_ALG_M-1):
    m=2*j+8
    assert PK[j+2] == (at(K,j+2)-at(K,j+1)-2*at(K,j-1)+at(K,j-2)),m
report={
    'schema':'ENTERPRISE_MATH_R284_GAP_SYZYGY_EXACT_EVIDENCE_V1',
    'status':'PASS','model':'ordered positive six-edge clean reset BRC auxiliary; not P000 native X6 or heartbeat time',
    'exact_algebraic_law':'x^3 O(x)=(1-x^2-2*x^6+x^8)*E(x)',
    'single_kernel':'E(x)=x^8 K(x^2); O(x)=x^5 p(x^2)K(x^2)',
    'kernel_ode':'(1-2y-y^2-2y^3+y^4)g\'=2(y^2-1)g; g=sqrt((1-3y+y^2)/(1+y+y^2))',
    'last_nonpositive_even_gap_through_3208':max(nonpositive_even),
    'last_nonpositive_odd_gap_through_3205':max(nonpositive_odd),
    'exact_generated_max_even_length':8+2*MAX_ALG_M,
    'exact_generated_max_odd_length':5+2*MAX_ALG_M,
    'independent_original_DP_max_length':MAX_DP_N,
    'independent_DP_levels_checked':checked_dp_levels,
    'crosschecked_even_lengths':checked_even,
    'crosschecked_odd_lengths':checked_odd,
    'finite_evidence_not_universal_positive_threshold':True,
    'analytic_asymptotics_proved_in_companion_note_not_by_DP':True,
    'samples':samples,
    'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'author_side_only':True,'driver_review':'NOT_DONE',
}
file=Path(__file__).with_name('EXACT_EVIDENCE.json')
file.write_text(dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
print('PASS: DP 0..%d, algebraic ODE to m=%d; %d even and %d odd direct matches.'%(MAX_DP_N,MAX_ALG_M,checked_even,checked_odd))
print('Last nonpositive central gap: even n=%d, odd n=%d (finite checks only).'%(max(nonpositive_even),max(nonpositive_odd)))
print('Evidence:',file)
