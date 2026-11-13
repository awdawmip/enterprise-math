#!/usr/bin/env python3
"""EC49H exact finite positive-rational two-source approximate causal quotient verifier.
Only the auxiliary observation tree is computed: no native signed-BRC/X6 arithmetic.
"""
from fractions import Fraction as F
from itertools import product
import json
import random

Q = ((F(22,48),F(15,48),F(11,48)), (F(26,48),F(9,48),F(13,48)))
P = ((F(11,48),F(15,48),F(22,48)), (F(13,48),F(9,48),F(26,48)))
r = (F(1,2),F(1),F(2))
qbar = tuple((Q[0][j]+Q[1][j])/2 for j in range(3))
pbar = tuple((P[0][j]+P[1][j])/2 for j in range(3))
epsilon = F(1,16)

def tv(a,b): return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2
assert all(x>0 for row in Q+P for x in row)
assert all(sum(row)==1 for row in Q+P)
assert qbar == (F(1,2),F(1,4),F(1,4))
assert pbar == (F(1,4),F(1,4),F(1,2))
for w,j in product(range(2),range(3)):
    assert P[w][j] == r[j]*Q[w][j]
for theta,bar in ((Q,qbar),(P,pbar)):
    assert all(tv(row,bar)==epsilon for row in theta)

# A pure strategy: root 'R' or 'A', or ('B', three-bit terminal acceptance mask).
policies = ['R','A'] + [('B',mask) for mask in range(8)]
def conditional(w,policy,law):
    if policy=='R': return F(0),F(0)
    if policy=='A': return F(1),F(0)
    return sum((law[w][j] for j in range(3) if policy[1] & (1<<j)),F(0)),F(1)
def raw_full(p0,p1):
    out=[]
    for law in (P,Q):
        a0,t0=conditional(0,p0,law); a1,t1=conditional(1,p1,law)
        out.extend(((a0+a1)/2,(t0+t1)/2))
    return (out[0],out[2],out[1],out[3])
def raw_coarse(p):
    if p=='R': return F(0),F(0),F(0),F(0)
    if p=='A': return F(1),F(1),F(0),F(0)
    pa=sum((pbar[j] for j in range(3) if p[1]&(1<<j)),F(0))
    qa=sum((qbar[j] for j in range(3) if p[1]&(1<<j)),F(0))
    return pa,qa,F(1),F(1)
def H(o): return o[0]-F(3,2)*o[1]-(o[2]+o[3])/16

# Q-occupation compilation: a single source-independent compressed randomized policy.
def compile_full(p0,p1):
    pair=(p0,p1)
    a=sum((F(1,2) for p in pair if p=='A'),F(0))
    b=sum((F(1,2) for p in pair if isinstance(p,tuple)),F(0))
    nu=[]
    for j in range(3):
        den=sum((Q[w][j]/2 for w,p in enumerate(pair) if isinstance(p,tuple)),F(0))
        num=sum((Q[w][j]/2 for w,p in enumerate(pair) if isinstance(p,tuple) and p[1]&(1<<j)),F(0))
        nu.append(num/den if den else F(0))
    assert a>=0 and b>=0 and a+b<=1
    assert all(F(0)<=x<=1 for x in nu)
    return (a+b*sum((pbar[j]*nu[j] for j in range(3)),F(0)),
            a+b*sum((qbar[j]*nu[j] for j in range(3)),F(0)),b,b)

all_full=[(raw_full(p0,p1),p0,p1) for p0,p1 in product(policies,repeat=2)]
all_coarse=[(raw_coarse(p),p) for p in policies]
assert len(all_full)==100 and len(all_coarse)==10
best_full=max(((H(o),p0,p1) for o,p0,p1 in all_full))
best_coarse=max(H(o) for o,p in all_coarse)
assert best_full[0]==F(1,192), best_full
assert best_coarse==0
witness=raw_full('R',('B',4))
assert witness==(F(13,48),F(13,96),F(1,2),F(1,2))
assert H(witness)==F(1,192)
max_alpha=max(abs(o[0]-compile_full(p0,p1)[0]) for o,p0,p1 in all_full)
max_beta=max(abs(o[1]-compile_full(p0,p1)[1]) for o,p0,p1 in all_full)
for o,p0,p1 in all_full:
    z=compile_full(p0,p1)
    assert abs(o[0]-z[0]) <= epsilon and abs(o[1]-z[1]) <= epsilon
    assert o[2:]==z[2:]
for o,p in all_coarse:
    assert raw_full(p,p)==o

# Test mixtures of two full strategies with exact Q-occupation compilation.
# A mixture is equivalent to a single randomized behavioral strategy in this finite perfect-recall tree.
rng=random.Random(4908)
num_mixtures=250
for _ in range(num_mixtures):
    i,j=rng.randrange(100),rng.randrange(100)
    w=F(rng.randint(0,100),101)
    o1,p01,p11=all_full[i]; o2,p02,p12=all_full[j]
    target=tuple(w*x+(1-w)*y for x,y in zip(o1,o2))
    a=(w*sum(F(1,2) for p in (p01,p11) if p=='A')
       +(1-w)*sum(F(1,2) for p in (p02,p12) if p=='A'))
    b=(w*sum(F(1,2) for p in (p01,p11) if isinstance(p,tuple))
       +(1-w)*sum(F(1,2) for p in (p02,p12) if isinstance(p,tuple)))
    nu=[]
    for k in range(3):
        def pieces(pa,pb):
            den=sum((Q[h][k]/2 for h,p in enumerate((pa,pb)) if isinstance(p,tuple)),F(0))
            num=sum((Q[h][k]/2 for h,p in enumerate((pa,pb)) if isinstance(p,tuple) and p[1]&(1<<k)),F(0))
            return num,den
        n1,d1=pieces(p01,p11);n2,d2=pieces(p02,p12)
        den=w*d1+(1-w)*d2
        nu.append((w*n1+(1-w)*n2)/den if den else F(0))
    z=(a+b*sum((pbar[k]*nu[k] for k in range(3)),F(0)),
       a+b*sum((qbar[k]*nu[k] for k in range(3)),F(0)),b,b)
    assert abs(target[0]-z[0])<=epsilon and abs(target[1]-z[1])<=epsilon
    assert target[2:]==z[2:]

def fmt(v): return str(v)
report={
    'scope':'finite positive rational two-source auxiliary observation model; not signed BRC/X6',
    'leaf_count_per_source':6, 'full_deterministic_strategies':len(all_full),
    'coarse_deterministic_strategies':len(all_coarse), 'rational_mixture_checks':num_mixtures,
    'Q_W':[[fmt(x) for x in row] for row in Q],
    'P_W':[[fmt(x) for x in row] for row in P],
    'quotient_Q':[fmt(x) for x in qbar],
    'quotient_P':[fmt(x) for x in pbar],
    'terminal_likelihood_ratios':[fmt(x) for x in r],
    'max_action_conditional_kernel_TV':{'Q':fmt(epsilon),'P':fmt(epsilon)},
    'max_compiled_abs_acceptance_error':{'P':fmt(max_alpha),'Q':fmt(max_beta)},
    'max_compiled_abs_clock_error':{'P':'0','Q':'0'},
    'best_full_support':fmt(best_full[0]),'best_coarse_support':fmt(best_coarse),
    'strict_support_gap':fmt(best_full[0]-best_coarse),
    'explicit_full_witness':[fmt(x) for x in witness],
    'explicit_compiled_witness':[fmt(x) for x in compile_full('R',('B',4))],
    'raw_region_exact_equal':False,
    'analytic_general_bound':'acceptance <= 1/16 each; clock errors = 0 for this model',
    'assertions':'PASS'
}
print(json.dumps(report,indent=2,ensure_ascii=False,sort_keys=True))
