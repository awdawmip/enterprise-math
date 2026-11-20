#!/usr/bin/env python3
"""PREFIX-969: exact interval-bounded modular bucket join for named XOR histories."""
from collections import Counter, defaultdict
from bisect import bisect_left
from hashlib import sha256
import argparse, json, time

EXPECTED = {
    1:(442,614,"ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71"),
    3:(839,1286,"1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3"),
    5:(3,3,"c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b")
}

def residuals(p):
    d=defaultdict(list)
    for i in range(p):
        for j in range(p):
            for sign in (-1,1):
                d[(1<<i)-sign*(1<<j)].append((i,j,sign))
    return {r:sorted((c,tuple(sl)) for c,sl in d.items() if c%2==r) for r in (0,1)}

def ceildiv(a,b):
    return -((-a)//b)

def join(p,k,m,bounded=True):
    assert p>=4 and k>=1 and k%2==1 and k+2<(1<<(p-1)) and m in (1,3,5)
    H=1<<(p-1);lo=H+1;hi=2*H-1
    r=residuals(p);out=[];cnt=Counter()
    for t in range(1,2*k+1):
        left=r[(1-t)%2];right=r[t%2]
        d=2*t-k*m
        assert d%2
        tab=defaultdict(list)
        for C,Cs in right: tab[(k*C)%abs(d)].append((C,Cs))
        cnt["bucket_entries"]+=len(right)
        cnt["bucket_queries"]+=len(left)
        for c,cs in left:
            bucket=tab[((k+2)*c)%abs(d)]
            cnt["congruence_candidates"]+=len(bucket)
            if bounded:
                dl=min(d*lo,d*hi);dh=max(d*lo,d*hi)
                a=max(ceildiv((k+2)*c+dl,k),ceildiv((t+m)*c+dl,t))
                b=min(((k+2)*c+dh)//k,((t+m)*c+dh)//t)
                if a>b:continue
                pool=bucket[bisect_left(bucket,(a,)):bisect_left(bucket,(b+1,))]
            else: pool=bucket
            cnt["range_candidates"]+=len(pool)
            for C,Cs in pool:
                N=k*C-(k+2)*c
                assert N%d==0
                b=N//d
                M=t*C-(t+m)*c
                assert M%d==0
                a=M//d
                if not(lo<=a<=hi and lo<=b<=hi):
                    if bounded:raise AssertionError("interval mismatch")
                    continue
                if a%2==0 or b%2==0 or a==b:continue
                cnt["odd_nondiagonal_pairs"]+=1
                lc=[(i,j) for i,j,s in cs if (((t*b+(1<<i))>>j)&1)==int(s==1)]
                rc=[(I,J) for I,J,s in Cs if ((((t+m)*b+(1<<I))>>J)&1)==int(s==1)]
                cnt["slot_checks"]+=len(cs)+len(Cs)
                for i,j in lc:
                    for I,J in rc:
                        assert ((k*a)^(1<<j))-(1<<i)==t*b
                        assert (((k+2)*a)^(1<<J))-(1<<I)==(t+m)*b
                        out.append((a,b,t,t+m,i,j,I,J))
    out.sort()
    h=sha256("".join(",".join(map(str,x))+"\n" for x in out).encode()).hexdigest()
    return out,dict(cnt),h

def direct(p,k,m):
    H=1<<(p-1);lo=H+1;hi=2*H-1;out=Counter()
    for a in range(lo,hi+1,2):
        left=defaultdict(list);right=defaultdict(list)
        for i in range(p):
            for j in range(p):
                x=((k*a)^(1<<j))-(1<<i)
                y=(((k+2)*a)^(1<<j))-(1<<i)
                if x>0:left[x].append((i,j))
                if y>0:right[y].append((i,j))
        for x,l in left.items():
            for y,r in right.items():
                z=y-x
                if z<=0 or z%m:continue
                b=z//m
                if b==a or b<lo or b>hi or b%2==0 or x%b:continue
                t=x//b
                if t>=1:
                    for i,j in l:
                        for I,J in r:out[(a,b,t,t+m,i,j,I,J)]+=1
    return out

def run(small=False,benchmark=False):
    cases=[]
    if small:
        for p in range(4,8):
            H=1<<(p-1)
            for k in range(1,H-2,2):
                for m in (1,3,5):
                    rows,_,_=join(p,k,m)
                    assert Counter(rows)==direct(p,k,m)
                    cases.append({"p":p,"k":k,"m":m,"count":len(rows)})
        assert len(cases)==168
    results=[]
    for m,(np,nw,want) in EXPECTED.items():
        before=time.perf_counter()
        named,counts,digest=join(19,21,m)
        elapsed=time.perf_counter()-before
        assert digest==want and len(named)==nw
        assert len(set((a,b) for a,b,*_ in named))==np
        row={"m":m,"modulus_pairs":np,"named_histories":nw,"named_sha256":digest,
             "counts":counts,"one_run_bounded_seconds":round(elapsed,6)}
        if benchmark:
            before=time.perf_counter()
            other,old,_=join(19,21,m,False)
            assert other==named
            row["old_counts"]=old
            row["one_run_unbounded_seconds"]=round(time.perf_counter()-before,6)
        results.append(row)
    return {"schema":"PREFIX969_R6_EXACT_REPRODUCTION_V1",
            "frozen_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
            "q19_k21":results,"small_cases":cases,
            "scientific_status":"AUTHOR_PROOF_EXACT_INTEGER_VERIFIED_NOT_REVIEWED"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--small",action="store_true")
    p.add_argument("--benchmark",action="store_true")
    p.add_argument("--output",default="PREFIX969_R6_RUN.json")
    args=p.parse_args()
    result=run(args.small,args.benchmark)
    with open(args.output,"w") as f:json.dump(result,f,indent=2);f.write("\n")
    print(json.dumps({"small_cases":len(result["small_cases"]),
                      "q19":result["q19_k21"]},indent=2))
