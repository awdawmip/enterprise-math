from minimum import *
from random import Random
branch=sys.argv[1] if len(sys.argv)>1 else 'global'
a0=(read('common_min.json') if branch=='C' else read('minima.json')[branch])['answer']
a=int(a0['root']);ps=tuple(q for q in (*P,*a0['supplement']) if q not in a0['all_old_survive_single_deletion'])
period=a0['cover_period']
rng=Random(20261125)
assert all(any(a*a*pow(2,n,q)%q==1 for q in ps) for n in range(1,period+1))
def private_candidates(limit):
    cc={q:[] for q in ps}
    phase={}
    for q in ps:
        d=next(d for d in range(1,100000) if pow(2,d,q)==1)
        good={i for i in range(d) if a*a*pow(2,i,q)%q==1}
        phase[q]=(d,good)
    for n in range(1,limit+1):
        qs=[q for q,(d,v) in phase.items() if n%d in v]
        if len(qs)==1:cc[qs[0]].append(n)
    return cc
@cache
def term(n):return (a*a<<n)-1
@cache
def compatible(n,m):
    u,v=sorted((n,m))
    return gcd(term(u),(1<<(v-u))-1)==1
last=None
for bound in (2500,7000,21000,42000):
    cs=private_candidates(bound)
    if any(not v for v in cs.values()):continue
    for itr in range(70):
        order=list(ps)
        if itr:rng.shuffle(order)
        match={}
        for q in order:
            b=cs[q].copy()
            if itr:rng.shuffle(b)
            for n in b:
                if all(compatible(n,m) for m in match.values()):
                    match[q]=n;break
            else:break
        if last is None or len(last)<len(match):last=match
        if len(match)==len(ps):
            break
    if len(last)==len(ps):break
from itertools import combinations
g=[gcd(term(n),term(m)) for n,m in combinations(last.values(),2)]
assert set(g)=={1}
print(json.dumps({'root':str(a),'count':len(last),'dictionary':ps,'witnesses':sorted(last.items()),
                  'max_n':max(last.values()),'direct_gcds':len(g),'search_limit':bound},indent=2))
