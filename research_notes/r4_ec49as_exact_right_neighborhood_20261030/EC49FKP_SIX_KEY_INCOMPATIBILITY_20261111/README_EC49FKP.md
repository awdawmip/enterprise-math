# EC49FKP — pairwise prefix incompatibility excludes all but nine full six-key BRC sets

**Date:** 2026-11-11. **Frozen science:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Status:** AUTHOR_EXACT_FINITE / TWO_NUMERICAL_IMPLEMENTATIONS_CROSSCHECK / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Exact finite result

Keep the same nine-state BRC model, 178,850 exact legal ordered six-axis signed native operation words, 94 full raw cache keys and 24 prescribed observation labels. Exactly **2,004** six-key subsets cover the 24 labels (EC49FKO); exactly **1,263** were already ruled out for any cost <=93 by the depthwise forced-label maximum-support lower bound.

For the remaining 741 six-key sets, the exact additional *pairwise native-prefix incompatibility* lower bound excludes **732** further sets. Thus **1,995/2,004** complete six-key subsets require at least **94 distinct literal nonempty signed ordered X6 microstep prefixes** to realize all 24 labels. Exactly **nine six-key sets survive these two necessary sieves**.

All **628 inclusion-minimal six-key covering subsets** are excluded. The nine remaining sets each contain one of the 16 earlier complete five-key subcovers; their five-key solutions alone are already known (EC49FKN) to need at least 99 prefixes, while adding a sixth key may change the prefix cost.

| Set class | EC49FKO excluded | EC49FKP additionally excluded | Remaining |
| --- | ---: | ---: | ---: |
| Contains five-key complete subcover (1,376) | 823 | 544 | **9** |
| Inclusion-minimal six-key cover (628) | 440 | 188 | **0** |
| **Total (2,004)** | **1,263** | **732** | **9** |

## New proved lower bound

Fix a six-key set K and signed native microstep depth d. Let `L_i(K)` be the shortest legal word's microstep length for label i, `A_d={i:L_i(K)>=d}` and `N_d=|A_d|`. These forced labels must each contribute a literal prefix at depth d in every legal completion.

Construct the **incompatibility graph** `G_{K,d}` on vertices `A_d`: distinct labels i,j are adjacent iff **there exists no** native signed ordered prefix p of length d shared by any legal K-word of each label. Any graph clique contains pairwise prefix-incompatible labels, so every selected completion needs at least one distinct depth-d prefix per clique vertex:

```text
depth_d_prefix_count >= omega(G_{K,d})
```

Combining with EC49FKO's existing `ceil(N_d/M_d)` layer bound, where `M_d` is maximum possible forced-label support of any literal depth-d prefix, yields the universally valid exact necessary inequality:

```text
|union_i P(w_i)| >= sum_d max(ceil(N_d/M_d), omega(G_{K,d})).
```

All edges and cliques are computed on **complete signed ordered microstep prefix identities**, retaining full raw cache keys; no endpoint projection or unsigned coordinate quotient enters this lower bound. The maximum clique is found exactly by recursive bitset branch-and-bound, with pruning `current_size + number_remaining <= current_best`, preserving the full finite search.

## All nine residual six-key sets

Each remaining set contains the four required raw keys:

```text
K4 = {(2,1,1),(3,0,1),(3,1,1),(4,2,1)}.
```

The additional two raw keys and the new per-depth exact lower bound (all in the same 24-label model) are:

| Extra raw keys beyond K4 | New lower bound |
| --- | ---: |
| (5,4,1), (5,5,1) | 92 |
| (5,4,1), (6,4,1) | 92 |
| (6,3,1), (6,4,1) | 92 |
| (6,3,1), (7,3,1) | 92 |
| (6,4,1), (6,6,1) | 92 |
| (6,4,1), (7,5,1) | **86** |
| (6,4,1), (7,6,1) | 92 |
| (6,4,1), (8,4,1) | 92 |
| (6,4,1), (8,5,1) | 92 |

These bounds are **necessary** and do not assert realizability with 86 or 92 prefixes. All 732 newly excluded sets have a computed combined lower bound **at least 96**.

Combining EC49FKM (four or fewer raw keys cannot cover all labels), EC49FKN (all five-key solutions need >=99 prefixes), EC49FKO and this EC49FKP, the mother search for a solution using <=6 keys and <=93 native prefixes is reduced to these nine exactly specified key sets. The seven-key global question remains `C_min(7) ?= 94`.

## Actually executed computation, reproduction and audit

Original Python verifier (adjacent `VERIFY_EC49FKP_PORTABLE.py`) executed on the exact frozen generator, the full existing 2,004-keyset EC49FKO report and all 741 earlier survivors, printing:

```text
EC49FKP_PART 0 741 new_excluded 732 improved 741
EC49FKP_ALL_1995_EXCLUDED_9_SURVIVORS_PASS
```

The full exactly computed 741-row per-keyset result is 207KB and has SHA256 `47b75aa011aa28825b63f64d832085211f8fc71a9ebf673bc20368a66defd73e`. The source `VERIFY_EC49FKP_PORTABLE.py` Git Blob has been verified against the **actually executed portable file** after publication.

A second check computed exact **per-depth set covers** for **all 741** keysets as binary integer programs (SciPy HiGHS; all statuses optimal), independently agreeing that every integer set-cover layer bound is >= the corresponding combinatorial clique bound; nine unresolved sets give layer-sum 86 or 92 exactly. This is a numerical audit supporting, not replacing, the finite combinatorial proof and full bitset enumeration. A separate NetworkX maximal-clique implementation cross-checked a first group of cases but did not finish all, so the exhaustive verified result uses the portable exact bitset program and the 741-instance integer set-cover audit.

For reproduction: regenerate `EXACT_REPORT_EC49FKO.json` with the sibling `EC49FKO_SIX_KEY_COMPLETE_DEPTH_20261111/VERIFY_EC49FKO_PORTABLE.py` and the already published frozen original `EC49FGW_RADIUS5_SCREEN.py` (in the EC49FJD source package). Then run `python VERIFY_EC49FKP_PORTABLE.py`; its input folder and FKO report may be explicitly set via `EC49FKM_INPUT_DIR` and `EC49FKO_REPORT`. Original scripts, exact full 2004+741 reports, frozen TSV/generator, independent secondary checker/log and SHA256 manifest are preserved in conversation evidence archive `EC49FKP_six_key_1995_excluded_9_survivors_evidence_20261111.tar.xz`, archive SHA256 `449a8117455a0c83858ac36d67c036966c089892b3e6572b70200a57ed4f6e0b`.

## Next scientific unit and actual Source status

For the nine explicit surviving sets, investigate *cross-depth prefix coherence* and exact joint-prefix union optimization, beginning with the eight depthwise-92 instances. A necessary new lower bound of 94 for each would finish the six-key obstruction. In parallel, explore legal seven-key 93-prefix constructions by direct search and larger-than-seven-word replacements.

No authenticated native CLAIM or formal Result is asserted. The private native gateway returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` and `operation_sent=false`; GitHub author-side research publication remains independently available. Current PR is Draft; independent Driver mathematical review remains pending. P000 and ACTIVE worldview are unchanged.
