#!/usr/bin/env python3
"""Exact R236 derivative identity and all-real Lipschitz bound for R234 source Perron root."""
from fractions import Fraction as F
import json
from R235_unique_slowest_source_mode_check import family, f

L,R=F(39,100),F(41,100)
XLO,XHI=F(99,100),F(991,1000)
C=F(5,18)

def tprime(s):
    return F(853776)/(2615*s-3539)**2

def Q(s,x):
    return 2615*s*x-767*s-4463*x+2615

def secular_s_derivative(s,x):
    a,pi,b=family(s)
    return C*(x-F(1,2))*(tprime(s)/(x-a[6])**2 - 1/(x-s)**2)

def factored_derivative(s,x):
    z=2615*s*x-1691*s-3539*x+2615
    return -C*(x-F(1,2))*2615*(s-1)*(x-1)*Q(s,x)/((x-s)**2*z**2)

def certify():
    assert tprime(R)<F(141,1000)
    assert F(97,125)<family(L)[0][6]<family(R)[0][6]<F(39,50)
    assert Q(R,XLO)==-F(2112823,2000) < 0
    assert Q(L,XHI)==-F(21925833,20000) > -1100
    assert 2615*XLO-767>0 and 2615*R-4463<0
    bound_diff=2615*F(61,100)*F(1,100)*1100 / (
      (F(58,100))**2 * ((3539-2615*R)*(XLO-F(39,50)))**2)
    fs_upper=C*(XHI-F(1,2))*bound_diff
    minus_fx_lower=C*(F(97,125)-F(1,2))/(XHI-F(97,125))**2
    certified_L=fs_upper/minus_fx_lower
    assert 0<certified_L<F(1,60)
    center=F(2,5)
    lo0,hi0=F(990705,1000000),F(990706,1000000)
    aa,pp,bb=family(center)
    assert f(3,lo0,aa,bb)>0 and f(3,hi0,aa,bb)<0
    uniform_lo=lo0-F(1,6000)
    uniform_hi=hi0+F(1,6000)
    assert uniform_lo==F(594323,600000)
    assert uniform_hi==F(1486309,1500000)
    for s in (L,center,R):
      for x in (XLO,F(990705,1000000),XHI):
        assert secular_s_derivative(s,x)==factored_derivative(s,x)
        assert secular_s_derivative(s,x)>0
    return {
     'status':'PASS','model':'R234 seven-source stationary sticky-reset observer',
     'parameter_interval_open':['39/100','41/100'],
     'monotonicity':'r prime(s) > 0 for all real s in I',
     'certified_global_lipschitz_strict':'1/60',
     'computed_conservative_bound':str(certified_L),
     'base_root_strict_interval':['990705/1000000','990706/1000000'],
     'uniform_refined_root_strict_interval':[str(uniform_lo),str(uniform_hi)],
     'derivative_factorization_samples':9,
     'exact_arithmetic':'fractions.Fraction',
     'proof_scope':'all real s in I from algebraic identity and endpoint rational inequalities; samples only check the identity',
     'review':'NOT_REVIEWED','native_brc_integration':'NOT_EXECUTED'
    }

if __name__=='__main__':
    print(json.dumps(certify(),ensure_ascii=False,indent=2))
