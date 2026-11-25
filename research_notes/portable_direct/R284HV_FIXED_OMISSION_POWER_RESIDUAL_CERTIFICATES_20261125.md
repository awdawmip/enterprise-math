# R284HV — Fixed-omission power-residual Bernstein certificates for full K

2026-11-25. Author proof via exact rational polynomial computation, NOT_REVIEWED. Same auxiliary binary-tag safe-word total-count observer as HU; no claim of native physical attribution or arbitrary labeled-branch quotient. Frozen immediate input: enterprise-math@73bbf287f040b2308558141e122f5fee34d2e9f5:research_notes/portable_direct/R284HU_FULL_K_TERMINAL_CORRECTION_20261125.md (definitions, boundary correction, finite signed tails, exact h transport). Keep its HT and HO provenance. Global entry blobs matched main@42c3c5ed5e02235fb2f64d5e560739aa436a23d0; current P000 V5 and ACTIVE worldview, joint preservation, continuation and portable research rules read. Original own RESEARCHER session recovery r1-20261125-2003-own-recovery verified original registration SUCCEEDED and session not closed; no run or CLAIM. Owner read r1-20261125-2003-owner-read SUCCEEDED, as_of 2026-11-25T12:04:15.341169Z at source 4113a2b7cfad6bb28b44df62c14a43a22ab69d78, tasks=[] for LEASED filter (later Source drift disclosed in receipt). Continue own independent research; no shared task ownership mutated.

## Theorem (full integer strips)
For every integer 0<=q<=12, K(q,u+1)>K(q,u) for every integer u>=q+1, and K(q,u)>K(q+1,u) for every integer u>=q+2. HU had established the read comparisons q=0,1 and omission q=0. Thus 23 additional unbounded strip propositions (some intersect previous fixed-deficit results, but here entire fixed-omission strips are covered). No extrapolation to arbitrary q.

## General power-residual transport
Define h_u=binom(2u,u)/binom(4u+4,u+1). HU's exact h transport is h_(u+1)=h_u rn(u)/rd(u), where
rn=3(u+2)(2u+1)(3u+4)(3u+5),
rd=4(u+1)(2u+3)(4u+5)(4u+7).
All coefficients of rd-2rn are positive (direct exact polynomial check), so 0<rn/rd<1/2 for u>=1. In particular h_u<=2^(-(u-1))/14. For any integer p>=1, if U>=2p and h_U<=1/(U+1)^p then h_u<=1/(u+1)^p for all integers u>=U. Indeed (1+1/(u+1))^p <= sum_{j>=0}(p/(u+1))^j <2, since u>=2p; induction via the exact transport proves the assertion. This permits any fixed polynomial tail payment when its initial bound is verified, without independently dropping the residual at either adjacent point.

## Exact finite-tail calculation and certificate
Use HU's M_n(k)=(k+1)/(n+1) binom(2n+2,n-k) for 0<=k<=n, zero elsewhere; n=u,m=u+q,d=u-q. Q=C_nm(d-1), V=C_nm(d), A=C_(n-1,m)(d)+C_(n-1,m)(d-1), E=M_(m-1)(0)(M_(n-1)(d)+M_(n-1)(d+1)), K=(A+E)Q(3u+q+1)^2/((Q+V+qA)^2(u+2q+1)). C_ab is the original joint convolution. No labeled observation is discarded for any other use.

For fixed shifts a,b,g, normalize C_(u+a,u+b)(u+g) by B=binom(4u+4,u+1). Its signed-extension main term and nonnegative finite tails give an affine polynomial in h. The function C in the replay implements HU exactly: if N=u+A+1, M=u+Bshift+1, each negative-factor tail i=1,...,Bshift-g-1 has r=Bshift-g-1-i, normalized contribution h * [binom(2N,N+i)/binom(2u,u)] * binom(2M,r) * i/N*(1-r/M); add both ordered capacities. The main term uses S=4u+2a+2b+4, j=u+a+b-g, factor (4(u+g+2)^2-S)/(S(S-1)) and binom(S,j)/B. In E the factor binom(2u+2q,u+q)/(u+q+1) is M_(m-1)(0). The factorial-shift function computes these quotients exactly as rational functions; at the chosen U and above all factorial arguments in the shift formulas are nonnegative (U>=32 and shifts bounded by 2q+O(1) for q<=13; larger q uses larger U). All denominator factors from these finite products are nonzero there. A common polynomial denominator of the four affine functions is then cleared in both numerator and denominator, so the denominator of K is positive at actual h by the original counts, regardless of common-denominator sign.

Write K=N_q(u,h)/D_q(u,h), both degree <=2 in h after clearing. Define T(P)=rd(u)^2 P(u+1,h rn/rd), a polynomial. The read sign is that of T(N_q)D_q-T(D_q)N_q, the omission sign is N_q D_(q+1)-D_q N_(q+1). The positive denominators at actual h justify both cross multiplications. For each resulting polynomial F(u,h)=sum a_i(u)h^i, degree L in h, substitute h=z/(u+1)^p and multiply by (u+1)^(pL). Shift u=U+x. The Bernstein coefficient of index k is
 b_k(x)=sum_{i<=k} a_i(U+x)(U+x+1)^(p(L-i))*binom(k,i)/binom(L,i).
If every ordinary coefficient is nonnegative and its constant is strictly positive, then b_k(x)>0 for x>=0. Bernstein basis functions binom(L,k) z^k(1-z)^(L-k) are nonnegative and sum to one on 0<=z<=1, proving strict F>0 on the entire infinite domain. This is a finite symbolic proof, not a sample-based threshold conjecture. The chosen p=2q+4 pays for the q-dependent finite tail; the exact initial h_U bound and U>=2p were checked for every certificate. For smaller budgets below U, original integer convolutions, including the original four P terms, establish the sign at every admissible integer. Thus no unknown threshold remains for these strips.

The code uses QQ univariate rational-function/polynomial arithmetic, retains h coefficient vectors and never expands a large rational expression in both variables. Earlier exploratory general-expression implementation timed out after some completed comparisons; it is not counted. The final replay completed with all assertions passing. The output records L, all Bernstein polynomial degrees and the total number of their nonzero coefficients. Zero missing coefficients are allowed; strict constants ensure positivity. 26 symbolic certificates, 16,601 nonzero coefficient tests (and strictly positive constants), 3,069 finite comparisons below chosen U, 104 direct formula crosschecks (56 distinct (q,u) locations for q=0..13). 23 new propositions, 16,245 nonzero coefficients and 2,978 finite comparisons in new propositions. The maximum degree is 226. No floating-point arithmetic used for any sign. The chosen start U is a sufficient certificate boundary, not a minimal onset. Local replay.py SHA256 31ee6ace5c6aaff0100b1fc6dc352cdefa9e87ae3caab1d0324f20c09b142f0d; local results.txt SHA256 6188834962c92e800924ad59f0108f983bbce687a6531be6f88400cbbd716bcd.

## Executed replay.py
```python
from math import comb, factorial
from fractions import Fraction as Fr
from functools import lru_cache
from sympy import QQ
from sympy.polys.fields import field
F,u=field('u',QQ); R=F.ring; x=R.gens[0]
def prod(seq):
    a=F.one
    for b in seq:a*=b
    return a
def shift(a,k):
    return prod(a+i for i in range(1,k+1)) if k>=0 else 1/prod(a-i for i in range(-k))
def binshift(a,b,i,j):return shift(a,i)/(shift(b,j)*shift(a-b,i-j))
def small(a,k):return prod(a-i for i in range(k))/factorial(k) if k>=0 else F.zero
@lru_cache(None)
def C(a,b,g):
    S=4*u+2*a+2*b+4; j=a+b-g-1
    main=binshift(4*u+4,u+1,2*a+2*b,j)*(4*(u+g+2)**2-S)/(S*(S-1))
    tail=F.zero
    for A,B in [(a,b),(b,a)]:
        N=u+A+1;M=u+B+1
        for i in range(1,B-g):
            r=B-g-1-i
            tail+=binshift(2*u,u,2*A+2,A+1+i)*small(2*M,r)*i/N*(1-r/M)
    return main,tail
def add(a,b):return [i+j for i,j in zip(a,b)]
def mul(a,b):
    p=[R.zero]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):p[i+j]+=v*w
    return p
@lru_cache(None)
def K(q):
    Q=C(0,q,-q-1);V=C(0,q,-q);A=add(C(-1,q,-q),C(-1,q,-q-1))
    E=(F.zero,binshift(2*u,u,2*q,q)/(u+q+1)*((u-q+1)*small(2*u,q-1)+(u-q+2)*small(2*u,q-2))/u)
    D=R.one
    for arr in [Q,V,A,E]:
        for a in arr:D=D.lcm(a.denom)
    Q,V,A,E=[[a.numer*D.exquo(a.denom) for a in arr] for arr in [Q,V,A,E]]
    N=[p*(3*x+q+1)**2 for p in mul(add(A,E),Q)]
    S=add(add(Q,V),[q*p for p in A]);D=[p*(x+2*q+1) for p in mul(S,S)]
    return N,D
rn=3*(x+2)*(2*x+1)*(3*x+4)*(3*x+5);rd=4*(x+1)*(2*x+3)*(4*x+5)*(4*x+7)
def transport(P):return [p.compose(x,x+1)*rn**i*rd**(2-i) for i,p in enumerate(P)]
def sub(a,b):return [v-w for v,w in zip(a,b)]
@lru_cache(None)
def M(n):
    a=[comb(2*n+2,n)//(n+1)]
    for k in range(n):
        b,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3));assert r==0;a.append(b)
    return a
def conv(a,b,g):return sum(a[k]*b[g-k] for k in range(max(0,g-len(b)+1),min(g+1,len(a))))
@lru_cache(None)
def exact(U,q):
    m=U+q;d=U-q;a,b,c,e=(M(n) for n in (U,m,U-1,m-1));Q=conv(a,b,d-1);V=conv(a,b,d);A=conv(c,b,d)+conv(c,b,d-1);P=sum(comb(3,j)*conv(c,e,d+1-j) for j in range(4));return Fr(P*Q*(3*U+q+1)**2,(Q+V+q*A)**2*(U+2*q+1))
def hval(U):return Fr(comb(2*U,U),comb(4*U+4,U+1))
def ev(P,U,H):return sum(Fr(str(p.evaluate(x,U)))*H**i for i,p in enumerate(P))
def check_reduction(q):
    N,D=K(q)
    for U in [q+1,q+2,q+5,2*q+15]:
        H=hval(U);a=ev(N,U,H);b=ev(D,U,H);assert b>0 and a/b==exact(U,q),(q,U)
def cert(P,start,power):
    while len(P)>1 and not P[-1]:P=P[:-1]
    L=len(P)-1
    pol=[p.compose(x,x+start)*(x+start+1)**(power*(L-i)) for i,p in enumerate(P)]
    degrees=[];count=0
    for k in range(L+1):
        b=sum((pol[i]*QQ(comb(k,i),comb(L,i)) for i in range(k+1)),R.zero)
        if b.get((0,),QQ.zero)<=0 or any(v<0 for v in b.values()):return None
        degrees.append(b.degree());count+=len(b)
    return L,degrees,count
assert all(v>0 for v in (rd-2*rn).values())
if __name__=='__main__':
    for q in range(13):
        check_reduction(q);N,D=K(q);N2,D2=K(q+1);check_reduction(q+1)
        for name,P,lo in [('read',sub(mul(transport(N),D),mul(transport(D),N)),q+1),('omit',sub(mul(N,D2),mul(D,N2)),q+2)]:
            power=2*q+4
            for start in [32,64,128,256]:
                if start<max(lo,2*power) or hval(start)>Fr(1,(start+1)**power):continue
                vals=cert(P,start,power)
                if vals:
                    for U in range(lo,start):
                        a=exact(U,q);b=exact(U+1,q) if name=='read' else exact(U,q+1);assert (b>a if name=='read' else a>b)
                    print(q,name,'start',start,'power',power,'Bernstein',vals,'finite',start-lo,flush=True);break
            else:print(q,name,'FAILED',flush=True)
```

## Actual results.txt
```text
0 read start 32 power 4 Bernstein (0, [22], 23) finite 31
0 omit start 32 power 4 Bernstein (2, [25, 25, 25], 78) finite 30
1 read start 32 power 6 Bernstein (4, [50, 50, 50, 50, 50], 255) finite 30
1 omit start 32 power 6 Bernstein (4, [47, 47, 47, 47, 47], 240) finite 29
2 read start 32 power 8 Bernstein (4, [66, 66, 66, 66, 66], 335) finite 29
2 omit start 32 power 8 Bernstein (4, [63, 63, 63, 63, 63], 320) finite 28
3 read start 64 power 10 Bernstein (4, [82, 82, 82, 82, 82], 415) finite 60
3 omit start 64 power 10 Bernstein (4, [79, 79, 79, 79, 79], 400) finite 59
4 read start 64 power 12 Bernstein (4, [98, 98, 98, 98, 98], 495) finite 59
4 omit start 64 power 12 Bernstein (4, [95, 95, 95, 95, 95], 480) finite 58
5 read start 128 power 14 Bernstein (4, [114, 114, 114, 114, 114], 575) finite 122
5 omit start 128 power 14 Bernstein (4, [111, 111, 111, 111, 111], 560) finite 121
6 read start 128 power 16 Bernstein (4, [130, 130, 130, 130, 130], 655) finite 121
6 omit start 128 power 16 Bernstein (4, [127, 127, 127, 127, 127], 640) finite 120
7 read start 128 power 18 Bernstein (4, [146, 146, 146, 146, 146], 735) finite 120
7 omit start 128 power 18 Bernstein (4, [143, 143, 143, 143, 143], 720) finite 119
8 read start 128 power 20 Bernstein (4, [162, 162, 162, 162, 162], 815) finite 119
8 omit start 128 power 20 Bernstein (4, [159, 159, 159, 159, 159], 800) finite 118
9 read start 128 power 22 Bernstein (4, [178, 178, 178, 178, 178], 895) finite 118
9 omit start 128 power 22 Bernstein (4, [175, 175, 175, 175, 175], 880) finite 117
10 read start 256 power 24 Bernstein (4, [194, 194, 194, 194, 194], 975) finite 245
10 omit start 256 power 24 Bernstein (4, [191, 191, 191, 191, 191], 960) finite 244
11 read start 256 power 26 Bernstein (4, [210, 210, 210, 210, 210], 1055) finite 244
11 omit start 256 power 26 Bernstein (4, [207, 207, 207, 207, 207], 1040) finite 243
12 read start 256 power 28 Bernstein (4, [226, 226, 226, 226, 226], 1135) finite 243
12 omit start 256 power 28 Bernstein (4, [223, 223, 223, 223, 223], 1120) finite 242
```

## Next
The previous HU goal to extend fixed q has been addressed for q<=12, not all q. Do not repeat these certificates as new science. Seek a uniform coefficient-sign argument in q (or an exact sign comparison in normalized A/Q,V/Q,E/Q) to remove both the q-dependent certificate search and the remaining central parameter region. HU boundary correction is essential: no discard of E. Combine with the already existing fixed-deficit strips and full-scale eventual result, but do not claim the whole integer domain until it is closed. Independent mathematical review and strict Activity observation audit remain pending.
