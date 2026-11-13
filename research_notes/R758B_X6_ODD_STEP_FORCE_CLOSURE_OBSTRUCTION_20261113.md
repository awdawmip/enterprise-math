# R758B — Exact X6 odd-step obstruction to interpreting primitive triadic force balance as spatial walk return

**Source scope:** P000 V5 at frozen scientific pin `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; Source `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`. **Classification:** exact theorem and counterexample to one explicitly specified candidate force-to-coordinate mapping; this does not invalidate P000 or rule out more refined triadic force dynamics. **Parent:** `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, `TP2-8B7E13C5904A2D6F1142`.

## 1. A tempting candidate mapping and the discriminating test

In the frozen X6 native spatial Cell torsor over `Z^6`, the **pure coordinate** primitive adjacency moves are `T_i^±(c)=c±e_i`. Consider the *candidate* (not a frozen foundation theorem):

- identify each primitive force quantum with exactly one signed native coordinate step `±e_i`;
- declare a group of `k` force quanta stable exactly when its `k` corresponding steps return to the starting spatial Cell.

This proposal conflates `PRIMITIVE_FORCE_QUANTUM` with `X6_PURE_COORDINATE_ADJACENCY` and `TRIADIC_CLOSURE_E` with `NATIVE_CELL_RETURN`. P000 itself neither requires nor grants those identifications. We test this optional proposal because it would supply a very short bridge from primitive balance to path dynamics if it worked.

## 2. Parity obstruction: every odd pure-coordinate walk has nonzero displacement

**Theorem R758B.1.** In X6, no walk consisting of an odd number of primitive coordinate steps `±e_i` can return to its starting native Cell.

*Proof.* Choose a Cell anchor only to express displacement coordinates; no ontic global origin is introduced. Define `\chi(z)=\sum_{i=1}^6 z_i\pmod 2`. Every `+e_i` or `-e_i` changes `\chi` by `1\pmod2`. A walk of odd length therefore changes `\chi` by `1`, whereas a returned Cell has zero displacement and parity `0`. This contradiction is independent of the axis labels, signs, order, or starting Cell. □

In particular all `12^3=1728` ordered three-step signed native paths fail to return, including repeated-axis paths. Conversely exactly `12` of the `12^2=144` two-step walks do return: choose one of twelve directions, then its inverse.

**Corollary R758B.2 (two-sided failure of the candidate mapping).** The candidate `stable iff native coordinate return` cannot reproduce P000's fixed primitive balance arity. It would assign `stable=true` to some two-force sequences even though P000 forbids primitive two-force stability, and `stable=false` to every three-force sequence although P000 admits canonical equal-quantum triadic closure. **This refutes that candidate interpretation, not P000's three-force balance law.**

## 3. Canonical three-distinct-axis refinement, multiplicity and observer scope

Assume three canonical equal-quanta inputs are associated to three different native axes `i,j,k`, using one signed primitive coordinate step on each. The possible unordered signed-axis sets number

`C(6,3)·2^3=20·8=160.`

Each has exactly `3!=6` orderings of the same three individual steps, giving `160·6=960` ordered three-step paths. Every endpoint displacement `z` has precisely three nonzero signed coordinates, so

`\|z\|_1=3, \qquad L_E(z)^2=\sum_i z_i^2=3, \qquad z\ne0.`

Every one of the `160` endpoint vectors has precisely six such shortest path histories. Thus the endpoint is a genuine many-to-one readout of native ordered path provenance, independent of whether future operations happen to distinguish these six orders. If all six are relevant under a declared future operation, their exact branch/ordering repair requires `\lceil\log_2 6\rceil=3` bits; *no universal three-bit memory requirement follows from the mere existence of six path orders*. This is the same observer-scope discipline underlying R758 and R757.

The R758B spatial paths are **not** automatically V39 completed based loops, because their endpoints do not return. Their counted permutations must not be silently combined with R757's admitted V39 macro-loop schedule proof. In particular, a two-step native spatial return is not evidence of P000 primitive two-force balance.

## 4. Scientific meaning and constructive next interface

The theorem isolates a concrete failed identification and points to a coherent candidate-development direction:

`PRIMITIVE_FORCE_QUANTUM` may be typed as an **incident Port/Cell force relation**, with a separately admitted three-branch incidence certificate and an ordered BRC update, while `±e_i` remains the native *spatial* adjacency; any displacement is an additional event readout, not the definition of balance. A minimal project-consistent next **candidate** is a Cell-local typed ternary hyperedge `H_c(p,q,r)` with an explicit force-closure admission predicate, independent of coordinate walk return. Enforcing `S_6` covariance, branch provenance and a V29/V39 update remains a real proof/design task, not an already source-approved native event. Such a relation does not create a new spatial dimension or a native 2D plane, and can live over the frozen six-axis Cell torsor.

The existing X6 native torsor foundation already warns that carrier triangle return is not full native Cell return. This note adds a sharp force-dynamics rejection theorem for the *specific* `one force = one coordinate step, stability = path return` mapping, including its exact 2/3-step witnesses and complete finite classification. Do not treat it as a universally new theorem about all primitive three-force event models.

## 5. Exact reproducibility

Run `python3 research_notes/R758B_X6_ODD_STEP_FORCE_CLOSURE_VERIFY_20261113.py`. The standard-library script exhausts all 144 two-step and 1,728 three-step paths, plus 960 signed distinct-axis canonical triad orderings and 160 endpoint fibers, and writes `R758B_X6_ODD_STEP_FORCE_CLOSURE_EVIDENCE_20261113.json`. No random sampling or floating point is used. Exact parity proof applies to every odd length.

**Hard-target status:** Source-approved `TRIADIC_CLOSURE_E` incidence, actual V29 PASS/TRANSFER and V39 frame effects, larger population triad decomposition and appearance of two-force equilibrium remain open. Preserve immutable science pin, P000, ACTIVE worldview, author/CLAIM provenance and independent Driver review requirements.
