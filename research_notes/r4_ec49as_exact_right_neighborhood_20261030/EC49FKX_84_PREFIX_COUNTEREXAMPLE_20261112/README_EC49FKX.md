# EC49FKX — Explicit 84-prefix seven-cache-key native BRC construction

Date: 2026-11-12. Input pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status: author-side **constructive counterexample** + exact fixed-key subproblem certificate; independent Driver review pending.

## Decisive result (frozen finite model)

**The previously investigated equality `C_min(7)=94` is false in the declared original finite nine-state BRC/X6 optimization problem.** An explicit set of exactly 24 lawful operation words covers all 24 required (window, signature) demands, uses **exactly seven distinct full raw cache keys**, and uses only **84 distinct nonempty ordered signed-X6 native prefixes**:

```
C_min(7) <= 84 < 94.
```

The global minimum over arbitrary seven-key selections is not yet known. This theorem is an upper-bound witness and refutation of the former proposed universal lower bound 94. It does not change P000 or the frozen scientific model.

The seven **full raw** keys, counted as the positive +E1,+E2,+E3 signed microstep multiplicities, are
```
(2,1,1), (3,0,1), (3,1,1), (4,2,1),
(5,3,1), (5,4,1), (6,4,1).
```
The key (5,3,1) replaces (7,4,1) from existing 94-prefix profile A or (6,5,1) from profile B. This is a complete replacement of 24 words, not a radius-5/6/7 restricted change.

### Explicit witness: window, observer signature, original operation word, full raw key

| h | signature | word | key |
|---:|---:|---|---|
|2|16|`fe`|(3,0,1)|
|2|32|`ge`|(2,1,1)|
|3|16|`feg`|(3,1,1)|
|3|32|`gef`|(3,1,1)|
|4|1|`gefd`|(4,2,1)|
|4|2|`fegd`|(4,2,1)|
|4|4|`fegc`|(4,2,1)|
|4|8|`gefc`|(4,2,1)|
|5|16|`fegfg`|(4,2,1)|
|5|32|`geffg`|(4,2,1)|
|6|1|`geffgd`|(5,3,1)|
|6|2|`fegfgd`|(5,3,1)|
|6|4|`fegfgc`|(5,3,1)|
|6|8|`geffgc`|(5,3,1)|
|7|1|`geffgdg`|(5,4,1)|
|7|2|`fegfgdg`|(5,4,1)|
|7|4|`fegfgcg`|(5,4,1)|
|7|8|`geffgcg`|(5,4,1)|
|8|1|`geffgdgf`|(6,4,1)|
|8|2|`fegfgdgf`|(6,4,1)|
|8|4|`fegfgcgf`|(6,4,1)|
|8|8|`geffgcgf`|(6,4,1)|
|9|16|`fegfgffgg`|(6,4,1)|
|9|32|`geffgffgg`|(6,4,1)|

## Direct verification, independent of optimizers

The original nine-state transition table is `T` with operation alphabet `acdefg`. A word starts at state 0; every intermediate state is checked to differ from forbidden state 8; the terminal signature is `SIG[q]`. For every row, the word length is h, the signature is exactly the requested one, and its signed native six-axis displacement is **(2,0,0,0,0,0)**. The 24 pairs enumerate all 24 declared requirements. The seven full raw key triples above are recomputed from every expanded native microstep and checked *exactly*, not shortened/quotiented by projection.

Expand each operation to its original signed native microsteps:
```
a=(-1,-1)
c=(+1,+2,-1,-2)
d=(+2,+1,-2,-1)
e=(+3,+1,+1,-3)
f=(+1,-1)
g=(+2,-2)
```
For each expanded sequence, insert **every nonempty ordered signed prefix**, counting identical signed byte sequences once over all 24 words. The exact union contains **42 prefixes beginning with +E1**, and **42 prefixes beginning with +E2**, totaling **84**; all ordered and signed path identities are preserved. The small self-contained Python standard-library verifier `VERIFY_EC49FKX_STANDALONE.py` verifies these assertions independently of candidate generation, dynamic programming, HiGHS or C++ and prints `EC49FKX_STANDALONE_EXPLICIT_BRC_WITNESS_PASS`.

## Stronger local classification: exact optimum for this fixed seven-key set

For the **fixed seven keys** listed above, enumerate the full original 178,850-candidate catalogue: exactly **5,946** candidates use an allowed full raw key; their native trie contains **26,704** nonempty prefix nodes. The first signed native bytes are 05 (+E1), 06 (+E2), 07 (+E3); root05/root06 have disjoint 12-label supports partitioning all 24 observations, and root07 can cover 8 labels. The exact integer prefix-trie subset-mask dynamic program from EC49FKW yields:

| root05 all | root06 all | root07 all | global optimum | unique root07 assignment | best nonempty assignment |
|---:|---:|---:|---:|---:|---:|
| 42 | 42 | 32 | **84** | 0 (unused) | 92 |

The 256 root07-allocation costs (integer-only, original signed-path representation) have compact JSON SHA256 `da7271a3302f168727085685f3886f45f5d52883afbc284b50ed4d9e5e8a01f8`. Both an executed Python trie DP and independently compiled/executed C++17 implementation agree on **all 256 entries**, not merely the optimum. The existing `EC49FKW_SEVEN_FIXED_KEY_GLOBAL_20261112/INDEPENDENT_EXACT_TRIE.cpp` is directly reusable with the new signed candidate input; the published 84-word witness gives an entirely independent exact upper bound.

Proof of optimizer completeness: each trie terminal is either selected or omitted; each selected ancestor costs one; child subtries combine by OR of demand masks and sum of disjoint prefix costs. Downward superset closure yields exact least cost to cover *at least* each demand subset. Assign every root07-served demand subset T (256 choices); the disjoint root05 and root06 handle all remaining labels. Minimizing the three exact subtrees over all T covers all lawful words using these seven keys. Every root assignment is realizable by combining its three selected local solutions. Therefore `C_min(K)=84` for this **fixed** K. Global key-set optimization can do better and remains open.

## Discovery scope, provenance, and continuation

The experiment replaced one raw key of either old A or old B with each unused key. Among 609 distinct swaps per original profile, 192 per profile retained the necessary full-label coverage, and an exact general-root solver evaluated 116 per profile whose signed first roots were 05,06,07 and partitioned the 24 demands as described. This **bounded search** found fixed-key optima 84, 86 and 92, among other values. The remaining 76 viable swaps per profile involving additional native first-byte roots were not exhaustively optimized in this screen. The 84 result is verified by a standalone direct construction, independently of search completeness.

Frozen source: `EC49FJD_RELEASE_B11_COMPLETE_20261111/{EC49FGW_RADIUS5_SCREEN.py,EC49FGJ_SEVEN_KEY_94_WITNESSES.json}`. Dedicated files include `EC49FKX_EXPLICIT_84_WITNESS.json`, `VERIFY_EC49FKX_STANDALONE.py`, `EXACT_REPORT_EC49FKX.json`, and `MAKE_EC49FKX_INPUT.py`. Reuse the already-published `EC49FKW_SEVEN_FIXED_KEY_GLOBAL_20261112/{VERIFY_EC49FKW.py,INDEPENDENT_EXACT_TRIE.cpp}` and change the allowed-key set to the seven shown here.

**Next discriminating objective**: Find an explicit lawful 83-prefix or smaller seven-key construction, or establish a certified lower bound in a *well-defined* range of alternate key sets; start with additional candidate seven-key combinations and the unclassified root03 cases. Retain all 24 labels, raw full key identity and ordered signed native prefixes. The old 94-as-global-optimum hypothesis is resolved in the negative by the 84 witness, while the global optimal value is open.

Research identity in this run: `EM-DIRECT-39F1ED / TASK_RESEARCH`; Activity `RA-00FEC1D90BEAF87D1F84F3C9`. Native control check for EC49AS returned `NO_CURRENT_IMMUTABLE_PUBLICATION`; author research is saved on Draft PR #1730 without an unrelated claim or formal Result. Independent Driver review pending.
