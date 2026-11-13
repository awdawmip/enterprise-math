#!/usr/bin/env python3
"""Exact theorem instance and support-boundary counterexample."""
from math import comb
def C(n,k):return comb(n,k) if 0<=k<=n else 0
def good(q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*C(q+w,q)*2**w*3**q for w in range(k+1))
def bad(q,k):
    def coeff(s,q):
        return C(s-2*q,q)*2**(s-3*q) if s>=3*q else 0
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*coeff(q+w,q) for w in range(k+1))
def main():
    for r in range(7):
        for u in range(12):
            assert good(r+u,u)==6**(r+u)*C(r+u,r)
    assert bad(0,0)==1 and bad(1,1)==0
    print('84 exact pairs pass; support violation counterexample D00=1, D11=0 !=1/2')
if __name__=='__main__':main()
