#!/usr/bin/env python3
"""Independent small exact crosschecks; none replaces a universal paper proof."""
from itertools import product
from pathlib import Path
import json

# A sieve and interval-event construction, independent of the author's
# trial-division/direct per-prime state selection implementation.
B = 1009
sieve = bytearray(b'\x01') * (B + 1)
sieve[0:2] = b'\x00\x00'
for p in range(2, B + 1):
    if sieve[p]:
        for j in range(p*p, B + 1, p):
            sieve[j] = 0
primes = [p for p in range(5, B+1) if sieve[p]]
assert primes[-1] == 1009
T = [1, 2, 3, 4, 6, 9]
states = [{0} for _ in range(1001)]
for q in primes:
    for k,t in enumerate(T):
        lo = q*t
        hi = q*T[k+1]-1 if k+1<len(T) else 1000
        for h in range(max(1,lo),min(1000,hi)+1):
            states[h].add(t)
assert all((len(states[h]) == 7) == (45 <= h <= 62 or h >= 66)
           for h in range(1,1001))
assert states[27] == {0,1,2,3,4} and states[28] == {0,1,2,4}

# q_4 depends only on coordinate parities. Exhaust its complete 64-state
# quotient and all 64 offset-parity classes, rather than sampling Z^6.
bits = list(product((0,1), repeat=6))
def q4(x,a):
    return sum((u+v)**2 for u,v in zip(x,a)) % 4
zero = (0,)*6
unit = [tuple(int(i==j) for i in range(6)) for j in range(6)]
chosen = [zero] + unit[:5]
images = {tuple(q4(x,a) for a in chosen) for x in bits}
assert len(images) == 64
checked = 0
for d in bits:
    if not any(d) or sum(d)%2:
        continue
    for x in bits:
        y = tuple(u+v for u,v in zip(x,d))
        for a in bits:
            difference = (q4(y,a)-q4(x,a))%4
            asserted = (2*sum((u+v)*w for u,v,w in zip(x,a,d))+sum(d))%4
            assert difference == asserted
            checked += 1

report = {
    'reviewer': 'EM-REVIEW-58D6A2',
    'status': 'EXACT_SMALL_CHECKS_PASS',
    'nt': {'thresholds': [1,1000], 'prime_bound':1009,
           'capacity_27': len(states[27]), 'capacity_28':len(states[28]),
           'full_capacity_ranges_in_finite_domain':[[45,62],[66,1000]],
           'universal_tail_not_proved_by_this_scan':True},
    'native': {'m4_all_parity_states':64, 'six_probe_image_size':len(images),
               'all_even_nonzero_displacements':31,
               'exact_polarization_checks':checked,
               'universal_lower_bound_is_paper_argument':True},
    'old_scientific_runs_repeated':False,
    'lean_or_kernel_certificate':False
}
Path(__file__).with_name('independent_checks_result.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
