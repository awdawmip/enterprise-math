from collections import defaultdict
from functools import cache
from fractions import Fraction
from decimal import Decimal,localcontext
from math import prod
import json
D=json.load(open('templates.json'))['types']
G=defaultdict(list)
for f,_,qs in json.load(open('inventory.json')).values():G[f].extend(qs)
shapes=[{f:frozenset(b for g,b in s if g==f) for f in G} for s in D]
def distribution(qs,p):
    weights={0:1}
    for q in qs:
        nxt=defaultdict(int)
        for m,w in weights.items():
            nxt[m]+=w*(q-2*p)
            for i in range(p):nxt[m|1<<i]+=2*w
        weights=nxt
    assert sum(weights.values())==prod(qs)
    return weights
def exact(families, order):
    groups=[]
    for f in order:
        wanted=sorted({b for s in families for b in s[f]})
        patterns=[sum(1<<wanted.index(b) for b in s[f]) for s in families]
        coeff=defaultdict(int)
        for m,w in distribution(G[f],len(wanted)).items():
            alive=sum(1<<i for i,k in enumerate(patterns) if m&k==k)
            coeff[alive]+=w
        groups.append(coeff)
    @cache
    def walk(i,alive):
        if not alive:return 0
        if i==len(groups):return 1
        return sum(w*walk(i+1,alive&m) for m,w in groups[i].items())
    return Fraction(walk(0,(1<<len(families))-1),prod(q for qs in G.values() for q in qs))
zfs=(7,14,35)
bfs=tuple(f for f in sorted(G) if f not in zfs)
zero=[s for s in shapes if s[7]]
both=[s for s in shapes if not s[7]]
# Each branch uses disjoint prime coordinates. exact() uses all sizes only for its
# denominator below; scale by irrelevant group sizes to get the marginal.
def marginal(ss,ff):
    return exact(ss,ff)*prod(q for f in G if f not in ff for q in G[f])
z=marginal(zero,zfs);b=marginal(both,bfs)
assert z==marginal(zero,zfs[::-1]) and b==marginal(both,bfs[::-1])
a=1-(1-z)*(1-b)
sev=[shapes[i] for i,s in enumerate(D) if len(s)==5]
u=marginal(sev,bfs)
# Independent closed form from the three disjoint groups of the v11 seven theorem.
from math import comb
def trip(qs):
    return Fraction(sum((-1)**j*comb(3,j)*prod(q-2*j for q in qs) for j in range(4)),prod(qs))
old=1-(1-Fraction(8,prod(G[12])))*(1-trip(G[15]))*(1-trip(G[9]))
assert u==old
def show(x):
    return {'num':str(x.numerator),'den':str(x.denominator),'decimal':str(Decimal(x.numerator)/x.denominator)}
with localcontext() as c:
    c.prec=65
    print(json.dumps({'at_most_8':show(a),'zero_W':show(z),'both_W':show(b),'exact_7':show(u),'exact_8':show(a-u)},indent=2))
