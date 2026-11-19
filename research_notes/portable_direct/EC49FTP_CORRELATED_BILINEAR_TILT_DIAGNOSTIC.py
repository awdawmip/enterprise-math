#!/usr/bin/env python3
"""Numerical diagnostic ONLY of correlated EC49FTP theorem; not a mathematical proof."""
import math
from scipy.integrate import quad
from fractions import Fraction as F
from itertools import combinations
A0,A1=F(3,4),F(49,64)
M0,M1,M2,M3=F(11457,512),F(1461,64),F(1469,64),F(187,8)
ALPHA,BETA=F(44,45),F(10,9)
alpha,beta=float(ALPHA),float(BETA)

def l(m):return float((4*m+2647)/3696 if m<M1 else (8*m+173)/480)
def u(m):return float((64*m+1411)/3840 if m<M2 else F(3,4))
def h(a,b):return (1+(a-.75)**2)*b*math.exp(a*b)
def kernel(m,z):
    m=float(m)
    a=(47-m)/945+alpha*z
    b=1/27-m/54+beta*z
    return (16/945)*h(a,b)
def clip(m):
    if m<=M2:return 0.0
    x=(740-float(m))/945;y=(47-float(m))/54
    return quad(lambda a:h(a,y),x,float(A1),epsabs=1e-14)[0]/54
def cdf(m,z):
    a,b=l(m),u(m)
    if z<=a:return 0
    if z>=.75 or (m<=M2 and z>=b):return 1
    atom=clip(m)
    whole=quad(lambda x:kernel(m,x),a,b,epsabs=1e-14)[0]
    partial=quad(lambda x:kernel(m,x),a,min(z,b),epsabs=1e-14)[0]
    return partial/(whole+atom)
ms=[]
for aa,bb in [(M0,M1),(M1,M2),(M2,M3)]:
    ms.extend([aa+(bb-aa)*j/9 for j in range(1,9)])
zs=[float(F(11,16)+(F(3,4)-F(11,16))*j/32) for j in range(33)]
checked=0;worst=0.0
for m,n in combinations(ms,2):
    for z in zs:
        a,b=cdf(m,z),cdf(n,z)
        worst=max(worst,b-a)
        assert b<=a+1e-12,(m,n,z,a,b)
        checked+=1
print({'numeric_diagnostic':'PASS','numeric_comparisons':checked,
       'max_later_cdf_minus_earlier_cdf':worst,'kappa':1,
       'numeric_arithmetic':'float64 scipy.quad','scientific_status':'diagnostic_only_not_proof'})
