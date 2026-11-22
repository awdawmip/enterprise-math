# R762IX — Exact 47→45 compression for the ten-triple star with one absent and one singleton support

Date: 2026-11-22 (Asia/Shanghai). Scientific status: **AUTHOR_PROVED / EXACT_INTEGER_CERTIFICATES_CHECKED / NOT_REVIEWED**.

Immutable scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, P000 V5 and the frozen composite Port–Euler observer from R762IW. Related (not rewritten) scientific frontier: R762IR triangle-redundancy reduction, R762IU uniform-47 conditional proof, R762IW nine-triple/one-absent branch in Draft PR #2954, commit `d2d348a32184532d8932c7c0533fb15fcb74db92`.

## Model and exact proposition

Let `A={0,1,2,3,4,5}`, `P=C(A,2)` (15 Ports), `H=C(A,3)` (20 support labels). Each event of support `S={a,b,c}` chooses an unordered edge joining two distinct Ports from `{ab,ac,bc}`. A legal closed realization of a histogram `n` is a connected multigraph with all *active* Port degrees positive and even, all inactive degrees zero, and a prescribed start Port `p` among the active vertices. This is an **observer-level** multigraph statement, not the native signed X6/P000 Cell/phase/time/rotation dynamics.

Choose an axis `a∈A`. Let `T_a={S∈H:a∈S}` (the ten supports of the full axis star). Let `z,q` be **distinct** supports in `H\T_a`. Consider the 47-event histogram

\[
n_S=\begin{cases}3& S\in T_a,\\0&S=z,\\1&S=q,\\2&\text{otherwise.}\end{cases}
\quad\sum_S n_S=10\cdot3+1+8\cdot2=47.
\]

**Theorem (star branch).** If this histogram admits a legal Port–Euler closed realization on an active set `V⊆P` with chosen start `p∈V`, then there exists `j∈T_a` and another legal closed realization with the **same** `V` and chosen start `p`, with histogram `h` given by `h_j=1` and `h_S=n_S` for every other support. Consequently `h≤n`, `h_S≡n_S (mod 2)`, the positive support set is unchanged, and `Σ_S h_S=45`. The quantifiers cover all six star axes, all 90 ordered `(z,q)` pairs per star axis, and every actually realizable active set.

## Proof

**Case 1: some Port is inactive.** Every Port (an unordered pair of axes) is contained in at least one support of `T_a`: if it includes `a`, extend by another axis; otherwise take its union with `{a}`. Thus an inactive Port lies in some `j∈T_a`. Since `n_j=3>0` and the original realization exists, its support triangle has at least two active Ports; with one Port inactive it has *exactly* two active Ports. All three events of support `j` are therefore forced onto the unique admissible edge of that triangle. Remove any two of those three parallel edges. One parallel edge remains, so the underlying simple graph is unchanged. Endpoint degrees each decrease by 2, remain positive and even: both had at least three incident events from `j`, so their original even degrees were at least 4. All other degrees and support labels are unchanged. Thus connectivity, exactly `V`, and the chosen start `p` remain valid.

**Case 2: all 15 Ports are active.** By relabeling axes take `a=0`, `z={1,2,3}`. The remaining five axes admit the full `S_5` permutation group. There are exactly two orbits of ordered distinct `(z,q)` pairs, because two different 3-subsets of a 5-set intersect in either two or one axes. Representatives are:

- **Overlap 2:** `z=123`, `q=124`, with `60` ordered pairs in its orbit;
- **Overlap 1:** `z=123`, `q=145`, with `30` ordered pairs in its orbit.

For each representative, the attached checker embeds a 60-entry nonnegative **integer** allocation over the three unordered Port–Port edges within each of the 20 support triangles. It reduces `j=012` from 3 events to 1. The verifier checks directly that each per-support sum equals the intended 45-event histogram, that all 15 degrees are positive and even, and that the graph is connected. Under an axis relabeling, every Port, support and event-edge is carried bijectively to another Port, support and event-edge, preserving those integer conditions. Hence the two verified witnesses cover all 90 ordered pairs for `a=0`. Swapping `0` with each target axis extends the coverage to all six stars. A connected even-degree multigraph admits an Euler circuit starting at any prescribed active Port `p`.

This proves both cases without relying on the earlier global triangle-redundancy lemma. **The result does not assume that a 45-event witness is literally a subsequence of a specified original Euler tour**: it is an exact existence theorem for a preserved observer histogram and active set. Once constructed, its two missing same-support events can be reinserted as a parallel pair to yield a legal realization of `n`.

## Reproduction and finite-domain coverage

Execute `python R762IX_STAR_TEN_TRIPLE_VERIFY.py` (Python standard library; no SciPy or solver required). The two initial proposals were obtained with SciPy/HiGHS integer optimization; only the explicit integer certificates and independent standard-library checker enter the argument. Deterministic exact checker result:

```json
{"status":"PASS R762IX","certificates":2,"s5_orbit_sizes":{"shared_two":60,"shared_one":30},"ordered_pairs_per_star":90,"all_active_histograms_checked":540,"witness_stream_sha256":"dc406bad176dbfe234e0330d8aab6ca89052862e0346c2cba39e047c6fbcc23a"}
```

Coverage: six choices of star axis `a` × 90 ordered choices of missing support `z` and singleton support `q` = **540** all-active histograms. Their integer witnesses are generated from the two embedded certificates by explicit edge-correct permutation and rechecked independently. The inactive-Port branch is a direct proof for **every** originally realizable active set, with no finite mask cutoff. The all-essential ten-triangle family being an axis star is a separate antecedent classification in R762IR/R762IU; no unreviewed global result is silently promoted by this local theorem.

## Implication and next discriminating unit

This discharges the **axis-star** all-essential subcase of the 47-event terminal histogram `(t,d,s,z)=(10,8,1,1)` by a two-certificate structural proof, without imposing an artificial active-set enumeration. To upgrade the entire terminal histogram, independently audit the prior statement that the only all-essential 10-support triangle systems are the six axis stars, and verify the R762IR reduction for a non-essential triple support while retaining the active set. The other 47-event terminal histograms `(8,11,1,0)`, `(9,9,2,0)`, `(10,7,3,0)` remain. The currently claimed k=0 upper bound `47` is an author-side theorem depending on earlier unreviewed reductions; k>0 retained bound `54` is a separate model statement. Neither yields a native signed TRIADIC_CLOSURE_E dynamics theorem.

No formal CLAIM, PROGRESS, Result, independent mathematical Review or P000 edit is implied by publishing this research note.
