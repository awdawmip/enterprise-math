#!/usr/bin/env python3
"""PREFIX-970: gcd-reduced cross-gap residue index, exact named XOR recovery.
Run: python PREFIX970_R6_GCD_QUOTIENT_INDEX.py --small --benchmark --output result.json
Stdlib only. No native X6/BRC dynamics are invoked.
"""
import argparse
from bisect import bisect_left
from collections import Counter, defaultdict
from hashlib import sha256
from math import gcd
from statistics import median
from time import perf_counter
import json

EXPECTED = {
  1:(442,614,'ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71'),
  3:(839,1286,'1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3'),
  5:(3,3,'c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b')
}

def residuals(p):
    d=defaultdict(list)
    for i in range(p):
        for j in range(p):
            for s in (-1,1):d[(1<<i)-s*(1<<j)].append((i,j,s))
    return {r:sorted((v,tuple(slots)) for v,slots in d.items() if v%2==r) for r in (0,1)}

def ceildiv(a,b):
    assert b>0
    return -((-a)//b)

def named(p,k,gaps=(1,3,5),reduced=True):
    assert p>=4 and k>=1 and k%2 and k+2<(1<<(p-1))
    assert all(m>0 and m%2 for m in gaps)
    H=1<<(p-1);L=H+1;U=2*H-1
    r=residuals(p);cache={};out={m:[] for m in gaps};stat={m:Counter() for m in gaps}
    for t in range(1,2*k+1):
        g=gcd(k,t)
        left=r[(1-t)%2];right=r[t%2]
        eligible=[(c,cs) for c,cs in left if c%g==0] if reduced else left
        for m in gaps:
            d=2*t-k*m
            assert d%2!=0
            q=abs(d)//g if reduced else abs(d)
            key=(q,t%2)
            if reduced:
                if key not in cache:
                    tab=defaultdict(list)
                    for C,Cs in right:tab[C%q].append((C,Cs))
                    cache[key]=tab
                tab=cache[key]
                inv=pow(k//g,-1,q) if q>1 else 0
            else:
                tab=defaultdict(list)
                for C,Cs in right:tab[(k*C)%q].append((C,Cs))
                stat[m]['baseline_index_builds']+=1
                stat[m]['baseline_index_entries']+=len(right)
            st=stat[m]
            st['c_examined']+=len(left)
            st['c_gcd_admissible']+=len(eligible)
            dl=min(d*L,d*U);dh=max(d*L,d*U)
            for c,cs in eligible:
                low=max(ceildiv((k+2)*c+dl,k),ceildiv((t+m)*c+dl,t))
                high=min(((k+2)*c+dh)//k,((t+m)*c+dh)//t)
                if low>high:continue
                residue=((k+2)*(c//g)*inv)%q if reduced else ((k+2)*c)%q
                bucket=tab[residue]
                st['congruence_candidates_in_window_probes']+=len(bucket)
                for C,Cs in bucket[bisect_left(bucket,(low,)):bisect_left(bucket,(high+1,))]:
                    st['interval_candidates']+=1
                    B=k*C-(k+2)*c;A=t*C-(t+m)*c
                    assert B%d==0 and A%d==0
                    b=B//d;a=A//d
                    assert L<=a<=U and L<=b<=U
                    if not(a%2 and b%2 and a!=b):continue
                    st['odd_nondiagonal_candidates']+=1
                    ls=[(i,j) for i,j,s in cs if (((t*b+(1<<i))>>j)&1)==int(s==1)]
                    rs=[(I,J) for I,J,s in Cs if ((((t+m)*b+(1<<I))>>J)&1)==int(s==1)]
                    for i,j in ls:
                        for I,J in rs:
                            assert ((k*a)^(1<<j))-(1<<i)==t*b
                            assert (((k+2)*a)^(1<<J))-(1<<I)==(t+m)*b
                            out[m].append((a,b,t,t+m,i,j,I,J))
    for m in gaps:out[m].sort()
    indices=sum(len(v) for tab in cache.values() for v in tab.values())
    meta={'index_builds':len(cache),'index_entries':indices,'index_keys':sorted([list(key) for key in cache])} if reduced else {}
    return out,{m:dict(s) for m,s in stat.items()},meta

def digest(rows):
    return sha256(''.join(','.join(map(str,row))+'\n' for row in rows).encode()).hexdigest()

def direct(p,k,m):
    H=1<<(p-1);lo=H+1;hi=2*H-1;out=Counter()
    for a in range(lo,hi+1,2):
        left=defaultdict(list);right=defaultdict(list)
        for i in range(p):
            for j in range(p):
                x=((k*a)^(1<<j))-(1<<i)
                y=(((k+2)*a)^(1<<j))-(1<<i)
                if x>0:left[x].append((i,j))
                if y>0:right[y].append((i,j))
        for x,ls in left.items():
            for y,rs in right.items():
                z=y-x
                if z<=0 or z%m:continue
                b=z//m
                if not(lo<=b<=hi and b%2 and b!=a and x%b==0):continue
                t=x//b
                if 1<=t<=2*k:
                    for i,j in ls:
                        for I,J in rs:out[(a,b,t,t+m,i,j,I,J)]+=1
    return out

def run(small=True,benchmark=False):
    small_rows=[]
    if small:
        for p in range(4,8):
            H=1<<(p-1)
            for k in range(1,H-2,2):
                out,_,_=named(p,k)
                for m in (1,3,5):
                    assert Counter(out[m])==direct(p,k,m),(p,k,m)
                    small_rows.append((p,k,m,len(out[m])))
        assert len(small_rows)==168
    q19,stats,meta=named(19,21)
    per_gap=[]
    for m,(want_pairs,want_named,want_digest) in EXPECTED.items():
        rows=q19[m]
        assert len(rows)==want_named and len({(a,b) for a,b,*_ in rows})==want_pairs
        assert digest(rows)==want_digest
        per_gap.append({'m':m,'modulus_pairs':want_pairs,'named_histories':len(rows),
                        'named_sha256':want_digest,**stats[m]})
    res={'schema':'PREFIX970_R6_GCD_REDUCED_JOIN_V1','frozen_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
         'small_cases':len(small_rows),'small_histories_by_p':{str(p):sum(n for x,k,m,n in small_rows if x==p) for p in range(4,8)},
         'q19_k21':{'gaps':per_gap,'cache':meta},'scientific_status':'AUTHOR_PROOF_EXACT_INTEGER_VERIFIED_NOT_REVIEWED'}
    if benchmark:
        base=[];new=[]
        for rep in range(16):
            for method in (('new','old') if rep%2==0 else ('old','new')):
                start=perf_counter()
                if method=='new':got,_,_=named(19,21)
                else:got,_,_=named(19,21,reduced=False)
                elapsed=perf_counter()-start
                assert got==q19
                (new if method=='new' else base).append(elapsed)
        res['benchmark']={'method':'16 alternating full 3-gap runs in one CPython process, stdlib, median seconds',
                          'baseline_seconds':median(base),'reduced_seconds':median(new),
                          'ratio_baseline_over_reduced':median(base)/median(new)}
    return res

if __name__=='__main__':
    cli=argparse.ArgumentParser()
    cli.add_argument('--small',action='store_true')
    cli.add_argument('--benchmark',action='store_true')
    cli.add_argument('--output',default='PREFIX970_R6_EXACT_RESULTS.json')
    args=cli.parse_args()
    result=run(args.small,args.benchmark)
    with open(args.output,'w',encoding='utf-8') as f:json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
    print(json.dumps({'cases':result['small_cases'],'cache_builds':result['q19_k21']['cache']['index_builds'],
                      'cache_entries':result['q19_k21']['cache']['index_entries'],
                      'gaps':result['q19_k21']['gaps'],'benchmark':result.get('benchmark')},indent=2))
