#!/usr/bin/env python3
"""Exact universal one-initial-read overlap classification for q=73,p=73+6h."""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp

N=73+6*131
weights=(1,1,2,3,6)
part=[0]*(N+1);part[0]=1
for w in weights:
    for i in range(w,N+1):
        part[i]+=part[i-w]
C=[0]*(N+1);T=[0]*(N+1)
for n in range(1,N+1):
    C[n]=C[n-1]+part[n-1]
    T[n]=T[n-1]+C[n-1]
def S(n):return 18*n**4+54*n**3-345*n**2+2070*n-16315
def Y(n,e,d):return F(n**3*(T[n]+e),C[n]+d)-F(S(n),108)
qmin=Y(73,-2,2);qmax=Y(73,2,-2)
assert qmin==F(-182118587,38196630)
assert qmax==F(962852177,38196414)>0

t=sp.symbols('t',nonnegative=True)
def Pc(z):return (z+13)*(z+14)*(54*z**3+2097*z**2+27103*z+116595)/sp.Integer(30)
def Pt(z):return (z+12)*(z+13)*(z+14)*(216*z**3+8532*z**2+112161*z+490715)/sp.Integer(120)
def Ssym(n):return 18*n**4+54*n**3-345*n**2+2070*n-16315
def f(k,e,d):
    n=73+6*k
    return sp.cancel(n**3*(Pt(k)+e)/(Pc(k)+d)-Ssym(n)/sp.Integer(108))
def positive_coefficients(name,expr):
    a,b=sp.fraction(sp.cancel(expr))
    num=list(sp.Poly(a,t).all_coeffs());den=list(sp.Poly(b,t).all_coeffs())
    assert all(v>0 for v in num) and all(v>0 for v in den),name
    return {'numerator_coefficients_desc':[str(v) for v in num],
            'denominator_coefficients_desc':[str(v) for v in den]}

monotone=positive_coefficients('max_read_strict_decrease',f(t,2,-2)-f(t+1,2,-2))
neg_lower=positive_coefficients('negative_min_read',-f(t+1,-2,2))
d129=Y(73+6*129,2,-2)-qmin
d130=Y(73+6*130,2,-2)-qmin
assert d129==F(27717700477367,1508935762911405)>0
assert d130==F(-623634232392236,114862724731769385)<0
assert all(Y(73+6*h,2,-2)>=qmin for h in range(1,130))
assert Y(73+6*130,2,-2)<qmin
out={
 'unit':'R749STS','evidence':'AUTHOR_EXACT_NOT_REVIEWED',
 'frozen_science_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'weights':list(weights),'q':73,'p':'73+6h, h positive integer',
 'legal_parameters':'each independent nuisance pair in real [-2,2]^2',
 'one_read_collision_h':'1 <= h <= 129',
 'one_read_separation_h':'h>=130',
 'qmin':str(qmin),'qmax':str(qmax),
 'boundary_h129_max_minus_qmin':str(d129),
 'boundary_h130_max_minus_qmin':str(d130),
 'certificate_top_strictly_decreasing':monotone,
 'certificate_bottom_strictly_negative':neg_lower,
 'combined_with_R749STR':'h=3..129 has exact minimum initial read count 2; h>=130 has count 1; h=1..2 requires at least 3',
 'next':'Determine exact minimum initial reads for h=1,2 and typed native BRC readout bridge'
}
Path(__file__).with_name('R749STS_ONE_READ_SHARP_THRESHOLD_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: q intervals, two positive-polynomial universal proofs, exact transition h=129/130')
print('gap129=',d129,'gap130=',d130)
