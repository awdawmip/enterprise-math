# D25 — reciprocal-index three-port theorem for the original 216 coefficients

Date 2026-11-03 (+08). TASK_RESEARCH author-side derivation; exact finite computations; **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Logical Research lane: chatgpt-research-hourly-enterprise-math-20260923 (not the maintenance lane). Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen input pin c47e13e4aba0e006366f989d6334d443f6333ae3. Mother target: Delta_p-R_p=0 mod p for p mod24 in {13,19}; equivalently original weighted W216=p mod p^3. It remains open.

## Original carrier and question

For any prime p>=5, 0<=k<p, define in Z_(p)

\[
b_k=\binom{2k}{k}^{2}\binom{3k}{k}\,216^{-k}
=\frac{(2k)!(3k)!}{(k!)^{5}\,216^k}.
\]

The reciprocal product pairs k with p-1-k. Preserve index, pairing, valuation, unit, and polynomial/signed weight w(k). This is an *auxiliary original-216 3F2 reflected product*, different from the *frozen 2F1 Clausen cutoff Q_p*. No transfer to Q_p is inferred.

## Theorem A: exact valuation and three exceptions

For every k in [0,p-1],

\[
v_p(b_k)=\left\lfloor\frac{2k}{p}\right\rfloor+
\left\lfloor\frac{3k}{p}\right\rfloor .
\]

Write a=floor(p/3), m=(p-1)/2, c=floor(2p/3); a+c=p-1. Then

\[
v_p(b_k b_{p-1-k})=
\begin{cases}2,&k\in\{a,m,c\},\\3,&\text{otherwise}.\end{cases}
\]

*Proof.* The denominator k! is p-unit for 0<=k<p. By Legendre's formula the numerator (2k)!, (3k)! contributes exactly the two displayed floors (both arguments <3p). For n=2,3, the reflected sum floor(nk/p)+floor(n(p-1-k)/p) equals n-1 except at floor(jp/n) with 1<=j<n, where it equals n-2. The exceptional sets are {m} and {a,c}, disjoint. Summing the two reflected floors proves the assertion. All valuations are exact, not lower bounds.

## Theorem B: normalized leading sources

\[
\boxed{\frac{b_a b_c}{p^2}\equiv3\pmod p,\qquad
\frac{b_m}{p}\equiv-2\left(\frac6p\right)\pmod p.}
\]
Thus (b_m/p)^2=4 mod p. The symbol (6/p) is Legendre's symbol.

*Middle proof.* For m=(p-1)/2, 2m=p-1 and 3m=p+(m-1). Wilson implies (3m)!/p=-(m-1)! mod p and (p-1)!=-1 mod p. Consequently b_m/p equals
\[
\frac{(m-1)!}{(m!)^5\,216^m}
=\frac{1}{m(m!)^4\,216^m}\pmod p.
\]
Wilson's complement identity gives (m!)^2=(-1)^{m+1} mod p, hence (m!)^4=1. Here m=-1/2 mod p and Euler's criterion gives 216^m=(216/p)=(6/p), proving -2(6/p).

*Edge proof.* At c the factorials (2c)!, (3c)! each contain one p-factor. Use (p+t)!/p=-t! mod p for 0<=t<p, 216^{a+c}=216^{p-1}=1 mod p, to obtain
\[
\frac{b_a b_c}{p^2}\equiv
\frac{(2a)!(3a)!(2c-p)!(3c-p)!}{(a!c!)^5}\pmod p.\tag{*}
\]
If p=3a+1 (a even), c=2a, 3a=p-1, 2c-p=a-1, 3c-p=p-2, and (a!c!)^5=-1 via factorial complements; (*) becomes (2a)!(a-1)!=-1/a=3 mod p. If p=3a+2 (a odd), c=2a+1, 3a=p-2, 2c-p=a, 3c-p=p-1, and (a!c!)^5=1; (*) becomes -(2a)!a!=1/(a+1)=3 mod p. These steps use Wilson (p-1)!=-1, (p-2)!=1, and n!(p-1-n)!=(-1)^{n+1} mod p.

## Theorem C: uniform polynomial-observer/three-atom law

For any p-integral weight w(k) on k=0,...,p-1, put
\[
C_p(w)=\sum_{k=0}^{p-1}w(k)b_kb_{p-1-k}.
\]
Theorems A and B, with integral factors divided in Z_(p), imply
\[
\boxed{\frac{C_p(w)}{p^2}\equiv3w(a)+4w(m)+3w(c)\pmod p.}\tag{1}
\]
For w polynomial over Z[1/6], the unordered pair {a,c} reduces to {-1/3,-2/3}, while m=-1/2, so
\[
\boxed{\frac{C_p(w)}{p^2}\equiv
3w(-1/3)+4w(-1/2)+3w(-2/3)\pmod p.}\tag{2}
\]
The source index/orientation is retained separately from the scalar observer equation.

For j>=0, define mu_j=C_p(k^j)/p^2 mod p. Then
\[
\mu_j=3(-1/3)^j+4(-1/2)^j+3(-2/3)^j,
\qquad \sum_{j\ge0}\mu_j t^j=
\frac3{1+t/3}+\frac4{1+t/2}+\frac3{1+2t/3}.
\]
In particular
\[
C_p(1)\equiv10p^2,\quad C_p(k)\equiv-5p^2,\quad
C_p(k^2)\equiv\tfrac83 p^2,\quad
C_p(6k+1)\equiv-20p^2\pmod{p^3}.
\]
By the exact involution on k, 2C_p(k)=(p-1)C_p(1), hence **exactly in Z_(p)**: C_p(6k+1)=(3p-2)C_p(1).

## Unit D: BRC observer minimality

For the full family of all polynomial index observers w in F_p[X] of degree <=p-1, the three nonzero evaluation atoms in (2) are minimal: a representation using only two fixed evaluation nodes cannot reproduce all outputs. Indeed, choose a Lagrange delta polynomial of degree <=p-1 that is 1 on a missing atom and zero on all other nodes; the original measure outputs its nonzero weight 3 or 4, whereas the purported two-node representation outputs zero. This theorem is scoped to this observer family; for the fixed linear weight the above exact involution safely compresses the scalar. This moment law is symmetric between p=1 and p=5 mod6: the ordered edge labels exchange while both edge weights equal 3; signed residue-class transport requires further source information.

## Portable arithmetic evidence (finite, not all-prime proof)

The standard-library Python checker uses the original rational recurrence
\[
b_{k+1}=b_k\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3},\qquad b_0=1
\]
inside Z/(p^3), also independently rebuilding binomial coefficients at p<=43. Exact verification passed all 428 primes 5<=p<=3000 (207 p=1 mod6; 221 p=5 mod6): valuation/band, individual source units, and moment checks.

For p=373: (a,m,c)=(124,186,248), C_p(1)=1,391,290=10(373)^2, C_p(6k+1)=49,112,537=-20(373)^2 mod373^3. The *separate* original unreflected weighted sum
\[
W_p=\sum_{k=0}^{p-1}(6k+1)b_k
\]
matched the broader candidate W_p=p(-3/p) mod p^3 at all 428 tested primes. This is **only a finite observation**; the target-class p mod24 in {13,19} remains an unproved universal statement.

## Exact scientific continuation and boundary

BRC_COMPOSE_APPLIED: carrier retains (k,p-1-k), p-valuations, original 216 coefficient units, signed observer and provenance. Theorem C proves the **specific observer** compression and Unit D its necessary information horizon. No universal native X6 transfer is asserted. Prior accepted D24 UR/CM0 and prior author-side finite Clausen/Gauss/Hensel work are consumed and not recredited.

Next: derive or falsify an exact original finite weighted W216-to-reflection-three-atom CM/WZ bridge with full original sources, signs and truncations, or find an in-hypothesis counterexample to W216=p mod p^3. The reflected product C_p is **not** the frozen Q_p; no W-p congruence follows from Theorem C alone. The native p373 H0/B0 experiment (#1559) remains an independent operator-level gate, and Source control support remains #1558. No native session/claim/run/checkpoint/result/review was created by this portable work.