# X6 LP026/LP028 — native discrete Voronoi comparator and exact bisector ties

Date: 2026-11-15 03:00 +08:00. Mother task RS-X6-LEGACY-PLANE-RECONCILIATION, publication TP2-B4A441B23DA3159232C2. Source author EM-X6-FB6990, own SID MCP-082892eb480e45dea6d4b9fcc0491034; original claim MCP-30a8f5fd123215e08bd4a7cf and RUN-3356cbe3c2b4916d79399941. These identifiers record provenance, not independent review. **AUTHOR-PROVED / EXECUTED EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED**.

## Frozen source scope

P000 V5 and the signed Cell torsor are frozen at enterprise-math commit 59538f585d037d09ef687b28715c4bc1a3f9fe03. The latter's native definition (definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md, blob b4d49a1bbcccad0521618c6d20f6dcfa242b420a, lines 71–103) expressly gives a native six-component square metric on **all** integer Cell displacements. Historical comparator input is frozen at fd2bcff10ca6e147348b6c1236027fc0d2877df3.

The August 23 historical report research_notes/TOOL_DISCOVERY_CARRIER_VORONOI_DELAUNAY_DUAL_CELL_RESULT_20260823.md, old/current blob f02124cce925bc181821f9429c87364c8652ffd5, §9.2 lines 300–303, said the **then-current** Foundation lacked an arbitrary cross-sector native metric. Its original experimental Python code scripts/tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py, blob 900e246b0dafaa35d2452191e3df508a2d15a389, lines 1–11 and 42–78, explicitly computes 2D rational Euclidean **carrier** distance, checking the semantic layer. Its August hard-target disposition concerns that older input and remains historical; no Foundation or frozen Result is changed here.

## Theorem A: a well-typed current native finite-site comparator

Let S be a nonempty finite set of *actual native Cell site coordinates* in a common chosen-Cell chart \(\mathbb Z^6\). Define for each Cell query \(x\in\mathbb Z^6\)

\[
D_s(x)=\sum_{i=1}^6 (x_i-s_i)^2,\qquad
N_S(x)=\{s\in S:D_s(x)=\min_{t\in S}D_t(x)\}.
\]

Then \(N_S(x)\) is an exact nonempty, possibly multi-valued native nearest-site set. It is invariant under common integer translation, signed six-axis coordinate permutations and a change of chosen Cell anchor that translates all coordinates together.

**Proof.** The minimum of a finite nonempty set of integer scores exists; simultaneous translation leaves coordinate differences unchanged; signed permutation preserves the sum of six squares. None of these operations passes through a min-zero quotient or a carrier Euclidean embedding. \(\square\)

## Theorem B: necessary and sufficient integer-native two-site tie criterion

For two distinct native Cell sites \(s,t\in\mathbb Z^6\), put \(v=t-s\ne0\), \(g=\gcd(|v_1|,\ldots,|v_6|)>0\), and \(h=G(t)-G(s)\), with \(G(z)=\sum_i z_i^2\).

An integer native Cell query \(x\in\mathbb Z^6\) lies on the two-site equidistance stratum **iff** \(2x\cdot v=h\). Such a native query exists **iff**
\[
\boxed{2g\mid h}.
\]

**Proof.** The exact identity \(D_s(x)-D_t(x)=2x\cdot(t-s)+G(s)-G(t)\) reduces equality to \(x\cdot v=h/2\). Every integer dot product \(x\cdot v\) is divisible by \(g\), establishing necessity. Bézout yields an integer vector \(u\) with \(u\cdot v=g\). When \(2g\mid h\), \(x=(h/(2g))u\) is an explicit native tie point. \(\square\)

Consequently a real Euclidean hyperplane bisector need not contain any discrete native Cell. For \(s=0,t=e_1\), \(g=1,h=1\), hence no integer tie. For \(s=0,t=2e_1\), \(g=2,h=4\), ties have \(x_1=1\). For \(s=0,t=e_1+e_2\), \(g=1,h=2\), ties have \(x_1+x_2=1\). Each statement holds on the **entire** \(\mathbb Z^6\).

## Actually executed exact certificate

The authored Python checker research_checks/X6_NATIVE_DISCRETE_VORONOI_TIE_CHECK_20261115_0300.py was executed on all \(5^6=15{,}625\) signed-native query Cells in \([-2,2]^6\) for all three site pairs: 46,875 exact pair comparisons, verifying both the sum-of-squares and expanded integer bisector expression for each comparison. Its original executable bytes SHA256 are 79bf61d9bdba0dab523ad13082e15105887048e7c50f09b284952223f5ed5a91; Git blob f494d5ffbf71991a10736fca1b43ae5c2e70c8b3 matched exact GitHub readback at commit dba8eed3b25b2001c9b1357c292d85acf3147efd.

| Sites | g,h | Closer to first | Closer to second | Exact ties |
|---|---|---:|---:|---:|
| 0,e1 | 1,1 | 9375 | 6250 | 0 |
| 0,2e1 | 2,4 | 9375 | 3125 | 3125 |
| 0,e1+e2 | 1,2 | 9375 | 3750 | 2500 |

Actual output ends PASS_X6_NATIVE_DISCRETE_VORONOI_INTEGER_TIE_20261115_0300. This is a bounded program certificate; the all-integer equivalence above follows from the separate Bézout proof.

## Type disposition and next source action

**PRESERVE_CARRIER:** original August 2026 rational Euclidean carrier Voronoi/Delaunay theorems, terminal tool decision and frozen evidence, with their dated older scope. **PRESERVE_NATIVE / NEW_TYPED_COMPARATOR:** current signed P000 V5 Cell metric permits a distinct exact finite-site native nearest-site operation. Do not identify Euclidean carrier polygons with native Cell Voronoi strata; this native comparator does not in itself establish the historical task's separately reviewed two-domain global-tool promotion.

The original frozen 28-LP mother ledger's particular LP011 erroneous full-native dominant-axis argmax invocation and LP019 erroneous signed cancellation of natural positive N-BRC counts are still not located. The exact current executable dependency census and independent Driver REQUEST_REVISION remain open. Original R063 C3/C4 native benchmark issue #2416 remains an unexecuted original-object support request. The 17:00 safety-denied prose report is not retried.

Next exact action: inspect active current source consumers passing 2D carrier nearest-site output to signed-native Cell identity/metric; test their call signatures with these three native pairs and make a targeted code correction only when an actual call-site type leak is demonstrated.
