# D25/LIFT: Lucas–Euler transfer of the two Clausen ports (H40 author portable)

Date: 2026-11-11. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, original science pin c47e13e4aba0e006366f989d6334d443f6333ae3. This mathematical author note extends the composite CRT port note at commit 1c641f9045b7d4242e91ac3c5cc80e181d13b75a. It is not a native Task checkpoint or independent review.

For integers u,v>=0 define F_{u,v}(X)=sum_{k=0}^{min(u,v)} binom(u,k)binom(v,k) X^k. For m>=0, e in {0,1}, define the labeled pair
P_m^(e)=(F_{m,2m+e}(1/2), (1-6e)F_{m,2m+e}(1/2)+6F'_{m,2m+e}(1/2)).
All denominators are invertible modulo odd primes.

## All-prime theorem

Let q>=5 be prime and q | (6m+1+4e). Define e_q=0 for q=1 mod6 and e_q=1 for q=5 mod6, a=(q-1-4e_q)/6, b=2a+e_q, d=q-1-a-b. Write m=m0+qM and 2m+e=b0+qR with digits m0,b0 in [0,q-1]. Define H=F_{M,R}(1/2) in F_q. Put s=1 if e=e_q and s=2^(-d) if e!=e_q. Then, as an exact ordered-pair identity in F_q^2,

P_m^(e) = s H P_a^(e_q).

This identity is unconditional for every indicated q,m,e. In the matching branch (m0,b0)=(a,b); in the mismatched branch (m0,b0)=(q-1-a,q-1-b).

## Proof

(1) Lucas's binomial congruence, applied to both binomial coefficients indexed by k=k0+qK, yields F_{m,2m+e}(X)=F_{m0,b0}(X)F_{M,R}(X^q) mod q. Its derivative has only the derivative of the first factor in characteristic q; at X=1/2 the second factor evaluates to H by Frobenius. Thus both ports share exactly H, with the input label e retained.

(2) For nonnegative a,b with a+b<=q-1 there is the polynomial identity in F_q[X]:
F_{q-1-a,q-1-b}(X)=(1-X)^(q-1-a-b)F_{a,b}(X).
Proof: the integer-coefficient Euler/Chu–Vandermonde generating-function identity
sum_{k>=0} binom(a+k,k)binom(b+k,k)X^k=(1-X)^(-a-b-1) F_{a,b}(X)
is proved by comparing the common coefficient recurrence (k+1)^2 c_(k+1)=(a+k+1)(b+k+1)c_k, with initial coefficient 1, for the two sides. For each k<q, binom(q-1-a,k)=(-1)^k binom(a+k,k) mod q, including zero values above k=q-1-a, and likewise for b. Since (1-X)^q=1-X^q mod q, the right-hand series equals (1-X)^d F_{a,b}(X)/(1-X^q), with numerator degree q-1-max(a,b)<q. Comparing coefficients below q proves the identity of the two polynomials.

(3) When e!=e_q, the low-digit polynomial P(X)=(1-X)^d F_{a,b}(X) satisfies P(1/2)=2^(-d)F(1/2), P'(1/2)=2^(-d)(F'(1/2)-2d F(1/2)). Consequently the weighted port transforms by 2^(-d), since
1-6e-12d = 1-6e_q mod q.
Indeed q=6r+1 gives (e_q,e,d)=(0,1,3r) and the left coefficient is -5-6(q-1)=1 mod q; q=6r+5 gives (1,0,3r+3) and the left coefficient is 1-6(q+1)=-5 mod q. Combining (1)-(3) proves both labeled coordinates with the same scalar.

## Exact mathematical consequences

For any fixed q>=5, every base-prime zero at P_a^(e_q) propagates to the same named port for every integer m and both e branches with q|6m+1+4e. For example direct finite base evaluations give B=0 for q=5,7 and A=0 for q=13,19, so these are proved infinite arithmetic progressions. If H!=0 the ordered projective pair is the same as the base; if H=0 both ports vanish even when the base pair has a unique zero. Example q=13,m=28,e=0,N=169: H=F_{2,4}(1/2)=0 mod13, and both ports vanish mod13. The high-digit factor is therefore a necessary BRC repair coordinate for distinguishing unique zero versus both-zero reduction.

For squarefree N=6m+1+4e, if every prime q|N has A_a B_a=0 mod q at its canonical base, then N divides U_m V_m where U_m=2^m A_m,V_m=2^m B_m are integers. This is CRT combined with the theorem. The all-prime base-product statement and the q-power valuation lifts are separate open units; the all-index composite N|U_mV_m conjecture is not asserted proved.

BRC carrier/observer: (named A,B ports; branch e; low prime q; high-digit H; scale s; for q^a the full pair v_q(U),v_q(V)). Operation scope: reduction, selection of named port, and CRT/valuation recombination. Reuse class COMPOSE_APPLIED.

## Exact checks

The portable independent verifier checks all 4077 coefficients of the complementary-polynomial identity over 52 primes q<=251; both labeled base-port evaluations for all 166 primes 5<=q<=997; and 1273 factor cases q|N from e=0,1 and 0<=m<=400 using a raw binomial sum independently of the Lucas/Euler path. Of these, 480 are branch-mismatched and 122 have both ports zero modulo q. All comparisons passed. The local exact certificate and program are in the zipped portable reproduction package (SHA256 of local ZIP 0b6ba00c647b85e3a7ea252f8660533f8ed9f5f8ee32965e674e4bd13a913d0e).

Next: distinguish all-prime base zero selection from q^a valuation lifting; separately the parent D25 native original H0/B0, Frobenius eta and Delta_p-R_p interface still require the original-class module and native authorized experiment. Existing predecessor native completed units, original claim identities, and UR V2 proof remain unchanged.