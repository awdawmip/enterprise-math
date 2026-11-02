# D25 | Exact signed 216–2304 cutoff transport and the nonzero p² source strip (2026-11-03)

**Status:** AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF + FINITE INTEGER REPLAY / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. This author-side construction is not an authenticated Source checkpoint, accepted theorem, or native H0/B0 execution.

**Frozen context:** Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific input c47e13e4aba0e006366f989d6334d443f6333ae3. Logical Research lane chatgpt-research-onhour-enterprise-math-20260923, separate from maintenance. Predecessor author-side frontier 8ddead488745b4b0d1a73717aed869ac76613d9f.

## Selected mother goal and two exact source series

For primes p=13 or 19 modulo 24, the selected D25 goal is equivalent, by the existing source-aligned D24/Clausen bridge, to W(p−1)=p modulo p³, where

\[
a_k=(6k+1)\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k},\qquad W(N)=\sum_{k=0}^{N}a_k.
\]

The distinct published 2304 source is

\[
b_k=(8k+1)\frac{\binom{4k}{2k}\binom{2k}{k}^{2}}{2304^k},\qquad S(N)=\sum_{k=0}^{N}b_k.
\]

Guo–Zudilin (Adv. Math. 346, 2019, DOI 10.1016/j.aim.2019.02.008, https://arxiv.org/abs/1803.01830) proved S(p−1)=p(−3/p) modulo p³ for all p>3. In the target classes (−3/p)=+1. All calculations below take place in Z_(p), respecting the two different original weights, cutoffs, ordered k and denominators.

## Theorem 1: sharp source-specific valuation atlas

For every prime p≡13,19 (mod 24) and 0≤k<p, exactly

\[
v_p(a_k)=\left\lfloor\frac{2k}{p}\right\rfloor+
\left\lfloor\frac{3k}{p}\right\rfloor+
{\bf1}_{k=(p-1)/6},
\]
\[
v_p(b_k)=\left\lfloor\frac{4k}{p}\right\rfloor+
{\bf1}_{k=r_p},\qquad
r_p=\begin{cases}(5p-1)/8,&p\equiv13\ (24),\\
(3p-1)/8,&p\equiv19\ (24).
\end{cases}
\]

Proof. Since k<p and 4k<4p<p² for p≥13, Legendre's factorial formula gives v_p((jk)!)=floor(jk/p) for j=2,3,4, while k! and 216,2304 are units. The weight 6k+1 can be divisible by p only at k=(p−1)/6 in this interval. Solving 8k+1=ap with odd a∈{1,3,5,7}, by p modulo 8, gives the unique r_p above. Both weight factors have exactly one p-factor at those indices. QED.

Consequences: define L=floor(2p/3), H=floor(3p/4). Then
\[
a_k\equiv0\pmod{p^3}\ (k>L),\qquad b_k\equiv0\pmod{p^3}\ (k>H).
\]
For k in the **extra 2304 strip** L<k≤H, v_p(a_k)=3 while v_p(b_k)=2, so this strip is a genuine p² contribution of 2304 and zero in the 216 p³ observer. Moreover at k_0=ceil(p/4)<p/3, a_(k_0) is a p-unit but b_(k_0) is divisible by p. Consequently no same-index coefficientwise **p-unit diagonal gauge** a_k=u_k b_k modulo p can connect these two coefficient arrays. This last statement concerns that precise transfer class; mixed-index/convolution and elliptic-period mechanisms remain open.

## Theorem 2: explicit signed correction and recurrence

Let D_p=sum_{k=0}^{L}(a_k−b_k). Define the retained boundary port
\[
T_p=\sum_{k=L+1}^{H}\frac{b_k}{p^2}\ \in \mathbf F_p.
\]
Theorem 1 gives the **exact source-preserving transfer**
\[
W(p-1)-S(p-1)\equiv D_p-p^2T_p\pmod{p^3}.
\]
Using the published S(p−1)≡p, the frozen D25 goal is equivalent to the single precise signed obligation
\[
\boxed{D_p\equiv p^2T_p\pmod{p^3}.}
\]
The previously established D24 first-digit congruence W(p−1)≡p (mod p²), together with the published S, ensures D_p is divisible by p² on this task's frozen scope; hence the target can also be stated D_p/p²≡T_p (mod p). Divisibility is asserted from those explicitly stated predecessor results, not inferred from finite tests.

For L<k≤H put s=4k−2p (0≤s<p). Full p-block multiplication and Wilson's theorem yield the exact finite-field factorial identity
\[
\frac{(4k)!}{p^2}\equiv 2s!\pmod p,
\]
so
\[
\boxed{\frac{b_k}{p^2}\equiv
2(8k+1)\frac{(4k-2p)!}{(k!)^4\,2304^k}\pmod p.}
\]
It is an actual computable source port with unit denominators. For u_k=b_k/p² mod p within the strip, consecutive coefficients satisfy
\[
\boxed{u_{k+1}=u_k
\frac{(8k+9)(4k+1)(4k+2)(4k+3)(4k+4)}
{(8k+1)\,2304\,(k+1)^4}\pmod p.}
\]
The denominators are p-units for L<k<H: k+1<p and 8k+1 cannot be a multiple of p in (2p/3,3p/4) for these residue classes. The recurrence uses a single seed at k=L+1 from the preceding factorial expression. QED.

## Exact executable examples and a signed cancellation witness

A standard-library integer checker, independently using the original binomial terms, verifies all theorem formulas and the finite original W/S sums for the 77 target primes p≤2000. The latter W finite replay is not a universal proof. The following p² strip digits are exact:
- p=13: strip k=9, T_13=6, p²T=1014 (mod 13³);
- p=19: strip k=13,14, T_19=16, p²T=5776 (mod 19³);
- p=373: strip k=249..279, T_373=281, p²T=39095249 (mod 373³);
- p=1171: strip k=781..878, T_1171=724.
- p=181: strip k=121..135 has 15 individually nonzero p²-normalized terms, yet **T_181=0 (mod 181)** by signed cancellation.

In all 77 bounded cases the separately evaluated lower defect D_p/p² equals T_p. Exactly 76 of the 77 sampled strips have nonzero total; 181 is a concrete cancellation exception. Neither finding is extrapolated to all primes. The nonzero examples demonstrate that simply shortening the published 2304 sum to the 216 cutoff changes its p³ value, while the 181 example shows that nonzero source terms need not imply a nonzero total.

## Applied Enterprise Math/BRC source semantics

Resolution **COMPOSE_APPLIED**. Carrier: two *distinct* original weighted coefficient families, indexed by k with their individual p-valuations, source weights and cutoff bands. Observer: signed sum modulo p³, with future division by p². Preserve the cross-model defect D_p and independent boundary port T_p. The source-specific p² strip is not erased by a shared elliptic j-invariant, differential-gauge normalization, or a total-only evaluation; all such future transfer maps must account for it. This is external p-adic arithmetic used as an explicitly typed auxiliary representation, not a native-X6 spatial model.

## Next scientific unit, native debt and control provenance

Find a terminating WZ/contiguous or explicit period-transformation certificate for **D_p/p²=T_p**, preserving the two target residue classes, original (6k+1)/(8k+1) weights, source labels, p-adic denominators, and the exceptional signed cancellation at p=181. A possible discriminating start is to derive a finite-difference pair whose boundary term is precisely the displayed u_k strip recurrence; compare both k_0 (p/4 to p/3) and upper (2p/3 to 3p/4) defects. No proof of this final congruence is claimed here.

Native original p=373 H0/B0 divided-power rank, [X]U modulo 139129, semilinear eta, signed odd Green/Hesse/kappa and independent replay remain **NOT_EXECUTED / PENDING_OWNER**, tracked by existing issue #1559. The current read-only gateway reports research_authority_granted=false, source control CODE_REVIEW_REQUIRED and no authenticated native Research session; former target request research-onhour-20261031-0205-dispatch-r15 returned CONTROL_REQUEST_NOT_FOUND on current read. No old mutation was replayed. This GitHub author evidence is not a canonical Source checkpoint or independent mathematical admission.
