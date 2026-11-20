# X6 Unit176 — A3→A4 容量加权粗支持的精确残差纤维

- Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`, parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`
- Frozen scientific input: `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical source comparison: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`
- Original researcher/session: `EM-X6-FB6990` / `MCP-082892eb480e45dea6d4b9fcc0491034`
- State: `AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`. Typed *derived* A3/A4 relation-observer, not a new primitive X6 axis or physical law.

## Actual frozen producer–consumer evidence

At the historical pin, `src/enterprise_math/weighted_relation_field.py` (blob `e50bf991e4dc4280063556a7aad1028f9f9404ed`) implements `Z_ij=m_j*c_i-m_i*c_j` and coarse cross-field summation. `src/enterprise_math/a3_a4_support_bridge.py` (blob `ee66d0f6d9846171ff732204d5337fb3c0087d75`, actual production import lines 29–35 and cross-pair predicates lines 155–201) consumes the former. Its genuine test consumer `tests/test_a3_a4_support_bridge.py` (blob `dd0c64af456c26ddfb51e4e0c7b74c9314c44728`, lines 52–61) already covers the one-way implication and an isolated cancellation counterexample. The new mathematical increment is the exact two-sided residual criterion, a fixed-coarse-data arbitrarily large counterfamily, and exhaustive mixed-capacity integer checking. This is a new typed consumer audit and strengthening, not a duplicate of the historical one-way claim.

## Exact theorem

Fix disjoint nonempty index groups `U,V`, arbitrary integer totals `c_i`, positive integer capacities `m_i`, and `Z_ij=m_j c_i-m_i c_j`. Define `M_U=Σ_U m_i`, `C_U=Σ_U c_i` (similarly V). For each cross-pair let

\[
\delta_{ij}=\frac{Z_{ij}}{m_i m_j},\qquad
w_{ij}=\frac{m_i m_j}{M_U M_V},\qquad
\mu=\frac{C_U}{M_U}-\frac{C_V}{M_V}.
\]

The positive rational weights sum to one, and
\[
\mu=\frac{\sum_{i\in U,j\in V}Z_{ij}}{M_U M_V}
=\sum_{i\in U,j\in V}w_{ij}\delta_{ij}.
\]

Let \(\alpha=\max_{i\in U,j\in V}(\delta_{ij}-\mu)\ge0\) and \(\beta=\max_{i\in U,j\in V}(\mu-\delta_{ij})\ge0\). Then **for every integer radius** \(r\ge0\), the exact production predicates satisfy

\[
\boxed{\text{coarse supported}\iff |\mu|\le r},\qquad
\boxed{\text{all fine cross-pairs supported}\iff -r+\beta\le\mu\le r-\alpha}.
\]

**Proof.** Expanding each relation and summing gives \(\sum Z_{ij}=M_V C_U-M_U C_V\), proving the weighted-mean identity. The mean is a convex combination of all cross-pair normalized relations, so it lies between their minimum and maximum. By definition their exact extrema are \(\mu-\beta\) and \(\mu+\alpha\). The implemented coarse predicate is \(|\sum Z_{ij}|\le rM_UM_V\), equivalently \(|\mu|\le r\). The implemented all-fine predicate is \(|Z_{ij}|\le rm_im_j\) for each pair, equivalently all \(\delta_{ij}\in[-r,r]\), equivalently the displayed interval bounds. All equalities are rational/integer exact. ∎

The oriented repair carrier \((\mu,\alpha,\beta)\) therefore suffices to answer every all-fine radius query after aggregation. Minimal encoding size is not claimed.

## Arbitrarily large hidden defect with identical *entire* coarse state

For every integer radius \(r\ge0\) put \(t=r+1\), capacities \(m=(1,1,1,1)\), fine totals \(c=(t,-t,0,0)\), and partition \(U=\{0,1\}, V=\{2,3\}\). Both coarse capacities equal 2, both coarse totals equal 0, and the coarse relation equals 0 for every t. Yet

\[
(Z_{ij})_{U\times V}=\begin{pmatrix}t&t\\-t&-t\end{pmatrix},
\qquad \mu=0,\quad \alpha=\beta=t>r.
\]

Thus the coarse predicate is true and the all-fine predicate false. Compare with the zero fine totals, which produce **identical coarse capacities, totals and field** but satisfy all-fine support. As t grows, the lost relation extrema grow without bound. The cancellation takes place in signed derived A3 relation entries; it is *not* cancellation of positive native N-BRC path mass.

## Independent computation

The separate exact-`Fraction` checker enumerated all \(m\in\{1,2,3\}^4\), \(c\in\{-2,-1,0,1,2\}^4\), \(r\in\{0,1,2,3\}\), with fixed U,V: **50,625 integer states and 202,500 radius tests**. It compared integer producer formulas, the independent rational weighted mean, and exact extrema: **0 violations**. Fine support appeared in 97,452 cases; coarse support in 145,416; 47,964 cases passed coarse support but failed fine support. The parametric counterfamily passed for r=0,…,11. Normal, `-O` and `-OO` modes yielded the same results (SHA-256 `273d543b0f9ce45fe3443f22daa462a3de12562d7a6c080e902eacfed0512332`). The universal conclusion relies on the proof rather than the finite check.

The independent checker executes formulas explicitly and does not import the entire historical repository. The earlier native R063 benchmark (17/17; 512/512) was not rerun. In this inspected chain, LP011's alleged invalid native argmax and LP019's alleged positive native N-BRC subtraction are **not established as offending source lines**; their exact `commit:path:line` remains unresolved.

## Next research obligations

Continue the frozen 28-LP consumer crosswalk, prioritizing uninspected genuine production import/call sites and exact LP011/LP019 provenance. Independently preserve/associate Units149–152 native history; submit native semantic linkage for Unit175 and Unit176 only under current own winning CLAIM/RUN authorization and after consuming all previous original receipts. Driver review and admission remain separate.
