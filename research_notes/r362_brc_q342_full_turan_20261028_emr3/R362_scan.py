#!/usr/bin/env python3
"""Exact finite signed-BRC Newton/Turan scan, r=1..342; requires R346_verify.py."""
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json,sys
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P/'research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import C,K,J,add,mul,forward_differences as diff,eval_newton
N=342

def D(b,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*b[q+w][q] for w in range(k+1))

def main():
    kk=[None]+[K(i) for i in range(1,13)]
    b=[[1,1]]
    for s in range(1,3*(N+1)+3):
        t=J(s)
        for i in range(1,min(12,s)+1):t=add(t,mul(kk[i],b[s-i],2*(N+1)+2),2*(N+1)+2)
        b.append(t)
    L=[]
    for r in range(N+2):
        d=diff([Fraction(D(b,r+u,u),5**u) for u in range(r+2)])
        assert d[-1]==0 and d[-2]==6**r,(r,'H samples')
        z=[x*5**r for x in d[:-1]]
        assert all(x.denominator==1 for x in z)
        L.append(eval_newton([int(x) for x in z],2*N+3))
    h=sha256();gap=sha256();c_total=0;t_total=0; q342=None
    for r in range(1,N+1):
        v=[L[r][i+1]*L[r][i+2]-L[r-1][i+2]*L[r+1][i+1] for i in range(2*r+1)]
        c=diff(v)
        assert len(c)==2*r+1 and all(x>0 for x in c),(r,'Newton')
        assert c[-1]==30**(2*r)*comb(2*r,r)//(r+1),(r,'Catalan')
        assert Fraction(c[-2],c[-1])==Fraction(17*r+11,10)
        assert Fraction(c[-3],c[-1])==Fraction(7803*r**3+2252*r**2-5523*r+3328,2700*(2*r-1))
        assert all(c[j]**2>c[j-1]*c[j+1] for j in range(1,2*r)),(r,'Turan')
        raw=''.join(f'{r},{j},{x}\n' for j,x in enumerate(c)).encode()
        h.update(raw)
        if 49<=r<=336:gap.update(raw)
        c_total+=len(c);t_total+=2*r-1
        if r==342:
            bad=[j for j in range(1,2*r) if c[j]**2*comb(2*r,j-1)*comb(2*r,j+1)<c[j-1]*c[j+1]*comb(2*r,j)**2]
            q342={'coefficient_sha256':sha256(raw).hexdigest(),'positive_coefficients':len(c),
                  'strict_turan':2*r-1,'ULC_failures':len(bad),'ULC_first_failure':bad[0],
                  'peak_index':max(range(len(c)),key=c.__getitem__)}
        if r==341:assert sha256(raw).hexdigest()=='8d266933eaa17e62317fe4709a85be633f4a09726d90757ef05facd9e672d346'
    assert (c_total,t_total)==(N*(N+2),N**2)
    out={'r_range':[1,N],'newton_positive':c_total,'turan_strict_positive':t_total,
         'previous_gap_r_range':[49,336],'gap_new_turan_checks':336**2-48**2,
         'all_coefficient_sha256':h.hexdigest(),'gap_coefficient_sha256':gap.hexdigest(),'q342':q342,
         'model':'original signed twelve-term BRC K/J; original R346 source',
         'arithmetic':'Python exact integer + Fraction; finite-r only'}
    (P/'R362_scan_evidence.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False))
if __name__=='__main__':main()
