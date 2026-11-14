# PREFIX-769 / R6 — Pointwise Gamma mixed-curvature certificate and a 1e-8 stationary bracket

Date: 2026-11-14. Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Status: AUTHOR_ANALYTIC_PROOF_AND_EXACT_INTEGER_RECALCULATION / UNREVIEWED / NOT_ADMITTED.
Scope: **external** 189-layer killed-Pascal BRC stopping / independent Gamma-clock maximum auxiliary, not the native X6-time dynamics. This note continues PREFIX-760–768 without reopening frozen P000 or claiming an additional 1/768 comparator exclusion.

## Theorem 769.1 — pointwise ratio gives a global mixed-phase upper bound

Let s_i(x)=Pr(T_x>i) (0<=i<=188) be the frozen 189-layer survivor polynomials, and C_x|T_x=m have the independent Gamma(m,1) law. Set Y(p,z)=max(C_p,C_z), mu(p,z)=E[Y], M_2(p,z)=E[Y²], W(p,z)=Var(Y), and V_q=q²W-q mu.

Use the exact kernels from PREFIX-760,
\[
K_{ij}=\binom{i+j}{i}2^{-i-j-1},\qquad L_{ij}=(i+j+1)K_{ij}.
\]
Write d(x)=s'(x), e(x)=s''(x). The frozen positive row-25 witness ensures the relevant mixed-mean derivative coefficient is strictly positive in the current interior domain:
\[
A(p,z)=d(p)^T K d(z)>0.
\]
By direct differentiation of the finite exact moment formulas,
\[
\mu_{pz}(p,z)=-A(p,z).
\]
Writing B(p,z)=d(p)^T Ld(z) and v_p=\mu_p, v_z=\mu_z, the variance mixed derivative is
\[
W_{pz}(p,z)=-D(p,z),\quad
D(p,z)=B(p,z)+2v_pv_z-2\mu(p,z)A(p,z).
\]
Consequently
\[
(V_q)_{pz}(p,z)=q[A(p,z)-q D(p,z)].
\]

**Claim.** At any interior rational point (p,z) with A>0 and D>0, define Q(p,z)=A(p,z)/D(p,z). If q>Q(p,z), then there exists a nondegenerate rational rectangle near (p,z) with strictly negative mixed difference of V_q. Therefore the PREFIX-763 global nonnegative mixed-difference phase threshold satisfies
\[
0<q_c\le Q(p,z).
\]

**Proof.** q(A-qD)<0 at the given point. The finite polynomial derivatives are continuous, hence remain negative on a sufficiently small neighborhood. Integrating (V_q)_{pz} over any rational subrectangle of that neighborhood gives a strictly negative mixed difference. Since q>Q(p,z) is arbitrary, the global phase threshold is at most Q(p,z). The previously established positive lower bound for q_c is inherited unchanged. QED.

This approach produces a certified global threshold bound directly from an exact pointwise ratio, without constructing a tiny explicit finite rectangle each time. Existence of a negative rational rectangle is rigorous, though no additional grid cell has been enumerated.

## Theorem 769.2 — new strict rational upper bound

On the diagonal p=z=u, set
\[
m=2{\bf1}^T s-s^TKs,\quad
v={\bf1}^Td-d^TKs,\quad A=d^TKd,\quad B=d^TLd,\quad
D=B+2v^2-2mA.
\]
Use u=5029714/100000000. Reconstruct the frozen killed-Pascal width predicate using W=2^18 and N=189, and evaluate the 189-by-189 K,L contractions with integer arithmetic and exact common denominators. The standalone checker establishes A>0, D>0 and the exact cross-product inequality
\[
\boxed{
0<q_c\le Q(5029714/10^8)
<\frac{28518591162858}{10^{15}}
=0.028518591162858.
}
\]
The pointwise Q decimal display, rounded only after comparison, is
0.0285185911628576750974116362406607443266469003.
This improves PREFIX-768's upper bound 0.028518591163. In conjunction with PREFIX-762's positive mixed-rectangle witness, every real q >= 0.028518591162858 has both mixed-difference signs.

## Theorem 769.3 — tenfold narrower diagonal stationary existence bracket

For Q(u)=A(u)/D(u), the exact diagonal derivative formulas are
\[
A'=2e^TKd,\quad B'=2e^TLd,\quad v'={\bf1}^Te-e^TKs-A,\quad
D'=B'+4vv'-4vA-2mA'.
\]
Therefore sign(Q')=sign(A'D-AD') on D>0. The checker evaluates this sign by exact integer cross products at denominator 10^8, yielding
\[
Q'(5029714/10^8)<0,\qquad Q'(5029715/10^8)>0.
\]
The whole bracket is contained in [251/5000,252/5000], where PREFIX-767 previously established D>27787. Hence the intermediate-value theorem yields
\[
\boxed{\exists u_*\in(5029714/10^8,5029715/10^8):Q'(u_*)=0.}
\]
The bracket width is 10^-8 versus PREFIX-768's 10^-7. No uniqueness or global-minimum assertion is needed for the upper bound.

## Executed verification, evidence scope and continuation

The independent author-local checker reconstructed 189 rows, confirmed exactly 9,529 nonzero survivor coefficient positions and the empty final row, evaluated the listed derivative signs and both A,D positivity checks with arbitrary-precision integers, and verified the strict q upper bound with cross multiplication. It returned ALL_CHECKS_PASS PREFIX769.

Portable reproduction: run Python 3 standard library file research_notes/portable_direct/PREFIX769_R6_POINTWISE_PHASE_CHECK.py. The published JSON research_notes/portable_direct/PREFIX769_R6_POINTWISE_PHASE_RESULTS.json records the exact rational bracket, integer-checked inequality and display-only decimal.

The code reuses the previously source-verified PREFIX-768 kernel implementation; this is an author computation and analytic reduction pending independent mathematical review. The stationarity argument reuses PREFIX-767's full-interval denominator bound. There is no claim of native X6 transfer or changed P000, nor of newly excluded 1/768 area.

Next discriminating questions: (i) certify uniqueness/nondegeneracy of the stationary zero via an exact interval polynomial/Bernstein/Sturm argument over the isolated rational bracket; (ii) determine whether an off-diagonal point has Q(p,z) below this diagonal candidate, and whether the global q_c is attained on or off the diagonal; (iii) use the exact K,L kernels on one genuinely unresolved comparator cell without assuming variance monotonicity.

Owner/Task status and native CLAIM are separate from this independent scientific publication; the current shared-owner authorization must be freshly checked before any shared task mutation.
