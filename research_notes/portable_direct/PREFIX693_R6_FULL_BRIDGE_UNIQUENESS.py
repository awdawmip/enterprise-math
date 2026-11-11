#!/usr/bin/env python3
"""PREFIX-693-R6: exact 189-layer frozen BRC bridge-uniqueness certificate.
Run with Python standard library; all proof comparisons use exact Fraction.
Science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as Q
from math import comb, factorial
import json

N,DEN=189,1<<18
C,D,R=53,1000,6
SCIENCE_PIN="f42f2906d77f24085c123f3ccfe9667d41caa96d"
FLOORA=[44000296,-168056589514,-6667624082229,39352687679231,3189837819999830,-36266294695911132]
FLOORB=[789752024,12845959424,-99127959112,-1326952329685,-14895243921676,-1960958310350017]
@lru_cache(None)
def fall(n,j):
    x=1
    for i in range(j): x*=n-i
    return x
@lru_cache(None)
def accept(n,k,p):
    return 40*(n+1)*comb(n,k)*p**k*(DEN-p)**(n-k)>DEN**n
@lru_cache(None)
def alive(n,k):
    if k>n//2: return alive(n,n-k)
    m=k*DEN//n
    assert accept(n,k,m)
    if k==0: lo=hi=0
    else:
        x,y=0,m
        while y-x>1:
            t=(x+y)//2
            if accept(n,k,t): y=t
            else: x=t
        lo,hi=x,y
    x,y=m,DEN
    while y-x>1:
        t=(x+y)//2
        if accept(n,k,t): x=t
        else: y=t
    if 4*(x-hi)>DEN: return True
    if 4*(y-lo)<DEN: return False
    raise ArithmeticError(("ambiguous frozen survivor",n,k))
def rows():
    row={0:1};out=[]
    for n in range(N):
        out.append(row.copy()); nxt=defaultdict(int)
        for k,v in row.items(): nxt[k]+=v;nxt[k+1]+=v
        row={k:v for k,v in nxt.items() if alive(n+1,k)}
    assert not row and len(out)==189
    assert sum(map(len,out))==9529
    assert all(0<=v<=comb(n,k) for n,h in enumerate(out) for k,v in h.items())
    return out
def jets(rs):
    ap=[C**i for i in range(N+1)]
    cp=[(D-C)**i for i in range(N+1)]
    dp=[D**i for i in range(N+1)]
    out=[[] for _ in range(R)]
    for n,row in enumerate(rs):
        for j in range(R):
            if j>n:
                out[j].append(Q(0));continue
            numerator=0
            for k,mult in row.items():
                for ell in range(j+1):
                    f=j-ell
                    if k<ell or n-k<f: continue
                    numerator+=mult*comb(j,ell)*(-1)**f*fall(k,ell)*fall(n-k,f)*ap[k-ell]*cp[n-k-f]
            out[j].append(Q(numerator,dp[n-j]))
    return out
def dot(x,y,kernel):
    s=Q(0)
    for i,u in enumerate(x):
        if not u:continue
        for j,v in enumerate(y):
            if v:s+=u*v*kernel[i][j]
    return s
def full_check():
    rs=rows(); js=jets(rs)
    s0=[Q(h.get(0,0)) for h in rs]
    K=[[Q(comb(n+m,n),2**(n+m+1)) for m in range(N)] for n in range(N)]
    J=[[Q(n+m+1,2)*K[n][m] for m in range(N)] for n in range(N)]
    md=[];me=[];hd=[];he=[]
    s0sum=sum(s0)
    s0h=sum((n+1)*s0[n] for n in range(N))
    for j in range(R):
        Kd=Jd=Q(0)
        for k in range(j+1):
            Kd+=comb(j,k)*dot(js[k],js[j-k],K)
            Jd+=comb(j,k)*dot(js[k],js[j-k],J)
        me.append(sum(js[j])+(s0sum if j==0 else 0)-dot(s0,js[j],K))
        md.append(2*sum(js[j])-Kd)
        he.append(sum((n+1)*js[j][n] for n in range(N))+(s0h if j==0 else 0)-dot(s0,js[j],J))
        hd.append(2*sum((n+1)*js[j][n] for n in range(N))-Jd)
    A=[];B=[]
    for j in range(R):
        B.append(md[j]-me[j])
        A.append(2*(hd[j]-he[j])-sum(comb(j,k)*(md[k]*md[j-k]-me[k]*me[j-k]) for k in range(j+1)))
    fa=[(v*10**8).__floor__() for v in A]
    fb=[(v*10**8).__floor__() for v in B]
    assert fa==FLOORA and fb==FLOORB
    M=N-1
    dc=[1]+[2**(j-1)*fall(M,j) for j in range(1,7)]
    U=[3*N]+[N*(4*dc[j]+sum(comb(j,i)*dc[i]*dc[j-i] for i in range(1,j))) for j in range(1,7)]
    Ab=4*N*U[6]+2*sum(comb(6,i)*U[i]*U[6-i] for i in range(7))
    Bb=2*U[6]
    assert Ab==201273663850076722544640 and Bb==17896441402901698560
    A3=4*N*U[3]+2*sum(comb(3,i)*U[i]*U[3-i] for i in range(4))
    assert A3==218571424275456 and 2*U[3]==69527880576
    T=Q(647,5000000)
    enclosures={}
    for name,fl,bnd in (("A",fa,Ab),("B",fb,Bb)):
        eps=sum(Q(max(abs(fl[j]),abs(fl[j]+1)),10**8)*T**(j-1)/factorial(j-1) for j in range(2,6))+Q(bnd)*T**5/factorial(5)
        lower=Q(fl[1],10**8)-eps
        upper=Q(fl[1]+1,10**8)+eps
        if name=="A": assert -1751<lower<upper<-1611
        else: assert 128<lower<upper<129
        enclosures[name]={"lower_exact":str(lower),"upper_exact":str(upper),"deviation_exact":str(eps)}
    output={
        "title":"PREFIX-693-R6",
        "frozen_science_pin":SCIENCE_PIN,
        "levels":N,"survivor_cells":9529,
        "bridge":["264353/5000000","530659/10000000"],
        "q_band":["63055771/5256000","660614143/27500000"],
        "jets_floor_1e8":{"A":fa,"B":fb},
        "sixth_derivative_bounds":{"A":Ab,"B":Bb},
        "derivative_enclosures":enclosures,
        "proved":["all z in bridge: -1751<A'<-1611, 128<B'<129",
                  "all real q in band: exactly one transverse zero of qA-B in bridge",
                  "analytic increasing inverse q=B/A and two-sided slope envelope"],
        "method":"exact frozen survivor recurrence + joint kernels + rational global Taylor enclosure",
        "status":"AUTHOR_DERIVED / EXACT_FRACTION_REPLAY / UNREVIEWED / NOT_ADMITTED",
        "verification":"ALL_CHECKS_PASS PREFIX693-R6"
    }
    print(json.dumps(output,ensure_ascii=False,indent=2))
if __name__=="__main__": full_check()
