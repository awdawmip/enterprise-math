#!/usr/bin/env python3
"""PREFIX-1007: formal-series exact reduction of X6 marked BRC collisions.

All rational arithmetic is on the post-observer combination formula proved in
PREFIX-1005, NOT a new native Stage46 run. No classical pi or floating dynamics.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from math import comb, factorial
import json

D = 6
ORBIT_POLYS = [
 ((0,0,0,0,0,0), (21660,-138300,241650)),
 ((-1,0,0,0,0,1), (22680,-142260,355440)),
 ((-2,0,0,0,0,2), (-3420,14100,-11100)),
 ((-2,0,0,0,1,1), (-30240,163200,-219840)),
 ((-1,-1,0,0,1,1), (-49680,324720,-539280)),
 ((-3,0,0,0,0,3), (120,-420,-240)),
 ((-3,0,0,0,1,2), (2880,-12960,2880)),
 ((-3,0,0,1,1,1), (2880,-14400,7200)),
 ((-2,-1,0,0,1,2), (12960,-71280,51840)),
 ((-2,-1,0,1,1,1), (17280,-103680,95040)),
 ((-1,-1,-1,1,1,1), (2880,-18720,20160)),
]

# Rational generating functions g_0=x and g_1=y. A monomial key is
# (exponent x, exponent y, exponent t). Negative powers of t are formal
# Laurent factors, and cancel in the complete marked coefficient sequence.
def add(a,b,scale=1):
    c=defaultdict(int,a)
    for k,v in b.items(): c[k]+=scale*v
    return {k:v for k,v in c.items() if v}

def shift(a,k):
    return {(i,j,h+k):v for (i,j,h),v in a.items()}

def mul(a,b):
    c=defaultdict(int)
    for (i,j,h),v in a.items():
        for (p,q,r),w in b.items(): c[i+p,j+q,h+r]+=v*w
    return {k:v for k,v in c.items() if v}

@lru_cache(None)
def g(k):
    if k==0: return {(1,0,0):1}
    if k==1: return {(0,1,0):1}
    return shift(add(g(k-2),g(k-1),-(k-1)),-1)

def marked_terms(delta):
    assert len(delta)==D and sum(delta)==0
    p=sum(max(v,0) for v in delta)
    poly={(0,0,p):1}
    for v in delta: poly=mul(poly,g(abs(v)))
    assert all(a+b==D for a,b,_ in poly)
    return {(b,k):v for (a,b,k),v in poly.items()}

def coefficients(max_index):
    previous=[Fraction(1)]*(D+1)
    rows=[tuple(previous)]
    for m in range(1,max_index+1):
        cur=[Fraction(0)]*(D+1)
        cur[0]=Fraction(D,m)*previous[1]
        for j in range(1,D+1):
            cur[j]=(Fraction(D-j)*previous[j+1] if j<D else 0)
            cur[j]=(cur[j]+j*cur[j-1])/(m+j)
        rows.append(tuple(cur))
        previous=cur
    return rows

def marked_from_module(m,delta,rows):
    s=Fraction(0)
    for (j,tshift),c in marked_terms(delta).items():
        i=m-tshift
        if 0<=i<len(rows): s+=c*rows[i][j]
    ans=s*factorial(m)**2
    assert ans.denominator==1,(m,delta,ans)
    return ans.numerator

def differential_reductions():
    out=[{(0,0):Fraction(1)},{(1,0):Fraction(1,D)}]
    for j in range(1,D):
        temp=defaultdict(Fraction)
        for (r,q),c in out[j].items():
            temp[r,q-1]+=c*Fraction(q+j,D-j)
            temp[r+1,q]+=c/Fraction(D-j)
        for (r,q),c in out[j-1].items():
            temp[r,q-1]-=c*Fraction(j,D-j)
        out.append({k:v for k,v in temp.items() if v})
    return out

REDUCTIONS=differential_reductions()
def marked_a_only_operator(delta):
    d=defaultdict(Fraction)
    for (j,p),v in marked_terms(delta).items():
        for (r,q),coef in REDUCTIONS[j].items(): d[r,q+p]+=v*coef
    return {key:v for key,v in d.items() if v}

def marked_from_A(m,delta,As):
    f=factorial(m)
    ret=Fraction(0)
    for (r,q),c in marked_a_only_operator(delta).items():
        v=m-q
        s=v+r
        if v>=0 and 0<=s<len(As):
            ret+=c*Fraction(f*f, factorial(v)*factorial(s))*As[s]
    assert ret.denominator==1,(m,delta,ret)
    return ret.numerator

def A_independent(max_m):
    prev=[1]*(max_m+1)
    for s in range(2,D+1):
        prev=[sum(comb(m,r)**2*prev[m-r] for r in range(m+1)) for m in range(max_m+1)]
    return prev

def compositions(d,m):
    if d==1:
        yield (m,)
        return
    for k in range(m+1):
        for tail in compositions(d-1,m-k):yield (k,)+tail

def direct(m,delta):
    f=factorial(m)
    total=0
    for a in compositions(D,m):
        b=tuple(ai+di for ai,di in zip(a,delta))
        if min(b)<0:continue
        den_a=1;den_b=1
        for ai,bi in zip(a,b):den_a*=factorial(ai);den_b*=factorial(bi)
        total+=(f//den_a)*(f//den_b)
    return total

def masked_mass(n,rows):
    m=n-4
    num=sum((a*n*n+b*n+c)*marked_from_module(m,delta,rows)
            for delta,(a,b,c) in ORBIT_POLYS)
    return Fraction(num,36**n)

def run():
    m_max=350
    all_deltas=[d for d,_ in ORBIT_POLYS]
    d1=(3,2,-2,-1,-1,-1)
    d2=(-3,2,2,1,-1,-1)
    all_deltas.extend([d1,d2,(4,-3,-1,0,0,0)])
    max_lookback=max((-p for d in all_deltas for (_,p) in marked_terms(d).keys()),default=0)
    rows=coefficients(m_max+max_lookback+6)
    A=A_independent(45)
    checked_direct=0
    checked_A=0
    for d in all_deltas:
        for m in range(0,9):
            assert marked_from_module(m,d,rows)==direct(m,d)
            checked_direct+=1
        for m in range(0,32):
            assert marked_from_module(m,d,rows)==marked_from_A(m,d,A)
            checked_A+=1
    for m in [5,6,9,20,50,100,200,300]:
        assert marked_from_module(m,d1,rows)==marked_from_module(m,d2,rows)
    old={5:'5285/419904',6:'9715/1259712',8:'259181485/78364164096',
         20:'89379684726508120031933065/371319292745659279662190166016',
         30:'13933171984643229314612138251752792090355/169700270766282144060148445395050707866877952'}
    for n,expected in old.items(): assert str(masked_mass(n,rows))==expected
    for m in range(30):
        a=A[m]; a1=A[m+1]; a2=A[m+2]
        formula=Fraction(a)-Fraction(a1,3*(m+1))+Fraction(a2-6*a1,30*(m+1)**2)
        assert formula==marked_from_module(m,(-2,0,0,0,0,2),rows)
    examples={str(n):str(masked_mass(n,rows)) for n in [5,8,20,30,50,100,200,300]}
    compact={}
    for n in [100,200,300]:
        f=masked_mass(n,rows)
        compact[str(n)]={'numerator_digits':len(str(f.numerator)),
                        'denominator_digits':len(str(f.denominator)),
                        'sha256_fraction':sha256(str(f).encode()).hexdigest()}
    sample={str(m):str(marked_from_module(m,d1,rows)) for m in [5,6,12,50,100,200,300]}
    return {'schema':'PREFIX1007_R6_FORMAL_POWER_REDUCTION_V1',
            'model':'Frozen X6 P000 V5, Stage46 signed typed Z2 BRC; PREFIX-1005 joint-port post-observer collision',
            'theorem':'For every zero-sum delta, H_m(delta)=m!^2[t^m]prod_i f_(delta_i), f_(k)=t^max(0,-k)g_|k|; g0=sum t^r/(r!)^2, g1=g0_prime, t*g_(k+1)=g_(k-1)-k*g_k. All marked H are finite A_d shifts by the d+1 symmetric-power differential operators.',
            'module_recurrence':'c_0,m=d*c_1,m-1/m; (m+j)c_j,m=(d-j)c_(j+1),m-1+j*c_(j-1),m',
            'checks_direct':checked_direct,'checks_A_only':checked_A,
            'checked_old_masked_n':list(old),
            'six_dim_sign_redistribution':{'delta_1':list(d1),'delta_2':list(d2),'same_absolute_multiset':True,'not_axis_permutation_or_global_sign':True,'samples':sample},
            'shift_two_example':'H_m(2e_i-2e_j)=A(m)-A(m+1)/(3(m+1))+(A(m+2)-6*A(m+1))/(30*(m+1)^2)',
            'masked_probability':examples,
            'large_n_fingerprints':compact,
            'method_limits':'O(D*m) exact rational operations/O(D) live coefficients for all g0^(D-j)*g1^j at fixed m, excluding large integer bit cost and finite-shift lookback; not new native Stage46 run or independent review.'}

if __name__=='__main__':print(json.dumps(run(),indent=2,ensure_ascii=False))
