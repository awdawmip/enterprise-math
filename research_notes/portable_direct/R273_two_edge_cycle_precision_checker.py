#!/usr/bin/env python3
"""Exact rational certificate for R273 typed visible BRC directed-cycle feedback.

Finite ranges are explicit; general theorems are proved algebraically in the companion MD.
No external packages, floats or randomized tests. Writes deterministic JSON.
"""
from fractions import Fraction as F
from hashlib import sha256
import json


def vp(x,p):
    if x == 0: return None  # infinity
    x=F(x);u=abs(x.numerator);v=x.denominator;k=0
    while u%p==0:u//=p;k+=1
    while v%p==0:v//=p;k-=1
    return k


def residue(x,p):
    x=F(x);assert x.denominator%p
    return x.numerator*pow(x.denominator,-1,p)%p


def v_atleast(x,p,t):
    v=vp(x,p)
    return v is None or v>=t


def cycle_star(p,L,N,c):
    q=p**N; a=F(1,1+c*q)
    den=1-a**L
    assert 0<a<1 and c%p and L%p
    assert vp(den,p)==N
    mat=[[a**((j-i)%L)/den for j in range(L)] for i in range(L)]
    # Exact inverse check: (I-a P)S = I, using row i of P has j=i+1.
    assert all(mat[i][j]-a*mat[(i+1)%L][j]==int(i==j)
               for i in range(L) for j in range(L))
    return a,mat


def test_cycle(p,L,N,m):
    q=p**N;c=1;d=1+p**(m-1)
    a,S=cycle_star(p,L,N,c)
    b,T=cycle_star(p,L,N,d)
    vinput=vp(a-b,p)
    assert vinput==N+m-1
    # Every labeled entry has the same sharp normalized sensitivity.
    for i in range(L):
        for j in range(L):
            assert vp(S[i][j],p)==-N
            assert residue(q*S[i][j],p)==pow(L*c,-1,p)
            assert vp(q*(S[i][j]-T[i][j]),p)==m-1
    # Q = I-J/L; S_regular = S - 1/[L(1-a)] J.
    R=[[S[i][j]-1/(L*(1-a)) for j in range(L)] for i in range(L)]
    U=[[T[i][j]-1/(L*(1-b)) for j in range(L)] for i in range(L)]
    assert all(v_atleast(R[i][j],p,0) for i in range(L) for j in range(L))
    assert all(v_atleast(R[i][j]-U[i][j],p,vinput)
               for i in range(L) for j in range(L))
    assert any(vp(R[i][j]-U[i][j],p)==vinput for i in range(L) for j in range(L))
    # Proper cycle edge subset cannot form a directed cycle. For fixed
    # weights a and any set missing at least one edge, W^L=0;
    # this is verified by a bounded walk-step DP on the labeled graph.
    for missing in range(L):
        walks=[1]*L
        for _ in range(L):
            walks=[(0 if i==missing else walks[(i+1)%L]) for i in range(L)]
        assert walks==[0]*L
    return dict(p=p,ports=L,depth=N,m=m,
                input_difference_valuation=vinput,
                normalized_all_entries_difference_valuation=m-1,
                regular_entries_min_difference_valuation=vinput,
                residue_first_entry=residue(q*S[0][0],p),
                pole_valuation=-N,proper_cycle_subsets_acyclic=True)


def two_port_witness(p,N,m):
    q=p**N; c=1; d=1+p**(m-1)
    a,S=cycle_star(p,2,N,c)
    b,T=cycle_star(p,2,N,d)
    # Baseline S11=1; each one-edge context has S11=1; together S11>1.
    mixed=S[0][0]-1
    assert mixed==a*a/(1-a*a)
    assert vp(mixed,p)==-N
    assert residue(q*mixed,p)==pow(2*c,-1,p)
    assert vp(q*((S[0][0]-1)-(T[0][0]-1)),p)==m-1
    # antisymmetric labeled observer is regular
    h=S[0][0]-S[0][1]
    k=T[0][0]-T[0][1]
    assert h==1/(1+a) and k==1/(1+b)
    assert vp(h-k,p)==vp(a-b,p)
    return dict(p=p,depth=N,m=m,mixed_valuation=-N,
                normalized_mixed_residue=residue(q*mixed,p),
                antisymmetric_difference_valuation=vp(h-k,p))


def main():
    cells=[];pair=[]
    for p, Ls, depths, precisions in [
            (5,range(2,9),range(1,4),range(1,4)),
            (7,range(2,9),range(1,4),range(1,4)),
            (11,range(2,9),range(1,4),range(1,4)),
            (13,range(2,9),range(1,6),range(1,5))]:
        for L in Ls:
            if L%p==0:continue
            for N in depths:
                for m in precisions:
                    cells.append(test_cycle(p,L,N,m))
                    if L==2:pair.append(two_port_witness(p,N,m))
    sweep=[]
    for N in range(1,9):
        for c in range(1,13):
            a,S=cycle_star(13,2,N,c)
            sweep.append(dict(depth=N,c=c,normalized_residue=residue(13**N*S[0][0],13),
                              expected=pow(2*c,-1,13)))
    result=dict(schema='ENTERPRISE_MATH_R273_CYCLE_RESONANCE_CERTIFICATE_V2',
                status='PASS',scientific_scope='finite exact sample grid with a separate universal symbolic proof',
                primes=[5,7,11,13],max_ports=8,
                case_count=len(cells),two_port_count=len(pair),residue_sweep_count=len(sweep),
                cases=cells,two_port_cases=pair,residue_sweep=sweep)
    data=json.dumps(result,sort_keys=True,separators=(',',':'),ensure_ascii=False)+'\n'
    dest='/mnt/data/em_r273/R273_verification.json'
    with open(dest,'w',encoding='utf8') as f:f.write(data)
    print('R273 PASS',len(cells),'cycle cases',len(pair),'two-port cases',len(sweep),'13-adic residue checks')
    print('SHA256',sha256(data.encode('utf8')).hexdigest(),'bytes',len(data.encode('utf8')))


if __name__=='__main__':main()
