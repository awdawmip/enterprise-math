# R284CD — Exact coordinate-mask arc frontier for the fixed 34-bit Port observer

Date: 2026-11-20 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**. Portable scientific continuation of R284CC; no new Task, CLAIM, Result, Review, P000 change or native X6 physical attribution.

## Frozen observer and finite domain

Preserve the R284BZ/R284CC scientific pin:
[
F_C=det(\operatorname{diag}(d_0,6,13,d_3)-C-z_1E_{01}-z_2E_{02}-z_3E_{03})\pmod p,
]
where ((p,d_0,d_3,z_1,z_2,z_3)=(17179869143,1120832,1651128,390139,394465,1497639)) and (C\in\{1,2\}^{4\times4}).

Keep lower coordinates in their frozen order
[
L=(u_1,a_{11},x,y,u_2,w,a_{22},z,u_3,g,h,r)\in\{1,2\}^{12}
]
and four top-row bits. Each of the 4,096 lower states yields 16 distinct top-row codewords. Their already verified global minimum circular separation is 59. The relevant observation noise satisfies (ho<59/2) in the circle of circumference (p).

For every coordinate subset (S\subseteq\{0,\dots,11\}), partition the lower states by their exact bits at positions in (S), retaining each group's 16 top-row possibilities. Each resulting group has (2^{12-|S|}) lower states and (2^{16-|S|}) full codewords. Store the **shortest closed covering circular arc** (A_G) for each group, formed by deleting the largest empty cyclic gap of its sorted codewords; ties choose the first gap. Define
[
Q(S)=\max_{y\in\mathbb R/p\mathbb Z}\#\{G:\operatorname{dist}_{\rm circle}(y,A_G)\le59/2\}.
]
The correct group is always retained at every valid noisy observation. Full decoding reconstructs at most (Q(S)2^{12-|S|}) lower states, using four exact thresholds per state as proved in R284CB.

## Exact finite classification: all 4,096 coordinate subsets

The exhaustive checker enumerated all (sum_{k=0}^{12}\binom{12}{k}=4096) coordinate masks, reconstructing every one of the 65,536 codewords from the frozen integer determinant formula and optimizing the circular arc for each group. Its complete classification of the minimum possible (Q(S)) at each cardinality is:

| |S| | Indexed arcs | Minimum worst-case retained groups | Best-mask multiplicity | Worst lower-state reconstructions |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 4,096 |
| 1 | 2 | 2 | 12 | 4,096 |
| 2 | 4 | 4 | 66 | 4,096 |
| 3 | 8 | 6 | 2 | 3,072 |
| 4 | 16 | 8 | 3 | 2,048 |
| 5 | 32 | 8 | 1 | 1,024 |
| **6** | **64** | **4** | **1** | **256** |
| **7** | **128** | **7** | **1** | **224** |
| 8 | 256 | 13 | 2 | 208 |
| 9 | 512 | 22 | 1 | 176 |
| 10 | 1,024 | 39 | 1 | 156 |
| 11 | 2,048 | 70 | 1 | 140 |
| 12 | 4,096 | 128 | 1 | 128 |

The unique optimum for **six** selected coordinates is
[
S_6=(u_1,a_{11},x,u_2,w,a_{22}),
\qquad Q(S_6)=4.
]
Its 64 index arcs require at most (4\cdot64=256) lower-state reconstructions and at most 1,024 threshold decisions per query. It **halves the persistent arc count** compared with R284CC's 128 arcs, at the same maximum reconstruction budget.

The unique optimum for **seven** selected coordinates is
[
S_7=(u_1,a_{11},x,u_2,w,a_{22},u_3),
\qquad Q(S_7)=7.
]
Its 128 arcs require at most (7\cdot32=224) lower-state reconstructions and 896 thresholds, improving the prior seven-prefix selection's (8\cdot32=256) states and 1,024 thresholds while keeping the same index-record count.

These are exact optima **within coordinate-subset groupings and the specified minimum-covering-arc index**, not lower bounds for all possible nonlinear residual partitions or decoding algorithms.

## Proof and evidence

1. The frozen formula yields (\beta_L,k_0,\dots,k_3) and exactly the same word list as R284CC. The 65,536 entries in frozen top-row/lexicographic-lower ordering have SHA-256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`.
2. For each of the 4,096 subsets, selecting coordinates specifies a disjoint exact partition of all 4,096 lower states. Sorting each group's complete codeword set and deleting its largest circular gap gives its minimum-length single covering arc, including the wraparound gap.
3. Doubling the circle to modulus (2p) makes radius (59/2) integer-exact. A group arc beginning at integer (a), width (w), becomes the inclusive circular interval starting at (2a-59) of width (2w+118). Splitting at the seam and processing starts before finishes at coincident endpoints counts closed arcs exactly; overlap is constant between all event points. Consequently the maximum computed by a complete endpoint sweep is the maximum over **every real circular observation**.
4. An independent direct modular interval-membership check covers all 129 distinct event/seam coordinates for (S_6) and all 257 for (S_7), corroborating the two advertised bounds and their shared peak witness at doubled circle coordinate (9213470267).
5. Repeating this finite procedure over all (inom{12}{k}) subsets certifies the minima and number of equality cases. For an independent exhaustive rerun, the sorted `mask:peak` text stream over all 4,096 masks has SHA-256 `d18f850b3240eba3c369f3860ef103f90c26476986e7caa119c24b43b4d6dc2e`; the companion checker asserts this.

Integer operations are exact: words and group distances fit signed 64-bit integers; the sweep also uses Python unbounded integers. The group guarantee is an index/pruning theorem, not a CPU benchmark. It includes conservative closed-endpoint ties, whereas the recovery theorem needs the open error inequality. Decoding continues to use the previously proven R284CB greedy four-threshold and global gap-59 uniqueness.

## Reproduction and continuation

- Source pin: [R284CC theorem](https://github.com/awdawmip/enterprise-math/blob/020c12dbfdc8ebefe1d02d74457f26e6f0fb9649/research_notes/portable_direct/R284CC_128_ARC_RESIDUAL_COARSE_DECODER_20261120.md) and its previous immutable mathematical dependencies.
- Executed locally with Python 3 and NumPy, exact full-mask enumeration; source: `R284CD_coordinate_arc_mask_checker.py`, companion `R284CD_coordinate_arc_mask_verification.json`.
- No independent researcher review or canonical Task Result promotion has been performed.
- Relevant account/project rules: P000 V4 projected core, ACTIVE worldview, current research method, research-continuation normative overlay, BRC observer-fidelity scope. Here BRC is used as an observer/fiber discipline; the numerical Port determinant is the explicitly selected finite auxiliary representation.

**Next scientific question:** Test small parity/affine partitions of the 12 lower bits or a residue-indexed inverse to reduce the 64-record/four-group cost without discarding Port provenance; separately derive a direct inverse for the five suffix bits, and compare whole decoder time (preprocessing, memory, reconstruction, verification) against R284CC and the full table. Preserve the fixed (p,d,z) scientific pin for these comparisons.
