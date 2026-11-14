#!/usr/bin/env python3
"""Generate all observer-compatible L-3 suffix-pair graph capacities for H=2..8.
Uses the frozen signed X6 operation codes and nine-history observer from EC49EXJ.
No floating point or task-state assumptions. Run: python GENERATE_EC49EXS.py
"""
from collections import defaultdict, Counter
from itertools import product, combinations
from functools import lru_cache
from pathlib import Path
import json

OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
H=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')
SIG4=(1836687,1867942,1872656,1873981)
SIG2=(1836425,1866380)

# Entire signal is driven by every signed native step, including negative steps.
def native(w): return tuple(x for c in w for x in OPS[c])
def sig(st):
    n=0;mul=1
    for ev,prev in H:
        for s in st:
            if prev==1 and s==2:
                if ev=='N': ev='A'
                elif ev=='B': ev='BA'
            elif prev==2 and s==1:
                if ev=='N': ev='B'
                elif ev=='A': ev='AB'
            prev=s
        n+=BUCKETS.index(ev)*mul;mul*=5
    return n

def families(h):
    ans={}
    for w in range(1,(h+1)//2+1):
        for u in range(0,2*h+3):
            for v in range(0,h+2):
                r=u+v-h-1;f=h+1-v-2*w;g=h+1-u
                if min(r,f,g)<0:continue
                t=4 if r>=1 else (2 if f>=1 and g>=1 else 0)
                if t:ans[(u,v,w)]=t
    return ans

F={h:families(h) for h in range(2,9)}
assert [len(F[h]) for h in range(2,9)]==[1,4,9,17,28,43,62]

# All possible exact L-3 pairs are P+c <-> P+fg or P+d <-> P+gf;
# P has h-1 operations (h<=7) and still satisfies #e=#a+1.
EDGES=defaultdict(set); WITNESS={}; raw_counts=Counter(); eligible_counts=Counter()
for h in range(2,8):
    for p in product('acdefg',repeat=h-1):
        if p.count('e')!=p.count('a')+1:continue
        pre=''.join(p)
        for long,short in (('c','fg'),('d','gf')):
            w1=pre+long;w2=pre+short
            st1=native(w1);st2=native(w2)
            assert len(st1)==len(st2) and sorted(st1)==sorted(st2)
            key=tuple(st1.count(j) for j in (1,2,3))
            assert key==tuple(st2.count(j) for j in (1,2,3))
            raw_counts[h]+=1
            t1,t2=F[h].get(key,0),F[h+1].get(key,0)
            if not(t1 and t2):continue
            s1,s2=sig(st1),sig(st2)
            if s1 in (SIG4 if t1==4 else SIG2) and s2 in (SIG4 if t2==4 else SIG2):
                eligible_counts[h]+=1
                EDGES[(h,key)].add((s1,s2))
                WITNESS.setdefault((h,key,s1,s2),(w1,w2))

def old_match(hs,m):
    if len(hs)<=1:return 0
    if len(hs)==2:return min(m) if hs[1]==hs[0]+1 else 0
    a,b,c=hs;x=b==a+1;y=c==b+1
    if x and y:return min(m[1],m[0]+m[2])
    if x:return min(m[0],m[1])
    if y:return min(m[1],m[2])
    return 0

@lru_cache(None)
def exact_match(hs,key):
    # Match distinct observation-signature slots; edges represent an actual
    # signed-native suffix rewrite. Allowing independent edges is an upper
    # bound on simultaneous prefix-sharing possibilities, hence safely used.
    vertices=tuple((h,s) for h in hs for s in (SIG4 if F[h][key]==4 else SIG2))
    mask_neighbor=[0]*len(vertices)
    for i,(h,s) in enumerate(vertices):
        for j,(t,q) in enumerate(vertices):
            if t==h+1 and (s,q) in EDGES.get((h,key),()):
                mask_neighbor[i]|=1<<j
                mask_neighbor[j]|=1<<i
    @lru_cache(None)
    def calc(av):
        if av==0:return 0
        b=av&-av;i=b.bit_length()-1
        best=calc(av^b)
        opts=mask_neighbor[i]&(av^b)
        while opts:
            t=opts&-opts;opts-=t
            best=max(best,1+calc(av^b^t))
        return best
    return calc((1<<len(vertices))-1)

rows=[];miss=[]
for n in (2,3):
    for hs in combinations(range(2,9),n):
        common=set(F[hs[0]])
        for h in hs[1:]:common.intersection_update(F[h])
        for key in sorted(common):
            types=[F[h][key] for h in hs]
            old=old_match(hs,types)
            new=exact_match(hs,key)
            assert 0<=new<=old
            rows.append((n,*(list(hs)+[0]*(3-n)),*key,old,new))
            if new<old:miss.append({'windows':hs,'key':key,'types':types,'EXQ_matching':old,'EXS_matching':new})
OUT=Path(__file__).resolve().parent
with (OUT/'EC49EXS_MATCH_TABLE.txt').open('w') as f:
    f.write('# n h1 h2 h3 u v w nu_EXQ nu_EXS\n')
    for row in rows:f.write(' '.join(map(str,row))+'\n')
summary={'status':'PASS','model':'frozen H8/M5/S<=6 signed X6 nine-history observer',
         'pair_raw_count':{str(h):raw_counts[h] for h in range(2,8)},
         'pair_eligible_count':{str(h):eligible_counts[h] for h in range(2,8)},
         'distinct_eligible_pair_edges':sum(len(v) for v in EDGES.values()),
         'matching_table_rows':len(rows),'strict_improvements':len(miss),
         'improved_cases':miss,
         'base_h2_h3_pair_cap':0,
         'proof_check':'all 6^(h-1) possible prefixes P for h=2..7 (and all suffix rewrites c<->fg, d<->gf) are covered; exact integer signature recurrence'}
(OUT/'EC49EXS_MATCH_GENERATION.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='improved_cases'},indent=2))
