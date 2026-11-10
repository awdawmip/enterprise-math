#!/usr/bin/env python3
"""PREFIX-680-R6. Frozen 189-layer BRC diagonal/edge crossover, exact certificate.
Stdlib only: arbitrary-precision Python integers and Fraction; no floating inference.
Frozen science: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as Q
from math import comb
import json

N, DEN, b_num, b_den = 189, 1 << 18, 53, 1000

@lru_cache(None)
def accept(n, k, p):
    return 40*(n+1)*comb(n,k)*p**k*(DEN-p)**(n-k) > DEN**n

@lru_cache(None)
def alive(n,k):
    if k > n//2: return alive(n,n-k)
    m=k*DEN//n
    assert accept(n,k,m)
    if k==0: lo=hi=0
    else:
        x,y=0,m
        while y-x>1:
            mid=(x+y)//2
            if accept(n,k,mid): y=mid
            else: x=mid
        lo,hi=x,y
    x,y=m,DEN
    while y-x>1:
        mid=(x+y)//2
        if accept(n,k,mid): x=mid
        else: y=mid
    if 4*(x-hi)>DEN: return True
    if 4*(y-lo)<DEN: return False
    raise ArithmeticError(("ambiguous frozen survivor",n,k))

def frozen_rows():
    row={0:1}
    out=[]
    for n in range(N):
        out.append(row.copy())
        nxt=defaultdict(int)
        for k,v in row.items():
            nxt[k]+=v
            nxt[k+1]+=v
        row={k:v for k,v in nxt.items() if alive(n+1,k)}
    assert len(out)==189 and not row
    assert sum(map(len,out))==9529
    assert all(0<=v<=comb(n,k) for n,h in enumerate(out) for k,v in h.items())
    return out

def jet(rows):
    a,d=b_num,b_den
    ap=[a**i for i in range(N+1)]
    cp=[(d-a)**i for i in range(N+1)]
    dp=[d**i for i in range(N+1)]
    res=[[],[],[]]
    for n,h in enumerate(rows):
        for j in range(3):
            if j>n:
                res[j].append(Q(0))
                continue
            numer=0
            for k,mult in h.items():
                for ell in range(j+1):
                    f=j-ell
                    if k<ell or n-k<f: continue
                    v1=v2=1
                    for u in range(ell): v1*=k-u
                    for u in range(f): v2*=n-k-u
                    numer += mult*comb(j,ell)*v1*v2*(-1)**f*ap[k-ell]*cp[n-k-f]
            res[j].append(Q(numer,dp[n-j]))
    return res

def dot(a,b,kernel):
    s=Q(0)
    for i,u in enumerate(a):
        if not u: continue
        for j,v in enumerate(b):
            if v: s+=u*v*kernel[i][j]
    return s

def main():
    rows=frozen_rows()
    S,S1,S2=jet(rows)
    S0=[Q(row.get(0,0)) for row in rows]
    K=[[Q(comb(n+m,n),2**(n+m+1)) for m in range(N)] for n in range(N)]
    J=[[Q(n+m+1,2)*K[n][m] for m in range(N)] for n in range(N)]
    # mu(p,z)=sum(s_p+s_z)-K[s_p,s_z]; H=E[Y^2]/2.
    md=2*sum(S)-dot(S,S,K)
    me=sum(S0)+sum(S)-dot(S0,S,K)
    md1=2*sum(S1)-2*dot(S1,S,K)
    me1=sum(S1)-dot(S0,S1,K)
    md2=2*sum(S2)-2*dot(S2,S,K)-2*dot(S1,S1,K)
    me2=sum(S2)-dot(S0,S2,K)
    hd=2*sum((n+1)*S[n] for n in range(N))-dot(S,S,J)
    he=sum((n+1)*(S0[n]+S[n]) for n in range(N))-dot(S0,S,J)
    hd1=2*sum((n+1)*S1[n] for n in range(N))-2*dot(S1,S,J)
    he1=sum((n+1)*S1[n] for n in range(N))-dot(S0,S1,J)
    hd2=2*sum((n+1)*S2[n] for n in range(N))-2*dot(S2,S,J)-2*dot(S1,S1,J)
    he2=sum((n+1)*S2[n] for n in range(N))-dot(S0,S2,J)
    B0,B1,B2=md-me,md1-me1,md2-me2
    A0=2*(hd-he)-md**2+me**2
    A1=2*(hd1-he1)-2*(md*md1-me*me1)
    A2=2*(hd2-he2)-2*(md1**2+md*md2-me1**2-me*me2)
    c=B0/A0
    cp=(B1*A0-B0*A1)/A0**2
    cpp=((B2*A0-B0*A2)*A0-2*(B1*A0-B0*A1)*A1)/A0**3
    vals=dict(A0=A0,A1=A1,A2=A2,B0=B0,B1=B1,B2=B2,c=c,cp=cp,cpp=cpp)
    floors={k:(v*10**8).__floor__() for k,v in vals.items()}
    assert floors=={
      "A0":44000296,"A1":-168056589514,"A2":-6667624082229,
      "B0":789752024,"B1":12845959424,"B2":-99127959112,
      "c":1794878866,"cp":6884631251314,"cpp":52862665534319204}
    # Uniform Bernstein derivative bounds on [0,1/2], N=189, M=188.
    M=N-1
    D2=2*M*(M-1)
    D3=4*M*(M-1)*(M-2)
    U0=3*N
    U1=4*N*M
    U2=N*(4*D2+2*M*M)
    U3=N*(4*D3+6*M*D2)
    H3=N*N*(4*D3+6*M*D2)
    W3=2*H3+6*U1*U2+2*U0*U3
    A3,B3=2*W3,2*U3
    assert (A3,B3)==(218571424275456,69527880576)
    r=Q(1,625000)
    ea=abs(A1)*r+abs(A2)*r*r/2+Q(A3,6)*r**3
    eb=abs(B1)*r+abs(B2)*r*r/2+Q(B3,6)*r**3
    amin,amax=A0-ea,A0+ea
    bmin,bmax=B0-eb,B0+eb
    assert amin>Q(437,1000)>0 and amax<Q(444,1000)
    assert bmin>Q(789,100) and bmax<Q(791,100)
    app=abs(A2)+A3*r
    bpp=abs(B2)+B3*r
    lip=bpp*amax+bmax*app
    R0=B1*A0-B0*A1
    rmin,rmax=R0-lip*r,R0+lip*r
    assert 0<rmin and rmin/amax**2>45000
    assert rmax/amin**2<100000
    qmin,qmax=Q(447,25),Q(901,50)
    assert c-45000*r<qmin<qmax<c+45000*r
    assert Q(0)<Q(53,1000)-r<Q(53,1000)+r<Q(1,2)
    assert (qmax-qmin)/Q(19,100000)==Q(14000,19)
    result={
      "title":"PREFIX-680-R6","frozen_science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
      "model":"189-level frozen survivor / independent Poissonized maximum clocks",
      "survivor_cells":sum(map(len,rows)),
      "center":"53/1000","radius":"1/625000",
      "q_range":["447/25","901/50"],
      "slope_guarantee":"45000 < q0'(z) < 100000",
      "uniform_third_derivative_bounds":{"A3":A3,"B3":B3},
      "exact_center_jet_floors_1e8":floors,
      "strict_enclosure_floor":{"Rmin":int(rmin),"slope_min":int(rmin/amax**2),
                                "slope_max_upper_ceil":int(rmax/amin**2)+1},
      "certified_q_width_gain_vs_PREFIX678":"14000/19",
      "arithmetic":"Python int / Fraction, no float evidence",
      "result":"ALL_CHECKS_PASS",
      "status":"AUTHOR_DERIVED / EXACT_INTEGER_FRACTION_RECOMPUTED / UNREVIEWED / NOT_ADMITTED"
    }
    print("PREFIX680_EXACT_PASS",json.dumps(result,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
