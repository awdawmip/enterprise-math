# Heartbeat multi-tick residual memory checkpoint

Event-ID: brc-heartbeat-multitick-20260920-6EF011
Status: RESEARCH_CANDIDATE / NOT ADMITTED

Continues the residual-first Heartbeat program from the autonomous-controller checkpoint. A controller C repeatedly contacts fresh environment units B while preserving the full S-C joint state between contacts.

For a partial-SWAP contact with c^2+s^2=1 and fresh bath state tau, the retained correlation operator Xi=Omega_SC-rho_C tensor rho_S obeys
Xi' = c^2 Xi + i c s [Xi, tau tensor I].
Thus imperfect reset changes both magnitude and phase; replacing it by scalar damping generally loses future-relevant information.

For initially fresh bath units, lost local S:C mutual information is transferred into environment correlation. Reusing the same environment can restore correlations while replacing it by a fresh environment need not; therefore local equality is not a sufficient future-state descriptor when discarded units may return.

A 32-contact finite experiment retained S-C correlations rather than re-factorizing after each beat. The final target marginal differs from the forced-product approximation by trace distance about 0.0521991. Energy bookkeeping includes bath heat and switching work: Q_B≈0.1613419143, W_switch≈0.0698471099, Delta E_SC≈-0.0914948044, satisfying Delta E_SC+Q_B=W_switch within the certified numerical budget.

If Omega_0 >= lambda_0 I and fresh bath j has least eigenvalue mu_j, the declared partial-reset channel preserves the explicit lower spectral factor
lambda_n=lambda_0 product_j(c_j^2+s_j^2 d_C mu_j).
For the frozen example this is lambda_n=(1/120)(17/25)^n and gives a strictly positive finite-n excitation lower bound. This is a conditional finite-resource result, not universal zero-temperature nonexistence.

A naive continuous-time deletion of the coherent commutator is invalid in general because its one-step size can scale as sqrt(dt), producing a derivative-scale term O(1/sqrt(dt)). Any continuous limit must specify cancellation, compensation, commutation, stochasticization, or another justified scaling.

Validation: 216 explicit-environment rational checks, 216 correlation-recursion checks, 18 high-order propagation checks, plus energy/entropy/memory and finite-window tests. Same-author evidence only; no Lean or independent review. The cumulative standalone bundle is BRC_Heartbeat_multitick_20260920.bundle, SHA-256 173f4a43a137962d501bcf9e4f325beec3a1aa6d1bd5b218bea50f7b40fc0064. This note records the research frontier; persistence is not theorem admission.
