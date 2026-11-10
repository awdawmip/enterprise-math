# R32 — Stern–Brocot to exact maximal affine runs (S23/AV)

**Date:** 2026-11-10. **Status:** author-side exact proof and finite certificate; independent review pending. **Frozen scientific pin:** `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Problem

For the auxiliary irrational-circle observer with 128 historical phase cuts, define (R_n=1-sum_I M_n(I)), where (M_n(I)) is the maximum remaining subinterval length within a historical arc after (n) total phase cuts. This is not a claim about native six-dimensional heartbeat dynamics. Fix the *open* rational interval
[
262204504569236716045286/10^{24}<	heta<262204504569236716045287/10^{24}
]
and compute (R_n) for all integers (128le nle10^{12}+128), as a minimal collection of integer-affine runs, without enumerating future cuts or individual growth events.

## Lemma 1 — Farey stage generation

Begin with Stern–Brocot neighbors (0/1<	heta<1/1); compare the mediant to both rational bounds and replace the lower or upper neighbor accordingly. Exactly 11 strict mediant comparisons produce (27/103<	heta<16/61) and denominator sum (164>128). At a pair (a/q<	heta<c/j), the determinant is (cq-aj=1). Its phase-gap stage runs through (n=q+j). When this sum lies below the requested horizon, the next mediant replaces one neighbor, and the next stage starts at (q+j+1). A further 77 strict comparisons produce 78 stages, the last truncated by (N=10^{12}+128). Both enclosure endpoints give identical decisions throughout.

## Lemma 2 — source ages compile into two blocks

Use the exact signed-source rigidity proved in predecessor R31 (commit `9bfccb2650cab28b88c21bc749295722e7134ad2`), with (m=128,H=164), negative clearance (ho_-(	heta)=59-225	heta) and last-maximal-gap source-age template
[
mathcal A={1,ldots,61}cup{98,ldots,164}.
]
All 75 stages after the three short initial stages satisfy (qge164,jge292) and (0<c-j	heta<ho_-(	heta)) at both interval endpoints. For each historical arc, its final long-gap source is (t=j-r), one distinct (rinmathcal A). The gap (w=u+v), where (u=q	heta-a>0) and (v=c-j	heta>0), disappears at cut (n=q+t+1=q+j-r+1), causing precisely (min(u,v)) risk growth; all other steps in the stage have zero increment. Hence the **complete positive event set** is represented by *two contiguous intervals*
[
[q+j-163,q+j-97],quad[q+j-60,q+j],
]
each intersected with the actual stage bounds. At every stage containing events, the minimum amplitude has one unambiguous integer-affine formula for all (	heta) in the open enclosure. Its identity changes within the final truncated stage, but that stage has zero events, so the ambiguity affects no output.

## Lemma 3 — small prefix and integration

For (129le nle389), reconstruct only the first 261 updates: sort exact residue phases at each rational endpoint, partition by the original 128 historical arcs, and choose the maximum affine subgap in each arc. Both endpoints choose the same gap expression. The resulting exact increment runs are

- (129ldots164: 16-61	heta);
- (165ldots292: 164	heta-43);
- (293ldots328: 0);
- (329ldots389: 164	heta-43).

For the remaining stages, append the two-block intervals, fill gaps with zero slope, merge adjacent intervals with identical slopes, and integrate from (R_{128}=0). Every output run is maximal: adjacent slopes are unequal. The generator never constructs the previous 9,697 individual positive-event rows.

## Certified S23 result

The complete risk table to (10^{12}+128) contains **298 maximal affine runs** (150 positive-slope and 148 zero-slope). The compiler performs 88 strict Stern–Brocot comparisons, 261 finite small-prefix cut updates, and only **148 block emissions** across 74 event-bearing eligible Farey stages; the 75th eligible truncated stage has no event. The final risk is
[
R_{10^{12}+128}=-4017401528447+15321634290944	heta.
]

A standalone standard-library exact verifier is provided as `VERIFY_R32.py`; it recomputes the entire 298-row table from ((128,10^{12}+128,L,U)), checks the stage inequalities and hashes the canonical TSV. The generated result's SHA-256 equals the previously independently obtained R27 risk-table digest:
`2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`.
Additional local cross-validation checked all 78 source stage rows and all 298 complete risk rows against the preserved R27 files (byte-exact).

## Complexity, provenance, next step

For this **fixed input**, the large-horizon stage compiler takes (O(S+R)) exact arithmetic operations with (S=78) and (R=298), after 88 Stern–Brocot decisions and the bounded initial-prefix reconstruction. Integer bit cost depends on (log_2(10^{24}N)), coefficient sizes and serialization, not a unit-cost infinite-precision oracle. No universal polylog bound is asserted for naïve Stern–Brocot mediant enumeration: a large continued-fraction partial quotient can require many consecutive mediants.

Predecessor: R31 author-side proof at `9bfccb2650cab28b88c21bc749295722e7134ad2`. Independent reference: R27 at `6cfd0bf078b3bd05fbd4c51508a868a4706a5823`. Reference risk table was preserved from the prior conversation run. This research note is not a formal Result, independent review, shared CLAIM or P000 promotion.

**Next:** replace the 261-step prefix by rank/select; use accelerated Euclidean partial quotient jumps for a variable-parameter output-sensitive *bit*-complexity theorem; test a second irrational rotation model with a different historical size and preserve source-age provenance.
