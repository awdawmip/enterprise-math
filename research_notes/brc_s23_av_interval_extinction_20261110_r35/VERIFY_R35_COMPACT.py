#!/usr/bin/env python3
"""R35 exact interval-output checker. Needs R34 VERIFY_R34_PREFIX.py.
Usage: python VERIFY_R35_COMPACT.py /path/to/VERIFY_R34_PREFIX.py
Frozen input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34
"""
import sys,importlib.util
from pathlib import Path
p=Path(sys.argv[1])
spec=importlib.util.spec_from_file_location('r34_reference',p)
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)

queries=0
def F(n,i,j):
    global queries
    queries+=1
    return sum(r.count(s,e,n-i,j)==0 for s,e in r.ARCS)

def stage(start,end,i,j,amp):
    cache={}
    def get(n):
        if n not in cache:cache[n]=F(n,i,j)
        return cache[n]
    out=[]
    def rec(a,b,fa,fb):
        d=fb-fa
        assert 0<=d<=b-a
        if d in (0,b-a):
            out.append((a+1,b,amp if d else (0,0)))
        else:
            x=(a+b)//2
            rec(a,x,fa,get(x));rec(x,b,get(x),fb)
    rec(start,end,get(start),get(end))
    return out

def push(segs,block):
    a,b,c=block
    if a>b:return
    if segs and segs[-1][1]+1==a and segs[-1][2]==c:
        segs[-1]=(segs[-1][0],b,c)
    else:segs.append(block)

def run():
    n=r.M;end=r.END
    value=r.risk_oracle(n);segs=[];stages=0;whole_queries=1
    while n<=end:
        a,i,c,j=r.farey(n);hi=min(end,i+j)
        d=r.amplitude(a,i,c,j)
        blocks=stage(n,hi,i,j,d)
        for block in blocks:push(segs,block)
        value=(value[0]+sum((b-a+1)*v[0] for a,b,v in blocks),
               value[1]+sum((b-a+1)*v[1] for a,b,v in blocks))
        assert r.risk_oracle(hi)==value
        whole_queries+=1;stages+=1
        if hi==end:break
        nxt=r.risk_oracle(hi+1);whole_queries+=1
        push(segs,(hi+1,hi+1,(nxt[0]-value[0],nxt[1]-value[1])))
        n=hi+1;value=nxt
    expected=[(129,164,(16,-61)),(165,292,(-43,164)),
              (293,328,(0,0)),(329,389,(-43,164))]
    assert segs==expected,(segs,expected)
    assert value==(-7551,28800)
    assert stages==3 and queries==19 and whole_queries==6
    print('EXACT',segs,'R389',value,'F_QUERY_COUNT',queries)
    print('PASS_R35_COMPACT_INTERVAL_CERT')

if __name__=='__main__':run()
