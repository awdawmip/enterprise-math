#!/usr/bin/env python3
"""Exhaustive observer-admissible cross-fiber native X6 LCP capacity table.
Uses the unchanged frozen EC49EXJ word/signature implementation.
"""
import argparse
from pathlib import Path
import sys, json
p=argparse.ArgumentParser()
p.add_argument('--source-dir',type=Path,default=Path(__file__).resolve().parent.parent/'EC49EXJ_H8_M4_S6_GLOBAL_EXACT')
a=p.parse_args()
sys.path.insert(0,str(a.source_dir))
from SCREEN_H5_EC49EXJ import words

def keys(h):
    for w in range(1,(h+1)//2+1):
        for u in range(2*h+3):
            for v in range(h+2):
                r=u+v-h-1; nf=h+1-v-2*w; ng=h+1-u
                if min(r,nf,ng)>=0 and (r>=1 or (r==0 and nf>=1 and ng>=1)):
                    yield (u,v,w), 4 if r>=1 else 2
families=[(h,k,t) for h in range(2,9) for k,t in keys(h)]
assert len(families)==164
children=[{}];mask=[0];depth=[0];total=0
for i,(h,k,t) in enumerate(families):
    for st,signature,operation_word in words(h,k,t):
        total+=1; node=0
        for signed_axis in st:
            if signed_axis not in children[node]:
                children[node][signed_axis]=len(children)
                children.append({});mask.append(0);depth.append(depth[node]+1)
            node=children[node][signed_axis]
            mask[node]|=1<<i
assert total==163888
n=len(families); caps=[[0]*n for _ in range(n)]
for node,m in enumerate(mask):
    if m.bit_count()<2: continue
    indices=[]
    while m:
        bit=m&-m;indices.append(bit.bit_length()-1);m-=bit
    for pos,i in enumerate(indices):
        for j in indices[pos+1:]:
            if depth[node]>caps[i][j]:caps[i][j]=depth[node]
strict=0
for i,(h,k,t) in enumerate(families):
    for j in range(i+1,n):
        hh,kk,tt=families[j]
        caps[j][i]=caps[i][j]
        I=2*(sum(min(x,y) for x,y in zip(k,kk))-1)
        if k!=kk:
            assert caps[i][j]<=I
            strict+=(caps[i][j]<I)
        else:
            assert caps[i][j]<=2*(sum(k)-1)-3
folder=Path(__file__).resolve().parent
header='# n families then rows: h u v w type cap[0] ... cap[n-1]\n'
rows=[str(n)]+[' '.join(map(str,(h,*k,t,*caps[i]))) for i,(h,k,t) in enumerate(families)]
(folder/'EC49EXY_CAPS_TABLE.txt').write_text(header+'\n'.join(rows)+'\n',encoding='utf-8')
report={'status':'PASS','families':n,'observer_admissible_words':total,'native_prefix_nodes_including_root':len(children),'distinct_key_family_pairs_strictly_tighter':strict,'pair_families_total':n*(n-1)//2}
(folder/'EC49EXY_CAPS_REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,sort_keys=True))
