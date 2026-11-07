# EC49EXY — Frozen-observer exact cross-fiber signed-X6 prefix capacities

**Date:** 2026-11-04. **Status:** AUTHOR_ANALYTIC_THEOREM / EXACT_FULL_FINITE_CENSUS_PASS / INDEPENDENT_CAP_AUDIT_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. **Parent:** EC49EXX at immutable `2499df0da76fa7d16c6958068ee061a4994a84c2`, Draft PR #1730. **Frozen scientific inputs:** account global `773d538180bfb49e24cffeb35c3ee75eb0628e2e`, Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. P000 and ACTIVE Heartbeat World remain unchanged.

## Target and preserved semantics

Exact finite mother model: seven ordered operation codes over signed *primitive* native six-axis steps (the `a,c,d,e,f,g` words used when `#b=0`), windows h=2,…,8; one **complete six-axis positive-step BRC key** K=(u,v,w,0,0,0) and frozen nine-history observer family T2 or T4 at each horizon; exactly five globally distinct K and ≤6 observation matrices. Cost E is the number of distinct nonempty signed primitive-step prefixes in the selected paths (including the 28 base prefixes). Every full key, operation order, signed primitive axis and observation signature is retained. The limited support on axes E1…E3 is explicitly a restricted typed X6 computation, not a 3D replacement worldview.

Previously published EXS independently screened all 1,989,509 feasible arrangements with the coarse cross-key histogram bound `I(K,K')=2(Σ min(K_j,K'_j)−1)` and signature-aware same-key lower bounds. EXX subsequently eliminated every triple-collision schedule by exact DP, leaving **44,234 double-collision arrangements** that were not excluded by EXS. Their existence as candidates did not imply feasibility.

## Theorem EXY-1 — Exact typed cross-fiber prefix capacity

Define `F(h,K)` to be **all** legal native signed paths at horizon h carrying K whose exact nine-history signature is one of the required T2/T4 signatures for this h and K. These are exactly the finite sets emitted by the frozen `SCREEN_H5_EC49EXJ.py:words(h,K,t)` source (SHA1 Git Blob `0e83eac43199e5854d462d1928aba6a146db5261`). Let

`C((h,K),(g,K')) = max_{x∈F(h,K), y∈F(g,K')} LCP_signed_primitive(x,y)`.

For different full keys, `C≤I(K,K')`; equality is **not** automatic. For disjoint complete-key groups A and B of horizon sets H_A,H_B, put

`C(A,B)=max_{h∈H_A,g∈H_B} C((h,K_A),(g,K_B))`.

This is a valid upper bound on the longest primitive-step prefix shared by **any** actually selected paths belonging to those two groups, even with future signature and cache choices, since the bound maximizes over the complete necessary word families. It is exact at the level of candidate word pairs, not an assertion of simultaneous feasibility of a whole schedule.

At depth d, denote by `q_A(d)` the previously proved EXS minimum number of distinct prefix nodes required by all signatures of the key group A: `q_A(d)=1` at earlier positive depths, `M_A−ν_obs(A)` at depth L_A−3, and `M_A` at depths L_A−2,L_A−1,L_A, where `M_A=Σ_{h∈H_A} (2 or 4)`. For depth exceeding L_A, put `q_A=0`. At depth d build the graph G_d on the five complete-key groups, with edge AB iff `C(A,B)<d` (so their actual depth-d nodes cannot overlap). Then every clique Q gives at least `Σ_{A∈Q} q_A(d)` distinct nodes. Consequently

**`E ≥ B_EXY := Σ_{d=1}^{L_max} max_{Q clique in G_d} Σ_{A∈Q} q_A(d)`.**

The proof follows directly by partitioning the union of distinct signed-prefix nodes at each depth and summing its cardinality. Taking C instead of I only adds incompatibility edges: **`B_EXY≥B_EXS` pointwise for every schedule**. The EXS intra-key T2/T4 observer matching bound and its finite coverage assumptions are reused unchanged. The new statement is a necessary cost lower bound; it does not claim a witness when the bound is below 80.

## Complete exact finite construction

Window-key pairs number 1+4+9+17+28+43+62=**164**. Generate all words using the unchanged frozen native operation/signature implementation: **163,888** observer-admissible signed paths. Insert them into one signed-axis prefix trie (**639,353** nodes including root). Every nonroot node stores the bitset of families reaching it. For any two families, the deepest shared node is precisely their maximum possible LCP: thus all **13,366** unordered family-pair capacities are computed completely without random sampling or floating point. Among pairs with distinct full keys, **10,544** have strict improvement `C<I`.

For the 40 possible cache-collision skeletons (eight triple and 32 double), `SCREEN_EC49EXY.cpp` enumerates all **1,989,509** full-key arrangements, derives the groupwise capacities by maxima of the pair-family table, recomputes the old EXQ and EXS checks as control values, and then calculates each depth's largest clique weight by all 31 nonempty subsets of five keys using integer arithmetic.

| collision type | all schedules | EXS still potentially E<80 | EXY still potentially E<80 | newly excluded by EXY |
| --- | ---: | ---: | ---: | ---: |
| triple | 123,147 | 946 | 24 | 922 (already covered by EXX's separate full-DP proof) |
| double | 1,866,362 | **44,234** | **12,356** | **31,878 new exclusions** |
| total | 1,989,509 | 45,180 | 12,380 | 32,800 (includes 922 redundant triple cases) |

Therefore **31,878** previously unresolved double-collision schedules are now rigorously excluded from E<80, provided the frozen generator/observer semantics and previously proved EXS intra-key capacities. The remaining global unresolved schedule count is **12,356 double-collision arrangements**: all triple-collision arrangements were separately disposed of by EXX. The existing rigorous mother bound **63≤E*≤80** does not change.

A concrete new exclusion: pairs (h2,h3) share K=(3,1,1), (h4,h5) share K=(3,3,1), and h6,h7,h8 use respectively (3,4,1),(3,5,1),(5,7,1). The EXS lower bound is 79; the exact EXY bound is **82**, so it cannot realize E<80. Input is an **exact schedule**, not an example path witness.

## Executed checks / reproducibility

The generator script `GENERATE_EC49EXY_CAPS.py` uses the unchanged sibling EC49EXJ `words` implementation and produces `EC49EXY_CAPS_TABLE.txt`; generated table SHA256 is **`7303fceb0299f7bf1ce0c53c950b680a8d0cef4a0737cafbd2d6f75b90402129`**. Independently, the sorted-two-fiber merge implementation checked all **13,366** pair capacities against the trie matrix and matched every entry. The full C++ screen regenerated EXQ/EXS base counts and yielded the census above; a second Python depth-by-depth clique implementation checked **133** explicit complete double schedules (123 survivors and 10 new exclusions), all PASS. The complete census JSON SHA256 is **`27c2ec3d601e4fe327474c4687549fe75f1ef7c04b5ecfdfc59d1dcfc49565dc`**. These hash strings identify files only; they are not proof by themselves.

In repository root relative to this folder, recreate caps and census with:

```sh
python3 GENERATE_EC49EXY_CAPS.py
python3 INDEPENDENT_CAP_AUDIT_EXECUTED.py
# C++17; supply exact previously published EXS signed-signature matching table
g++ -O3 -std=c++17 SCREEN_EC49EXY.cpp -o screen_exy
./screen_exy ../EC49EXS_H8_M5_OBSERVER_SIGNED_MATCH/EC49EXS_MATCH_TABLE.txt EC49EXY_CAPS_TABLE.txt > EC49EXY_EXACT_CENSUS.json
```

The submitted Python independent audit and schedule rechecker scripts used local archive paths in the original run; adapt their relative paths to the published sibling directories (or extract the complete accompanying evidence archive). Reproduction of raw signed words uses the **original repository EC49EXJ generator**; no foundation/P000 modifications are made. If an independent Driver reviews these counts, they should specifically verify that the EC49EXJ T2/T4 signed word family is complete and the EXS same-key matching bound applies to this finite model; a numeric match alone does not establish those dependencies.

## Unresolved unit — EC49EXZ

For the **12,356** remaining double-collision schedules, use exact `C` bounds for staged h≤7 private-suffix screening and then native signed-prefix OR-mask integer DP. Prioritize families with few legal words, deduplicate identical typed DP inputs, and demand an explicit full primitive-edge path witness (and all nine-history signatures) for every claimed E<80 construction; otherwise publish cutoff-80 infeasibility certificates. Retain input hash, actual solver output, scope, timeout states, and the exact unsigned/signed X6 observer bridge. This is a finite next task, not a claim that all 12,356 are feasible.

**Authority:** GitHub author-side only; native Sites returned `research_authority_granted=false`, native control tasks `CONTROL_QUOTA`, hence owner, canonical CLAIM/Result, and independent Driver admission are not confirmed. No canonical main or protected worldview changes were made.
