#!/usr/bin/env python3
"""PREFIX-635-R6: exact fixed-point interval/Bernstein certificate.
Frozen signed-BRC observer science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Requires only Python standard library. No external GitHub calls.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
import json
from pathlib import Path

N=189; DEN=1<<18; Q=1<<116
P2=F(19,128); A=F(4,25); B=F(161,1000)

@lru_cache(None)
def inside(n,k,a):
    return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k)>DEN**n

@lru_cache(None)
def wide(n,k):
    if k>n//2: return wide(n,n-k)
    mid=k*DEN//n
    assert inside(n,k,mid)
    if k==0: left_lo=left_hi=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            z=(lo+hi)//2
            if inside(n,k,z):hi=z
            else:lo=z
        left_lo,left_hi=lo,hi
    lo,hi=mid,DEN
    while hi-lo>1:
        z=(lo+hi)//2
        if inside(n,k,z):lo=z
        else:hi=z
    right_lo,right_hi=lo,hi
    if 4*(right_lo-left_hi)>DEN:return True
    if 4*(right_hi-left_lo)<DEN:return False
    raise AssertionError(('ambiguous primitive threshold',n,k))

rows=[{0:1}]; state={0:1};first=None
for n in range(1,N+1):
    raw=defaultdict(int)
    for k,v in state.items():raw[k]+=v;raw[k+1]+=v
    state={k:v for k,v in raw.items() if wide(n,k)}
    if first is None and len(raw)!=len(state):first=n
    rows.append(dict(state))
assert first==25 and not rows[189] and sum(rows[25].values())==2**25-2

def ceil_div(x,y):return -((-x)//y)
def I(x):
    if not isinstance(x,F):x=F(x)
    n=x.numerator*Q;d=x.denominator
    return n//d,ceil_div(n,d)
def plus(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def mul(x,y):
    z=[a*b for a in x for b in y]
    return min(z)//Q,ceil_div(max(z),Q)
def scale(x,n):return (x[0]*n,x[1]*n) if n>=0 else (x[1]*n,x[0]*n)
def div(x,n):return x[0]//n,ceil_div(x[1],n)

def split(ctrl,t):
    x,y=t.numerator,t.denominator
    layer=ctrl[:];left=[layer[0]];right=[layer[-1]]
    for _ in range(len(ctrl)-1):
        layer=[(((y-x)*layer[j][0]+x*layer[j+1][0])//y,
                ceil_div((y-x)*layer[j][1]+x*layer[j+1][1],y))
               for j in range(len(layer)-1)]
        left.append(layer[0]);right.append(layer[-1])
    return left,right[::-1]
def bounds(ctrl,a,b):
    clipped=split(split(ctrl,a)[1],(b-a)/(1-a))[0]
    return min(z[0] for z in clipped),max(z[1] for z in clipped)
def point(ctrl,p):return split(ctrl,p)[0][-1]

# Bernst. control points of the survivor polynomials and first 2 derivatives.
poly=[]
for n,row in enumerate(rows[:N]):
    c=[F(row.get(k,0),comb(n,k)) for k in range(n+1)]
    d=[n*(c[k+1]-c[k]) for k in range(n)] if n else [F(0)]
    dd=[n*(n-1)*(c[k+2]-2*c[k+1]+c[k]) for k in range(n-1)] if n>1 else [F(0)]
    poly.append(tuple([I(z) for z in seq] for seq in (c,d,dd)))

# Exact dyadic coefficients of mu=sum s_n + sum alpha_n*s_n and H derivative.
# p2=19/128 -> s_m(p2)=snum[m]/128**m. Common denominators remove
# all rounding until the final outward fixed-point conversion I(...).
snum=[sum(v*19**k*109**(n-k) for k,v in row.items()) for n,row in enumerate(rows[:N])]
M=N-1
mu0=I(F(sum(snum[m] << (7*(M-m)) for m in range(N)),1<<(7*M)))
alpha=[];beta=[]
for n in range(N):
    den=1<<(n+8*M+1)
    wa=wb=0
    for m in range(N):
        z=(comb(n+m,n)*snum[m]) << (8*(M-m))
        wa+=z;wb+=(n+m+1)*z
    alpha.append(I(F(den-wa,den)))
    beta.append(I(F((n+1)*2*den-wb,2*den)))
assert all(z[0]>0 for z in alpha) and all(z[0]>0 for z in beta)

def moments(a,b=None):
    mu=mu0;U=I(0);U2=I(0);J=I(0);J2=I(0)
    for n,(s,d,dd) in enumerate(poly):
        vals=[point(x,a) if b is None else bounds(x,a,b) for x in (s,d,dd)]
        mu=plus(mu,mul(vals[0],alpha[n]))
        U=plus(U,mul(vals[1],alpha[n]))
        U2=plus(U2,mul(vals[2],alpha[n]))
        J=plus(J,mul(vals[1],beta[n]))
        J2=plus(J2,mul(vals[2],beta[n]))
    return mu,U,U2,J,J2

def first_deriv(moment,q):
    mu,U,U2,J,J2=moment
    return sub(scale(sub(J,mul(mu,U)),2),div(U,q))
def second_deriv(moment,q):
    mu,U,U2,J,J2=moment
    return sub(scale(sub(sub(J2,mul(U,U)),mul(mu,U2)),2),div(U2,q))

# Four exact interval enclosures. An interval is a pair of outward-rounded
# multiples of 2**(-116); no floating-point step enters any assertion.
patches=[];u_lows=[];u_highs=[];sec_lows=[];sec_highs=[]
for k in range(4):
    lo=A+(B-A)*k/4;hi=A+(B-A)*(k+1)/4
    m=moments(lo,hi)
    assert 300*Q<m[1][0] and m[1][1]<310*Q
    u_lows.append(m[1][0]);u_highs.append(m[1][1])
    for q in (12,24):
        sec=second_deriv(m,q)
        assert sec[0]>23000*Q and sec[1]<50000*Q,(k,q,sec)
        sec_lows.append(sec[0]);sec_highs.append(sec[1])
    patches.append({'left':str(lo),'right':str(hi),'min_q12_F2_scaled':str(second_deriv(m,12)[0]),
                    'min_q24_F2_scaled':str(second_deriv(m,24)[0])})

# Strict exact derivative sign brackets of each unique local valley.
roots={}
for q,lo_num in ((12,168247),(24,167883)):
    left=F(lo_num,1<<20);right=F(lo_num+1,1<<20)
    assert A<left<right<B
    gd_left=first_deriv(moments(left),q)
    gd_right=first_deriv(moments(right),q)
    assert gd_left[1]<0 and gd_right[0]>0,(q,gd_left,gd_right)
    assert first_deriv(moments(A),q)[1]<0
    assert first_deriv(moments(B),q)[0]>0
    roots[q]={'left':str(left),'right':str(right),'left_gradient_sign':'NEGATIVE',
              'right_gradient_sign':'POSITIVE'}
assert F(167884,1<<20)<F(168247,1<<20)
assert F(168247-167884,1<<20)==F(363,1<<20)
assert F(168248-167883,1<<20)==F(365,1<<20)
# For q in [12,24], F_q'' is affine in t=1/q: endpoint q12,q24
# certificate => 23000<F_q''<50000; endpoint gradient signs are affine too.
# Analytic implicit branch c(q) gives c'(q)=-mu'(c)/(q²*F_q''(c)).
# Integration establishes 1/4000 < c12-c24 < 31/55200.
assert F(300,50000*24)==F(1,4000)
assert F(310,23000*24)==F(31,55200)

result={'schema':'PREFIX635_R6_LOCAL_UNIQUENESS_AND_GAP_V1',
 'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'p2':str(P2),'p1_window':[str(A),str(B)],'q_range':[12,24],
 'survival_levels':N,'first_stop':first,'final_state_empty':True,
 'fixed_point_denominator_power':116,'patches':4,
 'mu_prime_bounds':'300 < mu_prime < 310',
 'F_second_bounds':'23000 < F_q_second < 50000 for every q in [12,24]',
 'critical_points':roots,
 'spacing_bounds':'1/4000 < c_12-c_24 < 31/55200',
 'dyadic_spacing_bounds':'363/1048576 < c_12-c_24 < 365/1048576',
 'proof':'Bernstein convex hull + outward fixed-point de Casteljau + IVT + positive second derivative + IFT + integral bound',
 'validation':'ALL_CHECKS_PASS','status':'AUTHOR_PROVED / EXACT_INTEGER_INTERVAL_CHECKED / UNREVIEWED / NOT_ADMITTED'}
out=Path(__file__).with_name('PREFIX635_R6_RESULTS.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS')
print('min_F_second',min(sec_lows)//Q,'max_F_second',max(sec_highs)//Q)
print('mu_prime_envelope',min(u_lows)//Q,max(u_highs)//Q)
print('dyadic_brackets',roots)
