#!/usr/bin/env python3
"""PREFIX-645 exact finite BRC observer higher-moment and thinning cumulant certificate.

No native 96-port evolution is run. Pinned 189-layer survivor recurrence
and the original independent marked-Poisson stopping observer are used.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, factorial
import json
from pathlib import Path

DEN=1<<18; N=189
@lru_cache(None)
def inside(n,k,a):
    return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k)>DEN**n
@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    mid=k*DEN//n
    assert inside(n,k,mid),("missing midpoint",n,k)
    if k==0: left_lo=left_hi=0
    else:
        lo,hi=0,mid
        assert not inside(n,k,lo)
        while hi-lo>1:
            m=(hi+lo)//2
            if inside(n,k,m):hi=m
            else:lo=m
        left_lo,left_hi=lo,hi
    lo,hi=mid,DEN
    assert not inside(n,k,hi)
    while hi-lo>1:
        m=(hi+lo)//2
        if inside(n,k,m):lo=m
        else:hi=m
    right_lo,right_hi=lo,hi
    if 4*(right_lo-left_hi)>DEN:return True
    if 4*(right_hi-left_lo)<DEN:return False
    raise AssertionError(("undecidable-width",n,k))

def survivor_rows():
    rows=[{0:1}]; state={0:1}; first=None
    for n in range(1,N+1):
        nxt=defaultdict(int)
        for k,v in state.items():nxt[k]+=v;nxt[k+1]+=v
        state={k:v for k,v in nxt.items() if wide(n,k)}
        if first is None and sum(state.values())<sum(nxt.values()):first=n
        rows.append(state.copy())
    assert first==25 and not rows[189]
    assert sum(rows[24].values())==2**24
    assert sum(rows[25].values())==2**25-2
    return rows

def survivor_at(rows,x):
    a,b=x.numerator,x.denominator
    return [Q(sum(v*a**k*(b-a)**(n-k) for k,v in rows[n].items()),b**n)
            for n in range(N)]

def moments(p,z):
    rows=survivor_rows()
    u,v=survivor_at(rows,p),survivor_at(rows,z)
    assert all(0<=x<=1 for x in u+v)
    mu=sum(u)+sum(v)
    H=sum((n+1)*(u[n]+v[n]) for n in range(N))
    J=sum((n+1)*(n+2)*(u[n]+v[n]) for n in range(N))
    L=sum((n+1)*(n+2)*(n+3)*(u[n]+v[n]) for n in range(N))
    for n in range(N):
        if not u[n]:continue
        for m in range(N):
            if not v[m]:continue
            w=Q(comb(n+m,n),2**(n+m+1))*u[n]*v[m]
            s=n+m+1
            mu-=w
            H-=Q(s,2)*w
            J-=Q(s*(s+1),4)*w
            L-=Q(s*(s+1)*(s+2),8)*w
    c1=mu
    c2=2*H-mu**2
    c3=3*J-6*mu*H+2*mu**3
    c4=4*L-12*mu*J-12*H**2+24*mu**2*H-6*mu**4
    assert c1>0 and c2>0 and c3<0 and c4>0
    assert Q(108)<c1<Q(109) and Q(336)<c2<Q(337)
    assert Q(-1210)<c3<Q(-1209) and Q(50374)<c4<Q(50375)
    return (c1,c2,c3,c4),rows

def stirling_second(n,k):
    if n==k==0:return 1
    if not k or k>n:return 0
    a=[[0]*(n+1) for _ in range(n+1)];a[0][0]=1
    for i in range(1,n+1):
        for j in range(1,i+1):a[i][j]=a[i-1][j-1]+j*a[i-1][j]
    return a[n][k]

def stirling_first_unsigned(n,k):
    a=[[0]*(n+1) for _ in range(n+1)];a[0][0]=1
    for i in range(1,n+1):
        for j in range(1,i+1):a[i][j]=a[i-1][j-1]+(i-1)*a[i-1][j]
    return a[n][k]

def transformed(c,q):
    return tuple(sum((-1)**(r-j)*stirling_second(r,j)*q**j*c[j-1]
                     for j in range(1,r+1)) for r in range(1,len(c)+1))

def check_toy():
    # Two marked types each has probability 1/q per action, stop after seeing both once.
    # The informative Poisson clock maximum is Exp(2)+Exp(1), independent.
    toy=tuple(factorial(j-1)*(1+Q(1,2**j)) for j in range(1,5))
    assert toy==(Q(3,2),Q(5,4),Q(9,4),Q(51,8))
    for q in (12,24):
        cs=transformed(toy,q)
        # T_q = Geom(2/q) + Geom(1/q) independent, for positive integer steps.
        geom1=Q(q,2); geom2=Q(q)
        independent=(geom1+geom2,
            geom1*(geom1-1)+geom2*(geom2-1),
            geom1*(geom1-1)*(2*geom1-1)+geom2*(geom2-1)*(2*geom2-1),
            geom1*(geom1-1)*(6*geom1*geom1-6*geom1+1)
            +geom2*(geom2-1)*(6*geom2*geom2-6*geom2+1))
        assert cs==independent,(q,cs,independent)
    return toy

def summarise(x):
    # Exact decimal intervals; never use rounding for inequality proof.
    a=x*1000000
    floor=a.numerator//a.denominator
    return {'interval_6dp':[str(Q(floor,1000000)),str(Q(floor+1,1000000))],
            'decimal_display':f'{float(x):.9f}'}

def main():
    p=Q(1,6); z=Q(19,128)
    c,rows=moments(p,z)
    toy=check_toy()
    results={}
    for q in (12,24):
        k=transformed(c,q)
        assert k[2]<0 and k[3]>0
        assert (Q(-2234220)<k[2]<Q(-2234219) if q==12 else Q(-17299552)<k[2]<Q(-17299551))
        assert (Q(1057438820)<k[3]<Q(1057438821) if q==12 else Q(16814644408)<k[3]<Q(16814644409))
        assert k[0]==q*c[0] and k[1]==q*q*c[1]-q*c[0]
        assert k[2]==q**3*c[2]-3*q*q*c[1]+q*c[0]
        assert k[3]==q**4*c[3]-6*q**3*c[2]+7*q*q*c[1]-q*c[0]
        for r in range(1,5):
            assert sum(stirling_first_unsigned(r,j)*k[j-1]
                       for j in range(1,r+1))==q**r*c[r-1]
        results[str(q)]={f'kappa_{i+1}':summarise(x) for i,x in enumerate(k)}
    result={
       'schema':'PREFIX645_R6_CUMULANT_TRANSFER_V1',
       'date':'2026-11-10',
       'frozen_scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
       'observer':'signed two-informative-direction, dyadic 189-layer stopping observer',
       'p':'1/6','z':'19/128',
       'poissonized_cumulants':{f'kappa_{i+1}':summarise(x) for i,x in enumerate(c)},
       'native_action_cumulants':results,
       'finite_rows':'0..188; extinction at 189; first stop at 25',
       'all_order_identity':'kappa_r(T_q)=sum_{j=1}^r(-1)^(r-j)S(r,j)q^j kappa_j(Y)',
       'inverse':'q^r kappa_r(Y)=sum_{j=1}^r unsigned_s(r,j)kappa_j(T_q)',
       'toy_cumulants':[str(x) for x in toy],
       'exact_checks':'passed: 189-layer survivor invariants, positive finite moments, r<=4 Stirling inverses q=12/24, two-mark independent exact toy through r=4',
       'status':'AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED',
       'native_96port_reexecution':False
    }
    outfile=Path(__file__).with_name('PREFIX645_R6_RESULTS.json')
    outfile.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('ALL_CHECKS_PASS',len(rows),'layers',len(results),'q slots','four cumulant orders')
    for k,v in result['poissonized_cumulants'].items():print('Y',k,v['decimal_display'])
    for q,r in results.items():
        for name,v in r.items():print('T',q,name,v['decimal_display'])

if __name__=='__main__':main()
