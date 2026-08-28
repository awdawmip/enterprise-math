# R043-C7 Root-Local J_x Realizable Completion-Orbit Classification — Return

Status: `FROZEN FINAL RETURN / REDUCED_TO_STRICTLY_SMALLER_FINITE_EXTENSION_INVARIANT / NOT CANONICAL`

Date: `2026-08-28`

Task-ID: `RS-R043C7-ROOT-LOCAL-JX-REALIZABLE-COMPLETION-ORBIT-CLASSIFICATION`

Publication-ID: `TP2-26BA767D9D669F1A7534`

Researcher-ID: `EM-R043C7-C25873`

Claim-ID: `chatgpt-r043c7-20260828-1325-c25873`

Execution branch: `research/r043c7-root-local-jx-realizable-completion-orbits-em-r043c7-c25873`

Execution base: `0ffa4e1cbce1f9f33479bc02ea847530af1b3204`

## 0. Primary verdict

`REDUCED_TO_STRICTLY_SMALLER_FINITE_EXTENSION_INVARIANT` in both frozen worlds.

This return does **not** claim raw rooted-`G0` sufficiency and does **not** claim a harmful collision. It gives a complete exact classification of the twelve-site root-shell part of `J_x`, isolates the only two FCC shell-orbit ambiguities under the natural root-edge co-occupancy signature, and proves that the remaining base-relative shell alignment is uniformly finite of index at most eight.

The unresolved C7 datum is therefore no longer the whole `J_x`. It is compressed to:

- a bounded root-edge co-occupancy profile;
- in FCC only, one tiny exceptional shell discriminator;
- a finite shell-alignment coset of size at most eight;
- the outer second-shell frontier-port gluing.

This is strictly smaller than storing every new-new and new-old edge of `J_x`.

FCC disposition:

`ROOT_SHELL_CLASSIFIED_UP_TO_KAPPA_PLUS_DELTA_AND_ALIGNMENT / OUTER_PORT_GLUE_OPEN`.

HCP disposition:

`ROOT_SHELL_CLASSIFIED_UP_TO_KAPPA_AND_ALIGNMENT / OUTER_PORT_GLUE_OPEN`.

## 1. Exact shell parameterization

Fix a reachable rooted frontier state `[G,x]` in frozen FCC or HCP. Let the twelve native neighbors of `x` split as in C6:

`N(x) = I_x disjoint_union A_x disjoint_union Z_x`,

where

- `I_x = N(x) intersect C` are occupied shell sites;
- `A_x = N(x) intersect F` are old frontier shell sites, equivalently the neighbors of `x` visible in `G`;
- `Z_x` are the zero-weight shell sites newly exposed after occupying `x`.

Write `L_x` for the native link graph induced on the twelve neighbors of `x`.

Every globally realizable shell satisfies

`I_x != empty`

and

`E_L(I_x,Z_x)=empty`.

The second condition is forced: if `z in Z_x` were adjacent to an occupied shell site, then `z` would already be old frontier and hence lie in `A_x`.

Equivalently,

`boundary_L(I_x) subseteq A_x`.

The checker enumerates the entire finite **superset** of shell partitions satisfying exactly these necessary conditions. Therefore any uniqueness statement proved on this superset automatically applies to globally realizable shells. No generic occupied-animal census is used.

The exact counts are:

- FCC: `8,567` feasible shell status patterns;
- HCP: `8,657` feasible shell status patterns.

## 2. The root-edge co-occupancy signature

For every `a in A_x`, define the hidden common-occupied count

`kappa_x(a) = |C intersect N(x) intersect N(a)|`.

Both frozen worlds have the same exact edge-local incidence fact:

> every native edge has exactly four common native neighbors.

Let

`t_x(a) = |N_G(x) intersect N_G(a)|`.

Because common native neighbors of the adjacent pair `(x,a)` split inside the root shell into occupied sites, old-frontier sites, and newly exposed sites,

`r_x(a) := |N(a) intersect Z_x| = 4 - t_x(a) - kappa_x(a)`.

Here `t_x(a)` is already visible in the current rooted graph. Thus the hidden shell row data are equivalent to the bounded scalar profile `kappa_x` on the already visible root-neighbor set `A_x`.

Define the row-signature graph

`Q_x = (L_x[A_x], r_x)`,

that is, the visible induced shell graph on `A_x`, with each old vertex labelled by its number of new shell neighbors.

## 3. R043C7-S1 — exact HCP shell-orbit rigidity

For frozen HCP, among **all 8,657 feasible shell patterns**, exact graph isomorphism gives:

- `681` exact row-signature classes;
- `0` row-signature classes with more than one `A/Z`-coloured shell-completion orbit.

Therefore:

> In HCP, the abstract root-shell completion orbit `L_x[A_x union Z_x]`, with `A_x` and `Z_x` distinguished, is uniquely determined by `(|I_x|,|Z_x|,Q_x)`.

Since `|I_x|=w_G(x)` and `|Z_x|=12-w_G(x)-deg_G(x)` are already visible in rooted `G0`, the only additional scalar shell data needed at this level are `kappa_x(a)` for `a in A_x`.

This theorem is stronger than a globally realizable classification because the finite parameterization contains every globally realizable shell and potentially nonrealizable shells as well.

## 4. R043C7-S2 — exact FCC shell-orbit classification

For frozen FCC, among **all 8,567 feasible shell patterns**, exact graph isomorphism gives:

- `230` exact row-signature classes;
- exactly `2` ambiguous row-signature classes.

Both exceptional classes have exactly one occupied shell site:

1. `(|I_x|,|Z_x|)=(1,4)`.
   - The row-signature class has `48` raw realizations.
   - It splits `24/24` into two shell-completion orbits.
   - Their `Z_x` internal degree multisets are respectively
     - `(0,1,1,2)`,
     - `(1,1,1,1)`.

2. `(|I_x|,|Z_x|)=(1,5)`.
   - The row-signature class has `48` raw realizations.
   - It splits `24/24` into two shell-completion orbits.
   - Their `Z_x` internal degree multisets are respectively
     - `(0,2,2,2,2)`,
     - `(1,1,2,2,2)`.

Define the exceptional FCC discriminator

`Delta_x = multiset{ deg_{L_x[Z_x]}(z) : z in Z_x }`.

After augmenting the row signature by `Delta_x`, exact classification gives:

- `232` exact augmented classes;
- `0` ambiguous augmented classes.

Therefore:

> In FCC, the abstract root-shell completion orbit is uniquely determined by rooted `G0`, the co-occupancy profile `kappa_x`, and `Delta_x`.

`Delta_x` is needed only to split the two explicit exceptional row-signature orbit pairs in the shell-superset theorem. This return does not claim that both members of either exceptional pair occur over the same globally realizable rooted `G0`.

## 5. R043C7-S3 — the base-relative alignment residue is at most eightfold

Abstract shell-orbit uniqueness is not yet the same as uniqueness **over the actual old base graph**. A shell automorphism visible on `A_x` need not extend to an automorphism of the completed `A/Z` shell.

For each feasible shell let

- `Aut(Q_x)` be the automorphism group of the row-signature graph on `A_x`;
- `Aut(H_x)` be the colour-preserving automorphism group of the completed shell `H_x=L_x[A_x union Z_x]`;
- `R_x` be the image on `A_x` of `Aut(H_x)`.

Then `R_x` is a subgroup of `Aut(Q_x)`. The possible base-relative shell alignments are controlled by the finite coset set of `R_x` in `Aut(Q_x)`.

The exact raw-pattern index spectra are:

FCC:

- index `1`: `8,079`;
- index `2`: `476`;
- index `3`: `6`;
- index `8`: `6`.

HCP:

- index `1`: `8,301`;
- index `2`: `305`;
- index `3`: `6`;
- index `4`: `27`;
- index `8`: `18`.

Hence in both worlds

`[Aut(Q_x):R_x] <= 8`.

This prevents an overclaim: an unbased shell orbit theorem cannot simply be promoted to rooted-`G0` uniqueness by forgetting how the shell is aligned to the old graph. But the missing alignment is now a finite choice of at most eight classes, not an arbitrary graph completion.

## 6. Strictly smaller hidden extension invariant

Let

`B_x = (F \ {x}) \ A_x`

be the surviving old frontier vertices not native-adjacent to `x`.

Every edge of `J_x` from a new vertex to `B_x` is necessarily a native second-shell port: if `z in Z_x` and `y in B_x` are adjacent, then `y` is at native distance two from `x`.

Define `P_x` to be the **outer-port gluing orbit** of these `Z_x -- B_x` incidences, taken relative to the chosen shell alignment and the rooted-current base.

Then C7 reduces the C6 hidden profile `J_x` to the following smaller code:

HCP:

`K_x^HCP = (kappa_x, lambda_x, P_x)`,

FCC:

`K_x^FCC = (kappa_x, Delta_x, lambda_x, P_x)`,

where `lambda_x` is the shell-alignment coset from Section 5.

Interpretation:

- `kappa_x` reconstructs the shell row counts;
- `Delta_x` resolves exactly the two FCC exceptional shell orbit pairs;
- `lambda_x` selects one of at most eight ways to align the classified shell over the old base;
- `P_x` retains only the genuinely external gluing to old frontier sites outside the root shell.

Once `K_x` is fixed, the entire `J_x` orbit is fixed: the `A-Z` and `Z-Z` shell relations are reconstructed from the finite classification and alignment, and `P_x` supplies the remaining outer incidences. C6 then reconstructs the exact one-step successor.

Thus:

`ROOTED G0 + K_x -> J_x -> EXACT ONE-STEP SUCCESSOR`.

This is a strict reduction because the shell edge families of `J_x` are no longer stored explicitly.

## 7. What remains open

This return does **not** prove that `kappa_x`, `Delta_x`, `lambda_x`, or `P_x` are functions of raw rooted `G0`.

It also does **not** construct two globally realizable states with the same rooted weighted `G0` and different `K_x`.

The exact remaining theorem-critical question is now narrower:

> For a fixed globally realizable rooted weighted `G0`, are the reduced codes `K_x` successor-equivalent, or can the second-shell port gluing / finite alignment / co-occupancy data differ harmfully?

The next theorem-discriminating attack should therefore classify the native second-shell port types relative to the already-frozen shell orbit and its stabilizer. It should **not** resume broad occupied-animal enumeration.

## 8. Consequence for one-step and finite-horizon sufficiency

C6 proved:

`ROOTED G0 + J_x -> successor`.

C7 now proves the sharper factorization:

HCP:

`ROOTED G0 + (kappa_x, lambda_x, P_x) -> successor`.

FCC:

`ROOTED G0 + (kappa_x, Delta_x, lambda_x, P_x) -> successor`.

Therefore any future theorem showing that the reduced code is uniquely determined, or merely successor-equivalent, for every reachable rooted state proves raw one-step sufficiency.

The same induction gate from C6 remains: uniform one-step uniqueness on every reachable state implies every finite addition horizon.

Conversely, any globally realizable same-rooted-`G0` pair with different reduced codes and nonisomorphic successors kills raw one-step sufficiency immediately.

## 9. Deterministic certificate

Checker:

`scripts/check_r043c7_root_local_jx_realizable_completion_orbits.py`

Certificate:

`research_artifacts/R043C7_ROOT_LOCAL_JX_REALIZABLE_COMPLETION_ORBIT_CLASSIFICATION/RESULTS.json`

The checker independently verifies:

- exact frozen FCC/HCP 12-contact root links;
- every native root edge has four common neighbors;
- complete feasible shell enumeration under `I != empty` and `E(I,Z)=empty`;
- exact row-signature isomorphism classes;
- HCP zero shell-orbit ambiguity;
- the two and only two FCC row-signature ambiguity classes;
- exact resolution of both FCC classes by the `Z` internal degree multiset;
- exact shell alignment-index spectra and the universal bound `<=8`.

WL hashes are used only as safe candidate buckets. Every class split and completion comparison is confirmed by exact graph isomorphism.

## 10. Final classification

Primary classification:

`REDUCED_TO_STRICTLY_SMALLER_FINITE_EXTENSION_INVARIANT`.

FCC:

`KAPPA_PLUS_TWO_EXCEPTION_DELTA_PLUS_ALIGNMENT_LE_8_PLUS_OUTER_PORT_GLUE`.

HCP:

`KAPPA_PLUS_ALIGNMENT_LE_8_PLUS_OUTER_PORT_GLUE`.

No harmful rooted-`G0` collision is claimed.

No raw-`G0` sufficiency theorem is claimed.

No Foundation promotion is requested.

Recommended successor:

`SECOND_SHELL_PORT_GLUE_ORBIT_CLASSIFICATION_UNDER_ROOT_SHELL_STABILIZER`.
