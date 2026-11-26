#!/usr/bin/env python3
"""EC49FTL optimized exchange-gap CDF: independent exact Fraction checks."""
from fractions import Fraction as F
B0,B1=F(7,16),F(57,128)
W=B1-B0
m0,m1,m2,m3=F(11457,512),F(1461,64),F(1469,64),F(187,8)

def cdf(m):
    if m<m0: return F(0)
    if m<m1: return (512*m-11457)**2/F(242550)
    if m<m2: return (1024*m-23145)/F(1050)
    if m<m3: return -(137216*m*m-6555968*m+78144641)/F(127575)
    return F(1)

def direct_cdf(m):
    alpha=F(512,525)
    def partial_integral(lo,hi):
        return alpha*((m-F(1539,32))*(hi-lo)+F(231,8)*(hi*hi-lo*lo))
    if m<m0: return F(0)
    if m<m1:
        lo=(F(1539,32)-m)/F(231,4)
        return partial_integral(lo,B1)/W
    if m<m2: return partial_integral(B0,B1)/W
    if m<m3:
        upper=(47-m)/54
        return (partial_integral(B0,upper)+(B1-upper))/W
    return F(1)

assert [cdf(x) for x in (m0,m1,m2,m3)]==[F(0),F(11,50),F(359,1050),F(1)]
for i,(lo,hi) in enumerate(((m0,m1),(m1,m2),(m2,m3))):
    for j in range(49):
        m=lo+(hi-lo)*F(j,48)
        assert cdf(m)==direct_cdf(m),(i,j,m)

def integrate_poly(coeffs,lo,hi):
    return sum((q*(hi**(i+1)-lo**(i+1))/F(i+1) for i,q in enumerate(coeffs)),F(0))

polys=[
 [F(11457**2,242550),-F(2*512*11457,242550),F(512**2,242550)],
 [-F(23145,1050),F(1024,1050)],
 [-F(78144641,127575),F(6555968,127575),-F(137216,127575)]
]
mean=m0;second=m0*m0
for lo,hi,p in zip((m0,m1,m2),(m1,m2,m3),polys):
    complement=[F(1)-p[0]]+[-x for x in p[1:]]
    mean+=integrate_poly(complement,lo,hi)
    second+=integrate_poly([F(0)]+[2*x for x in complement],lo,hi)
assert mean==F(494813,21504)
assert second-mean*mean==F(60097,1204224)
print("EC49FTL_OPTIMIZED_GAP_FULL_CDF_PASS")
print("cutoffs",*[str(x) for x in (m0,m1,m2,m3)])
print("cdf_junctions",*(str(cdf(x)) for x in (m0,m1,m2,m3)))
print("cdf_fraction_samples",147)
print("E_M",mean)
print("Var_M",second-mean*mean)
