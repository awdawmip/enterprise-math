# EC49FOR — Native cross-root gauges inside the original frozen BRC corpus

Date: 2026-11-14. Continuation: EC49FOQ, [PR #2423](https://github.com/awdawmip/enterprise-math/pull/2423). Scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status: `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`. Independent portable scientific work, no formal Task/CLAIM/Result/Review.

## Main new finding

**The original, frozen 38,169-case BRC corpus contains nonzero cross-root cost gauges.** In particular, three pairs of *distinct* source configurations share the exact named legal-root domain and give the same cost for **every** complete legal root assignment, while their per-root reachable cost functions differ. Thus the absence of such gauges in the entire 966-case domain of EC49FOQ is a property of that domain, not of the frozen corpus as a whole.

All codewords and costs are taken from the frozen original `master_and_radius3_cases.txt`, with SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. It has 94 original signed-prefix key families, 178,850 codewords, and 38,169 original distinct seven-key configurations. The original corpus and C++17 min-plus trie implementation are in the EC49FOQ full evidence bundle and the preceding [EC49FOP PR #2419](https://github.com/awdawmip/enterprise-math/pull/2419); this result does not alter the scientific input.

Let `E_K(l)` be the named permitted-root set for demand label `l` in configuration `K`. Roots are precisely `03,05,06,07`. For root `r`, let `D_r^K(S)` be the minimum number of counted non-root signed-byte-trie vertices covering all named demand labels in `S`. Feasible `S` is the union of the labels forced to `r` with any subset of the optional labels that permit `r`. For a complete legal allocation `rho`, define `T_K(rho)=sum_r D_r^K(S_r(rho))`.

**Verified native witnesses** (orientation is from first case to second; each domain has exactly 144 complete assignments):

| Original case pair | Seven original key IDs, first -> second | Delta D_03 | Delta D_05 | Delta D_06 | Delta D_07 |
|---|---|---:|---:|---:|---:|
| 14361 -> 15331 | `0,2,4,5,22,31,63` -> `0,4,5,12,22,30,63` | 0 | +2 | -2 | 0 |
| 17928 -> 38165 | `0,3,4,5,11,54,77` -> `0,4,5,11,54,77,90` | 0 | -4 | +4 | 0 |
| 24541 -> 38166 | `0,4,5,11,17,54,77` -> `0,4,5,11,54,77,91` | 0 | -2 | +2 | 0 |

Each displayed delta is **identical for every feasible rooted subset**, not just an average, sampled subset or one complete allocation. The equalities are exact integers. The first pair belongs to named-domain block with representative 14355 and optional labels `11,13,15,17,19,21`; the other two belong to block 16943 and optional labels `5,7,15,17,19,21`. The optional root choices of the first block are `11:{05,07},13:{06,07},15:{03,07},17:{03,07},19:{03,05,07},21:{03,06,07}`; those of the second are `5:{05,07},7:{06,07},15:{05,07},17:{06,07},19:{03,05,07},21:{03,06,07}`.

## Proof: rooted-constant transfer criterion

For configurations `A,B` with identical legal-root signatures, suppose that for every root `r` a single integer `c_r` satisfies

`D_r^B(S) - D_r^A(S) = c_r`

for **every** reachable root subset `S`, and that `sum_r c_r=0`. Then for every complete legal assignment `rho`:

`T_B(rho)-T_A(rho)=sum_r (D_r^B(S_r(rho))-D_r^A(S_r(rho)))=sum_r c_r=0.`

The three above pairs satisfy this condition with `(c_03,c_05,c_06,c_07)=(0,+2,-2,0),(0,-4,+4,0),(0,-2,+2,0)`. Since at least one `c_r` is nonzero, their reachable rooted profiles differ. They are explicit original-corpus counterexamples to universal injectivity of the terminal observer on reachable rooted profiles. The proof preserves roots, labels, all feasible subsets, and complete allocation provenance; it does not collapse the rooted state to a total before validating the equality.

## Further exhaustive finite census

The unrestricted frozen corpus has 625 different 24-label named legal-root domains. As an independent second region beyond the 966-case EC49FOQ block, this run exhaustively covered **390 additional complete domains**: every domain of size <=4 (388 domains), plus the **entire** domain blocks with representatives 16943 (310 configurations) and 16995 (242 configurations).

Across these 390 blocks, there are exactly **1,477 configurations**, **231,028** native reachable root-cost entries, **605,023** complete-assignment cost evaluations, and **77,963** unordered *within-domain* configuration pairs. Grouping by exact full terminal vectors yields **3,518** equal pairs; grouping by exact complete rooted vectors yields **3,515** equal pairs. The difference is **3**: exactly the three nonzero gauge pairs above within these blocks. The 14355 domain has 4 cases, 3 terminal classes and 4 rooted classes; the 16943 domain has 310 cases, 139 terminal classes and 141 rooted classes. All remaining 388 covered domains have zero terminal-equal/root-different pairs.

Full-family enumeration is finite and exact, with no floating point or hash-based equality. Each domain is based on all seven original key families and all 24 named label-root supports. Per-root costs use the *native* signed-byte-trie min-plus union-mask recurrence from EC49FOP. The complete 1477-case scan was divided into 1230 wholly completed blocks from the initial collector and a separately completed 247-case remainder; one truncated last block (37612) was discarded from the first collector, then recomputed in the clean remainder. Only complete, unique root/mask sets were accepted. `VERIFY_EC49FOR_FULL_CLASSES.py` checks membership and completeness, equality of root profiles, full allocation costs, and exact pair counts. Independently, `EC49FOR_INDEPENDENT_TRIE.py` rebuilds the original byte tries in Python and checks all feasible rooted masks and all 144 complete allocations for each of the three named witness pairs; all six native configurations passed. A complete original-input, CSV, code, logs and digest evidence archive was delivered separately as `EC49FOR_NATIVE_GAUGE_EVIDENCE_20261114.tar.xz`.

## Scope and next question

These three witnesses settle **existence in the frozen original corpus** and the reported 390-class counts; EC49FOQ's prior 966-case same-domain injectivity remains intact. There remain 234 named legal-root classes outside the present 390 plus the EC49FOQ class (234 = 625-390-1), including larger classes. Next: enumerate the remaining domain blocks by full rooted signatures and test for genuine higher-order, nonconstant-in-S gauges; keep the named-root, signed-prefix and provenance interfaces.

P000 and the six-axis Heartbeat World premise remain unchanged. The scientific result concerns the specified BRC signed-prefix model's terminal versus rooted observer, without extrapolation to arbitrary future state operations.
