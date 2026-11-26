# R284JE — Deterministic large-prime window supply and sharper simultaneous certification
2026-11-27. Author proof, exact finite checks, NOT_REVIEWED. Auxiliary binary-tag joint-count observer; no native spatial transfer or formal Task/Result/Review. Continuing own RA-B82240E8488EF5A1DA5186C4 (own recovery succeeded, no runs). Owner inventory r1-20261127-0700-owner RUNNING at last prepublication observation; no shared task claimed or mutated.
Frozen inputs:
- JD 673771a11b75db41a98bbaaebba8305fe8f28e30:research_notes/portable_direct/R284JD_DENSITY_ONE_COMMON_CERTIFICATES_20261127.md (blob 7860e972da93f5b90594287214998f875c176a14).
- JC f4abd4b538f733777dc34f187b5236916806a72c:research_notes/portable_direct/R284JC_UNIFORM_GROWING_OFFSET_CERTIFICATES_20261127.md (blob d1ff271ebe73d9ec1f1509eea29459d1b128efa7).
- JB e92de4ef4680b68015e53c4c702fbf929dada0a0:research_notes/portable_direct/R284JB_FIXED_OFFSET_INTERIOR_POLE_FAMILY_20261127.md (blob 9ac16b9644637a8416a050c701568463acb70248).
Retain exactly V,Q,A,E,W,Z,C,Y and G_r(d) of JB and JC. P000 V5, ACTIVE worldview, joint preservation and portable research protocol consulted. No assumption of independent prime factors. This result replaces the short-interval statistical supply step of JD with a deterministic factorial/carry supply bound, while retaining its joint residue payments.

## 1. Deterministic window lemma
Let n,h,B be positive integers, h<=n, h<B and B^2>=n. Let L count integers a in [n-h+1,n] having a prime factor p>B. Then exactly
binom(n,h) = S * product_{a in window, P+(a)>B} P+(a),
where S is the B-smooth part of binom(n,h). In particular
S <= product_{p<=B} p^floor(log_p n) <= n^pi(B).
Consequently L >= log(binom(n,h))/log n - pi(B) for n>=2.
Proof: Each large prime occurs in precisely one window integer, at exponent one because p^2>n, and cannot divide h!. Conversely every p>B dividing the binomial occurs in the window. For each small prime, Legendre's formula for the binomial valuation is a sum of 0/1 floor differences, vanishing at p^j>n; thus v_p(S)<=floor(log_p n). This is the same type of exact carry bound used in IZ/JD, now applied to a whole composite-coordinate interval. The full window and the association (a,p) remain the source; the factor observation proves only the supply bound. No individual residual is erased.

Fix constants b,c,C>0, n in [X,3X], h comparable to sqrt(X), B=ceil(b sqrt(X)) with b>sqrt(3) and B>h. Using binom(n,h)>=((n-h+1)/h)^h and the elementary Chebyshev upper bound pi(B)=O(B/log B), the lemma yields uniformly in n:
L >= h/2 - O_{b,c,C}(sqrt(X)/log X).
Indeed log(n-h+1)-log h >= (1/2)log X-O(1) and log n<=log X+log 3. The Chebyshev estimate is standard and follows by bounding the primes in (m,2m] through binom(2m,m)<=4^m, dyadically summing to get theta(x)=O(x), and then pi(x)<=sqrt(x)+2theta(x)/log x.
This is a deterministic supply result for EVERY sufficiently large legal window at the given scale. It does not claim the exact uniform limiting fraction log 2.

## 2. Stronger joint certificate theorem
Fix 0<s<2. For q in [X,2X], put d0=floor(s sqrt(q)); let k=k(X)>=1 be an integer and D(q)={d: |d-d0|<=k}. Let R=floor(s sqrt(X)/40) and k<=R/8. For sufficiently large X all d legal, R<=d/10, and common coordinates are N=q+2d0-r+2 for 2k+1<=r<=R-2k, H=R-4k>=R/2. For every d=d0+e the same N uses r_d=r+2e in [1,R], hence the JC positive residue and JD denominator theorem apply.
Choose B=ceil(100 sqrt(X)), which for large X exceeds 20d+20, H, and sqrt(n) for n at the upper end of this interval. By section 1 every q has >=H/2-O_s(sqrt(X)/log X) raw large-prime witnesses; in particular >=H/3 for sufficiently large X, uniformly for k<=R/8.
Pay actual bad triples (q,d,r_d), not entire windows. For each fixed (d,r_d), JD bounds exceptional primes >20d+20 by O(d/log d). The q compatible with d lie in an interval of length O_s((k+1)sqrt(X)): invert |d-floor(s sqrt(q))|<=k. Each eligible prime hits N=q+2d-r_d+2 in O_s(k+1) such q. There are O_s(sqrt(X)) different d and O_s(sqrt(X)) r_d per d. Thus total bad triples are O_s((k+1)X^(3/2)/log X). Each spoiled common N at a fixed q can be charged to one bad triple, and different N at that q have distinct triples. Exclude the budgets with more than H/6 spoiled coordinates. There are at most O_s((k+1)X/log X) of these by incidence counting. All remaining budgets have >=H/6 common valid witnesses, each certifying Y(q,d)!=32/3 for all d in D(q) by the JB exact cross-residue criterion. The E residual remains included in every test.
For fixed k this strengthens the JD bound O(X/(log X)^(1/50)) to O(X/log X). By dyadic summation the fixed-band possible equality budgets <=X are O_s,k(X/log X). For k(X)=o(log X), a growing band still has density-one simultaneous certification with Omega_s(sqrt X) common witnesses per nonexceptional budget. In particular k=floor(sqrt(log X)) gives an explicit growing-width family with exceptional count O_s(X/sqrt(log X)). This does not exclude equality on the residual zero-density budgets.

## 3. Shorter deterministic search windows
The exact inequality in section 1 also applies with R=floor(C0 sqrt(X)/log X) and k<=R/8, for a sufficiently large absolute constant C0. Indeed pi(B)<=C1 sqrt(X)/log X for an absolute constant C1; choose C0>48 C1. H>=R/2, and log binom/log n>=H(1/2-O(1/log X)) for large X (the actual log(n/H) is even larger). Hence >=H/3 raw witnesses uniformly. R<=d/10 eventually. Use JC's O(r+1) exceptional prime count (rather than JD): sum over O_s(sqrt X) d and r<=R gives O_s((k+1)sqrt X R^2) bad triples. Exclude those q paying >H/6, giving O_s((k+1)sqrt X R)=O_s((k+1)X/log X) exceptions. Thus a window of size Theta(sqrt X/log X) suffices for the same exception order with Omega(sqrt X/log X) surviving witnesses. The hidden constants and asymptotic onset are not small numerical bounds. This reduces the number of candidate coordinates by a logarithmic factor, not an input-bit polynomial factor-discovery algorithm.

## 4. Executed exact verification
Python integer sieve (largest prime factor), factorial valuations and binomial identities. Tested every n=64..1024, h in {1,max(1,isqrt(n)//10),max(1,isqrt(n)//2),isqrt(n)}, B in {isqrt(n)+1,2*isqrt(n),min(n,20*isqrt(n)+20)} with duplicate choices removed: 10,524 exact cases. Plus 15 representative windows from the blocks below, 10,539 total exact binomial factorization/inequality checks, all passed.
Exhaustively counted raw (not residue-filtered) witnesses for s=1,k=1, R=isqrt(X)//10, B=100*(isqrt(X)+1), q=X..2X-1:
X,H,B,min,max,zero_windows,total_witnesses,windows
4096,2,6500,0,1,3687,409,4096
65536,21,25700,0,10,616,235800,65536
1048576,98,102500,10,41,0,25785265,1048576
These small scales do not assert the asymptotic lower bound is numerically effective there. No finite full Y or G reevaluation is claimed in this round; their certification uses frozen JB/JC/JD proofs. Source code (executed):

```python
from math import isqrt, comb, prod
N=2**21+5000
lpf=[0]*(N+1)
primes=[]
for p in range(2,N+1):
    if lpf[p]==0:
        primes.append(p)
        for j in range(p,N+1,p): lpf[j]=p
def vp_fact(n,p):
    v=0
    while n:
        n//=p; v+=n
    return v
def check(n,h,B):
    assert 1<=h<B and B*B>=n
    small_cap=1;small_part=1
    for p in primes:
        if p>B:break
        v=vp_fact(n,p)-vp_fact(n-h,p)-vp_fact(h,p)
        e=0;t=p
        while t<=n:e+=1;t*=p
        assert 0<=v<=e
        small_cap*=p**e;small_part*=p**v
    L=[lpf[j] for j in range(n-h+1,n+1) if lpf[j]>B]
    assert len(set(L))==len(L)
    C=comb(n,h)
    assert C==small_part*prod(L)
    assert C<=small_cap*n**len(L)
    return len(L)
count=0
for n in range(64,1025):
    for h in sorted({1,max(1,isqrt(n)//10),max(1,isqrt(n)//2),isqrt(n)}):
        for B in sorted({isqrt(n)+1,2*isqrt(n),min(n,20*isqrt(n)+20)}):
            check(n,h,B);count+=1
print('exact factorial window identities',count)
for X in (2**12,2**16,2**20):
    R=isqrt(X)//10; H=R-4; B=100*(isqrt(X)+1)
    assert H>0
    top=2*X+2*isqrt(2*X)+4
    pref=[0]*(top+1)
    for n in range(1,top+1):pref[n]=pref[n-1]+(lpf[n]>B)
    m=H;M=0;zero=total=0
    for q in range(X,2*X):
        d=isqrt(q);a=q+2*d-R+4;b=q+2*d-1
        assert b-a+1==H
        z=pref[b]-pref[a-1];m=min(m,z);M=max(M,z);zero+=z==0;total+=z
    print('block',X,'H',H,'B',B,'min',m,'max',M,'zero',zero,'total',total,'windows',X)
    for q in [X,X+1,X+X//4,X+X//2,2*X-1]:
        d=isqrt(q);n=q+2*d-1
        assert check(n,H,B)==pref[n]-pref[n-H]
        count+=1
print('total exact windows',count)
```
Next: all-budget non-equality now reduces in the linear window to ruling out simultaneous exceptional cross-residues on a deterministic positive fraction of coordinates (or finding complementary certificates on that residual set). Need pointwise joint incidence control, not another almost-all supply estimate. Real inverse-polynomial residual separation and worst-case factor discovery remain open.
