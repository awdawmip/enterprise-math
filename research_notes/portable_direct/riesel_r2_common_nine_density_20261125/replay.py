"""Exact weighted multivalued decision diagrams for R3 ninth-budget density."""
from functools import lru_cache
from itertools import product
from fractions import Fraction
from pathlib import Path
from math import gcd
from decimal import Decimal, localcontext
import json,sys
import zero_input as z

Z,J,U,T,L,V=z.Z,z.J,z.U,z.T,z.L,z.V
pool=list(dict.fromkeys(Z+J+T+L+V+U))
period={q:f for f,S in ((7,Z),(14,J),(35,U),(10,T),(28,L),(70,V)) for q in S}
def vv(q,b):return b%period[q]
patterns=z.patterns()
assert len(patterns)==47
zero_shapes=[[(tuple(z.GROUPS[G]),b,vv) for G,b in p['slots']] for p in patterns[5:]]
assert all(q in period for shape in zero_shapes for qs,_,_ in shape for q in qs)
eight_shapes=[]
for c in z.ROWS:
    rows=[(Z,b,vv) for b in z.ROWS if b!=c]
    eight_shapes += [rows+[(J,b,vv) for b in (c,c+7)]]
    if c in (1,5):eight_shapes += [rows+[(U,b,vv) for b in sorted(z.A) if b%7==c]]
EXTRA=[(8, [193, 22253377]), (9, [262657, 87211, 246241, 279073]), (12, [577, 487824887233]), (15, [631, 23311, 18837001, 181, 54001, 29247661]), (18, [33975937, 138991501037953]), (24, [1153, 6337, 278452876033, 38941695937]), (30, [168692292721, 469775495062434961])]
SPLIT=[[(8, 0), (8, 4), (12, 2)], [(8, 0), (12, 2), (24, 20)], [(8, 2), (8, 6), (12, 8)], [(8, 2), (12, 8), (24, 14)], [(8, 4), (12, 2), (24, 8)], [(8, 6), (12, 8), (24, 2)], [(9, 2), (9, 5), (18, 8)], [(9, 2), (9, 8), (18, 14)], [(9, 2), (18, 8), (18, 14)], [(9, 5), (9, 8), (18, 2)], [(9, 5), (18, 2), (18, 8)], [(9, 8), (18, 2), (18, 14)], [(10, 0), (10, 2), (15, 11)], [(10, 0), (10, 2), (30, 26)], [(10, 0), (10, 6), (15, 2)], [(10, 0), (10, 6), (30, 2)], [(10, 0), (15, 2), (15, 11)], [(10, 0), (15, 2), (30, 26)], [(10, 0), (15, 11), (30, 2)], [(10, 0), (30, 2), (30, 26)], [(10, 2), (10, 6), (15, 5)], [(10, 2), (10, 6), (30, 20)], [(10, 2), (15, 5), (15, 11)], [(10, 2), (15, 5), (30, 26)], [(10, 2), (15, 11), (30, 20)], [(10, 2), (30, 20), (30, 26)], [(10, 6), (15, 2), (15, 5)], [(10, 6), (15, 2), (30, 20)], [(10, 6), (15, 5), (30, 2)], [(10, 6), (30, 2), (30, 20)], [(12, 2), (12, 8)], [(12, 2), (24, 8), (24, 20)], [(12, 8), (24, 2), (24, 14)], [(15, 2), (15, 5), (30, 26)], [(15, 2), (15, 11), (30, 20)], [(15, 2), (30, 20), (30, 26)], [(15, 5), (15, 11), (30, 2)], [(15, 5), (30, 2), (30, 26)], [(15, 11), (30, 2), (30, 20)], [(9, 2), (9, 5), (9, 8)], [(9, 2), (9, 5), (18, 8), (18, 17)], [(9, 2), (9, 8), (18, 5), (18, 14)], [(9, 5), (9, 8), (18, 2), (18, 11)], [(10, 0), (10, 5), (15, 2), (15, 11)], [(10, 0), (15, 2), (15, 11), (30, 5)], [(10, 1), (10, 6), (15, 2), (15, 5)], [(10, 1), (15, 2), (15, 5), (30, 26)], [(10, 2), (10, 7), (15, 5), (15, 11)], [(10, 2), (15, 5), (15, 11), (30, 17)], [(10, 5), (15, 2), (15, 11), (30, 20)], [(10, 6), (15, 2), (15, 5), (30, 11)], [(10, 7), (15, 5), (15, 11), (30, 2)], [(15, 2), (15, 5), (15, 11)], [(15, 2), (15, 5), (30, 11), (30, 26)], [(15, 2), (15, 11), (30, 5), (30, 20)], [(15, 5), (15, 11), (30, 2), (30, 17)]]
for f,qs in EXTRA:
    pool.extend(qs)
    period.update((q,f) for q in qs)
by={f:tuple(q for q in pool if period[q]==f) for f in set(period.values())}
split_shapes=[[(by[f],b,vv) for f,b in t] for t in SPLIT]
shapes=zero_shapes+eight_shapes+split_shapes

used={q:set() for q in pool}
for shape in shapes:
    seen=set()
    for qs,b,cv in shape:
        pairs={(q,cv(q,b)) for q in qs}
        assert seen.isdisjoint(pairs),(shape,seen & pairs)
        seen|=pairs
        for q,v in pairs:used[q].add(v)
for q in pool:
    vals={-pow(2,-(4+6*b),q)%q for b in used[q]}|{pow(2,-(4+6*b),q) for b in used[q]}
    assert len(vals)==2*len(used[q]) and all(x for x in vals)

layout=sys.argv[1] if len(sys.argv)>1 else 'forward'
if layout=='alternate':
    blocks=(Z,J,T,L,V,U,*(tuple(qs) for _,qs in EXTRA))
    pool=list(dict.fromkeys(q for block in blocks for q in reversed(block)))
domains=[tuple(sorted(used[q]))+(None,) for q in pool]
weights=[(2,)*(len(d)-1)+(q-2*(len(d)-1),) for q,d in zip(pool,domains)]
qloc={q:i for i,q in enumerate(pool)}
N=len(pool)
nodes=[(N,()),(N,())]
unique={}
def node(i,children):
    if children.count(children[0])==len(children):return children[0]
    k=i,children
    j=unique.get(k)
    if j is None:
        j=len(nodes);nodes.append(k);unique[k]=j
    return j

@lru_cache(None)
def apply(op,a,b):
    if a>b:return apply(op,b,a)
    if a==b:return a
    if a<2:return (b if a==1 else 0) if op=='AND' else (b if a==0 else 1)
    i=min(nodes[a][0],nodes[b][0])
    ca=nodes[a][1] if nodes[a][0]==i else (a,)*len(domains[i])
    cb=nodes[b][1] if nodes[b][0]==i else (b,)*len(domains[i])
    return node(i,tuple(apply(op,x,y) for x,y in zip(ca,cb)))
@lru_cache(None)
def invert(a):
    if a<2:return 1-a
    i,children=nodes[a]
    return node(i,tuple(invert(c) for c in children))
@lru_cache(None)
def atom(q,b):
    i=qloc[q]
    return node(i,tuple(int(p==b) for p in domains[i]))
def disjoin(items):
    result=0
    for a in items:result=apply('OR',result,a)
    return result
def conjoin(items):
    result=1
    for a in items:result=apply('AND',result,a)
    return result

def make(shapes):
    if layout=='alternate':shapes=shapes[::-1]
    result=disjoin(conjoin(disjoin(atom(q,cv(q,b)) for q in qs) for qs,b,cv in s) for s in shapes)
    print('built',len(shapes),len(nodes),apply.cache_info(),file=sys.stderr)
    return result

eight=make(eight_shapes)
nine=make(zero_shapes)
all_common=apply('OR',eight,nine)
uplift=apply('AND',nine,invert(eight))
split_eight=make(split_shapes)
E8=apply('OR',eight,split_eight)
exact_nine_common=apply('AND',all_common,invert(E8))
overlap=apply('AND',uplift,split_eight)

total=[1]*(N+1)
for i in range(N-1,-1,-1):total[i]=pool[i]*total[i+1]
@lru_cache(None)
def weighted(a):
    if a<2:return a
    i,ch=nodes[a]
    ans=0
    for w,c in zip(weights[i],ch):
        j=nodes[c][0]
        assert j>i
        ans+=w*weighted(c)*(total[i+1]//total[j])
    return ans

def raw(a):
    return weighted(a)*(total[0]//total[nodes[a][0]])
def value(a):
    v=Fraction(raw(a),total[0])
    with localcontext() as ctx:
        ctx.prec=65
        dec=format(Decimal(v.numerator)/Decimal(v.denominator),'.55E')
    return {'numerator':str(v.numerator),'denominator':str(v.denominator),'decimal':dec}
print(json.dumps(dict(C8=value(eight),C9=value(all_common),C9_minus_C8=value(uplift),E8=value(E8),C9_exact_total9=value(exact_nine_common),C9local9_but_globally_le8=value(overlap),n_primes=N,groups={f:[q for q in pool if period[q]==f] for f in sorted(set(period.values()))},node_count=len(nodes)),indent=2))
