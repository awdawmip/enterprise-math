#!/usr/bin/env python3
"""Exact author-side certificate: uniform strict occupancy decline from t=699.
Auxiliary 4-label full-support BRC observer, NOT native X6.
"""
import json
from fractions import Fraction as Fr
from itertools import product
from math import comb, prod
from pathlib import Path

Q = {'0': (1,665,1,333), '2': (333,333,1,333), '3': (1,1,1,997)}
E = ((0,1),(1,2),(1,3),(2,3))
MASKS = tuple((1<<i)|(1<<j) for i,j in E)
DEG = tuple(sum(i in e for e in E) for i in range(4))
S = 698
# Each singleton input C_i*A_i is charged to exactly one incident good edge.
ASSIGN = {'0': ((0,1),(0,1),(2,3),(2,3)),
          '2': ((0,1),(1,2),(2,3),(2,3)),
          '3': ((0,1),(0,1),(2,3),(2,3))}
BETA = {(0,1): Fr(1), (1,0): Fr(1,665),
        (1,2): Fr(1,665), (2,3): Fr(333), (3,2): Fr(1,997)}
LOWER = {Fr(1): Fr(1000), Fr(1,665): Fr(3,2),
         Fr(333): Fr(1_000_000), Fr(1,997): Fr(1001,1000)}


def H(s,b):
    """A 3-term strictly positive lower bound to pair/singleton mass ratio."""
    return sum((comb(s,k)*b**k for k in (1,2,3)),Fr(0))

assert DEG == (1,3,2,2)
assert all(min(q)>0 and sum(q)==1000 for q in Q.values())
assert all(min(Fr(Q[a][j],Q[a][i]) for a in Q)==v for (i,j),v in BETA.items())
for beta,lower in LOWER.items():
    assert H(S,beta)>lower, (beta,H(S,beta),lower)

cert = []
for action,q in Q.items():
    C={i:sum(q[j] for e in E if i in e for j in e if j!=i) for i in range(4)}
    L={e:1000-q[e[0]]-q[e[1]] for e in E}
    for e in E:
        assigned=[i for i in range(4) if ASSIGN[action][i]==e]
        if not assigned: continue
        charge = sum((Fr(C[i],1)/LOWER[BETA[(i,e[0] if i!=e[0] else e[1])]] for i in assigned),Fr(0))
        assert charge<L[e], (action,e,charge,L[e])
        margin=Fr(L[e],1)-charge
        cert.append({'next_action':action,'edge':list(e),'charged_vertices':assigned,
                     'loss_units':L[e], 'charge_upper_units':str(charge),
                     'margin_units':str(margin)})
assert len(cert)==7


def dp_num(word):
    x=[0]*16;x[0]=1
    for a in word:
        y=[0]*16
        for mask,v in enumerate(x):
            if v:
                for i,mass in enumerate(Q[a]):
                    y[mask|(1<<i)]+=v*mass
        x=y
    return sum(x[mask] for mask in MASKS)


def product_num(word):
    ai=[prod(Q[a][i] for a in word) for i in range(4)]
    bij=[prod(Q[a][i]+Q[a][j] for a in word) for i,j in E]
    return sum(bij)-sum(d*x for d,x in zip(DEG,ai))+(4 if not word else 0)

nchecked=0
for length in range(8):
    for letters in product(Q,repeat=length):
        w=''.join(letters)
        assert dp_num(w)==product_num(w),(w,dp_num(w),product_num(w))
        nchecked+=1
assert nchecked==3280


def delta_numer_after(c,a):
    """Integer numerator of 1000**(s+1)*(delta_{s+1}-delta_s)."""
    ai=[prod(Q[x][i]**c.get(x,0) for x in Q) for i in range(4)]
    bij={e:prod((Q[x][e[0]]+Q[x][e[1]])**c.get(x,0) for x in Q) for e in E}
    pair={e:bij[e]-ai[e[0]]-ai[e[1]] for e in E}
    q=Q[a]
    inflow=sum(ai[i]*sum(q[j] for e in E if i in e for j in e if j!=i) for i in range(4))
    outflow=sum(pair[e]*(1000-q[e[0]]-q[e[1]]) for e in E)
    return inflow-outflow

samples=[(698,0,0),(0,698,0),(0,0,698),(1,1,696),(1,696,1),(696,1,1),
         (200,200,298),(100,250,348),(50,500,148),(349,0,349),(0,349,349)]
long_checks=0
for c0,c2,c3 in samples:
    c={'0':c0,'2':c2,'3':c3}
    for a in Q:
        assert delta_numer_after(c,a)<0,(c,a)
        long_checks+=1
assert long_checks==33

w='032020'
val=[Fr(dp_num(w[:j]),1000**j) for j in range(len(w)+1)]
assert val[0]==val[1]==0
M=Fr(0);R=Fr(0);Splus=Fr(0);last=Fr(0)
positive=[]
for t in range(1,len(w)+1):
    dt=val[t]-val[t-1]
    Splus+=max(Fr(0),dt)
    M=max(M,val[t])
    R=Splus-M
    if R>last:positive.append(t)
    last=R
assert positive==[4,6]

result={'schema':'EM_BRC_FULL_SUPPORT_UNIFORM_TAIL_698_AUTHOR_CERT_V1',
        'date':'2026-10-24','model':'auxiliary_four_label_exact_positive_occupancy',
        'good_pairs':[list(e) for e in E], 'action_weight_numerators':Q,
        'all_prefixes_length_at_least':698,
        'strict_negative_delta_from_round':699,
        'original_prior_uniform_threshold_from_round':7584,
        'H3_strict_threshold_checks':{str(b):{'H698':str(H(S,b)),'lower':str(lower)} for b,lower in LOWER.items()},
        'edge_charge_inequalities':cert,
        'exact_short_word_dp_product_checks':nchecked,
        'sample_length_698_exact_negative_checks':long_checks,
        'known_reentry_032020':[4,6],
        'review_status':'AUTHOR_CHECK_ONLY; NO_NATIVE_CLAIM; NO_INDEPENDENT_REVIEW; NOT_ADMITTED'}
path=Path(__file__).with_name('EXACT_EVIDENCE.json')
path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: four exact cubic H698 threshold inequalities')
print('PASS: seven strict action/edge charge inequalities')
print(f'PASS: {nchecked} short words exact 16-mask/product equivalence')
print(f'PASS: {long_checks} independent integer numerator checks at prefix 698')
print('PASS: known reentry episodes {4,6} remain possible before tail')
print('THEOREM (author proof): every word has delta_t < delta_(t-1) for all t>=699')
