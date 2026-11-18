#!/usr/bin/env python3
"""R749SUI exact integer certificate for auxiliary labeled WBRC Port bins."""
import json
from math import gcd, isqrt

def canonical(a,u,v,d):
    return a==d and abs(u-v)==2 and max(u,v)==a+1

def fast(M):
    best=0; winners=[]
    for u in range(1,M+1):
        if u==1:
            for a,U,v,d in [(1,1,1,2),(2,1,1,1)]:
                if a>M or d>M: continue
                z=U*a*d
                if z>best: best,winners=z,[(a,U,v,d)]
                elif z==best: winners.append((a,U,v,d))
            continue
        for a in range(1,M+1):
            if gcd(a,u)!=1:continue
            D=min(M,(u*u+1)//a); r=pow(a,-1,u)
            if D<r:continue
            d=r+u*((D-r)//u)
            if a*d<u+1:continue
            v=(a*d-1)//u
            assert 1<=v<=u and a*d-u*v==1
            if canonical(a,u,v,d):
                assert d==a and d<u
                continue
            z=u*a*d
            variants=[(a,u,v,d)] if u==v else [(a,u,v,d),(a,v,u,d)]
            if z>best:best,winners=z,variants
            elif z==best:winners+=variants
    return best, sorted(winners)

def brute(M):
    best=0; winners=[]; count=0
    for a in range(1,M+1):
      for d in range(1,M+1):
        p=a*d-1
        for u in range(1,M+1):
          if p%u:continue
          v=p//u
          if not 1<=v<=M:continue
          count+=1
          if canonical(a,u,v,d):continue
          z=max(u,v)*a*d
          if z>best:best,winners=z,[(a,u,v,d)]
          elif z==best:winners.append((a,u,v,d))
    return best,sorted(winners),count

def J(M,T):
    return sum((M-j+1)*(M-j)**2>T for j in range(1,M-1))

def witness(M):
    t=isqrt(M+1);m=t*t-1;delta=M-m
    assert t>=4 and 0<=delta<=2*t
    a=m-t;u=m;v=t*(t-2)
    assert 1<=a<=M and 1<=u<=M and 1<=v<=M
    assert a*a-u*v==1 and not canonical(a,u,v,a)
    return t,u*a*a

def run():
    count=0
    for M in range(2,97):
        A,W=fast(M);B,V,n=brute(M)
        assert (A,W)==(B,V),(M,A,B)
        count+=n
    assert count==360356,count
    for M in range(15,257):
        T,_=fast(M);t,W=witness(M)
        assert T>=W
        j=3*t
        assert j<=M-2 and W>(M-j+1)*(M-j)**2
        j0=max((k for k in range(1,M-1) if (3*k-1)**2<4*(M+1)),default=0)
        assert j0<=J(M,T)<=3*t-1
    cases=[]
    for M in (6,10,15,20,32,64,96,127,255,512,1024,2048):
        T,W=fast(M)
        cases.append({"M":M,"T_star":T,"multiplicity":len(W),"J":J(M,T),
                      "first_winner":list(W[0]),"q_values":sorted(set(u+v-a-d for a,u,v,d in W))})
    return {"status":"PASS","brute_M":[2,96],"brute_labeled_tuple_checks":count,
            "brute_vs_fast_cases":95,"uniform_M":[15,256],"uniform_cases":242,
            "additional_cases":cases,
            "scope":"labeled two-Port auxiliary WBRC feedback; exact Python integers"}

if __name__=="__main__":
    r=run()
    with open("R749SUI_UNIFORM_INTRUSION_RESULTS.json","w",encoding="utf-8") as f:
        json.dump(r,f,indent=2,ensure_ascii=False)
        f.write("\n")
    print("PASS",r["brute_labeled_tuple_checks"],r["uniform_cases"])
