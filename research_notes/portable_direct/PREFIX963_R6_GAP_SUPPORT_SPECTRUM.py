#!/usr/bin/env python3
"""Exact integer counts for the coarse necessary residual interval, not XOR sufficiency."""
import json
def formulas(p):
    assert p>=4
    N=1<<(p-2); R=N//2; q=(R-3)//3
    A6=0 if q<0 else (q+1)*(R-2)-3*q*(q+1)//2
    A=[N*N//2,N*N,N*N,(11*N*N+4)//12,N*N//2,(N*N-(-1)**p)//5,A6]
    D=[N//2,N,N,N,N//2,0,0]
    return dict(p=p,N=N,total=N*N,all=A,diagonal=D,off_diagonal=[x-y for x,y in zip(A,D)])
def interval_scan(p):
    N=1<<(p-2); H=2*N; A=[0]*7; D=[0]*7
    for z in range(N):
        u=2*z+1
        for m in range(7):
            lo=1-3*H-(2-m)*H+m*u
            hi=3*H-1-(2-m)*H+m*u
            # 4*r+2 lies between lo and hi.
            rmin=max(0,-((2-lo)//4))
            rmax=min(N-1,(hi-2)//4)
            if rmin<=rmax:
                A[m]+=rmax-rmin+1
                if rmin<=z<=rmax:D[m]+=1
    return A,D
def independent_pair_scan(p):
    N=1<<(p-2); H=2*N; A=[0]*7; D=[0]*7
    for z in range(N):
        b=H+2*z+1
        for r in range(N):
            a=H+2*r+1
            for m in range(7):
                delta=2*a-m*b
                if 1-3*H<=delta<=3*H-1:
                    A[m]+=1
                    if a==b:D[m]+=1
    return A,D
def main():
    results=[]
    for p in list(range(4,16))+[19]:
        expected=formulas(p)
        a,d=interval_scan(p)
        assert a==expected["all"] and d==expected["diagonal"], p
        if p<=9:
            a2,d2=independent_pair_scan(p)
            assert a2==a and d2==d,p
        expected["verification"]="exact interval scan + independent ordered-pair brute" if p<=9 else "exact interval scan"
        results.append(expected)
    output={"frozen_science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "model":"auxiliary_named_XOR_coarse_signed_residual_interval",
        "interval":"1-3H <= 2a-mb <= 3H-1",
        "necessary_only_not_XOR_sufficiency":True,
        "results":results}
    with open("PREFIX963_R6_EXACT_RESULTS.json","w",encoding="utf8") as f:
        json.dump(output,f,ensure_ascii=False,indent=2)
    print(json.dumps(results[-1],ensure_ascii=False))
if __name__=="__main__":main()
