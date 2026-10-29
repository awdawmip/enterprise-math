#!/usr/bin/env python3
"""Reproduce R359 signed-BRC Q339 certificate from the immutable R346 kernel."""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
from math import comb
import sys
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE.parent/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K,J,C,add,mul,forward_differences,eval_newton

def D(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))

def main():
    R=339; max_s=3*(R+1)+2; t_limit=2*(R+1)+2
    kernels=[None]+[K(i) for i in range(1,13)]
    B=[[1,1]]
    for s in range(1,max_s+1):
        z=J(s)
        for i in range(1,min(s,12)+1):
            z=add(z,mul(kernels[i],B[s-i],t_limit),t_limit)
        B.append(z)
    L={}
    for r in range(R-2,R+2):
        h=forward_differences([Fraction(D(B,r+u,u),5**u) for u in range(r+2)])
        assert h[-1]==0 and h[-2]==6**r
        scaled=[5**r*x for x in h[:-1]]
        assert all(x.denominator==1 for x in scaled)
        L[r]=eval_newton([int(x) for x in scaled],2*R+3)
    for r in (R-1,R):
        values=[L[r][v+1]*L[r][v+2]-L[r-1][v+2]*L[r+1][v+1] for v in range(2*r+1)]
        c=forward_differences(values)
        assert len(c)==2*r+1 and all(isinstance(x,int) and x>0 for x in c)
        assert c[-1]==30**(2*r)*comb(2*r,r)//(r+1)
        assert all(c[j]**2>c[j-1]*c[j+1] for j in range(1,2*r))
        raw=''.join(f'{r},{j},{x}\n' for j,x in enumerate(c))
        digest=sha256(raw.encode()).hexdigest()
        if r==338:
            assert digest=='a1bfe1e15b52143446f3e9b098278a992815f0e89a80ae14c6b474588723967d'
        else:
            assert Fraction(c[-2],c[-1])==Fraction(17*r+11,10)
            assert Fraction(c[-3],c[-1])==Fraction(7803*r**3+2252*r**2-5523*r+3328,2700*(2*r-1))
            for k in range(1,9):
                q=r+k
                minor=D(B,q,k)*D(B,q+1,k+1)-D(B,q,k+1)*D(B,q+1,k)
                assert Fraction(minor)==Fraction(values[k-1]*5**(2*k+1),5**(2*r)) and minor>0
            assert digest=='1463acfa336c2e8bf11b09dba027fb2fe8f45edd0a733d0fddcee1b92d001e2d'
        bad=[j for j in range(1,2*r) if c[j]**2*comb(2*r,j-1)*comb(2*r,j+1)<c[j-1]*c[j+1]*comb(2*r,j)**2]
        print(f'r={r} coefficients={len(c)} sha256={digest} strict_turan={2*r-1} ULC_fail={len(bad)} peak={max(range(len(c)),key=c.__getitem__)}')
if __name__=='__main__': main()
