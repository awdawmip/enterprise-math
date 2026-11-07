#!/usr/bin/env python3
"""R542 exact rational Rouche disks and residue dominance for signed BRC k=3,4.
Proof arithmetic: Fraction, integer isqrt. No floating point used in assertions.
Frozen science R462: 18783e01e3646c72b7aab3b16d3f565e83e6446f.
"""
from fractions import Fraction as F
from math import comb, isqrt
from itertools import combinations

def C(a,b=0): return (F(a), F(b))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def norm2(a): return a[0]*a[0]+a[1]*a[1]
def sqrt_floor(q,scale=1000000):
    assert q>=0
    return F(isqrt(q.numerator*scale*scale//q.denominator),scale)
def sqrt_ceil(q,scale=1000000):
    t=sqrt_floor(q,scale)
    return t if t*t==q else t+F(1,scale)
def LB(z): return sqrt_floor(norm2(z))
def UB(z): return sqrt_ceil(norm2(z))

def cat(k): return comb(2*k,k)//(k+1)
def H(k,t):
    r=2*k+1
    if not 2<=t<=r:return 0
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*cat(k-q)
        for q in range(min((t-1)//2,k)+1))
def poly(k):
    p={t:F(H(k,t),cat(k)) for t in range(2,2*k+2)}
    d=2*k-1
    a=[(-1)**(j-1)*p[j+2]*p[2]**(j-1) for j in range(1,d+1)]
    return [F(1)]+[-v for v in a],p
def taylor(poly,c):
    out=[C(0)]
    for v in poly:
        z=[C(0)]*(len(out)+1)
        for j,a in enumerate(out):
            z[j]=add(z[j],mul(c,a))
            z[j+1]=add(z[j+1],a)
        z[0]=add(z[0],C(v))
        out=z
    assert out[-1]==C(0)
    return out[:-1]

centers={
 3:[C('237.122'),C('57.813','33.070'),C('57.813','-33.070'),
    C('96.626','105.937'),C('96.626','-105.937')],
 4:[C('755.966'),C('148.322','67.276'),C('148.322','-67.276'),
    C('203.227','145.134'),C('203.227','-145.134'),
    C('392.468','452.340'),C('392.468','-452.340')]
}
eps=F(1,10)

for k in (3,4):
    coeff,p=poly(k);d=len(coeff)-1
    assert len(centers[k])==d
    for i,c in enumerate(centers[k]):
        a=taylor(coeff,c)
        left=UB(a[0])+sum(UB(a[j])*eps**j for j in range(2,d+1))
        right=LB(a[1])*eps
        # Rouche: P(c+w) has exactly one root in |w|<eps.
        assert left<right
        assert 100*left<right # simple published certificate: ratio < 1/100
    distances={(i,j):(LB(sub(centers[k][i],centers[k][j])),
                      UB(sub(centers[k][i],centers[k][j])))
               for i,j in combinations(range(d),2)}
    def dist(i,j):return distances[tuple(sorted((i,j)))]
    assert all(dist(i,j)[0]>2*eps for i,j in combinations(range(d),2))
    alpha_lower=centers[k][0][0]-eps
    def root_upper(i):return UB(centers[k][i])+eps
    assert all(root_upper(i)<alpha_lower for i in range(1,d))
    # All roots simple; the isolated dominant root alpha is real positive.
    # Since other roots come in conjugate pairs, P'(alpha)>0.
    dominant_lower=alpha_lower**(d-1)
    for j in range(1,d):
        dominant_lower/=dist(0,j)[1]+2*eps
    other_upper=[]
    for i in range(1,d):
        v=root_upper(i)**(d-1)
        for j in range(d):
            if j!=i:v/=dist(i,j)[0]-2*eps
        other_upper.append(v)
    total_other=sum(other_upper,F(0))
    assert dominant_lower>total_other
    if k==3:
        assert dominant_lower>F(305,100)>F(220,100)>total_other
        assert alpha_lower>237 and max(root_upper(i) for i in range(1,d))<144
    if k==4:
        assert dominant_lower>F(452,100)>F(369,100)>total_other
        assert alpha_lower>755 and max(root_upper(i) for i in range(1,d))<600
    # A_j=lambda_j^(d-1)/P'(lambda_j). The exact bounds above imply
    # A_0>sum_{j>0}|A_j| and |lambda_j|<lambda_0 for j>0.
    # Therefore [z^m]1/prod_j(1-lambda_j*z)>0 for every integer m>=0.
    f=[F(1)]
    a=[-v for v in coeff[1:]]
    for m in range(1,1001):
        f.append(sum(a[j-1]*f[m-j] for j in range(1,min(d,m)+1)))
    assert all(v>0 for v in f)
    print("k",k,"polynomial",','.join(map(str,coeff)))
    print("k",k,"dominant_lower",str(dominant_lower))
    print("k",k,"other_upper",str(total_other))
    print("k",k,"recurrence_orders_0_1000_PASS")
print("R542_EXACT_ROUCHE_RESIDUE_PASS")
