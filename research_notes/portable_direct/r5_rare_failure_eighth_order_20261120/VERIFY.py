#!/usr/bin/env python3
"""Exact R5 seventh-order N^89 certificate. Pass --frozen /path/to/EXACT_R5_ALL_101_BUDGETS.json."""
import argparse, hashlib, json
from math import comb, factorial
from fractions import Fraction as Q
A=tuple(range(214,219)); S1=(214,216,217,218,219,220,221)
S2=(215,216,217,218,219,220,221)
B=tuple(range(219,315)); D=tuple(range(222,315)); J=219*220*221
PIN="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"

def moments(prices,m,order):
    state=[[0]*(order+1) for _ in range(m)];state[0][0]=1
    for p in prices:
        nxt=[[0]*(order+1) for _ in range(m)]
        for t in range(m):
            for n in range(m-t):
                w=p*n
                for r in range(order+1):
                    nxt[t+n][r]+=sum(comb(r,j)*state[t][j]*w**(r-j) for j in range(r+1))
        state=nxt
    return [sum(state[t][r] for t in range(m)) for r in range(order+1)]

def fourth_center(c,d):
    C=c*(c+3); D=d*(d+3)
    return Q(C*(2*c*c+6*c-3)+D*(2*d*d+6*d-3),30)+Q(C*D,6)

def overlap(m):
    K=Z=Y=T=U=0
    for a in range(m):
        for b in range(m):
            for c in range(m):
                nc=comb(c+2,2)
                for d in range(m):
                    r=int(a+b+c<m)+int(a+c+d<m)+int(b+c+d<m)
                    if r<2:continue
                    mult=(r-1)*nc*comb(d+2,2)
                    w=214*a+215*b+217*c+220*d
                    L=c*(c+3)+d*(d+3)
                    K+=mult;Z+=mult*w
                    Y+=Q(mult)*(w*w+Q(L,6))
                    T+=Q(mult)*(w**3+Q(w*L,2))
                    U+=Q(mult)*(w**4+w*w*L+fourth_center(c,d))
    assert all(Q(v).denominator==1 for v in (Y,T,U))
    return K,Z,int(Y),int(T),int(U)

def brute(m):
    K=Z=Y=T=U=0
    def visit(ns):
        nonlocal K,Z,Y,T,U
        if len(ns)==8:
            a,b,c,d,e,f,g,h=ns
            r=int(a+b+c+d+e<m)+int(a+c+d+e+f+g+h<m)+int(b+c+d+e+f+g+h<m)
            if r>=2:
                w=sum((214+i)*n for i,n in enumerate(ns))
                K+=r-1;Z+=(r-1)*w;Y+=(r-1)*w*w;T+=(r-1)*w**3;U+=(r-1)*w**4
            return
        for i in range(m):visit(ns+[i])
    visit([])
    return K,Z,Y,T,U

def laplace(prices,n):
    ps={a:sum(p**a for p in prices) for a in (1,2,4,6)}
    logs={1:Q(ps[1],2),2:-Q(ps[2],24),4:Q(ps[4],2880),6:-Q(ps[6],181440)}
    a=[Q(0)]*(n+1);a[0]=Q(1)
    for k in range(1,n+1):
        a[k]=sum(i*logs[i]*a[k-i] for i in logs if i<=k)/k
    return a

def laplace_direct(prices,n):
    a=[Q(1)]+[Q(0)]*n
    for p in prices:
        terms={0:Q(1),1:Q(p,2),2:Q(p*p,12),4:-Q(p**4,720),6:Q(p**6,30240)}
        a=[sum(a[k-j]*v for j,v in terms.items() if j<=k) for k in range(n+1)]
    return a

def calculate(m):
    M=moments(A,m,7);H1=moments(S1,m,5);H2=moments(S2,m,5)
    K,Z,Y,T,U=overlap(m);aB=laplace(B,7);aD=laplace(D,4)
    def coeff(t):
        five=sum(Q((-1)**r*M[r],factorial(r))*aB[t-r] for r in range(t+1))
        seven=Q(0)
        if t>=2:
            for e,H in ((215,H1),(214,H2)):
                aa=laplace(D+(e,),t-2)
                seven+=Q(J,e)*sum(Q((-1)**r*H[r],factorial(r))*aa[t-2-r] for r in range(t-1))
        eight=Q(0)
        if t>=3:
            v=(K,Z,Y,T,U)
            eight=-J*sum(Q((-1)**r*v[r],factorial(r))*aD[t-3-r] for r in range(t-2))
        return five+seven+eight
    return {"m":m,"K":K,"Z":Z,"Y":str(Y),"T":str(T),"U":str(U),
            "B90":str(coeff(5)),"B89":str(coeff(6)),"B88":str(coeff(7))}

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--frozen")
    a=parser.parse_args()
    frozen=None
    if a.frozen:
        frozen=hashlib.sha256(open(a.frozen,"rb").read()).hexdigest()
        assert frozen==PIN,(frozen,PIN)
    for m in (1,2,3):assert overlap(m)==brute(m),m
    for prices in (A,S1,S2,B,D,D+(214,),D+(215,)):
        assert laplace(prices,7)==laplace_direct(prices,7)
    rows=[calculate(m) for m in (1,2,3,5,8,17)]
    old={1:"192246796156363620657466/69015",
         2:"359266601447523294727347/23005",
         3:"1174433640911767046508132/23005",
         8:"31222014331713440926846364/23005",
         17:"404469051805687687736090238/23005"}
    for row in rows:
        if row["m"] in old:assert Q(row["B90"])==Q(old[row["m"]])
    past89={1:"10196399865022551484551495847/1739178",2:"75227314298019395022085336997/2318904",
            3:"17335829107232613089479681163/165636",
            5:"14702324295059436015789971471/27606",8:"502196328267106451533943421385/193242",
            17:"804852096580328159785507501667/27606"}
    for row in rows: assert Q(row["B89"])==Q(past89[row["m"]]),row
    print(json.dumps({"schema":"R5_RARE_FAILURE_N88_V1","pin_sha256":PIN,
          "frozen_actual_sha256":frozen,"bruteforce_m":[1,2,3],
          "prior_B90_match":[1,2,3,8,17],"laplace_independent_sets":7,
          "status":"AUTHOR_SYMBOLIC_PROOF / EXACT_FINITE_CHECKED / NOT_REVIEWED",
          "rows":rows},indent=2))
if __name__=="__main__":main()
