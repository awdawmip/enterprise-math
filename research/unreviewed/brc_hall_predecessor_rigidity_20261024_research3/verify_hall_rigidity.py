#!/usr/bin/env python3
"""Exact finite certificate for K_r=H in one fixed 4-label BRC observer.

Author-side mathematical checker, Python 3 standard library only.
The infinite statement also requires the Hall hereditary scaling proof
spelled out in the accompanying paper.
"""
from functools import lru_cache
from itertools import product
import json

ACT = (0, 2, 3)
W = ((1, 665, 1, 333), (333, 333, 1, 333), (1, 1, 1, 997))
DEN = 1000
EDGES = ((0, 1), (1, 2), (1, 3), (2, 3))
DEG = tuple(sum(i in e for e in EDGES) for i in range(4))
MAX_AXIS = (16, 9, 690)

# The exact threshold T(a,b) is the least k>=0 such that H(a,b,k) holds.
# The pure-axis thresholds prove H outside this finite box.
EXPECTED_ROWS = (
 (690,684,676,661,635,588,503,354,111),
 (682,670,649,613,546,427,226,0,0),
 (661,632,580,486,323,61,0,0,0),
 (608,534,403,185,0,0,0,0,0),
 (467,289,8,0,0,0,0,0,0),
 (140,0,0,0,0,0,0,0,0),
 (1,0,0,0,0,0,0,0,0),
 (1,0,0,0,0,0,0,0,0),
 (1,0,0,0,0,0,0,0,0),
 (1,0,0,0,0,0,0,0,0),
 (1,0,0,0,0,0,0,0,0),
 (1,0,0,0,0,0,0,0,0),
 (1,0,0,0,0,0,0,0,0),
 (1,0,0,0,0,0,0,0,0),
 (1,0,0,0,0,0,0,0,0),
 (1,0,0,0,0,0,0,0,0),
)

@lru_cache(maxsize=None)
def integer_certificate(c):
    """Hall margins and step numerators, common denominator DEN^(|c|+1)."""
    single = [__import__('math').prod(W[a][i] ** c[a] for a in range(3)) for i in range(4)]
    pair = [__import__('math').prod((W[a][i] + W[a][j]) ** c[a] for a in range(3)) for i,j in EDGES]
    margins = []
    step_numerators = []
    for a in range(3):
        demand = [DEG[i] * (DEN - W[a][i]) * single[i] for i in range(4)]
        capacity = [(DEN - W[a][i] - W[a][j]) * pair[e]
                    for e, (i,j) in enumerate(EDGES)]
        for s in range(1,16):
            near_capacity = sum(capacity[e] for e,(i,j) in enumerate(EDGES)
                                if s & ((1<<i) | (1<<j)))
            subset_demand = sum(demand[i] for i in range(4) if s & (1<<i))
            margins.append(near_capacity-subset_demand)
        step_numerators.append(sum(demand)-sum(capacity))
    return tuple(margins), tuple(step_numerators)

def hall(c):
    return min(integer_certificate(c)[0]) >= 0

def exact_threshold(a,b):
    lo,hi=0,MAX_AXIS[2]
    while lo<hi:
        mid=(lo+hi)//2
        if hall((a,b,mid)): hi=mid
        else: lo=mid+1
    assert hall((a,b,lo))
    if lo: assert not hall((a,b,lo-1))
    return lo

def verify():
    assert DEG == (1,3,2,2)
    for axis, n in enumerate(MAX_AXIS):
        c=lambda k: tuple(k if j==axis else 0 for j in range(3))
        assert hall(c(n)) and not hall(c(n-1))
    # By the exact Hall hereditary scaling theorem, H is up-closed.
    # Therefore three verified axes bound every failure within the finite box.
    T = {(a,b): exact_threshold(a,b) for a in range(MAX_AXIS[0])
         for b in range(MAX_AXIS[1])}
    rows = tuple(tuple(T[a,b] for b in range(MAX_AXIS[1]))
                 for a in range(MAX_AXIS[0]))
    assert rows == EXPECTED_ROWS
    # Extend thresholds to the two proven safe boundary faces.
    def threshold(a,b):
        return 0 if a>=MAX_AXIS[0] or b>=MAX_AXIS[1] else T[a,b]
    maximal_failures=[]
    for a in range(MAX_AXIS[0]):
        for b in range(MAX_AXIS[1]):
            k=T[a,b]-1
            if k<0: continue
            c=(a,b,k)
            # By monotonicity in k, c is the highest excluded element
            # of its (a,b) column. It is maximal globally iff +e0,+e2 are H.
            if threshold(a+1,b)<=k and threshold(a,b+1)<=k:
                assert not hall(c)
                assert all(hall(tuple(c[j]+(j==u) for j in range(3)))
                           for u in range(3))
                maximal_failures.append(c)
    assert len(maximal_failures)==31
    exceptions=[]
    for c in maximal_failures:
        step=integer_certificate(c)[1]
        # Action 0 gives a positive delta except at one pure action-0 vertex.
        witness_index=2 if c==(15,0,0) else 0
        assert step[witness_index] > 0, (c,step)
        exceptions.append({'counts':list(c),'strict_positive_next_action':ACT[witness_index]})
    assert sum(T.values())==14102  # including some n<2 non-H boundary artifacts
    return {'schema':'EM_BRC_FIXED_MODEL_HALL_PREDECESSOR_RIGIDITY_V1',
        'global_knowledge_read_pin':'7c1187e2493cbf4a087a013bf4cfd4580e7027b6',
        'enterprise_math_source_read_pin':'90524eb9a43b8733acb3962ba905a2755de357b1',
        'arithmetic':'integer exact, common denominator 1000^(n+1)',
        'model':{'actions':list(ACT),'weights':[list(x) for x in W],
                 'good_edges':[list(x) for x in EDGES]},
        'pure_axis_first_hall':list(MAX_AXIS),
        'threshold_rows': [list(row) for row in rows],
        'non_hall_integer_states_in_finite_box':sum(T.values()),
        'maximal_non_hall_states':exceptions,
        'maximal_non_hall_count':len(exceptions),
        'maximal_non_hall_with_all_negative_next_increments':0,
        'theorem':'For every c with |c|>=2, K_1=K_0; hence K_r=K_0 for all r>=0',
        'scope':'fixed four-label positive three-action auxiliary observer only',
        'review':'AUTHOR_SIDE_EXACT_COMPUTATION_NOT_ADMITTED'}

if __name__=='__main__':
    print(json.dumps(verify(),indent=2,ensure_ascii=False))
