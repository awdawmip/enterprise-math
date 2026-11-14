"""PREFIX-773: exact rational 189-layer Gamma diagonal jet and quantitative local minimum bounds.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Uses the theorem PREFIX-772: 4<Q''<5 and the unique stationary root in I.
Pure Python integers; no floating-point decision logic.
"""
from math import comb
from collections import defaultdict
from functools import lru_cache
from decimal import Decimal, localcontext
import sys, json
N=189; WIDTH=1<<18
@lru_cache(None)
def inside(n,k,x):
    return 40*(n+1)*comb(n,k)*x**k*(WIDTH-x)**(n-k)>WIDTH**n
@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    m=k*WIDTH//n; assert inside(n,k,m)
    if k==0:lo=hi=0
    else:
        a,b=0,m
        while b-a>1:
            t=(a+b)//2
            if inside(n,k,t):b=t
            else:a=t
        lo,hi=a,b
    a,b=m,WIDTH
    while b-a>1:
        t=(a+b)//2
        if inside(n,k,t):a=t
        else:b=t
    if 4*(a-hi)>WIDTH:return True
    if 4*(b-lo)<WIDTH:return False
    raise AssertionError((n,k))
rows=[{0:1}]
for n in range(1,N+1):
    nextrow=defaultdict(int)
    for k,x in rows[-1].items():nextrow[k]+=x;nextrow[k+1]+=x
    rows.append({k:x for k,x in nextrow.items() if wide(n,k)})
assert not rows[-1] and sum(map(len,rows[:N]))==9529

def rational_jet(a,base):
    """Numerators of s,s',s'' at x=a/base over one denominator base**188."""
    assert 0<a<base//2
    basepow=[1]
    apow=[1];bpow=[1]; bb=base-a
    for _ in range(190):
        basepow.append(basepow[-1]*base)
        apow.append(apow[-1]*a)
        bpow.append(bpow[-1]*bb)
    s=[];d=[];e=[]
    for n,row in enumerate(rows[:N]):
        x=y=z=0
        for k,c in row.items():
            j=n-k
            x+=c*apow[k]*bpow[j]
            if k:y+=c*k*apow[k-1]*bpow[j]
            if j:y-=c*j*apow[k]*bpow[j-1]
            if k>=2:z+=c*k*(k-1)*apow[k-2]*bpow[j]
            if j>=2:z+=c*j*(j-1)*apow[k]*bpow[j-2]
            if k and j:z-=2*c*k*j*apow[k-1]*bpow[j-1]
        s.append(x*basepow[188-n]);
        d.append(y*basepow[189-n] if n>=1 else 0)
        e.append(z*basepow[190-n] if n>=2 else 0)
    return basepow[188],s,d,e

def dotkernel(u,v,withL=False):
    total=0
    for i in range(N):
        if not u[i]:continue
        row=0
        for j in range(N):
            if not v[j]:continue
            k=comb(i+j,i)<<(376-i-j)
            if withL:k*=i+j+1
            row+=v[j]*k
        total+=u[i]*row
    return total

def at_point(a,base,verbose=False):
    E,s,d,e=rational_jet(a,base)
    H=E*E*(1<<377)
    sum_s=sum(s);sum_d=sum(d);sum_e=sum(e)
    SKS=dotkernel(s,s);DKS=dotkernel(d,s);EKS=dotkernel(e,s)
    DKD=dotkernel(d,d);DLD=dotkernel(d,d,True)
    EKD=dotkernel(e,d);ELD=dotkernel(e,d,True)
    m=2*sum_s*E*(1<<377)-SKS
    v=sum_d*E*(1<<377)-DKS
    w=sum_e*E*(1<<377)-EKS
    A=DKD; B=DLD
    Aprime=2*EKD
    Bprime=2*ELD
    vprime=w-A
    D=B*H+2*v*v-2*m*A
    Dprime=Bprime*H+4*v*vprime-4*v*A-2*m*Aprime
    assert A>0 and D>0
    q_num=A*H;q_den=D
    qp_num=H*(Aprime*D-A*Dprime);qp_den=D*D
    return (q_num,q_den,qp_num,qp_den)

def gt(a,b,c,d):return a*d>b*c

def report(a,base):
    qn,qd,gn,gd=at_point(a,base)
    with localcontext() as ctx:
        ctx.prec=65
        return {"u":f"{a}/{base}","Q_display":str(Decimal(qn)/Decimal(qd)),"Qprime_display":str(Decimal(gn)/Decimal(gd)),"Qprime_sign":"negative" if gn<0 else "positive" if gn>0 else "zero"}

def outward_decimal(n,den,digits,round_up):
    scale=10**digits
    k=-( (-n*scale)//den ) if round_up else (n*scale)//den
    return k, str(k//scale)+'.'+str(k%scale).zfill(digits)

if __name__=='__main__':
    # New rational witness near the stationary root. At both points the vectors and
    # Gamma contractions are recomputed using exact integer arithmetic.
    B0=10**11;a0=5029714515
    q0n,q0d,g0n,g0d=at_point(a0,B0)
    assert g0n<0
    B=10**13;a=502971451537
    qn,qd,gn,gd=at_point(a,B)
    assert gn>0
    # We inherit PREFIX-772's UNIFORM 4<Q''<5 on the full rational interval I.
    # For positive g=Q'(u1), the unique root u_* satisfies
    #       u1-g/4 < u_* < u1-g/5.
    lo_n,lo_d=4*a*gd-gn*B,4*B*gd
    hi_n,hi_d=5*a*gd-gn*B,5*B*gd
    assert lo_n*hi_d < hi_n*lo_d
    assert 502971451*lo_d < 10**10*lo_n
    assert 10**10*hi_n < 502971452*hi_d
    assert lo_n*B<a*lo_d and hi_n*B<a*hi_d
    # For 4<Q''<5, integration between u1 and its stationary root gives
    #      Q(u1)-g²/8 < Q(u*) < Q(u1)-g²/10.
    lower_n=8*qn*gd*gd-gn*gn*qd
    lower_d=8*qd*gd*gd
    upper_n=10*qn*gd*gd-gn*gn*qd
    upper_d=10*qd*gd*gd
    assert lower_n>0 and upper_n>0 and lower_n*upper_d<upper_n*lower_d
    lo_dec,lo_str=outward_decimal(lo_n,lo_d,20,False)
    hi_dec,hi_str=outward_decimal(hi_n,hi_d,20,True)
    qlo_dec,qlo_str=outward_decimal(lower_n,lower_d,32,False)
    qhi_dec,qhi_str=outward_decimal(upper_n,upper_d,32,True)
    # New critical-phase strict upper, independent of the inherited derivative bound.
    # This proves q_c <= Q(u1) < target by exact integer comparison.
    qt=2851859116285760930847;den=10**23
    assert qn*den < qt*qd
    # The coarse decimal enclosure is certified rather than merely displayed.
    assert lo_dec*lo_d<=lo_n*10**20
    assert hi_dec*hi_d>=hi_n*10**20
    assert qlo_dec*lower_d<=lower_n*10**32
    assert qhi_dec*upper_d>=upper_n*10**32
    with localcontext() as ctx:
        ctx.prec=66
        dd=lambda n,d:str(Decimal(n)/Decimal(d))
        output={
           "schema":"PREFIX773_R6_EXACT_DIAGONAL_LOCAL_OPTIMUM_V2",
           "frozen_pin":"awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",
           "inherited_continuous_interval":"[502971451/1e10,502971452/1e10]",
           "inherited_curvature":"4<Qsecond(u)<5 for all u in the interval; unique stationary root",
           "u0":f"{a0}/{B0}","Qprime_u0_sign":"negative",
           "u1":f"{a}/{B}","Qprime_u1_sign":"positive",
           "Q_u1_display":dd(qn,qd),"Qprime_u1_display":dd(gn,gd),
           "stationary_root_rational_bracket":[lo_str,hi_str],
           "stationary_root_bracket_method":"u1-Qprime(u1)/4 < ustar < u1-Qprime(u1)/5; all exact",
           "local_min_rational_bracket":[qlo_str,qhi_str],
           "local_min_bracket_method":"Q(u1)-Qprime(u1)^2/8 < min_I Q < Q(u1)-Qprime(u1)^2/10",
           "new_global_qc_upper_strict":f"{qt}/{den}",
           "new_global_qc_upper_decimal":"0.02851859116285760930847",
           "local_root_unique":"inherited PREFIX772, not re-proved by numeric sampling",
           "global_min_2d":"open",
           "source_positions":9529,
           "computation_type":"exact integer, rational at two witness points",
           "status":"AUTHOR_EXACT_INTEGER_AND_INHERITED_INTERVAL_LEMMA / UNREVIEWED / NOT_ADMITTED",
           "verification":"ALL_CHECKS_PASS PREFIX773"
        }
    print(json.dumps(output,indent=2))
    with open(__import__('pathlib').Path(__file__).with_name('PREFIX773_R6_EXACT_DIAGONAL_LOCAL_BOUNDS_RESULTS.json'),'w') as ff:
        json.dump(output,ff,indent=2);ff.write('\n')
    print('ALL_CHECKS_PASS PREFIX773')
