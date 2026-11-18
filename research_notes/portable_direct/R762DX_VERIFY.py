#!/usr/bin/env python3
"""R762DX universal 27-subgroup quotient kernel: exact NumPy integer verifier.
Verified with Python 3 and numpy 2.3.5; no floats/approximations.
"""
import json
from collections import Counter, defaultdict
import numpy as np
S=((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))

def p(scale,q=27):
    out=defaultdict(int)
    for a,b,c in S: out[(a*scale%q,b*scale%q,c*scale%q)]+=1
    return dict(out)

def mul(a,b,q=27):
    out=defaultdict(int)
    for (i,j,k),v in a.items():
        for (x,y,z),w in b.items():out[((i+x)%q,(j+y)%q,(k+z)%q)]+=v*w
    return {k:v for k,v in out.items() if v}

def power(a,n,q=27):
    out={(0,0,0):1}
    for _ in range(n):out=mul(out,a,q)
    return out

def divdiff(a,b):
    keys=a.keys()|b.keys()
    d={k:(a.get(k,0)-b.get(k,0)) for k in keys}
    assert all(v%3==0 for v in d.values())
    return {k:v//3 for k,v in d.items() if v}

def direct(q,n,mod):
    a=np.zeros((q,q,q),dtype=np.int64);a[0,0,0]=1
    for _ in range(n):a=sum((np.roll(a,s,axis=(0,1,2)) for s in S))%mod
    return a

def one_step(a,mod):return sum((np.roll(a,s,axis=(0,1,2)) for s in S))%mod

def compute():
    B=p(1);C=p(3);A=p(9)
    T0=divdiff(power(B,3),C)
    T1=divdiff(power(C,3),A)
    A2=power(A,2);A3=power(A,3); C2=power(C,2)
    assert all(v%3==0 for v in A3.values())
    pieces=[{k:v//3 for k,v in A3.items()},
        {k:3*v for k,v in mul(A2,T1).items()},
        {k:9*v for k,v in mul(mul(A2,C2),T0).items()},
        {k:9*v for k,v in mul(A,mul(T1,T1)).items()},
        {k:9*v for k,v in mul(mul(T1,T1),T1).items()}]
    kernel=defaultdict(int)
    for part in pieces:
        for key,val in part.items():kernel[key]+=val
    K=np.zeros((27,27,27),dtype=np.int64)
    for key,val in kernel.items():K[key]=val%27
    D27=direct(27,27,81)
    assert np.all(D27%3==0) and np.array_equal(K,D27//3)
    hist=dict(sorted((str(x),int(c)) for x,c in Counter(K.ravel().tolist()).items()))
    expected={'0':9910,'2':13,'3':132,'5':6,'6':84,'9':4424,'12':120,'15':72,'18':4818,'20':8,'21':24,'24':72}
    assert hist==dict(sorted(expected.items())),hist
    valhist=[int(np.count_nonzero(K%3!=0)),int(np.count_nonzero((K%3==0)&(K%9!=0))),int(np.count_nonzero((K%9==0)&(K%27!=0)))]
    assert valhist==[27,504,9242]
    D81=direct(81,81,81)
    ix=np.indices((81,81,81))
    assert not np.count_nonzero((D81//3)[(ix%3!=0).any(axis=0)])
    assert np.array_equal(D81[::3,::3,::3]//3,K)
    strata=[]
    a=D81
    for r in range(3):
        c3=direct(3,r,27)
        s=int(np.count_nonzero(c3%3!=0))
        t=int(np.count_nonzero((c3%3==0)&(c3%9!=0)))
        u=int(np.count_nonzero((c3%9==0)&(c3%27!=0)))
        n1=int(np.count_nonzero((a%3==0)&(a%9!=0)))
        n2=int(np.count_nonzero((a%9==0)&(a%27!=0)))
        n3=int(np.count_nonzero((a%27==0)&(a%81!=0)))
        assert (n1,n2,n3)==(27*s,504*s+27*t,9242*s+504*t+27*u)
        strata.append({'q':81,'r':r,'S':s,'T':t,'U':u,'val1':n1,'val2':n2,'val3':n3})
        a=one_step(a,81)
    evidence={'theorem_id':'R762DX','author_result':'PASS','symbolic_kernel_modulus':27,'kernel_entries':19683,
       'kernel_mod27_histogram':hist,'quotient_valuation_classes':[27,504,9242,9910],
       'direct_checks':{'Q27_all':19683,'Q81_3_cases':3*81**3,'modulus_of_original_counts':81},
       'strata_Q81':strata,'method':'exact integer group-ring algebra vs cyclic recurrence (numpy int64)',
       'numpy_version':np.__version__,'independent_review':'NOT_REVIEWED'}
    print(json.dumps(evidence,indent=2,sort_keys=True)); return evidence
if __name__=='__main__':compute()
