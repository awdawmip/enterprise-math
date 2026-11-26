# R284IN - Sharp logarithmic discrepancy obstruction and exact Gauss support
2026-11-26. Author proof, NOT_REVIEWED. Own direct R284 continuation; no shared Task claimed or protected Task-state mutation. Original own session MCP-8cd6c4fa26b9459d923ff73ba0082220 recovered (registration SUCCEEDED, not closed, no runs). Owner inventory request r1-20261126-1400-owner-read last observed RUNNING; no ownership inference. Account normative entry blobs checked at 43b66da4a682a09bd071afc7ba028187cfc765b5; Source main snapshot ec75fb65c6b1f7716f98eb6edab21c77fb8c653e, P000 V5 and joint-relation/Heartbeat foundation projection read. This is an auxiliary external arithmetic-observer analysis for the R284 safe-word count, not a new native spatial or physical attribution.

Frozen scientific inputs:
- IM: 0b2b7b16e08ca9516a4fa64d75d6aec2f60f70fc:research_notes/portable_direct/R284IM_COMMON_RESONANCE_FREQUENCY_LATTICE_20261126.md
- IL: 0ba4281d63293680694a2bb4843b732fd2cf819f:research_notes/portable_direct/R284IL_QUANTITATIVE_JOINT_DIOPHANTINE_SEPARATION_20261126.md
IM supplies a general upper discrepancy bound O_epsilon(L^(-1/2+epsilon)) for pairs satisfying IL's joint separation condition. Here L=log M/log log M. The actual R284 critical coefficients retain their fixed definitions and endpoint constraint; no finite true-K computation is repeated.

## 1. Main result: the pure half exponent fails under the joint separation hypothesis alone
There exists an irrational A in (0,1), with B=0 and C=0, such that for every integer T>=1,
max(||T A||,||T B||) >= exp(-3 T log(T+2)),
but for the interval discrepancy D_M of {A n^2+B n+C}, n=1,...,M,
limsup_{M->infty} sqrt(L) D_M = +infty.
More precisely along an unbounded subsequence M, D_M >= c log(log(log L))/sqrt(L) for some c>0 (for sufficiently large L). Consequently no O(L^-1/2) upper bound, even with a constant depending on the fixed pair, follows from the joint separation condition alone. No exponent 1/2+epsilon is universally valid either. Together with IM this establishes the optimal supremal exponent 1/2 for that general hypothesis, with an unavoidable unbounded correction for at least one pair. This is a counterexample in the general coefficient class, NOT a counterexample for the actual R284 critical pair, its special exponential endpoint relation, or its actual exception-count bound.

## 2. Infinite exact denominator construction
Use continued-fraction convergents p_i/q_i, with p_0=0,q_0=1,p_1=1,q_1=3. A positive next partial quotient a gives p_next=a p+p_prev, q_next=a q+q_prev. Consecutive determinants have absolute value 1, so all fractions are reduced and consecutive denominators are coprime. Define an infinite sequence in stages: start a stage with x=q_(2k-1), preceding denominator q_(2k-2), and set H=x, P=8 product of all odd primes <=H (so P<=8 H^H). All denominators are odd.

First choose a >=(x+2)^x making y=q_(2k)=a x+q_(2k-2) coprime to P. For each prime ell|P with ell|x every residue a works since gcd(x,q_prev)=1; for ell not dividing x, exclude the single residue giving y=0 modulo ell. Choose one permissible residue per prime, including ell=2. CRT gives a choice with a<=(x+2)^x+P. Then y is coprime to P.

Second choose a >=(y+2)^y satisfying a y+x=-1 (mod P), possible because gcd(y,P)=1, and a<=(y+2)^y+P. Thus r=q_(2k+1)=a y+x is congruent to -1 modulo P, and is odd. This finishes the stage and is repeated with x=r. These steps use entire composite denominator/modulus relations, not independent prime observations; CRT is exact.

For each step with denominator q>=3, because H<=q and P<=8(q+2)^q,
q (q+2)^q <= q_next <= 10 q (q+2)^q.
In particular q_next>2q. The consecutive rational intervals are nested (positive partial quotients, determinant +/-1) and their lengths 1/(q_i q_(i+1)) tend to zero. Their unique limit A has |A-p_i/q_i|<=1/(q_i q_(i+1)). The limit is irrational: for a rational with denominator d, a distinct reduced approximant differs by >=1/(d q_i), incompatible for q_(i+1)>d; the infinitely many consecutive distinct convergents cannot all equal it. This also supplies the needed standard convergent error without a best-approximation theorem.

For T>=3 select consecutive q_i<=T<q_(i+1)=r'. The exact rational p_(i+1)/r' gives ||T p_(i+1)/r'||>=1/r' since T<r' and its numerator is coprime to r'. The limit differs in the multiplied observation by <=T/(r' q_(i+2))<1/q_(i+2)<1/(2r'). Thus ||TA||>1/(2r'). For q>=3, log(2q_next)<=q log(q+2)+log(20q)<=3q log(q+2)<=3T log(T+2). For T=1,2 use the same determinant-distance estimate with r'=q_1=3, q_2>6; the norm is >1/6, stronger than exp(-3T log(T+2)). This proves joint separation for every positive integer, with K=3.

## 3. Exact composite Gauss phase law
Write e(t)=exp(2 pi i t), G(a,b;r)=sum over n mod r of e((a n^2+b n)/r). For odd r and gcd(a,r)=1, IM's exact squared correlation has only shift zero, giving |G(a,0;r)|^2=r. For any unit h modulo odd r,
G(h a,0;r)=Jacobi(h,r) G(a,0;r).
Here is a proof retaining composite factors. For an odd prime p, the number of square roots of u is 1+Legendre(u,p) including u=0, so change variables in the signed character sum to obtain the scaling. For p^j, j>=2, write n=x+p^(j-1)t with x mod p^(j-1), t mod p. The t-sum vanishes unless p|x; then it equals p. Hence G(a,0;p^j)=p G(a,0;p^(j-2)) with G(...;1)=1. The scaling factor is Legendre(h,p)^j. For coprime moduli, CRT factors the sum into local Gauss sums with unit-scaled a; the same scaling law multiplies to Jacobi(h,r). This derivation covers repeated prime factors and does not assume r prime.

For the special r above, r=-1 mod 8 and r=-1 mod every odd prime <=H. Thus gcd(h,r)=1 and Jacobi(h,r)=1 for each 1<=h<=H: for odd prime ell<=H, quadratic reciprocity gives Jacobi(ell,r)=Legendre(r,ell)*(-1)^((ell-1)/2)=1, and the supplementary law gives Jacobi(2,r)=1. Multiplicativity covers all h. Also Jacobi(-1,r)=-1, so complex conjugation G(-a,0;r)=-G(a,0;r) implies G(a,0;r)=sigma i sqrt(r), sigma in {-1,+1}. Every low-frequency h<=H therefore carries exactly the SAME imaginary phase, not merely the same magnitude. The classical quadratic reciprocity and supplementary laws are used in their ordinary integer scope.

## 4. Convert joint phase alignment into a discrepancy lower bound
Use f(t)=1/2-{t} on the circle and its Fejer polynomial
F_H(t)=(1/pi) sum_(h=1)^H (1-h/(H+1)) sin(2 pi h t)/h.
This is convolution with the nonnegative Fejer kernel of integral 1 (kernel = |sum_(j=0)^H e(jt)|^2/(H+1)); hence its circular total variation is <=2, the total variation of f. Its mean is zero and |F_H'|<=2 sum_(h=1)^H (1-h/(H+1))=H. Integration by parts against the empirical-minus-uniform cumulative measure implies |mean F_H|<=2 D_M for interval discrepancy.

For a special denominator r=q_i, with numerator a=p_i, choose M=r floor(sqrt(q_(i+1))/(10r)); for all sufficiently large r this is positive and tends to infinity, and is an exact multiple of r. The average of F_H(a n^2/r) over n=1,...,M equals its complete-period average and therefore equals
sigma/(pi sqrt(r)) [sum_(h=1)^H 1/h - H/(H+1)].
The bracket is >=c0 log H for large H. By the rational approximation bound,
|A n^2-a n^2/r|<=M^2/(r q_(i+1))<=1/(100r).
The Lipschitz cost for F_H is at most H/(100r) in the average. Since r grows at least as y(y+2)^y and y>=x(x+2)^x with H=x, this cost is o(log H/sqrt(r)). Consequently D_M>=c1 log H/sqrt(r) on this subsequence. The error is an explicit observer-specific residual payment; the signed Gauss correlation is preserved before applying it.

The denominator growth yields log M=(1/2+o(1)) r log r and log log M=(1+o(1)) log r, hence L=(1/2+o(1))r. Also log y=(1+o(1)) x log x, log r=(1+o(1)) y log y, so log log log r=(1+o(1)) log x=(1+o(1))log H. Substitution proves the stated stronger lower bound. This is an infinite constructive argument with no numerical inference about the actual critical constants.

## 5. Additional exact support refinement for IM's upper-bound route
For arbitrary integer c,b and r>=1, put g=gcd(c,r), R=r/g. Translation by R proves G(c,b;r)=0 if g does not divide b; if it does, G(c,b;r)=g G(c/g,b/g;R). For primitive c' mod R, squaring via the shift correlation as in IM gives the exact value
|G(c',b';R)|^2 = R if R is odd;
|G(c',b';R)|^2 = R[1+(-1)^(c' R/2+b')] if R is even.
The latter follows because only shifts 0 and R/2 survive. Thus this is an exact vanishing criterion, not a numerical cutoff.

In IM's common lattice h=j k, b_h=k v with gcd(v,j)=1, a coprime to r, let r_parallel=product of the full prime powers p^nu||r for which p|j, and r_perp=r/r_parallel. If a resonant Gauss sum is nonzero then gcd(j k,r)|k v. At p|j and p|r, v is a unit, so min(v_p(j)+v_p(k),v_p(r))<=v_p(k), forcing v_p(k)>=v_p(r). Thus r_parallel|k. This retains all prime-power valuations of shared denominators; it is not enough to require only rad(r_parallel)|k. For k=r_parallel ell we have gcd(j k,r)=r_parallel gcd(ell,r_perp). After retaining the even-modulus vanishing condition if desired, IM's weighted sum therefore has the stronger upper bound
sum_(resonant h<=H) |G(h a,b_h;r)|/(r h)
<= sqrt(2)/(j r_parallel sqrt(r_perp)) (1+log H) sum_(d|r_perp) d^(-1/2).
If j r_parallel>H the sum is zero. Relative to the earlier prefactor sqrt(2/(jr)), this removes the factor sqrt(j r_parallel) and deletes the shared-prime part from the divisor sum. This is especially effective for repeated common prime factors; it does not remove the worst-case j=1 phase-alignment obstruction of sections 2-4. No stronger global IM upper bound is claimed.

## 6. Actual exact finite checks (supporting, not the infinite proof)
The following Python code was run locally. Cyclotomic remainders in Z[X]/Phi_r(X) provide exact equality and zero tests for the full signed Gauss sums; all other checks are integer/CRT/Jacobi. The last 58 stages deliberately use a capped anchor only to verify modular construction mechanics, not asymptotic growth. The first actual stage uses the full anchor. No true-K samples or native physical simulations are claimed.

```python
from math import gcd, prod
from sympy import primerange, cyclotomic_poly, Poly, Symbol, jacobi_symbol
from sympy.ntheory.modular import crt

x=Symbol('x')
def modulus(r):
    return [int(v) for v in reversed(Poly(cyclotomic_poly(r,x),x).all_coeffs())]
def reduce_poly(v,p):
    v=list(v); m=len(p)-1
    for i in range(len(v)-1,m-1,-1):
        c=v[i]
        if c:
            for j in range(m): v[i-m+j]-=c*p[j]
    return tuple(v[:m])
def gauss(r,a,b,p):
    v=[0]*r
    for n in range(r): v[(a*n*n+b*n)%r]+=1
    return reduce_poly(v,p)

c=0; zeros=0
for r in range(2,41):
    p=modulus(r)
    for a in range(r):
        for b in range(r):
            g=gcd(a,r)
            zero=(b%g!=0)
            if not zero:
                R=r//g
                zero=R%2==0 and ((a//g)*(R//2)+b//g)%2==1
            actual=not any(gauss(r,a,b,p))
            assert actual==zero,(r,a,b)
            c+=1;zeros+=actual
print('exact cyclotomic zero tests:',c,'zeros:',zeros)
c=0
for r in range(3,82,2):
    p=modulus(r)
    for a in (1,2,5):
        if gcd(a,r)!=1:continue
        v=gauss(r,a,0,p)
        for h in range(1,r):
            if gcd(h,r)!=1:continue
            sign=int(jacobi_symbol(h,r))
            assert gauss(r,h*a,0,p)==tuple(sign*t for t in v),(r,a,h)
            c+=1
print('exact Jacobi phase-transport tests:',c)

c=0
for r in range(1,81):
    for j in range(1,61):
        par=prod(p**next(k for k in range(1,r.bit_length()+1) if r%p**k!=0)//p for p in primerange(2,r+1) if j%p==0 and r%p==0)
        for k in range(1,61):
            if gcd(j*k,r) and k%gcd(j*k,r)==0:
                assert k%par==0
            if k%par==0: assert k%gcd(j*k,r)==0
            c+=1
print('exact resonance support tests (v=1):',c)

def next_coprime(q,prev,H,anchor):
    primes=list(primerange(2,H+1)); residues=[]
    for p in primes:
        residues.append(next(a for a in range(p) if (a*q+prev)%p))
    a0,mod=map(int,crt(primes,residues)); a=anchor+(a0-anchor)%mod
    return a*q+prev,a
def special(q,prev,H,anchor):
    P=8*prod(primerange(3,H+1)); assert gcd(q,P)==1
    a0=(-1-prev)*pow(q,-1,P)%P
    a=anchor+(a0-anchor)%P
    return a*q+prev,a,P

x0=3;prev=1;H=x0
q,a=next_coprime(x0,prev,H,(x0+2)**x0)
r,b,P=special(q,x0,H,(q+2)**q)
assert gcd(q,P)==1 and r%P==P-1 and gcd(q,r)==1
assert (x0+2)**x0<=a<=(x0+2)**x0+P
assert (q+2)**q<=b<=(q+2)**q+P
assert all(jacobi_symbol(h,r)==1 for h in range(1,H+1))
print('actual first stage:', 'H=',H,'q_even=',q,'special_denominator_bits=',r.bit_length(),'modulus=',P)
q,prev=3,1
for H in range(3,61):
    y,_=next_coprime(q,prev,H,2*H+1)
    r,_,P=special(y,q,H,2*H+1)
    assert gcd(y,P)==1 and r%P==P-1 and gcd(y,r)==1
    assert all(jacobi_symbol(h,r)==1 for h in range(1,H+1))
    prev,q=y,r
print('capped CRT stages:',58,'largest denominator bits:',q.bit_length())
```
Output:
```
exact cyclotomic zero tests: 22139 zeros: 9052
exact Jacobi phase-transport tests: 3860
exact resonance support tests (v=1): 288000
actual first stage: H= 3 q_even= 379 special_denominator_bits= 3258 modulus= 24
capped CRT stages: 58 largest denominator bits: 4270
```

## 7. Next
A universal pure-half bound from the IL inequality alone is now disproved; do not invest in a general Gauss-factor elimination as if it could prove that target. For actual R284 constants, use the extra endpoint relation exp(s0^2/2)=R(s0^2,C0), not just its weakest joint separation consequence. Investigate whether it forbids simultaneous low-denominator rational phase alignment or permits polynomial joint separation. Separately, extract explicit uniform true-K remainder and build the sparse BRC fallback. The counterexample says nothing about failure of a pure-half or power-saving bound for the actual R284 pair. Previous ID/IJ dependencies and review status remain unchanged.
