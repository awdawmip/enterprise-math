#!/usr/bin/env python3
"""Exact source-to-binomial crosswalk tests; author-side, not native H0/B0."""
from math import comb
import json

def exact_binomial(p):
    mod=p**3
    inv216=pow(216,-1,mod)
    power=1
    tot=0
    for n in range(p):
        tot=(tot+(6*n+1)*comb(2*n,n)**2*comb(3*n,n)*power)%mod
        power=power*inv216%mod
    return tot

def exact_rising(p):
    mod=p**3
    term=1
    tot=0
    for n in range(p):
        tot=(tot+(6*n+1)*term)%mod
        if n<p-1:
            numerator=(2*n+1)*(3*n+1)*(3*n+2)
            den=36*(n+1)**3
            term=term*numerator*pow(den,-1,mod)%mod
    return tot

if __name__=='__main__':
    data=[]
    for p in (13,19,37,43,157,163,373):
        a,b=exact_binomial(p),exact_rising(p)
        assert a==b, (p,a,b)
        data.append({'p':p,'p_mod_24':p%24,'modulus_p3':p**3,'binomial_W':a,'hypergeometric_F6':b,'signed_residual_mod_p3':(a-p)%(p**3),'passed_two_path':True})
    print(json.dumps({'scope':'AUTHOR_SIDE_SOURCE_6_8_IDENTITY_REGRESSION_NOT_NATIVE','values':data},indent=2))
