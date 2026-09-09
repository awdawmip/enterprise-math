#!/usr/bin/env python3
"""Exact/numerical verifier for EM-FREE-F6D046 Ramanujan period-Wronskian note."""
from decimal import Decimal, getcontext
from fractions import Fraction
import json

getcontext().prec = 90
D=Decimal

def sqrt(x: Decimal)->Decimal:
    return x.sqrt()

def gauss_legendre_pi(iterations: int=8)->Decimal:
    a=D(1); b=D(1)/sqrt(D(2)); t=D(1)/D(4); p=D(1)
    for _ in range(iterations):
        an=(a+b)/2
        b=sqrt(a*b)
        t=t-p*(a-an)*(a-an)
        a=an; p*=2
    return (a+b)*(a+b)/(4*t)

def ramanujan_inverse_pi(terms: int=8)->Decimal:
    z=D(1)/(D(99)**4)
    c=D(1); zp=D(1); s=D(0)
    for n in range(terms):
        s += c * (D(1103)+D(26390)*n) * zp
        k=D(n)
        c *= ((k+D(1)/4)*(k+D(1)/2)*(k+D(3)/4))/((k+1)**3)
        zp *= z
    return D(2)*sqrt(D(2))/D(9801)*s

def hyper_f_and_derivative(a: Decimal,x:Decimal,terms:int=300):
    term=D(1); f=term; fp=D(0)
    for n in range(1,terms):
        k=D(n-1)
        term *= ((a+k)*(D(1)-a+k)/(D(n)*D(n)))*x
        f += term
        fp += D(n)*term/x
        if abs(term) < D('1e-85'):
            break
    return f,fp

checks={}
checks['pell']=(9801**2-29*1820**2==1)
checks['mu_prime_integer']=(8824*9801==8*1103*99**2)
checks['A_fraction']=(Fraction(8824*9801,4*99**4)==Fraction(2206,9801))
checks['B_fraction']=(Fraction(29*1820,9801)==Fraction(52780,9801))
root29=sqrt(D(29))
alpha=D(1)/2-D(910)*root29/D(9801)
z=4*alpha*(1-alpha)
checks['z0_decimal']=abs(z-D(1)/(D(99)**4)) < D('1e-85')
B=root29*(1-2*alpha)
checks['B_decimal']=abs(B-D(52780)/D(9801)) < D('1e-84')
muprime=D(8824)*D(9801)
A=alpha*(1-alpha)*muprime
checks['A_decimal']=abs(A-D(2206)/D(9801)) < D('1e-80')
pi=gauss_legendre_pi()
invpi=ramanujan_inverse_pi(12)
checks['ramanujan_series']=abs(invpi-D(1)/pi) < D('1e-80')
a=D(1)/4; x=D(1)/2
f,fp=hyper_f_and_derivative(a,x)
J=D(1)/2*f*fp
target=sqrt(D(2))/(D(2)*pi)
checks['wronskian_midpoint']=abs(J-target) < D('1e-78')
result={
  'researcher_id':'EM-FREE-F6D046',
  'candidate_id':'EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN',
  'all_passed':all(checks.values()),
  'checks':checks,
  'values':{
    'alpha0':str(alpha),'z0':str(z),'A0':str(A),'B0':str(B),
    'inverse_pi_series':str(invpi),'inverse_pi_reference':str(D(1)/pi),
    'wronskian_J':str(J),'wronskian_target':str(target)
  }
}
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(0 if result['all_passed'] else 1)
