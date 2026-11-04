#!/usr/bin/env python3
"""PREFIX-491: exact native-X6/BRC full-KMP-suffix and source-support certificate.
Pure stdlib arbitrary-precision integers; no numerical approximations.
"""
from collections import defaultdict, Counter
from functools import lru_cache
from math import comb

ALPHABET='aAbBcCdDeE'
N,B,C=1,2,4

def obs(counts):
    y=tuple(counts[2*i]-counts[2*i+1] for i in range(5))
    p=[min(counts[2*i],counts[2*i+1]) for i in range(5)]
    return y,p[1]+2*p[3]+p[4],p[2]+p[4]

@lru_cache(None)
def kmp(q,ch,gate):
    s=gate[:q]+ch
    return next(i for i in range(len(gate),-1,-1) if s.endswith(gate[:i]))

def full_dp(gate,nmax):
    states={(0,)*10+(0,N)}
    result={}
    for n in range(nmax+1):
        masks=defaultdict(int)
        for state in states:
            *cc,q,tag=state
            if q==len(gate): masks[obs(cc)]|=tag
        result[n]=dict(masks)
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

def compositions(n,k):
    if k==1:
        yield (n,)
    else:
        for v in range(n+1):
            for rest in compositions(n-v,k-1):
                yield (v,)+rest

def prefix_support(cc,gate):
    nb=cc[2]+cc[3]; nc=cc[4]+cc[5]
    if nb and nc:return B|C
    if nb:return B
    if nc:return C
    for ch in gate:
        if ch in 'bB':return B
        if ch in 'cC':return C
    return N

def suffix_predict(gate,n):
    L=len(gate)
    if n<L:return {}
    off=[gate.count(ch) for ch in ALPHABET]
    fibers=defaultdict(int)
    for pre in compositions(n-L,10):
        cc=[pre[i]+off[i] for i in range(10)]
        fibers[obs(cc)]|=prefix_support(pre,gate)
    return dict(fibers)

def exact_base_coefficient(k):
    if k<0:return 0
    return sum(a*comb(k-j+7,7) for j,a in enumerate((1,2,3,4,2)) if k>=j)

def exhaustive_lattice(m):
    image=set()
    for pa in range(m+1):
      for pb in range(m-pa+1):
       for pc in range(m-pa-pb+1):
        for pd in range(m-pa-pb-pc+1):
         pe=m-pa-pb-pc-pd
         image.add((pb+2*pd+pe,pc+pe))
    exp={(v,w) for w in range(m+1) for v in range(2*m-w+1)}
    assert image==exp
    return len(image)

def test():
    for m in range(13):
        assert exhaustive_lattice(m)==(m+1)*(3*m+2)//2
    print('POLYGON_SATURATION_EXHAUSTIVE_M0_TO12_PASS')
    gates=('aab','aba','aa','aB','aAc','bca')
    for gate in gates:
        L=len(gate)
        for n in range(L,11):
            got=suffix_predict(gate,n)
            pred=exact_base_coefficient(n-L)
            assert len(got)==pred,(gate,n,len(got),pred)
            print('SUFFIX_FIBER_TOTAL_PASS',gate,n,len(got),'source_mask_counts',dict(sorted(Counter(got.values()).items())))
    print('ALL_GATE_TOTALS_N_LE10_PASS')
    for gate in gates:
        result=full_dp(gate,7)
        for n in range(0,8):
            exp=suffix_predict(gate,n)
            assert result[n]==exp,(gate,n,len(result[n]),len(exp),next(((x,result[n].get(x),exp.get(x)) for x in set(result[n])|set(exp) if result[n].get(x)!=exp.get(x)),None))
        print('RAW_ORDER_KMP_AGREEMENT_N0_TO7_PASS',gate)
    for n in range(3,11):
        a=suffix_predict('aab',n); b=suffix_predict('aba',n)
        assert a==b,(n,a,b)
    print('EQUAL_MULTISET_AND_FIRST_SOURCE_POINTWISE_MASK_N3_TO10_PASS')
    for n in range(11):
        def signed5(k):
            return sum(comb(5,i)*comb(k-i+4,4) for i in range(min(k,5)+1))
        total=sum(signed5(n-2*m)*(m+1)*(3*m+2)//2 for m in range(n//2+1))
        assert total==exact_base_coefficient(n)
    print('UNRESTRICTED_GENERATING_FUNCTION_COEFFICIENTS_N0_TO10_PASS')
    print('ALL_CHECKS_PASS')
if __name__=='__main__':test()
