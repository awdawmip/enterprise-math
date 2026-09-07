# BRC Finite-Group Phase Recoalescence — BSGS Square-Root Boundary

Status: `RESEARCH FRONTIER / EXACT PHASE-BRC REFORMULATION + SCOPED TWO-SUPPORT LOWER BOUND + PRIOR-ART BOUNDARY / NO SPEEDUP CLAIM`
Date: `2026-09-08`
Parent: `research_notes/BRC_CELL_COLLAPSE_PHASE_CARRIER_BOUNDARY_20260908.md`
Source snapshot before write: `main@0b94cdb653bece7247d7b42f88e342b66f2f270a`

## 0. Purpose and typing

The parent note identified finite multiplicative-group phase as a capability missing from the current positive-rational BRC carrier. This continuation introduces only the minimum abstract typed semantics needed to audit the algorithmic value of such a phase extension.

It does **not** promote a new Foundation family and does not identify group phase with positive branch weight.

Let `G` be a finite group, let `alpha in G`, and let the cyclic subgroup `<alpha>` have order `M`. A labeled exponent branch `x` carries the group value

`P(x)=alpha^x`.

For a target `Y=alpha^S`, recoalescence is exact group equality

`P(x)=Y`.

If the searched exponent interval has length `<M`, or more generally contains at most one representative of the congruence class `S mod M`, then a positive collision identifies the unique desired exponent once its branch provenance is retained.

This is a phase/equality carrier, not positive-mass recoalescence.

---

## 1. Factor-sum phase instance

For semiprime `N=pq`, `S=p+q`, every `alpha in (Z/NZ)^*` satisfies

`alpha^(N+1)=alpha^S (mod N)`.

Thus the factoring target is a phase collision between the known group value

`Y=alpha^(N+1)`

and a candidate exponent family for `S`.

The group value `Y` is N-only and cheap to compute. The hard operation is the inverse/collision search that recovers the exponent label.

A quotient that keeps only the fact

`Y belongs to {alpha^x : x in C}`

is not generally enough to recover `S`: unlike the one-factor gcd threshold, a positive phase-membership result returns only the already-known group value `Y`, not the exponent. Some exponent provenance or an equivalent decoding coordinate must survive.

Freeze:

`PHASE_MEMBERSHIP_POSITIVE != EXPONENT_RECOVERY`.

This is the key observer difference from the Boolean one-factor activation route.

---

## 2. BSGS is exactly a two-family BRC recoalescence

Let the candidate exponent interval contain `C` consecutive candidates. Choose a radix `m>=1` and write each candidate uniquely in the form

`x=x0+i*m+j`,

with

`0<=j<m`,

and `i` ranging over about `ceil(C/m)` values.

Define the baby branches

`B_j=alpha^(x0+j)`,

and giant/target branches

`G_i=Y*alpha^(-i*m)`.

Then

`B_j=G_i`

iff

`alpha^(x0+i*m+j)=Y`.

Under the no-wrap/injectivity condition, this collision is exactly the desired exponent branch.

So Shanks baby-step/giant-step is already a canonical BRC program:

`candidate exponent branching -> two typed phase supports -> equality recoalescence -> provenance pair (i,j) -> exponent reconstruction`.

No new factoring method follows from renaming this collision as BRC.

---

## 3. Exact square-root optimum in the explicit two-support model

Consider any explicit two-family meet-in-the-middle phase realization in which:

- a left support has `A` enumerated states;
- a right support has `B` enumerated states;
- every one of the `C` candidate exponents is represented by at least one pair of left/right branch choices;
- a candidate is recognized by equality/recoalescence of one state from each side.

Then necessarily

`A*B >= C`.

If the construction cost is at least linear in the number of explicitly materialized support states, its group-state work is at least

`A+B >= 2*sqrt(A*B) >= 2*sqrt(C)`.

Balanced BSGS takes `A,B=Theta(sqrt(C))` and achieves this bound up to rounding and group-operation/logarithmic costs.

Therefore:

`EXPLICIT_TWO_SUPPORT_PHASE_BRC -> THETA(sqrt(C)) SUPPORT WALL`.

This is a scoped lower bound only. It does not cover algorithms using additional algebraic structure, implicit batch evaluation, non-explicit supports, non-generic group properties, or a different candidate parameterization.

---

## 4. Multi-branch splitting does not automatically evade the wall

Splitting the exponent into many radix digits creates a k-way additive candidate relation, but ordinary meet-in-the-middle groups the digits into two superfamilies. If the two superfamily cardinalities multiply to at least `C`, the same square-root balancing reappears.

Thus simply increasing the BRC branch arity does not by itself yield `C^(1/k)` search. To beat the square-root phase wall, the algorithm must exploit structure beyond explicit Cartesian candidate decomposition, such as:

- a fast transform/convolution compatible with the actual group and candidate set;
- algebraic constraints that reduce the candidate population before collision;
- a collective implicit phase evaluator with sub-support construction cost;
- or number-theoretic relations tying many candidate phase values together.

No generic k-way speedup is claimed or ruled out beyond the explicit meet-in-the-middle model.

---

## 5. Interpretation of exponent one fifth

Harvey's deterministic `N^(1/5+o(1))` algorithm explicitly reviews the Pollard/Hittmeir phase equation

`alpha^(p+q)=alpha^(N+1) mod N`

and states that its further exponential improvement comes from applying BSGS much more aggressively across the global candidate space rather than chunking many smaller searches.

Structurally this is consistent with the phase-BRC audit:

- the main progress is **candidate-space organization/reduction** and global reuse;
- the final phase recoalescence still obeys the square-root meet-in-the-middle law on the organized candidate population.

Heuristically, a candidate population of power size `N^(2/5+o(1))` paired with a square-root phase collision naturally produces the `N^(1/5+o(1))` scale. The exact Harvey algorithm contains additional arithmetic structure and should not be reduced to this slogan for proof purposes; the slogan is only an exponent-level BRC interpretation.

---

## 6. Large order is an injectivity/provenance lease, not a free residue oracle

The identity

`alpha^(N+1)=alpha^S`

implies `S` modulo `ord(alpha)` mathematically, but an element of large order does **not** make that exponent residue computationally available for free.

Large order instead enlarges the range on which exponent branches remain distinguishable before wraparound and makes BSGS/collision searches valid over larger candidate sets.

Therefore the parent phrase “an order-M phase supplies an S phase modulo M” must be read as a semantic relation conditional on successful exponent decoding, not a zero-cost observer.

Freeze:

`LARGE_ORDER = PHASE_INJECTIVITY_CAPACITY`,

not

`LARGE_ORDER = FREE_DISCRETE_LOG`.

Harvey-Hittmeir's 2026 large-order work improves the deterministic construction of the **carrier capacity**; the subsequent exponent/candidate search remains a separate algorithmic task.

---

## 7. Observer-safe compression boundary

Within the finite-group phase carrier, what may be quotiented safely depends on the declared future operation.

If the goal is only to test whether a known exponent candidate is correct, group equality alone is sufficient.

If the goal is to recover an unknown exponent from a population, merging all candidate branches that merely share “nonempty support” is unsafe: a positive result loses the exponent label.

A BSGS table retains exactly the needed repair coordinate:

- group value for collision;
- baby/giant index provenance for exponent reconstruction.

Any proposed BRC compression must either preserve an equivalent decoding coordinate or prove that the final arithmetic operation (for example a proper gcd) returns the factor without needing the exponent label.

This is why Boolean support was sufficient for one-factor interval activation but not for phase-discrete-log recovery.

---

## 8. New algorithmic target after the phase audit

A finite-group BRC extension becomes interesting only if it changes one of the two quantities that ordinary BSGS fixes:

1. **candidate population C** — use new N-only arithmetic/BRC structure to reduce the guaranteed factor-bearing exponent/linear-form family below the best known parameterization;
2. **support exponent 1/2** — construct or test the phase recoalescence over C candidates in `o(sqrt(C))` effective work by an implicit algebraic operation not equivalent to ordinary BSGS/multipoint evaluation.

The current collision-energy/local-residue results do not yet reduce a growing candidate population, and the explicit phase BRC does not beat the `sqrt(C)` support wall.

Thus the immediate promising question is not “can BRC represent BSGS?” — it can — but:

> Can the multiplier-boundary/collision geometry produce a smaller guaranteed candidate family for `S` or for Lehman-type linear forms **before** the finite-group phase collision, while preserving N-only evaluability?

Any such reduction must be compared against Harvey/Hittmeir's existing candidate organization, not against naive `S` search.

---

## 9. Kill conditions

Kill a phase-BRC claim if:

- it is ordinary BSGS with branch terminology;
- it treats a high-order element as though its discrete logarithm were already known;
- it discards exponent provenance and then assumes a positive phase membership recovers the exponent;
- it reports `C^(1/k)` from k-way branching without accounting for the k-sum/recoalescence constructor;
- it ignores the `A*B>=C` support product in an explicit two-family search;
- it claims novelty from the identity `alpha^(N+1)=alpha^S` itself.

Retain only a new candidate-space reduction or a genuinely sub-square-root implicit phase collision with fully costed construction.

No Foundation promotion, Working Truth promotion, or factorization-speedup claim is made.