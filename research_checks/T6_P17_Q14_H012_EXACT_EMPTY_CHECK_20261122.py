#!/usr/bin/env python3
"""Exact p17 q14 split(7,7) H0/H1 cancellation-normalized multiplicity audit."""
from collections import defaultdict, Counter
from fractions import Fraction
from functools import lru_cache
import json

def smooth17(n):
    for p in (2,3,5,7,11,13,17):
        while n % p == 0:
            n //= p
    return n == 1

atoms = tuple((q,r,289*q+17*r-1,Fraction(1,17*q+r))
              for q in range(1,8) for r in range(1,17) if smooth17(17*q+r))
assert len(atoms) == 60

rosters = []
def enumerate_vertical(start,q_left,mass,items,reciprocal,mask):
    if not q_left:
        rosters.append((tuple(items),mass,len(items),reciprocal,mask))
        return
    for idx in range(start,len(atoms)):
        q,r,cost,term = atoms[idx]
        if q <= q_left and mass+cost <= 2331:
            items.append(idx)
            enumerate_vertical(idx,q_left-q,mass+cost,items,reciprocal+term,mask|(1<<idx))
            items.pop()
enumerate_vertical(0,7,0,[],Fraction(0),0)
assert len(rosters) == 1907
prior_disjoint = sum(1 for i,a in enumerate(rosters) for b in rosters[i+1:] if not (a[4]&b[4]))
assert prior_disjoint == 809566

q0 = []
def enumerate_q0(j,budget,mass,count,reciprocal,mask,counts):
    if j == 17:
        q0.append((tuple(counts),mass,count,reciprocal,mask))
        return
    cost = 17*j-1
    for k in range(budget//cost+1):
        counts.append(k)
        enumerate_q0(j+1,budget-k*cost,mass+k*cost,count+k,
                     reciprocal+Fraction(k,j),mask|((1<<(j-1)) if k else 0),counts)
        counts.pop()
enumerate_q0(1,292,0,0,Fraction(0),0,[])
assert len(q0) == 1223

vertical = defaultdict(list)
for row in rosters:
    vertical[row[2]].append(row)
min_mass = {n:min(row[1] for row in vertical[n]) for n in range(1,8)}
assert [min_mass[n] for n in range(1,8)] == [2039,2072,2071,2087,2103,2119,2135]

@lru_cache(None)
def allowed_vertical(n,q0_cost):
    grouped=defaultdict(list)
    for row in vertical[n]:
        if row[1] + q0_cost <= 2331:
            grouped[row[3]].append(row)
    return grouped

q0_by_count=defaultdict(list)
for side in q0:
    q0_by_count[side[2]].append(side)

pairs_count_compatible = 0
pairs_prequalified = 0
solution_count = 0
h2_survivors = 0
least_abs_h2_residual = None
histogram = Counter()
max_q0 = -1
best = None
# Quotient global sign exchange by n+ <= n-; when n+==n-,
# both named side orders remain represented, as intended.
for nplus in range(1,8):
    for nminus in range(nplus,8):
        for a in q0:
            if a[1] + min_mass[nplus] > 2331:
                continue
            kminus = nplus + a[2] - nminus
            for b in q0_by_count[kminus]:
                pairs_count_compatible += 1
                if (a[4]&b[4]) or b[1]+min_mass[nminus]>2331:
                    continue
                pairs_prequalified += 1
                plus = allowed_vertical(nplus,a[1])
                minus = allowed_vertical(nminus,b[1])
                target = b[3] - a[3]
                for reciprocal,rows_plus in plus.items():
                    rows_minus=minus.get(reciprocal-target,())
                    for vplus in rows_plus:
                        for vminus in rows_minus:
                            if vplus[4] & vminus[4]:
                                continue
                            solution_count += 1
                            second_plus = sum((Fraction(1,(17*atoms[i][0]+atoms[i][1])**2) for i in vplus[0]),Fraction(0))
                            second_plus += sum((Fraction(c,j*j) for j,c in enumerate(a[0],1)),Fraction(0))
                            second_minus = sum((Fraction(1,(17*atoms[i][0]+atoms[i][1])**2) for i in vminus[0]),Fraction(0))
                            second_minus += sum((Fraction(c,j*j) for j,c in enumerate(b[0],1)),Fraction(0))
                            h2_residual = second_plus - second_minus
                            if h2_residual == 0:
                                h2_survivors += 1
                            elif least_abs_h2_residual is None or abs(h2_residual) < least_abs_h2_residual:
                                least_abs_h2_residual = abs(h2_residual)
                            k = a[2] + b[2]
                            histogram[k] += 1
                            if k > max_q0:
                                max_q0, best = k,(nplus,nminus,a,b,vplus,vminus)

assert pairs_count_compatible == 1944619
assert pairs_prequalified == 167928
assert solution_count == 333
assert h2_survivors == 0
assert least_abs_h2_residual == Fraction(1,33075)
assert max_q0 == 11
assert dict(sorted(histogram.items())) == {
    0:74,1:3,2:44,3:33,4:58,5:44,6:36,7:16,8:13,9:5,10:4,11:3}

nplus,nminus,a,b,vplus,vminus=best
def vr(row): return [[atoms[i][0],atoms[i][1]] for i in row[0]]
def qr(row): return [[j,k] for j,k in enumerate(row[0],1) if k]
assert not(vplus[4]&vminus[4]) and not(a[4]&b[4])
assert nplus+a[2] == nminus+b[2]
assert vplus[3]+a[3] == vminus[3]+b[3]
assert vplus[1]+a[1]<=2331 and vminus[1]+b[1]<=2331
certificate={
    "schema":"T6_P17_Q14_H012_EMPTY_CERT_V1",
    "task_id":"RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND",
    "scope":"P17_Q14_SPLIT7_7_H0_H1_EXACT_BUDGET_NAMED_SUPPORT_DISJOINT",
    "vertical_named_atoms":len(atoms),
    "vertical_side_rosters":len(rosters),
    "unordered_vertical_disjoint_pairs":prior_disjoint,
    "q0_side_multisets_cost_le_292":len(q0),
    "q0_pair_loop_count_H0":pairs_count_compatible,
    "q0_pairs_H0_budget_disjoint":pairs_prequalified,
    "complete_H0_H1_solutions_nplus_le_nminus":solution_count,
    "q0_total_count_histogram":dict(sorted(histogram.items())),
    "sharp_max_q0_occurrences":max_q0,
    "H2_exact_survivors":h2_survivors,
    "min_abs_scaled_second_reciprocal_residual":str(least_abs_h2_residual),
    "witness":{
        "positive_vertical":vr(vplus),"negative_vertical":vr(vminus),
        "positive_q0":qr(a),"negative_q0":qr(b),
        "mass_positive":vplus[1]+a[1],"mass_negative":vminus[1]+b[1],
        "H0_both":nplus+a[2],
        "scaled_reciprocal_H1_both":str(vplus[3]+a[3]),
        "H1_both":str(Fraction(nplus+a[2])-(vplus[3]+a[3])/17),
        "q0_occurrences_total":a[2]+b[2]
    },
    "status":"AUTHOR_EXACT_FINITE_VERIFIED_UNREVIEWED_NOT_ADMITTED",
    "unresolved":["OTHER_Q14_P17_VALUATION_CLASSES","LOWER_PRIME_COMPLETION","GLOBAL_T6"]
}
print(json.dumps(certificate,indent=2,ensure_ascii=False))
