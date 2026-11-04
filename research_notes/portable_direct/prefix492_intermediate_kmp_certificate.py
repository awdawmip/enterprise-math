#!/usr/bin/env python3
"""PREFIX-492 exact bounded KMP/BRC/source certificate, stdlib integers only."""
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb
ALPHABET='aAbBcCdDeE'
N,B,C=1,2,4
def obs(cc):
    y=tuple(cc[2*i]-cc[2*i+1] for i in range(5))
    p=[min(cc[2*i],cc[2*i+1]) for i in range(5)]
    return y,p[1]+2*p[3]+p[4],p[2]+p[4]
@lru_cache(None)
def kmp(q,ch,gate):
    s=gate[:q]+ch
    return next(i for i in range(len(gate),-1,-1) if s.endswith(gate[:i]))
def raw_dp(gate,nmax):
    states={(0,)*10+(0,N)}
    result={}
    for n in range(nmax+1):
        masks=[defaultdict(int) for _ in range(len(gate)+1)]
        for state in states:
            *cc,q,tag=state
            masks[q][obs(cc)] |= tag
        result[n]=[dict(v) for v in masks]
        if n==nmax:break
        nxt=set()
        for state in states:
            *cc,q,tag=state
            for j,ch in enumerate(ALPHABET):
                arr=list(cc);arr[j]+=1
                t=tag
                if tag==N:
                    if ch in 'bB':t=B
                    elif ch in 'cC':t=C
                nxt.add(tuple(arr)+(kmp(q,ch,gate),t))
        states=nxt
    return result
def comps(n,k):
    if k==1:
        yield (n,)
    else:
        for x in range(n+1):
            for r in comps(n-x,k-1):yield (x,)+r
def source_mask(pre,suffix):
    nb=pre[2]+pre[3];nc=pre[4]+pre[5]
    if nb and nc:return B|C
    if nb:return B
    if nc:return C
    for ch in suffix:
        if ch in 'bB':return B
        if ch in 'cC':return C
    return N
def suffix_predict(suffix,n):
    if n<len(suffix):return {}
    off=tuple(suffix.count(c) for c in ALPHABET)
    result=defaultdict(int)
    for pre in comps(n-len(suffix),10):
        cc=tuple(pre[i]+off[i] for i in range(10))
        result[obs(cc)] |= source_mask(pre,suffix)
    return dict(result)
def coeff(t):
    return sum(a*comb(t-j+7,7) for j,a in enumerate((1,2,3,4,2)) if t>=j) if t>=0 else 0
def terminal(word,gate):
    q=0
    for ch in word:q=kmp(q,ch,gate)
    return q
def pilot(gate,k):
    return {terminal('a'*i+'b'+'a'*(k-i),gate) for i in range(k+1)}
def test():
    for k in range(11):
        assert pilot('aab',k)==({0} if k==0 else {0,1} if k==1 else {1,2,3})
        assert pilot('aba',k)==({0} if k==0 else {1,2} if k==1 else {1,2,3})
    print('PILOT_ALL_K_0_TO_10_PASS')
    for gate in ('aab','aba'):
        states=raw_dp(gate,7)
        for n in range(8):
            q1=suffix_predict('a',n)
            if gate=='aab' and n>=2:
                pure=obs((n,)+(0,)*9)
                assert q1.pop(pure)==N
            q2=suffix_predict('aa' if gate=='aab' else 'ab',n)
            assert states[n][1]==q1,(gate,n,'q1')
            assert states[n][2]==q2,(gate,n,'q2')
            assert len(q1)==coeff(n-1)-(gate=='aab' and n>=2)
            assert len(q2)==coeff(n-2)
            ns=sum(bool(mask&N) for mask in q2.values())
            assert ns==(comb(n+3,5) if gate=='aab' and n>=2 else 0)
            print('KMP_SOURCE_MASK_PASS',gate,'n',n,'q1',len(q1),'q2',len(q2),'q2_Nsupport',ns,'q2_masks',dict(sorted(Counter(q2.values()).items())))
    print('ALL_CHECKS_PASS')
if __name__=='__main__':test()
