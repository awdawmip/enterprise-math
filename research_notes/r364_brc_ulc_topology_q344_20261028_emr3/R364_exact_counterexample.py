#!/usr/bin/env python3
"""Independent direct exact small-index counterexample to uniform ULC single-change."""
from __future__ import annotations
import json,sys
from fractions import Fraction
from pathlib import Path
P=Path(__file__).resolve().parent
SRC=P/'research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3'
if not (SRC/'R346_verify.py').exists():
    SRC=P.parent/'r346_unbounded_interior_tp2_corank301_20261028_emr3'
sys.path.insert(0,str(SRC))
from R346_verify import K,J,C,add,mul,forward_differences as fd,eval_newton

def D(b,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*b[q+w][q] for w in range(k+1))

def main():
    r=5; lim=2*(r+1)+2; ks=[None]+[K(i) for i in range(1,13)]
    b=[[1,1]]
    for s in range(1,3*(r+1)+3):
        z=J(s)
        for i in range(1,min(12,s)+1):z=add(z,mul(ks[i],b[s-i],lim),lim)
        b.append(z)
    L={}
    for h in (4,5,6):
        ds=fd([Fraction(D(b,h+u,u),5**u) for u in range(h+2)])
        assert ds[-1]==0 and ds[-2]==6**h
        L[h]=eval_newton([int(x*5**h) for x in ds[:-1]],2*r+3)
    c=fd([L[r][v+1]*L[r][v+2]-L[r-1][v+2]*L[r+1][v+1] for v in range(2*r+1)])
    U={j:j*(2*r-j)*c[j]**2-(j+1)*(2*r-j+1)*c[j-1]*c[j+1] for j in range(1,2*r)}
    result={'r':r,'Q5_Newton':[str(x) for x in c], 'normalization_degree':10,
      'ulc_integer_cross_multiplication_differences':{str(k):str(v) for k,v in U.items()},
      'sign_runs':[[1,1,2],[-1,3,7],[1,8,9]],
      'witness_three_consecutive_sign_indices':[2,3,8],
      'witness_signs':[1,-1,1], 'arithmetic':'exact Python integers and Fraction; original signed 12 K/J'}
    (P/'R364_COUNTEREXAMPLE.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
