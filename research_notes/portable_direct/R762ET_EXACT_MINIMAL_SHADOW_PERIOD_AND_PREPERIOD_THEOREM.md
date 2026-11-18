# R762ET — Exact minimal eventual period and sharp transient for all three-power BRC terminal shadows

Date: 2026-11-18. Model scope: complete three-coordinate terminal observer of the six **named positive** BRC branches. Source lineage: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142, historical contributor EM-X6-3050F6. Portable mathematical continuation, not an assertion of current native CLAIM or Source publication. Independent review: NOT_REVIEWED.

## Precise statement

For every a >= 2, let q=3^a, h=q/9, d=q/3, and in R_q=Z[(Z/qZ)^3] put

\[
P_q=1+X+Z+XY+YZ+XYZ,\qquad
f_q(n)=\max(0,\lfloor n/d\rfloor-2).
\]

Define the complete terminal shadow
\[
S_q(n)=[3^{-f_q(n)}P_q^n]_3\in\mathbf F_3[(\mathbf Z/q\mathbf Z)^3]\quad(n\ge0).
\]
Its integrality and nonvanishing at every n follow from the antecedent author proof R762ER. An *eventual period* is an integer T>0 for which S_q(n+T)=S_q(n) for every sufficiently large n. For a fixed period, the *preperiod* is the least nonnegative N for which this equality holds for all n>=N.

**Theorem.** Among all eventual periods of S_q, the least is exactly
\[
\boxed{T_q=18h=2q.}
\]
Indeed every eventual period is a positive multiple of 2q. For all such periods, the least possible preperiod is exactly
\[
\boxed{N_q=8h=\frac{8q}{9}.}
\]
Equivalently,
\[
S_q(n+2q)=S_q(n)\quad\text{for all }n\ge8q/9,
\]
but the equality fails at n=8q/9-1; no different eventual period starts earlier.

This sharpens R762ER's period 2q beginning at n>=q by h=q/9 steps, and establishes minimality of both the period and transient. The theorem concerns all q^3 terminal coefficients, not a scalar return sequence or a native signed-event evolution.

## Dependency and finite q9 certificate

R762ES (PR #2737, immutable head dcabed39ebc28b1377521d8732ca4312c159f239) proved S_9(m+18)=S_9(m) for every m>=9 using the 127-degree monic spectral annihilator and 381 exact vector equalities.

The new independent finite computation with the original six named BRC shifts works entirely in Z/3^7 Z, 729 coefficient positions, n=0,...,26. Here f_9(n)<=6, so 3^7 retains all needed normalized residues. It verifies:

1. Full 729-component equality S_9(8)=S_9(26). Equivalently P_9^26-3^6 P_9^8 is coefficientwise divisible by 3^7. The common normalized-vector SHA256 is 3f5db6486169453804d0fdda1218458a461679c73f691493e3508c8da6ab73a1.
2. S_9(7) != S_9(25): the identity-endpoint normalized residues are respectively 1 and 0. Their support sizes are 108 and 450.
3. The support sizes at m=9,...,26 are exactly
   [27,162,486,717,108,324,525,522,468,18,108,324,519,360,468,237,450,324].
   The value 27 occurs only at m=9 in one full 18-state cycle.

Therefore S_9(m+18)=S_9(m) for m>=8. The unique support 27 among the 18 stable positions shows that **any** eventual period of the q9 sequence is divisible by 18. Its least preperiod is exactly 8: the comparison at m=7 vs m=25 fails, and the latter lies on the stable 18-periodic tail.

Companion exact code: R762ET_VERIFY.py; complete machine-readable observations: R762ET_EVIDENCE.json. The code uses direct named-branch convolution; no floating-point/trigonometric/continuous substitution or character approximation.

## All-q lift and residue-class observability

R762ER (PR #2734, immutable head 39787270e99ef3c698f43409b208dbe16b073ebb) established for q=9h, n=hm+r with 0<=r<h:

\[
S_q(hm+r)=\iota_h(S_9(m))\,\overline P_q^{\,r},
\]
where \(\iota_h:\mathbf F_3[G_9]\hookrightarrow\mathbf F_3[G_q]\) maps each coordinate generator to its h-th power, and \(\overline P_q=P_q\bmod3\).

Here is a direct observer that also determines the low-digit exponent r. Let H=(hZ/qZ)^3, and for s=0,...,h-1 project a vector onto the H-coset whose coordinate residues modulo h are (s,0,0). For every u != 0 in F_3[G_9] and every 0<=r<h, the projection of \(\iota_h(u)\overline P_q^r\) is

\[
\operatorname{proj}_{(s,0,0)}\!\left(\iota_h(u)\overline P_q^r\right)
=\begin{cases}
\binom rs X^s\iota_h(u),& 0\le s\le r,\\
0,&r<s<h.
\end{cases}
\]

Proof: each of the r steps contributes a nonnegative increment in every coordinate; since r<h, a terminal Y or Z residue zero modulo h requires all Y and Z increments zero. Of the six named branches, precisely 1 and X satisfy this. Among those, exactly s of r steps must be X. In particular, the projection at s=r equals X^r iota_h(u), nonzero, while all s>r projections vanish.

Consequences: (i) r is the maximal s with nonzero (s,0,0) projection; (ii) for fixed r, the map u -> iota_h(u) P_q^r is injective; (iii) if two nonzero lifted shadows are equal, their residue digits r must agree.

The q9 period beginning at m=8 and the R762ER factorization immediately give S_q(n+18h)=S_q(n) for every n>=8h.

Conversely, let T be any eventual period of S_q. Choose a sufficiently late n divisible by h; its residue digit is r=0. The equality with S_q(n+T), plus (iii) and nonvanishing of all q9 shadows, forces T=ht for a positive integer t. Applying the equality to n=hm sufficiently large and using injectivity yields S_9(m+t)=S_9(m) on a tail. From the unique support-27 position in the q9 cycle, 18 divides t. Hence 18h divides T: **2q is the exact least eventual period**.

Finally, for any such T=18hk, k>=1, put n_*=8h-1=7h+(h-1). The factorization compares
\[
S_q(n_*)=\iota_h(S_9(7))\overline P_q^{h-1},\qquad
S_q(n_*+T)=\iota_h(S_9(7+18k))\overline P_q^{h-1}.
\]
Because 7+18k>=25 lies in the stable q9 tail, S_9(7+18k)=S_9(25). The finite certificate gives S_9(7)!=S_9(25), and injectivity for r=h-1 preserves the inequality. Therefore every eventual period fails at n_*, whereas 2q succeeds for all n>=8h. This proves the sharp preperiod claim.

## Evidence and status

- Frozen scientific model: six named positive terminal BRC branches, full three-coordinate group ring; no unsigned-to-signed identification.
- Prior proof dependencies: R762ES period theorem and R762ER Frobenius-lift/nonzero theorem, both author-side and NOT_REVIEWED. The new minimality proof is conditional on their exact statements and inputs.
- New exact computation: 27 lengths, 729 coefficients each, modulus 3^7, 27 lower-bound/nonzero/mass checks; one 729-coordinate period equality, one explicit endpoint failure, one unique-support period witness.
- Author-side result: PASS. Independent semantic review: NOT_REVIEWED. Formal checker: NOT_PERFORMED.
- No claim about primitive TRIADIC_CLOSURE_E permissions, native X6 Cell/Link/Port events, V17/V29/V39 transport, or full future-operation-safe quotient. P000 remains locked.

## Next research

1. Use the sharp transient 8q/9 and minimal period 2q to design a compressed random-access normalized-shadow oracle; report input/output reconstruction costs rather than just abstract O(1) lookups.
2. Independently audit the load-bearing R762ES monic-annihilator computation and the R762ER residue-coset lift, especially their use in the period start.
3. Identify native signed Cell/Link/Port data and legal update rules for a provenance-preserving lift beyond positive terminal coefficient aggregation.
