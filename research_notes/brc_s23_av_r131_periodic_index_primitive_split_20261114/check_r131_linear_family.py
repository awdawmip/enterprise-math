#!/usr/bin/env python3
"""R131.4 exact variable-length one-hot / one-zero certificates."""
from fractions import Fraction as F
from check_r131 import word

def witness_map(m,K):
    assert m >= 3 and K >= m
    phases = {'0'*m: F(1,2*K), '1'*m: F(1)-F(1,K+m-1)}
    for r in range(m):
        phases['0'*r+'1'+'0'*(m-r-1)] = F(1,K+r)
    for z in range(1,m):
        phases['1'*z+'0'+'1'*(m-z-1)] = F(1)-F(1,K+z-1)
    phases['0'+'1'*(m-1)] = F(1)-F(2,2*K-1)
    assert len(phases) == 2*m+2
    return phases

def main():
    cases=0
    for m in range(3,35):
        for K in (m,m+1,2*m,10*m,10**80+m):
            for expected, t in witness_map(m,K).items():
                assert F(0) < t < F(1)
                found=''.join(map(str,word(F(0),K,1,1,m,t)))
                assert found==expected,(m,K,expected,found,t)
                cases+=1
    print('R131_LINEAR_CERTIFICATE_FAMILY_PASS cases='+str(cases))
if __name__=='__main__': main()
