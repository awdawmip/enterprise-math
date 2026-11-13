#!/usr/bin/env python3
"""R757 exact V39 source-labelled bow-tie three-packet closure check; Python standard library."""
from collections import Counter
from itertools import permutations, product
from fractions import Fraction
import json
ID = (0, 1, 2)
P = list(permutations(range(3)))
def mul(p, q):
    """Function composition p after q."""
    return tuple(p[q[i]] for i in range(3))
def inverse(p):
    return tuple(p.index(i) for i in range(3))
def holonomy(order, labels):
    h = ID
    for block in order:  # V39: h(gamma;r)=h(r) o h(gamma)
        h = mul(labels[block], h)
    return h
A = (0, 2, 1)  # actual V37 source loop A
B = (1, 0, 2)  # actual V37 source loop B
C = mul(inverse(A), inverse(B))  # C = B^-1;A^-1
labels = dict(A=A, B=B, C=C)
current = dict(A=(1,0), B=(0,1), C=(-1,-1))
expansion = dict(A=('A+',), B=('B+',), C=('B-','A-'))
rows=[]
for seq in permutations('ABC'):
    j=tuple(sum(current[k][axis] for k in seq) for axis in (0,1))
    hist=sum((Counter(expansion[k]) for k in seq), Counter())
    assert j==(0,0)
    assert hist == Counter({'A+':1, 'A-':1, 'B+':1, 'B-':1})
    rows.append(dict(order=''.join(seq), current=list(j),
                     frame=list(holonomy(seq,labels)), occurrences=dict(sorted(hist.items()))))
out={r['order']:tuple(r['frame']) for r in rows}
assert all(out[k]==ID for k in ('ABC','BCA','CAB'))
assert all(out[k]!=ID for k in ('ACB','BAC','CBA'))
assert Counter(out.values()) == Counter({(0,1,2):3,(1,2,0):2,(2,0,1):1})
group_pairs=Counter()
for a,b in product(P,repeat=2):
    c=mul(inverse(a),inverse(b))
    seq_h={''.join(order): holonomy(order,{'A':a,'B':b,'C':c})
           for order in permutations('ABC')}
    assert all(seq_h[k]==ID for k in ('ABC','BCA','CAB'))
    commute=mul(a,b)==mul(b,a)
    assert all((seq_h[k]==ID)==commute for k in ('ACB','BAC','CBA'))
    group_pairs['commuting' if commute else 'noncommuting']+=1
    group_pairs['distinct_endpoints_'+str(len(set(seq_h.values())))]+=1
assert group_pairs['commuting']==18
assert group_pairs['noncommuting']==18
assert sum((Fraction(v,6) for v in Counter(out.values()).values()),Fraction(0,1))==1
print(json.dumps({'status':'R757_V39_BOWTIE_EXACT_PASS','rows':rows,
    'fiber':{','.join(map(str,k)):v for k,v in Counter(out.values()).items()},
    'S3_pairs':dict(group_pairs),
    'scope':'V39 completed based macro-packets; matched V29 TRANSFER occurrence; not primitive force PASS'},indent=2,sort_keys=True))
