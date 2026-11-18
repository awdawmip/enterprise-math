# Discrete X6: connected point-action obstruction and observer-bridge boundary
Date: 2026-11-18. Task RS-DISC-COMPAT-20261026-01, publication TP2-E26E6CC48C96AD3D9227. Evidence: exact conditional mathematical proof; no empirical inference.

## Theorem (connected action on discrete points)
If a connected topological group G acts continuously on a discrete topological space D, then every element fixes every point of D.
Proof: For x in D the orbit map G->D, g|->g.x, is continuous. The image of a connected space is connected; every connected subset of a discrete space is a singleton. Since e.x=x, the image is {x}. QED.

Consequently, a *nontrivial continuous point-permutation* implementation of SO(3) or SO+(1,3) cannot act on the bare discrete X6 state carrier. This is conditional on the proposed action being continuous in the discrete topology on native points. It does not assume native 120-degree relations are ordinary Euclidean angles.

## Equivariant external vector-readout obstruction
Suppose f:D->R^3 is a nonzero external Euclidean vector readout and R_g is the standard SO(3) vector action. Requiring f(g.x)=R_g f(x) for all g forces f(x)=R_g f(x) for all rotations and hence f(x)=0, contradiction.

If the demand is approximate, the exact uniform defect E(x)=sup_{g in SO(3)} ||f(g.x)-R_g f(x)||_2 equals 2||f(x)||_2 under trivial point action. A half-turn orthogonal to f(x) gives equality; the triangle inequality gives the upper bound.

## Domain-specific applicability and viable next investigations
1. Continuous rotation/boost on native discrete **points**: theorem applies; nontrivial action excluded.
2. Action on non-discrete configurations, amplitudes or mixtures: this theorem does not apply; such a representation needs its own defined dynamics and operational readout.
3. Statistical invariance of a random discrete **ensemble** is not pointwise symmetry of each realized structure; a source-backed invariant law is required before claiming this route.
4. Laboratory apparatus rotation: must specify preparation kernel K_theta, native update U_t, instrument/readout M_theta, output-label action rho_g and a physical map from changing lab orientation to these objects. Then test P_(g.theta)(B)=P_theta(rho_g^(-1)B), with a resolution/energy-range and error budget.
5. Boost and signal causality: native time to measured clocks/lengths/velocities, plus permitted information-influence region for global/non-neighbor updates, are currently missing interfaces.
6. Bombelli-Henson-Sorkin no-preferred-direction result has hypotheses tied to a Lorentz-invariant Poisson causal-set ensemble; these have not been established for the fixed X6 native-axis carrier.

## Task return
EXCLUDED_WITHIN_SCOPE: exact nontrivial continuous point action of connected rotations/boosts on discrete native points.
THEOREM_NOT_APPLICABLE: configuration/amplitude/ensemble actions until declared.
MISSING_COMPONENT: lab orientation-to-native mapping, joint apparatus response, clock/length calibration and signal influence bound needed for physical predictions.

The parent task RS-DISC-COMPAT-20261026-00 has not yet frozen the common ModelCapsule/observer bridge. This note preserves the exact condition and gives the smallest next interface required, rather than assuming a physical prediction.

Sources: frozen taskbook research_tasks/RS-DISC-COMPAT-20261026-01.md (Git blob 4a30005eed4deb4c62f012218d3545efc9d6a547), publication TP2-E26E6CC48C96AD3D9227, account P000 startup (P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), earlier review research_notes/discrete_light_objections_20261026_9c8ddfc415e7.md (blob f009802adcb0d8b55f8e296598ca62f4a5eb8364).
