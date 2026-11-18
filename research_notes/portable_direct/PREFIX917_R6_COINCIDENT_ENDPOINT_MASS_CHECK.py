#!/usr/bin/env python3
"""Independent exact counting for PREFIX-917; Python 3 standard library only."""
from collections import defaultdict
from pathlib import Path
import json

P = 32
LOW = (1 << 18) + 1
HIGH = (1 << 19) - 1


def coefficient(p, m):
    assert m > 1 and (m & 1) == 1
    return sum((p - d) * (int(((1 << d)-1) % m == 0) +
                          int(((1 << d)+1) % m == 0)) for d in range(1, p))


def brute_same_initial(p, m):
    n = 1 << p
    return sum(1 for x in range(n) for i in range(p)
               for j in range(i+1, p)
               if ((x ^ (1 << i)) - (x ^ (1 << j))) % m == 0)


def brute_same_terminal(p, m):
    n = 1 << p
    return sum(1 for y in range(n) for i in range(p)
               for j in range(i+1, p)
               if ((y ^ (1 << i)) - (y ^ (1 << j))) % m == 0)


def factor(n):
    fs = []
    z = n
    q = 2
    while q*q <= z:
        if z % q == 0:
            e = 0
            while z % q == 0:
                z //= q
                e += 1
            fs.append((q,e))
        q += 1 if q == 2 else 2
    if z > 1:
        fs.append((z,1))
    return fs


def divisors_from_factors(fs):
    result = [1]
    for q,e in fs:
        result = [z*q**t for z in result for t in range(e+1)]
    return result


def interval_by_factor(p, low, high):
    weights = defaultdict(int)
    causes = defaultdict(list)
    for d in range(1,p):
        for sign in [-1,1]:
            number = (1<<d)+sign
            for m in divisors_from_factors(factor(number)):
                if low <= m <= high and m%2 == 1:
                    weights[m] += p-d
                    causes[m].append([d, sign])
    return weights, causes


def main():
    checks = 0
    for p in range(2,9):
        n = 1<<p
        for m in range(3,n,2):
            predicted = (n//2)*coefficient(p,m)
            assert brute_same_initial(p,m) == predicted, ('same_initial',p,m)
            assert brute_same_terminal(p,m) == predicted, ('same_terminal',p,m)
            checks += 2
    first = {m:coefficient(P,m) for m in range(LOW,HIGH+1,2)}
    nonzero = {m:w for m,w in first.items() if w}
    second, causes = interval_by_factor(P,LOW,HIGH)
    assert nonzero == dict(second)
    assert len(first)==131072 and len(nonzero)==24
    assert sum(nonzero.values())==134
    n = 1<<P
    cert = {
        'schema':'PREFIX917_EXACT_COINCIDENT_ENDPOINT_MASS_V1',
        'p':P,'N':n,'strict_19_bit_odd_moduli':[LOW,HIGH],
        'modulus_count':len(first),'exceptional_modulus_count':len(nonzero),
        'sum_of_weighted_differences':sum(nonzero.values()),
        'small_state_direct_checks':checks,
        'factor_divisor_method_agrees':True,
        'per_one_fixed_other_modulus_same_start_mass':(n//2)*sum(nonzero.values()),
        'all_ordered_modulus_pairs_same_start_mass':len(first)*(n//2)*sum(nonzero.values()),
        'all_ordered_modulus_pairs_same_end_mass':len(first)*(n//2)*sum(nonzero.values()),
        'combined_disjoint_mass_over_all_ordered_modulus_pairs':2*len(first)*(n//2)*sum(nonzero.values()),
        'exceptional_moduli': [{'m':m,'weight':w,'collision_mass_for_one_other_port':(n//2)*w,'divisor_causes':causes[m]} for m,w in sorted(nonzero.items())],
        'explicit_example':{'a':'any positive modulus','b':262145,'two_trajectories':[[1,0,0],[1,262145,18]],'start_state':1,'different_source_bits':[0,18]},
    }
    print(json.dumps({k:v for k,v in cert.items() if k!='exceptional_moduli'},indent=2))
    print('EXCEPTIONAL_LIST',[(t['m'],t['weight']) for t in cert['exceptional_moduli']])
    with Path(__file__).with_name('PREFIX917_R6_COINCIDENT_ENDPOINT_MASS_RESULTS.json').open('w',encoding='utf-8') as f:
        json.dump(cert,f,indent=2,ensure_ascii=False);f.write('\n')


if __name__=='__main__':
    main()
