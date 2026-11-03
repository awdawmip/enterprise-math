#!/usr/bin/env python3
"""Exact primitive-prefix lower bound at h=5 for EC49EXJ schedules.
Scientific model pinned to EC49EXH/EC49EXI. Requires C++17 integer DP.
No task-control authority is inferred from research computation.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from functools import lru_cache
from pathlib import Path
import subprocess, os, json, time, re
from ANALYTIC_EC49EXJ import families,BASE
HERE=Path(__file__).resolve().parent
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
H=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')
T4=(1836687,1867942,1872656,1873981)
T2=(1836425,1866380)
BASE_WORDS=('ce','de','ec','ed')

def native(w): return tuple(a for c in w for a in OPS[c])
def sig(st):
    n=0;mul=1
    for ev,prev in H:
        for s in st:
            if prev==1 and s==2:
                if ev=='N':ev='A'
                elif ev=='B':ev='BA'
            elif prev==2 and s==1:
                if ev=='N':ev='B'
                elif ev=='A':ev='AB'
            prev=s
        n+=BUCKETS.index(ev)*mul;mul*=5
    return n

def permutations(ct,prefix=''):
    if not sum(ct.values()):
        yield prefix;return
    for c in sorted(ct):
        if ct[c]:
            ct[c]-=1
            yield from permutations(ct,prefix+c)
            ct[c]+=1

@lru_cache(None)
def words(h,key,t):
    u,v,w=key
    r=u+v-h-1;na=w-1;nf=u-r-2*w;ng=v-r
    if min(r,na,nf,ng)<0:return ()
    tgt=T4 if t==4 else T2
    result=[]
    for nc in range(r+1):
        ct=Counter({'a':na,'c':nc,'d':r-nc,'e':w,'f':nf,'g':ng})
        for word in permutations(ct):
            st=native(word);ss=sig(st)
            if ss in tgt:result.append((st,ss,word))
    return tuple(result)

def build_input(prefix):
    # prefix = tuple ((p2,t2),...,(p5,t5)); T2/T4 is encoded by p/h.
    parents=[-1];kids=[{}];colors=[0];prepaid=[0];nwords=0
    expected_signatures={}
    for h,(key,t) in enumerate(prefix,start=2):
        sigs=T4 if t==4 else T2
        expected_signatures[h]=set(sigs)
        for st,ss,word in words(h,key,t):
            nwords+=1;v=0
            for a in st:
                if a not in kids[v]:
                    kids[v][a]=len(parents)
                    parents.append(v);kids.append({});colors.append(0);prepaid.append(0)
                v=kids[v][a]
            bit=sum(len(T4 if typ==4 else T2) for _,typ in prefix[:h-2])+sigs.index(ss)
            colors[v]|=1<<bit
            expected_signatures[h].discard(ss)
    assert all(not v for v in expected_signatures.values()),(prefix,expected_signatures)
    for word in BASE_WORDS:
        v=0
        for a in native(word):v=kids[v][a];prepaid[v]=1
    assert sum(prepaid)==28
    input_s=f'{len(parents)} {sum(len(T4 if t==4 else T2) for _,t in prefix)}\n'+''.join(f'{p} {pre} {mask}\n' for p,pre,mask in zip(parents,prepaid,colors))
    return input_s,len(parents),nwords

def schedules():
    fs={h:families(h) for h in range(2,9)}
    ks=sorted(set().union(*(set(z) for z in fs.values())))
    allpairs=[]
    for extras in combinations((k for k in ks if k!=BASE),3):
        q=(BASE,)+extras
        opts=[[(i,fs[h][p]) for i,p in enumerate(q) if p in fs[h]] for h in range(3,9)]
        if not all(opts):continue
        for seq in product(*opts):
            if len({0,*[i for i,_ in seq]})!=4 or len({0,*[i for i,_ in seq[:-1]]})!=4:continue
            allpairs.append(tuple([(BASE,4)]+[(q[i],t) for i,t in seq]))
    assert len(allpairs)==26933
    return allpairs

def run():
    t0=time.monotonic();ss=schedules()
    h5prefixes=sorted({s[:4] for s in ss})
    print('H5 prefixes',len(h5prefixes),flush=True)
    exe=HERE/'exact_dp'
    if not exe.is_file():
        subprocess.run(['g++','-O3','-std=c++17',str(HERE/'EXACT_OR_MASK_DP.cpp'),'-o',str(exe)],check=True)
    e5={};stats={};progress=0
    for ix,p in enumerate(h5prefixes):
        input_s,nn,nwords=build_input(p)
        run=subprocess.run([str(exe)],input=input_s,encoding='utf-8',capture_output=True,timeout=60)
        if run.returncode!=0:raise RuntimeError((p,run.stdout,run.stderr))
        match=re.search(r'total=(\d+)',run.stdout)
        assert match,run.stdout
        v=int(match.group(1));e5[p]=v
        stats[str(ix)]={'key_family':[[list(k),t] for k,t in p], 'E5':v,'nodes':nn,'eligible_words':nwords, 'solver_output':run.stdout.strip()}
        if (ix+1)%25==0:print('H5 progress',ix+1,'/',len(h5prefixes), 'seconds',round(time.monotonic()-t0,1),flush=True)
    # Exact E5 cost and independent terminal suffix increments give a valid bound.
    screened=[];unscreened=[];boundhist=Counter();types=Counter()
    for schedule in ss:
        suffix=sum(2*t for k,t in schedule[4:]) # t=2 =>4, t=4 =>8
        lower=e5[schedule[:4]]+suffix
        boundhist[lower]+=1
        typs=''.join(str(t) for k,t in schedule)
        (screened if lower>=90 else unscreened).append(schedule)
        types[(lower>=90,typs)]+=1
    out={
        'status':'PASS', 'method':'Exact native signed primitive-prefix OR-mask DP for all unique 4-horizon prefixes, then terminal-edge lemma for 6/7/8.',
        'h5_distinct_typed_prefixes':len(h5prefixes), 'count_four_keys_by_h7':len(ss),
        'screened_by_H5_bound':len(screened), 'remaining_after_H5_bound':len(unscreened),
        'E5_range':[min(e5.values()),max(e5.values())],
        'bound_hist':dict(sorted(boundhist.items())),
        'per_prefix_exact_results':stats,
        'by_type_pattern_and_screen':{f'{ok}:{typ}':v for (ok,typ),v in sorted(types.items())},
        'first_screened_example':None if not screened else [[list(k),t] for k,t in screened[0]],
        'first_unscreened_example':None if not unscreened else [[list(k),t] for k,t in unscreened[0]],
        'elapsed_seconds':round(time.monotonic()-t0,2),
    }
    path=HERE/'EC49EXJ_H5_EXECUTED.json'
    path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('status','h5_distinct_typed_prefixes','count_four_keys_by_h7','screened_by_H5_bound','remaining_after_H5_bound','E5_range','elapsed_seconds')},indent=2),flush=True)
if __name__=='__main__':run()
