# EC49FQM — Exact finite evidence index and reproduction contract

Frozen scientific commit: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This index belongs to the original BRC native class16943; it does not change the model or scientific pins.

## Source inputs
* `source/frozen_original_master.txt`: SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`
* `source/EC49FPG_PROFILE.csv`: SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`
* Exact finite domain: 141 root-response profiles; total original multiplicity 310; 144 terminal + 84 named-root physical observations = 228 queries; 209 response partitions; 139 terminal joint-output fibers with exactly two two-member exceptional fibers, each profile weight 1.

## Thirteen independently recomputed rational anchors

The integer Bellman value uses weights `w_i=310*(b-a)+141*a*m_i` for `lambda=a/b`. The value is the *unnormalized* sum of weighted query costs; divide by `141*310*b` to obtain expected cost.

| r:t | lambda | Exact unnormalized optimum | Complete optimal physical first indices | Certificate SHA256 |
|---|---|---:|---|---|
| 3:2 | 0 | 185380 | 32,34 | dc7acdcbe623f99105e23f4ffc41999fae97e73e38114c4ebccb7ef8ee7efdfa |
| 3:2 | 310/4869 | 911586620 | 32,34,140,142 | a3f931a468a7b2d045b1a0f21a19cf07a177da525470c926b884819ea1d9c7b3 |
| 3:2 | 620/3299 | 623523150 | 16,23,140,142 | 9b1816dce6245801b2bd11a1033936c01de455e4799f321da7b5ebabeb782f23 |
| 3:2 | 1 | 195285 | 16,23 | d39622ee462aa0dc4d33025c321a63d4d4d2d5552f4ba2cd805952fe064cd885 |
| 5:2 | 0 | 189100 | 32,34 | 2ef4b3c896c64431594fc3bcae13665955eccc7fa821773f7b26f61e50937a50 |
| 5:2 | 310/14269 | 2706610620 | 32,34,140,142 | e9ed36a55495f3f2f99f3cf64e522ce9aa2285f253540466301774f0620efaa7 |
| 5:2 | 620/3299 | 632702250 | 16,23,140,142 | 72542f841487bcf10d2988d862a3f89bfeaeddf04e3382ccf531ccb5d230af56 |
| 5:2 | 1 | 196695 | 16,23 | 629e301022153df4773228d45eca9b7b9bc3257babf6fbff4cdf5b8a8c27a718 |
| 1:1 | 620/3299 | 309466800 | 16,23,140,142 | 79c7245a73b6e7f8b053395c247d7fc7dc9aa4478c190c360180faf63552b8d0 |
| 1:1 | 1 | 97290 | 16,23,124,131 | e6eb4e1eec6181ee803ae7a5605d7c0c081b89df311366d035774cf7e5e0ea06 |
| 3:1 | 0 | 95480 | 32,34,140,142 | e0fff97ddfe12bd1da10bcecf0fa7637cf6b6c503347d1024b7c0889c71a6f12 |
| 3:1 | 620/3299 | 318645900 | 16,23,140,142 | 0c6704780fd9fea4a1bf2954023cc6a2af0c9e391b6248309de7030add3cb96c |
| 3:1 | 1 | 98700 | 16,23,59,88 | 3324f8ceabaab65fbc0cbe86d00d953fa35806db91e5a5fdf185e13bc72e1b58 |

## Reproduction

The self-contained archive accompanying the EC49FQM research handoff contains exact source files, these 13 `certificates/r*_t*_lambda_*.json` files, both the primary and independent Bellman programs, the pinned native decoder, logs, full theorem, and a per-file SHA256 manifest. No credential is contained in the archive.

From the unpacked evidence root:

```bash
sha256sum -c SHA256SUMS
PYTHONPATH=code python3 code/EC49FQM_INDEPENDENT_VERIFY.py
```

The independently rerun result is:

```text
FIBER_LOWER_BOUND_PASS 139 terminal fibers
INDEPENDENT_BELLMAN_AND_ALL_FIRST_TREE_PASS [13 complete rational anchors]
EC49FQM_13_INDEPENDENT_ANCHORS_TWO_SLICES_FULL_HIGH_RAY_AND_RIGHT_STRIP_PASS
```

The main theorem is `EC49FQM_FULL_HIGH_PRICE_TWO_PRICE_SLICES_THEOREM_20261116.md`, and the versioned audit checker is `EC49FQM_INDEPENDENT_BELLMAN_VERIFY_20261116.py`. The methods prove the whole high-price ray and right-prior strip via exact lower bounds and bilinear interpolation, and prove full-prior results at x=3/2 and 5/2 via complete Bellman endpoints. The remaining curved transition beyond those exact sections is unresolved.

**Status:** author-derived, independently implemented exact arithmetic finite checks; no external independent reviewer, no formal result/claim, no Lean proof.
