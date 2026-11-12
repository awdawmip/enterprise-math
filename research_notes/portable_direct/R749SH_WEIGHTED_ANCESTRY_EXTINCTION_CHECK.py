#!/usr/bin/env python3
"""R749SH weighted 8-mask ancestral extinction, exact Fraction checks."""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter, defaultdict
import json

MASKS = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
IDX = {m:i for i,m in enumerate(MASKS)}


def weight_matrix(p):
    A = Q(1+7*p, 8)
    B = Q(1-p, 8)
    R = [[Q(0) for _ in MASKS] for _ in MASKS]
    for m in MASKS:
        a,b,c=m
        for target, mass in [((b,c,a),A),((b,c,0),3*B),((c,b,0),4*B)]:
            R[IDX[m]][IDX[target]] += mass
    assert all(sum(row)==1 for row in R)
    assert R[0][0]==1
    return R


def solve_linear(a, v):
    m = len(v)
    w=[list(a[i])+[v[i]] for i in range(m)]
    for j in range(m):
        pivot=next(i for i in range(j,m) if w[i][j])
        w[j],w[pivot]=w[pivot],w[j]
        d=w[j][j]
        w[j]=[u/d for u in w[j]]
        for i in range(m):
            if i!=j:
                factor=w[i][j]
                w[i]=[t-factor*z for t,z in zip(w[i],w[j])]
    return [row[-1] for row in w]


def expected_vector(p):
    n = 7
    P=weight_matrix(p)
    B=[row[1:] for row in P[1:]]
    return solve_linear([[Q(int(i==j))-B[i][j] for j in range(n)] for i in range(n)], [Q(1)]*n)


def proposed(p):
    d=7*(1-p)*(1+p)*(7*p+9)
    return [
       24/(7*(1-p)),
       2*(7*p*p+5*p+12)/(7*(1-p)*(1+p)),
       2*(49*p**3+154*p*p+225*p+148)/d,
       2*(7*p+5)/(7*(1-p)),
       2*(49*p*p+126*p+113)/(7*(1-p)*(7*p+9)),
       (147*p**3+371*p*p+401*p+233)/d,
       (147*p**3+427*p*p+529*p+305)/d,
    ]


def independent_support_counts(steps):
    AX=range(6)
    sup=[frozenset(v) for v in combinations(AX,2)]
    ed=[(a,b) for a in sup for b in sup if len(a&b)==1]
    assert len(ed)==120
    for init in ed[:2]:
        current={(init,frozenset(init[0]|init[1])):1}
        for _ in range(steps):
            new=defaultdict(int)
            for (e,alive),mass in current.items():
                a,b=e
                for c in sup:
                    if len(c&b)!=1:continue
                    x=next(iter(c-b))
                    updated=(b&alive)|({x} if c==a^b and x in alive else set())
                    new[((b,c),frozenset(updated))]+=mass
            current=new
        tally=Counter()
        for (e,alive),mass in current.items():tally[len(alive)]+=mass
        assert sum(tally.values())==8**steps
        if init==ed[0]:return {str(k):tally[k] for k in range(4)}


assert independent_support_counts(1)=={'0':0,'1':0,'2':7,'3':1}
assert independent_support_counts(2)=={'0':0,'1':49,'2':14,'3':1}
assert independent_support_counts(3)=={'0':147,'1':343,'2':21,'3':1}

results={}
for p in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(9,10),Q(99,100)]:
    v=expected_vector(p)
    assert v==proposed(p)
    expected=(147*p**3+427*p*p+529*p+305)/(7*(1-p*p)*(7*p+9))
    assert v[-1]==expected
    R=weight_matrix(p)
    state=[Q(int(i==7)) for i in range(8)]
    survival=[]
    for step in range(9):
        survival.append(sum(state[1:]))
        state=[sum(state[j]*R[j][i] for j in range(8)) for i in range(8)]
    assert all(survival[i+1]<=survival[i] for i in range(8))
    results[str(p)]={'E_T':str(expected),'survival_probabilities_0_to_8':[str(x) for x in survival]}

assert expected_vector(Q(0))[-1]==Q(305,63)
assert expected_vector(Q(1,2))[-1]==Q(5557,525)
assert expected_vector(Q(9,10))[-1]==Q(1234133,20349)
print(json.dumps({'status':'PASS','parameters':results,
    'exact_all_p_formula':'(147p^3+427p^2+529p+305)/(7(1-p^2)(7p+9))',
    'p_to_one_limit_of_(1-p)_E_T':'44/7',
    'nonforced_three_step_extinction_lower_probability':'[3(1-p)/8]^3',
    'support_counts_per_start_m1':{'0':0,'1':0,'2':7,'3':1},
    'support_counts_per_start_m2':{'0':0,'1':49,'2':14,'3':1},
    'support_counts_per_start_m3':{'0':147,'1':343,'2':21,'3':1},
    'native_event_permission':False},indent=2,sort_keys=True))
