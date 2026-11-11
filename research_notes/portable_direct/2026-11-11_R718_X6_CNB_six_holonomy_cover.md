# R718 — Cyclic non-backtracking six-state X6/BRC holonomy cover

Date: 2026-11-11 (Asia/Shanghai). Parent research line: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`. Classification: independent author-side path-formal theorem / exact-integer verification. Formal Source CLAIM, native Result and independent Review are separate operational stages.

## 0. Reused frozen inputs

Science pin: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`; P000 V5, native X6 active three-axis states, V17 ordered-slot replacement. Scientific predecessor: R717, exact six-holonomy cover, \`7747c58ab33c7132cf9138c9ab6e7745eb3bac97\`. Earlier R709b candidate stock scheduler and R711/R712 microphase implementations are used only for the conditional ring corollary below. Current behavioral rules were independently read from the live canonical entrypoints; this work does not alter any frozen input.

## 1. Question, branch population, and observer

The R717 full path-formal BRC carrier permits immediate cancellation of a consecutive triad step \`T->U->T\`. Impose the stricter *cyclic non-backtracking* rule and ask if its full \`S_3\` relationship observer remains reachable.

Let \`S={0,1,2}\`, and let \`J(6,3)\` consist of all twenty subsets of three axes from \`{0,1,2,3,4,5}\`. Two distinct triads are adjacent when their intersection has size two. Each positive, source-labelled path branch is a rooted closed walk
\[
  W=(T_0=S,T_1,\ldots,T_{m-1},T_m=S).
\]
It is **cyclically non-backtracking (CNB)** iff every edge is Johnson-adjacent and
\[
 T_{i-1}\ne T_{i+1}\quad(\text{indices modulo }m).
\]
In particular \`T_{m-1} != T_1\` at the root seam. Retain one path per distinct ordered triad sequence; all BRC branch multiplicities are positive. No signed branch cancellation is performed.

Lift starting slots \`(0,1,2)\` by replacing the one departing axis in its existing slot at every step, preserving the common axes' slots. On return, let \`h(W)\in S_3\` be the tuple of positions of original axes 0,1,2. This is the same typed V17 readout as R717. Let \`N_m^{CNB}(h)\` be the exact number of such branches with the given readout.

## 2. Theorem R718-A — full six-state reachability survives cyclic non-backtracking

For all integers \`m>=4\`,
\[
 \boxed{\{h(W):W \text{ is CNB, rooted at }S,\ |W|=m\}=S_3.}
\]
No CNB walk of length \`1\` or \`2\` exists. At length \`3\`, precisely the identity and the three transpositions occur. Therefore the shortest CNB length realizing all six group elements is **four**.

### Exhaustive, exact small cases

The integers below count paths per **individual** transposition or three-cycle, not per entire conjugacy class.

| length m | identity | each transposition | each three-cycle | all paths |
|---:|---:|---:|---:|---:|
| 3 | 18 | 6 | 0 | 36 |
| 4 | 54 | 48 | 9 | 216 |
| 5 | 360 | 252 | 198 | 1,512 |
| 6 | 2,934 | 2,064 | 2,133 | 13,392 |

The accompanying deterministic Python program calculates these numbers twice: by state-tracking exact-integer dynamic programming over the 120 ordered triples, and by independent literal depth-first enumeration of every legal path for \`m=3,4,5,6\`. Equality is asserted for the entire six-component histogram. It also checks the six-state reachability through \`m=16\` (this finite extension is evidence, not the reason the infinite result holds).

### Explicit witnesses

Each line below is a list of **unordered active triads**; the V17 slot transport starts at ordered triple \`(0,1,2)\`. The six entries in each row group are indexed by the final axis-to-slot tuple.

At \`m=4\`:
- \`012\`: 012 / 123 / 124 / 125 / 012
- \`102\`: 012 / 123 / 124 / 024 / 012
- \`210\`: 012 / 123 / 124 / 014 / 012
- \`120\`: 012 / 123 / 023 / 013 / 012
- \`201\`: 012 / 123 / 013 / 023 / 012
- \`021\`: 012 / 023 / 024 / 014 / 012

At \`m=5\`:
- \`102\`: 012 / 123 / 124 / 125 / 025 / 012
- \`210\`: 012 / 123 / 124 / 125 / 015 / 012
- \`120\`: 012 / 123 / 124 / 024 / 014 / 012
- \`012\`: 012 / 123 / 124 / 234 / 023 / 012
- \`201\`: 012 / 123 / 124 / 014 / 024 / 012
- \`021\`: 012 / 123 / 234 / 024 / 014 / 012

At \`m=6\`:
- \`012\`: 012 / 123 / 124 / 012 / 123 / 124 / 012
- \`102\`: 012 / 123 / 124 / 012 / 123 / 023 / 012
- \`210\`: 012 / 123 / 124 / 012 / 123 / 013 / 012
- \`021\`: 012 / 123 / 124 / 012 / 023 / 013 / 012
- \`120\`: 012 / 123 / 124 / 125 / 025 / 015 / 012
- \`201\`: 012 / 123 / 124 / 125 / 015 / 025 / 012

Each is a short, independently inspectable certificate for a permitted holonomy. The program checks histogram counts and all non-backtracking transitions, not just their existence.

### The universal +3 extension lemma

Given **any** rooted CNB closed walk \`W\` and its final named-slot frame \`v\`, let \`a\in S\` be an axis present in both the initial and final triad \`S\` but not the axis absent from \`T_1\` nor the axis absent from \`T_{m-1}\`. Such \`a\` always exists: each neighbor of \`S\` is missing exactly one of its three axes, so at most two axes are excluded.

Choose distinct \`x,y\in\{3,4,5\}\`, and append at the rooted endpoint the three-edge triangle
\[
 S\ \longrightarrow\ (S\setminus\{a\})\cup\{x\}\
 \longrightarrow\ (S\setminus\{a\})\cup\{y\}\
 \longrightarrow\ S.
\]
The first new neighbor differs from \`T_{m-1}\`, and the last intermediate triad differs from \`T_1\`, because each is missing \`a\` whereas those old neighbors are not. The two intermediate triads differ by one axis. Thus all new consecutive transitions and both seam constraints remain CNB. In the final ordered frame, the same slot is replaced three times and restored. The appended triangle therefore contributes identity holonomy and preserves \`h(W)\` exactly. Hence
\[
   N_{m+3}^{CNB}(h)\ge N_m^{CNB}(h)
\]
in particular all six realized holonomies persist under \`m\mapsto m+3\`. This injection is for each branch when a deterministic \`a,x,y\` is chosen, and the inequality follows from the distinct original prefix.

Since the six histograms are strictly positive at lengths 4, 5 and 6, this propagation covers **every** integer \`m>=4\`. This is a universal argument, with the finite base verified by two exact enumeration algorithms. QED.

## 3. Corollary — information residue and stock-ring robustness

Reuse **only the declared R709b/R711/R712 candidate**: a labelled physical ring of \`m\` X6 Cells carrying the active-triad cyclic word, one token of each of two port types per Cell, old-state Johnson-neighbor gates and conservative paired counterflow events, with frozen-old-state macrostep followed by one simultaneous triad update. Every CNB witness is also a Johnson-adjacent cyclic word, so its ring rotates \`X_i(t)=T_{i+t\bmod m}\`, while all variants of fixed length have the same initial/final inventories, positive per-port event counts and edgewise signed microphase-current sequence when a common valid phase word is chosen (four phases for even \`m>=4\`, five for odd \`m>=5\`). Their based Cell-0 relationship results cover all six elements of \`S_3\`.

For the observer that retains this complete *typed event-ledger and microcurrent record* but discards the original joint active-triad field/path, the exact worst-case fixed-width repair remains
\[
 \boxed{\lceil \log_2 |S_3|\rceil=3\text{ binary bits}}
\]
for every \`m>=4\`, **even after imposing CNB**. Full triad-field retention defines a different observer and can distinguish the paths.

CNB is a deliberately selected additional local admissibility filter, **not** an assertion that every frozen native Link/Port system forbids backtracking. This is a discriminating restricted-carrier experiment aimed at the R717 native-interface problem. Spatial Cell identity, temporal ordering, V17 frame and event counters remain separately typed.

## 4. Evidence, replication and next question

Files: \`R718_BRC_NONBACKTRACKING_VERIFY.py\` and \`R718_BRC_NONBACKTRACKING_RESULTS.json\`. Standard-library Python, no floating point. One actual local execution completed all assertions, and JSON includes all six per-element counts for \`m=1..16\`. PASS marker: \`R718_BRC_CYCLIC_NB_SIX_STATE_PASS\`. A second local independent DFS route exhausts every sequence at \`m=3..6\`; the universal +3 proof establishes the unbounded domain.

Remaining scientific step: at the frozen science pin, extract the **actual** V29 Link/Port permission, event timing and conflict semantics. Form the exact native-legal transition predicate on the lifted triad/slot/port state, test the six short CNB witnesses, and compute the resulting restricted holonomy cover. If a native rule eliminates a witness, identify the exact excluded event and test a permitted alternative. Do not change P000 or treat this candidate ring scheduler as already native-admitted.

Evidence status: mathematical construction and author-side exact checking complete; independent proof Review, native Claim/Result and link/port-specific admission pending.
