#!/usr/bin/env python3
"""R749STA: exact infinite three-read collision and fourth-read witness.
Frozen input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Python 3 + SymPy; exact rational polynomial certificates.
"""
import json
from math import factorial
from pathlib import Path
import sympy as sp

q, d, k, u, z = sp.symbols("q d k u z")
S = lambda n: 18*n**4+54*n**3-345*n**2+2070*n-16315
A = sum(z**i for i in range(6))
B = (1+z**2+z**4)*(1+z**3)
PC = sp.Poly(sp.expand(z*A**3*B),z)
PT = sp.Poly(sp.expand(z**2*A**4*B),z)
assert (PC.degree(),PT.degree()) == (23,29)

def binom_poly(x,n):
    return sp.prod(x-i for i in range(n))/factorial(n)

def component(poly,order,r):
    return sp.factor(sum(
        poly.nth(r+6*j)*binom_poly((q-r)/6-j+order-1,order-1)
        for j in range((poly.degree()-r)//6+1)))

C1,T1 = component(PC,6,1),component(PT,7,1)
C5,T5 = component(PC,6,5),component(PT,7,5)
assert all(sp.degree(v,q)==deg for v,deg in
           ((C1,5),(T1,6),(C5,5),(T5,6)))

# q ≡ 1 (mod 6), p=q+4. The q-candidate has e=-3/2.
x,b = [],[]
for j in range(3):
    a,p = q+6*j,q+4+6*j
    y = a**3*(T1.subs(q,a)-sp.Rational(3,2))/(C1.subs(q,a)+d)-S(a)/108
    xx = sp.cancel((y+S(p)/108)/p**3)
    x.append(xx)
    b.append(sp.cancel(xx*C5.subs(q,p)-T5.subs(q,p)))

D = sp.factor(sp.together((b[0]-b[1])/(x[1]-x[0])))
E = sp.factor(sp.together(b[0]+x[0]*D))
F = sp.factor(sp.together(
    (b[0]-b[1])*(x[2]-x[0])-(b[0]-b[2])*(x[1]-x[0])))
FN,FH = sp.fraction(F)

# Verify positivity for all q=73+k (k>=0), d=-u/(1+u) (-1<=d<=0).
def positive_shift(poly,name):
    cs=sp.Poly(sp.expand(poly.subs(q,73+k)),k).all_coeffs()
    assert cs and all(c.is_Rational and c>0 for c in cs),name
    return dict(name=name,degree_k=len(cs)-1,count=len(cs),
                min_positive=str(min(cs)))

def positive_rectangle(poly,name):
    pp=sp.Poly(poly,d);m=pp.degree()
    src=[sp.Poly(pp.nth(j).subs(q,73+k),k) for j in range(m+1)]
    new=[sp.Poly(0,k) for _ in range(m+1)]
    for j in range(m+1):
        for h in range(m-j+1):
            new[j+h] += (-1)**j*sp.binomial(m-j,h)*src[j]
    cs=[c for p in new for c in p.all_coeffs()]
    assert cs and all(c.is_Rational and c>0 for c in cs),name
    return dict(name=name,degree_k=max(p.degree() for p in new),
                degree_u=m,count=len(cs),min_positive=str(min(cs)))

checks=[
    positive_shift(-FN.subs(d,-1),"-numerator_at_d=-1"),
    positive_shift(FN.subs(d,0),"numerator_at_d=0"),
    positive_rectangle(FH,"collinearity_denominator")]
for name,v in (("E",E),("D",D)):
    n,h=sp.fraction(v)
    checks.extend([
        positive_rectangle(h,name+"_denominator"),
        positive_rectangle(2*h+n,name+"_lower_guard"),
        positive_rectangle(2*h-n,name+"_upper_guard")])
assert len(checks)==9 and sum(c["count"] for c in checks)==450

# Exact isolated algebraic collision q=73, p=77.
poly=sp.Poly(FN.subs(q,73),d).primitive()[1]
assert poly.degree()==3
assert sp.sign(poly.eval(-1))*sp.sign(poly.eval(-sp.Rational(9,10)))==-1
assert sp.count_roots(poly,-1,-sp.Rational(9,10))==1
E0,D0=E.subs(q,73),D.subs(q,73)
a,p=91,95
y0=a**3*(T1.subs(q,a)-sp.Rational(3,2))/(C1.subs(q,a)+d)-S(a)/108
y1=p**3*(T5.subs(q,p)+E0)/(C5.subs(q,p)+D0)-S(p)/108
R4=sp.factor(y1-y0)
R4num,_=sp.fraction(R4)
assert sp.gcd(poly,sp.Poly(R4num,d)).degree()==0

out={
    "unit":"R749STA","status":"PASS","evidence":"AUTHOR_EXACT_NOT_REVIEWED",
    "scientific_pin":"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
    "theorem":"For every q>=73, q=1 mod 6, a q and q+4 pair has an exact three-read collision with all errors strictly inside (-2,2). Thus global minimum horizon >=4.",
    "fixed_original_e":"-3/2","original_d":"root in (-1,0)",
    "alternative_parameters":"E(q,d), D(q,d), rational functions defined in accompanying proof and code",
    "positivity_checks":checks,
    "strictly_positive_coefficients":sum(c["count"] for c in checks),
    "q73_cubic":str(poly.as_expr()),
    "q73_root_isolation":["-1","-9/10"],
    "q73_fourth_read_num_gcd_degree":0,
    "proof_scope":"exact all-cutoff rational algebra plus IVT, not a finite grid",
    "next":"four-read uniform separability versus a new exact collision family"
}
dest=Path(__file__).with_name("R749STA_INFINITE_THREE_READ_COLLISION_RESULTS.json")
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
print("PASS",out["strictly_positive_coefficients"],
      "positive coefficients; q73 fourth-read gcd 0")
