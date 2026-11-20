# X6 Unit184 — sharp finite-horizon depth-label bits, sourced relation-field recovery and exact BRC fibers

**Date:** 2026-11-20. **Parent:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`. **Author lane:** `chatgpt-research-onhour-enterprise-math-20260923`, not the maintenance lane. **Status:** AUTHOR_PROVED / INDEPENDENT_EXACT_FINITE_CHECK / UNREVIEWED / NOT_ADMITTED. No Native PROGRESS is claimed by this source file.

**Immutable scientific input:** `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`, especially `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` (Git blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`) and `research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md` (blob `aa005cd62c45d7f4105632257db9186b115c5b29`). Historical producer/consumer input: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, `src/enterprise_math/weighted_relation_field.py` (blob `e50bf991e4dc4280063556a7aad1028f9f9404ed`), `tests/test_weighted_relation_field.py` (blob `51748dfe340c385907c4f2218fa1ae5ae2260522`). The actual production function `recover_totals_from_weighted_field` consumes the field and a grand total; the actual test invokes it. The six-equal-capacity specialization below is a **new typed mathematical adapter**, not a claim that this A3 module was already wired to the X6 native executor.

## Frozen model and new question

Keep the six signed native coordinate directions `±e_i`, anchored start `0`, an exact number `M∈N_0` of primitive events, and a relative terminal observer `a=q(z)=z−min(z)·1` in `A={a∈N_0^6:min a=0}`. Unit182 established endpoint-fiber path summation, and Unit183 established that one initial depth lifts an *ordered relative trace*. Here the **terminal snapshot** `(M,a)` is given, with no intermediate trace. Determine the sharp worst-case number of possible native endpoints and the minimum fixed-length residual bits for **exact terminal native endpoint recovery**. This is a finite-horizon recovery claim, not an exact Path-formal history or decorated full-packet recovery claim.

## Theorem 1 — exact fiber and sharp bit count

Let `d(h)=Σ_{i=1}^6 |a_i+h|`. The full set of **reachable** terminal depth lifts at length exactly `M` is

\[
\mathcal H_M(a)=
\begin{cases}
\{h∈\mathbb Z:d(h)\le M\}, & M\equiv\sum_i a_i\pmod 2,\\
\varnothing, &\text{otherwise}.
\end{cases}
\]

For nonempty fibers the set of integers is a contiguous interval, and, **for all integer M≥0**,

\[
\boxed{\max_{a\in A}|\mathcal H_M(a)|=\lfloor M/3\rfloor+1}.
\]

Consequently, among all lossless fixed-length labels that disambiguate a full terminal endpoint from `(M,a)`, the exact worst-case number of additional bits is

\[
\boxed{b(M)=\left\lceil\log_2\big(\lfloor M/3\rfloor+1\big)\right\rceil}.
\]

This counts endpoint identity only. Path history, weight decorations, and arbitrary future operations can need additional information.

**Proof.** In the signed six-axis nearest-neighbor graph, `z` is reachable after exactly `M` steps iff `||z||_1≤M` and `M−||z||_1` is even: take a shortest path and insert backtracking pairs. For `z=a+h1`, `||z||_1≡Σ(a_i+h)≡Σa_i (mod 2)` since there are six axes. Thus parity is independent of `h`, proving the displayed fiber formula. Convexity of `d(h)` proves interval contiguity on integers.

For its minimum and maximum depth `h_-≤h_+`, their native endpoints differ by `(h_+−h_-)1`. Hence

\[
6(h_+-h_-)=\|z_+-z_-\|_1\le\|z_+\|_1+\|z_-\|_1\le 2M.
\]

The integer interval therefore contains at most `⌊M/3⌋+1` points. To attain this bound write `M=3d+r`, `r∈{0,1,2}`, and take a native starting-point-to-endpoint witness

\[
z=(-d,-d,-d,0,0,\mathbf{1}_{r=1}),\qquad a=q(z).
\]

For every `j=0,…,d`, `z+j1` has norm `3d+1` if `r=1`, and `3d` if `r=0` or `2`. These norms are ≤`M` and have the same parity as `M`, so all `d+1` lifts are reachable. This also handles `d=0`. Distinct lifts are distinct native endpoints, hence at least `d+1` codewords are required for the witness; indexing the ordered interval achieves the bound. □

**Variable-size repair:** for a specific observed `(M,a)` with nonempty fiber, retain the index `j=h-h_-(M,a)`, `0≤j<|\mathcal H_M(a)|`. The rank recovers `h`, then `z=a+h1`. The theorem gives a **sharp universal per-horizon codeword length**; it does not claim that a variable-length or entropy-optimal code must spend the same bits on every fiber.

## Theorem 2 — concrete production-field consumer bridge

Specialize the frozen A3 relation-field producer to **six unit capacities** `m=(1,1,1,1,1,1)` with integer totals `c_i=z_i`. The *actual source formula* is `Z_{ij}=m_jc_i−m_ic_j=z_i−z_j`. It follows without numerical approximation that

\[
\boxed{a_i=\max_{0\le j<6}Z_{ij}},\qquad
\boxed{h=(C-\sum_i a_i)/6},\quad C=\sum_i z_i.
\]

Thus the actual production consumer `recover_totals_from_weighted_field(m,Z,C)` can recover the six integer components if the genuine grand total `C` is present. In the new frozen-X6 finite-horizon adapter, `(M,Z,j)` suffices: compute `a` from the row maxima, reconstruct `h=h_-+j`, construct `C=Σa+6h`, and feed `(m,Z,C)` to the source consumer. For actual input states all integrality and closure conditions are satisfied. The extra rank label is information-equivalent to the grand total for each fixed `(M,Z)`, but uses at most `b(M)` bits. A row maximum over **legitimate signed relation differences** here is not an LP011 native-axis `argmax` error.

**BRC consequence.** Each allowed `h` may carry a different original exact all-length native BRC count `N_M(a+h1)` from frozen V17; the field alone aggregates these endpoint masses. For `M=10`, `a=(0,0,0,3,3,4)`, the four lifts `h=-3,-2,-1,0` have counts **16,800; 226,800; 151,200; 4,200**, respectively (in depth order). This is a typed witness that an aggregated field and known horizon cannot by themselves recover the **per-native-endpoint** BRC count. The sharp bit bound is on native endpoint recovery, not generally on BRC-count recovery.

## Independent finite execution and evidence status

An independently written exact-integer Python checker enumerated all signed six-axis paths by terminal multiplicity at `M=0,…,10`; it checked **184,690 reachable (M,z) cases** for the field-row reconstruction and grand-total inverse, **97,306 relative fibers** for exact interval and parity membership, and all sharp witnesses. All checks passed. The exact dynamic-programming BRC counts of the M10 witness are above. Its JSON result digest is SHA256 `a5552e6529baebf0dc79c1894b8a5b41ddef0dd767186d4e26df94e063ba964a`. Universal validity is established by the preceding proof; finite execution is a reproducibility check. No R063 native benchmark reexecution occurred.

**Novelty/provenance discipline:** the signed carrier and V17 count formula are preexisting Foundation; the relative common depth is already in P000; the A3 relation producer, grand-total recovery consumer, and its source tests preexist; Units177/182/183 already established observer information loss and ordered-trace lifting. New here are the **exact horizon-dependent interval/fiber cardinality maximum, sharp fixed-bit bound, attained witness family, and its field-consumer bridge**, all scoped to the stated six-axis terminal observer.

**Outstanding:** LP011 and LP019 still lack exact offending `commit:path:line`; current same-lane protected writer authorization must be revalidated before any Native PROGRESS (historically verified through Unit174, with Units175 onward pending); historical Units149–152 and independent Driver review remain separate. The old successful R063 six-file benchmark is consumed, not rerun. Current source identity is not inferred from source-file authorship.

**Scientific successor:** for a genuinely source-backed state-dependent operation, test whether the finite-horizon rank `j` remains sufficient after one step when the horizon is advanced, and quantify the rank-update complexity under varying allowed signed primitive weights. Preserve exact target populations and cost of reconstruction.
