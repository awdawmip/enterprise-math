#!/usr/bin/env python3
"""Independent Python exact signed-prefix rebuild, four FOH witness edges.
Run: python VERIFY_EC49FOH_INDEPENDENT.py master_and_radius3_cases.txt FOH_RESULTS_84.csv
Does not import or reuse the C++ rooted cost arrays or DFS traces.
"""
from pathlib import Path
from collections import defaultdict
import hashlib,csv,sys
INF=10**9
ROOTS=(3,5,6,7)
SOURCE=Path(sys.argv[1]); ROWS=Path(sys.argv[2])
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
data=iter(SOURCE.read_text().split())
assert tuple(int(next(data)) for _ in range(3))==(94,178850,38169)
words=[]
for key in range(94):
    n=int(next(data)); records=[]
    for _ in range(n):
        label=int(next(data));code=next(data)
        records.append((label,int(code[:2],16),bytes.fromhex(code[2:])))
    words.append(records)
ids=(32274,32279,32292,32315,32324)
selected={}
for i in range(38169):
    row=[int(next(data)) for _ in range(7)]
    if i in ids:selected[i]=row
assert len(selected)==len(ids)
try:
    next(data)
    raise AssertionError("unexpected trailing data")
except StopIteration:
    pass

def root_table(keys,root):
    records=[(l,code) for k in keys for (l,r,code) in words[k] if r==root]
    labels=sorted({l for l,_ in records})
    idx={l:i for i,l in enumerate(labels)}
    edges=[{}]; term=[0]
    for l,code in records:
        p=0
        for ch in code:
            if ch not in edges[p]:
                edges[p][ch]=len(edges);edges.append({});term.append(0)
            p=edges[p][ch]
        term[p]|=1<<idx[l]
    def cost_node(u):
        state={0:0}
        if term[u]:state[term[u]]=0
        for v in edges[u].values():
            nxt=cost_node(v); merged={}
            for m,c in state.items():
                for n,k in nxt.items():
                    z=m|n;val=c+k
                    if val<merged.get(z,INF):merged[z]=val
            state=merged
        return {mask:val+(mask!=0) for mask,val in state.items()}
    full=cost_node(0);size=1<<len(labels)
    f=[INF]*size
    for mask,c in full.items():f[mask]=c
    for j in range(len(labels)):
        for m in range(size):
            if not (m>>j&1):f[m]=min(f[m],f[m|(1<<j)])
    return labels,idx,f
T={i:{r:root_table(selected[i],r) for r in ROOTS} for i in ids}
OPT={i:{l:tuple(r for r in ROOTS if l in T[i][r][1]) for l in range(24)} for i in ids}
assert all(all(OPT[i][l] for l in range(24)) for i in ids)
def order(i):
    def p(l):
        return (len(OPT[i][l]),-min(T[i][r][2][1<<T[i][r][1][l]] for r in OPT[i][l]),l)
    return sorted(range(24),key=p)
ORD={i:order(i) for i in ids}
def cost(i,m):
    val=0
    for r in ROOTS:
        labels,idx,f=T[i][r]
        mask=sum(1<<j for j,l in enumerate(labels) if m[r]>>l&1)
        val+=f[mask]
    return val
def dfs(i):
    m={r:0 for r in ROOTS};trace=[]
    def rec(d):
        c=cost(i,m);cut=c>155
        trace.append((tuple(m[r] for r in ROOTS),d,cut,c))
        if cut or d==24:return
        label=ORD[i][d]
        for r in OPT[i][label]:
            m[r]|=1<<label
            rec(d+1)
            m[r]^=1<<label
    rec(0)
    return trace
TR={i:dfs(i) for i in ids}
assert len(TR[32315])==173 and len(TR[32279])==436
rows={(int(z["src"]),int(z["dst"])):z for z in csv.DictReader(ROWS.open())}
for a,b in [(32315,32274),(32315,32279),(32315,32292),(32315,32324)]:
    X,Y=TR[a],TR[b];z=rows[(a,b)]
    assert (len(X),len(Y))==(int(z["src_visits"]),int(z["dst_visits"]))
    same=len(X)==len(Y) and all(x[:3]==y[:3] for x,y in zip(X,Y))
    assert int(same)==int(z["full_trace_same"])
    flips=sum((cost(b,dict(zip(ROOTS,x[0])))>155)!=x[2] for x in X)
    changed=sum(cost(b,dict(zip(ROOTS,x[0])))!=x[3] for x in X)
    branch=sum((not x[2]) and x[1]<24 and
        (ORD[a][x[1]]!=ORD[b][x[1]] or
        OPT[a][ORD[a][x[1]]]!=OPT[b][ORD[b][x[1]]]) for x in X)
    assert (flips,changed,branch)==tuple(int(z[k]) for k in
         ("changed_sign_on_src","changed_lb_on_src","changed_branch_on_src"))
    assert int(flips==0 and branch==0)==int(z["certificate"])
    print("INDEPENDENT_EDGE_PASS",a,b,"visits",len(X),len(Y),
          "cutflips",flips,"branchflips",branch,"LBchanged",changed)
print("EC49FOH_INDEPENDENT_4_EDGES_PASS source_hash_verified, 5 caches, 20 rooted profile computations")
