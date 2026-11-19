#!/usr/bin/env python3
"""EC49FTS: exact rational verifier for a correlated decreasing log-concave ridge prior.
External price-prior postprocessing only; no native Bellman simulation.
"""
from fractions import Fraction as Q
import json

A0, A1 = Q(3,4), Q(49,64)
B0, B1 = Q(7,16), Q(57,128)
m2, m3 = Q(1469,64), Q(187,8)
p, q, threshold = Q(23), Q(93,4), Q(719,960)

def affine_cube_integral(c, d, left, right):
    """Integrate (c+d*x)^3 from left to right, entirely over Q."""
    return (c**3 * (right-left)
            + Q(3,2)*c*c*d*(right**2-left**2)
            + c*d*d*(right**3-left**3)
            + d**3*Q(1,4)*(right**4-left**4))

def int_square(c, d, left, right):
    """Integrate (c+d*x)^2 from left to right, entirely over Q."""
    return c*c*(right-left) + c*d*(right**2-left**2) + d*d*Q(1,3)*(right**3-left**3)

def L(m): return (8*m+173)/480
def b_m(m): return (47-m)/54
def x_m(m): return (740-m)/945
def a_c(b): return (77+6*b)/105
def a_m(b,m): return Q(3,175) + Q(8,525)*m + Q(22,25)*b

def A(m):
    return Q(16,945)*int_square(3-Q(82,945)+Q(37,1890)*m, -Q(94,45), L(m), Q(3,4))

def B(m):
    return Q(1,54)*int_square(3-b_m(m), -1, x_m(m), A1)

def cdf(m,t):
    return Q(16,945)*int_square(3-Q(82,945)+Q(37,1890)*m, -Q(94,45), L(m),t)/(A(m)+B(m))

def box_a_integral(a_low_constant, a_low_bcoef, b_low, b_high):
    # Integrate (3-a-b)^2 first in a, then in b.
    return Q(1,3)*(affine_cube_integral(3-a_low_constant,-1-a_low_bcoef,b_low,b_high)
                   - affine_cube_integral(3-A1,-1,b_low,b_high))

total=box_a_integral(A0,Q(0),B0,B1)
clipped=box_a_integral(Q(77,105),Q(2,35),B0,B1)
prior_prob=clipped/total

assert m2<p<q<m3
assert B0<b_m(q)<b_m(p)<B1
assert L(p)<L(q)<threshold<Q(3,4)
assert a_m(b_m(p),p)==x_m(p)
assert a_m(b_m(q),q)==x_m(q)
assert a_c(b_m(p))==x_m(p)
assert total==Q(4981,12582912)
assert clipped==Q(66463162673,372897113702400)
assert prior_prob==Q(66463162673,147612931200)
assert B(p)/A(p)==Q(68135166662375,57098970326016)
assert B(q)/A(q)==Q(1920393598107125,514197870898176)
assert B(p)/A(p)<B(q)/A(q)
assert cdf(p,threshold)==Q(142919525557120,375702410965173)
assert cdf(q,threshold)==Q(257409057608064,2434591469005301)
assert cdf(p,threshold)-cdf(q,threshold)==Q(251241454128026688021270338048,914681884620533840389663382073)>0

# Strict TP2 for rho(u)=(3-u)^2: d²log(K)/(dm dz)=3478/(42525*(3-u)^2)>0.
# Check independent exact 2x2 minors at rational interior rectangles.
def K(mm, zz):
    u=Q(82,945)-Q(37,1890)*mm+Q(94,45)*zz
    return Q(16,945)*(3-u)**2

strict_minors=0
for mlo,mhi in [(Q(23),Q(93,4)),(Q(921,40),Q(927,40)),(Q(93,4),Q(233,10))]:
    for zlo,zhi in [(Q(479,640),Q(719,960)),(Q(719,960),Q(3,4))]:
        if L(mhi)<zlo<zhi<=Q(3,4):
            det=K(mlo,zlo)*K(mhi,zhi)-K(mlo,zhi)*K(mhi,zlo)
            assert det>0
            strict_minors += 1
assert strict_minors>0
output={
    "schema":"EC49FTS_RIDGE_PRIOR_EXACT_CERT_V1",
    "scientific_pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
    "derived_from":"EC49FTR PR2795@6e6da57541f965b0c02c27ceed97daddff2e1417",
    "prior":"h(a,b) proportional to (3-a-b)^2",
    "domain":{"a":[str(A0),str(A1)],"b":[str(B0),str(B1)],"high_gap_m":[str(m2),str(m3)]},
    "clipped_probability":str(prior_prob),
    "cdf_at_m_23":str(cdf(p,threshold)),
    "cdf_at_m_93_over_4":str(cdf(q,threshold)),
    "cdf_positive_difference":str(cdf(p,threshold)-cdf(q,threshold)),
    "strict_tp2_minors_checked":strict_minors,
    "status":"AUTHOR_PROVED_EXACT_FRACTION_CHECKED_PARENT_DEPENDENT_NOT_REVIEWED"
}
print(json.dumps(output,indent=2))
