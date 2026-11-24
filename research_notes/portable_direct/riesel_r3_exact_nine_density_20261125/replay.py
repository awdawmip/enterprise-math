"""Exact weighted multivalued decision diagrams for R3 ninth-budget density."""
from functools import lru_cache
from itertools import product
from fractions import Fraction
from pathlib import Path
from math import gcd
from decimal import Decimal, localcontext
import json,sys
import zero_input as z

g=json.loads(Path(__file__).with_name('both_groups.json').read_text())['groups']
Z,K,J,U,T,L,V=z.Z,z.K,z.J,z.U,z.T,z.L,z.V
B8,D6,C10,R12,H20,F16=(tuple(g[s]) for s in ('B8','D6','C10','R12','H20','F16'))
assert set(g['Z7'])==set(Z) and set(g['G7'])==set(K)
assert set(B8)==set(z.B8) and set(D6)==set(z.D6) and set(C10)==set(z.C10)

# Exact mutually exclusive categories per q: v residue of hit or no hit.
def eff(q):
    x=1
    for d in range(1,841):
        x=2*x%q
        if x==1:return d//gcd(d,12)
    raise ValueError(q)
pool=list(dict.fromkeys(Z+K+J+T+L+V+U+B8+D6+C10+R12+H20+F16))
assert len(pool)==59 and all(gcd(q,z.S3)==1 for q in pool)
# A shape cannot use one prime twice if the requested phases disagree.
def vv(q,b):return b%eff(q)
def ww(q,b):return vv(q,2+3*b)
def tt(q,b):return ww(q,4*b)
zero_shapes=[[(tuple(z.GROUPS[G]),b,vv) for G,b in p['slots']] for p in z.patterns()]
B_shapes=[[(Z+K,b,ww) for b in (0,1,2,3,5)],
          [(B8,b,tt) for b in (0,1)],
          [(D6+R12,b,tt) for b in (0,2)],
          [(C10+H20,b,tt) for b in (0,2,4)]]
B_shapes += [[(B8,b,tt),(F16,1-b,tt),(F16,3-b,tt)] for b in (0,1)]
O_shapes=[]
eight_shapes=[[(gs,b,ww) for b in phases] for gs,phases in ((B8,(0,4)),(D6,(0,2)),(C10,(0,6,8)))]
for c in z.ROWS:
    rows=[(Z,b,vv) for b in z.ROWS if b!=c]
    bs=[c+7*j for j in range(3)]
    phase2=next(b for b in bs if b%3==2)
    O_shapes += [rows+[(K,phase2,vv),(K,b,vv)] for b in bs if b!=phase2]
    eight_shapes += [rows+[(J,b,vv) for b in (c,c+7)]]
    if c in (1,5):
        eight_shapes += [rows+[(U,b,vv) for b in sorted(z.A) if b%7==c]]
shapes=zero_shapes+B_shapes+O_shapes+eight_shapes
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
    blocks=(Z,K,J,T,L,V,U,B8,D6,C10,R12,H20,F16)
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

both=make(B_shapes)
one=make(O_shapes)
eight=make(eight_shapes)
zero_type1=make(zero_shapes[:5])
assert apply('AND',zero_type1,invert(one))==0
assert apply('AND',one,invert(both))==0
zero=make(zero_shapes)
target=apply('AND',apply('OR',both,zero),invert(eight))

def evaluate(a, state):
    while a>=2:
        i, children=nodes[a]
        phase=state.get(pool[i])
        domain=domains[i]
        a=children[domain.index(phase) if phase in domain else len(domain)-1]
    return bool(a)

def crosscheck():
    import random
    rng=random.Random(20261125)
    from math import lcm
    period=lcm(35, *(eff(q) for q in pool), 3, 6, 9, 12)
    assert period==5040
    points=[v for v in range(period) if v%35 in z.A]
    full=(1<<len(points))-1
    @lru_cache(None)
    def m(f,b):
        return sum(1<<i for i,v in enumerate(points) if v%f==b)
    fixed=[m(3,0),m(3,1),m(6,5),m(9,5),m(12,8)]
    def can(state,budget):
        masks=list(set(fixed+[m(eff(q),v) for q,v in state.items()]))
        # Removing dominated channels is sound for equal channel cost.
        masks=[x for x in masks if x and not any(x!=y and x&y==x for y in masks)]
        choices=tuple(tuple(x for x in masks if x>>i&1) for i in range(len(points)))
        @lru_cache(None)
        def dfs(rem,depth):
            if not rem:return True
            if not depth:return False
            if max(((x&rem).bit_count() for x in masks),default=0)*depth < rem.bit_count():
                return False
            # Any uncovered point can choose its covering class first.
            p=(rem&-rem).bit_length()-1
            return any(dfs(rem&~x,depth-1) for x in choices[p])
        return dfs(full,budget)
    states=[]
    # One root per shape; mutate it, then take a few unions of independent
    # shapes to exercise nonexclusive matches and unused categories.
    for shape in shapes:
        a={}
        for qs,b,cv in shape:
            q=rng.choice([q for q in qs if q not in a]); a[q]=cv(q,b)
        states += [a,{q:b for q,b in a.items() if q!=next(iter(a))}]
    for _ in range(100):
        state=dict(rng.choice(states)); state.update(rng.choice(states))
        for q in rng.sample(pool,rng.randrange(5)):
            state[q]=rng.randrange(eff(q))
        states.append(state)
    for a in states:
        old=can(a,6); new=can(a,7)
        assert evaluate(eight,a)==old
        assert (evaluate(both,a) or evaluate(zero,a) or evaluate(one,a) or old)==new
        assert evaluate(target,a)==(new and not old)
    return len(states)

samples=crosscheck() if layout=='forward' else 0
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
out={}
for name,pred in [('budget8',eight),('zero',zero),('one',one),('both',both),
                  ('zero_and_one',conjoin((zero,one))),('zero_and_both',conjoin((zero,both))),
                  ('zero_type1',zero_type1),('union',disjoin((eight,zero,one,both)))]:
    out[name]={'at_most9_predicate':value(pred),'exact9':value(apply('AND',pred,invert(eight)))}
assert raw(target)==raw(apply('AND',zero,invert(eight)))+raw(apply('AND',both,invert(eight)))-raw(conjoin((zero,both,invert(eight))))
assert out['union']['exact9']==value(target)
print(json.dumps({'densities':out,'n_primes':N,'represented_CRT_root_residues':str(total[0]),
                  'periodic_set_cover_crosschecks':samples,'node_count':len(nodes),'weighted_cache_size':weighted.cache_info().currsize,'variable_order':layout},indent=2))
