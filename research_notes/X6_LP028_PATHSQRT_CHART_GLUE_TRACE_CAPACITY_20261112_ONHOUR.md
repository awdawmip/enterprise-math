# LP028: R063 PathSqrt chart-gluing obstruction and exact consumer fiber capacity

Date: 2026-11-12. Status: AUTHOR_PROVED / EXECUTED_EXACT_CHECK / UNREVIEWED / NOT_ADMITTED.
Parent Task: RS-X6-LEGACY-PLANE-RECONCILIATION; publication TP2-B4A441B23DA3159232C2; Driver disposition REQUEST_REVISION.
Evidence only: not a CLAIM, native semantic checkpoint, review, change to frozen R063 or Task completion.

## 1. Actual downstream consumer and question

Historical source research_notes/TOOL_DISCOVERY_NATIVE_GEOMETRY_OF_NUMBERS_MINIMA_CALCULUS_RESULT_20260822.md (current Git blob e3b1488a9bfdc44795f5d0e78c67e8c128bd30dc, §10) uses the finite-fiber theorem for one fixed positive two-generator R063 chart:

\[
R_r=\{(a,b)\in\mathbb N_0^2:a^2+b^2=r^2\},\qquad
\operatorname{PathSqrt}_E(r^2)=\bigsqcup_{(a,b)\in R_r}\Lambda(a,b).
\]

For that fixed chart, the component-root quotient has \(|R_r|\) trace fibers; shortest path mass is \(P_r=\sum_{(a,b)\in R_r}\binom{a+b}{a}\). At \(r=50\), these are six fibers and 110695538274255714208 formal shortest paths. Preserve this historical result at its stated type.

Current X6 source definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md, blob e266c103cae02550c8bbaa794958f3423b41d151, uses Cell-anchored signed \(\mathbb Z^6\) coordinates. R061/R062 type a two-axis displacement as a composite signed primitive-step path. The 15 unordered X6 axis-pair charts overlap on the six axial directions.

Question resolved: whether the original six local root labels extend to a single chart-compatible global quotient and which capacities the current endpoint-sensitive consumer actually needs.

## 2. No chart-compatible six-root quotient (all d >= 3, r > 0)

Let \(\mathcal W^+_{d,r}\) be the union, **not a disjoint sum**, of positive primitive-axis shortest path words with squared component norm \(r^2\) and support at most two. Each pair chart \(i<j\) gives its local ordered component label \((a,b)\in R_r\).

**Theorem A.** For every \(d\ge3\) and integer \(r>0\), there is no function \(\pi:\mathcal W^+_{d,r}\to R_r\) whose restriction to *every* pair chart is its local ordered component-root map.

**Proof.** Choose an interior axis \(1<k<d\) (one-based indexing). The single word with \(r\) copies of \(+e_k\) lies in both charts \((i,k)\), \(i<k\), and \((k,j)\), \(k<j\). Those charts label the same word respectively \((0,r)\) and \((r,0)\). Since \(r>0\), these are distinct. A global function cannot take both values on the same word. QED.

Minimal witness: \(d=3,r=5\), word \((+e_2)^5\). Chart (1,2) calls its root (0,5); chart (2,3) calls it (5,0). This is a **shared-axis chart-name conflict**, not a failure of the historical R063 arithmetic.

## 3. Precise repair: two globally defined finite-fiber maps

Let \(\mathcal W^\pm_{d,r}\) denote the union of shortest signed-axis words with support at most two and squared norm \(r^2\). Count an identical word once when it occurs in several charts; only support-one words overlap.

Define two chart-independent maps:

\[
\pi_{\rm end}(w)=d(w)\in U^\pm_{d,r}, \qquad
\pi_{\rm abs}(w)=(|d_1(w)|,\ldots,|d_d(w)|)\in U^+_{d,r}.
\]

Here \(U^\pm\) comprises signed endpoints with support at most two, and \(U^+\) their nonnegative absolute coordinate vectors. Put \(C=\binom d2\), \(m_r=|R_r|\), \(P_r=\sum_{(a,b)\in R_r}\binom{a+b}{a}\).

**Theorem B (all d >= 2 and positive integer r).**

\[
\boxed{\kappa_{\rm end}=2d+4C(m_r-2)},\qquad
\boxed{\kappa_{\rm abs}=d+C(m_r-2)}.
\]

Total signed and positive shortest-path-word masses are respectively

\[
\boxed{M_{\pm}=2d+4C(P_r-2)},\qquad
\boxed{M_+=d+C(P_r-2)}.
\]

For the finite-fiber collision-forest rank of the *actual path-word population*, the exact results are

\[
\delta_{\rm end}=M_{\pm}-\kappa_{\rm end},\qquad
\delta_{\rm abs}=M_{\pm}-\kappa_{\rm abs}.
\]

**Proof.** A support-two endpoint has unique pair axes. Every nonaxial ordered positive root produces one nonnegative endpoint, four signed endpoints and \(\binom{a+b}{a}\) shortest words per signed endpoint. An axial endpoint is one of \(d\) nonnegative or \(2d\) signed endpoints, each with a single pure-axis word counted once even though present in \(d-1\) charts. Partitioning by support gives all formulas. The downstream finite-fiber identity \(\delta=|X|-|\pi(X)|\) applies to distinct formal shortest words and either total map. QED.

**Consumer predicate boundary.** One representative per \(\pi_{\rm end}\) fiber suffices for endpoint-only predicates. One per \(\pi_{\rm abs}\) fiber suffices when the downstream predicate truly factors through componentwise absolute value. A signed future unit-step norm \(G(z+e_i)=r^2+1+2z_i\) distinguishes signed points \(z_i=\pm a\) when \(a>0\), so it uses signed-endpoint or finer data. Order/provenance-sensitive predicates retain the richer path-word trace. These are actual operation-dependent quotient conditions.

## 4. R063 N=2500 consumer certificate

For six axes, radius 50, 15 unordered pair charts and roots (0,50), (14,48), (30,40), (40,30), (48,14), (50,0):

| Typed population / statistic | Exact value |
| --- | ---: |
| Original *single positive pair* root capacity | 6 |
| All-pair nonnegative / absolute endpoint capacity | **66** |
| All-pair signed endpoint capacity | **252** |
| All-pair positive shortest path mass | 1660433074113835713096 |
| All-pair signed shortest path mass | 6641732296455342852372 |
| Signed endpoint collision forest rank | **6641732296455342852120** |
| Signed absolute-endpoint collision forest rank | **6641732296455342852306** |
| Positive axial points with conflicting chart labels | **4** |

The conflicting endpoints are \(50e_2,50e_3,50e_4,50e_5\); axes 1 and 6 have multiple chart incidences with a consistent local root order. Full signed six-axis support-one/two endpoints total 252, matching the separately verified full \(G=2500\) support-stratum census; the 102539052 full-shell total also has support-three through six states and remains unchanged.

## 5. Verification and precise downstream patch target

Checker: research_checks/X6_LP028_PATHSQRT_CHART_GLUE_TRACE_CAPACITY_20261112_ONHOUR.py. Executed under Python 3 with only exact integer math and standard library: **PASS 640 dimension/radius combinations** for \(d=2,\ldots,6\), \(r=1,\ldots,128\), each tested in positive and signed modes (1280 mode-specific cases). It constructs labelled chart endpoint dictionaries, identifies shared axial words, checks both capacities and path masses, checks absolute quotient cardinality, and verifies every asserted chart conflict. The \(d=6,r=50\) anchor and \(d=3,r=5\) witness have dedicated assertions. Computation does not enumerate the astronomically many individual path words: it uses the exact multinomial word-mass formula. The originally executed checker byte SHA256 is be7fa4ebf703165fe292e95b92715ba7675c0e882b61e0c4431de1cb75f15e75; a published Git blob and scoped remote readback are separately required.

Targeted consumer addition: append a **typed X6 all-chart adapter** to the historical tool-discovery result's §10 successor/use site, retaining the fixed-positive-chart six-fiber statement; select the absolute endpoint, signed endpoint, or full word trace according to each actual consuming operation. Link R063 §6 origin-incidence type and current R061/R062 signed Cell path semantics. Do not rewrite the previously accepted historical proof or claim an automatic current-world lift.

Next mother-task unit: complete the 28-LP source-location/type/consumer/action ledger, especially LP011 and LP019 original caller provenance, and verify actual remaining consumers. Existing exact typed continuation support issue https://github.com/awdawmip/enterprise-math/issues/2141 is still OPEN at this observation. Research lane original request onhour-research-20261112-0422-x6-continuation-v1 succeeded as a read; no current winning X6 CLAIM/open was verified, so the present GitHub note is research evidence, not a native semantic checkpoint.

Frozen science pin: 59538f585d037d09ef687b28715c4bc1a3f9fe03. Historical comparison pin: fd2bcff10ca6e147348b6c1236027fc0d2877df3. Current normative rules are read separately and do not rewrite those pins.
