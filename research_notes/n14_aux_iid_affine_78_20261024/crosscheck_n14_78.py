#!/usr/bin/env python3
"""Ordered-word DFS crosscheck, independent algorithm but shared stopping table."""
from fractions import Fraction as F
from collections import Counter
import json
import verify_n14_78 as a
P,Q=a.P,a.Q

def first_hits(target):
    hits=[]
    def walk(st,p,q):
        if st==target:
            hits.append((p,q));return
        if st[0]>=target[0] or a.act(st)!='C':return
        for i in range(3):walk(a.child(st,i),p*P[i],q*Q[i])
    walk((0,0,0),F(1),F(1))
    return len(hits),sum((p for p,q in hits),F()),sum((q for p,q in hits),F())

def suffix_words(target):
    sums=[F(),F(),F(),F()];ends=Counter()
    def walk(st,p,q,t):
        z=a.act(st)
        if z!='C':
            ends[(st,z)]+=1
            if z=='Q':sums[0]+=p
            else:sums[1]+=q
            sums[2]+=t*p;sums[3]+=t*q
            return
        for i in range(3):walk(a.child(st,i),p*P[i],q*Q[i],t+1)
    walk(target,F(1),F(1),0)
    return tuple(sums),sum(ends.values()),len(ends)

def check():
    result={}
    for name,st in [('A',a.A),('B',a.B)]:
        k,p,q=first_hits(st)
        r,words,states=suffix_words(st)
        assert (p,q,k)==a.firsthit(st)
        assert r==a.suffix(st)
        result[name]={'live':k,'p':str(p),'q':str(q),'suffix_words':words,
                       'terminal_states':states,'truncated_paths':k*words}
    assert result['A']['live']==5 and result['A']['suffix_words']==275
    assert result['A']['truncated_paths']==1375
    assert result['B']['live']==12 and result['B']['suffix_words']==5
    return result
if __name__=='__main__':print(json.dumps(check(),indent=2))
