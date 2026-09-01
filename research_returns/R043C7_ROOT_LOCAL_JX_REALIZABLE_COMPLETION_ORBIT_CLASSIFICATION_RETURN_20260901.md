# R043-C7 Root-Local `J_x` Realizable Completion-Orbit Classification — Recovery/Revalidation Return

Status: `FROZEN RESEARCH RETURN / PASS_BY_STRICT_FINITE_EXTENSION_REDUCTION / AWAITING DRIVER REVIEW / NOT CANONICAL`

Date: `2026-09-01`

Task-ID: `RS-R043C7-ROOT-LOCAL-JX-REALIZABLE-COMPLETION-ORBIT-CLASSIFICATION`

Publication-ID: `TP2-26BA767D9D669F1A7534`

Researcher-ID: `EM-R043C7-0611C4`

Claim-ID: `chatgpt-r043c7-20260901-1130-0611c4`

Execution branch: `research/r043c7-root-local-jx-realizable-completion-orbits-em-r043c7-0611c4`

Execution base: `bd8781924b8423e18ef3d7b3a37d86ebc71fc1a6`

## 0. Primary verdict

`PASS: REDUCED_TO_STRICTLY_SMALLER_FINITE_EXTENSION_INVARIANT` in both frozen worlds.

The taskbook expressly permits a fourth discriminating outcome besides full uniqueness or a harmful pair: reduce the realizable completion question to a strictly smaller finite link/extension invariant with an exact certificate. This return satisfies that route.

It does **not** prove that raw rooted weighted `G0` is one-step sufficient, and it does **not** construct a harmful same-`G0` collision.

The exact reduction is:

- HCP: `K_x = (kappa_x, lambda_x, P_x)`;
- FCC: `K_x = (kappa_x, Delta_x, lambda_x, P_x)`,

with

- `kappa_x` a bounded root-edge co-occupancy profile;
- `Delta_x` needed only for two explicit FCC exceptional shell classes;
- `lambda_x` a base-relative shell-alignment class of index at most `8`;
- `P_x` the remaining outer-port gluing on a fixed native second-shell carrier of `42` slots in FCC and `44` slots in HCP.

Thus

`ROOTED G0 + K_x -> J_x -> EXACT ONE-STEP SUCCESSOR`.

The root-shell `A-Z` and `Z-Z` edge sets of the original `J_x` are no longer retained explicitly. The only remaining edge-level residue is the genuinely external second-shell port gluing.

## 1. Frozen accepted input

The only promoted mathematical input used is accepted C6:

`ROOTED G0 + J_x -> EXACT ONE-STEP SUCCESSOR`.

For a finite connected occupied state `C`, one unoccupied component `Omega`, current frontier slice `F = F(C) intersect Omega`, weighted current graph `G=G0[F]`, and admissible root `x in F`, C6 gives the exact partition

`N(x) = I_x disjoint_union A_x disjoint_union Z_x`

where

- `I_x = N(x) intersect C`;
- `A_x = N(x) intersect F = N_G(x)`;
- `Z_x = N(x) \ (C union F)`.

Visible current data determine

`|I_x| = w_G(x)`,
`|A_x| = deg_G(x)`,
`|Z_x| = 12 - w_G(x) - deg_G(x) <= 11`.

The hidden profile `J_x` is exactly the induced native edges in `Z_x` together with native incidence from `Z_x` to `F\{x}`.

No historical C7 branch is treated as accepted mathematics. A prior PASS branch was read only as a recovery candidate; every numerical classification used below was recomputed from the frozen FCC/HCP neighbor definitions and C6 interface in the current execution.

## 2. Exact realizability definition

Fix world `W` equal to frozen FCC or frozen HCP and fix an abstract rooted weighted graph `[G,x]`.

A **globally realizable `J_x` completion over `[G,x]`** is an equivalence class of witnesses `(C,Omega,phi)` where:

1. `C` is a finite connected occupied subset of `W`;
2. `Omega` is an unoccupied connected component for `C`;
3. `F=F(C) intersect Omega` and `x_W in F`;
4. `phi : [G,x] -> [G0[F],x_W]` is a rooted weighted graph isomorphism;
5. the extracted C6 profile from `(C,Omega,x_W)` is transported back along `phi` on all old-frontier endpoints.

Two profiles are **root-current equivalent** if they differ by an element of `Aut(G,x)` together with an isomorphism of the new `Z_x` vertices preserving all `Z-Z` and `Z-(F\{x})` incidences.

Two completions are **successor-equivalent** if the C6 successors are weighted-graph isomorphic after the corresponding rooted-current identification.

This definition is exact and global. The finite shell enumeration below is deliberately a superset theorem: it proves statements for every actual globally realizable completion without pretending that every enumerated shell partition extends to a global occupied state.

## 3. Complete root-shell feasible superset

Let `L_x` be the native link graph induced by the twelve neighbors of `x`.

Every globally realizable shell obeys:

`I_x != empty`

because `x` is frontier, and

`E_L(I_x,Z_x)=empty`.

The second condition is forced: if `z in Z_x` were adjacent to occupied `i in I_x`, then `z` already had an occupied neighbor before adding `x` and therefore would already be frontier, contradicting `z in Z_x`.

Equivalently,

`boundary_L(I_x) subseteq A_x`.

The checker enumerates all status partitions of the twelve shell sites satisfying exactly these necessary conditions. Therefore the enumeration contains every globally realizable root shell.

Exact counts:

- FCC: `8,567` feasible shell patterns;
- HCP: `8,657` feasible shell patterns.

In both worlds the root link has `12` vertices, `24` edges, and degree `4` at every shell vertex. Every native edge `(x,a)` also has exactly four common native neighbors.

## 4. Root-edge co-occupancy profile `kappa_x`

For each visible root-neighbor `a in A_x`, define

`kappa_x(a) = |C intersect N(x) intersect N(a)|`.

Let

`t_x(a) = |N_G(x) intersect N_G(a)|`.

All four common neighbors of adjacent `(x,a)` lie in the root shell and split into occupied `I_x`, old-frontier `A_x`, and newly exposed `Z_x`. Hence

`r_x(a) := |N(a) intersect Z_x| = 4 - t_x(a) - kappa_x(a)`.

The current rooted graph already knows `L_x[A_x]=G[A_x]` and `t_x(a)`. Thus the hidden row data are equivalent to the bounded scalar profile `kappa_x`.

Define the exact row-signature graph

`Q_x = (L_x[A_x], r_x)`.

## 5. HCP exact root-shell orbit theorem

Across all `8,657` feasible HCP shell patterns:

- exact row-signature classes: `681`;
- row-signature classes with more than one `A/Z`-coloured completion orbit: `0`.

Therefore, for every globally realizable HCP completion, the abstract coloured root-shell completion `H_x = L_x[A_x union Z_x]` is determined up to colour-preserving graph isomorphism by rooted `G0` plus `kappa_x`.

This is stronger than a direct realizability census because it holds on a combinatorial superset of the globally realizable shells.

HCP root-shell disposition:

`G0 + kappa_x -> UNIQUE ABSTRACT A/Z ROOT-SHELL ORBIT`.

## 6. FCC exact root-shell classification and `Delta_x`

Across all `8,567` feasible FCC shell patterns:

- exact row-signature classes: `230`;
- ambiguous row-signature classes: exactly `2`.

They are:

1. `(|I_x|,|Z_x|)=(1,4)`, with `48` raw realizations split `24/24`. The two `Z_x` internal degree multisets are `(0,1,1,2)` and `(1,1,1,1)`.
2. `(|I_x|,|Z_x|)=(1,5)`, with `48` raw realizations split `24/24`. The two `Z_x` internal degree multisets are `(0,2,2,2,2)` and `(1,1,2,2,2)`.

Define

`Delta_x = multiset{deg_{L_x[Z_x]}(z) : z in Z_x}`.

After augmenting the row signature by `Delta_x`:

- exact augmented classes: `232`;
- ambiguous augmented classes: `0`.

Therefore every globally realizable FCC root shell is determined up to abstract `A/Z`-coloured orbit by rooted `G0 + kappa_x + Delta_x`.

No claim is made that both members of either exceptional combinatorial pair are globally realizable over the same rooted `G0`; `Delta_x` is retained precisely because that stronger global statement has not been proved.

FCC root-shell disposition:

`G0 + kappa_x + Delta_x -> UNIQUE ABSTRACT A/Z ROOT-SHELL ORBIT`.

## 7. Base-relative alignment residue is at most eightfold

Abstract shell orbit is not yet a completion over the actual old base.

For a feasible shell let:

- `Aut(Q_x)` be the automorphism group of the row-signature graph;
- `Aut(H_x)` be the colour-preserving automorphism group of the completed root shell;
- `R_x` be the restriction image of `Aut(H_x)` on `A_x`.

Every restriction in `R_x` is explicitly checked to preserve both the `A-A` graph and row labels, hence

`R_x <= Aut(Q_x)`.

Choosing an identification of the abstract shell's `A` part with the actual visible `A_x` is a torsor under `Aut(Q_x)`. Two identifications differing by `R_x` produce the same completed shell over `A_x`; further automorphisms of the full rooted old base can only identify additional choices. Thus the number of base-relative alignment classes is bounded by

`[Aut(Q_x):R_x]`.

Exact spectra over all feasible shell patterns are:

FCC: index `1`: `8,079`; index `2`: `476`; index `3`: `6`; index `8`: `6`.

HCP: index `1`: `8,301`; index `2`: `305`; index `3`: `6`; index `4`: `27`; index `8`: `18`.

Therefore uniformly in both worlds:

`[Aut(Q_x):R_x] <= 8`.

Let `lambda_x` denote the resulting base-relative alignment class.

## 8. Fixed second-shell carrier for every outer port

Let

`S_x = N(x)`

and let the strict second-shell slot set be

`T_x = ( union_{z in S_x} N(z) ) \ (S_x union {x})`.

If `z in Z_x` has a `J_x` edge to an old frontier vertex `b` outside the root shell, then `b in N(z)` and `z in S_x`; hence `b` occupies a slot of `T_x`.

Exact native counts:

- FCC: `|T_x|=42`;
- HCP: `|T_x|=44`.

For each second-shell slot `q`, define its root-shell trace

`tau_x(q)=N(q) intersect S_x`.

Exact trace-size histograms are:

FCC: size `1`: `12` slots; size `2`: `24` slots; size `4`: `6` slots.

HCP: size `1`: `18` slots; size `2`: `18` slots; size `3`: `2` slots; size `4`: `6` slots.

Thus every outer old endpoint has hidden incidence to at most four members of `Z_x`, and no `J_x` edge can depend on a native site deeper than two native steps from the root.

Because `I_x` is nonempty, `|A_x|+|Z_x|<=11`. Hence the whole possible native support participating in `J_x` is bounded by:

- FCC: `11 + 42 = 53`;
- HCP: `11 + 44 = 55`.

This fixed-carrier theorem makes the residual extension invariant genuinely finite independently of the size of the old frontier component.

## 9. The reduced finite extension invariant

Let

`B_x = (F\{x}) \ A_x`.

After choosing the classified root-shell orbit and `lambda_x`, define `P_x` as the orbit, relative to the rooted-current base and the chosen shell alignment, of all remaining incidences

`E(Z_x,B_x)`.

By Section 8 every endpoint of these incidences occupies one of the fixed second-shell slots and its `Z_x` incidence is the restriction of one of the finite traces `tau_x(q)`.

Define:

HCP: `K_x^HCP = (kappa_x, lambda_x, P_x)`.

FCC: `K_x^FCC = (kappa_x, Delta_x, lambda_x, P_x)`.

### Reconstruction theorem

Given rooted `G0` and `K_x`:

1. `kappa_x` reconstructs every row label `r_x(a)`;
2. the HCP shell theorem, or the FCC theorem with `Delta_x`, reconstructs the abstract coloured root-shell orbit;
3. `lambda_x` chooses its base-relative alignment, among at most eight classes;
4. `P_x` supplies exactly the remaining `Z_x-B_x` incidence;
5. therefore the full `J_x` orbit is fixed;
6. accepted C6 then reconstructs the exact one-step successor.

Hence:

`ROOTED G0 + K_x -> J_x -> EXACT ONE-STEP SUCCESSOR`.

### Why the reduction is strict

The original `J_x` explicitly retains all hidden shell-edge families `E(A_x,Z_x)` and `E(Z_x,Z_x)` plus outer ports.

`K_x` no longer retains either hidden shell-edge family. They are reconstructed from a bounded scalar row profile, one exceptional FCC multiset, and a finite alignment class of size at most eight. Only the genuinely external port-gluing orbit remains edge-level data, and even that lives on the fixed `42/44` second-shell catalogue.

So the target has been reduced to a strictly smaller finite link/extension invariant, not merely renamed.

## 10. Successor comparison and stationary-sufficiency consequence

For two globally realizable completions over the same rooted current state:

- equal reduced `K_x` orbit implies equal `J_x` orbit;
- equal `J_x` orbit implies the same C6 successor up to the permitted rooted-current automorphism and weighted-graph isomorphism.

This does **not** show that raw rooted `G0` determines `K_x`.

The exact remaining gate is:

> For fixed realizable rooted weighted `G0`, are all possible reduced codes `K_x` successor-equivalent, or can two globally realizable reduced codes yield nonisomorphic successors?

A single harmful pair would refute raw one-step sufficiency in that world.

Conversely, if a future theorem proves successor-equivalence of all reduced codes for every reachable state, C6's induction gate gives stationary sufficiency for every finite addition horizon.

No finite-horizon theorem is claimed here.

## 11. Deterministic certificate and recovery audit

Checker:

`research_checks/R043C7_ROOT_LOCAL_JX_REALIZABLE_COMPLETION_ORBIT_CLASSIFICATION_CHECK_20260901.py`

Certificate:

`research_artifacts/R043C7_ROOT_LOCAL_JX_REALIZABLE_COMPLETION_ORBIT_CLASSIFICATION/RESULTS.json`

The checker recomputes from the frozen native neighbor maps:

- root-shell `12/24/4-regular` incidence in both worlds;
- four common neighbors for every native root edge;
- all `8,567` FCC and `8,657` HCP feasible shell patterns;
- `230` FCC and `681` HCP exact row classes;
- zero HCP ambiguity;
- exactly two FCC ambiguous row classes with the exact `24/24` splits;
- complete FCC resolution by `Delta_x` to `232` augmented classes;
- exact alignment-index spectra and universal maximum `8`;
- fixed second-shell counts `42/44`;
- exact second-shell trace histograms and support bounds `53/55`.

WL hashes are used only as isomorphism-invariant buckets. Every class decision is made by exact graph isomorphism. The current execution also adds an explicit assertion that every restriction of a colour-preserving shell automorphism is a genuine row-signature automorphism before the coset index is formed.

Local deterministic replay on the current execution returned `pass=true`.

## 12. Terminal classification

Terminal verdict:

`PASS`.

Hard-target disposition:

`SATISFIED_BY_EXACT_REDUCTION / REDUCED_TO_STRICTLY_SMALLER_FINITE_EXTENSION_INVARIANT / ROOT_SHELL_ORBITS_CLASSIFIED / ALIGNMENT_LE_8 / OUTER_PORTS_FIXED_TO_42_OR_44_SLOT_SECOND_SHELL`.

FCC:

`KAPPA + TWO-CLASS-ONLY DELTA + ALIGNMENT_LE_8 + 42-SLOT OUTER PORT GLUE`.

HCP:

`KAPPA + ALIGNMENT_LE_8 + 44-SLOT OUTER PORT GLUE`.

Unresolved residue:

`FOR_FIXED_ROOTED_G0, CLASSIFY THE REDUCED K_X ORBITS OR PRODUCE A GLOBALLY REALIZABLE HARMFUL SUCCESSOR SPLIT`.

Recommended next mathematical task, if Driver accepts this result:

`SECOND_SHELL_PORT_GLUE / REDUCED_K_X ORBIT CLASSIFICATION UNDER THE CLASSIFIED ROOT-SHELL STABILIZER`.

Do not reopen broad occupied-animal census. Do not infer Working Truth, Foundation status, novelty, raw-`G0` sufficiency, or a harmful collision from this return.
