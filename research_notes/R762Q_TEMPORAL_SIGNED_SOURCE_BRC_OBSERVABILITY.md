# R762Q — Temporal observability of the three-source parity residual

**Status:** Author-side exact theorem and exhaustive finite certificate; independent candidate-model research, not a formal native Result and not a P000 amendment.
**Date:** 2026-11-14 (Asia/Shanghai)
**Parent line:** RS-X6-TRIADIC-CLOSURE-DYNAMICS; builds on the exact three-source signed BRC observer setting of R762M, R762N, R762O and R762P.
**Frozen scientific reference:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 and source foundations unchanged).
**Source scope:** three named signed force-source labels in the *candidate observer model*. This work does not postulate that an affine source-sign update is a legal TRIADIC_CLOSURE_E Cell/Link/Port event.

## 1. Question and definition

R762M exhibits two disjoint three-source Boolean admission laws that have identical complete two-source counts. Can several **temporally ordered** observations resolve the ambiguity, if the labels evolve under explicit reversible candidate operations?

Let V=F_2^3. A Boolean admission law is f:V->{0,1}; there are 2^8=256 such laws. Each source sign bit is **named**, and no coordinate, provenance or future operation is silently discarded.

For j=0,1,2, define four unweighted two-source marginals

    M_j(f)(t)=f(t with bit j=0)+f(t with bit j=1), for t_j=0.

These are the R762M BRC hidden-source counts divided by their fixed multiplicity factor 4; scaling by 4 preserves all equalities and distinctions. The complete one-time observer M consists of 12 integer measurements, each in {0,1,2}.

For an affine reversible candidate update U(x)=Ax+b, A in GL(3,2), b in V, define the transported law by U_*f(y)=f(U^{-1}y). The temporal observation is (M(f), M(U_*f)). This transports the *entire named law*, not just a coordinate or positive mass.

## 2. First-time ambiguity and its exact size

For any difference d=f-g viewed as an integer-valued function, M_j(d)=0 means d(x+e_j)=-d(x). Holding for every j implies uniquely

    d(x)=c (-1)^(x_0+x_1+x_2).

Conversely every such function is killed by every M_j. Therefore ker(M) is the one-dimensional parity-character line over the rationals. For Boolean f,g, a nonzero c must be +1 or -1, and the pair is precisely

    f_even(x)=[x_0+x_1+x_2=0 mod 2]
    f_odd(x) =[x_0+x_1+x_2=1 mod 2].

Their bit masks, indexing a truth table by x=0,...,7, are 105 and 150. Exactly 255 of the 256 Boolean laws have distinct one-time M signatures. This reuses R762M at its exact scope.

## 3. Main theorem: two measurement rounds and the parity-preservation criterion

**Theorem R762Q.** The pair of full BRC observation rounds (M(f),M(U_*f)) distinguishes all 256 Boolean admission laws if and only if

    A^T (1,1,1)^T != (1,1,1)^T   over F_2.

When equality holds, the two complementary parity laws remain observationally indistinguishable. A single full observation round, even after any invertible affine update, always has 255 signatures, so **two rounds are the global minimum within this observation architecture**.

**Proof.** Any two laws colliding in the first round must differ by c chi(x), with chi(x)=(-1)^(1·x). Under U,

    U_*chi(y)=(-1)^[ (A^(-T)1)·(y-b) ].

A nonzero signed character chi_q has all its coordinate-pair marginals zero if and only if q_j=1 for all j. Thus the second observation also kills the difference exactly when A^(-T)1=1, equivalent to A^T1=1. Otherwise it distinguishes the only possible first-round collision. Since an invertible affine update merely permutes the 256 Boolean laws, every individual M(U_*f) has the same 255 one-time signatures; at least two distinct rounds are necessary. QED.

**Adaptive/infinite-horizon corollary.** Suppose at each time an observer may choose its next affine update from a group G of parity-preserving maps A^T1=1, based on all previously seen two-source marginals. The even and odd laws produce identical observations at every finite stage, by induction: equal past observations imply identical chosen actions, compositions preserve parity, and each marginal kills the transported parity difference. Thus no finite or infinite adaptive schedule composed only of those maps resolves the missing parity bit. A parity-breaking update, followed by a new full marginal observation, resolves it in a single additional round.

This is a statement about **information under the specified update alphabet**, not a claim about all possible X6 native dynamics.

## 4. Exact count of candidate update classes

| Set | Count |
| --- | ---: |
| GL(3,F_2) | (8-1)(8-2)(8-4)=168 |
| Reversible affine maps AGL(3,F_2) | 168*8=1344 |
| Parity-preserving linear maps A^T1=1 | 168/7=24 |
| Parity-preserving affine maps | 24*8=192 |
| Parity-revealing affine maps | (168-24)*8=1152 |
| Coordinate permutations and independent sign flips | 3!*8=48 |

The 24-element stabilizer follows from the transitive action of GL(3,2) on the seven nonzero dual vectors. The usual signed-source relabeling and independent sign-flip subgroup (48 maps) lies strictly inside the 192 parity-preserving maps. Therefore observing for arbitrarily long time under only independent sign flips and permutations cannot recover the parity relation.

## 5. Explicit minimal revealing candidate

Take the invertible binary shear

    U(x_0,x_1,x_2)=(x_0+x_1,x_1,x_2)  mod 2.

Then an old parity law is transported to a predicate of y_0+y_2. It becomes independent of the *visible-state coordinate y_1*, so M_1(U_*f_even) takes values (2,0,0,2), whereas M_1(U_*f_odd) takes (0,2,2,0), in the canonical truth-table order. The other eight marginal measurements remain 1. Hence two rounds recover the full Boolean law.

This shear is a **candidate source-mixing readout/update**; its admissibility as a P000-compatible, typed TRIADIC_CLOSURE_E event remains open. Source labels and the post-event mapping are explicitly retained.

## 6. Reproduction

Run Python 3 standard library:

    python research_artifacts/R762Q_TEMPORAL_BRC_OBSERVER.py

The script exhausts all 3x3 binary invertible matrices (168), all affine translations (8), and all Boolean laws (256) for every affine map. It compares actual integer marginal signatures and checks the analytic criterion; it also checks the one-time collision, CNOT witness and the 48 signed-coordinate relabelings. Output is the independently stored JSON certificate at research_artifacts/R762Q_TEMPORAL_BRC_OBSERVER_EVIDENCE.json. No floating-point arithmetic, external dependency or stochastic testing is used.

This finite enumeration verifies the 3-source instance. The kernel and affine criterion are proved algebraically. No physical-time experiment, V29 ledger computation, V39 holonomy readback, original event-predicate admission, or independent mathematical Driver review was performed.

## 7. Link to the parent objective and next discriminating step

The Task hard target is a typed X6 Cell/Link/Port TRIADIC_CLOSURE_E event, with first and repeated event admission, V29 PASS/TRANSFER and V39 transport. This theorem supplies a concrete fork for *the real event's signed-source transition law*:

1. Derive from the actual event, without guessing, whether an induced reversible sign-state transport exists and whether it preserves the all-sources parity functional.
2. If every admitted transition is parity-preserving, prove the one-bit BRC residual survives **all** allowed temporal tests in this observer family; then a provenance or explicitly symmetry-breaking observer is necessary.
3. If an admitted update changes the dual parity functional, run the two-round observer construction on the **actual event alphabet**, retaining source identities and the Cell/Link/Port state.
4. Compute V29 PASS/TRANSFER and V39 effects on those actual trajectories, not on a purely algebraic sign shear.

The frozen P000 constraints hold: six X6 spatial axes and independent time, PERP_E at native 120 degrees, a minimum triadic primitive balance, composite paths with provenance and no identification of parity-bit algebra with force cancellation. R762Q is a sharp **temporal observer theorem under typed candidate assumptions**; it does not imply full TRIADIC_CLOSURE_E dynamics have been constructed.
