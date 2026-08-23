# CBRC F5 Blind Input — Forgetful Branch Semantics Gate

Status: `DRIVER_FROZEN_BLIND_INPUT`
Date: `2026-08-23`
Driver-ID: `EM-DVR-CBRC-F0-7C3A21`

This packet isolates one semantic question. It is not a downstream wave/amplitude task.

## 1. Canonical Path-formal facts

On the current component-typed BRC bridge:

- a Path-formal BRC element is a finite formal `N`-sum of typed composable concrete path witnesses;
- each witness retains generator word, prefix cell trajectory, typed placement and terminal;
- augmentation forgets provenance and keeps multiplicity;
- Boolean BRC keeps only support;
- the minimal `(1,1)` commuting diamond contains two distinct concrete witnesses with one common typed terminal.

Canonical source for these facts:

`definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md`

blob SHA:

`6ec0d73a19e28ec586c59a97d24f5798c9119771`.

## 2. Accepted signed/enriched coefficient boundary

Earlier accepted forward work established a conservative signed completion of occurrence coefficients and later coefficient enrichments equipped with a forgetful additive retraction to the old signed occurrence coordinate.

For F5, represent only the abstract part:

`pi : C -> Z e`

with embedded old signed occurrence generator `e` and

`pi(e)=e`.

`pi` forgets coefficient enrichment only. It is not a final scalar readout.

Do not assume any particular finite torsion group, phase group, ring, norm, or rank-two structure.

## 3. Marked refinement bookkeeping

A pre-collapse two-branch bookkeeping state is a pair

`(x,y) in C ⊕ C`.

A local reversible refinement/mixing may send

`(e,0) -> (x,y)`.

The two marked slots are intended to represent retained alternatives before marker erasure. Existing issued semantics require the two enriched outputs to be nonzero in `C`, but did not previously state that each output must remain nonzero after applying `pi`.

## 4. Accepted F4 mathematical boundary

F4 classified the following facts at accepted scope:

1. `GLOBAL_ZERO_SEPARATION` alone does not force torsion-free rank to increase from one.
2. In torsion-free rank one with arbitrary finite torsion, every globally zero-separating balanced conserving model induces a **signed-permutation** free quotient block.
3. A pure-enrichment/torsion output can evade this obstruction: an elementary split may have two nonzero enriched outputs while one output has zero projection to the old signed coordinate.
4. Therefore the rank-lift question turns on whether such a projection-zero marked alternative is semantically admissible as a refinement of an old Path-formal occurrence.

Accepted Driver review:

`driver_reviews/CBRC_F4_POSITIVE_SEPARATION_RANK_LIFT_DRIVER_REVIEW_20260823.md`

source commit:

`de9f70687b83a3921d4961376a6f94330826eab4`.

## 5. Candidate condition — NOT accepted

Define the candidate:

`FORGETFUL_BRANCH_NONDEGENERACY`

For an elementary refinement

`M(e,0)=(x,y)`, require

`pi(x) != 0` and `pi(y) != 0`.

Interpretation candidate only: after forgetting the newly added coefficient enrichment, each retained branch would still carry a nonzero old signed/path-occurrence contribution.

F5 must **not** assume this is already native truth.

## 6. F5 question

Classify the semantic status of `FORGETFUL_BRANCH_NONDEGENERACY`:

- Is it forced by the existing meaning of Path-formal witness, marked alternative, conservative coefficient enrichment, refinement, and no-resurrection?
- Is it compatible but genuinely additional?
- Is it too strong or inconsistent with legitimate native refinements?
- Is a weaker exact condition derivable instead?

If and only if a nondegeneracy condition is actually derived from existing semantics, state the exact rank consequence obtained by combining it with the accepted F4 free-block theorem.

Do not select or construct a rank-two carrier in F5.

## 7. Firewall

Before raw freeze, do not read/use:

- downstream coherent-BRC/wave free research;
- R063/R064/R065/FQ mathematics;
- external quantum mechanics, Hilbert spaces, Born rules, quantum walks, path integrals, wave equations;
- preselected complex/quadratic carriers, finite phase groups, norms, inner products, square laws, known splitter matrices.

The task is a semantic derivability / independence classification only.
