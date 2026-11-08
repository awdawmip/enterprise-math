# R5 constructive follow-up: an exact 11-edge nonseedless witness and a universal 19-edge coupling sparsifier

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_DERIVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific inputs **unchanged**: Global Knowledge `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. The statistical model and source/target orientation are exactly those of draft PR #1831, immutable commit `83431247dad45aba95b43125bca63c94d81e5750`, `research_notes/brc_r5_full_model_close_20261109/RESEARCH.md`. The purpose here is an independently checkable **additional construction and sparsity lemma**, not an independent review or formal acceptance of the predecessor coverage theorem. P000 and native X6 premises are not changed.

## 1. New exact 11-edge physical witness

Seven likelihood ratios: `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. Write a lawful flow as `(g,a,b,u,v,w,z)`. Take the previously published high-signal **source/target flow** pair in PR #1829, now supply an exact coupling:

```
source x = (1, 1/6, 1, 0, 31/240, 0, 1/60)
target y = (403649/517950, 462959/2071800, 403649/517950,
            455051/5524800, 20479/103590, 279431/1841600,
            462959/20718000)
```

The source has `9*b*z-4*a*(v-z) = 3/40` (calculate from the listed exact fractions); the target obeys the seedless relation exactly. Both are lawful, with `T_P=169/60` and `T_Q=217/80` on both sides.

Set `E[i,j]` (row = target likelihood node, column = source node) to the following **11 positive rational entries**, and set all 38 omitted entries to zero:

| i | j | E[i,j] |
|---:|---:|---:|
| 0 | 0 | 1099/21600 |
| 0 | 1 | 1/39 |
| 0 | 2 | 3227713/64640160 |
| 2 | 1 | 8/195 |
| 2 | 2 | 1417929/5985200 |
| 3 | 2 | 3227713/24861600 |
| 3 | 3 | 1511/10800 |
| 3 | 5 | 94567/1035900 |
| 5 | 5 | 32043/460400 |
| 6 | 5 | 94567/828720 |
| 6 | 6 | 1099/21600 |

Exact `fractions.Fraction` checking confirms nonnegativity and all 21 transport equalities:

```
sum_j E[i,j] = M_i(y)                     (7 target row masses)
sum_i E[i,j] = M_j(x)                     (7 source column masses)
sum_i r_i * E[i,j] = r_j * M_j(x)         (7 weighted column moments)
```

The 7-node P/Q marginal formulas are imported verbatim into `VERIFY_SPARSE.py` from the pinned R5 model. The transport is independent of any terminal declaration. For any `d_j ∈ [0,1]`, declare at target node `i` with probability `d'_i = Σ_j E[i,j]d_j / M_i(y)` on nonzero rows, otherwise zero. The 21 equalities directly imply the same two terminal error probabilities under Q and P. The stop times already match. This is an explicit **11-edge** realization for a genuinely nonseedless physical source.

## 2. General exact 19-edge theorem

**Lemma.** For any two seven-point probability measures `mu=(M_i(y))` and `nu=(M_j(x))` on these fixed distinct likelihood ratios, if a nonnegative martingale coupling `E` exists satisfying the 21 equalities above, then there exists one with **at most 19 positive entries**, with the same two marginals and all seven weighted column moments. If the marginals and grid are rational, the sparse coupling can be chosen rational.

**Proof.** Regard `E` as a point of a bounded, nonempty polytope `{E≥0: A E=b}` in 49 variables. The 21 equalities contain two linearly dependent rows: (i) total of row sums equals total of column sums; and (ii) likelihood-weighted sum of the row sums equals total of the weighted column sums. Thus `rank(A) ≤ 21-2=19`. Take an extreme point of the polytope. If more than 19 entries were positive, the corresponding columns of `A` would be linearly dependent; a nonzero signed kernel perturbation supported only on positive entries could be applied in both directions while preserving nonnegativity for a sufficiently small step. This contradicts extremality. For rational input the polytope is rational; a basic feasible point has rational coordinates. QED.

**Stronger constructive form.** From any exact feasible coupling, take any 20 positive edge-columns. Their constraint vectors are dependent. Find a rational null vector by exact Gaussian elimination. It has both positive and negative entries because every row-mass sum of its perturbation is zero. Increase the coupling along this null direction until the first negative-direction edge reaches zero. Nonnegativity and all 21 equalities persist, and positive support decreases by at least one. Repeating terminates after at most `max(0, support_initial - 19)` rounds. The same argument works for an `n`-node distinct-ratio grid with the general bound `3n-2` (or fewer when the constraint rank is lower). This is a support-size bound and an **exact finite procedure**, not a proved polynomial bit-complexity bound.

### Fully rational standalone experiment

`VERIFY_SPARSE.py` (Python standard library only) checks the 11-edge physical certificate; separately constructs a deliberately dense **abstract seven-node** exact martingale coupling with 37 positive entries, and sparsifies it to 19 in 18 steps. The abstract benchmark is solely for the transport polytope; no FULL_HIST flow membership is claimed for its synthetic marginals.

Actual local execution: `python -S VERIFY_SPARSE.py`, exit status 0:

```
PASS_EXACT_11_EDGE_NONZERO_RESIDUAL_PHYSICAL_R5_CERTIFICATE
PASS_EXACT_DENSE_TO_SPARSE_MARTINGALE_37_TO_19
SPARSIFY_PASSES 18
PROVED_GENERAL_7_NODE_COUPLING_SUPPORT_UPPER_BOUND_19
```

Full proof and exact code are included; finite experiments verify the specific examples while the rank argument proves the general bound.

## 3. Relation to BRC and mother objective; next exact question

BRC carrier: retain full source/target seven-node Q distributions, likelihood-ratio-weighted moments, branch identity and the actual edge joint measure `E`. The sparse operation discards edges only **after** proving the 21 exact observer equations remain unchanged, so no required future terminal declaration observation is lost. Reuse the parent R5 kernel semantics; no new primitive physical model is introduced.

The #1831 author-side whole-parameter covering proof and its cited predecessor PRs still require actual independent mathematical review. This note adds a reusable sparse **kernel certificate**, a bounded edge count and a complete one-example edge matrix.

Next: integrate the exact reduction with the existing `EXACT_COUPLING_SIMPLEX.py` from PR #1831 and benchmark coupled operations/bit growth. More ambitiously determine whether the sharp guaranteed edge bound under the physical seven-node flow constraints can be improved below 19; seek either a construction or an exact lower-bound witness. These are separate algorithmic questions and do not repin the frozen science.

## Control and provenance

GitHub writer: authenticated account `awdawmip` (repository admin). Native task/owner/CLAIM was still unconfirmed during this run; a queued native session request is not an issued Researcher-ID nor formal Result. This branch/PR is durable author-side scientific evidence, not canonical main integration or independent Driver admission. No credentials are included.
