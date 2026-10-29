#!/usr/bin/env python3
"""R387 exact signed-BRC PF2 no-go checker. Python fractions + SymPy.
Import the original signed R384_verify.py sibling to rebuild K/J -> B -> D.
Finite checking r<=16 is regression; universal quantifier uses R386 and exact jets.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib, json, sys
import sympy as sp

HERE=Path(__file__).resolve().parent
SRC=HERE.parent/'r384_universal_signed_k3_catalan_top_20261029_emr3'
sys.path.insert(0,str(SRC if (SRC/'R384_verify.py').is_file() else HERE))
from R384_verify import build, differences

theta=F(15,8)
s,k=sp.symbols('s k')
def rational(x): return sp.Rational(x.numerator,x.denominator)
def reduced(x): return sp.factor(sp.cancel(sp.expand(sp.expand_func(x))))
def finitejet(m,d,C):
    return sum(sp.binomial(m,j)*sp.expand(C**j).coeff(s,d) for j in range(d+1))

H,Q=build(theta,16)
A=[H(r,0) for r in range(7)]
B=[]
for r in range(7):
    B.append(H(r,1)-sum((A[j]*B[r-j] for j in range(1,r+1)),F(0)))
assert A[:5]==[F(1),F(6),F(32),F(40),F(-320)]
assert B==[F(1),F(0),F(36,5),F(248,5),F(496),F(26304,5),F(63040)]
bs=sum(rational(B[j])*s**j for j in range(7))
lb=sp.series(sp.log(bs),s,0,7).removeO().expand()
E={j:lb.coeff(s,j) for j in range(2,7)}
assert E=={2:sp.Rational(36,5),3:sp.Rational(248,5),
           4:sp.Rational(11752,25),5:sp.Rational(122592,25),
           6:sp.Rational(7295392,125)}
a={i:rational(A[i]) for i in range(5)}
C=sum(E[j]/E[2]*s**(j-2) for j in range(3,7))
def U(m,d):
    return reduced(sum(a.get(i,0)*finitejet(m,d-i,C) for i in range(d+1)))
R=reduced(k/E[2]*U(k-1,2))
S=reduced(k*(k-1)/E[2]**2*U(k-2,4))
bt=reduced(k/E[2]*U(k-1,1))
bn=reduced(k*(k-1)/E[2]**2*U(k-2,3))
ct=U(k,1)
cn=reduced(k/E[2]*U(k-1,3))
M=reduced(bt*ct)
N=reduced(bt*cn+bn*ct)
q1=reduced(2*R+3*k-M)
q2=reduced(2*S+(6*k-3)*R+R**2+(9*k**2-5*k)/2-N-(3*k-2)*M)
e1=reduced(q1+sp.binomial(2*k,2))
e2=reduced(q2+sp.binomial(2*k-1,2)*q1+sp.binomial(2*k,3)+3*sp.binomial(2*k,4))
p=23088025*k**4-166084966*k**3+303079583*k**2-290082956*k+241021182
assert reduced(e1-k*(5069*k-3503)/729)==0
assert reduced(e2-k*(23088025*k**4+142252166*k**3-277249951*k**2+70249636*k+167395128)/6377292)==0
assert reduced((2*k-1)*e1**2-2*k*e2+k*k*p/sp.Integer(3188646))==0
t=sp.symbols('t')
positive=sp.Poly(sp.expand(p.subs(k,t+5)),t)
assert positive==sp.Poly(23088025*t**4+295675534*t**3+1275008843*t**2+1828352924*t+36990852,t)
assert all(v>0 for v in positive.all_coeffs())
rows=[]; even_checks=0; odd_checks=0
for r in range(1,17):
    c=differences(Q(r))
    assert len(c)==2*r+1
    negatives=[i for i,v in enumerate(c) if v<0]
    turans=[i for i in range(1,2*r) if c[i]**2-c[i-1]*c[i+1]<0]
    assert negatives or turans
    assert max(i for i,v in enumerate(c) if v)==r
    row={"r":r,"negative_coefficient_indices":negatives,"negative_turan_indices":turans}
    if r%2:
        assert c[r]==-comb(r,r//2)*180**r
        odd_checks+=1
    else:
        h=r//2
        f=F(25**r)*(F(36,5)**h/F(factorial(h)))**2
        z1=F(h*(5069*h-3503),729)
        z2=F(h*(23088025*h**4+142252166*h**3-277249951*h**2+70249636*h+167395128),6377292)
        assert c[r]==factorial(r)*f
        assert c[r-1]==factorial(r-1)*f*z1
        assert c[r-2]==factorial(r-2)*f*z2
        pp=23088025*h**4-166084966*h**3+303079583*h**2-290082956*h+241021182
        turan=c[r-1]**2-c[r-2]*c[r]
        assert turan==-F(factorial(r-1)**2)*f*f*F(h*h*pp,3188646*(r-1))
        even_checks+=4
        row["turan_at_r_minus_1"]=str(turan)
        if h>=5: assert turan<0
    rows.append(row)
for r,kind,idx,expected in [
    (2,"T",1,-36550080000),
    (4,"c",1,-38801920000),
    (6,"c",0,-611532248000000000),
    (8,"T",3,-363895513606887945543769505792000000000000000000)]:
    c=differences(Q(r))
    got=c[idx] if kind=="c" else c[idx]**2-c[idx-1]*c[idx+1]
    assert got==expected
    rows[r-1]["small_even_exact_negative_witness"]={"kind":kind,"index":idx,"value":str(got)}
assert even_checks==32 and odd_checks==8
evidence={"schema":"R387_EXACT_EVIDENCE_V1","model":"original signed twelve-branch BRC","theta":"15/8",
          "a_jet":[str(v) for v in A[:5]],"b_jet":[str(v) for v in B],
          "even_top_equalities":even_checks,"odd_highest_equalities":odd_checks,
          "shifted_positive_polynomial":str(positive.as_expr()),"rows":rows,
          "domain":"finite regression r=1..16; universal proof from R386 + exact symbolic finite jet",
          "admission":"AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED"}
ev=HERE/"R387_EVIDENCE.json"
ev.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
summary={"schema":"R387_SUMMARY_V1","status":"R387_EXACT_PASS",
         "even_top_identities":32,"odd_top_identities":8,"r_range":[1,16],
         "theta":"15/8","even_turan_negative_from_r":10,
         "small_even_witnesses":[2,4,6,8],
         "evidence_sha256":hashlib.sha256(ev.read_bytes()).hexdigest(),
         "project_admission":"UNREVIEWED_NOT_ADMITTED"}
(HERE/"R387_SUMMARY.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("R387_EXACT_PASS",json.dumps(summary,ensure_ascii=False))
