#!/usr/bin/env python3
"""R70 exact independent arithmetic certificate for the conditional BRC star-moment model."""
from fractions import Fraction
from itertools import product
import json

WEIGHTS = (50, 1, 1, 1)
D = 4
PAIRS = [(i,j) for i in range(D) for j in range(i+1,D)]

def q(a):
    return max(sum(x for x in a if x > 0), -sum(x for x in a if x < 0))

def moment_differences(a):
    return (0,) + tuple(sum(a[d-2]*(d**t-d) for d in range(2,D+1)) for t in range(2,D+1))

def pair_radius(a, w=WEIGHTS):
    z = moment_differences(a)
    return max(Fraction(abs(z[j]-z[i]), 2*(w[i]+w[j])) for i,j in PAIRS)


def finite_min(p):
    best = None
    winning = []
    tested = 0
    for a in product(range(-p,p+1), repeat=D-1):
        if not 0 < q(a) <= p:
            continue
        tested += 1
        score = pair_radius(a)
        if best is None or score < best:
            best, winning = score, [a]
        elif score == best:
            winning.append(a)
    return dict(p=p, feasible_vectors=tested, optimum=str(best), witnesses=[list(x) for x in winning], witness_q=[q(x) for x in winning])

EXPECTED = {4:Fraction(3), 5:Fraction(2), **{p:Fraction(3,2) for p in range(6,11)}}
rows = [finite_min(p) for p in range(4,11)]
for r in rows:
    assert Fraction(r['optimum']) == EXPECTED[r['p']], r

# Under 1/2 noise, all contrasts among the three cheap channels must vanish.
# Equal contrasts z2=z3=z4=C force (a2,a3,a4) = C*(3,-4/3,1/4).
# Integrality => 12 | C, and q(a)=39*|C|/12.
a_half = (10,-5,1)
a_plateau = (36,-16,3)
assert moment_differences(a_half) == (0,2,0,2)
assert moment_differences(a_plateau) == (0,12,12,12)
assert (q(a_half), pair_radius(a_half)) == (11,Fraction(1,2))
assert (q(a_plateau), pair_radius(a_plateau)) == (39,Fraction(2,17))
assert all((3*c)%1 == 0 for c in moment_differences(a_half))

# Exhaustive arithmetic sanity check at the two analytically protected transitions.
for p, expected in [(11,Fraction(1,2)), (12,Fraction(1,2)), (13,Fraction(1,2))]:
    row=finite_min(p)
    assert Fraction(row['optimum']) == expected

out = {
 'schema':'X6_R70_WEIGHTED_CONE_D4_CERTIFICATE_V1',
 'frozen_p000_commit':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'weights':list(WEIGHTS),
 'target':'recover high degree histogram c2,c3,c4 with one unknown shared bias',
 'radius_definition':'0.5*max_ij abs(z_i-z_j)/(w_i+w_j), z_t=sum_d a_d*(d**t-d)',
 'finite_domain':'all nonzero integer (a2,a3,a4) with max(sum positive, abs(sum negative)) <=p, p=4..10',
 'finite_checks':rows,
 'analytic_staircase':[
    {'p':'4','radius':'3'},
    {'p':'5','radius':'2'},
    {'p':'6..10','radius':'3/2'},
    {'p':'11..38','radius':'1/2'},
    {'p':'39..infinity','radius':'2/17'}
 ],
 'analytic_witnesses':[
     {'a':list(a_half),'q':11,'z':list(moment_differences(a_half)),'eta':str(pair_radius(a_half))},
     {'a':list(a_plateau),'q':39,'z':list(moment_differences(a_plateau)),'eta':str(pair_radius(a_plateau))}
 ],
 'proof_status':'finite_exact_checks_plus_analytic_reduction; not independent review',
 'computation_status':'PASS'
}
with open('/mnt/data/x6_r70_weighted_cone_d4_results.json','w',encoding='utf-8') as f:
    json.dump(out,f,ensure_ascii=False,indent=2)
    f.write('\n')
print(json.dumps({'finite_counts':[(r['p'],r['feasible_vectors'],r['optimum'],len(r['witnesses'])) for r in rows], 'plateau':'PASS','status':'PASS'},indent=2))
