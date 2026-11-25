from pathlib import Path
from math import gcd,lcm
import json
b=Path('branches.txt').read_text().splitlines()
assert int(b[0])==len(b)-1
def read(i,d):
    f=Path(f'branch-{i}-{d}.txt').read_text().splitlines()
    stats=list(map(int,f.pop().split()[1:]))
    terms={tuple(tuple(map(int,x.split(':'))) for x in line.split(',')) for line in f}
    assert len(terms)==len(f)==stats[3]
    return terms,stats
stat=[[],[]]; all_terms={tuple((7,x) for x in (0,1,2,3,5))}
for i,s in enumerate(b[1:]):
    k,P,n,h,r,*data=map(int,s.split())
    if not h: continue
    D=data[:n]
    hs=data[n:n+h]
    R=data[n+h:]
    assert len(R)==r
    sets=[]
    for d in range(2):
        t,z=read(i,d)
        assert z[0]==i and z[-1]==P
        stat[d].append(z)
        sets.append(t)
    assert sets[0]==sets[1],i
    for ts in sets[0]:
        t=[(h,b) for h,b in ts if h!=7]
        assert len(t)<=k and all(h in hs for h,b in t) and [b for h,b in ts if h==7]==R
        hit=[tuple(j for j,(h,b) in enumerate(t) if x%h==b) for x in D]
        assert all(hit) and {a[0] for a in hit if len(a)==1}==set(range(len(t))),(i,ts)
    all_terms.update(sets[0])
frozen=[]
sets=[]
for t in sorted(all_terms,key=lambda t:(len(t),t)):
    z=frozenset(t)
    if not any(s<=z for s in sets):
        frozen.append(t);sets.append(z)
groups=sorted({h for t in frozen for h,b in t})
orders={h:[h*m for m in (1,2,3,4,6,9,12,18,36) if h*m//gcd(h*m,36)==h] for h in groups}
report={'branchCount':len(stat[0]),'stats':[{'visited':sum(x[1] for x in s),'kept':sum(x[3] for x in s),'maxPeriod':max(x[-1] for x in s)} for s in stat],'unique':len(all_terms),'minimalCount':len(frozen),'groups':groups,'orders':orders,'countPerBranch':[[x[0],x[3]] for x in stat[0]],'templates':[[f'{h}:{b}' for h,b in t] for t in frozen]}
Path('enumeration-cpp.json').write_text(json.dumps(report,separators=(',',':'))+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('templates','countPerBranch')}))
