#!/usr/bin/env python3
"""Independent Python-only signed native trie DP (without C++ or its DP tables).
Checks completed EC49FME indices 738, 757, 840, 922, 969.
"""
import collections,itertools,json,sys
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/"EC49FJD_RELEASE_B11_COMPLETE_20261111"))
from EC49FGW_RADIUS5_SCREEN import PIN,all_words,pref,raw_key
BASE={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
E=json.loads((P/"EXACT_VECTOR_EC49FME.json").read_text())
assert PIN==E["model_pin"]
import zlib,base64
rows=[line.split() for line in zlib.decompress(base64.b64decode(E["rows_zlib_b64"])).decode().splitlines()]
assert len(rows)==232
catalog=list(all_words());labs=sorted(set(label for label,word in catalog))
labels={x:i for i,x in enumerate(labs)};support=collections.defaultdict(int)
for label,word in catalog:support[raw_key(word)]|=1<<labels[label]
outside=sorted(set(support)-BASE);old=sorted(BASE);full=(1<<24)-1
keysets=[]
for dropped in itertools.combinations(old,2):
    for added in itertools.combinations(outside,2):
        K=set(BASE)-set(dropped)|set(added)
        if (lambda v:v==full)(__import__("functools").reduce(int.__or__,(support[k] for k in K),0)):
            keysets.append(K)
assert len(keysets)==6315

def root_dp(group,local_labels):
    ix={label:i for i,label in enumerate(local_labels)}
    children=[{}];terminal=[0]
    for label,word in group:
        v=0
        for p in pref(word):
            nxt=children[v].get(p)
            if nxt is None:
                nxt=len(children);children[v][p]=nxt;children.append({});terminal.append(0)
            v=nxt
        terminal[v]|=1<<ix[label]
    def walk(v):
        dp={0:0}
        if terminal[v]:dp[terminal[v]]=0
        for w in children[v].values():
            q=walk(w);next_dp={}
            for a,x in dp.items():
                for b,y in q.items():
                    m=a|b;z=x+y
                    if z<next_dp.get(m,10**9):next_dp[m]=z
            dp=next_dp
        return {m:c+(v!=0 and bool(m)) for m,c in dp.items()}
    best=[10**9]*(1<<len(local_labels))
    for m,c in walk(0).items():best[m]=c
    for bit in range(len(local_labels)):
        for mask in range(len(best)):
            if not(mask>>bit&1):best[mask]=min(best[mask],best[mask|(1<<bit)])
    return best,ix

for global_index in (738,757,840,922,969):
    K=keysets[global_index]
    groups=collections.defaultdict(list)
    for label,word in catalog:
        if raw_key(word) in K:
            groups[pref(word)[0]].append((label,word))
    costs={};options=collections.defaultdict(list)
    for root,group in groups.items():
        local_labels=sorted(set(label for label,word in group))
        cost,index=root_dp(group,local_labels);costs[root]=cost
        for label,bit in index.items():options[label].append((root,bit))
    assert len(options)==24
    order=sorted(options,key=lambda lab:len(options[lab]))
    assigned={root:0 for root in groups};answer=10**9
    def visit(j):
        global answer
        if j==24:
            answer=min(answer,sum(costs[r][assigned[r]] for r in groups))
            return
        for root,bit in options[order[j]]:
            assigned[root]|=1<<bit
            visit(j+1)
            assigned[root]&=~(1<<bit)
    visit(0)
    expectation=int(rows[global_index-738][1])
    assert answer==expectation,(global_index,answer,expectation)
    print("EC49FME_INDEPENDENT_PASS",global_index,answer,"roots",len(groups),flush=True)
print("EC49FME_FIVE_INDEPENDENT_CASES_PASS")
