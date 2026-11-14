#!/usr/bin/env python3
"""EC49FGL: exact raw-key support/primitive-length Pareto classification.
Run with EC49FGK 94-row catalogue; --full regenerates it from the frozen
BRC nine-state DFA and operation counts, no optimizer needed.
"""
import argparse
import itertools
import json
from collections import defaultdict
from functools import reduce
from math import comb
from pathlib import Path

OPS = 'acdefg'
T = ((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
     (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
     (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),
     6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
DEMANDS=[(h,s) for h,ss in REQ.items() for s in ss]
BIT={p:1<<i for i,p in enumerate(DEMANDS)}
FULL=(1<<len(DEMANDS))-1
FORCED={(2,1,1),(3,0,1),(3,1,1)}
A=1008; B=16776192

def read_catalogue(path):
    out={}
    for line in Path(path).read_text().splitlines():
        x,y,z,m=map(int,line.split()); key=(x,y,z)
        assert key not in out
        out[key]=m
    assert len(out)==94 and len(set(out.values()))==21
    return out

def rebuild_catalogue():
    out=defaultdict(int); matched=0
    for h,ss in REQ.items():
        for z in range(1,(h+1)//2+1):
            a=z-1; e=z
            for x in range(1,h+2):
                g=h+1-x
                for y in range(h+2):
                    b=x+y-h-1; f=h+1-y-2*z
                    if min(b,f,g)<0: continue
                    assert a+b+e+f+g==h
                    for c in range(b+1):
                        d=b-c
                        remaining=[a,c,d,e,f,g]
                        def visit(depth,state):
                            nonlocal matched
                            if depth==h:
                                sig=SIG[state]
                                if sig in ss:
                                    matched+=1
                                    out[x,y,z] |= BIT[h,sig]
                                return
                            for i in range(6):
                                if remaining[i] and T[state][i]!=8:
                                    remaining[i]-=1
                                    visit(depth+1,T[state][i])
                                    remaining[i]+=1
                        visit(0,0)
    assert matched==178850,(matched,len(out))
    return dict(out),matched

def binom(n,r): return comb(n,r) if 0<=r<=n else 0

def analyze(table):
    length={k:2*(sum(k)-1) for k in table}
    # Strict Pareto dominance: support inclusion and no-longer path.
    # Equal support and equal length do not count as domination.
    efficient={k for k,m in table.items() if not any(
        j!=k and (m|v)==v and length[j]<=length[k] and
        (v!=m or length[j]<length[k]) for j,v in table.items())}
    assert len(efficient)==14
    classes=defaultdict(list)
    for k in efficient: classes[table[k]].append(k)
    expected={1:1,2:1,12:1,1008:3,16776192:3,261120:4,15600:1}
    assert {k:len(v) for k,v in classes.items()}==expected
    assert FORCED<=efficient
    assert (table[(7,4,1)]|table[(6,4,1)])==table[(6,4,1)]
    assert (table[(6,5,1)]|table[(6,4,1)])==table[(6,4,1)]
    assert length[(7,4,1)]==length[(6,5,1)]==22
    assert length[(6,4,1)]==20
    keys=sorted(efficient)
    counts={};mincounts={}
    for k in range(0,15):
        n=binom(11,k-3)-2*binom(8,k-3)+binom(5,k-3)
        assert n>=0
        brute=0;minimal=0
        for subset in itertools.combinations(keys,k):
            mask=0
            for key in subset: mask|=table[key]
            if mask!=FULL: continue
            brute+=1
            if all(reduce(lambda mask,v: mask|table[v],
                          (v for v in subset if v!=key),0)!=FULL
                   for key in subset):
                minimal+=1
            assert FORCED <= set(subset)
            assert any(table[z]==A for z in subset)
            assert any(table[z]==B for z in subset)
        assert n==brute,(k,n,brute)
        if k>=5: assert minimal==(9 if k==5 else 0)
        counts[k]=n;mincounts[k]=minimal
    return {'key_count':len(table),'support_mask_classes':len(set(table.values())),
            'efficient_keys':[list(k) for k in keys],
            'efficient_masks':{str(m):len(v) for m,v in sorted(classes.items())},
            'all_efficient_cover_counts':counts,
            'inclusion_minimal_efficient_cover_counts':mincounts,
            'forced_efficient_core':[list(k) for k in sorted(FORCED)],
            'formula':'C(11,k-3)-2*C(8,k-3)+C(5,k-3)',
            'path_length_formula':'2*(x+y+z-1)',
            'dominated_profile_keys':[[7,4,1],[6,5,1]],
            'dominator':[6,4,1]}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('catalogue',nargs='?',default='EC49FGK_key_masks.txt')
    ap.add_argument('--full',action='store_true')
    ap.add_argument('--report',default='EXACT_REPORT_EC49FGL.json')
    args=ap.parse_args()
    table=read_catalogue(args.catalogue)
    if args.full:
        rebuilt,num=rebuild_catalogue()
        assert rebuilt==table,(len(rebuilt),len(table),set(rebuilt)^set(table))
        print('PASS frozen DFA catalogue: 94 keys,',num,'matching words')
    report=analyze(table)
    Path(args.report).write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print('PASS efficient',len(report['efficient_keys']),
          '5/6/7/8 covers',[report['all_efficient_cover_counts'][i] for i in (5,6,7,8)],
          'minimal 7',report['inclusion_minimal_efficient_cover_counts'][7])
if __name__=='__main__': main()
