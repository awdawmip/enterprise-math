#!/usr/bin/env python3
"""R762DT exact checker: sparse augmentation F3 and independent cyclic six-branch integer recurrence."""
from collections import defaultdict
import json, hashlib

F={(1,0,1):1,(1,1,0):2,(0,1,1):2,(1,1,1):1} # P(1+x,1+y,1+z) in F3

def step(c,Q):
    out=defaultdict(int)
    for (i,j,k),a in c.items():
        for (u,v,w),b in F.items():
            if i+u<Q and j+v<Q and k+w<Q:
                key=(i+u,j+v,k+w)
                out[key]=(out[key]+a*b)%3
    return {t:v for t,v in out.items() if v}

def pred(n):
    ones=twos=0
    while n:
        n,r=divmod(n,3)
        ones+=(r==1); twos+=(r==2)
    support=4**ones*10**twos
    imbalance=0 if ones else 6**twos
    return support,(support+imbalance)//2,(support-imbalance)//2

def verify():
    evidence={"schema":"EM_R762DT_AUTHOR_CHECK_V1",
              "arithmetic":"finite exact F3 sparse polynomial and integer cyclic mod 3^12",
              "status":"PASS","augmentation_cases":0,"runs":[]}
    for a in range(1,5):
        Q=3**a;c={(0,0,0):1}
        for n in range(Q):
            plus=sum(v==1 for v in c.values())
            minus=sum(v==2 for v in c.values())
            assert (len(c),plus,minus)==pred(n),(Q,n,"digit support")
            assert c.get((n,0,n))==1,(Q,n,"witness")
            evidence["augmentation_cases"]+=1
            c=step(c,Q)
        assert not c,(Q,"nilpotence")
        evidence["runs"].append({"Q":Q,"basis":"augmentation","checked_n":"0.."+str(Q-1),
                                 "nilpotence_at_Q":True})
    try:
        import numpy as np
        for Q,end in ((9,30),(27,85),(81,147)):
            d=Q//3; mod=3**12
            a=np.zeros((Q,Q,Q),dtype=np.int64);a[0,0,0]=1
            boundary=[]
            for n in range(1,end+1):
                b=a.copy()
                for axes in ((0,),(2,),(0,1),(1,2),(0,1,2)):
                    b+=np.roll(a,1,axis=axes)
                a=b%mod
                actual=0
                while actual<12 and not np.any(a%(3**(actual+1))):
                    actual+=1
                expected=max(0,n//d-2)
                assert actual==expected,(Q,n,actual,expected)
                assert int(a.sum()%mod)==pow(6,n,mod),("mass",Q,n)
                if n in (Q-1,Q,Q+d-1,Q+d,5*d-1,5*d):
                    boundary.append({"n":n,"v3":actual})
            evidence["runs"].append({
                "Q":Q,"basis":"cyclic monomial","checked_n":"1.."+str(end),
                "modulus":mod,"formula_disagreements":0,
                "boundary":boundary,
                "final_vector_digest_sha256":hashlib.sha256(a.tobytes()).hexdigest()})
    except ImportError:
        evidence["runs"].append({"cyclic_monomial":"SKIPPED_NUMPY_UNAVAILABLE"})
    return evidence

if __name__=="__main__":
    e=verify()
    with open("R762DT_EVIDENCE.json","w",encoding="utf-8") as f:
        json.dump(e,f,ensure_ascii=False,indent=2)
    print("PASS",e["augmentation_cases"],"augmentation exponents; ",
          [(r.get("Q"),r.get("checked_n")) for r in e["runs"]])
