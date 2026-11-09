# D25 — Source-normalization identifiability certificate for the frozen p=373 H0/B0 benchmark

Date: 2026-11-09 (Asia/Hong_Kong).
Author-side mathematical diagnostic for TASK_RESEARCH, logical Research lane `chatgpt-research-onhour-enterprise-math-20260923` (never the maintenance lane).
Parent: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific input Source `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Status: **AUTHOR-SIDE EXACT CONDITIONAL CERTIFICATE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**.

## Research question and actual mother interface

The still-open native benchmark #1559 requests the **same-original-class**, fixed H0/B0 divided-power module at p=373, coefficient `[X]U mod 139129`, rank, genuine semilinear Frobenius direction, normalization `eta`, signed odd Hesse/Green observer, native kappa, and original `Delta_p-R_p`. Earlier source work proposed a conditional comparison to the *ordinary external Hesse* candidate `a=92060+21788*T`, with `T^2=2`. This note decides whether the norm of such a candidate is a discriminating reference **before** the native source normalization is fixed. It does not supply the missing native evaluator or a native result.

The p=373 ordinary candidate is inherited evidence, not rediscovered or promoted here. The source tag is `ORDINARY_HESSE_CANDIDATE`, not `ORIGINAL_NATIVE_FROBENIUS`.

## Theorem A — unramified norm surjectivity and unit ambiguity

Let p be any odd prime with `(2/p)=-1` (in particular target p≡13,19 mod24), and
$$
R_r=(\mathbb Z/p^r\mathbb Z)[T]/(T^2-2),\quad
\sigma(T)=-T,\quad N(u)=u\sigma(u).
$$
For every r≥1 the norm map `N:R_r^× → (Z/p^r)^×` is surjective, and every target unit has exactly `(p+1)p^(r-1)` preimages.

**Proof.** Mod p, `R_1=F_(p²)` and its norm is `x↦x^(p+1)`, onto `F_p^×` by cyclicity. Suppose a solution modulo p^r is lifted arbitrarily to `R_(r+1)`; its norm has the correct residue modulo p^r. If the needed multiplicative correction is `1+p^r d`, multiply the lifted element by the **central base scalar** `1+p^r d/2`. Its norm is `(1+p^r d/2)^2=1+p^r d (mod p^(r+1))`; induction proves surjectivity. Counting units,
$$
|R_r^×|=(p^2-1)p^{2r-2},\qquad
|(\mathbb Z/p^r)^×|=(p-1)p^{r-1},
$$
gives the stated uniform fiber size. QED.

**Identifiability consequence.** If a native purported rank-one `F=a σ` is compared to `N(eta) N(a)` but `eta∈R_r^×` is left unconstrained by the original H0/B0 source, then any **unit** target for `F²` can be matched by choosing eta after seeing it. Thus that bare equality, without a native pinned eta, cannot certify an identification of operators. Source-derived, independently fixed eta and operator/basis map are required. This is a precise nonidentifiability result for the *unit-rank-one comparison* only, not a no-go for native H0/B0 itself.

## Theorem B — scalar coefficient gauge obstruction

For a rank-one sigma-semilinear operator `F_a(v)=a σ(v)`, an actual basis change `v↦u v` sends `a↦u^(-1)a σ(u)` and leaves `N(a)` invariant. If some such gauge makes its coefficient a **base scalar** `c∈(Z/p^r)^×`, then `N(a)=c²`; hence the reduction of `N(a)` modulo p must be a quadratic residue. (The reverse implication when a square root exists follows from the previously proved finite-ring Hilbert 90 gauge theorem; it is not needed for this obstruction.)

In particular a source normalization **multiplying** a by an eta is not the same operation as a basis gauge: its norm changes by `N(eta)`. Preserve these two operation tags separately.

## p=373 exact discriminating witness

Use integer arithmetic in `R_2`, p=373 and p²=139129. The previously author-reported ordinary Hesse source candidate is
$$
a=92060+21788 T.
$$
Direct multiplication:
$$
N(a)=92060^2-2(21788)^2\equiv122102\pmod{139129},
\qquad N(a)\bmod373=131.
$$
Euler checks give `2^186 mod373=372` and `131^186 mod373=372`. The first is the coefficient-field inert condition; the second establishes that 131 is a **quadratic nonresidue**. Therefore **no rank-one basis gauge makes this ordinary Hesse candidate's sigma-semilinear coefficient base-valued modulo 373 or 139129**.

However, the independently explicit multiplier
$$
\eta=89901+6579T
$$
satisfies
$$
a\eta=1\pmod{139129},\qquad N(\eta)=18818,\qquad
122102\cdot18818\equiv1\pmod{139129}.
$$
Thus, if eta were allowed to be chosen freely, its norm could make a proposed unit-norm comparison equal to 1 even though no basis gauge makes a itself base-valued. This is the concrete ambiguity the authentic native normalization must resolve.

The actual p=373 sigma-semilinear **matrix of the candidate** in the external coefficient basis (1,T), mod p, is
$$
M_a=\begin{pmatrix}302&65\\154&71\end{pmatrix},
\qquad\det M_a\equiv242\pmod{373}.
$$
This is an invertible **external candidate**; it is not the original whole-E3 crystalline Frobenius matrix. The separate previously published odd-valuation obstruction to identifying a unit-rank-one unramified module with the *whole* geometric supersingular E3 remains in force.

## Reproducible exact exhaustive checks

The companion Python standard-library checker `research_notes/portable_direct/d25_norm_eta_identifiability_20261109.py` was actually executed locally (no floating point). It enumerates all `13^4=28561` and `19^4=130321` elements at r=2 and checks every norm fiber. In p=13, all 156 base units have exactly 182 preimages, zero has 169 preimages, and every nonzero multiple of p has none. In p=19, all 342 base units have exactly 380 preimages, zero has 361, other p-multiples have none. This exactly matches Theorem A. It independently checks the p373 residues, explicit eta and matrix determinant. This finite enumeration certifies the listed finite rings; the all-r statement uses the proof above.

## BRC residual and actual next action

**Carrier** = (original frozen Task/source class; module rank and semilinear direction; operator F; selected coefficient-basis/gauge u; independently source-fixed normalization eta; p-adic precision p²; odd signed observer; provenance). **Observer** = original `[X]U`, `F²`, kappa and Delta-R. **Future operation** = semilinear composition and signed second-digit extraction. Arbitrary eta insertion loses source identifiability; discarding sigma, odd port or precision cannot preserve the observer.

This certificate permits a stricter **input validation** for #1559 when a native H0/B0 computation arrives: demand the original source formula and pin for eta *before* norm/F² comparison; distinguish basis gauge from multiplication; retain a matrix if module rank is not one, and preserve odd Hesse/Green sign and original Delta-R. Native evaluation remains **NOT_RUN / PENDING_OWNER**, unchanged.

No Source CLAIM/open/Result, native execution or mathematical admission is claimed. Do not repeat prior finite field source checks or treat this certificate as the missing H0/B0 experiment.
