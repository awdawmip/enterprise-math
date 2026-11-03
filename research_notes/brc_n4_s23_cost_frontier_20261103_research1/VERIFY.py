#!/usr/bin/env python3
"""Exact rational finite-budget certificates for the BRC-S23 two-state T/B experiment.

No floating-point arithmetic and no external packages.  Read PROOF.md for the
experiment definition and scope.  Fraction is used on labeled stopping outcomes;
source labels and sampling prices remain fixed in the experimental model.
"""
from fractions import Fraction as Q
from math import comb
from functools import lru_cache
from itertools import product
from pathlib import Path

H = Q(1, 42)
S = Q(1, 4)
P, R = Q(1, 2) + H, Q(1, 2) - H

@lru_cache(None)
def aggregate_error(f, r):
    # k = nonerased ternary draws, t = their positive signs, u = positive B draws.
    e = Q(0)
    for k in range(f + 1):
        for t in range(k + 1):
            for u in range(r + 1):
                m = comb(f, k) * comb(k, t) * comb(r, u)
                m *= (1-S) ** (f-k) * S**k
                plus = P**t * R**(k-t) * (S*P)**u * (1-S*P)**(r-u)
                minus = R**t * P**(k-t) * (S*R)**u * (1-S*R)**(r-u)
                e += m * min(plus, minus)
    return e / 2

@lru_cache(None)
def direct_error(f, r):
    # Independently enumerate each labeled sample sequence; do not aggregate by k/t/u.
    tp = ((S*P, S*R), (1-S, 1-S), (S*R, S*P))
    bp = ((S*P, S*R), (1-S*P, 1-S*R))
    total = Q(0)
    for tr in product(range(3), repeat=f):
        a, b = Q(1), Q(1)
        for v in tr:
            a *= tp[v][0]
            b *= tp[v][1]
        for br in product(range(2), repeat=r):
            c, d = a, b
            for v in br:
                c *= bp[v][0]
                d *= bp[v][1]
            total += min(c, d)
    return total/2

# Covers every budget L=n/4 for integer n=0..56, including slack and ties.
rows=[]
unique_portfolios=set()
for n in range(57):
    candidates=[(f,r,aggregate_error(f,r))
                for f in range(n//7+1)
                for r in range((n-7*f)//4+1)]
    unique_portfolios.update((f,r) for f,r,_ in candidates)
    e=min(v for _,_,v in candidates)
    winners=[(f,r) for f,r,v in candidates if v == e]
    assert len(winners) >= 1
    rows.append((n,e,winners,len(candidates)))

# An independent full sequence-based check for ALL feasible distinct f,r at L<=11.
checked=0
for f,r in sorted(unique_portfolios):
    if 7*f+4*r<=44:
        assert aggregate_error(f,r)==direct_error(f,r), (f,r)
        checked += 1

# Error decreases with an added fixed experiment; compare possible slack/ties.
for n,e,winners,k in rows:
    if n and n%4==0:
        assert e <= rows[n-1][1]
    for f,r in winners:
        assert 7*f+4*r<=n

# Key exact optima and strict gap certificates.
w7=rows[28][2]; w11=rows[44][2]; w14=rows[56][2]
assert w7==[(1,5)], w7
assert w11==[(0,11)], w11
assert w14==[(1,12)], w14
assert aggregate_error(0,7)-aggregate_error(1,5)==Q(50769489581,59018069311488)
assert aggregate_error(4,4)-aggregate_error(0,11)==Q(368056034177868079,1469170321634239709184)
assert aggregate_error(0,14)>aggregate_error(1,12)

# Verify budget-bounded candidate lists can be compressed to max-r for each f.
for n in (28,44,56):
    feasible=[(f,r,aggregate_error(f,r)) for f in range(n//7+1)
              for r in range((n-7*f)//4+1)]
    reduced=[(f,(n-7*f)//4,aggregate_error(f,(n-7*f)//4))
             for f in range(n//7+1)]
    assert min(t[2] for t in feasible)==min(t[2] for t in reduced)

out=Path(__file__).resolve().parent
with (out/'COST_FRONTIER.tsv').open('w',encoding='utf-8') as h:
    h.write('quarter_budget\tbudget\twinning_f\twinning_r\tmin_error\twinner_count\tfeasible_count\n')
    for n,e,winners,k in rows:
        for f,r in winners:
            h.write(f'{n}\t{Q(n,4)}\t{f}\t{r}\t{e}\t{len(winners)}\t{k}\n')
print('PASS_BRC_S23_FINITE_BUDGET_EXACT_FRONTIER_20261103')
print('h=',H,'s=',S,'cost_T=7/4 cost_B=1')
print('budgets_checked=',len(rows),'quarter_grid=[0,56]')
print('unique_feasible_portfolios=',len(unique_portfolios))
print('independent_sequence_checks_at_budget_le_11=',checked)
for n in [28,44,56]:
    e=rows[n][1]
    print('budget=',Q(n,4),'winner=',rows[n][2], 'Bayes_error=',e,'candidate_count=',rows[n][3])
    print('maximal_r_by_f:')
    for f in range(n//7+1):
        r=(n-7*f)//4
        print('  ',f,r,str(aggregate_error(f,r)))
print('gap_L7_B7_minus_T1B5=',aggregate_error(0,7)-aggregate_error(1,5))
print('gap_L11_T4B4_minus_B11=',aggregate_error(4,4)-aggregate_error(0,11))
print('gap_L14_B14_minus_T1B12=',aggregate_error(0,14)-aggregate_error(1,12))
print('frontier_tsv_rows=',len(rows))
