#!/usr/bin/env python3
"""PREFIX-698-R6: exact 189-row BRC endpoints + rational uniform-derivative bridge.

Frozen science: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
Spatial observer chart: z in [211/4000,213/4000], q real.
Model: two labelled branches Y(z,z), Y(0,z), not native X6 evolution.
No floating point participates in any theorem check.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, factorial
import json

N=189
DEN=1<<18
D=4000
BASE=2*D
B=Q(53,1000)
H=Q(1,4000)
LEFT=B-H
RIGHT=B+H
PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
FLOOR_A=(44000296,-168056589514,-6667624082229,
         39352687679231,3189837819999830,-36266294695911132)
FLOOR_B=(789752024,12845959424,-99127959112,
         -1326952329685,-14895243921676,-1960958310350017)
M_A=201273663850076722544640
M_B=17896441402901698560

@lru_cache(None)
def accepted(n,k,p):
    return 40*(n+1)*comb(n,k)*p**k*(DEN-p)**(n-k)>DEN**n

@lru_cache(None)
def alive(n,k):
    if k>n//2:return alive(n,n-k)
    m=k*DEN//n
    assert accepted(n,k,m)
    if not k:lo=hi=0
    else:
        a,b=0,m
        while b-a>1:
            p=(a+b)//2
            if accepted(n,k,p):b=p
            else:a=p
        lo,hi=a,b
    a,b=m,DEN
    while b-a>1:
        p=(a+b)//2
        if accepted(n,k,p):a=p
        else:b=p
    if 4*(a-hi)>DEN:return True
    if 4*(b-lo)<DEN:return False
    raise ValueError(('ambiguous survivor cell',n,k))

def survivor_rows():
    row={0:1};allrows=[]
    for n in range(N):
        allrows.append(row.copy())
        nextrow=defaultdict(int)
        for k,c in row.items():
            nextrow[k]+=c
            nextrow[k+1]+=c
        row={k:c for k,c in nextrow.items() if alive(n+1,k)}
    assert not row
    assert sum(len(row) for row in allrows)==9529
    assert all(c<=comb(n,k) for n,row in enumerate(allrows) for k,c in row.items())
    return allrows

def endpoint_at(rows,t,weights,common_denominator):
    """Exact K/J moments at z=t/4000, K_nm=C(n+m,n)/2**(n+m+1),
    J_nm=(n+m+1)*K_nm/2. Common denominator absorbs D powers.
    """
    u=[sum(c*t**k*(D-t)**(n-k) for k,c in row.items()) for n,row in enumerate(rows)]
    v=[int(row.get(0,0))*D**n for n,row in enumerate(rows)]
    denom=[D**n for n in range(N)]
    sx=sum(Q(u[n],denom[n]) for n in range(N))
    sy=sum(Q(v[n],denom[n]) for n in range(N))
    hx=sum(Q((n+1)*u[n],denom[n]) for n in range(N))
    hy=sum(Q((n+1)*v[n],denom[n]) for n in range(N))
    xxK=xxJ=yxK=yxJ=0
    for n in range(N):
        if u[n]==v[n]==0:continue
        for m in range(N):
            wt=weights[n][m]
            xx=u[n]*u[m]*wt
            yx=v[n]*u[m]*wt
            xxK+=xx;xxJ+=(n+m+1)*xx
            yxK+=yx;yxJ+=(n+m+1)*yx
    md=2*sx-Q(xxK,common_denominator)
    me=sx+sy-Q(yxK,common_denominator)
    hd=2*hx-Q(xxJ,2*common_denominator)
    he=hx+hy-Q(yxJ,2*common_denominator)
    A=2*(hd-he)-(md**2-me**2)
    Bvalue=md-me
    assert A>0 and Bvalue>0
    return A,Bvalue

def uniform_derivative(floors,bound6,k,h):
    """Entire |z-b|<=h, using exact j<=5 floors and |G^(6)|<=bound6."""
    eps=sum(Q(max(abs(floors[j]),abs(floors[j]+1)),10**8)
            *h**(j-k)/factorial(j-k) for j in range(k+1,6))
    eps+=Q(bound6)*h**(6-k)/factorial(6-k)
    return Q(floors[k],10**8)-eps, Q(floors[k]+1,10**8)+eps

def main():
    assert (LEFT,RIGHT)==(Q(211,4000),Q(213,4000))
    rows=survivor_rows()
    pw=[BASE**i for i in range(2*(N-1)+1)]
    W=[[comb(n+m,n)*pw[2*(N-1)-n-m] for m in range(N)] for n in range(N)]
    common=2*pw[2*(N-1)]
    (Al,Bl)=endpoint_at(rows,211,W,common)
    (Ar,Br)=endpoint_at(rows,213,W,common)
    ql,qr=Bl/Al,Br/Ar

    def strict_floor(x,place):
        floor=(x*10**place).__floor__()
        assert Q(floor,10**place)<x<Q(floor+1,10**place)
        return floor
    afloor_left=strict_floor(Al,12)
    afloor_right=strict_floor(Ar,12)
    bfloor_left=strict_floor(Bl,12)
    bfloor_right=strict_floor(Br,12)
    qfloor_left=strict_floor(ql,12)
    qfloor_right=strict_floor(qr,12)
    assert (afloor_left,afloor_right)==(858059787356,17778889403)
    assert (bfloor_left,bfloor_right)==(7865374402224,7929604130236)
    assert (qfloor_left,qfloor_right)==(9166464293188,446012343644423)
    assert 9<ql<10 and 446<qr<447
    assert 10*Al-Bl>0 and 446*Ar-Br<0
    assert 9*Al-Bl<0 and 447*Ar-Br>0

    a1_lo,a1_hi=uniform_derivative(FLOOR_A,M_A,1,H)
    b1_lo,b1_hi=uniform_derivative(FLOOR_B,M_B,1,H)
    assert Q(-3336)<a1_lo<a1_hi<-25
    assert 128<b1_lo<b1_hi<129
    # A'<-25, B'>128 on ENTIRE J. Exact endpoints give A>0, B>0.
    assert Ar>Q(17,1000) and Bl>Q(786,100)
    # Q'=(B'A-B A')/A^2>0.
    # Exactly one interior zero for real q in (Q(L),Q(R)).
    # All nonnegative integers 10..446 (437 values), exactly.
    # For q in [10,446], F'_q<-25q-128<0; z'(q)>0.
    assert int(ql)==9 and int(qr)==446
    assert 446-10+1==437
    result={
      'id':'PREFIX-698-R6',
      'science_pin':PIN,
      'levels':189,'live_cells':9529,
      'space_J':['211/4000','213/4000'],
      'endpoint_A_floor12':[str(afloor_left),str(afloor_right)],
      'endpoint_B_floor12':[str(bfloor_left),str(bfloor_right)],
      'endpoint_Q_floor12':[str(qfloor_left),str(qfloor_right)],
      'real_q_exact_interval':'(B(211/4000)/A(211/4000), B(213/4000)/A(213/4000))',
      'integer_q_with_one_interior_root':[10,446],
      'number_of_integer_q_values':437,
      'rational_derivative_bounds':{
        'A_prime_lower':str(a1_lo),
        'A_prime_upper':str(a1_hi),
        'B_prime_lower':str(b1_lo),
        'B_prime_upper':str(b1_hi)},
      'proof_checks':{
        'A_right_gt_0_017':True,
        'B_left_gt_7_86':True,
        'F10_left_positive':True,
        'F446_right_negative':True,
        'Q_strictly_increasing_throughout':True,
        'real_q_interval_complete_for_fixed_J':True},
      'arithmetic':'integer + Python Fraction; no float used in theorem checks',
      'inherited_exact_input':'PREFIX-695 jet floors and sixth-derivative bounds; frozen survivor predicate and labelled K/J kernels',
      'verification':'ALL_CHECKS_PASS PREFIX698-R6',
      'status':'AUTHOR_RECOMPUTED / EXACT_189_ROW_ENDPOINTS_AND_RATIONAL_DERIVATIVE / UNREVIEWED / NOT_ADMITTED',
      'next':'Certify [0.05325,0.0532600] and connect q>446 to the near-singular crossing branch; then assess PREFIX-675 global variance target.'
    }
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return result

if __name__=='__main__':main()
