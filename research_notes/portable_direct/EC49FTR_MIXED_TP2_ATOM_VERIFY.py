#!/usr/bin/env python3
"""EC49FTR: exact rational certificate for nonconstant TP2 and top atom.
Standard library only. External price-prior postprocessing, no native Bellman.
"""
from fractions import Fraction as F
import json

M0,M1=F(1469,64),F(187,8)
U=F(3,4)
L=lambda m:(8*m+173)/480
X=lambda m:(740-m)/945
am=lambda m,z:(47-m)/945+F(44,45)*z
bm=lambda m,z:F(1,27)-m/54+F(10,9)*z
bclip=lambda m:(47-m)/54
h=lambda a,b:1+a+b
c=F(16,945)

# Integrate a linear K across the moving continuous fiber exactly.
def primitive(m,z):
    return c*((1+(47-m)/945+F(1,27)-m/54)*z
              +(F(44,45)+F(10,9))*z*z/2)
def A(m): return primitive(m,U)-primitive(m,L(m))
def B(m):
    left=X(m); right=F(49,64); bc=bclip(m)
    return ((1+bc)*(right-left)+(right*right-left*left)/2)/54
def N(m,t): return primitive(m,t)-primitive(m,L(m))
def r(m): return B(m)/A(m)

def A_pol(m): return (8*m-187)*(328*m-339677)/F(4286520000)
def B_pol(m): return -(64*m-1055)*(256*m-35545)/F(43893964800)
def r_pol(m):
    return -25*(64*m-1055)*(256*m-35545)/(256*(8*m-187)*(328*m-339677))
def d_r_pol(m):
    return 175*(86716736*m*m-4206719534*m+128240419955)/(
        4*(8*m-187)**2*(328*m-339677)**2)

def poly_mul(u,v):
    ans=[F(0)]*(len(u)+len(v)-1)
    for i,a in enumerate(u):
        for j,b in enumerate(v): ans[i+j]+=a*b
    return ans
def poly_deriv(u): return [i*u[i] for i in range(1,len(u))]
def poly_sub(u,v):
    return [(u[i] if i<len(u) else F(0))-(v[i] if i<len(v) else F(0))
            for i in range(max(len(u),len(v)))]
def poly_eval(p,x):
    acc=F(0)
    for a in reversed(p): acc=acc*x+a
    return acc

num=poly_mul([F(-1055),F(64)],[F(-35545),F(256)])
den=poly_mul([F(-187),F(8)],[F(-339677),F(328)])
Rnum=[F(-25,256)*a for a in num]
dnum=poly_sub(poly_mul(poly_deriv(Rnum),den),
              poly_mul(Rnum,poly_deriv(den)))

for i in range(1,100):
    m=M0+(M1-M0)*F(i,100)
    assert A(m)==A_pol(m) and B(m)==B_pol(m)
    assert r(m)==r_pol(m)
    assert poly_eval(dnum,m)/poly_eval(den,m)**2==d_r_pol(m)>0
    assert L(m)<U and A(m)>0 and B(m)>0
    mm=m+(M1-m)/7
    for v,w in [(F(1,5),F(3,5)),(F(1,4),F(4,5)),(F(1,6),F(5,6)),(F(2,7),F(6,7))]:
        s=L(mm)+(U-L(mm))*v
        t=L(mm)+(U-L(mm))*w
        k=lambda xx,zz:c*h(am(xx,zz),bm(xx,zz))
        assert k(m,s)*k(mm,t)>k(m,t)*k(mm,s)

quad=[128240419955,-4206719534,86716736]
disc=quad[1]**2-4*quad[0]*quad[2]
assert disc==-26785873329330290364<0

p,q,t=F(23),F(93,4),F(719,960)
assert M0<p<q<M1 and L(q)<t<U
rp,rq=r(p),r(q)
fp,fq=N(p,t)/(A(p)+B(p)),N(q,t)/(A(q)+B(q))
assert rp==F(103058075,85026048)
assert rq==F(320344225,85005056) and rp<rq
assert fp==F(212459840,564252369)
assert fq==F(42481472,405349281)
assert fp-fq==F(20716724056922624,76239764025565563)>0

certificate={
    "schema":"EC49FTR_MIXED_TP2_ATOM_CERT_V1",
    "frozen_science":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
    "parent_pr":2793,"model":"external-price-prior postprocessing only",
    "density":"h(a,b) proportional to 1+a+b",
    "continuous_kernel":"(16/945)*(2054-37m+3948z)/1890, strictly TP2",
    "atom_ratio_derivative_discriminant":str(disc),
    "r_23":str(rp),"r_93_over_4":str(rq),
    "F_23":str(fp),"F_93_over_4":str(fq),
    "exact_positive_gap":str(fp-fq),
    "sampled_integral_rational_checks":99,
    "sampled_tp2_checks":396,
    "mathematical_scope":"analytic iff + exact rational nonproduct witness; inherited native parent unreviewed",
    "status":"AUTHOR_PROVED_EXACT_RATIONAL_CHECKED_PARENT_DEPENDENT_NOT_REVIEWED"
}
print(json.dumps(certificate,indent=2,ensure_ascii=False))
