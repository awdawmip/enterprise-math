# CBRC F7 r492 — 171 independent mandatory repair sites for the fixed B30 witness at B31

Date: 2026-11-22 Asia/Taipei. Contributor: continuing established RESEARCH_DRIVER logical lane **EM-DVR-DEBB5E**, original own SID `MCP-9b4714dc46b948afa4875a86c89c713c`. Preserve the separate historical original F7 researcher `EM-CBRCF7-83A1D4`, frozen Result `RR-AA38973D56330E59D315`, authorship and Native Review status.

## Precise question and baseline

Keep the original F7 problem: \(q:\mathbb Z^2\to\mathbb R\), \(q(-x,y)=q(x,y)\), \(q(0,0)=0\), \(q(x,0)=1\) for \(x\ne0\), \(q(x,y)\ge\tfrac12\) when \(y\ne0\), and \(q(2,1)=q(-1,-1)=\tfrac12\). For integers \(a,b,c,d\), set
\[
k=a-2b-c+2d,\qquad D_q=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d),
\]
and \(E_B(q)=\max_{(a,b,c,d)\in[-B,B]^4\cap\mathbb Z^4}|D_q|\).

Fix **the particular globally defined r491 B30 witness** \(q_{30}\) from the [r491 exact theorem](https://github.com/awdawmip/enterprise-math/blob/9a0b3e7c673777e59a9b8efa13ad9c1ac48d5f65/research_notes/driver/2026-11-22_f7_r491_B30_exact_quarter_minimax.md) and its [immutable encoded values](https://github.com/awdawmip/enterprise-math/blob/004f12cbe85d0ac39a1ef92afac298bbda2b0611/research_artifacts/F7_R491_B30_Exact_Quarter_Witness_20261122.b85). All unlisted off-axis keys take \(q_{30}=1/2\); \(E_{30}(q_{30})=1/2\).

## Theorem r492 — exact, witness-specific necessary condition

Let \(U\) denote the **436 distinct free evenness-orbit keys** \(p=(|x|,y)\) occurring in the 171 explicit quadruples of the pinned certificate below, excluding \(y=0\) and the two fixed marked keys. For **every globally admissible real-valued** \(q'\) satisfying \(E_{31}(q')\le 1/2\),
\[
\boxed{\#\{p\in U:q'(p)\ne q_{30}(p)\}\ge171,\qquad
\sum_{p\in U}|q'(p)-q_{30}(p)|\ge47.}
\]
These count *evenness-orbit variables*, not individual signed \(x\) coordinates. No quarter-grid restriction is imposed on \(q'\).

### Short proof

Put \(Q=4q\). On each of the 171 chosen original inputs, \(|D_{Q_{30}}|=3\) (154 rows) or \(|D_{Q_{30}}|=4\) (17 rows). Write each shear equation as a linear combination of free orbit variables \(Q(p)\). Axis coordinates and the two marked values cancel in \(Q'-Q_{30}\) because they are fixed by the model. The 171 resulting nonempty supports \(S_i\subseteq U\) are pairwise disjoint; each nonzero coefficient is exactly \(+1\) or \(-1\).

For any \(E_{31}(q')\le1/2\), the corresponding \(|D_{Q'}|\le2\), so with \(\Delta Q=Q'-Q_{30}\),
\[
\sum_{p\in S_i}|\Delta Q(p)|
 \ge |D_{\Delta Q}| \ge |D_{Q_{30}}|-|D_{Q'}|
 \ge |D_{Q_{30}}|-2.
\]
Every \(S_i\) therefore contains at least one changed orbit variable. The disjointness implies at least 171 changed keys, and summing all rows gives
\[
\sum_{p\in U}|4(q'(p)-q_{30}(p))|
\ge154\cdot1+17\cdot2=188.
\]
Dividing by four proves the stated \(47\) bound.

The exact [171 original-input quadruples](../../research_artifacts/F7_R492_B31_171_Disjoint_Violation_Quadruples_20261122.json) and [Python integer verifier](../../research_checks/CBRC_F7_R492_B31_DISJOINT_REPAIR_BOUND_20261122.py) reconstruct the *actual* immutable r491 q witness, verify all row values, \(\pm1\) coefficients, pairwise disjoint supports, 436 unique variables and exact 154/17 counts. The verifier uses no LP solver, approximation or custom axiom.

## Additional complete B31 diagnostic for the unchanged q30

An independent local C++ original-quadruple enumeration covered the complete \(63^4=15,752,961\) input box for the unchanged \(q_{30}\), with exact \(4D_{q_{30}}\) histogram:

| Value | −4 | −3 | −2 | −1 | 0 | +1 | +2 | +3 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Count | 288 | 24,162 | 480,750 | 3,393,372 | 7,461,153 | 3,874,062 | 519,154 | 20 |

Exactly **24,470** B31 inputs of this specific function violate the half-error requirement. Changing only the 1,258 newly indexed B31 orbit keys leaves 23,944 violations of this same construction.

This establishes a quantitative modification obligation **relative to the specified r491 witness**, not \(e_{31}>1/2\) or any minimum possible repair count. The finite optimal values \(e_B=1/2\) for \(B\le30\) remain proved; **\(e_{31}\) and the infinite-box minimax remain open**, with the previously established global interval \([1/2,4/7]\).

## Scientific and control status

This is one new exact scientific subunit (**r492**), independently checkable from original arithmetic and a fixed certificate. It is not a Native Result admission, Task completion, independent author-blind F7 classification, or parent-Objective closure. Preserve original scientist/Result/Review lineage; the review input budget and frozen-manifest discrepancy remain tracked in [Issue #2874](https://github.com/awdawmip/enterprise-math/issues/2874). Next useful scientific discrimination: construct an exact B31 rational witness (fully validate original four-variable domain), or prove a strict B31 lower bound with a genuine dual infeasibility certificate; the 171 rows give a proven repair floor for the r491 extension.
