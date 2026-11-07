# EC49FDT — Three late BRC keys: complete rank-feasibility census and eight exact rooted schedules

Date: 2026-11-07. Status: AUTHOR FINITE COMPUTATION + CONSTRUCTIVE EXACT FRACTION CHECK; SOURCE-NATIVE REVIEW PENDING. Frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Previous author stage EC49FDS at immutable GitHub commit `29a48cdfd821f9a0b6ee86c9c6b9d4f79c90dad8`. P000, ACTIVE worldview and all native-X6 semantics remain unchanged.

## Mother objective and chosen subproblem

The H2–H9 target is an ordered *signed primitive X6* path-family with displacement (+2 E1), a global budget of **five distinct complete positive BRC keys**, six allowed nine-history observer signatures, rational observer rank 9 at every horizon, stated path quotas, and **at most 93 distinct nonempty signed-native primitive prefixes**. Prior four explicit EC49FAJ solutions cost 94. EC49FDS identifies eight H2-three/H3-two seeds consuming just two positive BRC keys and costing four times 31 and four times 35 early edges. This unit studies their remaining three full-key slots.

Exact frozen operation alphabet: `a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`, with each integer a signed **native primitive-axis label**. The zero-positive operation `b=(-2,-2)` cannot occur in valid target-displacement words. For horizon h and key (x,y,z), exact operation counts are `a=z-1, e=z, c+d=x+y-h-1, f=h+1-y-2z, g=h+1-x`. The nine-state T4/T2 finite observer uses original EC49FDS `TRANS`, six signature bits 1,2,4,8,16,32, and rank-nine equivalent four clauses 18,20,33,40. Every signed primitive prefix is charged once globally.

## Theorem A — exact rank coverage across all three-key late sets

The union of complete keys with at least one signature-admissible word at an H4–H9 window consists of **155 keys**. Exactly **124** unordered key pairs support observer rank 9 at every H4–H9 horizon. There are C(155,3)=**608685** triples. Exactly **23728** triples support rank 9 at all six windows; **16994** contain a rank-feasible pair and **6734** require the third key for *rank feasibility*. This is a complete finite rank/key classification over the stated alphabet, signatures and windows; it does not yet optimize prefix edges or window quotas.

**Proof/certificate:** `EC49FDT_TRIPLE_KEY_CENSUS.py` performs an exact integer DP on six operator counts and the original nine-state observer. It reproduces the earlier EC49FAW horizon counts for every h=2,...,9, then scans each of 608685 triples and verifies all four rank clauses separately at H4,...,H9. Independently, a graph argument checks the 16994 count: make a graph whose 124 edges are the globally rank-feasible key pairs. Any edge has one key available at H4 and another at H9. No full key can be available at both H4 and H9, by EC49FAM lifespan: an H4 key has x+y<=8 while an H9 key has x+y>=10. Thus the feasible-pair graph is triangle-free. Its exact degree-wedge count is `sum_v C(deg(v),2)=1978`; inclusion-exclusion over the 124 edges gives `124*(155-2)-1978=16994`, agreeing with enumeration. Remaining `23728-16994=6734` triples are structurally new rank-only designs.

One genuinely three-key rank-feasible triple is `L=(3,2,1), M=(3,4,1), N=(4,6,1)`, with horizon assignment `H4=L; H5=H6=M; H7=H8=H9=N`. Here the three-key requirement is for the *union of six rank tests*, not a claim about every conceivable two-key model.

## Theorem B — exact scheduled signed-prefix optima for all eight two-key early seeds

Fix the just-named late keys and one key per late horizon as in the assignment above. Select any legal allowed-signature word at each horizon and enforce rank9 per window. Use the eight explicit H2-three/H3-two early seeds from EC49FDS. The exact signed-prefix Trie binary MILP minima, in EC49FDS seed enumeration order, are:

| H2 triple | H3 pair | early edges | signed-prefix optimum |
|---|---|---:|---:|
| ce,ed,ge | feg,gef | 31 | **114** |
| ce,ed,ge | feg,gfe | 35 | **118** |
| ce,ed,ge | fge,gef | 31 | **114** |
| ce,ed,ge | fge,gfe | 35 | **118** |
| de,ec,fe | feg,gef | 31 | **124** |
| de,ec,fe | feg,gfe | 31 | **124** |
| de,ec,fe | fge,gef | 35 | **128** |
| de,ec,fe | fge,gfe | 35 | **128** |

Each optimization used **1180** late accepted words and a **8116-edge** signed-native Trie; HiGHS status OPTIMAL, dual bound matching objective and MIP gap zero on all eight. The linear constraints select terminal signed-word paths with prefix closure and cover the original four observer clauses in every H4–H9 window. Exact word quotas were *not* required by the MILP, but the eight emitted witnesses in `EXACT_WITNESSES_EC49FDT.json` each satisfy quota vector `[3,2,2,4,2,4,4,2]` and exactly five distinct complete positive BRC keys; this matching feasible upper bound proves the same optima with that quota vector as well.

An independently implemented **nine-history full output rank** computation, using Fraction Gaussian elimination on the 9×5m Boolean observer matrix, re-expanded signed primitives and verified all eight witness costs, legal displacement, full BRC keys and all 8×8 rational ranks (see `VERIFY_EC49FDT_FRACTION.py`). This is independent method arithmetic cross-check, not independent Source-Driver authorship/review.

The results discriminate early-prefix geometry: for the same 31-edge early budget and identical three late keys, seed `ce,ed,ge | feg,gef` reaches 114 while `de,ec,fe | feg,gef` requires 124. Early key count and edge count alone therefore do not determine later full prefix reuse.

## Reproduction and exactly claimed scope

Run `python EC49FDT_TRIPLE_KEY_CENSUS.py` (standard library) to reproduce all 155/124/23728/16994/6734 census values and EC49FAW horizon checks. Run `python EC49FDT_FIXED_SCHEDULE_MILP.py` after installing NumPy and SciPy (HiGHS) to recompute the eight fixed-late-schedule integer optima and print their selected witnesses. Run `python VERIFY_EC49FDT_FRACTION.py EXACT_WITNESSES_EC49FDT.json` for independently executed rank/word/prefix checks. Proof of MILP lower bounds uses the exact binary model equivalence and the solver's optimality certificate; a separate formal SAT/Lean unsatisfiability certificate was not produced.

The 6734 truly three-key rank-only sets are a new searchable design space; this fixed late-key schedule has optimum >=114. The 93-edge mother problem remains open, with known 94-edge legal constructions.

## Next EC49FDU

Use the 6734 genuinely 3-key rank-feasible triples to prioritize those with strong compatible early native signed-prefix roots. Jointly optimize horizon key assignment and intra-horizon mixing for the two-key early family, first using cheap provable signed-prefix lower bounds and exact rank/quota feasibility. Compare with changing the early seed beyond the eight classified triples/pairs. Seek a fully certified 93-edge or lower system, or a proved lower bound for a separately specified finite family. Do not turn a failed local schedule into universal impossibility.

## Actual Source/role state

Research content is an author-side GitHub-branch artifact under PR #1730. Native Enterprise Math `em_status` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE` with `operation_sent=false`; current native owner and authenticated CLAIM could not be confirmed. No Source-native Result, independent Driver review or theorem admission is asserted. GitHub identity observed `awdawmip`. No P000 or ACTIVE worldview edit.
