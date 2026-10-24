"""R248 author-side exact tests for typed BRC effect-histogram claims.
Finite 1-axis affine specialization of 6-axis maps; not native package execution.
Run: python research_notes/R248_verify_effect_histograms.py
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json

I=(1,0); R=(-1,0); T=(1,1)
def compose(first,later):
    """(f then g)(x)=g(f(x))."""
    return later[0]*first[0], later[0]*first[1]+later[1]
def serial(a,b):
    out=defaultdict(int)
    for f,c in a.items():
        for g,d in b.items():
            out[compose(f,g)]+=c*d
    return dict(out)
def moments(hist):
    return [sum(cnt*effect[1]**k for effect,cnt in hist.items()) for k in range(4)]

h={I:1}; translation_results=[]
for n in range(19):
    m=moments(h)
    assert len(h)==n+1 and sum(h.values())==2**n
    assert m[1]==(0 if n==0 else n*2**(n-1))
    assert m[2]==(0 if n==0 else (1 if n==1 else n*(n+1)*2**(n-2)))
    translation_results.append((n,len(h),m[0],m[1],m[2]))
    h=serial(h,{I:1,T:1})

def matrices(edges,n=3,effects=(I,R)):
    idx={(s,e):s*len(effects)+i for s in range(n) for i,e in enumerate(effects)}
    out={}
    for label,es in edges.items():
        m=[[0]*(n*len(effects)) for _ in range(n*len(effects))]
        for src,dst,effect,cnt in es:
            for h in effects:
                m[idx[(dst,compose(h,effect))]][idx[(src,h)]]+=cnt
        out[label]=m
    return out,idx

def mul(matrix,vec):
    return tuple(sum(x*y for x,y in zip(row,vec)) for row in matrix)

def rowrank(rows):
    a=[[Fraction(x) for x in row] for row in rows]
    if not a: return 0
    r=0
    for j in range(len(a[0])):
        piv=next((i for i in range(r,len(a)) if a[i][j]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        coef=a[r][j];a[r]=[x/coef for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][j]:
                coef=a[i][j];a[i]=[x-coef*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def observation(vec,labels,n=3,effects=(I,R)):
    out=defaultdict(int)
    for s in range(n):
        for i,e in enumerate(effects):
            out[labels[s],e]+=vec[s*len(effects)+i]
    return tuple(out.get((label,e),0) for label in sorted(set(labels)) for e in effects)

def shortest_or_certificate(edges,labels=(0,0,0),start=(0,1)):
    maps,idx=matrices(edges)
    size=len(idx);v=[0]*size
    v[idx[start[0],I]]=1;v[idx[start[1],I]]-=1
    nodes=[("",tuple(v))];span=[];i=0
    while i<len(nodes):
        word,vec=nodes[i];i+=1
        if any(observation(vec,labels)):
            return dict(status="WITNESS",word=word,length=len(word),basis_before=len(span))
        if rowrank(span+[vec])==len(span):continue
        span.append(vec)
        for a in sorted(maps): nodes.append((word+a,mul(maps[a],vec)))
    return dict(status="EQUIVALENT",invariant_span_rank=len(span))

edges={"a":[(0,2,I,1),(1,0,I,1),(2,2,R,1)],
       "b":[(0,0,I,1),(1,1,I,1),(2,2,I,1)]}
delayed=shortest_or_certificate(edges)
assert delayed["word"]=="aa" and delayed["length"]==2
equiv=shortest_or_certificate({
    "a":[(s,0,I,1) for s in range(3)],
    "b":[(s,0,I,1) for s in range(3)]})
assert equiv["status"]=="EQUIVALENT"

hist0={(1,k):4 for k in range(4)}
hist1={(1,0):5,(1,1):1,(1,2):7,(1,3):3}
assert moments(hist0)[:3]==moments(hist1)[:3]==[16,24,56]
assert moments(hist0)[3]==144 and moments(hist1)[3]==138
print(json.dumps(dict(status="PASS",translation_n_max=18,
    translation_m18=translation_results[18],
    delayed=delayed,all_future_equivalent=equiv,
    collision_moments0=moments(hist0),
    collision_moments1=moments(hist1)),sort_keys=True))
