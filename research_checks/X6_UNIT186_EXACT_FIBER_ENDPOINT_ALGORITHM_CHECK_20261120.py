#!/usr/bin/env python3
"""Independent exact-integer verification of six-axis signed-X6 endpoint fiber inversion.
The adapter is new research code; not the frozen native R063 benchmark.
"""
import hashlib, itertools, json, random
from collections import defaultdict

def q(z):
    h=min(z)
    return tuple(x-h for x in z)

def bounds(M, a):
    if not isinstance(M,int) or M < 0 or len(a)!=6 or min(a)!=0 or any(not isinstance(x,int) or x<0 for x in a):
        raise ValueError('invalid finite horizon/relative observer')
    if (M-sum(a))%2:
        return None
    s=sorted(a)
    S=sum(s)
    B=[2*sum(s[6-t:])-S if t else -S for t in range(7)]
    if B[3]>M:
        return None
    lower=max(-((M-B[t])//(6-2*t)) for t in range(3)) # ceil((B-M)/positive) == -floor((M-B)/positive)
    upper=min((M-B[t])//(2*t-6) for t in range(4,7))
    if lower>upper:
        return None
    return lower,upper

def reference(M,a):
    if (M-sum(a))%2: return None
    v=[h for h in range(-M,M+1) if sum(abs(x+h) for x in a)<=M]
    return (v[0],v[-1]) if v else None

def relation(a):
    return tuple(tuple(ai-aj for aj in a) for ai in a)

def restore_from_field(M,Z,j):
    a=tuple(max(row) for row in Z)
    hspan=bounds(M,a)
    if hspan is None or not (0<=j<=hspan[1]-hspan[0]): raise ValueError('not feasible')
    h=hspan[0]+j
    C=sum(a)+6*h
    # Frozen A3 source consumer formula with six unit-capacity blocks:
    # c_i = (C + sum_j Z_ij)/6, plus closure and C consistency.
    z=[]
    for row in Z:
        numerator=C+sum(row)
        if numerator%6: raise ValueError('non-integral')
        z.append(numerator//6)
    if sum(z)!=C or relation(tuple(z))!=Z: raise ValueError('not closed')
    return tuple(z)

def ref_binary(M,a):
    if (M-sum(a))%2: return None
    f=lambda h:sum(abs(x+h) for x in a)
    # Median interval gives a global minimum.  h0=-sorted(a)[2].
    h0=-sorted(a)[2]
    if f(h0)>M: return None
    lo,hi=-M,h0
    while lo<hi:
        mid=(lo+hi)//2
        if f(mid)<=M: hi=mid
        else: lo=mid+1
    L=lo
    lo,hi=h0,M
    while lo<hi:
        mid=(lo+hi+1)//2
        if f(mid)<=M: lo=mid
        else: hi=mid-1
    return L,lo

def run():
    totals=defaultdict(int); active={t:0 for t in (0,1,2,4,5,6)}
    for M in range(0,11):
        # All endpoints in the six-axis signed primitive M-step graph; no word enumeration.
        endpoints={ (0,0,0,0,0,0) }
        # Rebuild per horizon to keep exact populations explicit.
        for _ in range(M):
            nextset=set()
            for z in endpoints:
                for i in range(6):
                    for sign in (-1,1):
                        w=list(z);w[i]+=sign;nextset.add(tuple(w))
            endpoints=nextset
        groups=defaultdict(set)
        for z in endpoints:
            groups[q(z)].add(min(z))
        for a,hs in groups.items():
            got=bounds(M,a)
            want=reference(M,a)
            if got!=want or hs!=set(range(want[0],want[1]+1)):
                raise RuntimeError(('fiber mismatch',M,a,got,want))
            sorted_a=sorted(a); S=sum(sorted_a)
            B=[2*sum(sorted_a[6-t:])-S if t else -S for t in range(7)]
            for t in (0,1,2):
                if got[0]==-((M-B[t])//(6-2*t)): active[t]+=1
            for t in (4,5,6):
                if got[1]==(M-B[t])//(2*t-6):active[t]+=1
            for h in hs:
                z=tuple(x+h for x in a)
                if restore_from_field(M,relation(z),h-got[0])!=z:
                    raise RuntimeError(('field repair mismatch',M,z))
                totals['field_recoveries']+=1
            totals['fibers']+=1
        maxfiber=max(map(len,groups.values()))
        if maxfiber != M//3+1:
            raise RuntimeError(('sharp-bit mismatch',M,maxfiber))
        totals['all_endpoints']+=len(endpoints)
        totals['horizon_'+str(M)+'_fibers']=len(groups)
        totals['horizon_'+str(M)+'_endpoints']=len(endpoints)
    rng=random.Random(18620261120)
    for case in range(3000):
        M=rng.randrange(0,10**15)
        a=[rng.randrange(0,10**14) for _ in range(6)]
        a[rng.randrange(6)]=0
        if rng.randrange(2): M+=(sum(a)-M)%2
        expected=ref_binary(M,tuple(a))
        computed=bounds(M,tuple(a))
        if computed!=expected:
            raise RuntimeError(('large-M mismatch',case,M,a,computed,expected))
        totals['large_exact_integer_cases']+=1
    totals['violations']=0
    result={'schema':'X6_UNIT186_EXACT_FIBER_BOUNDS_CERT_V1','science_pin':'59538f585d037d09ef687b28715c4bc1a3f9fe03','historical_source_pin':'fd2bcff10ca6e147348b6c1236027fc0d2877df3','model':'six signed primitive axes; anchored 0; endpoint at exactly M steps; q(z)=z-min(z)1','formula':'B_t=2 sum(top t a)-sum(a), L=max_{t=0,1,2} ceil((B_t-M)/(6-2t)), U=min_{t=4,5,6} floor((M-B_t)/(2t-6)), require B_3<=M and parity M=sum(a) mod2','counts':dict(totals),'active_affine_constraints':active,'mode':'EXACT_INTEGER_ALWAYS_RAISES_ON_MISMATCH','original_R063_native_benchmark_executed':False,'native_progress_submitted':False,'review_status':'UNREVIEWED_NOT_ADMITTED'}
    print(json.dumps(result,sort_keys=True,separators=(',',':'),ensure_ascii=False))

if __name__=='__main__':run()
