#!/usr/bin/env python3
"""
Local rerun checks for RS-RHR-CLAUDE-RH-RERUN-20260811.
Numerics are EVIDENCE_ONLY; the analytic arguments live in CLASSICAL_RERUN.md.
"""
from fractions import Fraction
import math

def rvm_leading(T):
    return T/(2*math.pi)*math.log(T/(2*math.pi)) - T/(2*math.pi) + 7/8

def lemma10_polynomial_stress():
    # g(z)=(1-z/2)(1-z/3)=1-5z/6+z^2/6.
    coeff = [Fraction(1), Fraction(-5, 6), Fraction(1, 6)]
    # For m>=3 all Taylor coefficients are exactly zero.
    # If 0 = R1*(1/2)^m + R2*(1/3)^m for m=3,4,
    # the 2x2 determinant is nonzero, forcing R1=R2=0.
    det = Fraction(1,2)**3 * Fraction(1,3)**4 - Fraction(1,3)**3 * Fraction(1,2)**4
    return coeff, det

def count_table():
    rows=[]
    for L in (1e4,1e8,1e12,1e16):
        base=L**0.25
        target=rvm_leading(math.sqrt(L))
        rows.append((L,base,target,target/base))
    return rows

if __name__=="__main__":
    coeff, det = lemma10_polynomial_stress()
    print("Lemma-10 polynomial stress")
    print("coefficients:", coeff)
    print("m=3,4 exponential-system determinant:", det, "(nonzero)")
    print()
    print("Candidate-A count scale")
    for L,base,target,ratio in count_table():
        print(f"Lambda={L:.0e} Lambda^1/4={base:.6g} RvM(sqrtLambda)={target:.6g} ratio={ratio:.6g}")
    print()
    print("Analytic reminder:")
    print("entire g=sum gamma_m z^m => limsup |gamma_m|^(1/m)=0.")
    print("A nonzero fixed-base exponential leading term rho^m with rho>0 contradicts this.")
