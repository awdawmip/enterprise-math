#!/usr/bin/env python3
"""R749SQF: exact marginal/joint Dirichlet spline and finite source-tail certificate.
Python stdlib only; no float, all rational coefficients. Independent of live Source controls.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from math import comb, factorial
import json

FACETS = [(-1,-1,-1,-2),(-1,-1,1,-2),(-1,1,-1,-2),(-1,1,1,-2),
          (1,-1,-1,-2),(1,-1,1,-4),(1,1,-1,-4),(1,1,1,-2)]
P = [(h,u,v) for h in range(-2,3) for u in range(-2,3) for v in range(-2,3)
     if all(a*h+b*u+c*v >= t for a,b,c,t in FACETS)]
assert len(P)==33
pairs=defaultdict(list)
for i in range(len(P)):
    for j in range(i,len(P)):
        pairs[tuple(P[i][k]+P[j][k] for k in range(3))].append((i,j))
forced = sorted({P[i] for opts in pairs.values() if len(opts)==1 for i in opts[0]})
assert len(forced)==25
B=[(h,2-u,v) for h,u,v in forced if u<2]
assert len(B)==23 and B.count((0,1,1))==1
OTHER=sorted((2*d-1-v,h+d-v,h,d,v) for h,d,v in B if (h,d,v)!=(0,1,1))
LETTERS=[(s,b,b,0) for s,b,_,_,_ in OTHER]+[(3,2,1,1)]
assert len(LETTERS)==23
assert Counter(s for s,b0,b1,k in LETTERS)=={1:3,2:4,3:6,4:4,5:3,6:2,7:1}
assert all(s>0 and b0>=0 and b1>=0 for s,b0,b1,k in LETTERS)

# Conditional core has Z0 and 22 compulsory positive-slack letters.
KNOTS=[Q(0)]+[Q(b1,s) for s,b0,b1,k in LETTERS if k==0]
M=len(KNOTS)
assert M==23
MULT=Counter(KNOTS)
assert sorted(MULT.items())==[(Q(0),6),(Q(1,4),1),(Q(1,3),1),
    (Q(1,2),2),(Q(4,7),1),(Q(3,5),1),(Q(2,3),2),
    (Q(3,4),1),(Q(4,5),2),(Q(1),4),(Q(4,3),1),(Q(2),1)]

# R(z)=prod(z-a)^-mult; partial fractions: R(z)=sum c[a,j]/(z-a)^j.
# Compute local Taylor coefficients at every pole by finite binomial products.
COEFF={}
for a,mult in sorted(MULT.items()):
    series=[Q(1)]+[Q(0)]*(mult-1)
    for b,m in MULT.items():
        if a==b:continue
        delta=a-b
        factor=[Q((-1)**i*comb(m+i-1,i),1)/delta**(m+i) for i in range(mult)]
        series=[sum(series[i-k]*factor[k] for k in range(i+1)) for i in range(mult)]
    for j in range(1,mult+1): COEFF[(a,j)]=series[mult-j]
assert len(COEFF)==sum(MULT.values())

# For m=23, CDF = sum_a,j (-1)^(m+j-2) * C(m-1,j-1) * c[a,j] * (x-a)_+^(m-j).
# All max multiplicities are <m, so no point-mass boundary terms.
TERMS=sorted((a, M-j, Q((-1)**(M+j-2)*comb(M-1,j-1))*c)
             for (a,j),c in COEFF.items())
def cdf(x):
    return sum((co*(x-a)**p for a,p,co in TERMS if x>a),Q(0))

def integrate_x_power_times_cdf(pminus1):
    nodes=sorted(MULT)
    total=Q(0)
    for lo,hi in zip(nodes,nodes[1:]):
        for a,degree,co in TERMS:
            if a>lo:continue
            for k in range(pminus1+1):
                total+=co*comb(pminus1,k)*a**(pminus1-k)*(
                    (hi-a)**(degree+k+1)-(lo-a)**(degree+k+1))/Q(degree+k+1)
    return total

def poly_moment(p):
    return Q(2)**p - p*integrate_x_power_times_cdf(p-1)

# Dirichlet simplex moment: p!*h_p(knots)/(M)_p.
def homogeneous_moments(maxp):
    h=[Q(1)]+[Q(0)]*maxp
    for a in KNOTS:
        for p in range(1,maxp+1):h[p]+=a*h[p-1]
    return h

def dirichlet_moment(p,h):
    rising=1
    for j in range(p):rising*=M+j
    return Q(factorial(p)*h[p],rising)

h=homogeneous_moments(4)
moments={}
for p in range(1,5):
    via_spline=poly_moment(p)
    via_simplex=dirichlet_moment(p,h)
    assert via_spline==via_simplex, (p,via_spline,via_simplex)
    moments[p]=via_spline
assert moments[1]==Q(482,805)
assert moments[2]-moments[1]**2==Q(11407951,1119787200)
for a in sorted(MULT):
    assert 0 <= cdf(a) <= 1
    assert cdf(a) <= cdf((a+Q(2))/2) <= 1
assert cdf(Q(0))==0 and cdf(Q(2))==1
assert all(cdf(hi)>cdf(lo) for lo,hi in zip(sorted(MULT),sorted(MULT)[1:]))

# Finite depth: C_r=# {m>=0: slack dot m <= r-1}.
# Independent check of exact optional-counter tail decomposition against
# 22-letter integer weighted partition coefficient dynamic programming.
R=120
def counts(weights):
    exact=[0]*R
    exact[0]=1
    for s in weights:
        for d in range(s,R):exact[d]+=exact[d-s]
    accum=[];s=0
    for n in exact:
        s+=n;accum.append(s)
    return accum
all_counts=counts([s for s,b0,b1,k in LETTERS])
base_counts=counts([s for s,b0,b1,k in LETTERS if not k])
checks=[]
for r in range(1,R+1):
    dist=[base_counts[r-1-3*k] for k in range((r-1)//3+1)]
    assert sum(dist)==all_counts[r-1]
    tail=[sum(dist[k:]) for k in range(1,len(dist))]
    expected_tail=[all_counts[r-3*k-1] for k in range(1,len(dist))]
    assert tail==expected_tail, (r,tail,expected_tail)
    EK=Q(sum(k*v for k,v in enumerate(dist)),all_counts[r-1])
    assert EK==sum((Q(c,all_counts[r-1]) for c in expected_tail),Q(0))
    if r in (1,4,8,10,20,40,80,120):
        checks.append({'r':r,'C_r':str(all_counts[r-1]),'E_K':str(EK),
                       'Pr_K_ge_1':str(Q(expected_tail[0],all_counts[r-1]) if expected_tail else Q(0)),
                       'support_K':len(dist)})
# Exact boundary marginal K=Zoptional/3 where Zoptional~Beta(1,23).
# Density 69*(1-3k)^22 on [0,1/3], exact p-th moments.
Kmom={}
for p in range(1,5):
    num=1;den=1
    for j in range(1,p+1):num*=j;den*=23+j
    Kmom[p]=Q(num,3**p*den)
assert Kmom[1]==Q(1,72)
assert Kmom[2]-Kmom[1]**2==Q(23,129600)
# Paired limit Y1=K+(1-3K)S, Y0=2K+(1-3K)S, K independent of S.
EY1=Kmom[1]+(1-3*Kmom[1])*moments[1]
EY0=EY1+Kmom[1]
assert (EY0,EY1)==(Q(379,630),Q(1481,2520))
# Covariance structure from independent (S,K) using Bernoulli-free algebra.
E_Y1K=Kmom[2]+(Kmom[1]-3*Kmom[2])*moments[1]
CovY1K=E_Y1K-EY1*Kmom[1]
assert CovY1K==Q(-641,4536000)
CovY0K=CovY1K+(Kmom[2]-Kmom[1]**2)
assert CovY0K==Q(41,1134000)

out={
 'schema':'R749SQF_DIRICHLET_SPLINE_AND_PROVENANCE_TAIL_V1','status':'PASS',
 'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'provenance':'R749SQE immutable science @087166f458cef7c564d4e4df1de7c58846075861',
 'model':'auxiliary 16-atom Walsh t=1/10,s=1/2, uniform missing-source multisets',
 'arithmetic':'Python stdlib Fraction and integer only; no float',
 'source_types':{'positive_slack':23,'other':22,'conditional_simplex_barycentric':23},
 'conditional_knots':[{'knot':str(a),'multiplicity':m} for a,m in sorted(MULT.items())],
 'spline':{'degree':21,'distinct_knots':len(MULT),'partial_fraction_terms':len(TERMS),
           'boundary_F_0':str(cdf(Q(0))),'boundary_F_2':str(cdf(Q(2)))},
 'conditional_S_moments':{str(p):str(v) for p,v in moments.items()},
 'conditional_S_variance':str(moments[2]-moments[1]**2),
 'marginal_K_density':'69*(1-3k)^22 indicator(0<k<1/3)',
 'marginal_K_moments':{str(p):str(v) for p,v in Kmom.items()},
 'limit_means':{'Y0':str(EY0),'Y1':str(EY1),'K':str(Kmom[1])},
 'limit_covariances':{'Y1_K':str(CovY1K),'Y0_K':str(CovY0K)},
 'finite_tail_identity':'Pr(K_r >= k)=C_(r-3k)/C_r, C_s=0 for s<1',
 'finite_checks':{'r_max':R,'tail_full_range':True,'independent_no_optional_partition':True,'cases':checks},
 'formal_claim':'all-depth exact finite tail + Dirichlet conditional disintegration and confluent spline by divided differences',
 'scope':'AUTHOR_EXACT_NOT_REVIEWED; dependent on inherited 33-point and 25-forced-letter classification'}
print(json.dumps(out,indent=2,ensure_ascii=False))
