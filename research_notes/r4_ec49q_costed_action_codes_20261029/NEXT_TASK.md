# EC49R — Cost-neutral coding and padding for multistage positive-BRC observers

Status: AUTHOR-SIDE PROPOSED SUCCESSOR / UNREVIEWED / NOT_ADMITTED. This is a research question and handoff, NOT a native V2 Task/CLAIM publication.

## Highest verified frontier

Consume EC49P PR #1654 (27-atom-per-source model) and EC49Q from this PR. EC49Q establishes:
(1) K*m>=|W| action-memory coding cardinality is INSUFFICIENT for coupled raw (alpha,beta,E_PT,E_QT) preservation when action labels have different prices, even for clone observation kernels, strictly positive rational sources and arbitrary real fresh behavioral policies.
(2) Sharp one-stage separation sup_full H=1/8 > sup_compressed H=1/16 for H=alpha-beta-(E_PT+E_QT)/16.
(3) Sharp exact budget L frontiers F_full(C)=min(C/4,1/4), F_compressed(C)=C/4 (0<=C<=1/2), (C+1/2)/8 (1/2<=C<=3/2), 1/4 (C>=3/2).
(4) Source-wise equal-kernel, equal-cost clone action labels DO suffice when K*m>=|W| in the one-purchase protocol: an explicit causal compiler preserves all four coordinates, and rational targets admit rational fresh-behavioral controllers.
Executed evidence: VERIFY.py / EXACT_REPORT.json, Fraction pass; see PROOF.md and SOURCES.md.

## Next independently decidable problem

For two adaptive purchases or more, define a *cost-neutral action-code simulation* precisely: a causal coding of forgotten W into retained action labels and external memory such that source-conditioned joint observation kernels, all terminal acceptance decisions, and BOTH expected P/Q cost coordinates match. Classify a minimal resource-aware code criterion beyond K*m>=|W|.

First concrete challenge: W={0,1,2}, sensor labels A,B (identical conditional observation kernels), costs c_A=1,c_B=2, m=2 external memory states, two potential purchases and early stopping. Determine whether there exists a strictly positive rational two-source table and exact four-vector separation *despite* K*m>=3 and an unused fourth label. If yes, exhibit a complete P/Q joint table, all actions, memory update rules, exact rational separating linear functional, and finite exhaustive or analytic all-real certificate. If not, state and prove an explicit necessary/sufficient padding feasibility condition including equality of P/Q cost coordinates and early-stop routes. Extend via a dynamic occupancy LP that retains causal information and source coupling.

A sharper variant asks if the mere existence of a *cost-balanced randomized encoding* preserving two source expectations is equivalent to raw-region preservation, or if terminal policy-dependent correlations give a further obstruction. Try a counterexample with action-dependent conditional Z kernels but identical P/Q marginal spectra; distinguish kernel preserving, mass preserving and full multi-stage outcome preserving.

Do not silently treat a terminal observer's ability to decode W as an admissible zero-cost private memory. Keep exact action/observation sigma-algebras and cost/coin provenance. Preserve original EC49P and EC49Q inputs; never replace one with the other. Use real analytic dual certificates to justify claims for arbitrary real behavioral policies. Any fixed rational grid is diagnostic only.

## Native scientific bridge obligation

If mapping the result toward heartbeat/X6 or signed/phase BRC, supply an explicit typed provenance-and-port morphism, three-dimensional slice embedding/third coordinate where relevant, source-wise acceptance/cost observer, operation commutation and a separate finite/discrepancy certificate. Positive P/Q weights and derived P-Q difference are not native signed BRC amplitudes, and sensor cost is not heartbeat time. P000/ACTIVE worldview remain fixed. Formal Owner/CLAIM and independent Driver review require fresh native authority, not the existence of this PR.
