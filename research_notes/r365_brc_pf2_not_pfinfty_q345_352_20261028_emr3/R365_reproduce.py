#!/usr/bin/env python3
"""R365 original signed BRC: exact Newton/Turan/ULC r=345..352."""
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json,sys
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P/'research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K,J,C,add,mul,forward_differences as fd,eval_newton

def D(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))

def main():
    hi=352;lim=2*(hi+1)+2; smax=3*(hi+1)+2
    ks=[None]+[K(i) for i in range(1,13)]; B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(s,12)+1):z=add(z,mul(ks[i],B[s-i],lim),lim)
        B.append(z)
    L={}
    for r in range(343,354):
        h=fd([Fraction(D(B,r+u,u),5**u) for u in range(r+2)])
        assert h[-1]==0 and h[-2]==6**r
        h=[z*5**r for z in h[:-1]]
        assert all(z.denominator==1 for z in h)
        L[r]=eval_newton([int(z) for z in h],2*hi+3)
    rows=[]; pieces=[]
    for r in range(344,353):
        n=2*r
        values=[L[r][v+1]*L[r][v+2]-L[r-1][v+2]*L[r+1][v+1] for v in range(n+1)]
        c=fd(values)
        assert len(c)==n+1 and all(z>0 for z in c)
        assert all(c[j]**2>c[j-1]*c[j+1] for j in range(1,n))
        assert c[-1]==30**n*comb(n,r)//(r+1)
        assert Fraction(c[-2],c[-1])==Fraction(17*r+11,10)
        assert Fraction(c[-3],c[-1])==Fraction(7803*r**3+2252*r**2-5523*r+3328,2700*(2*r-1))
        signs=[(j*(n-j)*c[j]**2>(j+1)*(n-j+1)*c[j-1]*c[j+1])-(j*(n-j)*c[j]**2<(j+1)*(n-j+1)*c[j-1]*c[j+1]) for j in range(1,n)]
        runs=[]
        for j,z in enumerate(signs,1):
            if not runs or runs[-1][0]!=z:runs.append([z,j,j])
            else:runs[-1][2]=j
        raw=''.join(f'{r},{j},{x}\n' for j,x in enumerate(c)).encode()
        h=sha256(raw).hexdigest()
        if r==344:assert h=='8b840f5fa5cb8aff6ccb57600fa792ad8ee98bfde39393107f1784361bac2143'
        else:
            pieces.append(raw)
            for k in range(1,9):
                q=r+k
                minor=D(B,q,k)*D(B,q+1,k+1)-D(B,q,k+1)*D(B,q+1,k)
                predicted=Fraction((L[r][k]*L[r][k+1]-L[r-1][k+1]*L[r+1][k])*5**(2*k+1),5**(2*r))
                assert minor==predicted and minor>0
            assert runs[0][0]==-1 and runs[-1][0]==1 and len(runs)==2
        rows.append({'r':r,'sha256':h,'newton_positive':len(c),'strict_turan':n-1,'ulc_negative':signs.count(-1),'ulc_positive':signs.count(1),'ulc_runs':runs})
    raw=b''.join(pieces)
    (P/'R365_Q345_352_FULL_COEFFICIENTS.txt').write_bytes(raw)
    out={'schema':'R365_EIGHT_BRC_STRIPS_V1','r_new':[345,352], 'B_max':smax,'H_range':[343,353],
         'positive_newton':sum(x['newton_positive'] for x in rows[1:]),
         'strict_turan':sum(x['strict_turan'] for x in rows[1:]),
         'ulc_negative':sum(x['ulc_negative'] for x in rows[1:]),
         'ulc_positive':sum(x['ulc_positive'] for x in rows[1:]),
         'ulc_zero':0,'raw_D_minor_checks':64,
         'combined_rows_sha256':sha256(raw).hexdigest(),'rows':rows,
         'scope':'signed BRC auxiliary model; infinite k depends on R363 author-side extraction; no native X6 bridge'}
    (P/'R365_EVIDENCE_COMPACT.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
