#!/usr/bin/env python3
"""R36 exact batched fibre-extinction checker (S23 frozen auxiliary observer).
Usage: python VERIFY_R36_COMPACT.py /path/to/VERIFY_R34_PREFIX.py
Source input: Enterprise Math @43ec6098b1330ae86d0a7863be336c5d97f6ef34.
"""
import sys, importlib.util
from pathlib import Path
from bisect import bisect_left, bisect_right
spec=importlib.util.spec_from_file_location('r34_pin',Path(sys.argv[1]))
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
PHASES=sorted((t*r.P)%r.Q for t in r.ORDER)
queries=0; lookups=0; rank_counts=0; last_by_arc=[]

def prepare(first,i,j):
    """Compute owner-labelled final-source vector once for the Farey stage."""
    global lookups,rank_counts,last_by_arc
    low=first-i; source_count=j-low
    last=[None]*r.M
    if source_count<=2*r.M:
        for t in range(low,j):
            k=(bisect_right(PHASES,(t*r.P)%r.Q)-1)%r.M
            last[k]=t;lookups+=1
    else:
        for k,(s,e) in enumerate(r.ARCS):
            rank_counts+=1
            if r.count(s,e,low,j)==0:continue
            left,right=low,j
            while left+1<right:
                mid=(left+right)//2;rank_counts+=1
                if r.count(s,e,mid,j)>0:left=mid
                else:right=mid
            last[k]=left
    last_by_arc.append(last)
    return sorted(t for t in last if t is not None)

def stage(first,end,i,j,amp):
    global queries
    last=prepare(first,i,j)
    cache={}
    def get(n):
        global queries
        if n not in cache:
            cache[n]=r.M-len(last)+bisect_left(last,n-i)
            queries+=1
        return cache[n]
    blocks=[]
    def rec(a,b,fa,fb):
        d=fb-fa
        assert 0<=d<=b-a
        if not d or d==b-a:
            if a<b:blocks.append((a+1,b,amp if d else (0,0)))
            return
        x=(a+b)//2;y=get(x)
        rec(a,x,fa,y);rec(x,b,y,fb)
    rec(first,end,get(first),get(end))
    return blocks

def push(segs,block):
    l,h,d=block
    if l>h:return
    if segs and segs[-1][1]+1==l and segs[-1][2]==d:
        segs[-1]=(segs[-1][0],h,d)
    else:segs.append(block)

def main():
    n=r.M; value=r.risk_oracle(n); runs=[];stages=0
    while n<=r.END:
        a,i,c,j=r.farey(n);hi=min(i+j,r.END)
        amp=r.amplitude(a,i,c,j)
        blocks=stage(n,hi,i,j,amp)
        for b in blocks:push(runs,b)
        value=(value[0]+sum((h-l+1)*d[0] for l,h,d in blocks),
               value[1]+sum((h-l+1)*d[1] for l,h,d in blocks))
        assert value==r.risk_oracle(hi)
        stages+=1
        if hi==r.END:break
        next_value=r.risk_oracle(hi+1)
        push(runs,(hi+1,hi+1,(next_value[0]-value[0],next_value[1]-value[1])))
        n=hi+1;value=next_value
    expected=[(129,164,(16,-61)),(165,292,(-43,164)),
              (293,328,(0,0)),(329,389,(-43,164))]
    assert runs==expected and value==(-7551,28800)
    assert stages==3 and queries==19 and lookups==259 and rank_counts==0
    assert all(len(a)==r.M for a in last_by_arc)
    print('R36 PREFIX',runs,'F QUERIES',queries,'OWNER LOOKUPS',lookups)
    print('PASS_R36_COMPACT_BATCH_EXTINCTION')
if __name__=='__main__':main()
