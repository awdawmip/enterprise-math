#!/usr/bin/env python3
"""Exact author-side exploration of Newton coefficient log-concavity, r=1..48.
No independent acceptance and no all-index claim.  Original signed K/J engine.
"""
import sys,json
from pathlib import Path
from math import comb
from fractions import Fraction
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE.parent/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K,J,C,add,mul,forward_differences,eval_newton

def D(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))

def main():
    hi=48
    smax=3*(hi+1)+2; lim=2*(hi+1)+2
    kk=[None]+[K(i) for i in range(1,13)]
    B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(12,s)+1):z=add(z,mul(kk[i],B[s-i],lim),lim)
        B.append(z)
    L={}
    for r in range(hi+2):
        h=forward_differences([Fraction(D(B,r+u,u),5**u) for u in range(r+2)])
        assert h[-1]==0 and h[-2]==6**r,('H degree',r)
        scaled=[5**r*c for c in h[:-1]]
        assert all(v.denominator==1 for v in scaled)
        L[r]=eval_newton(list(map(int,scaled)),2*hi+3)
    records=[]
    for r in range(1,hi+1):
        y=[L[r][v+1]*L[r][v+2]-L[r-1][v+2]*L[r+1][v+1] for v in range(2*r+1)]
        c=forward_differences(y)
        assert len(c)==2*r+1 and all(x>0 for x in c)
        if r==1: assert c==[2620,2520,900],c
        lc=[c[j]*c[j]-c[j-1]*c[j+1] for j in range(1,2*r)]
        violations=[j for j,a in enumerate(lc,1) if a<0]
        norms=[comb(2*r,j) for j in range(2*r+1)]
        ulc=[j for j in range(1,2*r) if c[j]**2*norms[j-1]*norms[j+1]<c[j-1]*c[j+1]*norms[j]**2]

        zero=[j for j,a in enumerate(lc,1) if a==0]
        peak=max(range(len(c)),key=lambda j:c[j])
        records.append(dict(r=r, coefficients=len(c),turan_checks=len(lc),turan_violations=violations,zeros=zero,peak_index=peak,all_strict_positive=True,ultra_logconcavity_violations=ulc))
    out=dict(schema='R358_LOGCONCAVITY_PROBE_V1',r_range=[1,hi],check='c_j^2-c_(j-1)c_(j+1)>=0 for j=1..2r-1',total_checks=sum(x['turan_checks'] for x in records),violations=sum(len(x['turan_violations']) for x in records),zero_count=sum(len(x['zeros']) for x in records),r1_newton_coefficients=[2620,2520,900],r1_ULC_scaled_defect=-3081600,ulc_total_violations=sum(len(x['ultra_logconcavity_violations']) for x in records),records=records,scope='signed BRC auxiliary recurrence; author-side finite exact checks, no universal proof')
    (BASE/'R358_LOGCONCAVITY_PROBE.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print('r=1..',hi,'total Turan',out['total_checks'],'violations',out['violations'],'zero',out['zero_count'])
    print('first',records[:5]);print('last',records[-5:]);
if __name__=='__main__':main()
