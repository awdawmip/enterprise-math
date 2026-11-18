# EC49FGY — BRC five-path radius: exact budget 11–15 exclusion (2026-11-10)

**Research mode:** independent author-side TASK_RESEARCH, not a formal immutable Task/CLAIM or accepted Result. 
**Frozen scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
**Parent frontier:** EC49FGX at immutable commit `d35943eca83482777e0ba376554839891010011c`, using the original nine-state BRC observer, 24 H2–H9 labels, 12 signed native X6 microstep directions and original full raw cache keys.

## Exact finite theorem

Let `W_A,W_B` be the two previously verified seven-key, 94-prefix witnesses. Fix any 19 of their 24 labelled paths, with the other five labels indexed by `Q`. Write `F(Q)` for the union of prefixes belonging to the fixed paths. All original seven cache keys continue to be represented by the fixed paths exactly when no key-support set is a subset of Q. Under this **no-key-release** condition, every allowed replacement path of a <=7-key solution must use one of those same seven full keys.

The budget for reaching at most 93 distinct signed, ordered, nonempty native microstep prefixes is

`B(Q)=93-|F(Q)|=r(Q)-1`, where `r(Q)=#{e: S(e)⊆Q}` and `S(e)` is the set of original paths containing prefix e.

**Theorem.** For either baseline `W_A` or `W_B`, for *every* no-key-release five-label replacement set Q with `11<=B(Q)<=15`, no choice of the five legal replacement paths under the original seven-key constraint has native prefix-union cost <=93.

### Proof and complete-check certificate

For each replacement label i and each legal path w whose full raw key belongs to the fixed seven, compute exactly the new-prefix set `A_i(w)=P(w)\F(Q)`. A completion of cost <=93 is equivalent to a choice w_i for all five labels with `|⋃_i A_i(w_i)|<=B(Q)`.

The program enumerates **all 178850** frozen legal signed paths, of which **9838** use one of the seven baseline keys, and all `binom(24,5)=42504` five-position sets. It derives the exact budget and filters all **3524** no-key-release cases in range 11–15 per witness. Pairwise necessary tests exclude 1458 A positions and 1484 B positions; exact five-way union DP checks the remaining 2066 A and 2040 B positions and rejects **all**.

The DP represents each distinct ordered signed native prefix as a separate bit, and each candidate's genuinely new suffix as an integer bitset. Its state transition is bitwise union; discard a union once its bit count exceeds B. Whenever two intermediate unions satisfy `X⊆Y`, retain only X: for every future set Z, `X∪Z⊆Y∪Z`, so dropping Y preserves exact feasibility. Once all five labels have been processed, the nonempty-state criterion is necessary and sufficient. Enumerated keys, signatures, path lengths and observer transitions come from the pinned predecessor's original validator.

| Profile | Budget 11–15 positions | Pairwise rejected | Five-way exact DP rejected | Budget frequencies of DP rejects |
|---|---:|---:|---:|---|
| A | 3524 | 1458 | **2066** | 11:1376; 12:13; 13:421; 14:214; 15:42 |
| B | 3524 | 1484 | **2040** | 11:1376; 13:408; 14:214; 15:42 |

The independent direct-prefix-set depth-first search (separate catalog construction) verified two deterministically chosen cases per budget and witness (20 total); all reject <=93. This is an author-side finite certificate with executable exhaustive checker, not a separate Driver admission.

## Updated parent frontier

EC49FGX had 7708 (A) and 7682 (B) unexcluded five-position sets. This result newly excludes 2066 and 2040 respectively, leaving **5642 sets for either witness**, partitioned into **744 no-key-release sets with B>=16** and **4898 with key release**. An earlier attempt to run all B>=11 five-way DP timed out in the higher-budget region; no inference is made for those unfinished sets.

The seven-key global classification remains open: `C_min(7)<=94`; seek <=93 by high-budget five-way search, key-release cases, or path replacements outside this local shell.

## Reproduction and durable dependencies

Run `python VERIFY_EC49FGY.py` from this directory. It imports sibling `EC49FGX_RADIUS5_PAIR_FIVE_DP_20261110/VERIFY_EC49FGX.py`, which in turn imports sibling `EC49FGW_RADIUS5_EXACT_SCREENS_20261110/EC49FGW_RADIUS5_SCREEN.py` and its exact witness JSON. All are pinned by predecessor `d35943eca83482777e0ba376554839891010011c` and carried forward unmodified.

The JSON file alongside this README is a report of the executed finite test. The additional local evidence archive contains the exact independently executed B11/B11–15 implementations, intermediate logs and a separate direct-DFS cross-check. Final program output: `EC49FGY_EXACT_PASS`.

**Native role:** `EM-DIRECT-D2A6A9 / TASK_RESEARCH`; activity `RA-61301ABEE99A8F28B80CC4D7` was registered and Source-read-back. No formal EC49AS owner/CLAIM, RR or independent Driver mathematics admission is asserted.
