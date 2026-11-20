"""Exact algebra checks accompanying ENDPOINT_LIMIT.md; no Monte Carlo."""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as s

ell,u,v=s.symbols('ell u v',real=True)
checks={}
checks['two_phase_density']=s.integrate(2*ell,(ell,0,1))==1
# Four signed quadrants; same-sign region doubled across its diagonal.
same=2*s.integrate((1-u)*s.integrate((1-v)*(u-v),(v,0,u)),(u,0,1))
opposite=s.integrate((1-u)*s.integrate((1-v)*(u+v),(v,0,1)),(u,0,1))
checks['triangular_absolute_difference']=s.simplify(2*same+2*opposite)==s.Rational(7,15)
gamma=Q(1,20)
checks['holder_coefficient']=4*gamma/(1-gamma**2)==Q(80,399)
checks['holder_exponent']=(gamma+1)/2==Q(21,40)
ratios={}
for k in range(2,9):
    density=k*(k-1)*ell*(1-ell)**(k-2)
    checks[f'density_k{k}']=s.integrate(density,(ell,0,1))==1
    # Integrate a finite polynomial termwise with rational exponent 1/20.
    poly=s.Poly(s.expand(density),ell)
    integral=sum(Q(int(coef),1)/(Q(power[0])+gamma+1) for power,coef in poly.terms())
    product=Q(1)
    for j in range(2,k+1):product*=Q(20*j,20*j+1)
    checks[f'beta_product_k{k}']=integral==product
    ratios[str(k)]=str(product)
# Exact grid checks for the interval symmetric-difference lemma.
qs=[Q(i,12) for i in range(-12,13)]
for q in qs:
    for qp in qs:
        lo=max(Q(0),-q);hi=min(Q(1),1-q)
        lop=max(Q(0),-qp);hip=min(Q(1),1-qp)
        sd=hi-lo+hip-lop-2*max(Q(0),min(hi,hip)-max(lo,lop))
        assert sd<=abs(q-qp)
checks['interval_difference_625_rational_pairs']=True
result={'status':'passed' if all(checks.values()) else 'failed',
        'checks':checks,'exact_mellin_ratios':ratios,
        'scope':'Exact coefficient checks; general event/limit proof is ENDPOINT_LIMIT.md.'}
Path(__file__).with_name('endpoint_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
assert all(checks.values())
