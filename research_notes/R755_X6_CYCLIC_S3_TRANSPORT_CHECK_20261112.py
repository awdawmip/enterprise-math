#!/usr/bin/env python3
"""R755: exhaustive exact S3 algebra for R754's forward cyclic BRC frame kernel."""
from itertools import permutations, product
from collections import Counter
import json
G=tuple(permutations(range(3)))
I=(0,1,2)
def mul(x,y): return tuple(x[y[i]] for i in range(3))
def prod(a,b,c): return mul(mul(a,b),c)
def commute(a,b): return mul(a,b)==mul(b,a)
def order(x):
    n=1
    z=x
    while z!=I:
        z=mul(z,x)
        n+=1
    return n
count=Counter()
cyclic_by_order=Counter()
full_by_order=Counter()
reverse_multiplicities=Counter()
witness=None
for a,b,c in product(G,repeat=3):
    z=prod(a,b,c)
    cyclic=(prod(b,c,a)==z==prod(c,a,b))
    full=(len({prod(*[ (a,b,c)[i] for i in p]) for p in permutations(range(3))})==1)
    pairwise=all([commute(a,b),commute(a,c),commute(b,c)])
    centralizer=all(commute(z,x) for x in (a,b,c))
    assert cyclic==centralizer
    assert full==pairwise
    count["all"]+=1
    if cyclic:
        count["cyclic"]+=1
        cyclic_by_order[order(z)]+=1
    if full:
        count["full"]+=1
        full_by_order[order(z)]+=1
    if cyclic and not full:
        count["exception"]+=1
        assert z==I
        rev=[prod(a,c,b),prod(c,b,a),prod(b,a,c)]
        assert all(x!=I and order(x)==3 for x in rev)
        pattern=tuple(sorted(Counter(rev).values()))
        assert pattern==(1,2)
        reverse_multiplicities[str(pattern)]+=1
        if witness is None:
            witness={"a":a,"b":b,"c":c,"forward":[prod(a,b,c),prod(b,c,a),prod(c,a,b)],"reverse":rev}
assert count==Counter({"all":216,"cyclic":66,"full":48,"exception":18})
assert cyclic_by_order==Counter({1:36,2:12,3:18})
assert full_by_order==Counter({1:18,2:12,3:18})
assert reverse_multiplicities==Counter({"(1, 2)":18})
R={"schema":"R755_X6_CYCLIC_S3_FRAME_KERNEL_V1","status":"PASS",
"candidate_bridge_only":True,"S3_label_triples":count["all"],
"cyclic_frame_independent":count["cyclic"],
"all_order_frame_independent":count["full"],
"cyclic_only_noncommuting":count["exception"],
"cyclic_by_product_order":dict(cyclic_by_order),
"full_by_product_order":dict(full_by_order),
"reverse_multiplicities":dict(reverse_multiplicities),
"X6_signed_oriented_triads":320,
"X6_candidate_label_instances":320*count["all"],
"X6_cyclic_independent_instances":320*count["cyclic"],
"X6_all_order_independent_instances":320*count["full"],
"X6_cyclic_only_instances":320*count["exception"],
"witness":witness,"native_V39_packet_admitted":False}
print(json.dumps(R,ensure_ascii=False,sort_keys=True,indent=2))
