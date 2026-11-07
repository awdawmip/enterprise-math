#!/usr/bin/env python3
"""Stage512-B: exact structural quotient D_h (Python stdlib, no dependencies).
Frozen source: GK bf84bd7c, EM 2af3fc48, Stage509-B 94f52374,
Stage511-B 191cac08. Only authored mathematical/provenance-tag operations.
"""
from itertools import product
from time import perf_counter_ns
from tracemalloc import start, stop, get_traced_memory
import json


def fast(tags,h,R,S):
    """BFS over direction-free skeletons, inserted public tokens all = -1.
    Omit SET stutters; remember the shortest depth for any skeleton.
    """
    root=tuple(range(len(tags))); seen={root};front={root};D=set();scanned=0
    for depth in range(h):
        later=set()
        for w in front:
            scanned+=1;n=len(w)
            if n:
                if w[-1]>=0:D.add(w[-1])
                later.add(w[:-1])
            if n>=3:
                if w[-3]>=0:D.add(w[-3])
                later.add(w[:-3]+w[-2:])
            if n>=2:later.add(w[:-2]+(-1,)+w[-2:])
            for r in R:
                if r<n and w[n-1-r]>=0:D.add(w[n-1-r])
            ranked=[j for j in range(n-1,-1,-1) if w[j]<0 or tags[w[j]]]
            for k in S:
                if k<=len(ranked):
                    j=ranked[k-1]
                    if w[j]>=0:D.add(w[j])
                    later.add(w[:j]+w[j+1:])
        front=later-seen;seen.update(front)
    return frozenset(D),scanned


def old(tags,h,R,S):
    """Stage509-style identity/tag layer BFS incl. SET self loops.
    Fresh P insertions have per-depth negative identity.
    """
    front={tuple((i,int(t)) for i,t in enumerate(tags))};D=set();scanned=0
    for depth in range(h):
        later=set()
        for w in front:
            scanned+=1;n=len(w)
            if n:
                if w[-1][0]>=0:D.add(w[-1][0])
                later.add(w[:-1])
            if n>=3:
                if w[-3][0]>=0:D.add(w[-3][0])
                later.add(w[:-3]+w[-2:])
            if n>=2:later.add(w[:-2]+((-depth-1,1),)+w[-2:]) 
            for r in R:
                if r<n:
                    if w[n-1-r][0]>=0:D.add(w[n-1-r][0])
                    later.add(w)
            ranked=[j for j in range(n-1,-1,-1) if w[j][1]]
            for k in S:
                if k<=len(ranked):
                    j=ranked[k-1]
                    if w[j][0]>=0:D.add(w[j][0])
                    later.add(w[:j]+w[j+1:])
        front=later
    return frozenset(D),scanned


def full_F(word):
    """BRC joint observation: length, signed X6 displacement, 144 directed edges."""
    d=[0]*6;e=[0]*144
    for j,a in enumerate(word):
        d[a//2]+=1 if a%2==0 else -1
        if j:e[word[j-1]*12+a]+=1
    return len(word),tuple(d),tuple(e),word[0] if word else None,word[-1] if word else None


def join(x,y):
    if not x[0]:return y
    if not y[0]:return x
    e=[i+j for i,j in zip(x[2],y[2])];e[12*x[-1]+y[-2]]+=1
    return (x[0]+y[0],tuple(i+j for i,j in zip(x[1],y[1])),tuple(e),x[-2],y[-1])


def verify_F(tags,D):
    word=[(i*i+3*i+7)%12 for i in range(len(tags))]
    pieces=[];gap=[]
    for i,a in enumerate(word):
        if i in D:
            if gap:pieces.append(full_F(gap));gap=[]
            pieces.append(full_F([a]))
        else:gap.append(a)
    if gap:pieces.append(full_F(gap))
    state=full_F([])
    for p in pieces:state=join(state,p)
    assert state==full_F(word)


def measured(fn,tags,h,R,S):
    vals=[];peak=[];mask=None;nodes=None
    for _ in range(5):
        start();t=perf_counter_ns();mask,nodes=fn(tags,h,R,S)
        vals.append((perf_counter_ns()-t)/1e6)
        peak.append(get_traced_memory()[1]);stop()
    return {'mask':sorted(mask),'scanned':nodes,'median_ms':round(sorted(vals)[2],4),
            'max_tracemalloc_peak_bytes':max(peak)}


def main():
    count=0;full=0
    for n in range(2,9):
        patterns=product((0,1),repeat=n) if n<=6 else [tuple(i in z for i in range(n)) for z in ({0,2,5},{1,4,7},set(range(n)))]
        for tags in patterns:
            for h,R,S in ((1,(2,n-1),(1,3)),(2,(0,2,n-1),(1,2)),(3,(2,n-1),(1,3))):
                a,_=fast(tags,h,R,S);b,_=old(tags,h,R,S)
                assert a==b,(tags,h,R,S,a,b)
                verify_F(tags,a);count+=1;full+=1
    trials=[]
    for name,tags,h,R,S in (
        ('n19',tuple(i in {0,3,6,12,15,18} for i in range(19)),3,(2,11),(1,3)),
        ('n28',tuple(i in {0,20,24,26,27} for i in range(28)),2,(2,12),(1,2)),
        ('n28_h5',tuple(i in {0,5,10,17,20,24,26,27} for i in range(28)),5,(2,12),(1,3)),
        ('n100_h5',tuple(i%7==0 for i in range(100)),5,(2,61),(1,3))):
        a=measured(old,tags,h,R,S);b=measured(fast,tags,h,R,S)
        assert a['mask']==b['mask'];verify_F(tags,set(a['mask']))
        trials.append({'case':name,'h':h,'R':list(R),'S':list(S),'old':a,'quotient':b})
    return {'schema':'EM_STAGE512B_STRUCTURAL_QUOTIENT_V1',
      'comparisons':count,'exact_X6_BRC_F_checks':full+len(trials),
      'benchmarks':trials,'assertions':'PASS',
      'qualification':'5 timed Python tracemalloc repetitions per variant; single-process results, not system-independent speedups'}

if __name__=='__main__':print(json.dumps(main(),indent=2,ensure_ascii=False))
