#!/usr/bin/env python3
"""Exact local q=12,24 crossover certificates for frozen 189-level stopping-time observer.
Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run: python PREFIX688_R6_CROSSING_BRACKETS.py 12 ends
     python PREFIX688_R6_CROSSING_BRACKETS.py 12 center
     python PREFIX688_R6_CROSSING_BRACKETS.py 24 ends
     python PREFIX688_R6_CROSSING_BRACKETS.py 24 center
     python PREFIX688_R6_CROSSING_BRACKETS.py 12 all
"""
from functools import lru_cache
from collections import defaultdict
from fractions import Fraction as Q
from math import comb
import json, sys
N, DEN = 189, 1 << 18
SCIENCE_PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
A3, B3 = 218571424275456, 69527880576

@lru_cache(None)
def accept(n,k,p):
    return 40*(n+1)*comb(n,k)*p**k*(DEN-p)**(n-k) > DEN**n

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
    if 4*(x-hi)>DEN:return True
    if 4*(y-lo)<DEN:return False
    raise ArithmeticError((n,k))

def frozen_rows():
    row={0:1};out=[]
    for n in range(N):
        out.append(row.copy());nextrow=defaultdict(int)
        for k,v in row.items():
            nextrow[k]+=v;nextrow[k+1]+=v
        row={k:v for k,v in nextrow.items() if alive(n+1,k)}
    assert not row and len(out)==189 and sum(map(len,out))==9529
    return out

def dot(a,b,kernel):
    s=Q(0)
    for i,u in enumerate(a):
        if u:
            for j,v in enumerate(b):
                if v:s+=u*v*kernel[i][j]
    return s

def jet(rows,p,max_order):
    a,d=p.numerator,p.denominator
    ap=[a**i for i in range(N+1)]
    cp=[(d-a)**i for i in range(N+1)]
    dp=[d**i for i in range(N+1)]
    res=[[] for _ in range(max_order+1)]
    for n,row in enumerate(rows):
        for j in range(max_order+1):
            numer=0
            for k,mult in row.items():
                for ell in range(j+1):
                    f=j-ell
                    if k<ell or n-k<f:continue
                    v1=v2=1
                    for u in range(ell):v1*=k-u
                    for u in range(f):v2*=n-k-u
                    numer+=mult*comb(j,ell)*v1*v2*(-1)**f*ap[k-ell]*cp[n-k-f]
            res[j].append(Q(numer,dp[n-j]) if n>=j else Q(0))
    return res

def getAB(rows,K,J,z,with_jet):
    js=jet(rows,z,2 if with_jet else 0)
    S=js[0];S0=[Q(row.get(0,0)) for row in rows]
    md=2*sum(S)-dot(S,S,K)
    me=sum(S0)+sum(S)-dot(S0,S,K)
    hd=2*sum((i+1)*S[i] for i in range(N))-dot(S,S,J)
    he=sum((i+1)*(S0[i]+S[i]) for i in range(N))-dot(S0,S,J)
    B=md-me;A=2*(hd-he)-md*md+me*me
    if not with_jet:return [A],[B]
    T,U=js[1],js[2]
    md1=2*sum(T)-2*dot(T,S,K)
    me1=sum(T)-dot(S0,T,K)
    hd1=2*sum((i+1)*T[i] for i in range(N))-2*dot(T,S,J)
    he1=sum((i+1)*T[i] for i in range(N))-dot(S0,T,J)
    md2=2*sum(U)-2*dot(U,S,K)-2*dot(T,T,K)
    me2=sum(U)-dot(S0,U,K)
    hd2=2*sum((i+1)*U[i] for i in range(N))-2*dot(U,S,J)-2*dot(T,T,J)
    he2=sum((i+1)*U[i] for i in range(N))-dot(S0,U,J)
    return [A,2*(hd1-he1)-2*(md*md1-me*me1),2*(hd2-he2)-2*(md1*md1+md*md2-me1*me1-me*me2)],[B,md1-me1,md2-me2]

def main(q):
    assert q in (12,24)
    l,h=({12:('0.0528706','0.0528708'),24:('0.0530655','0.0530659')})[q]
    lo,hi=Q(l),Q(h)
    c=(lo+hi)/2;r=(hi-lo)/2
    mode=sys.argv[2] if len(sys.argv)>2 else 'all'
    rows=frozen_rows()
    K=[[Q(comb(n+j,n),2**(n+j+1)) for j in range(N)]for n in range(N)]
    J=[[Q(n+j+1,2)*K[n][j] for j in range(N)]for n in range(N)]
    if mode in ('ends','all'):
        boundary=[]
        for z in (lo,hi):
            A,B=getAB(rows,K,J,z,False)
            F=q*A[0]-B[0]
            boundary.append({'z':str(z),'sign':1 if F>0 else -1 if F<0 else 0,
                             'F_floor_scaled_1e9':(F*10**9).__floor__(),
                             'A_positive':A[0]>0,'B_positive':B[0]>0})
        assert [v['sign'] for v in boundary]==[1,-1]
        assert all(v['A_positive'] and v['B_positive'] for v in boundary)
        if mode=='ends':
            print(json.dumps({'result':'ENDPOINTS_PASS','q':q,'endpoints':boundary},indent=2));return
    if mode in ('center','all'):
        A,B=getAB(rows,K,J,c,True)
        f1=q*A[1]-B[1];f2=q*A[2]-B[2]
        U=f1+abs(f2)*r+Q(q*A3+B3,2)*r*r
        assert U<0
        assert A[0]-abs(A[1])*r-abs(A[2])*r*r/2-Q(A3,6)*r**3>0
        assert B[0]-abs(B[1])*r-abs(B[2])*r*r/2-Q(B3,6)*r**3>0
        center={'midpoint':str(c),'radius':str(r),
                'jet_floors_1e6':{k:[(v*10**6).__floor__() for v in vals]
                                     for k,vals in [('A',A),('B',B)]},
                'F_prime_upper_floor':U.__floor__(),
                'F_prime_negative':True,'A_B_positive':True}
        if mode=='center':
            print(json.dumps({'result':'CENTER_PASS','q':q,**center},indent=2));return
    assert mode=='all'
    print(json.dumps({'result':'ALL_CHECKS_PASS PREFIX688-R6','q':q,
        'science_pin':SCIENCE_PIN,'levels':N,'survivor_cells':9529,
        'interval':[str(lo),str(hi)],'width':str(hi-lo),
        'endpoints':boundary,'center':center,'unique_local_zero':True,
        'method':'exact Python Fraction and integer recurrence'},indent=2))

if __name__=='__main__': main(int(sys.argv[1]))
