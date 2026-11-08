# EC49FEC — Exact H5 mixture comparison in twelve quota-feasible BRC triples

Date: 2026-11-08; status: **author-side finite/exact calculation, pending independent Driver review and Source-native task admission**. Continuing EC49FEB, with frozen scientific input commit `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, original nine-state observer, literal six typed operation alphabet, signed X6 primitives and full positive BRC keys. Account normative read: `awdawmip/chatgpt-global-knowledge main@a1bb513ee83f0c88387f8c79e578a5714b670c24`; Source main: `awdawmip/enterprise-math main@4d4ea3c543ec82db371a9f920d771dcc1e620906`.

## Finite proposition and method

For each of the **twelve** triples

[
 A\in\{(3,2,1),(4,1,1)\},\quad
 B\in\{(3,4,1),(4,3,1),(5,2,1),(5,2,2),(6,1,1),(6,1,2)\},\quad
 C=(6,4,1),
]

fix a concrete valid **20-word context outside H5**: H2 has four words, H3 two, and H4/H6/H7/H8/H9 have 2/2/4/4/2. The exact fixed word lists, both optimal H5 completions and their complete 24-path certificates are in the evidence bundle. Compare two admissible selections for the remaining four H5 words: (i) all four have full key B, (ii) at least one B and at least one C. The respective minima are over *every* literal admissible H5 word, with the other 20 words held exactly fixed; they are not global H2–H9 lower bounds.

The original observer's nonzero terminal signatures are `{1,2,4,8,16,32}`; its rank-nine predicate is
`(mask&18) and (mask&20) and (mask&33) and (mask&40)`.
Both eligible keys B and C support only signatures `{1,2,4,8}` in H5. Consequently, with exactly four distinct H5 words the rank predicate forces **exactly one word of each signature**. The full four-dimensional finite product of candidate pools is therefore exhaustive. The study first enumerated all multiset permutations of `a,c,d,e,f,g` with the original state automaton, the signed displacement constraint and full key `(x,y,z)`; then minimized the union of literal signed native-step prefixes. A separate literal-word enumerator recomputed all twelve minima and verified each resulting 24-word system.

For `h=5`, every candidate has `n_a=z-1`, `n_e=z`, `n_c+n_d=x+y-h-1`, `n_f=h+1-y-2z`, `n_g=h+1-x`; the split between c and d is exhaustively enumerated. The length identity is `L(k)=2(x+y+z)-2`. For a fixed set F of outside native prefixes and selected H5 words W, the objective is `|F ∪ ⋃_{w∈W} Pref(native(w))|`. Exact bitset cardinality was used, with no floating-point approximations.

## Exact results for the twelve *specified fixed contexts*

Rows are A family 0/1, followed by B option 0..5 in the order above. The first cost is the exact optimum with H5 all-B, the second the exact optimum with H5 B/C mixed. The final column is mixed minus all-B.

| A index | B index | all-B | mixed | delta |
|---:|---:|---:|---:|---:|
| 0 | 0 | 133 | 142 | 9 |
| 0 | 1 | 110 | 122 | 12 |
| 0 | 2 | 117 | 129 | 12 |
| 0 | 3 | 143 | 147 | 4 |
| 0 | 4 | 148 | 159 | 11 |
| 0 | 5 | 154 | 158 | 4 |
| 1 | 0 | 148 | 159 | 11 |
| 1 | 1 | 114 | 126 | 12 |
| 1 | 2 | 113 | 125 | 12 |
| 1 | 3 | 154 | 158 | 4 |
| 1 | 4 | 133 | 141 | 8 |
| 1 | 5 | 143 | 147 | 4 |

Across all twelve fixed contexts, the exhaustive enumerator evaluated **7,447,104 distinct four-word H5 choices** (all-B or genuine B/C mixtures). Within these twelve **explicit fixed contexts**, allowing a genuine H5 mixture costs between **4 and 12 additional native prefix edges** relative to the all-B minimum. This is a new local result delimiting the EC49FEB mixing route. It leaves the simultaneous optimization of the other 20 words and H2/H3 structure open.

The exhaustive product sizes per B option are: all-B `4096,746496,746496,497664,4096,497664`, and genuine B/C mixtures `9488,289488,289488,314544,9488,314544`; the same cardinalities occur for both A options. Candidate counts are derived from distinct literal complete words, not signatures treated as interchangeable.

## A new full valid construction: 109 native prefix edges

A reproducible joint coordinate-descent search (not an exact global solver) produced a strictly better **109-edge** complete H2–H9 witness in the newly quota-admissible family `A=(3,2,1), B=(4,3,1), C=(6,4,1)`. List every original operator word, grouped by window:

```json
{
  "2":["ce","ed","ge","ec"],
  "3":["feg","gef"],
  "4":["fegg","gefg"],
  "5":["gefgd","feggd","feggc","gefgc"],
  "6":["feggfg","gefgfg"],
  "7":["gefgdfd","feggddf","feggcfc","gefgccf"],
  "8":["gefgdfgf","feggfgfd","feggcffg","gefgfgfc"],
  "9":["feggfgfgf","gefgfgffg"]
}
```

The independent verifier expands every literal operation into its exact signed native X6 steps and recomputes the five distinct positive BRC keys, endpoint displacement `(+2,0,0,0,0,0)`, window quotas, rank predicates, exact native Trie edge cardinality and the 24 distinct complete words. Its computed result is **109 edges**, with all checks passing. This improves the present newly isolated 12-family constructive witness from its 110-edge fixed-context seed; the separately established full mother-problem best witness remains **94** edges.

## Reproduction and evidence

The full executed exploratory sources and raw witnesses are preserved in the conversation research evidence bundle `EC49FEC_complete_research_evidence.tar.xz`; the repository includes the self-contained `VERIFY_EC49FEC.py` and `EC49FEC_FIXED_CONTEXT_CERTIFICATES.json`, plus the exact operator-Trie proof `OPERATOR_TRIE_IDENTITY_EC49FEC.md` and its separate checker `VERIFY_OPERATOR_TRIE_EC49FEC.py`. The bundle contains the actual executed `EC49FEC_H5_FIXED_OPT.py`, `EC49FEC_JOINT_HEURISTIC.py`, `EC49FEC_INDEPENDENT_VERIFY.py`, `EC49FEC_RESULTS.json`, `EC49FEC_JOINT_WITNESSES.json`, `EC49FEC_INDEPENDENT_REPORT.json`, plus the frozen previous enumerator support files `EC49FDV_NATIVE_WITNESSES.py`, `EC49FDU_THREE_PHASE_RANK.py` and `EC49FDV_QUOTA_SCHEDULES.json`. These are standard-library Python programs, except the inherited support scripts as stated in their own source. The independent checker ran to completion, reporting **12/12 exact contexts, 24/24 conditional 24-word certificates and 5/5 joint-search 24-word certificates**, lowest joint cost 109. The joint-search run was interrupted after recording five valid candidates; it makes no claim of exhaustive global optimization.

## Remaining scientific question

The mother target remains a **legal complete 24-word H2–H9 system, with at most five full positive BRC keys, nine-state rank 9 per window, and ≤93 distinct signed native primitive prefix edges**. Retain the 94-edge global witness. Next: optimize the 44 newly quota-admissible triples jointly with early H2/H3 paths, test genuinely mixed H5 with jointly variable outside words, and use exact MIP or a lower-bound certificate on shortlisted key schedules. A fixed-context mixed-H5 penalty does not imply a general mixed-H5 impossibility.

## Storage, identity, authority

GitHub identity for this run: authenticated login `awdawmip`, repository write permission present. Source-native gateway `em_status`/`em_control_tasks` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, with `operation_sent=false`. No authenticated Source-native CLAIM, owner selection, Result, independent Driver review or admission is asserted. This manuscript and its evidence are author-side on PR #1730 until reviewed and admitted through native Source.
