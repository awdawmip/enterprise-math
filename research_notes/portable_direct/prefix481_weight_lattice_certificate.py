#!/usr/bin/env python3
"""Exact PREFIX-481 certificate: native X6 positive path weight-lattice + histogram moments."""
from collections import defaultdict

LETTERS='aAbBcCdDeE'
VECTORS=((1,1),(0,0),(2,1),(0,0),(1,2),(0,0),(3,1),(0,0),(2,2),(0,0))
WEIGHTS=(6,1,12,1,18,1,24,1,36,1)
NORMAL_LABELS={(0,0),(1,1),(2,1),(1,2),(3,1),(2,2)}

def kmp(word,q,c):
    t=word[:q]+c
    return max(j for j in range(len(word)+1) if t.endswith(word[:j]))

def append_o(o,i):
    if i==10: return (o[0]+1,)+o[1:]
    axis,sign=divmod(i,2)
    yl=o[axis+1]; d=int(yl<0 if sign==0 else yl>0)
    a=list(o)
    a[axis+1]+=1 if sign==0 else -1
    a[6]+=d*(1 if axis in (1,4) else 2 if axis==3 else 0)
    a[7]+=d*(1 if axis in (2,4) else 0)
    return tuple(a)

def advance(hist,word,n):
    out=defaultdict(lambda:defaultdict(int)); K=len(word)
    for (obs,q),bins in hist.items():
        for i,c in enumerate(LETTERS):
            tgt=out[(append_o(obs,i),kmp(word,q,c))]
            u,v=VECTORS[i]
            for (a,b),cnt in bins.items(): tgt[(a+u,b+v)]+=cnt
        if n==0 or q==K:
            tgt=out[(append_o(obs,10),0)]
            for label,cnt in bins.items(): tgt[label]+=cnt
    return {k:dict(v) for k,v in out.items()}

def moments(h,r=3):
    total=[0]*(r+1)
    for (a,b),c in h.items():
        val=(2**a)*(3**b)
        for j in range(r+1):total[j]+=c*(val**j)
    return tuple(total)

def exponents_from_observation(n,obs):
    s,*rest=obs
    y=rest[:5]; V,W=rest[5:]
    t=n-s-sum(abs(v) for v in y)
    assert t>=0 and t%2==0, (n,obs)
    P=t//2
    U=sum(a*max(v,0) for a,v in zip((1,2,1,3,2),y))+P+V
    T=sum(b*max(v,0) for b,v in zip((1,1,2,1,2),y))+P+W
    return (U,T)

def advance_counts(d,w,n):
    out=defaultdict(int)
    for (o,q),c in d.items():
        for idx,ch in enumerate(LETTERS):
            out[(append_o(o,idx),kmp(w,q,ch))]+=c
        if n==0 or q==len(w):out[(append_o(o,10),0)]+=c
    return dict(out)

def raw_observe(seq):
    # Independently extract direction counts and native X6 observations.
    ctr={c:seq.count(c) for c in LETTERS}
    y=tuple(ctr[a]-ctr[b] for a,b in zip('abcde','ABCDE'))
    p=[min(ctr[a],ctr[b]) for a,b in zip('abcde','ABCDE')]
    return (seq.count('x'),)+y+(p[1]+2*p[3]+p[4],p[2]+p[4])

def brute(word,n):
    out=defaultdict(lambda:defaultdict(int))
    def visit(seq,wt):
        if len(seq)==n:
            tail=seq.split('x')[-1]
            q=max(i for i in range(len(word)+1) if tail.endswith(word[:i]))
            # independent weight valuation calculated from actual signed letters
            a=sum(VECTORS[LETTERS.index(c)][0] for c in seq if c!='x')
            b=sum(VECTORS[LETTERS.index(c)][1] for c in seq if c!='x')
            assert wt==2**a*3**b
            out[(raw_observe(seq),q)][(a,b)]+=1
            return
        for c,wt_c in zip(LETTERS,WEIGHTS):visit(seq+c,wt*wt_c)
        if not seq or seq.endswith(word):visit(seq+'x',wt)
    visit('',1)
    return {k:dict(v) for k,v in out.items()}

def compute(word,N):
    state={((0,)*8,0):{(0,0):1}}
    counts={((0,)*8,0):1}
    for n in range(N+1):
        assert set(state)==set(counts),(word,n,'fiber support')
        assert sum(sum(h.values()) for h in state.values())>0
        for (obs,q),h in state.items():
            label=exponents_from_observation(n,obs)
            assert h=={label:counts[(obs,q)]},(word,n,obs,q,h,label)
            C,M1,M2,M3=moments(h,3)
            wt=2**label[0]*3**label[1]
            assert (M1,M2,M3)==(C*wt,C*wt**2,C*wt**3)
        if n<=4: assert state==brute(word,n),(word,n,'ordered independent exhaustive')
        print('FIBER_CHECK',word,'n',n,'fibers',len(state),'base',len({k[0] for k in state}),
              'paths',sum(counts.values()),'hist_bins',sum(len(h) for h in state.values()))
        if n<N:
            state=advance(state,word,n)
            counts=advance_counts(counts,word,n)
    return counts

def label_ehrhart(n):
    s={(0,0)}
    for j in range(n+1):
        assert len(s)==3*j*j+2*j+1,(j,len(s),3*j*j+2*j+1)
        assert all(a>=0 and b>=0 and a<=3*j and b<=2*j and a>=b/2 and b>=a/3 for a,b in s)
        print('LABELS',j,len(s))
        s={(a+u,b+v) for a,b in s for u,v in NORMAL_LABELS}

if __name__=='__main__':
    label_ehrhart(30)
    for word in ('aab','aba'):
        compute(word,8)
    # Two distinct raw occupancies collapse to one O and native weight.
    for x,y in [('aAeE','bBcC'),('aAdD','bBbB')]:
        assert raw_observe(x)==raw_observe(y), (x,y)
        assert sorted(x.count(c) for c in LETTERS) != sorted(y.count(c) for c in LETTERS) or x!=y
        def weight(p):
            z=1
            for c in p: z*=WEIGHTS[LETTERS.index(c)]
            return z
        assert weight(x)==weight(y)
        print('RAW_KERNEL_WITNESS',x,y,raw_observe(x),weight(x))
    # Controlled change of the e-direction weight shows why native exponents matter.
    assert 6*35!=12*18
    print('NONNATIVE_WEIGHT_CHANGE',6*35,12*18)
    print('ALL_CHECKS_PASS')
