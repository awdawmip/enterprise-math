#!/usr/bin/env python3
"""PREFIX-954 exact top-bit cross moment, parity-run method."""
import json
import time

def floor_sum(n,m,a,b):
    assert n>=0 and m>0 and a>=0 and b>=0
    ans=0
    while True:
        if a>=m:
            ans+=(n-1)*n*(a//m)//2
            a%=m
        if b>=m:
            ans+=n*(b//m)
            b%=m
        y=a*n+b
        if y<m:
            return ans
        n=y//m
        b=y%m
        m,a=a,m

def ceil_div(a,b):
    assert b>0
    return -(-a//b)

def top_runs(p,s):
    H=1<<(p-1); N=H//2; v0=s*(H+1); step=2*s
    qmin=v0//H
    qmax=(v0+step*(N-1))//H
    runs=[]
    for q in range(qmin,qmax+1):
        lo=max(0,ceil_div(q*H-v0,step))
        hi=min(N,ceil_div((q+1)*H-v0,step))
        if lo<hi and q%2==0:
            runs.append((lo,hi))
    return runs

def lower_zero_prefix(p,k,j,n):
    H=1<<(p-1); b=k*(H+1); a=2*k
    ones=floor_sum(n,1<<j,a,b)-2*floor_sum(n,1<<(j+1),a,b)
    return n-ones

def lower_top(p,k,l):
    return sum(lower_zero_prefix(p,k,j,hi)-lower_zero_prefix(p,k,j,lo)
               for lo,hi in top_runs(p,l)
               for j in range(1,p-1))

def top_top(p,k,l):
    left=top_runs(p,k);right=top_runs(p,l)
    i=j=0; answer=0
    while i<len(left) and j<len(right):
        a,b=left[i];c,d=right[j]
        answer+=max(0,min(b,d)-max(a,c))
        if b<=d:
            i+=1
        if d<=b:
            j+=1
    return answer

def sweep(p,k,l):
    return {
        "lower_k_top_l":lower_top(p,k,l),
        "top_k_lower_l":lower_top(p,l,k),
        "top_k_top_l":top_top(p,k,l),
        "top_runs_k":len(top_runs(p,k)),
        "top_runs_l":len(top_runs(p,l)),
    }

def direct(p,k,l):
    H=1<<(p-1);N=H//2
    ls_t=ts_l=tt=0
    for r in range(N):
        a=H+1+2*r;vk=k*a;vl=l*a
        lk=sum(((vk>>j)&1)==0 for j in range(1,p-1))
        ll=sum(((vl>>j)&1)==0 for j in range(1,p-1))
        tk=1-((vk>>(p-1))&1)
        tl=1-((vl>>(p-1))&1)
        ls_t+=lk*tl
        ts_l+=tk*ll
        tt+=tk*tl
    return {"lower_k_top_l":ls_t,"top_k_lower_l":ts_l,"top_k_top_l":tt}

def verify():
    t0=time.perf_counter(); checks=0
    for p in range(4,9):
        H=1<<(p-1)
        for k in range(1,H,2):
            for l in range(1,H,2):
                c=sweep(p,k,l); d=direct(p,k,l)
                for name,v in d.items():
                    assert c[name]==v,(p,k,l,name,c[name],v)
                for s in (k,l):
                    found={r for lo,hi in top_runs(p,s) for r in range(lo,hi)}
                    truth={r for r in range(H//2)
                           if ((s*(H+1+2*r)>>(p-1))&1)==0}
                    assert found==truth
                checks+=1
    for k in (1,3,5,21,23,127,129,251,255):
        for l in (1,3,5,21,23,127,129,251,255):
            c=sweep(9,k,l);d=direct(9,k,l)
            for name,v in d.items():
                assert c[name]==v,(9,k,l,name,c[name],v)
    result=sweep(19,21,23)
    observed=direct(19,21,23)
    for name,v in observed.items():
        assert result[name]==v,(name,result[name],v)
    assert observed=={
        "lower_k_top_l":532848,
        "top_k_lower_l":530485,
        "top_k_top_l":29848,
    }
    return {"scope":"auxiliary named XOR observer",
            "frozen_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
            "exhaustive_p4_to_p8_ordered_pairs":checks,
            "selected_p9_ordered_pairs":81,
            "p19_compressed":result,
            "p19_direct":observed,
            "integer_exact":True,
            "seconds_including_tests":round(time.perf_counter()-t0,5)}

if __name__=="__main__":
    print(json.dumps(verify(),indent=2))
