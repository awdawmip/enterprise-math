from cyclic11 import observations,class_cost,setbits
import json
from pathlib import Path
from itertools import combinations
from collections import Counter
cert=json.load(open('cyclic11.json'))
U=sorted(set(i for cl in cert['classes'][5:] for i in cl))
bad,pair=observations();allmask=sum(1<<i for i in U)
counts=Counter();large=[]
def visit(S,m,forb):
    if len(S)+m.bit_count()<9:
        return
    r=m;order=[];c=0
    while r:
        c+=1
        clique=r
        while clique:
            bit=clique&-clique;i=bit.bit_length()-1
            order.append((i,c));r^=bit;clique&=r&forb[i]
    for i,cap in reversed(order):
        if len(S)+cap<9:return
        m^=1<<i;T=S+[i];nx=m&~forb[i]
        if len(T)>=9:
            h=sum(1<<w for w in T);counts[len(T)]+=1
            large.append((h,class_cost(T,pair)))
        if len(T)+nx.bit_count()>=9:
            visit(T,nx,{k:forb[k]|bad[i][k] for k in setbits(nx)})
visit([],allmask,{k:0 for k in U})
print('counts',counts,flush=True)
rows=[(s,c) for s,c in large if s.bit_count()==10]
lookup={s:c for s,c in rows}; partitions=Counter();winner={};nodes=0
def cover(free,rows,chosen,acc):
    global nodes
    nodes+=1
    if not free:
        partitions[acc]+=1
        winner.setdefault(acc,list(chosen))
        return
    buckets={i:[] for i in setbits(free)}
    for s,c in rows:
        if s&free!=s:continue
        for i in setbits(s):
            buckets[i].append((s,c))
    for s,c in min(buckets.values(),key=len):
        cover(free^s,[(z,v)for z,v in rows if not z&s],chosen+[s],acc+c)
cover(allmask,rows,[],0)
print('partitions',partitions,'nodes',nodes,flush=True)
best=min(partitions)
classes=cert['classes'][:5]+[list(setbits(t))for t in winner[best]]
code=[next(l for l,c in enumerate(classes) if i in c)for i in range(125)]
di=dict(family="fixed five large classes, all unrestricted remaining six classes",
        legal_nine_and_up_by_size=sorted(counts.items()),ten_cost_distribution=sorted(Counter(c for s,c in rows).items()),
        cover_nodes=nodes,total_partitions=sum(partitions.values()),residual_cost_frequency=sorted(partitions.items()),
        best_total=best+5*1296,best_zero=31250-best-5*1296,best_classes=classes,best_code=code)
Path("residual11.json").write_text(json.dumps(di,indent=2)+'\n')
Path("residualbest11.txt").write_text(' '.join(map(str,code))+'\n')
