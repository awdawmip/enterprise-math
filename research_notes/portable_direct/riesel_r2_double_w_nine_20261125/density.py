"""Exact weighted multivalued decision diagrams for R3 ninth-budget density."""
from functools import lru_cache
from itertools import product
from fractions import Fraction
from pathlib import Path
from math import gcd
from decimal import Decimal, localcontext
import json,sys
import zero_input as z


D=json.loads(Path(__file__).with_name('templates.json').read_text())
group={int(h):tuple(qs) for h,qs in D['by_h'].items()}
Z,J,U,T,L,V=z.Z,z.J,z.U,z.T,z.L,z.V
pool=list(dict.fromkeys(q for h in (15,3,4,6,8,9,10,12,16,20,5,7,35) for q in group.get(h,())))
pool=list(dict.fromkeys((*pool,*J,*L,*V)))
assert set(pool)=={q for qs in group.values() for q in qs}|set((*J,*L,*V))
period={int(q):r['f'] for r in json.loads(Path(__file__).with_name('low_inventory.json').read_text()) for q in r['primeFactors']}
def vv(q,b):return b%period[q]
def ww(q,b):return vv(q,2+3*b)
double_shapes=[[(group[h],b,ww) for h,b in t if h!=2] for t in D['shapes']]
old_double=[double_shapes[i] for i,t in enumerate(D['shapes']) if len(t)<=4]
patterns=z.patterns()
assert len(patterns)==47
zero_shapes=[[(tuple(z.GROUPS[G]),b,vv) for G,b in p['slots']] for p in patterns[5:]]
eight_shapes=[]
for c in z.ROWS:
    rows=[(Z,b,vv) for b in z.ROWS if b!=c]
    eight_shapes += [rows+[(J,b,vv) for b in (c,c+7)]]
    if c in (1,5):eight_shapes += [rows+[(U,b,vv) for b in sorted(z.A) if b%7==c]]
shapes=zero_shapes+eight_shapes+double_shapes
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
    pool=pool[:-len(J+L+V)]+list(reversed(J+L+V))
    assert set(pool)==set(used)
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
    result=disjoin(conjoin(disjoin(atom(q,cv(q,b)) for q in qs) for qs,b,cv in s) for s in shapes)
    print('built',len(shapes),len(nodes),apply.cache_info(),file=sys.stderr)
    return result

eight=make(eight_shapes)
nine=make(zero_shapes)
common=apply('OR',eight,nine)
old=make(old_double)
E8=apply('OR',eight,old)
double=make(double_shapes)
partial=apply('OR',common,double)
exact_partial=apply('AND',partial,invert(E8))
exact_double=apply('AND',double,invert(E8))
common_overlap=conjoin((common,double,invert(E8)))
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
print(json.dumps(dict(C8=value(eight),E8=value(E8),D8=value(old),C9=value(common),D9=value(double),D9_exact=value(exact_double),C9_and_D9_exact=value(common_overlap),C9_or_D9_exact=value(exact_partial),n_primes=N,node_count=len(nodes),layout=layout),indent=2))
