# R57: exact grouped observer-phase cut transforms

Status: author proof + exact integer experiments, pending independent review. Date: 2026-11-11.
Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: `47a06fcf92aad7db81a117fd05f0a313f7fa2cbf:research_notes/brc_s23_av_split_block_20261111_r56/PROOF.md`.
Model: auxiliary irrational circle rotation with original historical labels, not a native six-axis dynamic.

## Definitions

Fix irrational `0<theta<1`, positive integers `m,H`, and `K=m+H-1`. Original historical labels `z=0,...,m-1` mark boundaries `b_z={z theta}`. Let `B=(B_0,...,B_{m-1})` be those *labels*, ordered by increasing circular boundary phase. The arc labelled z begins at b_z and ends at the next boundary.

At observer phase `x`, source age `r=1,...,H` has phase `P_r(x)={x-r theta}`, owner `L_r(x)` (one original label z), and youngest-age vector `tau_z(x)=min{r:L_r(x)=z}`, with empty entries recorded as None. Move observer phase *downward* from `x0` to `x1` with `0<x1<x0<1`, neither endpoint on a cut. The crossed cuts, in descending phase order, are `s in [1,K]` whose phases `d_s={s theta}` lie in `(x1,x0)`.

R52 identifies all events at cut s as `z+r=s`. R54's Farey-upper-error successor visits the s in strictly descending `{s theta}` order. Fix lower/upper Farey neighbours a/i < theta < c/j with determinant ci-aj=1 and i+j>K; start s=j and iterate
`T(s) = s-i if s>i; else s+j if s+j<=K; else s+j-i`.
A selected consecutive k-cut run is described by its starting s, k, i, j, K and descending orientation.

## Theorem R57-A (difference-array batched source transform)

At cut s, all and only affected source ages form the integer interval
`I_s=[max(1,s-m+1), min(H,s)]`.
For each selected cut s add +1 to a difference array at the lower endpoint of I_s and -1 just after its upper endpoint. Let C_r be the prefix sum at source age r. Then
`L_r(x1) = B[(rank_B(L_r(x0))-C_r) mod m]`
for every r. The exact youngest ages follow by taking the minimum r in each resulting original label. All observers that factor through full endpoint labelled membership/youngest ages are preserved.

Proof. The equation z=s-r with 0<=z<m and 1<=r<=H is equivalent to r in I_s. The difference-array prefix therefore counts every crossing of each source precisely once. When x decreases across the boundary b_z for source r, that source moves from the arc starting at z into its *immediate circular predecessor*. This is true at wrap-around and when m=1. By induction over the strictly ordered crossings, C_r events shift that source backwards exactly C_r positions in B. This is the stated formula. Taking the minimum source age per preserved original label yields tau exactly. QED.

Given the initial full source labels and B, k selected cuts require 2k difference-array endpoint additions, H prefix operations, H labelled index updates, and O(H+m) labelled youngest-age reconstruction; workspace O(H+m). Contrast the E=sum_s min(s,m,H,m+H-s) individual micro-events. Initial source classification, Farey bracket generation, theta precision, source index bit lengths, observer rephasing, output and verification are separate costs. A physical source timestamp t=j-r is rephased by x=x_phys+j theta: large |j| does not enlarge the number of cut events, although its modular phase arithmetic uses O(log |j|) input bits.

## Theorem R57-B (lossless symbolic cut tape)

A consecutive R54 cut run is encoded by (Farey i,j,K, starting cut, count k, orientation). The ordered events at any cut s are reconstructed as the original labelled pairs `(r,z=s-r)` for each r in I_s. Thus a tape using O(1) run metadata plus the initial source state reconstructs the entire E-event labelled trajectory on demand; the difference-array C_r is an exact quotient for endpoint observers. A path/intermediate observer can be evaluated by replaying the encoded ordered cuts and their event intervals.

Proof. R54's successor is a permutation of indices 1..K, so the starting cut and length select exactly one ordered run. Each cut's r interval enumerates every event and uniquely determines its original z. Replaying those events yields the original observer-phase path. Theorem A supplies the endpoint quotient. QED.

**Witness for observer scope:** taking all K positive cuts crosses every historical boundary exactly once per source, so C_r=m for all r and the final original-labelled membership equals the initial membership. Yet exactly mH labelled micro-events occur in between. In frozen S23 m=128, H=225 this is **28,800** transient events despite identical endpoint owners and endpoint youngest-age vectors.

## Validation

`CHECK_R57.py` is a standalone exact integer checker of the individual-event replay and the difference-array transform against an independent rational-phase bisect oracle. `VERIFY_R57.py` (full local evidence in the handoff bundle) additionally checks physical timestamps j=-10^18, j=10^12+128 and j=10^18, and records the detailed certificate. Requiring the rational reduced denominator to exceed K avoids finite-test phase ties. These finite tests check the implementation; the propositions above are proved for irrational theta.

The exact small tests cover m=1..12, H=1..15, eight cases per pair: **1,440 tests and 39,295 explicitly replayed labelled micro-events**, all matching. Frozen S23 uses m=128,H=225,K=352, D=10^24, p_lo=262204504569236716045286, p_hi=p_lo+1. Both endpoints share the same R54 ordering and pass for k=1,4,32,88,176,264,352. For k=176, explicit micro-events **14,418** against **352 difference endpoints + 225 prefix steps = 577**; full youngest age vector changes. For k=352, explicit micro-events **28,800** and both the 225 source labels and 128 youngest ages return to their initial values. Frozen input denominator bit length is 80. The numeric comparison counts only these grouped arithmetic primitives, not total machine-time or full integer bit cost. `EVIDENCE.md` records values and boundaries.

Next: R58 multi-checkpoint range-add/point-query structure preserving labelled trajectory, followed by bit-cost measurement against R49 caching, R55 full-gap merge, and R56 split-block merge. Shared CLAIM, independent review and mathematical admission have not been claimed.
