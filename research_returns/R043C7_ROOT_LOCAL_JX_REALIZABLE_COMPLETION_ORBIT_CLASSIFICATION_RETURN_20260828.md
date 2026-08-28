# R043-C7 — Root-Local J_x Realizable Completion-Orbit Classification Return

Status: `FROZEN RESEARCH RETURN / UNRESOLVED_EXACT_FRONTIER / FIXED_TWO_SHELL_SUPPORT_REDUCTION / NOT CANONICAL`

Date: `2026-08-28`  
Task-ID: `RS-R043C7-ROOT-LOCAL-JX-REALIZABLE-COMPLETION-ORBIT-CLASSIFICATION`  
Publication-ID: `TP2-26BA767D9D669F1A7534`  
Researcher-ID: `EM-R043C7-3726F5`  
Claim-ID: `chatgpt-r043c7-20260828-2228-3726f5`  
Execution branch: `research/r043c7-root-local-jx-realizable-completion-orbits-em-r043c7-3726f5`  
Execution base: `3524ea4f3c9fb67295c3ade09029c57b180df59f`

## 0. Primary verdict

The mother classification is **not closed**.

I did not find an exact harmful completion pair, and I do not have a global proof that all globally realizable `J_x` completions over a fixed rooted weighted `G0` are successor-equivalent. No finite pressure result is promoted to such a theorem.

The exact progress is instead a further structural reduction of the C6 completion interface:

`J_x` is supported entirely on a **fixed native two-shell carrier around the action root**. In FCC that carrier has `12 + 42 = 54` non-root slots; in HCP it has `12 + 44 = 56` non-root slots. Because at least one root neighbor is occupied, the vertices that can actually participate in `J_x` are bounded by `53` in FCC and `55` in HCP.

Moreover, every old frontier vertex can have hidden incidence to at most four new `Z_x` sites. The second-shell incidence is drawn from a finite exact root-shell trace catalogue:

- FCC trace-size histogram: `1^12, 2^24, 4^6`;
- HCP trace-size histogram: `1^18, 2^18, 3^2, 4^6`.

This removes any need to search deeper native geometry merely to determine the edges of `J_x`.

A second exact result kills an attractive but invalid shortcut: the relevant old endpoint can be far from the root in **abstract current `G0` graph distance** even though it is only two native steps from the root. Explicit connected FCC and HCP witnesses below give graph distances `3` and `4`, respectively. Therefore the next classifier must work with native two-shell slot incidence relative to the full abstract rooted base, not with a naïve small `G0`-radius truncation.

Classification status:

- FCC: `OPEN / FIXED_TWO_SHELL_TRACE_CARRIER_PROVED / RADIUS_2_G0_SHORTCUT_REFUTED`.
- HCP: `OPEN / FIXED_TWO_SHELL_TRACE_CARRIER_PROVED / RADIUS_3_G0_SHORTCUT_REFUTED`.

No Foundation promotion is requested.

## 1. Frozen input from C6

Use the accepted C6 theorem only:

`ROOTED G0 + J_x -> EXACT ONE-STEP SUCCESSOR`.

Let `C` be a finite connected occupied state in frozen FCC or HCP. Let `Omega` be the current unoccupied component containing the admissible action site `x`, let

`F = F(C) intersect Omega`,

and let `G=G0[F]` be the current weighted native frontier graph rooted at `x`.

C6 partitions the twelve native neighbors of `x` as

`N(x) = I_x disjoint_union A_x disjoint_union Z_x`,

where

- `I_x = N(x) intersect C`;
- `A_x = N(x) intersect F = N_G(x)`;
- `Z_x = N(x) \ (C union F)`.

The visible quantities satisfy

`|I_x| = w_G(x)`,

`|A_x| = deg_G(x)`,

and therefore

`|Z_x| = 12 - w_G(x) - deg_G(x) <= 11`.

The missing profile `J_x` consists of the native edges induced inside `Z_x` plus native edges from `Z_x` to `F\{x}`.

The only question here is how much native carrier is truly needed to realize those missing edges.

## 2. R043C7-T1 — fixed two-shell support theorem

Define the first native shell

`S_x = N(x)`

and the strict second-shell slot set

`Q_x = ( union_{z in S_x} N(z) ) \ (S_x union {x})`.

Then every vertex incident to an edge of `J_x` belongs to

`S_x union Q_x`.

### Proof

Every new vertex of `J_x` is by definition a member of `Z_x subset S_x`.

Consider an edge of `J_x` from `z in Z_x` to an old surviving frontier vertex `y in F\{x}`. Native adjacency gives `y in N(z)`. Since `z in S_x`, every such `y` lies in

`N(S_x) \ {x} subset S_x union Q_x`.

Internal `Z_x-Z_x` edges are already inside `S_x`.

Thus no `J_x` vertex or edge can require a native site outside the fixed two-shell carrier. QED.

This theorem is independent of the size and depth of `Omega` and of the size of the old frontier.

## 3. Exact carrier sizes in the two frozen worlds

The task-local deterministic checker constructs the native carrier directly from the frozen 12-contact neighbor maps.

### FCC

`|S_x| = 12`.

`|Q_x| = 42`.

Hence

`|S_x union Q_x| = 54`.

The induced root-link graph on `S_x` has `24` edges and is `4`-regular.

### HCP

`|S_x| = 12`.

`|Q_x| = 44`.

Hence

`|S_x union Q_x| = 56`.

The induced root-link graph on `S_x` also has `24` edges and is `4`-regular.

These are exact incidence counts, not Euclidean-distance surrogates.

## 4. R043C7-T2 — finite second-shell trace catalogue

For each strict second-shell slot `q in Q_x`, define its root-shell trace

`tau_x(q) = N(q) intersect S_x`.

If `q` is an old frontier endpoint participating in `J_x`, then its hidden adjacency to the new vertices is exactly

`N(q) intersect Z_x = tau_x(q) intersect Z_x`.

Thus all second-shell old-to-new incidence is obtained by restricting one of finitely many fixed native traces.

The exact trace-size distributions are:

### FCC

Among the `42` second-shell slots:

- `12` have trace size `1`;
- `24` have trace size `2`;
- `6` have trace size `4`.

No other trace size occurs.

### HCP

Among the `44` second-shell slots:

- `18` have trace size `1`;
- `18` have trace size `2`;
- `2` have trace size `3`;
- `6` have trace size `4`.

No other trace size occurs.

For an old endpoint `a in A_x subset S_x`, the hidden adjacency to `Z_x` is instead

`N_{L_x}(a) intersect Z_x`,

where `L_x` is the induced root-link graph on `S_x`. Since `L_x` is `4`-regular in both worlds, this also has size at most four.

Therefore:

> **Every old frontier vertex has hidden degree at most four into `Z_x`.**

This is a uniform exact bound in both frozen worlds.

## 5. R043C7-C1 — complete participating-support bound

Because `x` is frontier, `I_x` is nonempty. The root shell partitions as

`S_x = I_x disjoint_union A_x disjoint_union Z_x`.

Only `A_x union Z_x` can participate in `J_x` inside the first shell. Hence

`|A_x| + |Z_x| = 12 - |I_x| <= 11`.

At most all second-shell slots can be old endpoints. Therefore the entire vertex support participating in `J_x` is bounded by

FCC:

`11 + 42 = 53`.

HCP:

`11 + 44 = 55`.

C6 bounded only the newly exposed side by `|Z_x|<=11`. C7 now gives a uniform bound on the **whole native support of the missing completion profile**, including every possible old endpoint.

This still does not classify which slot assignments are globally realizable over the same abstract rooted `G0`.

## 6. Why this does not yet prove raw-G0 sufficiency

The fixed carrier theorem removes deep geometry from the edge support of `J_x`, but it does not identify which abstract old frontier vertices occupy the relevant native slots.

For a fixed abstract rooted weighted graph `[G,x]`, the unresolved datum can be described as a bounded native slot-assignment problem:

1. identify `A_x=N_G(x)` with root-shell frontier slots;
2. choose the remaining root-shell partition into occupied `I_x` and zero-weight `Z_x` consistently with `w_G(x)`;
3. identify the old frontier vertices that lie in second-shell slots `Q_x`;
4. enforce the visible current `G0` edges and weights together with exact native trace incidence;
5. quotient the resulting completed successors by rooted-current automorphisms / successor weighted-graph isomorphism.

The carrier is finite, but the identity of a second-shell slot need not be detectable at small graph distance in the abstract `G0`. The next section gives exact witnesses.

Therefore I do **not** claim that the global realizability problem has been replaced by a purely local `G0`-radius census.

## 7. R043C7-X1 — FCC radius-2 abstract-G0 shortcut is false

Take root

`x=(0,0,0)`

and occupied state

`C_FCC = {(0,-3,-1), (0,-1,1), (1,-3,0), (1,-2,1)}`.

The checker verifies that `C_FCC` is native-contact connected and `x` is current frontier.

Set

`z=(0,-1,-1)`

and

`y=(0,-2,-2)`.

Then:

- `z in Z_x`;
- `y in F\{x}`;
- `z~y` natively, so `z-y` is an edge of `J_x`;
- `y` is captured by the native two-shell carrier;
- but the distance from `x` to `y` in the current abstract frontier graph `G0` is exactly `3`.

Therefore a rule that attempts to reconstruct all of `J_x` from the radius-`2` rooted `G0` neighborhood is false even in FCC.

This is not a harmful completion collision; it is an exact counterexample to a proposed localization shortcut.

## 8. R043C7-X2 — HCP radius-3 abstract-G0 shortcut is false

Take root

`x=(0,0,0)`

and occupied state

`C_HCP = {(-1,1,0), (-1,1,1), (0,1,2), (1,0,2), (1,0,3), (1,1,3), (2,-2,1), (2,-1,2)}`.

Set

`z=(1,-1,0)`

and

`y=(2,-2,0)`.

The checker verifies:

- `C_HCP` is native-contact connected;
- `x` is current frontier;
- `z in Z_x`;
- `y in F\{x}`;
- `z~y` natively;
- `y` is in the fixed native two-shell carrier;
- the distance from `x` to `y` in the current abstract `G0` is exactly `4`.

Therefore radius `3` in abstract rooted `G0` is insufficient even in HCP.

Again, this is a shortcut refutation, not a harmful completion pair.

## 9. What the two counterexamples mean

Native distance and current-`G0` graph distance are different resources here.

Every hidden `J_x` edge is geometrically confined to two native steps from the action root, yet a participating old endpoint can be connected back to the root only through a longer path in the current frontier graph because the intermediate `z` is precisely a zero-weight site absent from current `G0`.

So the correct next object is not a ball `B_r^G(x)` for a guessed small `r`. It is the fixed native two-shell **slot carrier** together with its assignment to vertices of the full abstract rooted base.

This is the main route correction supplied by C7.

## 10. Exploratory collision pressure and its boundary

During research I also used exact native state generation to search for small FCC harmful pairs, quotienting occupied states by the root stabilizer. The orbit counts through occupied size six were

`1, 4, 33, 312, 3578, 43540`.

No decisive harmful pair emerged from the candidate filter.

This pressure is deliberately **not** a theorem and is not used in the frozen certificate: the filter was designed to find splits efficiently, not to certify exact successor equivalence for every same-current class. It therefore supplies no positive rigidity claim.

Broad occupied-animal census is not proposed as the next action.

## 11. Exact finite certificate

Checker:

`scripts/check_r043c7_root_local_jx_realizable_completion_orbit_classification.py`

Certificate:

`research_artifacts/R043C7_ROOT_LOCAL_JX_REALIZABLE_COMPLETION_ORBIT_CLASSIFICATION/RESULTS.json`

The checker deterministically verifies:

1. frozen FCC/HCP 12-contact neighbor maps;
2. root-shell size `12` in both worlds;
3. second-shell slot counts `42` and `44`;
4. root-link `24` edges and degree `4` at all twelve root-shell slots;
5. exact second-shell trace-size histograms;
6. the support-capture identity `N(S_x)\{x} subset S_x union Q_x`;
7. the FCC explicit radius-2 shortcut counterexample with exact `G0` distance `3`;
8. the HCP explicit radius-3 shortcut counterexample with exact `G0` distance `4`.

The equivalent task-local checker was run against the frozen source and returned `pass=true` before handoff.

## 12. Hard-target audit

Hard target:

`R043C7_REALIZABLE_JX_COMPLETION_ORBITS_CLASSIFIED_UNIQUE_OR_HARMFUL_COLLISION`.

Disposition:

`NOT YET SATISFIED`.

What is proved:

`J_X_NATIVE_SUPPORT subset FIXED TWO-SHELL CARRIER`.

`FULL J_X PARTICIPATING SUPPORT <= 53 FCC / 55 HCP`.

`OLD_TO_Z_X HIDDEN DEGREE <= 4`.

`SECOND-SHELL HIDDEN INCIDENCE = ROOT-SHELL TRACE RESTRICTION`.

`SMALL ABSTRACT-G0-RADIUS LOCALIZATION SHORTCUT = REFUTED BY EXACT EXAMPLES`.

What remains open:

- whether two globally realizable slot assignments over the same rooted weighted `G0` can yield nonisomorphic successors;
- or whether all such assignments are successor-equivalent in FCC;
- and independently in HCP.

No one-step raw-`G0` sufficiency theorem follows yet.

## 13. Finite-horizon consequence

Unchanged from the C6 induction gate:

- if a later theorem proves global successor-equivalence of every realizable two-shell slot assignment over every reachable rooted `G0`, one-step sufficiency follows and then composes to every finite horizon;
- one exact harmful slot-assignment pair would kill one-step sufficiency in that world immediately.

The present return neither proves nor refutes finite-horizon stationary raw-`G0` sufficiency.

## 14. Recommended next action

Do **not** expand generic occupied-animal radius.

Instead build an exact finite slot-assignment classifier on the frozen carrier:

1. freeze the root-link `L_x` and second-shell trace catalogue `tau_x` separately for FCC/HCP;
2. for a fixed rooted weighted `G`, enumerate only native slot assignments compatible with the visible root neighborhood, current weights, and current induced edges;
3. quotient assignments by the native root stabilizer and `Aut(G,x)` before successor construction;
4. use exact weighted graph isomorphism on successors;
5. if a split occurs, materialize the smallest globally realizable occupied witness pair;
6. if no split occurs, do not claim a theorem until the slot parameterization is proved complete for all globally realizable assignments.

The difficult residue is now **slot-to-abstract-base identification**, not deep exterior geometry.

## 15. Final classification

Primary classification:

`UNRESOLVED_EXACT_FRONTIER / FIXED_TWO_SHELL_SUPPORT_REDUCTION`.

FCC:

`TWO_SHELL_CARRIER_54 / ACTIVE_J_SUPPORT_AT_MOST_53 / TRACE_SIZES_1_2_4 / RADIUS_2_G0_SHORTCUT_FALSE / COMPLETION_ORBIT_CLASSIFICATION_OPEN`.

HCP:

`TWO_SHELL_CARRIER_56 / ACTIVE_J_SUPPORT_AT_MOST_55 / TRACE_SIZES_1_2_3_4 / RADIUS_3_G0_SHORTCUT_FALSE / COMPLETION_ORBIT_CLASSIFICATION_OPEN`.

No harmful pair is claimed. No uniqueness theorem is claimed. No Foundation mutation is requested.