#!/usr/bin/env python3
"""EC49FTP exact polynomial witness validation; derived from EC49FTO pricing maps.
No native BRC Bellman computation. Python stdlib fractions only.
"""
from fractions import Fraction as F
from itertools import combinations
import json
A0,A1=F(3,4),F(49,64)
B0,B1=F(7,16),F(57,128)
M0,M1,M2,M3=F(11457,512),F(1461,64),F(1469,64),F(187,8)
ALPHA,BETA=F(44,45),F(10,9)

def f(a):return 1+(a-A0)**2
def g(b):return b
def af(m,z): return (47-m)/945+ALPHA*z
def bf(m,z): return F(1,27)-m/54+BETA*z
def lo(m):return (4*m+2647)/3696 if m<M1 else (8*m+173)/480
def hi(m):return (64*m+1411)/3840 if m<M2 else F(3,4)
def fl_primitive(a):return a+(a-A0)**3/3

def poly_convolve(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):r[i+j]+=x*y
    return r

def integral(p,l,u):return sum(c*(u**(k+1)-l**(k+1))/(k+1) for k,c in enumerate(p))
def polynomial_k(m):
    aa=(47-m)/945-A0; bb=F(1,27)-m/54
    return poly_convolve([1+aa*aa,2*aa*ALPHA,ALPHA*ALPHA],[bb,BETA])
def continuous_integral(m,l,u):return F(16,945)*integral(polynomial_k(m),l,u)
def atom_integral(m):
    if m<=M2:return F(0)
    x=(740-m)/945; y=(47-m)/54
    return y*(fl_primitive(A1)-fl_primitive(x))/54

def cdf(m,z):
    l,u=lo(m),hi(m)
    if z<=l:return F(0)
    if z>=F(3,4) or (m<=M2 and z>=u):return F(1)
    numer=continuous_integral(m,l,min(z,u))
    return numer/(continuous_integral(m,l,u)+atom_integral(m))

# clip probability = [int_b b (int_a^A1 f(a)da) db] / [int_A f int_B b].
# ac(b)=(77+6b)/105, with A0=3/4 and a_c <=A1 for b in B.
# Since (ac - A0) = (77+6b)/105 -3/4, integrate polynomial exactly.
ac0=F(77,105); ac1=F(6,105)
t0=ac0-A0
# F(A1)-F(ac)= A1 - ac + ((A1-A0)^3-(ac-A0)^3)/3
# polynomial of b, as list coefficients
cub=[t0**3,3*t0*t0*ac1,3*t0*ac1**2,ac1**3]
C=[A1-ac0+(A1-A0)**3/3-cub[0]/3, -ac1-cub[1]/3,-cub[2]/3,-cub[3]/3]
num=integral(poly_convolve(C,[F(0),F(1)]),B0,B1)
den=(fl_primitive(A1)-fl_primitive(A0))*(B1*B1-B0*B0)/2
clip=num/den
# TP2 derivative lower bound: [beta/(54 *B1^2)] - 2*alpha/945 >0
TP2margin=BETA/(54*B1**2) - 2*ALPHA/945
assert TP2margin>0
# d reaches max at m=M3 since x=(740-m)/945 decreases
Dmax=A1-(740-M3)/945
assert Dmax>0 and Dmax <1
assert 2*Dmax*Dmax <2
# support endpoint monotonically increasing (inherited)
assert lo(M0)==hi(M0)
assert hi(M2)==F(3,4)
assert lo(M3)==hi(M3)==F(3,4)

ms=[]
for l,u in ((M0,M1),(M1,M2),(M2,M3)):
    ms += [l+(u-l)*j/13 for j in range(1,13)]
zlist=[F(11,16)+(F(3,4)-F(11,16))*j/36 for j in range(37)]
passed=0
for m,n in combinations(ms,2):
    for z in zlist:
        x,y=cdf(m,z),cdf(n,z)
        assert y<=x,(m,n,z,x,y)
        passed+=1
# exact check for inverse points
inverse_count=0
for m in ms:
    l,u=lo(m),hi(m)
    assert continuous_integral(m,l,u)>0
    assert atom_integral(m)>=0
    for j in range(13):
        z=l+(u-l)*j/12
        aa,bb=af(m,z),bf(m,z)
        assert A0<=aa<=A1 and B0<=bb<=B1,(m,z,aa,bb)
        assert af(m,z)==(47-m)/945+ALPHA*z
        inverse_count+=1
report={"schema":"EC49FTP_EXACT_POLYNOMIAL_PRIOR_CERT_V1","date":"2026-11-19","status":"AUTHOR_PROVED_EXACT_FRACTION_REPRODUCED_PARENT_DEPENDENT_NOT_REVIEWED","original_science":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab","price_parent":"EC49FTO PR2788@d790653d2e61b3d4db0a8fe066e746d0ad6196d7","prior":{"f":"1+(a-3/4)^2","g":"b","f_logconcave":False,"g_logconcave":True,"f_logcurvature_upper_bound":"2","g_logcurvature_upper_bound":str(-1/B1**2)},"clipping_probability":str(clip),"clipping_num":str(num),"weight_den":str(den),"tp2_margin_rational":str(TP2margin),"dmax":str(Dmax),"cdf_checks":passed,"inverse_grid_points":inverse_count,"m_grid_size":len(ms),"threshold_grid_size":len(zlist),"native_bellman_rerun":False,"formal_review":False}
print(json.dumps(report,indent=2,ensure_ascii=False))
