# Causal Collapse Spectrum Core — Reinterpreting P011 as a General Finite Collapse Spectrum

Status: `CROSS-ROUTE RESEARCH WIP / REINTERPRETATION OF PROVED P011 FINITE THEOREMS`

Suggested owner: A1/P011. This note records the causal-absorption derivation.

## 1. Correction

P011 began from irreversible forward maps that merge fine histories into coarse states. The same fiber mathematics now appears in temporal history merge, cross-future forgetting, task-signature reduction, finite coarse observation, finite dimension contraction, and measurement collapse. Therefore `J_k` has a more basic meaning than entropy or irreversibility.

## 2. CC-01 — Any finite causal collapse

Let `X` be a finite set of states currently distinguished by the theory and let

\[
q:X\to Q
\]

be any declared abstraction, forgetting operation, or observation. Define

\[
m_q(z)=|q^{-1}(z)|
\]

and

\[
\boxed{J_k(q)=\sum_{z\in\operatorname{im}q}\binom{m_q(z)}k.}
\]

## 3. CC-02 — Universal distinction-loss meaning

`J_k(q)` counts the `k`-element fine-state subsets whose members were distinct before `q` but receive one common coarse label after `q`. P011 already proves that the complete spectrum recovers the fiber-size multiset by integer binomial inversion.

## 4. CC-03 — Different domains are different causal roles of one collapse

- Temporal irreversibility: `q` is a history-to-current-state map.
- Signature coupling: `q=rho:Q_AB->R` forgets cross-future information.
- Task precision: `q` restricts a full future signature to the task signature.
- Measurement: `q` maps fine causal states to observation labels.
- Dimension contraction: on finite sections/balls, `q` maps fine relation states to coarse partition states.

Thus irreversibility, coupling loss, precision loss, and contraction loss are different interpretations of the same finite causal-collapse structure.

## 5. CC-04 — Staged collapse already has exact P011 accounting

For

\[
X\xrightarrow{F}Y\xrightarrow{G}Z,
\]

P011 proves

\[
J_k(G\circ F)\ge J_k(F)
\]

and gives exact collision increments counting newly cross-old-fiber `k`-history groups. No separate entropy chain rule is needed for this finite distinction-loss accounting.

## 6. CC-05 — The spectrum is not the full causal state

The complete spectrum recovers fiber-size multiplicities but not fiber identities, incidence, or which concrete witnesses were merged. Hence

\[
\boxed{\text{collapse relation / witness} > \text{collision spectrum} > \text{scalar shadows}.}
\]

This matches P021: anonymous cardinality statistics are not automatically sufficient for future composition when witness identity remains operationally relevant.

## 7. Traditional entropy/information status

Any finite symmetric scalar depending only on the fiber-size multiset is a postprocessing of the complete `J_k` spectrum. This does not derive thermodynamic entropy, Shannon coding theorems, or continuous information theory. The narrower claim is that finite causal distinction loss has an exact integer mother object below many traditional scalar summaries.

## 8. Orthogonality to support

The collapse spectrum says how existing fine states are identified. It does not say which theoretical combinations never exist. Accordingly, typed signature coupling `(M,S)` separates support/reachability defect `M` from cross-future-forgetting collapse defect `S` and `C_k`.

## 9. Existing tools

No new computational primitive is needed. Reuse P011, `causal_count_measure.py::collision_count`, `collision_interaction_basis.py`, and `causal_signature_coupling.py`.

## 10. Next

1. identify the structural analogue of finite collapse spectra for infinite integer relation systems;
2. connect A3 lost relation rank with `J_k` profiles on finite balls;
3. characterize operation languages for which anonymous spectra are future-safe;
4. make P021 witness necessity the composability gate of the collapse core.
