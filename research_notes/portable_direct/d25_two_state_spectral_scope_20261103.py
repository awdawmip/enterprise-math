#!/usr/bin/env python3
"""Exact p^4 original-216 two-state transfer and spectral counter-control."""
import json
from math import comb

PRIMES = (5, 7, 13, 19, 37, 43, 109, 181, 373)

def check(p):
    modulus = p**4
    coeff, s = 1, 0
    for k in range(p-1):
        s = (s + (6*k+1)*coeff) % modulus
        numerator = (2*k+1)*(3*k+1)*(3*k+2)
        denominator = 36*(k+1)**3
        assert denominator % p
        coeff = coeff*numerator*pow(denominator,-1,modulus)%modulus
    b=coeff
    direct=(comb(2*p-2,p-1)**2*comb(3*p-3,p-1)*pow(216,-(p-1),modulus))%modulus
    assert b==direct==(-p**3)%modulus
    endpoint=((6*p-5)*b)%modulus
    assert endpoint==(5*p**3)%modulus
    w_full=(s+endpoint)%modulus
    # Matrix [[1,s],[0,b]] has T^2=T mod p^3.
    assert b%p**3==0
    assert (s*b)%p**3==0
    kernel_x=-s%p**3
    assert (s+kernel_x)%p**3==0
    assert -kernel_x%p**3==w_full%p**3
    # Both lambda=1 and lambda=0 controls have spectrum {1,b}.
    assert (1+b)%p**3==1
    return {
        "p":p,"b_terminal_mod_p4":b,"endpoint_mod_p4":endpoint,
        "W_original_mod_p3":w_full%p**3,
        "kernel_chart_x_mod_p3":kernel_x,
        "W_zero_weight_control_mod_p3":0,
        "transfer_characteristic_polynomial_mod_p3":"X*(X-1)"
    }

if __name__=="__main__":
    results=[check(p) for p in PRIMES]
    assert all(r["W_original_mod_p3"]==r["p"] for r in results
               if r["p"]%24 in (13,19))
    assert next(r for r in results if r["p"]==13)["W_original_mod_p3"]==13
    print(json.dumps({"schema":"D25_TWO_STATE_SPECTRAL_EXACT_V1",
                      "status":"FINITE_EXACT_CHECK_NOT_ALL_PRIME_W_PROOF",
                      "cases":results},indent=2))
