# R059D Stage K — BRC6 Selector Identifiability / True Relational State Dynamics

Researcher-ID: `EM-R059D-9C6B2A`

Taskbook source: `9ea3c173873b23f52977a7ba99e9c091329e5748`

Frozen Stage-J BRC6 head: `9f2b70d6cca5ccd66a46cc6dd18730f40a6add72`

## Disposition

`BRC6_SELECTOR_DEPENDENT_BUT_TRUE_STATE_DYNAMICS_FOUND`

Stage K preserves the Driver's Stage-J strength exactly: BRC6 is a cyclic-equivariant partial selector construction, not a total or canonical native law. The Stage-J embedded `EM-R059D-4C7E21` label is treated only as stale provenance text; the authoritative BRC6 identity from this stage forward is `EM-R059D-9C6B2A`.

## 1. Full pre-frozen comparator audit

Before scoring new Stage-K witnesses, the registry was frozen with 1,258 exact label-blind controls:

- F0 C0 max/min;
- Stage-J F1 lexicographic maximum;
- reverse-horizon F1R;
- endpoint C3 max/min;
- visit-sum max/min;
- coefficient-free Pareto dominance;
- F3 lex tournament;
- all 624 nonzero theta in `{-2,-1,0,1,2}^4`, each with MAX and MIN polarity.

Every comparator uses identical arithmetic on every channel and never reads absolute channel number, target identity, N/q-specific output tables, or candidate segment L.

### W_ASYM_BASE

Exact resolved-output counts over all 1,258 controls are:

`channel 0: 44`
`channel 4: 521`
`channel 5: 583`
`unresolved: 110`

Therefore:

`SELECTOR_DEPENDENT`

is exact. F1 selects 4, reverse lex / endpoint max / visit max select 5, and admissible F2 controls also resolve channel 0. F1 is not protected from this negative identifiability result.

Freeze:

`BRC6_SELECTOR_CANONICALITY = NOT_ESTABLISHED`.

### Nonempty robust state domain

A predeclared dominance witness has one candidate with spectrum

`(10,15,20,25)`

and five equal competitors

`(5,6,7,8)`.

Across all 1,258 controls:

- 623 comparators resolve;
- every resolved comparator selects channel 2;
- 635 are unresolved;
- zero controls resolve a conflicting channel.

Freeze:

`BRC6_SELECTOR_ROBUST_STATE_DOMAIN = ESTABLISHED_NONEMPTY`.

This is a robust state domain, not a proof of one universal comparator.

## 2. Four unresolved/dependence classes

Stage K distinguishes all required cases.

`SELECTOR_DEPENDENT`:
W_ASYM_BASE and W_S1_TIE_S2_RESOLVE have conflicting exact resolved outputs across the frozen comparator registry.

`SELECTOR_CONSENSUS_RESOLVED`:
W_CONSENSUS_DOMINANT2 has one common resolved output, channel 2.

`SYMMETRY_UNRESOLVED`:
W_FULLY_SYMMETRIC has six identical candidate spectra. All 1,258 comparators are unresolved and the exact cyclic symmetry obstruction applies.

`SIGNATURE_INSUFFICIENT_UNRESOLVED`:
W_SIGNATURE_INSUFFICIENT_PAIRS has candidate spectra in three exact duplicate pairs `[X,X,Y,Y,Z,Z]`, so all 1,258 Z-based controls are unresolved. Its full S0 diagnostic diagonal pattern `(3,10,20,30,40,50)` has no nonzero cyclic period, so no declared cyclic-stabilizer impossibility theorem is available. The finite selector signature is therefore insufficient rather than symmetry-forbidden.

`BRC6_UNRESOLVED_BY_CURRENT_SIGNATURE` remains evaluator status, never a seventh BRC output.

## 3. Horizon audit

The frozen horizon registry is:

`K in {0,1,2,3,4,6,8}`.

For the Stage-J affine continuation quotient

`C_n^d = A_d + n I[d]`,

the first two coordinates determine the entire continuation:

`C0=A`
`I=C1-C0`.

Hence if two candidates tie at K=1, they tie at every deeper horizon.

Freeze:

`AFFINE_HORIZON_DISCRIMINATION_SATURATES_AT_K1`.

W_S1_TIE_S2_RESOLVE is unresolved at K=0 but F1 selects channel 5 for every tested K>=1, so:

`HORIZON_INSUFFICIENT_UNRESOLVED_RESOLVED`

is explicitly realized.

W_FULLY_SYMMETRIC remains symmetry-unresolved at every depth. The pair-duplicate signature-insufficient witness remains unresolved at every depth within this affine signature family.

## 4. Pure-relational port carriers

Three frozen carriers were scored.

### Carrier A
Nodes `x in Z/6Z`

`T_NODE(x,d)=d`

`T_INGRESS(x,d)=d+2 mod6`

### Carrier B
Nodes `(a,b) in Z/6Z x Z/2Z`

`T_NODE((a,b),d)=(d, b XOR ((d-a) mod2))`

`T_INGRESS((a,b),d)=d+3 mod6`

### Carrier C
Nodes `x in Z/6Z`

`T_NODE(x,d)=x`

`T_INGRESS(x,d)=d+1 mod6`

These are relational transport tables only. No angle/opposite/vector semantics are introduced.

For every carrier and every decision node:

`L(x,0)=...=L(x,5)=4`.

The exact covariance identities

`T_NODE(tau x,tau d)=tau T_NODE(x,d)`
and
`T_INGRESS(tau x,tau d)=tau T_INGRESS(x,d)`

hold.

## 5. True state update

After selecting d at current node x with ingress i, Stage K really updates:

`O_x[d] += 1`
`M_x[i,d] += 1`

then traverses the declared equal-L segment and records at the target:

`I_y[j] += 1`

with

`y=T_NODE(x,d)`
`j=T_INGRESS(x,d)`.

Every next BRC6 decision is recomputed from the newly accumulated exact I/O/M state.

No Stage-J normalized profile is reused.

## 6. True multi-step dynamics

All 1,258 comparators were executed on all three carriers for 48 actual aligned decisions or until unresolved, from both W_ASYM_BASE and W_CONSENSUS_DOMINANT2.

For W_ASYM_BASE the first-decision distribution remains, on each carrier:

`0:44, 4:521, 5:583, unresolved:110`.

By decision 48:

- carriers A/B: 545 controls remain resolved through the window and 713 have stopped unresolved;
- carrier C: the same 545/713 split holds, with more distinct exact channel words.

Representative true-state channel projections from W_ASYM_BASE:

Carrier A:
- F1: `4,0,4,0,...`
- F1R: `5,1,3,5,1,3,...`
- representative F2-to-0: `0,4`, then unresolved.

Carrier B:
- F1: `4,1,4,1,...`
- F1R: `5,2,5,2,...`
- representative F2-to-0: `0,4`, then unresolved.

Carrier C:
- F1: channel 4 throughout the proved 48-decision window;
- F1R: repeated 5 then later 0 within the proved window;
- representative F2-to-0 produces a longer state-dependent word before unresolved.

These are true channel-label projections generated by actual state updates. They are not full-state periods.

At every resolved decision exactly one O count increments. Therefore

`TOTAL_O(e)=TOTAL_O(0)+e`.

The complete relevant exact state can never repeat at two distinct resolved epochs. Consequently repeated output-label words are projections of a strictly count-growing state, not certified full-state cycles.

This is the required correction to Stage-J profile-reuse diagnostics.

## 7. Selector dependence becomes trajectory dependence

Using the same W_ASYM_BASE and each carrier, representative admissible selectors with first outputs 4, 5, and 0 were cross-tested for 120 decisions.

No first-output-distinct representative pair exactly recoalesced to the same full state at the same epoch within the proved 120-decision window.

Freeze:

`BRC6_SELECTOR_DEPENDENT_DYNAMICS = ESTABLISHED`.

`BRC6_DYNAMIC_RECOALESCENCE_ACROSS_SELECTORS = NOT_ESTABLISHED`.

The latter is only a finite-window negative; it is not promoted to a global impossibility theorem.

## 8. True trajectory perturbations

Baseline: W_ASYM_BASE under F1 on all three frozen carriers.

First-decision exact six-way response tables:

Count token `A_j += 1`:
`[0,1,2,3,4,5]`

Incidence event `I_j += 1`:
`[4,4,4,4,4,4]`

Tagged launch contribution `j -> j+1`:
`[1,2,3,4,5,0]`

Within 96 actual decisions:

- no tested perturbation exactly recoalesced with the baseline full state at the same epoch;
- all six incidence perturbations preserve the F1 channel projection through the 96-decision window while the exact states remain different;
- count-token and tagged-adjacency perturbations usually diverge at decision 0.

Unresolved states can also be created or removed exactly:

- W_S1_TIE_S2_RESOLVE has F1=5; `I[3]+=1` creates an exact maximal tie between channels 3 and 5 and makes F1 unresolved;
- from W_FULLY_SYMMETRIC, one count token or one incidence event resolves F1 to the perturbed channel; one tagged launch transfer `j->j+1` resolves F1 to `j+1`.

All perturbations preserve equal candidate L.

## 9. Large-N system scale

For every frozen huge N around `10^36`, use the replicated family

`A_d(N)=N+A_d(0)`.

Then

`C_n^d(N)=N+C_n^d(0)`.

F0/F1/F1R/endpoint/visit/Pareto/F3 comparisons are unchanged by this common shift. Every F2 score acquires the same additive term

`N * sum(theta)`

for all six candidates, so every F2 winner/tie is also unchanged.

The true state update inherits the same identity inductively: initialize every local O[d] with the common N background, then each actual event contributes the same candidate-specific +1 increments as in the small-state process. Thus every BRC6 output, unresolved status, and port-transport choice is exactly N-invariant.

No huge object enumeration occurs.

`N` is not L and no length threshold is searched.

## 10. Final selector status

Stage K establishes both:

`BRC6_SELECTOR_ROBUST_STATE_DOMAIN = ESTABLISHED_NONEMPTY`

and

`BRC6_SELECTOR_DEPENDENT_STATE_DOMAIN = ESTABLISHED`.

Because W_ASYM_BASE has exact comparator conflict, the stage does not promote F1 or any other comparator to a unique native law.

Primary disposition:

`BRC6_SELECTOR_DEPENDENT_BUT_TRUE_STATE_DYNAMICS_FOUND`.

Continue:

`BRC6_TOTAL_SELECTOR = NOT_ESTABLISHED`

`BRC6_SELECTOR_CANONICALITY = NOT_ESTABLISHED`.

## 11. Checker

Deterministic checker:

`772 / 772 PASS`

Checks digest:

`9e1f44b80da24096967b8ee86f1ddede57a07dca26fbc0be22878ca9981826d0`

The checker reconstructs all 1,258 comparators, exact witness classifications, horizon theorem, port covariance, all-comparator 48-step trajectory digests, perturbation tables, and huge-N common-shift invariance.

## Firewalls

`PHYSICAL_DIRECTION_CALIBRATION = NOT_ESTABLISHED`

`PHYSICAL_PROBABILITY_FROM_BRC_COUNTS = NOT_ESTABLISHED`

`PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`

`PHYSICAL_ELASTICITY_INTERPRETATION = NOT_ESTABLISHED`

`QUANTUM_BRIDGE = NOT_ESTABLISHED`

`STOP_FOR_DRIVER_REVIEW`
