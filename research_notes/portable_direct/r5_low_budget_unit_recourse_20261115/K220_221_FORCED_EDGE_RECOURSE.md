# R5 recourse: forced newly admissible optimal edges at K=220 and K=221

Date: 2026-11-15. Status: AUTHOR-PROVED / EXACT FINITE COMPUTATION / NOT_REVIEWED. Frozen scientific input: 435e77af0d180eac32bd1f9c4c464bc4010b7551.

## Question

For the 954-event derived integer one-dimensional radius-two indexed-center model, let Opt_B(K) be the entire optimal K-center family under closure mask B. Continue the prior exact recourse lower bounds at K=214 by concentrating on the low-budget edge cases K=220 and 221, where uniform sampling of globally optimal new paths can miss the rare optimizer changes.

For a singleton cut i, directed worst-nearest recourse is

\[
R_i(K)=\max_{S\in Opt_{\{i\}}(K)}
        \min_{T\in Opt_{\varnothing}(K)}|S\setminus T|.
\]

This notation here fixes the other 27 cuts open. The all-background version maximizes over B separately.

## Forced-new-edge lemma

Suppose closing one isolated internal gap leaves the optimal value J(K) unchanged and, as established for this frozen observer, any fixed center set feasible in both configurations retains its exact total nearest-center distance. Then every *new-only* optimal indexed-center set S contains an adjacent-center edge that is admissible after closure but inadmissible before closure, provided the boundary prefix and suffix admissibility sets are unchanged. This boundary condition holds for the present cut indices 3,8,9,10.

Proof: If S remained feasible in the old model, cost invariance would give old cost J(K), so it would already belong to the old optimizer family. A new-only S is therefore old-infeasible. The radius-two coverage decomposition assigns any infeasibility either to a prefix, suffix or consecutive-selected-center interval. Its prefix/suffix feasibility is unchanged here, so at least one selected-center interval must be newly admissible. Conversely any new-optimal path containing a newly admissible edge is old-infeasible and hence new-only. This exactly characterizes the new-only optimal path family by a union of changed-edge-constrained optimal paths.

To construct these paths, identify every new-only directed edge i→j on an exactly optimal dynamic-programming path at layer t using

\[
C_{t-1}(i)+w_{ij}=C_t(j),\qquad
C_t(j)+D_{K-t-1}(j)=J(K).
\]

Fix one such edge, then backtrack the optimal prefix and forward-track an optimal suffix; the result is a globally optimal new path. To certify its *nearest old optimum*, run the prior exact integer max-overlap DP over **all old optimal paths**, then compute K minus maximum shared-center count.

## Exact new lower-bound witnesses

One guaranteed newly optimal but originally infeasible center set is reconstructed for every cut and each budget below:

| K | Cut (zero-based) | Cut event index | Min replacements of this S to all old optima (exact) | Number of changed optimal edge-layer states |
|---:|---:|---:|---:|---:|
| 220 | 3 | 46 | 3 | 1 |
| 221 | 3 | 46 | 3 | 1 |
| 220 | 8 | 110 | 5 | 2 |
| 221 | 8 | 110 | 5 | 1 |
| 220 | 9 | 116 | 5 | 2 |
| 221 | 9 | 116 | 5 | 1 |
| 220 | 10 | 123 | 4 | 2 |
| 221 | 10 | 123 | 3 | 1 |

Thus for these original-to-singleton closures, the directed maximum R is at least each listed value. The far-from-cut ripple previously detected at K=214 continues in the restricted K=220/221 model at a certified five-center distance for cuts 8 and 9.

For the finite computation, the supplied standard-library Python program runs with the earlier verified source VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE.py in this directory. It asserts equality of old/new global optimal costs, validates complete 954-event radius and total cost for each selected new path, asserts old infeasibility, and performs an exact minimum over the entire old optimum family by maximizing center overlap. Each selected witness is a full K-element indexed-center set in the deterministic full JSON output.

Run:

    python VERIFY_R5_K220_221_FORCED_EDGE.py > exact_forced_edges.json

Expected status: PASS_EXACT_R5_FORBIDDEN_EDGE_K220_221. The actual locally executed equivalent-module program returned this status; the 8 full-witness output bytes have SHA-256 eed62d56067bec5d1915e4b3dac9a2043791097be511014bf86243cd46708384. The compact JSON summary in the same folder lists all 8 results, edge identities and scope. Independent mathematical review remains pending.

## Open continuation

For K=214..221 and the five relevant variables (3,8,9,10,27), combine changed-edge-constrained new optimal paths with the global old-optimal overlap automaton to compute **max over every new-optimum** of **min over old-optimum** exactly, including other closure contexts. The present table supplies verified finite lower bounds and a changed-edge enumeration route, not an upper bound or equality for R.
