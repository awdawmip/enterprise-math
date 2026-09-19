# Heartbeat World BRC: joint residue × environment ports

Status: `RESEARCH_CONSTRUCTION / EXECUTED_FINITE_CERTIFICATE / NOT_FOUNDATION`
Date: `2026-09-20`

## Why the product state matters

The residue-port and environment-port results solve different information problems. Residue belongs to a spatial congruence fiber; the six-channel environment mask is typed external control state. When an interaction depends on both, BRC must test the joint port rather than assume that two separate marginal summaries can be combined later.

Use residue `r in Z/4Z` and the 64 binary environment masks from the prior environment experiment, giving 256 raw finite control states. The declared starting partition is the product of the two-class macro residue quotient `{0,3}/{1,2}` and the 13-class D6 environment quotient, hence 26 classes.

## Exact refinement ladder

A symmetry-safe packet rotates the six-channel mask and applies an X6 translation whose sign depends only on the macro residue class and whose magnitude depends only on an environment orbit invariant. `certify_control_partition` accepts the 26-class product quotient.

Then add independently:

- `MICRO`: the within-cycle fine block swap, which distinguishes the two raw residues inside each macro residue class;
- `PHASE`: a phase-addressed environment update/effect that depends on heartbeat slot 0.

Exact effect-valued refinement gives:

| allowed future packet family | retained classes |
|---|---:|
| SAFE | 26 = 2 × 13 |
| SAFE + MICRO | 52 = 4 × 13 |
| SAFE + PHASE | 128 = 2 × 64 |
| SAFE + MICRO + PHASE | 256 = 4 × 64 |

Thus each formerly omitted repair coordinate becomes necessary exactly when a future operation can observe/use it. The result is a finite, declared-language statement, not a universal minimal representation of Heartbeat World.

## Separate marginals are not enough for a coupled effect

Let the macro residue sign be `+` or `-`, and let the environment gate be even/odd occupied-count parity. Use spatial displacement magnitude `4*(1+gate)` with the macro sign.

Two positive distributions have identical residue marginals and identical environment marginals:

- A: half on `(+ , gate0)`, half on `(- , gate1)`;
- B: half on `(+ , gate1)`, half on `(- , gate0)`.

Yet their mean displacements are `-2 e1` and `+2 e1` respectively. The lost information is the joint pairing. Therefore `marginal residue summary + marginal environment summary` is not an observer-safe replacement for the joint BRC port when the effect couples the two coordinates.

An independence or exact factorization certificate can make marginals sufficient for a specified observer, but independence must be declared/proved; it cannot be manufactured by Cartesian-product recombination after joint provenance was erased.

## BRC consequence

This gives a general design rule for the current tool family: compose typed repair coordinates by product only as far as the declared future language requires, then let exact quotient/refinement remove dimensions of control state that are provably invisible. Do not encode control state as extra X6 axes, and do not split a coupled joint distribution into unrelated positive marginals without a certificate.

Local regression: previous 15 tests plus 3 new joint-port tests = 18 passed. No full repository suite, independent review, production Nollm mutation or semantic recall benchmark is claimed.
