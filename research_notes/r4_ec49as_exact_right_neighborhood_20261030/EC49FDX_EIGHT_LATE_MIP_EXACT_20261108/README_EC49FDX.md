# EC49FDX — Eight exact conditional H7–H9 prefix minima

2026-11-08 (Asia/Shanghai). Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Source from author branch `f60cfd6ca32b442661622bb0382dbbd6449778f0`: EC49FDW's eight complete literal witnesses; EC49FDV's exhaustive word-pool enumerator; EC49FDU's nine-history rank observer. This is author-side finite, solver-backed mathematical evidence. Native task CLAIM and independent Driver review remain pending.

## Exact finite proposition

For each of the eight EC49FDW witness systems **fix every literal H2–H6 word**, keep the supplied complete positive BRC key `K` on H7, H8 and H9, and retain their exact window quotas (4,4,2) and rank-nine observation requirement. Allow **every legal positive-key, signed-native, observer-qualified operation word** as a replacement in H7–H9, while preserving native signed primitive prefixes and the global five-key constraint.

For cases 0–3, the exact minimum full H2–H9 cost is **118 edges**; for cases 4–7, the exact minimum is **120 edges**. In all eight cases, the fixed early H2–H6 prefix union is 70 or 72 edges respectively, and the minimal additional H7–H9 prefix union contributes **exactly 48 edges**. Consequently, changing the ten late complete words jointly, with that early configuration and fixed late key, has been optimized exactly. It is a result for eight declared finite subproblems, not a lower bound for arbitrary five-key systems; the original 93-edge mother target remains open and the previously established construction upper bound remains 94.

## Exhaustive pool and certificate table

| Case | H7–H9 key | Fixed H2–H6 edges | Eligible full-word pool | Unpaid native-prefix edge variables | Binary constraints | HiGHS bound = incumbent | Full minimum |
|---|---|---:|---:|---:|---:|---:|---:|
| 0 | (4,6,1) | 70 | 1106 | 8046 | 18326 | 48 | 118 |
| 1 | (5,5,1) | 70 | 2968 | 19326 | 49476 | 48 | 118 |
| 2 | (7,3,1) | 70 | 2968 | 19326 | 49488 | 48 | 118 |
| 3 | (8,2,1) | 70 | 1106 | 8046 | 18326 | 48 | 118 |
| 4 | (4,6,1) | 72 | 1106 | 8044 | 18359 | 48 | 120 |
| 5 | (5,5,1) | 72 | 2968 | 19324 | 49497 | 48 | 120 |
| 6 | (7,3,1) | 72 | 2968 | 19324 | 49509 | 48 | 120 |
| 7 | (8,2,1) | 72 | 1106 | 8044 | 18347 | 48 | 120 |

Eight bounded independent runs of HiGHS through SciPy `milp` returned `status=0` (`OPTIMAL`), **MIP dual bound 48**, integer incumbent 48, and **zero reported gap**. These are model-exact MILP results with solver-dependent lower-bound certificates. The complete executable model is `EC49FDX_EXACT_MIP.py`; `EC49FDX_SOLVER_SUMMARY.json` stores the eight finite statistics.

## Exact derivation of enumeration and prefix MILP

Operations are the *original* six literal codes:
`a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`.
The signed native path is the complete concatenation of these codes (with axis signs and order retained). Let `K=(x,y,z)` be the complete positive primitive BRC key and `h` the operator-word length. Return displacement `+2E1` forces
`#e=z; #a=z-1; #c+#d=x+y-h-1; #f=h+1-y-2z; #g=h+1-x`.
These equations and the split of `#c+#d` enumerate every legal word of key K and operator horizon h by all distinct permutations, followed by the exact nine-history observer filter. For this schedule, H7 and H8 each have exactly four available signatures (1,2,4,8), and H9 has exactly two (16,32). Their exact quotas and rank-nine clauses force **one word per signature** in each window, yielding 10 disjoint word-choice groups.

Let `F` be the primitive-prefix union of all fixed H2–H6 words. For each eligible late word w, `x_w ∈ {0,1}`; for each unpaid primitive prefix p outside F, `y_p ∈ {0,1}`. Impose `sum_{w in group} x_w = 1` for all ten groups, and `x_w ≤ y_p` whenever p is a native signed prefix of w not in F. Minimize `|F|+sum_p y_p`. Every legal collection of ten words provides such a binary solution and vice versa; positivity of all edge costs makes paid y exactly their prefix union at optimum. Thus the integer optimum equals the exact minimum cost of this finite restricted construction family.

All eight supplied EC49FDW literal witnesses already realize the matching upper bounds 118/120. The original independent `VERIFY_EC49FDW.py` checks **8 full systems, 64 exact rational rank-nine window tests and 192 signed primitive paths**. The new solver also constructs and independently validates a 24-word system for each optimum via `verify_full`. The low-level signed path codes are uniquely decodable (the first two primitives distinguish all six operations), so the primitive trie uses faithful original path identity.

For case 0, the continuous linear relaxation has objective 45 while the integer optimum is 48, exposing a **three-edge integrality gap** in this restricted late-word coverage model (additional diagnostic via SciPy HiGHS LP).

## Reproduction

Requirements: Python, NumPy, SciPy/HiGHS, and the original parent source files already committed in sibling EC49FDU, EC49FDV and EC49FDW directories. In this directory, `IDX=0 python EC49FDX_EXACT_MIP.py` runs a chosen case. Set `IDX` from 0 to 7 for all eight separate exact solves; the program prints the full path witness and solver state and can save the executed JSON. Read `EC49FDX_SOLVER_SUMMARY.json` for the original eight runs and compare their source counts. For construction verification, run the original EC49FDW independent verifier against its unchanged immutable witnesses.

## Scientific next unit

The eight exact late-only optima identify where to modify the route: vary H4–H6 word choices, change the late full BRC key or its three-stage assignment, or jointly change the H2–H6 seed. Each relaxes a *specific* assumption of this certificate. Prioritize an exact discriminating experiment that might reach or beat 93 edges; preserve the original mathematical constraints and all observations. This report changes no frozen task input, P000, Source publication or Driver decision.
