#!/usr/bin/env python3
"""R239: exact rational uniform amplitude and horizon certificate, Python stdlib."""
from fractions import Fraction as F
from math import comb
import json

W=[144,576,1440,4320,17280,86400,518400]
GAMMA0=sum(comb(6,u)*W[u] for u in range(6))
GAMMA1=sum(comb(5,u-1)*W[u] for u in range(1,6))
z3=F(50,1089)
amp_lower=F(19,100)*(1-z3)**2
ETA=amp_lower*F(W[5],GAMMA0)
prefactor=(1-ETA)/ETA
q=F(14771007,14858075)
def fmt(x):return str(x.numerator)+"/"+str(x.denominator)
def bound_at(n):
    return prefactor*q**(n-1)
def main():
    assert GAMMA0==889200 and GAMMA1==655776 and GAMMA0>GAMMA1
    assert F(5,18)*F(1,20)==F(1,72)
    assert F(1,72)/(F(11,20)**2)==z3
    assert amp_lower==F(20510899,118592100)
    assert F(W[5],GAMMA0)==F(24,247)
    assert ETA==F(2159042,128474775)>F(16,1000)
    assert prefactor==F(126315733,2159042)
    assert 0<q<1
    assert q==F(9847338,10000000)/F(594323,600000)
    horizon=[]
    for tol,n in [(F(1,100),1477),(F(1,1000),1869)]:
        assert bound_at(n)<tol<bound_at(n-1)
        horizon.append({"tolerance":fmt(tol),"first_certified_n":n,
            "comparison_at_n":"strictly below tolerance by exact integer cross multiplication",
            "comparison_at_previous":"strictly above tolerance by exact integer cross multiplication"})
    return {"status":"PASS","arithmetic":"exact Python Fraction",
        "scope":"m=12,k=6,L=2; real s in (39/100,41/100) via symbolic proof",
        "stirling_fibre_weights":W,
        "gamma0":GAMMA0,"gamma1":GAMMA1,
        "omitted_source3_stationary_Z_term":fmt(z3),
        "uniform_A_over_W5_lower":fmt(amp_lower),
        "uniform_A_over_T_lower":fmt(ETA),
        "relative_tail_prefactor_upper":fmt(prefactor),
        "relative_tail_ratio_upper":fmt(q),
        "certified_horizons":horizon,
        "independent_review":"NOT_REVIEWED","native_BRC_execution":"NOT_EXECUTED"}
if __name__=="__main__":
    print(json.dumps(main(),ensure_ascii=False,indent=2,sort_keys=True))
