from math import prod
from fractions import Fraction
from collections import defaultdict
from functools import cache
from decimal import Decimal,localcontext
import json
G=json.load(open('inventory.json'))
P={int(d):[int(q) for q in ps] for d,ps in json.load(open('factor_stage2.json')).items()}
H={int(h):[q for d,_ in rows for q in P[d]] for h,rows in G.items()}
assert all(prod(P[d])==int(n) for r in G.values() for d,n in r)
assert len({q for ps in H.values() for q in ps})==sum(map(len,H.values()))
T=[[tuple(map(int,x.split(':'))) for x in s] for s in json.load(open('observer_templates.json'))['templates']]
B={
 'rows':(7,14,35),
 'divide12':(12,24),
 'divide20':(20,40),
 'binary':(16,),
}
old={
 'rows':[[(7,x) for x in [0,1,2,3,5]]],
 'divide12':[[(12,x) for x in [0,8]]],
 'divide20':[[(20,x) for x in [0,8,16]]],
 'binary':[],
}
def counts(terms,hs):
    if not terms:return Fraction(0)
    data=[]
    for h in hs:
        classes=sorted({b for t in terms for j,b in t if h==j})
        masks=[sum(1<<classes.index(b) for j,b in t if h==j) for t in terms]
        st={0:1}
        for q in H[h]:
            new=defaultdict(int)
            w=q-2*len(classes)
            assert w>=0
            for s,v in st.items():
                new[s]+=v*w
                for i in range(len(classes)):new[s|(1<<i)]+=v*2
            st=new
        new=defaultdict(int)
        for s,v in st.items():
            if v:new[sum(1<<i for i,m in enumerate(masks) if m&s==m)]+=v
        data.append(new)
    @cache
    def dp(i,a):
        if not a:return 0
        if i==len(hs):return 1
        return sum(v*dp(i+1,a&m) for m,v in data[i].items())
    return Fraction(dp(0,(1<<len(terms))-1),prod(q for h in hs for q in H[h]))
r9={k:counts(old[k],hs) for k,hs in B.items()}
r10={k:counts([t for t in T if all(h in hs for h,b in t)],hs) for k,hs in B.items()}
assert sum(len([t for t in T if all(h in hs for h,b in t)]) for hs in B.values())==42
for k,hs in B.items():
 assert counts([t for t in T if all(h in hs for h,b in t)],hs[::-1])==r10[k]
 assert r9[k]<r10[k]
e9=1-prod(1-c for c in r9.values())
e10=1-prod(1-c for c in r10.values())
x=e10-e9
def fmt(x):
    with localcontext() as c:
        c.prec=75
        v=format(Decimal(x.numerator)/Decimal(x.denominator),'.64E')
    return dict(numerator=str(x.numerator),denominator=str(x.denominator),decimal=v)
M=prod(q for ps in H.values() for q in ps)
orig=H[40]
H[40]=[q for q in H[40] if q not in P[1440]]
limited=counts([t for t in T if all(h in B['divide20'] for h,b in t)],B['divide20'])
H[40]=orig
delta=(r10['divide20']-limited)*prod(1-r10[k] for k in B if k!='divide20')
assert 0<delta<x
print(json.dumps(dict(E9=fmt(e9), E10=fmt(e10), exact10=fmt(x),roots_per_ten=fmt(1/x), needs_order_1440=fmt(delta), share_needs_order_1440=fmt(delta/x),
    supports={h:len(ps) for h,ps in H.items()},count=sum(map(len,H.values())),bits=M.bit_length(),
    digits=len(str(M)),modulus=str(M), nine_by_component={k:fmt(v) for k,v in r9.items()},
    ten_by_component={k:fmt(v) for k,v in r10.items()}),indent=2))
