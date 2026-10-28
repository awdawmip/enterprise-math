#!/usr/bin/env python3
"""Exact, dependency-pinned BRC N4 two-parameter terminal-gauge certificate.

Depends on the previously published frozen N4 Phase VERIFY.py and validates
its SHA256 before importing; Python stdlib only, no native EM authority implied.
"""
import contextlib
import hashlib
import io
import json
import runpy
from fractions import Fraction as F
from itertools import product
from pathlib import Path

BASE = Path(__file__).resolve().parent
OLD = BASE.parent / 'brc_n4_complete_postflat_minimax_20261028_r1t11' / 'VERIFY.py'
EXPECTED_SHA256 = '1efe4f96160ed7f2e9a3e1c15d17359f7b8d778f52b8e0a2bfab1fcabcbca959'
assert hashlib.sha256(OLD.read_bytes()).hexdigest() == EXPECTED_SHA256
with contextlib.redirect_stdout(io.StringIO()):
    S = runpy.run_path(str(OLD))
N = S['N']
ZERO, ONE = F(0), F(1)
L2, END = F(89,125), ONE
L0, LC = F(27483,39215), F(11526,16445)

# Exact model. AV00 and AV01 are the two children of AV0; both have r=1/4.
assert N[3]['AV0'][:2] == (F(1,6), F(1,4))
for h in ('AV00','AV01'):
    assert N[4][h][0] == F(1,12) and N[4][h][1] == F(1,4)

# Constrained full-history model: only AV0's two t4 terminal decisions change.
def full_action(lam, eta, t, h):
    if t == 4 and h in ('AV00','AV01'):
        return (eta, ONE-eta, ZERO)
    return S['full_history'](lam, t, h, N[t][h][1])

# A C3 policy: AV0 and AV1 share the same instantaneous decision at t3.
# On the unreachable BV fiber all histories use the same P decision.
def c3_action(lam, eta, t, h):
    if t == 3 and h in ('AV0','AV1'):
        return ZERO, (ONE-lam)/2, (ONE+lam)/2
    if t == 4 and h in ('AV00','AV01'):
        p = (F(253,500)*(ONE-lam) + 2*lam*eta)/(ONE+lam)
        assert ZERO <= p <= ONE
        return p, ONE-p, ZERO
    return S['full_history'](lam, t, h, N[t][h][1])

# Compute complete 16-cell Q/P observable from labeled leaf paths, separately
# from the 53-flow certificate. Each leaf carries exact P and Q masses.
def evaluate(action, lam, eta):
    v = [ZERO] * 16
    for leaf, (q, r, _) in N[4].items():
        survivor = ONE
        for t, h in enumerate((leaf[:1],leaf[:2],leaf[:3],leaf), 1):
            p, qq, cc = action(lam,eta,t,h)
            assert ZERO <= p <= ONE and ZERO <= qq <= ONE and ZERO <= cc <= ONE
            assert p+qq+cc == ONE and (t != 4 or cc == ZERO)
            i = 2*(t-1)
            v[i] += q*survivor*p
            v[i+1] += q*survivor*qq
            v[8+i] += q*r*survivor*p
            v[8+i+1] += q*r*survivor*qq
            survivor *= cc
        assert survivor == ZERO
    assert sum(v[:8],ZERO) == sum(v[8:],ZERO) == ONE
    return v

def full_target(lam,eta):
    v = S['target'](lam).copy()
    v[6] += lam*eta/6
    v[7] -= lam*eta/6
    v[14] += lam*eta/24
    v[15] -= lam*eta/24
    return v

def phase_floor(lam):
    assert L0 <= lam <= END
    return max(fun(lam) for fun in S['floors'])

# The previous four exact 53-flow endpoint witnesses are reused WITHOUT
# reoptimizing or treating an unreachable convexification as an actual policy.
def c23_occupancy(lam,eta):
    assert L0 <= lam <= ONE and ZERO <= eta <= ONE
    ab = [(L0,LC),(LC,L2),(L2,END)]
    a,b = next((a,b) for a,b in ab if a <= lam <= b)
    alpha = (lam-a)/(b-a)
    xa,xb = S['endpoint'][a],S['endpoint'][b]
    x = {k: (ONE-alpha)*xa[k] + alpha*xb[k] for k in S['keys']}
    keyP,keyQ = (4,F(1,4),0),(4,F(1,4),1)
    assert x[keyQ] >= lam  # exact endpoint check + affine interpolation
    x[keyP] += lam*eta
    x[keyQ] -= lam*eta
    S['check_flow'](x)
    return x

# Independent S3 Bellman minimum: 9 t1 * 81 t2 prefix configurations,
# then exact min over the constrained t3 common-ratio fibers and free t4.
W3Q = list(map(F, ['1/10','1/10','97/1000','1/10','1/10','374/3875','1/10','-1/10']))
W3P = list(map(F, ['2/5','2/5','-2/5','2/5','2/5','-617/1550','-2/5','2/5']))
assert max(W3Q)-min(W3Q) + max(W3P)-min(W3P) == ONE

def bellman_s3():
    def cost(t,r,d): return W3Q[2*(t-1)+d] + r*W3P[2*(t-1)+d]
    c4 = {}
    for h,(q,r,_) in N[3].items():
        c4[h] = sum((qc/q * min(cost(4,rr,0),cost(4,rr,1))
                    for hh,(qc,rr,pa) in N[4].items() if pa == h), ZERO)
    best,count=None,0
    for first in product(range(3),repeat=2):
        early=dict(zip(('A','B'),first))
        for second in product(range(3),repeat=4):
            count += 1
            later=dict(zip(('AU','AV','BU','BV'),second))
            value=ZERO
            reachable={}
            for h,(q,r,_) in N[1].items():
                if early[h] != 2: value += q*cost(1,r,early[h])
            for h,(q,r,pa) in N[2].items():
                if early[pa] != 2: continue
                d=later[h]
                if d!=2:value+=q*cost(2,r,d)
                else:
                    for h3,(q3,r3,pa3) in N[3].items():
                        if pa3==h:
                            reachable.setdefault(r3,[]).append((q3,h3))
            for r, items in reachable.items():
                value += min(
                    sum((q*cost(3,r,0) for q,h in items),ZERO),
                    sum((q*cost(3,r,1) for q,h in items),ZERO),
                    sum((q*c4[h] for q,h in items),ZERO))
            if best is None or value<best: best=value
    assert count==729
    return best,count

assert bellman_s3() == (-F(1229,4000),729)
W2Q,W2P = S['w2q'],S['w2p']
assert S['bellman_S2'](W2Q,W2P) == (-F(85,456),243)
for qdual,pdual,_ in S['weights']:
    assert (qdual[6]-qdual[7])+F(1,4)*(pdual[6]-pdual[7]) == ZERO
for lam0 in (L0,LC,L2,END):
    assert S['endpoint'][lam0][(4,F(1,4),1)] >= lam0
assert (W2Q[6]-W2Q[7])+F(1,4)*(W2P[6]-W2P[7]) == ZERO
assert (W3Q[6]-W3Q[7])+F(1,4)*(W3P[6]-W3P[7]) == ZERO

def dot(w,v):return sum((a*b for a,b in zip(w,v)),ZERO)

def record(lam,eta):
    assert L0 <= lam <= END and ZERO<=eta<=ONE
    ref = full_target(lam,eta)
    assert evaluate(full_action,lam,eta)==ref
    # S3: shared t3 action plus independently chosen legal t4 decisions.
    c3 = evaluate(c3_action,lam,eta)
    # S23: occupancy-flow is exact causal behavior on this specific tree.
    x = c23_occupancy(lam,eta)
    c23 = S['observations'](x)
    t3q,t3p = S['tvs'](c3,ref)
    t23q,t23p = S['tvs'](c23,ref)
    d3 = (ONE-lam)/2000
    d23 = phase_floor(lam)
    assert (t3q,t3p)==(d3,d3)
    assert (t23q,t23p)==(d23,d23)
    assert -F(1229,4000)-dot(W3Q+W3P,ref)==d3
    assert -F(85,456)-dot(W2Q+W2P,ref) == S['floors'][2](lam)
    # In the right-hand phase the third Bellman dual is exactly active.
    if lam>=L2:assert S['floors'][2](lam)==d23
    else:
        j = 0 if lam <= LC else 1
        q,p = S['weights'][j][:2]
        lower = S['weights'][j][2]-dot(q+p,ref)
        assert lower == d23
    return {
        'lambda':str(lam), 'eta':str(eta),
        'd2_equals_d23':str(d23), 'd3':str(d3),
        'gap':str(d3),
        'realized_TV_C3':[str(t3q),str(t3p)],
        'realized_TV_C23':[str(t23q),str(t23p)],
        'changed_target_mass_Q_T4_P':str(lam*eta/6),
        'changed_target_mass_P_T4_P':str(lam*eta/24),
        'terminal_C23_P_occupancy_at_r_1over4':str(x[(4,F(1,4),0)])
    }

# All real λ and η are covered by symbolic causal-flow algebra and endpoint
# inequalities. These exact rational probes test independent implementations.
pairs = [(L0,ZERO),(L0,ONE),(LC,F(1,3)),(LC,ONE),
         (L2,ZERO),(L2,F(1,2)),(L2,ONE),
         (F(4,5),F(1,3)),(F(9,10),ONE),(ONE,ONE),
         (F(71,100),F(7,8)),(F(99,100),F(99,100))]
results=[record(a,b) for a,b in pairs]
print(json.dumps({
    'status':'PASS_EXACT_FRACTION_N4_TWO_PARAMETER_TERMINAL_GAUGE',
    'predecessor_sha256':EXPECTED_SHA256,
    'two_parameter_domain':['27483/39215<=lambda<=1','0<=eta<=1'],
    'formula_d2_equals_d23':'max(1/506,11/22855+39*lambda/18284,13*lambda/228-11/285)',
    'formula_d3':'(1-lambda)/2000',
    'formula_subadd_gap':'(1-lambda)/2000',
    'bellman_S2_cases':243,'bellman_S3_cases':729,
    'exact_samples':results,
    'proof_scope':'author-side exact finite external BRC tree; no X6-native transfer, no formal admission'
},indent=2,sort_keys=True,ensure_ascii=False))
