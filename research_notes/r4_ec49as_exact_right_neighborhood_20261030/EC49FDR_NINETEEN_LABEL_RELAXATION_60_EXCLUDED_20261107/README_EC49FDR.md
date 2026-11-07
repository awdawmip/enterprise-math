# EC49FDR — Exact 19-label signed-X6 prefix relaxation excludes 16 remaining critical-key exchanges

Date: 2026-11-07. Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Parent problem: construct an H2–H9 system with ≤93 **ordered signed primitive X6 prefix edges**, exact per-horizon path quotas, rational observation rank 9 in every horizon, and exactly five complete positive BRC cache keys. P000 and ACTIVE worldview remain unchanged. This is an author-side finite proof-by-exhaustion with a reproducible exact integer dynamic program, pending independent review and Source-native Result admission.

## Main result (fixed H2/H3 seed and one critical-last-key exchange)

Freeze six earliest words: H2=`de,ed,ce,ec` and H3=`feg,gef`. Their union has exactly **42** distinct nonempty ordered signed-X6 primitive prefixes. For each of the original four EC49FAJ key-set families 1512, 1513, 2200, 2203, retain its first four distinct full BRC cache keys and replace only the fifth H9-essential key by one of the 15 distinct EC49FDO rank/slot/key-occurrence feasible replacements. There are 4×15=**60 named family/key replacement events**.

**Theorem.** Every one of these 60 events requires **at least 94 signed native prefix edges** under the original full 22-path requirements, and therefore does not achieve the 93-edge target. The four *unmodified* baseline five-key sets have 94-edge explicit witnesses (EC49FDN); the exact optimum over the union of those four originals and the above 60 exchanges is **94 edges**. Other early seeds, changes to more than one key, or exchange of a different key remain open.

Proof combines disjoint previously verified finite ranges with the present new exact relaxation: EC49FDP excluded 28 exchanges using H8/H9 six-label prefix lower bounds >93; EC49FDQ excluded the 16 additional z=1 exchanges with full 0–1 integer optima >93; this run derives and computes stronger 19-label lower bounds ≥106 for the **16 remaining z≥2 exchanges**. These are counts of family/replacement events, not necessarily deduplicated isomorphism classes.

## Exact 19-label relaxation

For a full positive BRC key `(x,y,z)` and horizon `h`, all operation words are generated from frozen counts

`a=z−1; e=z; c+d=x+y−h−1; f=h+1−y−2z; g=h+1−x`

with every nonnegative c/d split, all word orderings, and the unchanged nine-state DFA with six accepted signature bits 1,2,4,8,16,32. Each operation is expanded to its *ordered signed primitive X6* steps via the unchanged PRIM mapping of EC49FDQ. An edge is a distinct nonempty signed-primitive prefix; the seed's 42 prefixes are prepaid.

For the remaining 16 new keys, the retained early-key sums satisfy `x+y≤8`, and the new key satisfies `x+y=10`. Consequently every H8/H9 selected word must use the new key. The frozen observer language permits H8 signatures 1,2,4,8 and H9 signatures 16,32. Exact rank 9 and 4 H8 + 2 H9 word quotas therefore force one of each signature. Every H7 with only two words and rank 9 must contain both 16 and 32. Likewise, the H6 two-slot horizon and one earlier two-slot horizon (H5 for 1512/1513; H4 for 2200/2203) each require signatures 16 and 32; the remaining earlier four-slot horizon must hit four rank clauses 18,20,33,40. The three retained nonseed full keys must each occur in a selected H4–H9 word.

These conditions yield 19 mandatory Boolean coverage labels: 8 labels from H7/H8/H9, 3 from occurrence of the three retained nonseed keys, 4 from two H6 and two earlier-two-slot signatures, and 4 from the rank clauses of the earlier-four-slot horizon. They are necessary for every original legal solution, but the relaxation omits exact word-count quotas outside the conditions described. This can only decrease the optimized prefix cost.

Construct a trie of **all accepted signed-native complete words** in the relevant H4–H9 horizons, assigning to a terminal its mask of any of the 19 labels that its word realizes. Distinct candidate words that coincide in signed-primitive path may share the same terminal and their label masks may be ORed (this is a legitimate relaxation). Define `D_u[m]` as the minimum total charged primitive prefix-edge cost of a selected terminal set inside the subtree rooted at node `u`, with combined label mask `m`. Include an empty choice of cost zero and the node terminal choice of cost zero. For children `v`, combine via

`D_new[m ∨ n] = min(D_new[m ∨ n], D_old[m] + D_v[n])`.

At each nonroot node charge its incoming edge once whenever its mask is nonzero, except if that primitive prefix belongs to the prepaid seed. By induction over trie height, the recurrence gives the **exact minimum for the 19-label relaxation**. Thus for each new key `K`, the original cost obeys `C_full(K) ≥ 42 + D_root[2^19−1]`.

## Actual finite results

| Original family | Replacement fifth full BRC key | Lower bound for full edge cost | Accepted candidate words | Trie primitive edges |
|---|---|---:|---:|---:|
| 1512 | (6,4,2) | **110** | 9896 | 66977 |
| 1512 | (7,3,2) | **106** | 14216 | 97115 |
| 1512 | (8,2,2) | **110** | 9896 | 68780 |
| 1512 | (8,2,3) | **118** | 10736 | 82681 |
| 1513 | (6,4,2) | **110** | 9896 | 68780 |
| 1513 | (7,3,2) | **106** | 14216 | 97115 |
| 1513 | (8,2,2) | **110** | 9896 | 66977 |
| 1513 | (8,2,3) | **118** | 10736 | 82681 |
| 2200 | (6,4,2) | **106** | 9833 | 66977 |
| 2200 | (7,3,2) | **106** | 14153 | 97115 |
| 2200 | (8,2,2) | **114** | 9833 | 68780 |
| 2200 | (8,2,3) | **118** | 10673 | 82681 |
| 2203 | (6,4,2) | **114** | 9833 | 68780 |
| 2203 | (7,3,2) | **106** | 14153 | 97115 |
| 2203 | (8,2,2) | **106** | 9833 | 66977 |
| 2203 | (8,2,3) | **118** | 10673 | 82681 |

New computed bounds are 106 (6 cases), 110 (4 cases), 114 (2 cases), 118 (4 cases). These 16 exact finite lower bounds, together with prior 44 excluded exchanges, complete the **60/60 critical-key single-exchange exclusion** for the declared early-seed family. The smallest new bound is **106 > 93**.

## Reproducibility, scope, and next task

`EC49FDR_RELAXATION_DP.py` contains the unchanged six-axis primitive/DFA/complete-key enumerator from EC49FDQ and the new 19-label integer trie DP, runnable with Python standard library. `EXACT_REPORT_EC49FDR.json` stores all 16 objectives, full input keys, counts, science pin, and verification metadata. It was actually executed on all 16 combinations and rerun with a distinct `PYTHONHASHSEED`; all objective values, candidate counts, and trie sizes agreed. Separate four-family unchanged original-key regressions returned **94** for the relaxation, matching the prior explicit 94-edge witnesses. Only the finite author-side computation and proved recurrence are claimed; no independent full proof-checker certificate or Source-native Driver acceptance has occurred.

**EC49FDS next research unit:** jointly search *new H2/H3 path systems and at least two late BRC keys*, retaining six-axis native signed-order provenance, five global complete cache keys and the frozen observer. Explore the original 94-edge witnesses' early-prefix sharing geometry; the present no-93 result is confined to the 60 fixed-seed single-critical-key exchanges.

Source predecessors: EC49FDO screening `SCREEN_EC49FDO.py`; EC49FDP exact H8/H9 lower bound and certificate; EC49FDQ full z=1 exact MILPs and freeze-pin implementation; immutable author predecessor `9eb422ab5476e11583f4dbafd65c6d423b3b1a21`. Repository: `awdawmip/enterprise-math`, PR #1730 author branch.