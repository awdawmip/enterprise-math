# EC49FNJ — Exact original BRC seven-key radius-three configurations 27500–28499

**Date:** 2026-11-13. **Status:** author-side, finite, exact computation; not an independent Driver review or native Result. **Predecessor:** [EC49FNI / PR #2266](https://github.com/awdawmip/enterprise-math/pull/2266). **Frozen science:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (not rebased).

## Exact finite optimization result

Maintain the original nine-state BRC operation grammar, its 178,850 original lawful words, 94 complete cache keys and 24 observation labels. There are 38,169 indexed seven-key radius-three configurations; this report covers **all indices 27500 through 28499 (1000 cases)**. Each path uses its **ordered, signed, native-X6 microsteps**, with branch identity and source lawful-word provenance. The cost `C(K)` is the number of *distinct nonempty original signed-native prefixes* in selected legal words covering all 24 observations.

The complete exact C++17 first-step trie / demand-subset DP emitted 1000 contiguous records and an explicit `FINISHED` receipt. The finite result is

```text
min_{27500 <= i <= 28499} C(K_i) = 115
```

Precisely two configurations attain 115:

| Index | Seven complete cache-key indices | Optimal used-root costs |
| --- | --- | --- |
| **27511** | [0,4,5,11,26,43,46] | 05:52 + 06:63 = **115** |
| **27523** | [0,4,5,11,26,43,58] | 05:52 + 06:63 = **115** |

The one-key substitution is **46 → 58**. The maximum for this interval is **138**, attained by **712** configurations. Assignment-optimum counts returned by the solver have histogram **{1:951, 2:47, 3:2}**; both minimizers have exactly one optimal root-demand assignment. The entire interval's cost vector is losslessly embedded in `EXACT_COMPACT_EC49FNJ.json`. The raw optimizer output SHA256 is `41d64f1eb67ef6bf5edae2ec994fbf0a12fd1247ee3efb8e36cc2c817adfd192`.

For each minimizer, reconstructed 24 source-lawful BRC words cover all 24 labels and realize 115 distinct native prefixes. Full witnesses are represented compactly by the label/word arrays in the certificate; the 24 original words are not replaced by abstract coordinate paths. Four independently recomputed Python trie/subset-DP test cases matched the C++ outputs: 27500→138, 27511→115, 27523→115, 28499→138. All 1000 C++ records were completely checked for continuity, but not recomputed independently in Python.

## New finite structural theorem: eight envelopes suffice for a strict gap

In each minimizing case, first-step roots 05 and 06 cover **disjoint** 12-label sets; root 07 can take only the 8 labels `Q=[5,7,11,13,15,17,19,21]` (these are *catalogue label indices*, not axis names). Let `f_r(S)` be the exact root-r nonempty-prefix minimum for required labels `S` (incidental coverage is allowed). For any transfer `T⊆Q` to root 07 define

```text
B_K      = f_05(L_05) + f_06(L_06) = 115
S_K(T)   = f_05(L_05)-f_05(L_05\T) + f_06(L_06)-f_06(L_06\T)
G_K(T)   = f_07(T)-S_K(T)
F_K(T)   = B_K+G_K(T)
a_k      = min_{|T|=k} f_07(T)
b_k      = max_{|T|=k} S_K(T)
```

For *every* finite root system with these roles, `G_K(T) ≥ a_k-b_k` for `|T|=k`: subtracting at most `b_k` from at least `a_k` proves it. This separate-envelope lower bound is exact integer arithmetic, with no submodularity assumption.

The frozen original C++ root-function arrays for each minimizer yield:

| `|T|=k` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 27511: `a_k-b_k` | 4 | 2 | 2 | 2 | 3 | 4 | 9 | 13 |
| 27523: `a_k-b_k` | 5 | 2 | 2 | 2 | 3 | 4 | 9 | 13 |

**All eight cardinality classes have lower bound at least two**. Thus for each of the two configurations `G_K(∅)=0`, and `G_K(T)≥2` for **all 255 nonempty transfers**, without requiring any coupled-mask comparison for the proof of the lower bound. The exact tabulated transfer `T={11,13,15,17}` (bitmask 60) realizes `G_K(T)=2` in both cases. Therefore:

```text
min_{T ⊆ Q, T ≠ ∅} G_27511(T) = min_{T ⊆ Q, T ≠ ∅} G_27523(T) = 2
```

The empty transfer is the **unique optimal first-root demand allocation**, but not necessarily the unique 24-word realization. The two configurations have different root subset-cost functions: their 256 transfer gap values agree on 122 masks and differ on 134, while preserving both the exact minimum 115 and strict gap two. This is a finite example of **strict-gap stability under a single cache-key substitution without full internal root-function equivalence**.

The original root-table SHA256 hashes are 27511: `9c5abaf40293f22362d31611ca20852af1baa239588c2e3f49d358d1fef655bd`; 27523: `7783680b17957d041a63c0232b972ecf13d6e1ca99b310efe32eb399fcfe534e`. Recompute those tables from the frozen master with the archived `DUMP_ROOTS_EC49FNJ.cpp`, then check the 256 exact values and eight envelopes. The complete original evidence bundle additionally contains all raw 1000 C++ lines, full root tables, each complete 24-word witness (including per-microstep prefixes), source generator, independent Python solver, and input/operation SHA256 manifest.

## Method and provenance

For each selected complete cache-key set, partition lawful source words by their *first signed native microstep*. Make a prefix trie for each root; a trie DP over its terminal observation labels computes exact minimal nonempty-prefix cost for every required label subset (incidental coverage allowed). Enumerate admissible root allocations for 24 labels, minimize the sum of the independent root costs. This is exhaustive finite optimization, not sampling of candidate constructions. The verified master input SHA256 is `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; `cases.json` SHA256 is `d18c8f3177083c5b39ef6c8ca068589042617a2a797b53f98818a427040e4f33`; solver C++ source SHA256 is `6ea17ff267f599c69967b420ebf1a8abe151e587e57b25f599f8ecdfb9f2ecac`.

The mathematical claim's exact domain is the frozen radius-three finite family. Continuous author-side coverage now reaches **28,500 / 38,169** (74.67%); next unfinished index is **28500**, with 9,669 cases remaining. Previously observed minimum across the covered radius-three family remains 86 (indices 21524/21525), while a distinct unrestricted seven-key problem retains a feasible 84-prefix construction.

## Native control and admission

On 2026-11-13 UTC the `RS-EC49AS` exact lookup returned `NO_CANONICAL_PUBLICATION_DIRECTORY` at Source `883cfd5440cbb32ac1c913949ebc3fd97b746695`; no formal execution CLAIM, Result, or mathematical Driver acceptance is asserted for this author-side report. The exact prior scientific input pin is retained. **Next unit:** optimize indices 28500 onward and search for root-local perturbation criteria that preserve the strict two-prefix exclusion gap across substitutions.

Files: `EXACT_COMPACT_EC49FNJ.json` (lossless 1000-cost vector, two source words per label and hashes); `VERIFY_COMPACT_EC49FNJ.py` (lossless decode/native-prefix/witness checks, with optional full root-table checks).