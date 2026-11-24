from decide import *
from random import Random
from collections import Counter
from hashlib import sha256
from known_inputs import P,U9,E,C,D
rows,allC,pC,cC=carriers()
assert len(rows)==47 and len(allC)==22 and max(d for d in rows if d<1260)==840
assert all(q0<2*A2*A2-1 for _,q0 in rows.values())
assert all(gcd(x,S2)==1 for x in allC.values()) and all(gcd(x,y)==1 for x,y in combinations(allC.values(),2))
assert prod(allC.values()).bit_length()==3265
assert lcm(35,*allC)==15120
def order(q):
    return next(d for d in range(1,1261) if pow(2,d,q)==1)
def crt(a,m,b,n):
    return a+m*((b-a)*pow(m,-1,n)%n),m*n
known=sorted(set(U9+E+C+D+(870031,1765891,2521,163,2593,71119,271,541,811)))
df={q:order(q) for q in known}
assert all(rows[d][1]%q==0 for q,d in df.items())
def build(desired):
    a,M=A2,S2
    zero=strip(prod(allC.values()),prod(desired))
    a,M=crt(a,M,0,zero)
    for q,b in sorted(desired.items()):
        d=df[q]
        a,M=crt(a,M,pow(2,-(4+6*b),q),q)
    return a
def freew(q,w):return (q,2+3*w)
high=dict([freew(q,w) for q,w in zip((181,631,2521,92737,649657),(0,3,21,26,31))])
low_dual=high|{870031:high[2521]}
topoff={q:b for q,b in high.items() if q!=2521}
assert high_only_geometry(build(high)) and high_only_geometry(build(low_dual)) and not high_only_geometry(build(topoff))
orders840={29:2,43:3,1429:4,5419:5,3361:1,61681:6,127681:22}
# One short row remains v=1,22 mod35. J covers odd v; T and order840 cover
# the two even lifts. v=1 becomes v=36 mod70; v=22 is even already.
case={"all_inactive":{}, "top_only":high, "top_and_low":low_dual, "top_off":topoff,
      "order_840":orders840,"order_840_off":{q:b for q,b in orders840.items() if q!=127681}}
case["ternary_extra"] = dict(freew(q,w) for q,w in zip((87211,246241,2593,71119,163),(0,1,2,5,8)))
case["column_split"] = dict(freew(q,w) for q,w in zip((181,631,271,811,541),(0,3,6,1,11)))
case["plain7"] = dict(freew(q,w) for q,w in zip((181,631,23311),(0,3,1)))
case["older8"]={29:2,43:3,1429:4,5419:5,3361:1,15790321:8}
rng=Random(20261125)
fixtures={}
for name,c0 in case.items():
    fixtures[name]=build(c0)
    for q in c0:fixtures[f'{name}_minus_{q}']=build({p:b for p,b in c0.items() if p!=q})
for i in range(180):
    c0=dict(rng.choice(list(case.values())))
    for q in list(c0):
        if rng.randrange(7)==0:del c0[q]
    for q in rng.sample(known,rng.randrange(1,15)):
        d=df[q];f=d//gcd(d,12);c0[q]=rng.randrange(f)
    fixtures[f'perturb_{i}']=build(c0)
def is_real_cover(a,z,cut):
    qz=set()
    for slot in z:
        if slot in FIX:
            qz.add(dict(zip(FIX,(19,73,38737)))[slot]);continue
        c=phase_value(a,slot,cut)
        assert c>1
        qz.add(c)
    assert len(qz)==len(z) and all(gcd(x,y)==1 for x,y in combinations(qz,2))
    period=lcm(35,*(f for f,b in z))
    return all(any(v%f==b for f,b in z) for v in range(period) if v%35 in A)
out={};ct=Counter()
for name,a in fixtures.items():
    x8=predicate(a,8)
    for cut in (840,1260):
        for k in (7,8,9):
            p,q=predicate(a,k,cut),literal(a,k,cut)
            assert (p is None)==(q is None),(name,cut,k,p,q)
            ct['direct_cover_comparisons']+=1
            if p is not None:assert is_real_cover(a,p,cut); ct['returned_covers_verified']+=1
    y=predicate(a,9,840); p=predicate(a,9);t=high_only_geometry(a)
    assert (p is not None)==(y is not None or t)
    assert x8 is None or y is not None
    out[name]={'low':y is not None,'high':t,'at_most_8':x8 is not None,'at_most_9':p is not None}
assert out['top_only']==dict(low=False,high=True,at_most_8=False,at_most_9=True)
assert out['top_and_low']==dict(low=True,high=True,at_most_8=False,at_most_9=True)
assert out['top_off']==dict(low=False,high=False,at_most_8=False,at_most_9=False)
assert out['order_840']==dict(low=True,high=False,at_most_8=False,at_most_9=True)
assert out['order_840_off']==dict(low=False,high=False,at_most_8=False,at_most_9=False)
assert (predicate(fixtures['order_840'],9,839) is None)
assert out['plain7']['at_most_8'] and out['older8']['at_most_8']
print(json.dumps(dict(families=len(allC),all_order_layers=len(rows),low_order_layers=len(carriers(840)[0]),joint_v_period=lcm(35,*allC),fixtures=len(fixtures),**ct,core={k:dict(root_hex=hex(fixtures[k]),**out[k]) for k in case},all_outputs_sha256=sha256(json.dumps(out,sort_keys=True).encode()).hexdigest()),indent=2))
