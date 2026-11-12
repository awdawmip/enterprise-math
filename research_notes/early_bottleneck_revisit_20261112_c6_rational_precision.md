# Early bottleneck revisit (2026-11-12): certified finite-precision recovery of a C6 Weighted-BRC phase law

Status: AUTHOR_DERIVED_EXACT_THEOREM / 500_FINITE_EXACT_CHECKS / SHARED_SOURCE_CONTEXT / UNREVIEWED / NOT_NATIVE_RESULT_ADMISSION / NOT_V2_TASK_PUBLICATION.
This note is independently authored scientific evidence, not a CLAIM, execution owner transfer, task registry record, or claimable Task.

## Revisit trigger and fixed scientific ancestry

Old obstacle: the P018/R019 precision-object and future-operation mismatch required distinguishing a coarse readout from sufficient future state; the 2026-10-29 RH rough-factor fixed-low-moment linear-readout obstruction further demonstrates the importance of observer type. These negative results remain in force in their own scopes.

New available, *scoped* inputs:
1. At `awdawmip/enterprise-math@30afe94772306113ea7a03cd455e6fc1663d890c:research_notes/driver/2026-11-12_x6_cyclic_phase_transfer_sharp_four_start_tomography.md`, the author proves that four consecutive **registered complete** one-period O/I Weighted-BRC transfer matrices identify the six positive phase weights, and gives a three-origin collision.
2. At `awdawmip/enterprise-math@ccae96c930:research_notes/driver/2026-11-12_x6_weighted_brc_periodic_phase_gauge_rigidity.md`, rational phase-gauge equivalence and the positive-cone/labelled-state rigidity boundary are separated.
3. The native X6 Cell/path substrate and P000 retain the pinned older mathematical basis `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; the C6 transfer is a candidate BRC path observer, not an admitted native physical rotation law.

Unlike scale-fingerprint table inversion (`research_notes/2026-11-05_early_bottleneck_rough_moment_scale_fingerprint_and_cost.md`), the following reconstruction has **no enumerated lookup table** and has bit-polynomial decoder cost in a declared bounded-rational phase model. The new work is a finite-precision certificate and total decoder accounting for the previously proved exact inverse, not a second claim to have discovered its injectivity.

## Exact new theorem: certified fixed-point tomography

Fix `H >= 2` and a six-phase law `t=(t_1,...,t_6)`, where every `t_j=a_j/b_j>0` with integers `1 <= a_j,b_j <= H`. The O/I-labelled transfer is

```
T(t)=[[1,t],[1,0]],  P_j=T(t_j)T(t_(j+1))...T(t_(j+5)),
```

with phases interpreted modulo six and all four `P_1,...,P_4` supplied in their **common registered boundary-state frame**.

Let `m=ceil(log2 H)`, `p=12m+3`. Round all 16 rational matrix entries independently to nearest multiples of `2^(-p)` (ties arbitrarily). Then *every* original `P_j` entry, hence the entire ordered six-weight law `t`, is uniquely and exactly recoverable from those rounded values and `H`. The decoder uses 16 bounded-denominator rational reconstructions and a fixed number of exact 2x2 rational operations; its arithmetic bit complexity is polynomial in `log H`. No precomputed table of laws or scales is needed.

**Proof of precision certificate.** Let `Q=H^6`. Every entry of a product of six `T(a_j/b_j)` is a rational whose denominator divides the product of the six `b_j`, so its reduced denominator is at most `Q`. Distinct reduced rationals with denominator at most `Q` differ by at least `1/Q^2`. The certified rounding error is at most `2^(-p-1) <= 2^(-12m-4) < 1/(4Q^2)`. Consequently the original rational is uniquely the nearest rational with reduced denominator at most `Q` to each rounded entry; compute it by bounded-denominator continued fractions.

After recovering the exact four matrices, the already proved cyclic intertwining `P_j T(t_j)=T(t_j)P_(j+1)` gives

```
t_j=(P_(j+1))[1,2]/(P_j)[2,1],   j=1,2,3.
R=P_4 * inverse(T(t_1)*T(t_2)*T(t_3))
 =T(t_4)*T(t_5)*T(t_6).
t_4=R[1,2]/R[2,2]-1;  t_5=R[2,1]-1;  t_6=R[2,2].
```

All denominators are nonzero because `t_j>0`; the three-factor product has `R[2,2]=t_6>0`. The formulas recover the original law exactly. Rational entries have numerator magnitude at most `H^6(1+H)^6` after multiplication by a common denominator and hence `O(log H)` input bit length for six fixed phases. Euclidean rational reconstruction and the fixed number of rational operations therefore use `poly(log H)` bit work. QED.

**Four origins remain necessary in the same declared consecutive-origin observer class**, even with exact rational weights of height `H=2`. The prior collision
`U=(1/2,1/2,1/2,1/2,2,2)` and
`V=(1/2,1/2,1,2,1/2,1)`
has `P_j(U)=P_j(V)` for j=1,2,3, but `P_4(U) != P_4(V)`. Increasing output precision of the first three matrices does not distinguish those two laws.

## Independent finite reproduction (not the universal proof)

A separate Python `fractions.Fraction` check performed on 2026-11-12 used `Random(20261112)`, `H=2,3,4,5,6`, 100 independently generated six-tuples per H with `a_j,b_j` sampled uniformly in `[1,H]` (500 exact rational laws). For each law, recomputed the four matrix products with rational 2x2 multiplication; rounded each of their 16 entries to `p=12ceil(log2 H)+3` binary fractional bits; applied `Fraction(rounded).limit_denominator(H**6)`; then reconstructed all six weights by the displayed inverse. Every matrix and phase weight recovered exactly: **500/500 passed**. Values of p were respectively 15,27,27,39,39.

The same checker recovered the documented three-origin collision:
`P_4(U)=((23/2,33/8),(9,13/4))` and
`P_4(V)=((23/2,33/4),(9/2,13/4))`.
This is exact finite arithmetic, not independent theorem review.

## What changed and what remains

The historical precision bottleneck had no authorized reason to infer future sufficiency from a coarse scalar or from floating-point fitting. The new C6 **registered full-boundary** observer plus a rational height bound supplies a constructive theorem: precision `O(log H)` is sufficient for *exact law recovery* and thus for any later **explicit deterministic operation defined solely on the six weights**. This is an observer-specific local recovery result. The old scope-typed negative statements remain unchanged.

This does **not** yet reconstruct native Cell histories, original path provenance, incoming phase clock, triadic forces, or unregistered state frames: they are not among the six recovered weights. Without a denominator-height bound, finite-precision exact identification of arbitrary positive real weights is not possible by this certificate. If complete registered O/I matrices are unavailable, the input assumptions must be tested anew.

## Possible genuinely changed research unit and acceptance test

**Question:** Can a *physically/algorithmically realizable* native-X6 BRC observer return four full, consistently phase-registered boundary matrices from a typed Cell/path input while preserving provenance and future concatenation, under a measured error budget that meets this certificate?

First executable unit: choose one exact six-phase rational BRC path carrier and a nontrivial incoming phase/provenance state. Implement/locate its existing typed BRC transfer; compute `P_1,...,P_4` in the same O/I convention and the input-to-observer cost; apply certified rational reconstruction, then compare two-phase concatenation before and after recovering weights. Test the U/V collision on only three origins, plus a mismatched phase-gauge witness, and confirm that any apparent success does not erase differing native path histories.

PASS: exact scope-typed construction and observer factorization for the declared finite operation family, plus bit-accurate cost, and either a valid future-safe quotient or a minimal residual repair. NEGATIVE: exhibit two same-observer states with distinct declared future outputs; retain it as an exact counterexample for that observer. STOP/DOWNGRADE: when four registered full matrices cannot be emitted by the chosen BRC carrier, preserve this as an algebraic decoder theorem, not as native realization.

Full cost must count constructing the original typed BRC carrier, branch/port provenance, observer evaluation to p bits, calibration/frame registration, 16 scalar I/O and storage values of O(log H) bits, exact continued-fraction decoding, rational arithmetic, later operations, recovery, and independent verification. In this note the decoder cost is bounded; the **native observer-generation cost remains unknown**.

## Deduplication and Source state

Relevant *existing* taskbooks include `RS-X6-NATIVE-ROTATION-DYNAMICS` (directly asks for BRC path dynamics and minimum state), `RS-X6-LEGACY-PLANE-RECONCILIATION`, `RTASK-RF-GUARDED-MOMENT-CLOSURE-20260927`, `RS-BRC-FUTURE-FAITHFUL-INTEGRATION-20261028`, and the 2026-11-01 `RS-ROUGH-PARITY-LOCAL-STATE-UPDATE-20261101`. This scientific result is a proposed scoped continuation of the *existing* native-rotation research, not a duplicated task ID or another general BRC future-fidelity task. Live Owner/CLAIM is not inferred from static records.

No immutable V2 publication, native Researcher activity, CLAIM, Result or review is created by this note. For this 2026-11-12 conversation, native `em_session_start` returned `SESSION_ISSUANCE_QUOTA`; the independent tasks inventory query `early-bottleneck-20261112-ctl-tasks-01` was RUNNING at last read. Those are control facts rather than mathematics. Do not adopt another conversation's session, private capability or CLAIM. Publication requires a fresh authorized identity, equivalent V2 preflight and current owner check.
