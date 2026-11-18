#!/usr/bin/env python3
"""Independent pure-Python signed-prefix trie DP for selected frozen-model cases."""
import sys,importlib.util,json,collections
from pathlib import Path
P=Path(__file__).resolve().parent
if len(sys.argv)<2:raise SystemExit(__doc__)
spec=importlib.util.spec_from_file_location('frozen_brc',sys.argv[1])
gen=importlib.util.module_from_spec(spec);spec.loader.exec_module(gen)
assert gen.PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
selected=[int(v) for v in sys.argv[2:]] or [0,8,57,322,329,685,1136]
manifest=json.loads((P/'EC49FMC_RADIUS5_MANIFEST.json').read_text())
# Cost vector is embedded in the compact report, independent of C++ log.
import zlib,base64
report=json.loads((P/'EXACT_REPORT_EC49FMC.json').read_text())
allcost=list(zlib.decompress(base64.b64decode(report['costs_zlib_base64'])))
needed={tuple(k) for idx in selected for k in manifest[idx]['keys']}
bykey=collections.defaultdict(list);count=0
for lab,w in gen.all_words():
    count+=1
    k=gen.raw_key(w)
    if k in needed:bykey[k].append((lab,gen.pref(w)))
assert count==178850

def root_minimum(rows,labs):
    pos={lab:i for i,lab in enumerate(labs)}
    children=[{}];outputs=[0]
    for lab,path in rows:
        u=0
        for p in path:
            if p not in children[u]:
                children[u][p]=len(children);children.append({});outputs.append(0)
            u=children[u][p]
        outputs[u]|=1<<pos[lab]
    def dp(u):
        cur={0:0}
        if outputs[u]:cur[outputs[u]]=0
        for v in children[u].values():
            child=dp(v);new={}
            for a,ca in cur.items():
                for b,cb in child.items():
                    mask=a|b;c=ca+cb
                    if c<new.get(mask,10**9):new[mask]=c
            cur=new
        if u:cur={m:c+(m!=0) for m,c in cur.items()}
        return cur
    states=dp(0)
    f=[10**9]*(1<<len(labs))
    for m,c in states.items():f[m]=c
    for j in range(len(labs)):
        for m in range(len(f)):
            if not ((m>>j)&1):f[m]=min(f[m],f[m|1<<j])
    return f,pos,len(children)

for idx in selected:
    keys={tuple(q) for q in manifest[idx]['keys']}
    roots=collections.defaultdict(list)
    for key in keys:
        for lab,ps in bykey[key]:roots[ps[0]].append((lab,ps))
    costs={};choices=collections.defaultdict(list);nn=0
    for r,rows in roots.items():
        labs=sorted({lab for lab,ps in rows});f,li,n=root_minimum(rows,labs);nn+=n
        costs[r]=f
        for lab,bit in li.items():choices[lab].append((r,bit))
    assert len(choices)==24
    order=sorted(choices,key=lambda k:(len(choices[k]),k))
    accum={r:0 for r in roots};best=10**9
    def rec(j):
        global best
        if j==24:
            best=min(best,sum(costs[r][m] for r,m in accum.items()))
            return
        for root,bit in choices[order[j]]:
            before=accum[root];accum[root]=before|(1<<bit)
            rec(j+1)
            accum[root]=before
    rec(0)
    assert best==allcost[idx],(idx,best,allcost[idx])
    print('EC49FMC_INDEPENDENT_PASS',idx,'cost',best,'roots',len(roots),'trie_nodes',nn,flush=True)
