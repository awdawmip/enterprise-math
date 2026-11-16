"""X6 native signed six-axis BRC bivariate shell mass certificate.

Scientific input: pinned P000 V5, pure signed-unit-axis coordinate adjacency.
No final Cell address encoding, signed branch cancellation, or physical state model is assumed.
"""
from collections import defaultdict
from math import comb, factorial, isqrt
import json


def coefficient_dp(dim: int, square_norm: int):
    """(G,T,support) -> (distinct signed endpoints, shortest natural path count)."""
    states = {(0, 0, 0): (1, 1)}
    for _ in range(dim):
        following = defaultdict(lambda: (0, 0))
        for (q, t, support), (count, mass) in states.items():
            for a in range(isqrt(square_norm-q)+1):
                factor = 2 if a else 1
                key = (q+a*a, t+a, support + int(a != 0))
                prev_count, prev_mass = following[key]
                following[key] = (prev_count + factor*count,
                                  prev_mass + factor*mass*comb(t+a, a))
        states = dict(following)
    return {(t, support): value for (q,t,support), value in states.items() if q == square_norm}


def independent_endpoint_enumeration(dim: int, square_norm: int):
    result = defaultdict(lambda: (0, 0))
    def visit(prefix, remainder):
        if len(prefix) == dim:
            if remainder == 0:
                t = sum(map(abs, prefix))
                s = sum(a != 0 for a in prefix)
                denominator = 1
                for a in prefix:
                    denominator *= factorial(abs(a))
                mass = factorial(t) // denominator
                key = (t,s)
                count0, mass0 = result[key]
                result[key] = (count0+1, mass0+mass)
            return
        radius = isqrt(remainder)
        for a in range(-radius, radius+1):
            visit(prefix+[a], remainder-a*a)
    visit([], square_norm)
    return dict(result)


def stirling2(n, k):
    row = [0]*(k+1)
    row[0]=1
    for j in range(1,n+1):
        following=[0]*(k+1)
        for b in range(1,min(j,k)+1):
            following[b]=b*row[b]+row[b-1]
        row=following
    return row[k]


def p022_sc_shell_total(dim, radius):
    return sum(comb(dim,k)*2**k*factorial(k)*stirling2(radius,k)
               for k in range(1,min(dim,radius)+1)) if radius else 1


def run():
    dimension, q = 6,25
    exact=coefficient_dp(dimension,q)
    independently=independent_endpoint_enumeration(dimension,q)
    if exact != independently:
        raise ArithmeticError('independent six-axis endpoint enumeration differs from coefficient DP')
    table=[]
    for (t,s),(count,mass) in sorted(exact.items()):
        table.append({'shortest_length_T':t,'nonzero_axes':s,
                      'signed_endpoints':count,'natural_BRC_mass':mass})
    count=sum(r['signed_endpoints'] for r in table)
    mass=sum(r['natural_BRC_mass'] for r in table)
    covered_count=sum(r['signed_endpoints'] for r in table if r['nonzero_axes']<=2)
    covered_mass=sum(r['natural_BRC_mass'] for r in table if r['nonzero_axes']<=2)
    l1_radius5=p022_sc_shell_total(dimension,5)
    expected=(7812,2538954612,132,4212,106452)
    if (count,mass,covered_count,covered_mass,l1_radius5)!=expected:
        raise ArithmeticError('cross-check against source-pinned R063 or P022 failed')
    if sorted({r['shortest_length_T'] for r in table})!=[5,7,9,11]:
        raise ArithmeticError('G=25 six-axis T support mismatch')
    return {'schema':'X6_P022_QUADRATIC_L1_JOINT_SHELL_CERTIFICATE_V1',
            'dimensions':6,'quadratic_G':25,
            'method_1':'exact iterative multinomial coefficient DP',
            'method_2':'independent signed-endpoint recursive enumeration',
            'table_by_shortest_length_and_support':table,
            'quadratic_shell':{'endpoints':count,'natural_BRC_mass':mass},
            'support_at_most_two':{'endpoints':covered_count,'natural_BRC_mass':covered_mass},
            'support_above_two':{'endpoints':count-covered_count,'natural_BRC_mass':mass-covered_mass},
            'p022_L1_radius_5_shell_mass':l1_radius5,
            'G25_intersect_L1_5':{'endpoints':12,'natural_BRC_mass':12},
            'comparison':'P022 L1 aggregate is not X6 quadratic G shell aggregate',
            'evidence_status':'AUTHOR_COMPUTED_EXACT_NOT_DRIVER_REVIEWED_NOT_ADMITTED'}

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
