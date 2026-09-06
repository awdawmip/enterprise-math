#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product
from math import gcd
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_rational_holonomy import (  # noqa:E402
    rational_prime_valuations,
    rational_from_prime_valuations,
)

V=tuple(range(6))
PAIRS=tuple(combinations(V,2))
TRIPLES=tuple(combinations(V,3))
PAIR_INDEX={e:i for i,e in enumerate(PAIRS)}
TRIPLE_INDEX={S:i for i,S in enumerate(TRIPLES)}

# A=P^T : pair valuations -> triad valuations.
A=[[1 if set(e).issubset(S) else 0 for e in PAIRS] for S in TRIPLES]


def rank_q(M):
    B=[[Fraction(x) for x in row] for row in M]
    if not B:return 0
    m=len(B);n=len(B[0]);r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if B[i][c]),None)
        if piv is None:continue
        B[r],B[piv]=B[piv],B[r]
        z=B[r][c]
        B[r]=[x/z for x in B[r]]
        for i in range(m):
            if i!=r and B[i][c]:
                f=B[i][c]
                B[i]=[x-f*y for x,y in zip(B[i],B[r])]
        r+=1
        if r==m:break
    return r


def rank_mod(M,p):
    B=[[x%p for x in row] for row in M]
    if not B:return 0
    m=len(B);n=len(B[0]);r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if B[i][c]),None)
        if piv is None:continue
        B[r],B[piv]=B[piv],B[r]
        inv=pow(B[r][c],-1,p)
        B[r]=[(x*inv)%p for x in B[r]]
        for i in range(m):
            if i!=r and B[i][c]:
                f=B[i][c]
                B[i]=[(x-f*y)%p for x,y in zip(B[i],B[r])]
        r+=1
    return r


def det_bareiss(M):
    B=[list(map(int,row)) for row in M]
    n=len(B)
    if n==0:return 1
    sign=1;prev=1
    for k in range(n-1):
        if B[k][k]==0:
            piv=next((i for i in range(k+1,n) if B[i][k]),None)
            if piv is None:return 0
            B[k],B[piv]=B[piv],B[k];sign*=-1
        pivot=B[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                B[i][j]=(B[i][j]*pivot-B[i][k]*B[k][j])//prev
        prev=pivot
        for i in range(k+1,n):B[i][k]=0
    return sign*B[-1][-1]


def perfect_matchings(items):
    items=tuple(items)
    if not items:
        yield ();return
    a=items[0]
    for q in range(1,len(items)):
        b=items[q]
        rest=items[1:q]+items[q+1:]
        for tail in perfect_matchings(rest):
            yield tuple(sorted(((min(a,b),max(a,b)),)+tail))

MATCHINGS=tuple(sorted(set(perfect_matchings(V))))
assert len(MATCHINGS)==15


def trade_vector(M):
    v=[0]*20
    for bits in product((0,1),repeat=3):
        S=tuple(sorted(M[r][bits[r]] for r in range(3)))
        v[TRIPLE_INDEX[S]] += 1 if sum(bits)%2==0 else -1
    return tuple(v)

TRADES=tuple(trade_vector(M) for M in MATCHINGS)


def trade_flat_valuation(nu):
    return all(sum(v[s]*nu[s] for s in range(20))==0 for v in TRADES)


def pair_lambda_from_nu(nu):
    T=sum(nu)
    R=[sum(nu[s] for s,S in enumerate(TRIPLES) if i in S) for i in V]
    t=[sum(nu[s] for s,S in enumerate(TRIPLES) if set(e).issubset(S)) for e in PAIRS]
    return tuple(Fraction(6*t[a]-2*R[e[0]]-2*R[e[1]]+T,12) for a,e in enumerate(PAIRS))


def apply_pair_lambda(lam):
    return tuple(sum(lam[e] for e,pair in enumerate(PAIRS) if set(pair).issubset(S)) for S in TRIPLES)


def prime_nu(weights,p):
    vals=[]
    for w in weights:
        vals.append(dict(rational_prime_valuations(w)).get(p,0))
    return tuple(vals)


def factor_rational_pairs(weights):
    weights=tuple(Fraction(w) for w in weights)
    assert len(weights)==20 and all(w>0 for w in weights)
    primes=sorted({p for w in weights for p,_ in rational_prime_valuations(w)})
    pair_valuations=[{} for _ in PAIRS]
    defects={}
    for p in primes:
        nu=prime_nu(weights,p)
        if not trade_flat_valuation(nu):
            return None,('TRADE_DEFECT',p,nu)
        lam=pair_lambda_from_nu(nu)
        if apply_pair_lambda(lam)!=nu:
            raise AssertionError('trade-flat inverse reconstruction failed')
        if any(x.denominator!=1 for x in lam):
            defects[p]=lam
            continue
        for e,x in enumerate(lam):
            if x:
                pair_valuations[e][p]=x.numerator
    if defects:
        return None,('ROOT_TORSION',defects)
    q=tuple(rational_from_prime_valuations(v) for v in pair_valuations)
    rebuilt=tuple(
        q[PAIR_INDEX[tuple(sorted((S[0],S[1])))]]
        *q[PAIR_INDEX[tuple(sorted((S[0],S[2])))]]
        *q[PAIR_INDEX[tuple(sorted((S[1],S[2])))]]
        for S in TRIPLES
    )
    assert rebuilt==weights
    return q,None


def defect_order(nu):
    assert trade_flat_valuation(nu)
    lam=pair_lambda_from_nu(nu)
    for k in range(1,13):
        if all((k*x).denominator==1 for x in lam):
            return k
    raise AssertionError('unexpected denominator exponent')

# ---------- exact inverse formula on random-looking integer pair data ----------
examples=[
    tuple(range(-7,8)),
    tuple(((-1)**i)*(i%4) for i in range(15)),
    tuple(1 if i%3==0 else -2 if i%3==1 else 0 for i in range(15)),
]
for lam0 in examples:
    nu=apply_pair_lambda(lam0)
    assert trade_flat_valuation(nu)
    assert pair_lambda_from_nu(nu)==tuple(Fraction(x) for x in lam0)

# ---------- exact SNF/torsion certificate ----------
assert rank_q(A)==15
assert rank_mod(A,2)==10
assert rank_mod(A,3)==14
assert rank_mod(A,5)==15
minor_rows=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,16)
minor_det=abs(det_bareiss([A[r] for r in minor_rows]))
assert minor_det==96
# Rank drops force at least 2^5*3 in the nonzero Smith product; explicit minor
# gives an upper bound 96, hence the product is exactly 96 and invariant factors
# are 1^10,2^4,6 by divisibility ordering.
assert (2**(15-rank_mod(A,2)))*(3**(15-rank_mod(A,3)))==96
smith=(1,)*10+(2,)*4+(6,)
assert len(smith)==15
prod=1
for x in smith:prod*=x
assert prod==96
assert all(smith[i+1]%smith[i]==0 for i in range(14))

# ---------- exact rational factorization recovers a deliberately complicated pair field ----------
q0=tuple(Fraction(i+2,i+1) for i in range(15))
w0=tuple(
    q0[PAIR_INDEX[tuple(sorted((S[0],S[1])))]]
    *q0[PAIR_INDEX[tuple(sorted((S[0],S[2])))]]
    *q0[PAIR_INDEX[tuple(sorted((S[1],S[2])))]]
    for S in TRIPLES
)
qrec,err=factor_rational_pairs(w0)
assert err is None and qrec==q0

# ---------- cubic obstruction ----------
p=2
wcubic=(Fraction(p),)*20
assert all(
    __import__('functools').reduce(lambda a,s:a*wcubic[s],[i for i,x in enumerate(v) if x==1],Fraction(1))
    ==__import__('functools').reduce(lambda a,s:a*wcubic[s],[i for i,x in enumerate(v) if x==-1],Fraction(1))
    for v in TRADES
)
nucubic=(1,)*20
assert trade_flat_valuation(nucubic)
lamc=pair_lambda_from_nu(nucubic)
assert set(lamc)=={Fraction(1,3)}
assert defect_order(nucubic)==3
q,err=factor_rational_pairs(wcubic)
assert q is None and err[0]=='ROOT_TORSION'

# ---------- square obstruction ----------
nusquare=tuple(1 if 0 in S else 0 for S in TRIPLES)
assert trade_flat_valuation(nusquare)
lams=pair_lambda_from_nu(nusquare)
for e,pair in enumerate(PAIRS):
    expected=Fraction(1,2) if 0 in pair else Fraction(0)
    assert lams[e]==expected
assert defect_order(nusquare)==2
wsquare=tuple(Fraction(p) if 0 in S else Fraction(1) for S in TRIPLES)
q,err=factor_rational_pairs(wsquare)
assert q is None and err[0]=='ROOT_TORSION'

# ---------- order-six obstruction ----------
nu6=tuple(a+b for a,b in zip(nucubic,nusquare))
assert trade_flat_valuation(nu6)
assert defect_order(nu6)==6
lam6=pair_lambda_from_nu(nu6)
for e,pair in enumerate(PAIRS):
    expected=Fraction(5,6) if 0 in pair else Fraction(1,3)
    assert lam6[e]==expected
w6=tuple(a*b for a,b in zip(wcubic,wsquare))
q,err=factor_rational_pairs(w6)
assert q is None and err[0]=='ROOT_TORSION'

print('PASS_X6_TRIADIC_RATIONAL_PAIR_FACTORIZATION_V19')
print('incidence_rank_Q',rank_q(A))
print('rank_mod_2',rank_mod(A,2))
print('rank_mod_3',rank_mod(A,3))
print('maximal_minor_certificate',minor_det)
print('smith_invariants',smith)
print('residual_torsion','(Z/2)^4 x Z/6')
print('torsion_order',96)
print('cubic_obstruction_order',defect_order(nucubic))
print('square_obstruction_order',defect_order(nusquare))
print('combined_obstruction_order',defect_order(nu6))
print('exact_rational_factorization_recovery',True)
