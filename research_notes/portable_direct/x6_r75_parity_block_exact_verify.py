"""R75: exact integer checks for the conditional positive-count BRC star-moment observer.
The core is an explicitly typed degree-count/moment operation. This does not
simulate native X6 Cell/Link/Port dynamics or a physical heartbeat.
"""
import itertools
import json
from fractions import Fraction
from math import comb


def q(a):
    return max(sum(max(v, 0) for v in a), sum(max(-v, 0) for v in a))


def signature(a):
    D = len(a) + 1
    return [0] + [sum(v * (d**t - d) for d, v in enumerate(a, 2)) for t in range(2, D + 1)]


def target(D):
    return tuple((-1)**d * comb(D + 1, d + 1) for d in range(2, D + 1))


def cross_max(z):
    return max(abs(z[i]-z[j]) for i in range(len(z)) for j in range(len(z)) if (i-j)%2)


def pair_radius(z, x, y):
    w = [x if t % 2 else y for t in range(1, len(z)+1)]
    return max(Fraction(abs(z[j]-z[i]), 2*(w[i]+w[j]))
               for i in range(len(z)) for j in range(i+1, len(z)))


small_domains = {2: 2, 3: 5, 4: 11, 5: 8}
ratios = [(1,1),(1,1000),(1000,1),(3,17),(101,7)]
output = {
    'schema': 'X6_R75_PARITY_BLOCK_HETEROSCEDASTIC_CERTIFICATE_V1',
    'model': 'conditional positive-count BRC star-moment histogram; shared real offset',
    'exact_arithmetic': 'Python integer and fractions.Fraction',
    'tested_D': list(range(2, 13)),
    'small_domains': [],
    'witnesses': [],
    'sharp_boundary_samples': [],
}

for D in range(2, 13):
    a = target(D)
    z = signature(a)
    Q = 2**D-D-1
    assert q(a) == Q
    assert z == [0 if t % 2 else 2 for t in range(1, D+1)]
    for x,y in ratios:
        assert pair_radius(z,x,y) == Fraction(1,x+y)
    output['witnesses'].append({'D':D,'q':Q,'a':list(a),'z':z,'parity_weight_pairs_checked':len(ratios)})

for D, bound in small_domains.items():
    Q = 2**D-D-1
    total = 0
    feasible = 0
    low = 0
    boundary = 0
    witnessed = 0
    worst_below = 10**20
    for a in itertools.product(range(-bound, bound+1), repeat=D-1):
        if not any(a):
            continue
        total += 1
        qa = q(a)
        if qa > bound:
            continue
        feasible += 1
        z = signature(a)
        C = cross_max(z)
        assert C >= 2 and C%2 == 0
        if C == 2:
            boundary += 1
            assert a == target(D) or a == tuple(-v for v in target(D))
            assert qa == Q
        else:
            assert C >= 4
            if qa < Q:
                low += 1
                worst_below = min(worst_below, C)
                for x,y in ratios:
                    assert pair_radius(z,x,y) >= Fraction(2,x+y)
        if qa == Q and a == target(D):
            witnessed += 1
    output['small_domains'].append({'D':D,'q_limit':bound,'integer_boxes_examined':total,
         'q_feasible_nonzero':feasible,'cross_gap_two_candidates':boundary,
         'below_Q_count':low,'minimal_cross_gap_below_Q':None if low==0 else worst_below,
         'witness_inside_domain':bool(witnessed)})

for D,p,x,y in [(3,3,1,1000),(3,4,1,1000),(4,10,1,1000),(4,11,1,1000),(4,10,1000,1),(4,11,1000,1),(5,26,1,1000000),(6,57,17,101)]:
    z = signature(target(D))
    ans = {'D':D,'p':p,'w_odd':x,'w_even':y,'target_radius':str(Fraction(1,x+y))}
    if p >= q(target(D)):
        ans['witness_radius']=str(pair_radius(z,x,y))
        assert pair_radius(z,x,y)==Fraction(1,x+y)
    output['sharp_boundary_samples'].append(ans)

output['status']='PASS'
print(json.dumps(output,ensure_ascii=False,indent=2))
