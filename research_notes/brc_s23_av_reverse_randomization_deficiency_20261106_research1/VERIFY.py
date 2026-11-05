"""Exact rational author-side certificate for the S23 AV binary reverse-kernel deficiency.

Arithmetic uses fractions.Fraction throughout. The analytic proof in PROOF.md supplies
universal quantifiers; these tests are deliberately a finite algebraic audit.
"""
from fractions import Fraction as F

Z, O = F(0), F(1)
checks = cases = priors = 0

def check(ok, message):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(message)

def total_variation(p, v):
    return sum((abs(x-y) for x,y in zip(p,v)), Z)/2

def risk(p0,p1,t):
    return sum((min((O-t)*x,t*y) for x,y in zip(p0,p1)), Z)

As = [F(1,2),F(5,8),F(3,4),F(7,8)]
Xs = [F(1,2),F(5,8),F(3,4)]
Ys = [F(5,8),F(3,4),F(7,8)]

for a in As:
    q = O-a
    for x in Xs:
        for y in Ys:
            if x >= y:
                continue
            cases += 1
            r,s = q*x,q*y
            epsilon = a*(s-r)/(2-r-s)
            u = 2*a/(2-r-s)
            check(Z < u <= O, 'kernel stochastic domain')
            check(Z < epsilon <= F(1,14), 'claimed sharp global bound')
            p0=(a,r,q-r)
            p1=(a,s,q-s)
            b0=(r,O-r)
            b1=(s,O-s)
            # K(yes)=(0,1,0), K(no)=(u,0,1-u).
            d0=((O-r)*u,r,(O-r)*(O-u))
            d1=((O-s)*u,s,(O-s)*(O-u))
            check(sum(p0)==sum(p1)==sum(b0)==sum(b1)==O,'normalized source distributions')
            check(sum(d0)==sum(d1)==O,'normalized reconstructions')
            check(total_variation(p0,d0)==epsilon,'TV minus exact')
            check(total_variation(p1,d1)==epsilon,'TV plus exact')
            check(d0[0]-a==epsilon and d1[0]-a==-epsilon,'symmetric common-mass residual')
            knot = (O-r)/(2-r-s)
            h=(O-x)/(2-x-y)
            check(F(1,2)<knot<h<O,'prior knot ordering')
            check(risk(b0,b1,knot)-risk(p0,p1,knot)==epsilon,'matching Bayes risk dual bound')
            check(risk(b0,b1,F(1,2))==risk(p0,p1,F(1,2)),'equal-prior loss zero')
            for t in [Z,F(1,3),F(1,2),knot,(knot+h)/2,h,O]:
                delta=risk(b0,b1,t)-risk(p0,p1,t)
                check(Z <= delta <= epsilon,'bounded prior loss')
                priors += 1

# Sharp witness, including unique optimal-prior and simple 2-row recovery kernel.
a,x,y=F(1,2),F(1,2),F(7,8)
q=O-a;r=q*x;s=q*y
check((O-r)/(2-r-s)==F(4,7),'sharp prior 4/7')
check(2*a/(2-r-s)==F(16,21),'sharp kernel u 16/21')
check(a*(s-r)/(2-r-s)==F(1,14),'sharp deficiency 1/14')
print(f'PASS_S23_AV_REVERSE_DEFICIENCY_EXACT_20261106; cases={cases}; priors={priors}; exact_checks={checks}; sharp=1/14; kernel_no_common=16/21')
