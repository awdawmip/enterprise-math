# EC49FBM — H9 observer-spine theorem and exact rank-feasibility filtering

Date: 2026-11-05 · TASK_RESEARCH · author-side finite proof and integer enumeration.
Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Immediate source: EC49FBL `d0f10160abe2fc77fdeaa800f7536ea29445c72f`, exactly its 124 EC49FBH early-feasible (L,M) pairs; no earlier scientific pin was refreshed.

## Target and definitions

The H2–H9 mother question minimizes distinct **signed native-X6 primitive prefix edges** with rank-nine observer clauses and at most five complete BRC keys. Retain `H2={fe,ge}, H3={feg,gef}` as the fixed three-key root. Each later horizon h has valid complete BRC key K=(x,y,z,0,0,0), endpoint (2,0,0,0,0,0), ordered operation word over `a,c,d,e,f,g`, and frozen nine-state observer T/S of EC49FBL.

The complete operation-count equations remain:
`#a=z-1; #e=z; #(c+d)=x+y-h-1; #f=h+1-y-2z; #g=h+1-x`.
The observer outputs 16 and 32 exactly at automaton states 4 and 5; its other accepted outputs are 1,2,4,8. H4–H8 retain the original four rank clauses 18,20,33,40 (a clause is covered by a path when signature & clause != 0); H9 requires both 16 and 32.

## Theorem 1: exact terminal F/G criterion (all h>=1)

For a legal positive-key terminal word w of length h, observer signature 16 occurs exactly when w begins with `f` and all remaining letters lie in `{a,e,f,g}`; signature 32 occurs exactly when w begins with `g` and all remaining letters lie in that same alphabet.

Proof: the sole entrances to states 4 and 5 are the transitions from initial state 0 on f and g, respectively. In state 4 or 5 every a/e/f/g transition fixes that state. A c or d transition exits and there are no return transitions to states 4 or 5 from other states. These are directly readable from EC49FBL's frozen transition matrix.

Therefore, **both** F/G rank signatures exist at one horizon h and key K if and only if
[
 x+y=h+1,quad z\ge1,quad x-2z\ge1,quad y\ge1.
]
For h=9, the precise key condition is `x+y=10, z>=1, x>=2z+1, y>=1`.

For an admissible K set a=z-1, e=z, f=x-2z, g=y. The exact number of F/G terminal words is
[
 N_F(h,K)=\frac{(h-1)!}{a!e!(f-1)!g!},\quad
 N_G(h,K)=\frac{(h-1)!}{a!e!f!(g-1)!}.
]
The two formulas count the fixed first f/g letter followed by all multiset permutations of the remaining h-1 operations. The proof uses the full ordered native path, signed displacement, BRC key and exact observer, not an observer-unsafe prefix quotient.

## Theorem 2: finite schedule screening of the 124 EC49FBL pairs

For each frozen pair (L,M), compute observer signature supports by an exact multiset-count × nine-state DFA recurrence (separate c and d transitions). At every h=4,...,8, all four original clauses must be hit; at h=9 both F and G must be hit. This is **necessary and sufficient for per-window rank-witness existence** under the declared fixed key at that window, because the window can select the union of one legal terminal per clause.

Executed exact classifications:
- 124 frozen candidate (L,M) configurations.
- **52** have an M key admitting both required H9 signatures.
- **27** satisfy every window under the fixed schedule H4–H6:L, H7–H9:M.
- **28** satisfy every window under the alternate schedule H4–H5:L, H6–H9:M.
- From the previously counted EC49FBL 6→9 pair edges, **12** pairs have F/G-compatible inheritance, totaling **2,000** ordered terminal pairs (across hypothetical configurations).

This validates and sharpens the EC49FBL caveat about the need to check full-window feasibility. In particular, two previously highest total terminal-inheritance pairs, `L=(4,3,1), M=(7,4,2)` and `L=(5,2,1), M=(8,3,2)`, have M coordinate sum 11, so the declared M-only H9 cannot provide F/G witnesses. The third 1,440-inheritance example `L=(4,2,1), M=(7,3,2)` has H9 F/G witnesses; H6 under L is empty, while the H6→M key reassignment passes the per-window test.

The 27 and 28 cases are **feasible rank-witness schedules**, a first-stage screen before actual joint primitive-prefix minimization. A simultaneous witness exists by selecting terminal words independently at each window, and their primitive path union has some finite edge cost. No edge minimum is asserted here.

## Computation and replication

`VERIFY_EC49FBM.js` reads the exact immutable EC49FBL report present in the preceding sibling directory, checks the 124-pair universe, and evaluates complete word permutations by a memoized *exact integer* nine-state DFA recurrence on the five operation-count classes (a,c+d,e,f,g). c and d are branched as distinct native words. Every count is checked as a JavaScript safe integer. It also checks Theorem 1 against the independent closed-form multinomial counts for **each** H9-eligible M key; all 124 source configurations are checked against the iff test. Output: `EXACT_REPORT_EC49FBM.json`, whose 124 records include signature supports, horizon eligibility and the two schedules. `status=PASS` means these explicit arithmetic/assertion checks completed.

Next discriminating step: optimize full primitive-prefix edges for the 27 fixed and 28 shifted schedules, prioritizing the verified H9-capable cases and comparing the joint edge cost against the mother upper bound 94. Rank-feasible path selection can be improved by mixed keys or changed early H2/H3 roots; the present theorem applies to its exact declared schedules.

## Evidence and status

- Original transition matrix, signatures, operation-count identities, prior 124 pairs and suffix-transfer counts: EC49FBL@d0f10160abe2fc77fdeaa800f7536ea29445c72f.
- Original per-window rank clauses and primitive signed steps: EC49FBJ@74aff4c6debe08da27ddc16b72a3075c2fdc367c.
- Pure integers, bounded horizon 4–9; full 124-pair enumeration in the new verifier; no sampled approximation.
- Author-side proof and exact finite computation, independent Driver mathematical admission outstanding; native Source CLAIM/Result follows actual service authority.
