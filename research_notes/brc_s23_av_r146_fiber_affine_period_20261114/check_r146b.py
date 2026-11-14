#!/usr/bin/env python3
"""R146B exact two-rotation single-step law; run beside check_r146.py."""
from fractions import Fraction as Q
from itertools import product
from math import floor, ceil, lcm
import json
from check_r146 import support, fiber_count

def indicators(A,B,alpha,beta):
    fracA = A-floor(A)
    fracB = B-floor(B)
    jA = int(alpha>0 and fracA>=1-alpha)
    jB = int(beta>0 and (fracB==0 or fracB>1-beta))
    return jB,jA

def main():
    tested=0
    transitions=0
    orbit_sums=0
    absences=0
    recovered=0
    events=[0,0,0]
    for m in range(1,12):
        for w in product((0,1),repeat=m):
            d=support(w)
            if d is None:
                continue
            alpha,beta,u,ell=d
            P=lcm(alpha.denominator,beta.denominator)
            for L in (1,2,3,10,31,100,10**70+321):
                C=fiber_count(d,L)
                Cn=fiber_count(d,L+1)
                A=L*alpha-u
                B=L*beta-ell
                jB,jA=indicators(A,B,alpha,beta)
                assert Cn-C==jB-jA
                assert -1<=Cn-C<=1
                if C>=2: assert Cn>0
                if C>=1 and Cn==0:
                    assert C==1 and (jB,jA)==(0,1)
                    absences+=1
                if C==0 and Cn>=1:
                    assert Cn==1 and (jB,jA)==(1,0)
                    recovered+=1
                events[Cn-C+1]+=1
                transitions+=1
            L=1
            a_sum=b_sum=0
            for i in range(P):
                B=(L+i)*beta-ell
                A=(L+i)*alpha-u
                jB,jA=indicators(A,B,alpha,beta)
                a_sum+=jA
                b_sum+=jB
            assert a_sum==P*alpha and b_sum==P*beta
            assert b_sum-a_sum==P*(beta-alpha)
            orbit_sums+=1
            tested+=1
    result={"word_records":tested,"single_steps":transitions,"orbit_checks":orbit_sums,"local_disappearances_observed":absences,"local_recoveries_observed":recovered,"delta_counts_neg_zero_pos":events,"signature":"R146B_TWO_ROTATION_STEP_PASS"}
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
