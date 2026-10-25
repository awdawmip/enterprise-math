#!/usr/bin/env python3
"""Exact author checks: D25 corrected-Clausen oriented diagonal moment transfer.
Reuses adjacent project jet checker; not independent review or native CM.
"""
from pathlib import Path
from runpy import run_path

D=run_path(str(Path(__file__).with_name("20261026_hourly_d25_dual_strip_flux_check.py")))

def check(p):
    m=(p-1)//6; q=p*p; J=2*m; U=D["jets"](p,4)
    def moment(a,b,s,n):
        if a<0 or b<0:return 0
        return sum(j**s*U[j][a]*U[p-(j+n)][b]
                   for j in range(1,J+1) if 1<=j+n<=J)%q
    def port(a,b,n):
        S=(2*m*m*(a==0)+4*m*(a==1)+2*(a==2))%q
        T=(2*m*U[J][a-1] if a>=1 else 0)-(2*U[J][a-2] if a>=2 else 0)
        C=lambda e:U[p-e][b] if 1<=e<=J else 0
        return (S*C(n+1)+T*C(J+n+1))%q
    for a in range(5):
        for b in (2,3):
            for n in range(-J-1,J+1):
                lhs=(moment(a,b,2,n)-p*pow(2,-1,q)*moment(a,b,1,n)
                     -3*moment(a-1,b,1,n))%q
                rhs=(moment(a,b,2,n+1)-3*m*moment(a,b,1,n+1)
                     +2*m*m*moment(a,b,0,n+1)-3*moment(a-1,b,1,n+1)
                     +4*m*moment(a-1,b,0,n+1)+2*moment(a-2,b,0,n+1))%q
                assert (lhs-rhs)%q==port(a,b,n),(p,a,b,n)
                if a in (0,1) and n<0:assert (lhs-rhs)%q==0
    return True

if __name__=="__main__":
    tested=[p for p in D["primes"](211) if check(p)]
    assert len(tested)==22,len(tested)
    print("PASS: 22 p=1 mod6 primes <=211; a=0..4; b=2,3; all oriented diagonals; quadratic moments and boundary ports")
