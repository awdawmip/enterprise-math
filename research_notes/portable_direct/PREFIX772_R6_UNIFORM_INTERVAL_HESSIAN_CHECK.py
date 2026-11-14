"""PREFIX-772: certified rational interval diagonal/transverse curvature on a narrow interval.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
The model and first-stop recurrence are copied from published PREFIX-771; all signs
are certified by integer interval operations with directed outward rounding.
Python 3 standard library only.
"""
from collections import defaultdict
from functools import lru_cache
from math import comb
from decimal import Decimal, localcontext
import json

N,W=189,1<<18
F=10**48  # interval fixed-point scale, true quantity in [lo/F,hi/F]

@lru_cache(None)
def inside(n,k,x):
    return 40*(n+1)*comb(n,k)*x**k*(W-x)**(n-k)>W**n
@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    m=k*W//n
    assert inside(n,k,m)
    if k==0:lo=hi=0
    else:
        a,b=0,m
        while b-a>1:
            t=(a+b)//2
            if inside(n,k,t):b=t
            else:a=t
        lo,hi=a,b
    a,b=m,W
    while b-a>1:
        t=(a+b)//2
        if inside(n,k,t):a=t
        else:b=t
    if 4*(a-hi)>W:return True
    if 4*(b-lo)<W:return False
    raise ArithmeticError((n,k))

rows=[{0:1}]
for n in range(1,N+1):
    v=defaultdict(int)
    for k,x in rows[-1].items():v[k]+=x;v[k+1]+=x
    rows.append({k:x for k,x in v.items() if wide(n,k)})
assert len(rows)==190 and not rows[-1]
assert sum(map(len,rows[:N]))==9529

# Interval primitives with exact integer floors and ceilings.
def ceildiv(a,b):return -((-a)//b)
def scalar(z):return (z*F,z*F)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def sub(a,b):return (a[0]-b[1],a[1]-b[0])
def neg(a):return (-a[1],-a[0])
def times(a,k):return (a[0]*k,a[1]*k) if k>=0 else (a[1]*k,a[0]*k)
def mul(a,b):
    p=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]);return (min(p)//F,ceildiv(max(p),F))
def divpos(a,b):
    assert b[0]>0
    p=(a[0]*F*F//b[0],a[0]*F*F//b[1],a[1]*F*F//b[0],a[1]*F*F//b[1])
    # Perform rigorous min/max by endpoint pair cross-multiplication, not rounded candidate values.
    vals=[(x,y) for x in a for y in b]
    lo=min(vals,key=lambda t:__import__('fractions').Fraction(t[0],t[1]));hi=max(vals,key=lambda t:__import__('fractions').Fraction(t[0],t[1]))
    return (lo[0]*F//lo[1],ceildiv(hi[0]*F,hi[1]))
def isum(vals):
    a=b=0
    for v in vals:a+=v[0];b+=v[1]
    return (a,b)
def fracpos(num,den):return (num*F//den,ceildiv(num*F,den))

def coefficient_jets(XL,XR,XB):
    # Bound each nonnegative monomial over the full interval and apply its exact sign.
    pL=[1];pR=[1];qL=[1];qR=[1]
    for _ in range(N):
        pL.append(pL[-1]*XL);pR.append(pR[-1]*XR)
        qL.append(qL[-1]*(XB-XR));qR.append(qR[-1]*(XB-XL))
    common=XB**191
    jets=[[],[],[],[]]
    bpow=[XB**k for k in range(195)]
    for n,row in enumerate(rows[:N]):
        buf=[[0,0] for _ in range(4)]
        for k,coef in row.items():
            j=n-k
            for order in range(4):
                for a in range(order+1):
                    b=order-a
                    if a>k or b>j:continue
                    ff=comb(order,a)*coef
                    for t in range(a):ff*=k-t
                    for t in range(b):ff*=j-t
                    lower=ff*pL[k-a]*qL[j-b]
                    upper=ff*pR[k-a]*qR[j-b]
                    if b%2:buf[order][0]-=upper;buf[order][1]-=lower
                    else:buf[order][0]+=lower;buf[order][1]+=upper
        for r in range(4):
            factor=bpow[191+r-n]
            lo=buf[r][0]*factor
            hi=buf[r][1]*factor
            jets[r].append((lo*F//common,ceildiv(hi*F,common)))
    return jets


def certify(xl,xr,xb):
    S,d,e,f=coefficient_jets(xl,xr,xb)

    def bilinear(v,w,second=False):
        a=b=0
        for i in range(N):
            for j in range(i,N):
                kval=comb(i+j,i)
                if second:kval*=i+j+1
                k=fracpos(kval,1<<(i+j+1))
                term=mul(v[i],w[j])
                if i<j:term=add(term,mul(v[j],w[i]))
                val=mul(k,term)
                a+=val[0];b+=val[1]
        return (a,b)

    m=sub(times(isum(S),2),bilinear(S,S))
    v=sub(isum(d),bilinear(d,S))
    w=sub(isum(e),bilinear(e,S))
    A=bilinear(d,d);B0=bilinear(d,d,True)
    A1=times(bilinear(e,d),2)
    Asecond=times(add(bilinear(f,d),bilinear(e,e)),2)
    B1=times(bilinear(e,d,True),2)
    Bsecond=times(add(bilinear(f,d,True),bilinear(e,e,True)),2)
    v1=sub(w,A)
    v2=sub(sub(isum(f),bilinear(f,S)),times(bilinear(e,d),3))
    m1=times(v,2)
    msecond=times(v1,2)
    D=sub(add(B0,times(mul(v,v),2)),times(mul(m,A),2))
    D1=sub(sub(add(B1,times(mul(v,v1),4)),times(mul(m1,A),2)),times(mul(m,A1),2))
    Dsecond= sub(sub(sub(sub(add(add(Bsecond,times(mul(v1,v1),4)),times(mul(v,v2),4)),times(mul(msecond,A),2)),times(mul(m1,A1),4)),times(mul(m,Asecond),2)),scalar(0))

    # Uniform Q'' numerator: (A''D-AD'')D - 2(A'D-AD')D'.
    qp_num=sub(mul(A1,D),mul(A,D1))
    qpp_num=sub(mul(sub(mul(Asecond,D),mul(A,Dsecond)),D),times(mul(qp_num,D1),2))
    Dcube=mul(mul(D,D),D)
    assert D[0]>0
    assert 4*Dcube[1]<qpp_num[0] and qpp_num[1]<5*Dcube[0], 'UNIFORM_QSECOND_NOT_CERTIFIED'

    # Transverse t^2 coefficient Q2.
    m2=add(sub(isum(e),bilinear(e,S)),A)
    two_vp2=add(sub(isum(f),bilinear(f,S)),bilinear(e,d))
    A2=sub(bilinear(f,d),bilinear(e,e))
    B2=sub(bilinear(f,d,True),bilinear(e,e,True))
    D2=sub(sub(sub(add(B2,times(mul(v,two_vp2),2)),times(mul(m2,m2),2)),times(mul(m2,A),2)),times(mul(m,A2),2))
    q2_num=sub(mul(A2,D),mul(A,D2))
    Dsquare=mul(D,D)
    assert 21*Dsquare[1]<q2_num[0] and q2_num[1]<22*Dsquare[0], 'UNIFORM_Q2_NOT_CERTIFIED'

    assert D[0]>0
    assert 4*Dcube[1] < qpp_num[0] and qpp_num[1] < 5*Dcube[0]
    assert 21*Dsquare[1] < q2_num[0] and q2_num[1] < 22*Dsquare[0]
    return {'A':A,'D':D,'qpp_num':qpp_num,'Dcube':Dcube,'q2_num':q2_num,'Dsquare':Dsquare}

if __name__ == '__main__':
    bracket=certify(502971451,502971452,10**10)
    point=certify(5029714515,5029714515,10**11)
    target=28518591162857609310
    # Uniform strict upper certificate: the exact interval upper A/D
    # lies below target/10**21 by positive integer cross multiplication.
    assert 10**21*point['A'][1] < target*point['D'][0]
    with localcontext() as ctx:
        ctx.prec=46
        A,D=point['A'],point['D']
        qlo=str(Decimal(A[0])/Decimal(D[1]))
        qhi=str(Decimal(A[1])/Decimal(D[0]))
    result={
        'schema':'PREFIX772_R6_CERTIFIED_RATIONAL_INTERVAL_HESSIAN_V2',
        'frozen_science_pin':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'continuous_interval':['502971451/10000000000','502971452/10000000000'],
        'interval_quantification':'all real u in the closed interval',
        'point_witness':'5029714515/100000000000',
        'new_global_qc_upper_strict':'28518591162857609310/1000000000000000000000',
        'Q_point_lower_display':qlo,
        'Q_point_upper_display':qhi,
        'survivor_rows':N,'nonzero_survivor_positions':9529,
        'terminal_layer_empty':True,'interval_fixed_point_scale':str(F),
        'continuous_D_positive':True,
        'continuous_Q_diagonal_second_derivative':'4<Qsecond<5',
        'continuous_Q_transverse_coefficient':'21<Q2<22',
        'stationary_root_exactly_one':'from PREFIX771 strict opposite endpoint signs + uniform Qsecond>4',
        'local_2d_minimum':'strict at (u_star,u_star) under Q symmetry and positive diagonal/transverse Hessian',
        'global_2d_minimum':'open',
        'independent_review':'not performed',
        'execution':'ALL_CHECKS_PASS PREFIX772 UNIFORM_HESSIAN_AND_POINT_Q'
    }
    with open('/mnt/data/PREFIX772_R6_UNIFORM_INTERVAL_HESSIAN_RESULTS.json','w') as out:
        json.dump(result,out,indent=2,ensure_ascii=False);out.write('\n')
    print(json.dumps(result,indent=2,ensure_ascii=False))
