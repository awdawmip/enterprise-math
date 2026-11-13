#!/usr/bin/env python3
"""Reproduce R363 signed 12-term BRC Q343 and Q342 digest anchor; exact arithmetic."""
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json,sys,time
P=Path(__file__).resolve().parent
ROOT=P.parent.parent
sys.path.insert(0,str(ROOT/'research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K,J,C,add,mul,forward_differences as fd,eval_newton
def D(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))
def main():
    R=343;smax=3*(R+1)+2;lim=2*(R+1)+2
    kk=[None]+[K(i) for i in range(1,13)];B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(12,s)+1):z=add(z,mul(kk[i],B[s-i],lim),lim)
        B.append(z)
    L={}
    for r in range(R-2,R+2):
        ds=fd([Fraction(D(B,r+u,u),5**u) for u in range(r+2)])
        assert ds[-1]==0 and ds[-2]==6**r
        z=[t*5**r for t in ds[:-1]]
        assert all(t.denominator==1 for t in z)
        L[r]=eval_newton([int(t) for t in z],2*R+3)
    for r in (342,343):
        val=[L[r][v+1]*L[r][v+2]-L[r-1][v+2]*L[r+1][v+1] for v in range(2*r+1)]
        c=fd(val)
        assert all(x>0 for x in c)
        assert c[-1]==30**(2*r)*comb(2*r,r)//(r+1)
        assert Fraction(c[-2],c[-1])==Fraction(17*r+11,10)
        assert Fraction(c[-3],c[-1])==Fraction(7803*r**3+2252*r**2-5523*r+3328,2700*(2*r-1))
        assert all(c[j]**2>c[j-1]*c[j+1] for j in range(1,2*r))
        raw=''.join(f'{r},{j},{x}\n' for j,x in enumerate(c)).encode()
        digest=sha256(raw).hexdigest()
        if r==342:
            assert digest=='aa4b0e6390085106420e442b79dd81ffca80f6f9e1106fb14de474e13acc2f74'
        else:
            assert digest=='019e7f8866384a1e5beed7ed05f69a77c784333932057106c3dd4a20dca90899'
            (P/'R363_Q343_FULL_COEFFICIENTS.txt').write_bytes(raw)
            for k in range(1,9):
                q=r+k
                minor=D(B,q,k)*D(B,q+1,k+1)-D(B,q,k+1)*D(B,q+1,k)
                assert Fraction(minor)==Fraction(val[k-1]*5**(2*k+1),5**(2*r)) and minor>0
        ulc=[c[j]**2*j*(2*r-j)-c[j-1]*c[j+1]*(j+1)*(2*r-j+1) for j in range(1,2*r)]
        print(r,len(c),digest,'Turan',2*r-1,'ULC negative',sum(x<0 for x in ulc),'positive',sum(x>0 for x in ulc),'peak',max(range(len(c)),key=c.__getitem__))
if __name__=='__main__':main()
