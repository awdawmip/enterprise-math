# EC49FJC — released-key B=9 reallocation completes radius-six class (2026-11-11)

## Author-side exact finite theorem

Frozen nine-state ordered/signed native X6 BRC input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Two original EC49FGJ 24-observation witnesses A and B each use seven *complete raw cache keys* and 94 distinct native prefixes. For every six-position replacement Q, retain the other 18 witness words; define their ordered signed prefix union F(Q) and their complete-key set K_F.

**Claim.** Among six-position choices that release at least one original complete key and satisfy |F(Q)|=84, there are exactly 7,888 choices for each witness. Each such choice has exact minimum total native-prefix cost **94** over all legal replacements using at most seven complete raw cache keys. Across A and B this covers 15,776 finite subproblems.

**Evidence composition.** Previous immutable source EC49FJA + EC49FJB (at PR #1730 ancestor `62c283edadbdeca90e40fdf91c339d1ee62b26f1`) proves 7,824 forced-seven-key cases per witness. EC49FJC solves their complement: **64 per witness allowing a different cache-key cover at the key-only level**, 128 new finite problems. The exact key-and-prefix union dynamic program gives zero feasible complete states for each of the 128 cases at a 93-prefix target. The original 94-prefix words give the attained upper bound.

## Exact state and recurrence

The nine-state frozen generator EC49FGW enumerates all **178,850** legal operation words and **94** complete raw-key types. Fix one of the 128 reallocation-permitted positions Q, and set B=93-|F(Q)|=9. For each selected observer label i, consider every word w from the full legal catalog satisfying |P(w)\F(Q)| <= 9. Each native prefix P(w) retains microstep **order and sign**; each raw key k(w) is the full frozen key tuple, not a terminal-coordinate alias.

Start from (U,K)=(empty,K_F). For each selected observation i and legal word w, update
```
(U,K) -> (U union (P(w)\F), K union {k(w)})
```
retaining precisely states with |U|<=9 and |K|<=7. At a fixed stage and an **identical complete key set K**, a prefix union U that contains another U' is dominated: for every subsequent sequence of words, |U' union S| <= |U union S|. Consequently keep only inclusion-minimal unions per exact K. All selected labels are processed once in ascending candidate-count order; this order is only a computation choice. An empty final state space is equivalent to infeasibility of a 93-prefix, at-most-seven-key completion for that Q.

Each of 64 Q per witness has an empty final state set; all **128/128** are thus excluded. This is exhaustive within the declared frozen finite catalog, not sampling. It includes cache-key reallocation rather than fixing the original seven keys.

## Executed evidence and scope

Author-side Python runs use frozen `EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` from immutable research ancestor `f1cfadff6d9949c5278195f0b3f5f0f39a42531d`. The exact local runner produces 16 batch reports (eight per witness), plus a consolidated 128-case report in which each record gives the changed position indices, selected labels, number of previously fixed keys, per-layer key-set/state counts, and final zero states. Original report SHA256: `cb528b25f44ed549bd0d724998747857d2136de16694add918ff0e0d83cef09d`; report length 239,269 bytes; source validator uses integer bitsets and exact set inclusion only.

Earlier standalone unrestricted-H8/H9 antichain screening also excluded 34 of these cases per witness; the complete joint cache-key/prefix DP closes all 64 per witness. Author result: `AUTHOR_EXACT_FINITE / UNREVIEWED / NOT_ADMITTED`. No live EC49AS CLAIM, shared Result or independent Driver approval is asserted.

**Next:** classify released-key B=11,15,17,18,23 and the other open six-position backgrounds; retain the global mother question whether a seven-key 93-prefix witness exists.

Reproduction: the compact verifier and exact case report are separate sibling artifacts. Their source input is the immutable EC49FGW generator and FGJ witness set listed above. This record is a finite certificate narrative with explicit state recurrence, not a substitute for executing the verifier.
