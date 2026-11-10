# R52 — Exact phase-cut incidence update of labelled source-age vectors

**Date:** 2026-11-11 (Asia/Shanghai). **Status:** author-side mathematical proof and reproducible exact finite verification; independent review pending. **Frozen science:** `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. **Predecessor:** R51 Draft PR #2014 at `dffc106cbf006484c1883376543f58ce345f00bf`.

## 1. Retained observer and original labels

Fix irrational `0<theta<1`, integers `m,H>=1`, and `K=m+H-1`. Historical phases `p_z={z theta}`, `0<=z<m`, define right-half-open oriented circle intervals `I_z` beginning at `p_z` and ending at the next historical phase, with original label `z`. Let `pred(z)` be the label of the interval ending at `p_z`.

For observation phase `x`, age/source `r=1,...,H` lies at `{x-r theta}`. Retain its complete owner map `owner_x(r)=z` iff it lies in `I_z`, source membership `M_x(z)={r:owner_x(r)=z}`, and its labelled youngest-source readout `A_H(x)[z]=min M_x(z)` or `None` if empty. The full membership retains branch/source identity, age, provenance and multiplicity; scalar coverage or even the youngest vector is not substituted for the full partition when future operations require the latter.

All possible positive changes of this observer occur among `p_s={s theta}`, `1<=s<=K` (R49–R51). Calculations at a rational midpoint are transferred to the original irrational theta by R51's exact whole-enclosure comparison certificate.

## 2. Complete phase-incidence theorem

**Theorem 1.** When `x` moves forward through cut `p_s`, the exact source changes are all and only pairs `(z,r)` with `0<=z<m`, `1<=r<=H`, `z+r=s`. For each pair, source `r` crosses the boundary `p_z` from `I_pred(z)` to `I_z`. Descending through `p_s` reverses that move, `I_z -> I_pred(z)`. Every source not in that finite incidence list retains its owner.

**Proof.** A source reaches a historical boundary exactly when `{x-r theta}={z theta}`, equivalently `x={(r+z)theta}`. Irrationality ensures distinct phases indexed by `0,...,K`, hence at `p_s` precisely the pairs with `r+z=s` are incident. Sources move forward with increasing x, crossing from the interval ending at `p_z` into the interval starting at it under the right-half-open convention. All remaining sources are away from every boundary in a sufficiently small neighborhood; reversing phase direction reverses the moves. QED.

**Corollary 1 (exact incidence budget).** With `1<=s<=K`, the number of source movements is

`e(s)=max(0,min(m-1,s-1)-max(0,s-H)+1)=min(s,m,H,m+H-s)`.

Consequently `e(s)<=min(m,H)`, and `sum_{s=1}^{K} e(s)=mH`: every ordered source/history-boundary pair appears once. The list itself depends on s,m,H only; phase ordering depends on theta.

**Corollary 2 (labelled move).** At the cell immediately to the right of cut `p_s`, descend across that cut and perform simultaneously for each valid pair `r=s-z`:

`M(z) := M(z) \ {r};  M(pred(z)) := M(pred(z)) union {r}`.

Recompute minima only in the affected set `{z,pred(z)}`. All other labelled ages are unchanged; empty intervals, wrap-around and age/source multiplicity remain explicit. The simultaneous movements are distinct in `r` and `z`.

## 3. Lazy terminal plateau via R51 rank/select

Obtain descending rightmost cut indices `s_1,...,s_k` using R51's certified Euclidean Floor Sum order-statistic oracle. Classify `H` ages once in the right-hand cell of `p_{s_1}`, retaining the entire owner array. For each later cut rank `j>=2`, descend *across the preceding cut* `p_{s_(j-1)}` using Corollary 2, then read the new vector. This state is precisely that of the right-hand cell of `p_{s_j}`. Stop at the first changed complete labelled vector to obtain the exact maximal terminal equal-vector plateau.

**Theorem 2.** Given the correct ordered cuts and one exact initial source partition, the incidence algorithm computes the full labelled source partition and youngest vector on every requested successive phase cell. The first changed full-vector predecessor identifies the terminal plateau's left boundary. Across k cells the number of post-initialization source moves is `E=sum_{j=1}^{k-1} e(s_j)<= (k-1)min(m,H)`; for all K cuts, it is at most `mH`.

**Proof.** At rank 1 source membership is classified directly. Given the correct partition in one cell, Theorem 1 lists every source crossing at the next leftward boundary, so its update yields the exact next cell's partition. Induction proves all requested states and vectors. The first complete-vector change after traversing every intervening cut gives the maximal contiguous terminal suffix. The incidence bound is Corollary 1. QED.

**Data-structure accounting.** The executable reference keeps an authoritative `owner[r]` for every age, plus versioned min-heaps per historical label, counts and affected-label minima. A generation version distinguishes repeated visits by the same age to the same arc, so stale heap entries cannot masquerade as current provenance. After `O(m log m+H log m)` initialization comparisons and `O(H)` heap build, E movements cost `O(E log(H+E))` amortized heap work and `O(H+E)` stored heap entries. Only changed/affected labels are recomputed after a cut. Emitting an entire m-label vector still requires `Omega(m)` output per emitted state. R51's cut-ranking, certified parameter enclosure, bit lengths, verification and output are separate charged costs. An indexed balanced age tree could reduce the event heap's accumulation to `O(H+m)` storage; it remains a proposed alternative.

## 4. Exact scalar-collapse witness

Use `theta=sqrt(2)-1`, `m=5`, `H=8`. The two rightmost positive cuts are indexed 12 and 7 and share the complete youngest vector `(2,1,5,4,3)`. Descending across cut `p_7` produces `(2,1,7,6,5)`. **Both vectors have exactly 5 nonempty historical labels**, yet three age labels differ. Scalar nonempty-interval count is therefore insufficient for identifying the vector change or locating the terminal plateau boundary.

For frozen S23 (`m=128,H=225`), rightmost cut labels begin `[225,61,286,122,347]`; the first changed vector is at rank 2, with scalar coverage still 128 across that transition.

## 5. Exact finite verification, 2026-11-11

The full Python-standard-library `VERIFY_R52.py` imports the exact R51 Floor Sum/rational enclosure oracle from the preserved `VERIFY_R51_REFERENCE.py`, implements the event-state update and **independently reconstructs each source's owner from modular phase comparisons** at every tested cut, alongside full m-vectors and per-label counts. A separate compact independent reproduction uses complete phase sorting/heap top-k instead of the R51 rank oracle.

15 executed families: **881 checked phase cells; 33,237 exact source movements; 625 true labelled-vector changes; 13 families with witnessed equal scalar coverage but changed complete vectors**. Frozen S23 full 352-cut atlas: 28,672 movements, 290 vector changes, all independent full-source reconstructions matched. Quadratic cases include `(m,H)=(5,8),(8,17),(16,25),(23,31)` and eight deterministic small pairs; two long-source lazy tests `(8,99993)` and `(8,999993)` classified 5 and 4 cells respectively. The latter requires 999,993 initial owner classifications **plus** 24 incremental moves; it is not a claim of 24 total operations. All comparisons use exact integers; endpoint checks for selected smaller cases use the certified S23 or quadratic rational enclosures.

The executed original programs, full 15-family JSON certificate and logs are preserved in the R52 research bundle; the independent compact reproduction and its log are included as repository files. No new 298-affine-run risk compilation or native-X6 physical dynamics identification was made in this round.

## 6. Concrete continuation

R53: (A) complete direct k-smallest upper-error generation via Farey/Stern–Brocot/semiconvergents, including nonrecord candidates, and compare full bit costs with R51; (B) bounded-memory indexed age-set variant retaining all sources and original labels; (C) couple source event updates to R45 stage-wise risk increments and verify a frozen S23 horizon against exact reference. Retain the same immutable scientific pin and current source authority boundaries.
