#!/usr/bin/env python3
"""R680: exact integer replay of primitive-time V23/V27/V29 priority repair."""
from itertools import combinations, permutations
from collections import Counter
import json

TRIADS=tuple(combinations(range(6),3))
MATCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
PASS=((0,1),(1,2),(2,0))
BIASES=((-4,-3,-2,10),(-3,-2,-4,10),(-2,-4,-3,10),(2,4,3,-10),(3,2,4,-10),(4,3,2,-10))

def code(s,m):
    if any((a in s)+(b in s)!=1 for a,b in m): return 0
    return 1 if sum(b in s for a,b in m)%2==0 else -1

C={s:tuple(code(s,m) for m in MATCH) for s in TRIADS}
N={s:tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
assert len(set(C.values()))==20 and all(len(N[s])==9 for s in TRIADS)

def states(bias,order):
    u=list(bias);M=[[0]*4 for _ in range(4)]
    yield tuple(u),tuple(tuple(row) for row in M)
    for e in order:
        a,b=PASS[e];u[a]+=1;u[b]-=1;M[a][b]+=1
        yield tuple(u),tuple(tuple(row) for row in M)

def scores(u,M):
    O=[[M[i][j]-M[j][i] for j in range(4)] for i in range(4)]
    p={t:sum(u[i]*C[t][i] for i in range(4)) for t in TRIADS}
    return {s:{t:p[t]+sum(C[s][i]*O[i][j]*C[t][j] for i in range(4) for j in range(4)) for t in N[s]} for s in TRIADS}

def shell(k):
    def rec(i,r,acc):
        if i==4:
            if r==0: yield tuple(acc)
            return
        for n in range(r+1):
            for v in ((0,) if n==0 else (-n,n)):
                yield from rec(i+1,r-n,acc+[v])
    yield from rec(0,k,[])

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def tag(s):return ''.join(map(str,s))

hist={};pairs=set();stage_ties=Counter();max_group=0
for u in BIASES:
    for order in permutations(range(3)):
        st=[]
        for i,(v,M) in enumerate(states(u,order)):
            sc=scores(v,M)
            winners={s:tuple(t for t in N[s] if sc[s][t]==max(sc[s].values())) for s in TRIADS}
            stage_ties[i]+=sum(len(q)>1 for q in winners.values())
            max_group=max(max_group,max(map(len,winners.values())))
            for q in winners.values():
                pairs.update(tuple(sorted((a,b))) for a,b in combinations(q,2))
            st.append(sc)
        hist[(u,order)]=st
assert len(hist)==36 and len(pairs)==30 and max_group==3
assert [stage_ties[i] for i in range(4)]==[0,108,108,0]

def valid(w):
    return all(dot(w,C[a])!=dot(w,C[b]) for a,b in pairs)

out=[]
for k in range(6):
    test=list(shell(k));ok=[w for w in test if valid(w)]
    out.append((len(test),len(ok)))
    if k==5: minimizers=ok
assert out==[(1,0),(8,0),(32,0),(88,0),(192,0),(360,12)]
w=(-1,1,-2,-1)
assert w in minimizers
r={s:dot(w,C[s]) for s in TRIADS}
assert min(r.values())==-3 and max(r.values())==3

k6_failure=False
for (u,order),st in hist.items():
    for i,sc in enumerate(st):
        for s in TRIADS:
            mx=max(sc[s].values())
            refined=[(7*sc[s][t]+r[t],t) for t in N[s]]
            top=max(x for x,t in refined)
            final=[t for x,t in refined if x==top]
            assert len(final)==1 and sc[s][final[0]]==mx
            for a,b in combinations(N[s],2):
                if sc[s][a]==sc[s][b]: continue
                hi,lo=(a,b) if sc[s][a]>sc[s][b] else (b,a)
                assert 7*sc[s][hi]+r[hi]>7*sc[s][lo]+r[lo]
                if 6*sc[s][hi]+r[hi]<=6*sc[s][lo]+r[lo]:
                    k6_failure=True
                    if (u,order,i,s,hi,lo)==(BIASES[0],(0,1,2),2,(0,2,3),(0,1,2),(0,2,5)):
                        assert sc[s][hi]-sc[s][lo]==1 and r[lo]-r[hi]==6
assert k6_failure

def end(u,order,start):
    s=start
    for sc in hist[(u,order)][1:]:
        s=max(N[s],key=lambda t:7*sc[s][t]+r[t])
    return s

histogram=Counter();by_bias={}
for u in BIASES:
    c=Counter()
    for s in TRIADS:
        destinations={end(u,o,s) for o in permutations(range(3))}
        c[len(destinations)]+=1
    by_bias[str(u)]=dict(c)
    histogram.update(c)
assert histogram==Counter({1:59,2:29,3:27,4:5})
assert sum(histogram.values())==120
example={''.join('ABC'[i] for i in o):tag(end(BIASES[0],o,(0,1,2))) for o in permutations(range(3))}
assert example=={'ABC':'034','ACB':'123','BAC':'025','BCA':'123','CAB':'123','CBA':'123'}

summary={'schema':'R680_CHECKER_RESULT_V1','frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
 'baseline_count':len(BIASES),'labeled_histories':len(hist),'distinct_comax_pairs':len(pairs),
 'tied_source_count_by_prefix':[stage_ties[i] for i in range(4)],'max_winner_set_size':max_group,
 'integer_norm_shell_counts':out,'minimal_norm':5,'minimizers':[list(v) for v in minimizers],
 'priority_covector':list(w),'priority_multiplier':7,'K6_preservation_counterexample_exists':k6_failure,
 'trajectories_checked':720,'distinct_end_histogram':dict(histogram),'per_bias':by_bias,
 'witness_end_by_event_word':example,'co_max_pairs':[[tag(a),tag(b)] for a,b in sorted(pairs)]}
print(json.dumps(summary,ensure_ascii=False,indent=2))
print('R680_PRIMITIVE_TIME_INTEGER_PRIORITY_MEMORY_EXACT_PASS')
