"""All low-order R2 split ninth-budget templates using both W primes."""
import json
from math import gcd,lcm,prod
from collections import Counter,defaultdict
from pathlib import Path
from itertools import combinations
base=Path(__file__).parent
data=json.loads((base/'low_inventory.json').read_text())
H={1,2,3,4,5,6,7,8,9,10,12,15,16,20,35}
D={0,3,5,8,10,15,21,23,26,28,30,31,33}
group=defaultdict(list)
for r in data:
    h=r['d']//gcd(r['d'],36)
    assert r['f']//gcd(r['f'],3)==h
    if h in H:group[h].extend(map(int,r['primeFactors']))
# h=2 describes the fixed prime 38737 only.
assert 2 not in group and 1 not in group
period=lcm(35,2,*group)
W=tuple(w for w in range(period) if w%35 in D)
FULL=(1<<len(W))-1
def bits(xs):
    v=0
    for x in xs:v|=x
    return v
cats=[]
for h in sorted(set(group)|{2}):
    for b in ((1,) if h==2 else range(h)):
        covered=sum(1<<i for i,w in enumerate(W) if w%h==b)
        if covered:cats.append((h,b,covered))
N=len(cats)
ms=[e[2] for e in cats]
f=[e[0] for e in cats]
indices={h:bits(1<<i for i in range(N) if f[i]==h) for h in set(f)}
caps={h:len(p) for h,p in group.items()}|{2:1}
# A full truth matrix; compress repeated sets of choices.
opts=[(1<<i,bits(1<<j for j,x in enumerate(ms) if x>>i&1)) for i in range(len(W))]
seen=[]
templates=[]
nodes=Counter()
def walk(missing,avail,depth,used):
    nodes[depth]+=1
    if not missing:
        if any((ms[j]&~bits(ms[k] for k in seen if k!=j))==0 for j in seen):return
        templates.append(tuple(sorted((cats[j][0],cats[j][1]) for j in seen)))
        return
    if depth==0:return
    a=avail
    if not a:return
    # Largest gains give a safe additive bound; used also on the final slot.
    gains=[]
    while a:
        b=a&-a;a-=b;j=b.bit_length()-1
        x=(ms[j]&missing).bit_count()
        if not x:avail^=b
        else:gains.append(x)
    if sum(sorted(gains,reverse=True)[:depth])<missing.bit_count():return
    if depth==1:
        for j,m in enumerate(ms):
            if avail>>j&1 and missing&~m==0:
                seen.append(j);walk(0,0,0,used);seen.pop()
        return
    hit=0;count=depth+N
    for bit,ok in opts:
        if not bit&missing:continue
        ok&=avail
        k=ok.bit_count()
        if k<count:hit,count=ok,k
        if count<=1:break
    while hit:
        b=hit&-hit;hit-=b;avail^=b
        j=b.bit_length()-1;h=f[j];u=used.get(h,0)+1
        seen.append(j)
        walk(missing&~ms[j],avail&~indices[h] if u==caps[h] else avail,depth-1,used|{h:u})
        seen.pop()
walk(FULL,(1<<N)-1,5,{})
assert len(set(templates))==len(templates)
templates.sort()
assert Counter(map(len,templates))[3]==3
result={'period_w':period,'residual_points':len(W),'categories':N,'nodes_by_remaining':dict(sorted(nodes.items())),
        'shapes_by_size':dict(sorted(Counter(map(len,templates)).items())),'by_h':{h:list(qs) for h,qs in sorted(group.items())},
        'shapes':templates}
print(json.dumps(result,separators=(',',':')))
