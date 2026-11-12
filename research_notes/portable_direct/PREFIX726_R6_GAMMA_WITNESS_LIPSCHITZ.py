"""PREFIX-726 — actual frozen 189-row BRC Gamma witness + global Lipschitz square.
Source science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Proof and result remain author-checked pending independent research review.
"""
from collections import defaultdict
from functools import lru_cache
from math import comb
from fractions import Fraction as F
from pathlib import Path
import hashlib, json

N=189
WD=1<<18

@lru_cache(None)
def inside(m,k,x):
    return 40*(m+1)*comb(m,k)*x**k*(WD-x)**(m-k)>WD**m

@lru_cache(None)
def wide(m,k):
    if k>m//2:
        return wide(m,m-k)
    mid=k*WD//m
    assert inside(m,k,mid)
    if k==0:
        lo=hi=0
    else:
        a,b=0,mid
        while b-a>1:
            x=(a+b)//2
            if inside(m,k,x):b=x
            else:a=x
        lo,hi=a,b
    a,b=mid,WD
    while b-a>1:
        x=(a+b)//2
        if inside(m,k,x):a=x
        else:b=x
    if 4*(a-hi)>WD:return True
    if 4*(b-lo)<WD:return False
    raise ValueError('undecided frozen width')

rows=[{0:1}]
for n in range(1,N+1):
    new=defaultdict(int)
    for k,v in rows[-1].items():
        new[k]+=v
        new[k+1]+=v
    rows.append({k:v for k,v in new.items() if wide(n,k)})
assert not rows[-1] and sum(map(len,rows[:N]))==9529

Z=2**(2*N-1)
coeff=[[comb(n+m,n)*2**(2*N-2-n-m) for m in range(N)] for n in range(N)]

@lru_cache(None)
def scaled_tails(num,den):
    a,b=num,den-num
    pa=[1];pb=[1]
    for _ in range(N):
        pa.append(pa[-1]*a)
        pb.append(pb[-1]*b)
    return tuple(sum(v*pa[k]*pb[n-k] for k,v in row.items())*den**(N-1-n)
                 for n,row in enumerate(rows[:N]))

@lru_cache(None)
def pair_moments(p_num,p_den,z_num,z_den):
    t1,t2=scaled_tails(p_num,p_den),scaled_tails(z_num,z_den)
    A1,A2=sum(t1),sum(t2)
    B1=sum((n+1)*v for n,v in enumerate(t1))
    B2=sum((n+1)*v for n,v in enumerate(t2))
    C0=C1=0
    for n,x in enumerate(t1):
        if not x:continue
        for m,y in enumerate(t2):
            if not y:continue
            c=x*y*coeff[n][m]
            C0+=c
            C1+=(n+m+1)*c
    R=p_den**(N-1)*z_den**(N-1)*Z
    mu=F((A1*z_den**(N-1)+A2*p_den**(N-1))*Z-C0,R)
    M2=F(2*(B1*z_den**(N-1)+B2*p_den**(N-1))*Z-C1,R)
    return mu,M2-mu*mu

center=pair_moments(88,768,88,768)
witness=pair_moments(0,1,146,1000)
gap0=witness[1]-center[1]
gap_half=(witness[1]-witness[0]/2)-(center[1]-center[0]/2)
assert gap0>245 and gap_half>245

# s_n Bernstein controls in {0,1} imply |s_n'|<=n.
# Influence a_n=1-sum_m c_nm*s_m, h_n=2(n+1)-sum_m (n+m+1)c_nm*s_m
# obey 0<=a_n<=1, 0<=h_n<=2(n+1) by the infinite negative-binomial
# kernel identities. Therefore bound every coordinate derivative globally.
mu_grad=sum(range(N))
M2_grad=2*sum(n*(n+1) for n in range(N))
assert mu_grad==17766 and M2_grad==4500720
# E[max(T_p,T_z)] <= E[T_p+T_z] <= 2*N by row-189 extinction.
Lipschitz=F(M2_grad)+(4*N+F(1,2))*mu_grad
assert Lipschitz==17940699
radius=F(1,200000)
margin=F(245)-2*radius*Lipschitz
assert margin==F(6559301,100000)>0

def H(x):return hashlib.sha256(str(x).encode()).hexdigest()
result={
    'schema':'PREFIX726_R6_FROZEN_GAMMA_REAL_WITNESS_SQUARE_V1',
    'date':'2026-11-12',
    'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'model':'frozen 189-row BRC stopping count + independent conditional Gamma maximum',
    'center':['11/96','11/96'],'witness':['0','73/500'],
    'square_radius':str(radius),'range':'all real q>=2',
    'exact_moment_computations':{
        'center_mu':{'num_sha256':H(center[0].numerator),'den_sha256':H(center[0].denominator)},
        'center_W':{'num_sha256':H(center[1].numerator),'den_sha256':H(center[1].denominator)},
        'witness_mu':{'num_sha256':H(witness[0].numerator),'den_sha256':H(witness[0].denominator)},
        'witness_W':{'num_sha256':H(witness[1].numerator),'den_sha256':H(witness[1].denominator)}},
    'exact_center_gap_endpoints':{
        't0_floor_strict':'245','t1/2_floor_strict':'245',
        't0_numerator_sha256':H(gap0.numerator),
        't0_denominator_sha256':H(gap0.denominator),
        't1/2_numerator_sha256':H(gap_half.numerator),
        't1/2_denominator_sha256':H(gap_half.denominator)},
    'uniform_mu_coordinate_derivative_bound':mu_grad,
    'uniform_M2_coordinate_derivative_bound':M2_grad,
    'uniform_f_coordinate_derivative_bound':str(Lipschitz),
    'uniform_f_gap_floor_strict':str(margin),
    'uniform_V_gap_floor_strict':'q^2 * '+str(margin),
    'nonzero_survivor_coefficients':9529,
    'inherited_grid_coverage':'139018/147456; not updated, existing cell overlap not checked',
    'status':'AUTHOR_EXACT_INTEGER_FRACTION_RECOMPUTED / UNREVIEWED / NOT_ADMITTED'
}
if __name__=='__main__':
    Path(__file__).with_name('PREFIX726_R6_GAMMA_RESULTS.json').write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('ALL_CHECKS_PASS PREFIX726-R6')
    print('mu gradient',mu_grad,'M2 gradient',M2_grad,'f gradient',Lipschitz)
    print('gamma exact center gaps >245:',gap0>245,gap_half>245)
    print('strict region gap >',margin,'times q^2')
    print('gap0 approx',float(gap0),'gap_half approx',float(gap_half))
