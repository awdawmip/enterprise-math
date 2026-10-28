#!/usr/bin/env python3
"""Independent Newton binomial-definition check of R365 r347->348 ULC tail jump.
Uses signed original K/J recurrence but does not call forward_differences.
"""
from __future__ import annotations
import sys, json, time
from pathlib import Path
from math import comb
from fractions import Fraction
from hashlib import sha256
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P/'research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K,J,C,add,mul,eval_newton

def differences(a):
    return [sum((-1)**(j-i)*comb(j,i)*a[i] for i in range(j+1)) for j in range(len(a))]

def d(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))

def main():
    R=348; lim=2*(R+1)+2
    K0=[None]+[K(i) for i in range(1,13)]
    B=[[1,1]]
    for s in range(1,3*(R+1)+3):
        v=J(s)
        for i in range(1,min(12,s)+1):v=add(v,mul(K0[i],B[s-i],lim),lim)
        B.append(v)
    L={}
    for r in range(346,350):
        ds=differences([Fraction(d(B,r+u,u),5**u) for u in range(r+2)])
        assert ds[-1]==0
        vals=[t*5**r for t in ds[:-1]]
        assert all(q.denominator==1 for q in vals)
        L[r]=eval_newton([int(t) for t in vals],2*R+3)
    records=[]
    for r in (347,348):
        n=2*r
        values=[L[r][i+1]*L[r][i+2]-L[r-1][i+2]*L[r+1][i+1] for i in range(2*r+1)]
        for j in ((636,637) if r==347 else (637,638)):
            coeff=[sum((-1)**(l-i)*comb(l,i)*values[i] for i in range(l+1)) for l in (j-1,j,j+1)]
            T=j*(n-j)*coeff[1]**2-(j+1)*(n-j+1)*coeff[0]*coeff[2]
            s='+' if T>0 else '-' if T<0 else '0'
            td=str(T)
            records.append({'r':r,'j':j,'sign':s,'T_decimal_digits':len(td.lstrip('-')),
                            'T_sha256_decimal_newline':sha256((td+'\n').encode()).hexdigest(),
                            'T_first_42_significant_digits':td[:43],
                            'c_j_sha256_decimal_newline':sha256((str(coeff[1])+'\n').encode()).hexdigest()})
    assert [(x['r'],x['j'],x['sign']) for x in records]==[(347,636,'-'),(347,637,'+'),(348,637,'-'),(348,638,'+')]
    result={'schema':'R365_ULC_347_348_EDGE_CROSSCHECK','method':'direct binomial sum of Q(v) to compute exact differences','records':records,'source':'R346 signed K/J, regenerated independently'}
    (P/'R365_TRANSITION_EVIDENCE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
