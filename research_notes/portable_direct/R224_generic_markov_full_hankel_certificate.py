#!/usr/bin/env python3
"""R224 exact two-prime determinant certificate for a rational Markov 250x250 Hankel matrix.
Run: python R224_generic_markov_full_hankel_certificate.py (standard library).
"""
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import json

K,M,L=6,12,2
N=K+1
WEIGHTS=[
 [62,38,60,37,72,74,49],
 [79,61,12,35,39,30,14],
 [47,37,16,87,62,44,39],
 [63,63,72,96,44,19,27],
 [30,42,83,62,82,52,75],
 [45,71,49,82,79,46,86],
 [11,53,67,59,35,1,60],
]
PRIMES=[1000000007,1000000009]
DEGREE=(K+2)*2**(K-1)-K


def stirling(n,k):
    row=[1]
    for i in range(1,n+1):
        nex=[0]*(i+1)
        for j in range(1,i+1):
            nex[j]=(row[j-1] if j-1<len(row) else 0)+(j*row[j] if j<len(row) else 0)
        row=nex
    return row[k]


def fibers():
    return [factorial(r)*M**L*sum(stirling(L+1,j+1) for j in range(min(r,L)+1)) for r in range(K+1)]


def observable_series_mod(p,nmax):
    W=fibers()
    den=[sum(row) for row in WEIGHTS]
    assert all(x%p for x in den)
    P=[[v*pow(den[i],-1,p)%p for v in WEIGHTS[i]] for i in range(N)]
    invn=pow(N,-1,p)
    blocks=[]
    for mask in range(1<<K):
        idx=[0]+[a+1 for a in range(K) if mask>>a&1]
        blocks.append((idx,[invn]*len(idx),W[mask.bit_count()]))
    out=[]
    for t in range(1,nmax+1):
        out.append(sum(w*sum(vec) for idx,vec,w in blocks)%p)
        updated=[]
        for idx,vec,w in blocks:
            nv=[sum(vec[i]*P[idx[i]][j] for i in range(len(idx)))%p for j in idx]
            updated.append((idx,nv,w))
        blocks=updated
    return out


def hankel_determinant_mod(seq,p):
    n=DEGREE
    H=[[seq[L+i+j-1] for j in range(n)] for i in range(n)]
    det=1
    for col in range(n):
        pos=next((i for i in range(col,n) if H[i][col]),None)
        if pos is None:return 0,col
        if pos!=col:
            H[col],H[pos]=H[pos],H[col]
            det=-det
        pivot=H[col][col]
        det=det*pivot%p
        inv=pow(pivot,-1,p)
        v=H[col]
        for i in range(col+1,n):
            if H[i][col]:
                z=H[i][col]*inv%p
                a=H[i]
                for j in range(col+1,n):
                    a[j]=(a[j]-z*v[j])%p
                a[col]=0
    return det%p,n


def crosscheck_first_four():
    W=fibers()
    T=[sum(comb(K-r,j-r)*W[j] for j in range(r,K+1)) for r in range(K+1)]
    den=[sum(row) for row in WEIGHTS]
    P=[[Fraction(v,den[i]) for v in WEIGHTS[i]] for i in range(N)]
    state={(i,(0 if i==0 else 1<<(i-1))):Fraction(1,N) for i in range(N)}
    direct=[]
    for _ in range(4):
        direct.append(sum(v*T[mask.bit_count()] for (i,mask),v in state.items()))
        nex={}
        for (i,mask),v in state.items():
            for j in range(N):
                key=(j,mask|(0 if j==0 else 1<<(j-1)))
                nex[key]=nex.get(key,Fraction())+v*P[i][j]
        state=nex
    blocks=[]
    for mask in range(1<<K):
        idx=[0]+[j+1 for j in range(K) if mask>>j&1]
        blocks.append((idx,[Fraction(1,N)]*len(idx),W[mask.bit_count()]))
    spectral=[]
    for _ in range(4):
        spectral.append(sum(w*sum(vec) for idx,vec,w in blocks))
        nxt=[]
        for idx,vec,w in blocks:
            nv=[sum(vec[i]*P[idx[i]][j] for i in range(len(idx))) for j in idx]
            nxt.append((idx,nv,w))
        blocks=nxt
    assert direct==spectral
    return [str(x) for x in direct],den


def run():
    assert K==6 and DEGREE==250
    assert len(WEIGHTS)==N and all(len(row)==N for row in WEIGHTS)
    assert all(v>0 for row in WEIGHTS for v in row)
    assert fibers()==[144,576,1440,4320,17280,86400,518400]
    early,den=crosscheck_first_four()
    certs=[]
    for p in PRIMES:
        values=observable_series_mod(p,L+2*DEGREE)
        det,rank=hankel_determinant_mod(values,p)
        assert rank==DEGREE and det!=0
        certs.append({"prime":p,"hankel_dimension":DEGREE,"modular_rank":rank,
                      "determinant_mod_p":det,"first_six_terms_mod_p":values[:6],
                      "row_denominators_all_units_mod_p":True})
    res={"status":"PASS",
      "theorem":"Exact minimal rational scalar recurrence order 250, generic sharpness under freely varying positive row-stochastic P with uniform initial pi",
      "arithmetic":"Integer Fp with exact Fraction independent four-term crosscheck",
      "m":M,"k":K,"L":L,"initial_distribution":"uniform 1/7",
      "integer_transition_weights":WEIGHTS,"row_denominators":den,
      "P_ij":"integer_transition_weights[i][j]/row_denominators[i]",
      "W_r":fibers(),"D_general":256,"D_reduced_upper_bound":DEGREE,
      "determinant_certificates":certs,"first_four_exact_rational_terms":early,
      "certificate_logic":"All row sums and 7 are units mod each prime; a nonzero determinant reduction certifies nonzero determinant over Q.",
      "native_brc_runtime":"NOT_EXECUTED","review":"NOT_REVIEWED"}
    target=Path(__file__).with_name("R224_verification.json")
    target.write_text(json.dumps(res,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("PASS R224 250x250",[(c["prime"],c["determinant_mod_p"]) for c in certs])
    return res

if __name__=="__main__":
    run()
