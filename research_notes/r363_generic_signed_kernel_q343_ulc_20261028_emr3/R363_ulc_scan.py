#!/usr/bin/env python3
"""Exact BRC r337..343 ULC sign-change scan; no floating-point sign tests."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json,sys
P=Path(__file__).resolve().parent;ROOT=P.parent.parent
sys.path.insert(0,str(ROOT/'research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K,J,C,add,mul,forward_differences as fd,eval_newton
def D(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))
def main():
    N=343;lim=2*(N+1)+2
    ks=[None]+[K(i) for i in range(1,13)];B=[[1,1]]
    for s in range(1,3*(N+1)+3):
        z=J(s)
        for i in range(1,min(12,s)+1):z=add(z,mul(ks[i],B[s-i],lim),lim)
        B.append(z)
    L={}
    for r in range(335,N+2):
        d=fd([Fraction(D(B,r+u,u),5**u) for u in range(r+2)])
        assert d[-1]==0 and d[-2]==6**r
        x=[t*5**r for t in d[:-1]]
        assert all(z.denominator==1 for z in x)
        L[r]=eval_newton([int(z) for z in x],2*N+3)
    out=[]
    for r in range(337,N+1):
        c=fd([L[r][v+1]*L[r][v+2]-L[r-1][v+2]*L[r+1][v+1] for v in range(2*r+1)])
        assert all(v>0 for v in c)
        n=2*r
        a=[]
        for j in range(1,n):
            z=c[j]**2*j*(n-j)-c[j-1]*c[j+1]*(j+1)*(n-j+1)
            a.append((z>0)-(z<0))
        transitions=sum(a[i]!=a[i-1] for i in range(1,len(a)))
        row=(r,a.count(-1),a.count(1),a.count(0),transitions,next((i+1 for i,x in enumerate(a) if x>0),None))
        assert row[3]==0 and row[4]==1 and all(x<0 for x in a[:row[5]-1]) and all(x>0 for x in a[row[5]-1:])
        out.append(row)
    assert sum(a[1]+a[2]+a[3] for a in out)==4753
    assert sum(a[1] for a in out)==4358 and sum(a[2] for a in out)==395
    with (P/'R363_ULC_TRANSITIONS.csv').open('w') as f:
        f.write('r,ulc_failed,ulc_passed,ulc_equal,sign_changes,first_strict_positive_j\n')
        for x in out:f.write(','.join(map(str,x))+'\n')
    for x in out:print(x)
if __name__=='__main__':main()
