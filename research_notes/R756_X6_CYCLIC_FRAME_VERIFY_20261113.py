#!/usr/bin/env python3
"""R756 exact finite-group/S3 conjugacy-kernel checker, Python stdlib only."""
from itertools import permutations, product
from collections import Counter, defaultdict
from fractions import Fraction
import json

G = list(permutations(range(3)))
e = (0, 1, 2)

def mul(a, b):
    return tuple(a[b[i]] for i in range(3))

def inv(a):
    return tuple(a.index(i) for i in range(3))

def conj_class(z):
    return frozenset(mul(mul(inv(g), z), g) for g in G)

patterns = Counter()
by_size = defaultdict(Counter)
for a, b, c in product(G, repeat=3):
    z = mul(mul(a, b), c)
    t = mul(a, b)
    w = (z, mul(mul(b, c), a), mul(mul(c, a), b))
    assert w[1] == mul(mul(inv(a), z), a)
    assert w[2] == mul(mul(inv(t), z), t)
    k = len(conj_class(z))
    assert all(y in conj_class(z) for y in w)
    pat = tuple(sorted(Counter(w).values(), reverse=True))
    patterns[pat] += 1
    by_size[k][pat] += 1

assert patterns == {(3,):66,(2,1):126,(1,1,1):24}
assert dict(by_size[1]) == {(3,):36}
assert dict(by_size[2]) == {(3,):18,(2,1):54}
assert dict(by_size[3]) == {(3,):12,(2,1):72,(1,1,1):24}

K={z:{y:Fraction(1,3)*(y==z)+Fraction(2,3*len(conj_class(z)))*(y in conj_class(z)) for y in G} for z in G}
assert all(sum(K[z].values())==1 for z in G)
assert all(K[z][y]==K[y][z] for z in G for y in G)
Q={z:{y:Fraction(int(z==y)) for y in G} for z in G}
for n in range(1,7):
    Q={z:{y:sum(Q[z][v]*K[v][y] for v in G) for y in G} for z in G}
    for z in G:
        k=len(conj_class(z))
        for y in G:
            expected=Fraction(int(y in conj_class(z)),k)+Fraction(1,3)**n*(Fraction(int(z==y))-Fraction(int(y in conj_class(z)),k))
            assert Q[z][y]==expected

assert sum(patterns.values())==216
collision=sum(Fraction(count,216)*sum(Fraction(v,3)**2 for v in pat) for pat,count in patterns.items())
assert collision==Fraction(2,3)
report={
 'schema':'R756_S3_CONJUGACY_BRC_EXACT_V1',
 'group_size':len(G),
 'checked_triples':216,
 'conjugacy_class_sizes':{'identity':1,'transpositions':3,'three_cycles':2},
 'forward_output_multiplicity_patterns':{'3':66,'2+1':126,'1+1+1':24},
 'by_class_size':{str(k):{'+'.join(map(str,p)):v for p,v in sorted(x.items())} for k,x in sorted(by_size.items())},
 'necessary_fixed_length_repair_bits':{'constant':0,'two_distinct':1,'three_distinct':2},
 'independent_uniform_schedule_collision_probability':str(collision),
 'kernel_eigenvalues':{'1':3,'1/3':3},
 'exact_kernel_power_checks':'n=1..6, all 36 entries each',
 'exact_arithmetic':'fractions.Fraction; no numerical tolerance',
 'formal_native_v39_event_admission':'NOT_TESTED',
 'proof_scope':'finite groups general; S3 complete enumeration; conditional V39 bridge'
}
print(json.dumps(report,indent=2,ensure_ascii=False,sort_keys=True))
