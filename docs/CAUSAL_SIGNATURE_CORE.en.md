# Causal Signature Core — Generating Mathematical Structure from LEGO States, Causal Operations, and Future Signatures

Status: `ACTIVE CROSS-ROUTE RESEARCH ORIENTATION / NOT YET CANONICAL FOUNDATION`

This note consolidates the correction away from "traditional mathematics + precision annotation". It creates no new canonical problem number and does not modify `我眼中的世界.md`.

## 1. Three primitive layers

### LEGO state / composition
States are built from discrete units and their relations. In an independently composable regime there is an operation `x ⊕ y`; unit count `1` does not change with dimension.

### Causal operation language
Only declared finite operation words generate futures. The theory does not assume that every mathematically definable transform is physically or semantically allowed.

### Observation language
Only declared discrete/integer observations are read. Different future tasks may use different observation languages.

## 2. CS-01 — Future signature

For a state `x`, define the labeled future signature

\[
\boxed{\Sigma(x)(\omega,o):=o(\omega(x)).}
\]

The operation and observation identities remain part of the label; `Sigma(x)` is a causal experiment-result table, not a real embedding.

## 3. CS-02 — Theory-level state equality

For the declared future language,

\[
\boxed{x\equiv_\Sigma y\iff\Sigma(x)=\Sigma(y).}
\]

If no allowed finite future experiment distinguishes two states, the current theory should collapse them to one state.

## 4. CS-03 — Collapse before precision

The causal collapse is

\[
C_\Sigma:X\to X/{\equiv_\Sigma}.
\]

The order is therefore

\[
\boxed{\text{future indistinguishability}\to\text{collapse}\to\text{remaining structure}.}
\]

Precision is only a later diagnostic describing how much future distinction remains.

## 5. Finite-depth signatures

Restricting to operation words of length at most `t` gives `Sigma_t` and equivalence `~_t`. These equivalences refine monotonically with depth and form the common mother object for depth topology, agreement geometry, and future precision.

## 6. Traditional shadows

- **Quotient:** representation of future-signature equivalence classes; future indistinguishability is causal, quotient is encoding.
- **Linear algebra:** when LEGO composition is free integer addition and operations preserve composition, matrices are unit-effect tables; kernel/rank/basis/observability are shadows of future distinguishability.
- **Topology / ultrametric:** finite-depth equivalence classes form a clopen basis; first distinguishing depth obeys a non-Archimedean similarity law. A real ultrametric is only a recoding.
- **Metric / norm:** transport geometry comes from shortest causal program cost. P012 graph distance is an existing special case; `L1` is a closed form for one generator family.
- **Measure / probability:** a collapsed signature class has integer weight equal to the number of fine unit histories in its fiber. Probability is a later count-ratio rendering under additional sampling semantics.
- **Nonlinearity / Taylor:** failure of LEGO composition is analyzed by exact finite interaction spectra. Repeated-unit fiber responses expand in the P011 collision basis `J_k`.

## 7. CS-05 — Traditional-tool absorption criterion

A traditional structure `T` may enter core only after proving a causal signature object `S` for which `T=Shadow(S)`, with the shadow preserving the actual future distinctions and not installing hidden continuum state or undeclared operations.

Otherwise the traditional structure remains external tooling.

## 8. Current first-stage absorptions

First-stage causal derivations now exist for quotient/congruence, finite integer linear rank/kernel/observability, causal probe bases, finite-depth clopen topology, agreement depth, P012 word metric, finite counting measure, exact count-ratio probability shadows, LEGO interaction spectra, and the P011 collision-interaction basis.

Not yet absorbed: general real vector spaces, Euclidean inner products as primitive, general norms, manifolds, calculus as foundation, Hilbert/Banach completion, arbitrary probability measures, continuous stochastic processes, Lebesgue measure, and quantum amplitudes.

## 9. Executable sources

Current experimental sources include `causal_future_module.py`, `causal_probe_basis.py`, `lego_additive_operation.py`, `causal_count_measure.py`, `lego_interaction_spectrum.py`, and `collision_interaction_basis.py` with corresponding tests.

## 10. Next target

Do not keep adding traditional invariants. The next primary target is the **signature composition law**:

1. how two causal subsystems generate a joint future signature;
2. when collapse preserves composability without restoring fine state;
3. when transport geometry, interaction spectra, and counting weights all descend through one signature quotient;
4. identify the first important traditional tool that cannot be absorbed by the signature core and make that boundary explicit.
