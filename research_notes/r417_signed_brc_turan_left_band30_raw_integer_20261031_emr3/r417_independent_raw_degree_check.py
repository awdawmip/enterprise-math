#!/usr/bin/env python3
"""Independent raw-integer cross-check of R417 A/B certificate, standard library only."""
import json
from math import comb
from pathlib import Path
S=30

def cat(n):return comb(2*n,n)//(n+1)
def delta_raw(r,s):
    ans=0
    for j in range(2*s+1):
        for bit in (0,1):
            n=r-j-bit
            if n>=0 and n%2==0 and n//2<=r-s:
                ans+=(-1)**bit*comb(2*s,j)*comb(r-s,n//2)
    return ans

def delta_kernel(r,s):
    return sum(comb(s-1,j)*2**(s-1-j)*cat((r-s+j)//2)
               for j in range(s) if r-s+j>=0 and (r-s+j)%2==0)
def horner(c,x):
    v=0
    for a in reversed(c):v=v*x+int(a)
    return v

def main():
    data=json.loads((Path(__file__).parent/'R417_RAW_EVIDENCE.json').read_text())
    assert data['schema']=='EM_R417_RAW_INTEGER_CERTIFICATE_V1'
    count=kernel=0
    for obj in data['results']:
        eps=int(obj['epsilon']);m0=(16 if eps==0 else 15);d=(14 if eps==0 else 15)
        assert int(obj['r0'])==2*m0+eps
        A=obj['A_coefficients_ascending'];B=obj['B_coefficients_ascending']
        assert len(A)==len(B)==2*d+3 and all(int(v)>0 for v in A+B)
        # A/B computed from degree <=d polynomial Catalan-ratio numerators;
        # the test is an independent check of the algebraic construction.
        for x in range(2*d+3):
            r=2*(m0+x)+eps; C=cat(m0+x-1+eps)
            vals=[]
            for s in (29,30,31):
                raw=delta_raw(r,s)
                assert raw==delta_kernel(r,s)
                kernel+=1
                vals.append(comb(r+s,2*s)*raw)
            D=vals[1]**2-vals[0]*vals[2]
            assert horner(B,x)*D==horner(A,x)*(comb(r+30,60)*C)**2 and D>0
            count+=1
        print('R417_RAW_INDEPENDENT_PARITY_PASS',eps,2*d+3,'points')
    print('R417_RAW_INDEPENDENT_PASS',count,'Turan',kernel,'Catalan')
if __name__=='__main__':main()
