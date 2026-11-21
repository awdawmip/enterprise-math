# X6 Native Time / Unit238 — exact signed wedge BRC observer and sharp aggregate-fiber theorem

Date: 2026-11-21 (Asia/Hong_Kong); status **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.
Mother objective: PO-X6-UPPER-STRUCTURE-20260906. Task: RS-X6-NATIVE-TIME-DYNAMICS / TP2-91D4A7C2F63805BE21A3.
Research provenance: logical lane \`chatgpt-research-onhour-enterprise-math-20260923\`; registered Researcher EM-X6-FB6990; original session \`MCP-082892eb480e45dea6d4b9fcc0491034\`. This is **not** the maintenance lane.

Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`, especially:
- \`p000_reality_foundation.json\`, \`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md\`;
- \`definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json\`;
- \`research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md\`;
- \`research_notes/VIETE_NATIVE_HALF_TURN_PRINCIPAL_ROOT_BUNDLE_20260905.md\`.
Consumes already saved and unreviewed Unit236 (bidirectional 36-state possible graph) and Unit237 (all \`2^(6W+1)\` histories share the full signed-step histogram). Does not redo their certificates or claim physical branch admissibility.

## Research question and actual advance

Unit237's midpoint-radius branch bit uses the chosen pivot Cell and the intermediate Cell. Determine whether a **translation-invariant, signed, chronological joint two-event observable** can distinguish INNER versus OUTER without choosing an absolute spatial origin, and exactly what information remains if that joint observable is only aggregated over a full loop. This is a concrete proposed typed Link/Port readout interface, not a claim that an actual native physical Port already measures it.

We work in the *full* P000 signed six-axis coordinate torsor; the example uses a declared centered three-axis sub-torsor with the other three *known zero relative components*, not a global reduction of native space. The formal exterior square \`Λ² Z^6\` is an **observer algebra of joint ordered increments**. Its 15 integer coefficients are neither 15 extra spatial axes nor a replacement for the native 120-degree Enterprise perpendicular relation.

Let
\[
a_0=e_1,\ a_1=e_2,\ a_2=e_3,\ a_3=-e_1,\ a_4=-e_2,\ a_5=-e_3,\quad a_{r+6}=a_r.
\]
For chirality \(\varepsilon\in\{+1,-1\}\), set \(a=a_r\), \(b=a_{r+\varepsilon}\), with the actual two primitive signed step increments:
\[
\begin{array}{c|c|c}
\text{branch}&(s_1,s_2)&\text{intermediate Cell relative to chosen pivot}\\
\mathrm{INNER}&(-a,b)&0\\
\mathrm{OUTER}&(b,-a)&a+b.
\end{array}
\]

## Theorem A — exact pivot-free, time-odd one-bit repair

Define the joint observer on **ordered** native steps by the alternating integer bivector
\[
\mathcal{J}(s_1,s_2)=s_1\wedge s_2
\in\Lambda^2\mathbf{Z}^6,
\qquad
\mathcal{J}_{ij}=s_{1,i}s_{2,j}-s_{1,j}s_{2,i}.
\]
Then
\[
\boxed{\mathcal{J}_{\rm INNER}=-a\wedge b,\qquad
\mathcal{J}_{\rm OUTER}=+a\wedge b.}
\]
Because \(a,b\) occupy different native coordinate axes, \(a\wedge b\neq0\) and indeed has one coefficient \(\pm1\). Thus **one signed bit relative to the known oriented macro-edge** separates the two paths, without reading the pivot or inserting another spatial coordinate.

The observer is invariant under a common translation of all Cells and equivariant under every positive-axis permutation \(P\in S_6\):
\(\mathcal{J}(Ps_1,Ps_2)=\Lambda^2P\,\mathcal{J}(s_1,s_2)\).
It is time-odd under physical reversal of the same primitive path:
\[
(s_1,s_2)\mapsto(-s_2,-s_1)
\quad\Longrightarrow\quad
\mathcal{J}\mapsto-\mathcal{J}.
\]
By contrast, unordered pair statistics, signed-axis counts, the event sum and unsigned bivector magnitude are equal for the two alternatives. **Signed chronological coupling is the decisive coordinate**, not a positive mass or a scalar norm. This is an observer algebraic identity; no physical device/Port readout or update law is assumed.

## Theorem B — the exact aggregate collision distribution for all W

Fix a start Cell \(a_0\). Consider \(W\ge1\) full six-edge circuits in each of the two fixed chiralities, with an independent INNER/OUTER choice on every macro-edge. The population contains \(2^{6W+1}\) distinct ordered native Cell histories. For one history define its single aggregated joint readout:
\[
\Omega=\sum_{t=0}^{6W-1}\mathcal{J}(s_{2t+1},s_{2t+2})
\in\Lambda^2\mathbf Z^6.
\]
This is **one final total** and not the ordered stream of local bivectors.

Set \(E_{12}=e_1\wedge e_2\), \(E_{23}=e_2\wedge e_3\), \(E_{13}=e_1\wedge e_3\). For \(\varepsilon=+1\), the six underlying \(a_r\wedge a_{r+1}\) form two copies of each of these three basis bivectors. For \(\varepsilon=-1\), they form their negatives. In \(W\) circuits there are exactly \(2W\) occurrences of each basis type.

Let \(k_i\in\{0,\ldots,2W\}\) count OUTER choices in the \(2W\) occurrences of type \(i\), for a fixed positive chirality. Then
\[
\boxed{
\Omega=\sum_{i\in\{12,23,13\}}(2k_i-2W)E_i
\quad(\varepsilon=+1),
}
\]
with the global negative of this expression for negative chirality using that chirality's own counts. Consequently the observer image consists of **exactly \((2W+1)^3\)** distinct bivectors, and for every observed \(c=(c_{12},c_{23},c_{13})\) with each \(c_i\in\{-2W,-2W+2,\ldots,2W\}\), its complete two-chirality fiber is
\[
\boxed{
|\Omega^{-1}(c)|
=2\prod_{i\in\{12,23,13\}}
{2W\choose W+c_i/2}.
}
\]
The factor of 2 counts the two chiralities; for the negative chirality the requisite OUTER count is \(W-c_i/2\), and binomial symmetry makes its multiplicity equal. No arbitrary probability weighting is used.

The maximum fiber size, reached at \(c=(0,0,0)\), is
\[
\boxed{F_{\max}(W)=2{2W\choose W}^{3}}.
\]
For a decoder *already supplied* with \(W\), the starting Cell and the aggregate \(\Omega\), the **sharp number of additional uniform fixed-length bits** that identifies every complete ordered native history is
\[
\boxed{B_{\rm residual}(W)=\left\lceil\log_2\bigl(2{2W\choose W}^3\bigr)\right\rceil.}
\]
Lower bound: a largest fiber has \(F_{\max}\) members. Upper bound: within each observed fiber enumerate the histories canonically in lexicographic order, encode the index, and reuse the same \(B_{\rm residual}\)-bit field for all fibers. This is an exact scope-typed observer descent/repair certificate; it does not license discarding provenance for another future observer.

By the central binomial coefficient asymptotic,
\(B_{\rm residual}(W)=6W-\frac32\log_2 W+O(1)\).
So an **aggregate** two-event joint observable recovers only logarithmically many bits of the missing chronological BRC history, whereas preserving each *ordered local* \(\mathcal{J}\) with its macro-edge location recovers all \(6W\) branch bits. For a fixed known chirality the aggregate fiber is half the displayed count.

## Executed exact source-possible native certificate

- Checker: \`research_checks/X6_TIME_BRC_SIGNED_WEDGE_OBSERVER_CHECK_20261121_1700.js\` at \`e345f9fc5280ae4f4e25f61c7ea12f55ec2d1912\`, Git blob \`3c53724d918f5c6442597976d96ac94ec13afedf\`.
- JSON certificate: \`research_checks/X6_TIME_BRC_SIGNED_WEDGE_OBSERVER_RESULTS_20261121_1700.json\` at \`fe7308eedb9be2906cc7b19838438cfbbc0bc3ae\`, Git blob \`632e0d77f3eec32a7a48e5422d11d1885ef3952c\`.
- Actually executed JavaScript checker in V8: **43,547,952 exact integer assertions, 0 failures**; **19,072,512 individual primitive event instances** traversed, 24 reverse-path local cases, all 17,280 \`S6\` covariance cases; exhaustive entire path populations for \(W=1,2,3\).

| W | Complete ordered histories | Distinct \(\Omega\) | Maximum fiber | Sharp extra bits |
|---|---:|---:|---:|---:|
| 1 | 128 | 27 | 16 | 4 |
| 2 | 8192 | 125 | 432 | 9 |
| 3 | 524288 | 343 | 16000 | 14 |

For \`W<=2\`, the checker also checked distinct complete chronological Cell trace strings; for \`W=3\`, symbolic injectivity and the exact fiber census cover multiplicity. All integer arithmetic is exact for these tested sizes. The general-W statement is symbolically proved, not inferred from this sample.

## Parent objective and the next discriminating native experiment

This gives an executable **candidate Link/Port joint-observation interface**: at a known oriented macro-edge, retrieve the two actual signed primitive event increments in order and compute the alternating integer bivector. The *physical* evidence still required is a Source-qualified native transition/Port definition that (i) actually emits or consumes that ordered pair or an equivalent time-antisymmetric relation; (ii) specifies which INNER/OUTER alternatives are reachable; (iii) preserves any triadic closure/state dependencies; and (iv) supplies full-source normalizations to compare before/after the loop, including whether a C12/C24 precision-fiber state is actually observable.

The frozen Viète half-turn \(\Sigma=\pm3\) is a static OUTER-qualified principal-root **selection**, not the value of \(\Omega\) or a demonstrated precision-fiber time increment. The frozen R063 six-file native benchmark stays entirely with the distinct \`RS-X6-LEGACY-PLANE-RECONCILIATION\` task / Issue #2416; none of the assertions here fulfills that benchmark.

**Control debt preserved separately:** last Source-backed own researcher SID above. Original protected request \`onhour-20261121-1502-own-time-units233-235-native-progress-v1\` is terminal \`FAILED / no current winning live CLAIM\`. Original same-session typed continuation attempts \`onhour-20261121-1627-own-x6-time-typed-continuation-after-expired-claim-v1\` and \`onhour-20261121-1640-own-x6-time-typed-continuation-compact-repair-v1\` are terminal \`FAILED / NATIVE_INPUT_SCOPE_METADATA_BUDGET_EXCEEDED\`; engineering support Issue #2903 is open. Own new Source continuation read \`onhour-20261121-1700-x6-own-current-continuation-read-v1\` was last seen RUNNING and must be consumed by its original ID. No new native CLAIM, RUN, protected semantic PROGRESS, physical Port law, independent Driver admission or task completion is asserted. This new note and exact certificate are independent GitHub science sources, subject to subsequent Activity CAS and lawful Native association.
