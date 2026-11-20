#!/usr/bin/env python3
"""PREFIX-952: independent integer floor-sum verification and small-width brute."""
import csv
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def floor_sum(n,m,a,b):
    """Exact sum of floor((a*r+b)/m) for 0<=r<n; m>0,a,b>=0."""
    z=0
    while True:
        if a>=m:
            z+=(n-1)*n*(a//m)//2
            a%=m
        if b>=m:
            z+=n*(b//m)
            b%=m
        y=a*n+b
        if y<m:return z
        n=y//m
        b=y%m
        m,a=a,m

def first_moment(p,k):
    H=1<<(p-1);M=2*H;N=H//2
    assert p>=3 and 1<=k<H and k%2==1
    top_ones=floor_sum(N,H,2*k,k*(H+1))-2*floor_sum(N,M,2*k,k*(H+1))
    assert 0<=top_ones<=N
    top_zeros=N-top_ones
    bonus=2 if k>=3 else 0
    return ((p-2)*N)//2+top_zeros+bonus,top_zeros,bonus

def verify_q19(csv_path="PREFIX952_PER_CORE_Q19.csv"):
    rows=list(csv.DictReader((ROOT/csv_path).open()))
    assert len(rows)==4096
    tot=tz=b=0
    for row in rows:
        k=int(row["k"])
        m,z,bonus=first_moment(19,k)
        assert m==int(row["witness_total"]),(k,m,row["witness_total"])
        assert z==int(row["top_zero_count"]),k
        assert bonus==int(row["rescue_bonus"]),k
        tot+=m;tz+=z;b+=bonus
    assert (tot,tz,b)==(4831509378,268098436,8190)
    return {"cores_checked":len(rows),"sum_witnesses":tot,
            "sum_top_zero":tz,"sum_bonus":b}

def brute_small():
    cases=0; total=0;sample=[]
    for p in range(3,9):
        H=1<<(p-1); M=2*H
        for k in range(1,H,2):
            s=0
            for a in range(H+1,M,2):
                v=k*a
                found=[]
                for i in range(p):
                    for j in range(p):
                        q=(v^(1<<j))-(1<<i)
                        if q>0 and q%a==0:found.append((i,j,q//a))
                zero_bits=p-(v&(M-1)).bit_count()
                asserted=zero_bits+(2 if (a==H+1 and k>=3) else 0)
                assert len(found)==asserted,(p,k,a,found,asserted)
                if (p,k,a)==(7,63,65):sample=found
                s+=len(found)
            assert s==first_moment(p,k)[0],(p,k,s)
            cases+=1;total+=s
    assert cases==126 and sample==[(0,6,62),(6,0,62)]
    return {"p_k_cases":cases,"witnesses":total,
            "p7_k63_a65_source_triples":sample}

if __name__=="__main__":
    out={"schema":"PREFIX952_INDEPENDENT_FLOORSUM_BRUTE_V1",
         "q19":verify_q19(),"small_width":brute_small(),"passed":True}
    (ROOT/"PREFIX952_R6_INDEPENDENT_RESULTS.json").write_text(
      json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(out,ensure_ascii=False,indent=2))
