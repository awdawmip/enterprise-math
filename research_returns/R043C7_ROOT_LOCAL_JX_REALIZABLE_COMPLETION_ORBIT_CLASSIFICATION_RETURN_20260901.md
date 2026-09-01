# R043-C7 Root-Local J_x Realizable Completion-Orbit Classification — Return

Status: `FROZEN RESEARCH RETURN / PASS_BY_STRICT_FINITE_EXTENSION_REDUCTION / AWAITING DRIVER REVIEW / NOT CANONICAL`

Date: `2026-09-01`

Task-ID: `RS-R043C7-ROOT-LOCAL-JX-REALIZABLE-COMPLETION-ORBIT-CLASSIFICATION`

Publication-ID: `TP2-26BA767D9D669F1A7534`

Researcher-ID: `EM-R043C7-0611C4`

Claim-ID: `chatgpt-r043c7-20260901-1130-0611c4`

Execution branch: `research/r043c7-root-local-jx-realizable-completion-orbits-em-r043c7-0611c4`

Execution base: `bd8781924b8423e18ef3d7b3a37d86ebc71fc1a6`

## 0. Verdict

`PASS: REDUCED_TO_STRICTLY_SMALLER_FINITE_EXTENSION_INVARIANT` in both frozen worlds.

This uses the taskbook's explicit success route allowing a strict reduction to a smaller finite link/extension invariant. It does not claim raw rooted-G0 sufficiency and does not construct a harmful same-G0 collision.

Accepted C6 supplies:

`ROOTED G0 + J_x -> EXACT ONE-STEP SUCCESSOR`.

For a rooted action x, the twelve native neighbors split exactly as

`N(x)=I_x disjoint_union A_x disjoint_union Z_x`

with `|I_x|=w_G(x)`, `|A_x|=deg_G(x)`, and

`|Z_x|=12-w_G(x)-deg_G(x)<=11`.

The hidden C6 profile `J_x` consists exactly of the `Z_x-Z_x` native edges and the `Z_x-(F\{x})` native incidences.

## 1. Exact realizability interface

Fix frozen world W in {FCC,HCP} and an abstract rooted weighted current graph `[G,x]`.

A globally realizable completion is represented by a finite connected occupied set C, an unoccupied component Omega, a current frontier slice `F=F(C) intersect Omega`, a root `x_W in F`, and a rooted weighted isomorphism `[G,x] -> [G0[F],x_W]`. Extract the C6 profile in W and transport its old-frontier endpoints back to G.

Profiles are equivalent modulo `Aut(G,x)` and an isomorphism of the new `Z_x` vertices preserving all hidden incidences. Successor-equivalence is weighted-graph isomorphism of the C6 successors under the same rooted-current identification.

The finite shell census below is a superset theorem: every globally realizable shell occurs in it, but no converse global-realizability claim is made.

## 2. Complete root-shell superset

Let `L_x` be the native link on the twelve neighbors of x.

Every realizable shell satisfies `I_x != empty` because x is frontier, and

`E_L(I_x,Z_x)=empty`.

Indeed, if `z in Z_x` touched occupied `i in I_x`, then z already had an occupied neighbor and would already lie in the old frontier.

The exact checker enumerates all shell partitions satisfying these necessary conditions.

Exact totals:

- FCC: `8,567` feasible shell patterns.
- HCP: `8,657` feasible shell patterns.

In both worlds the root link has 12 vertices, 24 edges, degree 4 at every vertex, and every native root edge has exactly four common native neighbors.

## 3. Root-edge co-occupancy signature

For each visible root neighbor `a in A_x`, define

`kappa_x(a)=|C intersect N(x) intersect N(a)|`

and let

`t_x(a)=|N_G(x) intersect N_G(a)|`.

The four common neighbors of x and a split into I/A/Z shell sites, hence

`r_x(a)=|N(a) intersect Z_x|=4-t_x(a)-kappa_x(a)`.

The graph `L_x[A_x]=G[A_x]` and `t_x(a)` are visible in current G0. Therefore the hidden shell row data are equivalent to the bounded scalar profile `kappa_x`.

Define the row-signature graph

`Q_x=(L_x[A_x],r_x)`.

## 4. HCP shell theorem

Across all 8,657 feasible HCP patterns:

- exact row-signature classes: `681`;
- ambiguous row-signature classes: `0`.

Therefore rooted G0 plus `kappa_x` determines the abstract A/Z-coloured HCP root-shell completion orbit.

## 5. FCC shell theorem

Across all 8,567 feasible FCC patterns:

- exact row-signature classes: `230`;
- ambiguous row-signature classes: exactly `2`.

The exceptions are:

- `(|I_x|,|Z_x|)=(1,4)`: 48 raw realizations, split 24/24, with Z-degree multisets `(0,1,1,2)` and `(1,1,1,1)`;
- `(|I_x|,|Z_x|)=(1,5)`: 48 raw realizations, split 24/24, with Z-degree multisets `(0,2,2,2,2)` and `(1,1,2,2,2)`.

Define

`Delta_x=multiset{deg_{L_x[Z_x]}(z):z in Z_x}`.

After adding Delta there are exactly `232` augmented classes and `0` ambiguous classes.

Therefore rooted G0 plus `kappa_x` plus `Delta_x` determines the abstract A/Z-coloured FCC root-shell completion orbit. No claim is made that both members of either exceptional combinatorial pair are globally realizable over the same rooted G0.

## 6. Base-relative alignment is at most eightfold

Let `H_x=L_x[A_x union Z_x]`, with A/Z colours. Let `Aut(Q_x)` be the row-signature automorphism group and let `R_x` be the restriction image on A of the colour-preserving group `Aut(H_x)`.

The checker explicitly verifies `R_x <= Aut(Q_x)`. Distinct alignments of the abstract completed shell over the actual visible A are controlled by the cosets of R in `Aut(Q_x)`; automorphisms of the larger rooted old base can only identify more choices.

Exact raw-pattern spectra are:

FCC: `1:8079, 2:476, 3:6, 8:6`.

HCP: `1:8301, 2:305, 3:6, 4:27, 8:18`.

Thus in both worlds:

`[Aut(Q_x):R_x] <= 8`.

Let `lambda_x` denote the remaining base-relative alignment class.

## 7. Every outer port lives on a fixed second shell

Let `S_x=N(x)` and

`T_x=(union_{z in S_x} N(z)) \ (S_x union {x})`.

If `z in Z_x` has a J_x edge to an old frontier vertex outside the root shell, that old endpoint lies in `T_x`.

Exact counts:

- FCC: `|T_x|=42`.
- HCP: `|T_x|=44`.

For `q in T_x`, define its shell trace `tau_x(q)=N(q) intersect S_x`.

Trace-size histograms:

FCC: `1^12, 2^24, 4^6`.

HCP: `1^18, 2^18, 3^2, 4^6`.

Hence every outer endpoint has hidden degree at most four into Z_x. Since `|A_x|+|Z_x|<=11`, the complete native support that can participate in J_x is bounded by 53 vertices in FCC and 55 in HCP.

## 8. Strictly smaller finite invariant

Let `B_x=(F\{x})\A_x`.

After the root-shell orbit and alignment are fixed, let `P_x` be the orbit, relative to the rooted-current base and chosen shell alignment, of the remaining incidences `E(Z_x,B_x)`. Section 7 shows that all such incidences lie on the fixed 42/44-slot second-shell catalogue.

Define

HCP:
`K_x=(kappa_x,lambda_x,P_x)`.

FCC:
`K_x=(kappa_x,Delta_x,lambda_x,P_x)`.

Then:

1. kappa reconstructs the shell row labels;
2. the HCP theorem, or FCC theorem plus Delta, reconstructs the abstract coloured root shell;
3. lambda chooses its base-relative alignment among at most eight classes;
4. P supplies exactly the remaining outer incidences;
5. therefore the full J_x orbit is fixed;
6. accepted C6 reconstructs the exact successor.

So

`ROOTED G0 + K_x -> J_x -> EXACT ONE-STEP SUCCESSOR`.

The reduction is strict because K no longer stores either hidden root-shell edge family `E(A_x,Z_x)` or `E(Z_x,Z_x)` explicitly. Those are reconstructed from bounded scalar/orbit data; only the genuinely external port-gluing orbit remains edge-level data, itself confined to a fixed finite second-shell carrier.

## 9. Consequence and remaining gate

Equal reduced K-orbits over the same rooted current state imply equal J_x orbits and therefore successor-equivalent C6 successors.

This does not prove that raw rooted G0 determines K_x.

The remaining theorem-critical question is now:

For a fixed globally realizable rooted weighted G0, are all reduced K_x orbits successor-equivalent, or can two globally realizable K_x values produce nonisomorphic successors?

One harmful pair kills one-step sufficiency in that world. Conversely, uniform successor-equivalence of K_x at every reachable state would combine with C6 to give every finite addition horizon.

## 10. Deterministic certificate

Checker:

`research_checks/R043C7_ROOT_LOCAL_JX_REALIZABLE_COMPLETION_ORBIT_CLASSIFICATION_CHECK_20260901.py`

Certificate:

`research_artifacts/R043C7_ROOT_LOCAL_JX_REALIZABLE_COMPLETION_ORBIT_CLASSIFICATION/RESULTS.json`

The checker recomputes all shell counts, exact isomorphism classes, FCC exceptional splits, Delta resolution, alignment-index spectra, second-shell sizes, trace histograms, and support bounds from the frozen native-neighbor definitions. WL hashes are used only as safe candidate buckets; class decisions use exact graph isomorphism. It also asserts that every shell-automorphism restriction used in an alignment quotient is a genuine row-signature automorphism.

Current deterministic replay returned `pass=true`.

## 11. Recovery audit and terminal disposition

A historical C7 PASS branch was inspected only as a recovery candidate. The present result independently replayed its root-shell certificate against the accepted C6 interface and strengthened the finite-residue statement with the fixed second-shell carrier and trace catalogue. No historical C7 result is treated as Driver-accepted input.

Terminal verdict: `PASS`.

Hard-target disposition:

`SATISFIED_BY_EXACT_REDUCTION / REDUCED_TO_STRICTLY_SMALLER_FINITE_EXTENSION_INVARIANT / ROOT_SHELL_ORBITS_CLASSIFIED / ALIGNMENT_LE_8 / OUTER_PORTS_FIXED_TO_42_OR_44_SLOT_SECOND_SHELL`.

FCC:
`KAPPA + TWO-CLASS-ONLY DELTA + ALIGNMENT_LE_8 + 42-SLOT OUTER-PORT GLUE`.

HCP:
`KAPPA + ALIGNMENT_LE_8 + 44-SLOT OUTER-PORT GLUE`.

Unresolved residue:

`FOR_FIXED_ROOTED_G0, CLASSIFY REDUCED K_X ORBITS OR PRODUCE A GLOBALLY REALIZABLE HARMFUL SUCCESSOR SPLIT`.

Recommended successor, if Driver accepts:

`SECOND_SHELL_PORT_GLUE / REDUCED_K_X ORBIT CLASSIFICATION UNDER THE CLASSIFIED ROOT-SHELL STABILIZER`.

Do not reopen broad occupied-animal census. Do not infer Working Truth, Foundation status, novelty, raw-G0 sufficiency, or a harmful collision from this return.
