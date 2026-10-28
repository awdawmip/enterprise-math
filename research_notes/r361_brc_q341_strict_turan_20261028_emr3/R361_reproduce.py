#!/usr/bin/env python3
"""Independent R361 replay of signed-BRC Q341 coefficient certificate using R346 K/J."""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
from math import comb
import sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent if HERE.parent.name=="research_notes" else HERE
sys.path.insert(0,str(ROOT/'research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K,J,C,add,mul,forward_differences,eval_newton

def D(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))

def main():
    rmax=341; smax=3*(rmax+1)+2; lim=2*(rmax+1)+2
    kk=[None]+[K(i) for i in range(1,13)]
    B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(s,12)+1):
            z=add(z,mul(kk[i],B[s-i],lim),lim)
        B.append(z)
    L={}
    for r in range(339,343):
        d=forward_differences([Fraction(D(B,r+u,u),5**u) for u in range(r+2)])
        assert d[-1]==0 and d[-2]==6**r
        integers=[5**r*x for x in d[:-1]]
        assert all(x.denominator==1 for x in integers)
        L[r]=eval_newton([int(x) for x in integers],2*rmax+3)
    expected={340:'6b4bd495ab7910a1d95e5c28e2c542da082cd1aa7130566172f8a1e4079698d1',
              341:'8d266933eaa17e62317fe4709a85be633f4a09726d90757ef05facd9e672d346'}
    for r in (340,341):
        val=[L[r][v+1]*L[r][v+2]-L[r-1][v+2]*L[r+1][v+1] for v in range(2*r+1)]
        d=forward_differences(val)
        assert len(d)==2*r+1 and all(x>0 for x in d)
        assert d[-1]==30**(2*r)*comb(2*r,r)//(r+1)
        assert Fraction(d[-2],d[-1])==Fraction(17*r+11,10)
        assert Fraction(d[-3],d[-1])==Fraction(7803*r**3+2252*r**2-5523*r+3328,2700*(2*r-1))
        assert all(d[j]**2>d[j-1]*d[j+1] for j in range(1,2*r))
        raw=''.join(f'{r},{j},{x}\n' for j,x in enumerate(d))
        digest=sha256(raw.encode()).hexdigest()
        assert digest==expected[r],(r,digest)
        bad=[j for j in range(1,2*r) if d[j]**2*comb(2*r,j-1)*comb(2*r,j+1)<d[j-1]*d[j+1]*comb(2*r,j)**2]
        if r==341:
            assert len(bad)==624 and bad[0]==1
            for k in range(1,9):
                q=r+k
                minor=D(B,q,k)*D(B,q+1,k+1)-D(B,q,k+1)*D(B,q+1,k)
                assert Fraction(minor)==Fraction(val[k-1]*5**(2*k+1),5**(2*r)) and minor>0
        print(f'r={r} n={len(d)} sha256={digest} turan={2*r-1} ulc_fail={len(bad)} peak={max(range(len(d)),key=d.__getitem__)}')
if __name__=='__main__':main()
