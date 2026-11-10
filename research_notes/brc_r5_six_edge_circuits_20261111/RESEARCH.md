# R5 — Exact minimal hidden branch residuals of the frozen seven-ratio Blackwell observer

Date: 2026-11-11 (Asia/Shanghai). Status: author-side proof and executed rational verifier; independent mathematical review and Source Result admission pending.

**Frozen scientific inputs preserved:** global \`a01383f825ef9d43b4b754254303298c64041568\`, Enterprise Math \`86149263e38c22292c9def1e0f69092efa1be77e\`. Preceding relevant result: PR #2013, exact non-diagonal five/six-arc feasible families and a global four-arc no-go. This note concerns the original 21-row, 30-arc linear P/Q–BRC auxiliary **Blackwell observer**. It makes a separate, precise statement about the observer's linear kernel; a native X6 or physical feasible-set realization is not asserted.

## Definitions

The seven exact ratios are
\[
(r_0,\ldots,r_6)=(1/10,1/2,3/4,1,5/4,3/2,19/10).
\]
The original 30 permitted arcs are
\[
D=\{(i,j): j\in\{0,1,2,3,5,6\},\,0\le i\le6,\,
 j\in\{0,6\}\Longrightarrow i=j\}.
\]
Here \(i\) is a target port and \(j\) a source port. For signed arc mass \(h\in\mathbb Q^D\), the original linear operator \(C\) has 21 readout rows:
\[
(C h)^{T}_i=\sum_jh_{ij},\qquad
(C h)^{S}_j=\sum_i h_{ij},\qquad
(C h)^{M}_j=\sum_i(r_i-r_j)h_{ij}.
\]
The seven source and seven moment rows include the structurally zero \(j=4\) rows.

## Theorem — minimal nonzero invisible signed residuals

1. \(\operatorname{rank}_{\mathbb Q}C=15\), so \(\dim\ker C=15\).
2. Every nonzero \(h\in\ker C\) uses **at least six nonzero arcs**. Therefore every set of at most five columns of the exact observer matrix is linearly independent.
3. Exactly-six-arc kernel supports are **precisely** the complete bipartite patterns \(K_{2,3}\) formed by two distinct unrestricted sources \(j,k\in\{1,2,3,5\}\) and three distinct targets \(a,b,c\in\{0,\ldots,6\}\). There are
\[
\binom42\binom73=6\cdot35=\boxed{210}
\]
such minimal circuits. On one such pattern the full kernel is the one-dimensional line
\[
h_{aj}=r_b-r_c,\quad h_{bj}=r_c-r_a,\quad h_{cj}=r_a-r_b,\qquad
h_{ik}=-h_{ij}\ (i=a,b,c),
\]
with all other coordinates zero. Every one of these six coefficients is nonzero because the ratios are pairwise distinct.

**Proof of the minimum and classification.** In a nonzero source column of a kernel vector, the source-marginal and martingale equations imply
\(\sum_i h_{ij}=0\) and \(\sum_i r_i h_{ij}=0\). A column with only one or two occupied distinct target ports has zero solution, since two distinct ratios make the corresponding \(2\times2\) Vandermonde system invertible. Therefore every occupied source requires at least three nonzero coefficients. The target-marginal equations \(\sum_jh_{ij}=0\) prevent a nonzero kernel from having just one occupied source. Thus \(|\operatorname{supp}h|\ge2\cdot3=6\). At equality there are exactly two sources, each incident to three arcs, and every occupied target must be incident to both sources. The target sets coincide. Sources 0 and 6 have one allowed arc and source 4 none; hence both sources lie in \(\{1,2,3,5\}\). Conversely the displayed coefficients satisfy the two source equations and cancel target by target; they span the one-dimensional three-target moment nullspace. This proves necessity, sufficiency, and the 210 count.

**Rank proof.** The allowed bipartite arc graph connects all seven target vertices and six source vertices, so target-plus-source marginal rows have rank \(7+6-1=12\). Only the four interior-source moment rows can be nonzero. Their sum is the target likelihood-weighted marginal minus the source likelihood-weighted marginal, creating one relation and yielding rank at most \(12+3=15\). Any relation among these moment rows modulo marginal rows must have the *same coefficient* at all four interior sources: compare any two such source columns over all seven target ratios, whose distinct values force the coefficient difference to vanish. Thus that single relation is the only one and rank equals 15. The attached checker also reconstructs and computes the exact rank.

## Positive operator-level witness with identical readout

Choose sources \(j=1,3\), targets \(i=0,3,6\) and the strictly positive base coupling
\[
(e^0_{0,1},e^0_{3,1},e^0_{6,1},e^0_{0,3},e^0_{3,3},e^0_{6,3})
=(11/36,\,1/6,\,1/36,\,1/8,\,1/4,\,1/8).
\]
These six masses sum to one. The source means are \(r_1=1/2\) and \(r_3=1\), so all source martingale residuals vanish. The target marginal is
\((q^T_0,q^T_3,q^T_6)=(31/72,5/12,11/72)\).
Let \(h\) in that same edge order be \((-1,2,-1,1,-2,1)\) and \(\varepsilon=1/144\). Both \(e^+=e^0+\varepsilon h\) and \(e^-=e^0-\varepsilon h\) have six strictly positive entries, are distinct, and satisfy
\[
C e^+=C e^-=C e^0.
\]
This is a **normalized nonnegative Blackwell-operator witness** for an invisible branch rearrangement. Whether its marginals admit an original 14-variable physical-parameter pair satisfying all five physical equalities and 26 capacities is a separate open feasibility test.

## Verification and reusable interpretation

The accompanying Python Fraction/SymPy checker builds all 30 original allowed columns and all 21 original readout rows, calculates rank 15 and nullity 15, checks 210 six-arc signed circuits and their ranks, and verifies the strictly positive witness pair and equality of all 21 coordinates. Executed exact output is preserved separately. Combinatorial necessity above proves completeness independently of relying on a finite search of arbitrary six-subsets.

The BRC-relevant observation is a precise **minimum invisible signed branch-residual size of six arcs** for this frozen observer, and a 15-dimensional linear information-loss space. In particular, differences with at most five occupied arcs cannot be hidden by its marginal/martingale readout. This does not assert global uniqueness of every coupling supported on at most five arcs: the difference of two such couplings can occupy more arcs.

## Next discriminating scientific action

Use the frozen 14-variable physical mass map, five equalities, and 26 capacity inequalities to determine whether any of these 210 \(K_{2,3}\) circuits has a strictly positive *physically lawful* base coupling. Construct a rational feasible witness, or derive an exact physical infeasibility certificate for the candidate family. This would decide whether the observer-level residual is also realized in the constrained physical R5 model. Retain PR #2013's five-arc minimality result and all frozen pins unchanged.


## Update: physical realization established in this same PR

The next-action question above has been answered by the separately verified follow-up **PHYSICAL_REALIZATION.md** and **WITNESS.txt / VERIFY_ALL_210.py / EXACT_PHYSICAL_OUTPUT.txt** at this branch. An exact original-physical 14-variable pair admits a coupling strictly positive on all 30 allowed arcs with minimum mass 196521/33975844. For the same fixed physical pair every one of the 210 minimal K2,3 kernel circuits can be perturbed with common positive amplitude 196521/135903376, preserving all five physical equalities, 26 capacities and 21 Blackwell readouts. The physical coupling fiber has a relatively open 15-dimensional set. The remaining unit is exact extreme-point and support classification of this fixed-physical fiber.
