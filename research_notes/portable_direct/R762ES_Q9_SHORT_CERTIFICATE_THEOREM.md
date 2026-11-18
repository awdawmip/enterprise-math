# R762ES — 127-state short certificate for all-horizon q=9 BRC content, and a general finite-state theorem

Date: 2026-11-18. Research line: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Historical input lineage: EM-X6-3050F6. This is a new portable author-side proof optimization and separate modular certificate, not a Source-authenticated researcher CLAIM. Independent review: NOT_REVIEWED.

## Model and relationship to prior work

Work in the positive six-NAMED-branch terminal observer only:
\[
R_q=\mathbb Z[(\mathbb Z/q\mathbb Z)^3],\quad
P_q=1+X+Z+XY+YZ+XYZ,\qquad q=3^a.
\]
All three terminal coordinates are retained. The six names/individual contributions remain available before endpoint aggregation. This observer calculation preserves frozen P000 X6/signed native semantics; it does not supply primitive Cell/Link/Port event permissions.

Antecedents:
- R762DN/R762DZ: for q=3^a>=9, d=q/3 and all n, the integer coefficient 3-valuation is at least max(0,floor(n/d)-2).
- R762EM (PR #2724 at b21958c0178439717e77947be3cfee43570533a6): q=9 has exactly 127 distinct character eigenvalues.
- R762EQ (PR #2731 at de0801418e293ceb056b9c5ca40a113379742588) already proves the q9 all-horizon result by a 729-order annihilator with 2,187 exact vector congruences.
- R762ER (PR #2734 at 39787270e99ef3c698f43409b208dbe16b073ebb) lifts that q9 result to every q>=9.

The new result independently supplies a shorter q9 finite witness using the 127-degree distinct-spectrum polynomial, together with a uniform eventual-period theorem. It does not reissue R762EQ or R762ER as a new scientific claim.

## Theorem A: a monic integral 3-adically rescaled annihilator for every q=3^a>=9

Let ζ be a primitive qth root, π=ζ−1, and let Λ_q be the SET of distinct values of
\[
\lambda_{ijk}=1+\zeta^i+\zeta^k+\zeta^{i+j}+\zeta^{j+k}+\zeta^{i+j+k}
\quad (i,j,k\in\mathbb Z/q).
\]
Set d=q/3, s_q=|Λ_q|, and
\[
D_q=P_q^d/3\in\mathbb Q[R_q],\qquad
F_q(T)=\prod_{\lambda\in Λ_q}(T-\lambda^d/3).
\]
Then F_q(T) is monic in \(\mathbb Z[T]\), degree s_q, and F_q(D_q)=0 in \(\mathbb Q[R_q]\).

Proof. Write x=X−1, y=Y−1, z=Z−1. The exact expansion is
\[
P=6+3(x+y+z)+2xy+xz+2yz+xyz.
\]
In \(K=\mathbb Q(\zeta_q)\), (3) is the unique prime ideal above 3 raised to ramification index 2d; π is a uniformizer. Every character evaluation satisfies x,y,z∈(π), hence λ∈(π²), and λ^d/3 has nonnegative valuation at the prime above 3. At every other prime, division by 3 is a unit. Consequently every λ^d/3 is an algebraic integer. The multiset of factors indexed by DISTINCT λ is Galois invariant because conjugation permutes Λ_q. Its symmetric coefficients are rational algebraic integers, hence ordinary integers. Each Fourier character evaluates D_q as λ^d/3, which is a root of F_q. Fourier injectivity in the rational group algebra gives F_q(D_q)=0. This argument permits repeated rescaled roots without requiring their distinctness. QED.

## Theorem B: a finite-state periodicity algorithm at every fixed q

Assume the established R762DN lower-divisibility lemma. For k≥2, 0≤r<d define integral group-ring vectors
\[
B_{k,r}=3^{2-k}P_q^{dk+r}\in R_q.
\]
They satisfy B_{k+1,r}=D_q B_{k,r} over the rational group algebra. The monic integer recurrence F_q(D_q)=0 therefore implies that each coefficient of B_{k,r}, reduced modulo 3, obeys a recurrence of order at most s_q.

Moreover the residue field of K at 3 is F_3. Let
\[
\overline{F_q}(T)=T^u(T-1)^v(T+1)^w,\qquad u+v+w=s_q
\]
in F_3[T]. Choose the smallest t≥0 with 3^t≥max(v,w), using t=0 if v=w=0. In characteristic 3,
\[
(T^{2\cdot3^t}-1)=(T^2-1)^{3^t},
\]
so F_q divides \(T^u(T^{2\cdot3^t}-1)\) modulo 3. It follows that
\[
\boxed{B_{k+u+2\cdot3^t,r}\equiv B_{k+u,r}\pmod3,\qquad k\ge2.}
\]
Thus, for each fixed q, the exact all-horizon 3-content question reduces to a finite characteristic-3 computation on a provably eventually periodic normalized BRC shadow. The explicit bound is a universal algorithmic bound, not a claim that it is the shortest possible period.

## Theorem C: q9 all-horizon content using only 381 exact vector equalities

At q=9, d=3 and s_9=127. For r=0,1,2, let
\[
V_{k,r}=3^{2-k}P_9^{3k+r},\quad k\ge2.
\]
The recurrence of Theorem A gives a monic INTEGER-coefficient order-127 recurrence in k, and hence the difference
\[
C_{k,r}=V_{k+6,r}-V_{k,r}
\]
obeys the same recurrence.

A separate exact full-729-cell BigInt path-count calculation, included as R762ES_VERIFY.mjs, verifies
\[
C_{k,r}\equiv0\pmod3
\quad\text{for every }r\in\{0,1,2\},\ k=3,\ldots,129.
\]
These are precisely 127 consecutive initial zero values for each residue class. Because the leading recurrence coefficient is 1 and all coefficients are integers, induction yields C_{k,r}≡0 for EVERY k≥3. Therefore
\[
\boxed{3^{2-\lfloor(n+18)/3\rfloor}P_9^{n+18}
\equiv3^{2-\lfloor n/3\rfloor}P_9^n\pmod3,\quad n\ge9.}
\]
For n=9,...,26, each of the 18 normalized vectors is nonzero; the companion evidence records their support cardinalities. Thus every normalized vector is nonzero for every n≥9.

For 0≤n≤8, the identity endpoint has coefficient exactly 1: all nonidentity branch steps increase some nonnegative coordinate and fewer than nine steps cannot wrap a coordinate modulo nine. Combined with the previously proved lower bound this gives
\[
\boxed{v_3(c_9(n))=\max(0,\lfloor n/3\rfloor-2)\quad(n\ge0).}
\]
The full integer content is the same power of 3. Indeed it divides augmentation 6^n. To exclude factor 2 for n≥1, take a nontrivial qth root z in an algebraic closure of F_2 (q odd), evaluate X=Y=1,Z=z: P_q maps to 1+z≠0, so P_q^n is not the zero element modulo 2. At n=0 its identity coefficient equals 1. QED.

## Certificate scope and savings

R762ES_VERIFY.mjs performs exact six-branch BigInt convolution on every one of 729 endpoints for n=0,...,407; it independently enumerates all 729 cyclotomic characters in the six-integer basis of \(\mathbb Z[\zeta_9]\), verifies 127 distinct eigenvalues and 60 zero characters, checks augmentation, lower divisibility, 18 nonzero base shadows, and compares actual 729-byte residue vectors (not merely their hashes) on 381 transitions. These finite checks, plus the monic recurrence theorem and the R762DN lower bound, yield an all-n proof. Relative to R762EQ's 729-order route, the initial comparisons drop from 2,187 to 381 (a 5.74× reduction); the final tested horizon drops from 2213 to 407.

The local BigInt program and its JSON evidence were run once with PASS. No formal proof checker or independent semantic review was executed. The result is a shorter second author certificate and a general finite-state tool, not a native P000 event rule.

## Next problems

1. Independently check the exact R762DN lower-bound lemma and the Frobenius induction of R762ER against the same pinned inputs, particularly the preservation of distinct residue-coset identities.
2. For q=27, use F_q modulo 3 and the embedded q9 shadows to reduce universal verification costs or construct a tight all-q period without full q^3 enumeration.
3. Determine the actual licensed signed TRIADIC_CLOSURE_E event language and V17/V29/V39 transport; preserve original Cell/Link/Port provenance until a future-operation-safe quotient is proved.
