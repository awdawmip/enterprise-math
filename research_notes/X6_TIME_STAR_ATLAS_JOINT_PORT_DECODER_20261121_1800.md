# X6 Native Time / Unit239 — four-STAR joint-event decoder and its exact 3-bit local bound

Date: 2026-11-21 (Asia/Hong_Kong). Status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

Parent: PO-X6-UPPER-STRUCTURE-20260906. Existing Task: RS-X6-NATIVE-TIME-DYNAMICS, publication TP2-91D4A7C2F63805BE21A3. Same research provenance: logical research lane \`chatgpt-research-onhour-enterprise-math-20260923\`, Researcher EM-X6-FB6990, SID MCP-082892eb480e45dea6d4b9fcc0491034; no maintenance-lane identity used.

Immutable scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Applicable source objects: \`p000_reality_foundation.json\`; \`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md\`; \`definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json\`; \`research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md\`. Reuses Unit237 (signed-axis histogram loses chronological BRC), Unit238 (ordered two-event wedge distinguishes INNER/OUTER at a *known oriented macro-edge*) at their actual author-proved scope.

## Question and exact answer

Unit238 requires a known oriented macro-edge \`a→b\` to decode its signed wedge. At the four-STAR K4 atlas, ask whether this edge, its STAR frame, its local sweep direction and the BRC branch can all be recovered from **only the known current signed shell Cell \`a\` and one ordered primitive-event wedge \`J\`**.

**Theorem.** Fix a chosen pivot Cell, a current signed unit shell displacement \`a=±e_i\` and a specific local C6 cyclic order on each of the four established STARs. Permit one adjacent shell macrostep within any STAR containing axis \`i\`, and permit either of its two shortest primitive BRC branches. Then exactly **eight** labeled successors \`(STAR, sweep, b, INNER/OUTER)\` are possible. The map
\[
(a,\mathrm{STAR},\mathrm{sweep},\beta)\longmapsto
\left(a,\ J=s_1\wedge s_2\right)
\]
is injective on these eight possibilities. It has an explicit inverse. Hence the sharp uniform fixed-length local record, *conditioned on the known current signed Cell and the frozen local atlas phase conventions*, needs **three bits**. The bivector is one compressed signed chronological joint observation; it has no interpretation as extra native spatial axes.

**Refined theorem.** On the frozen Viète local nonzero-intermediate-phase refinement lease, only the OUTER branch survives. The set has exactly four outgoing choices; the **support** of the bivector coordinate alone determines the outgoing STAR, signed next shell Cell and sweep. The sharp local record becomes **two bits**, within this lease.

## Proof

The four established K4 STAR line-family triples are
\[
S_A=\{1,3,6\},\quad S_B=\{1,4,5\},\quad
S_C=\{2,3,5\},\quad S_D=\{2,4,6\}.
\]
Each axis family \`i\` occurs in exactly two STAR triples. The two other families in one of these STARs are disjoint from the two other families in the other STAR. Thus at \`a=±e_i\`, an allowed signed C6 cycle has exactly two adjacent signed shell Cells \`b\` inside each STAR, with **four different axis supports** across the two STARs. This is independent of which of the six cyclic order conventions per STAR is chosen; it also holds under consistent signed reorientation of the three families because each neighbor still has a distinct axis family.

For an oriented edge \`a→b\`, with distinct native axes \`i\ne j\`, the two shortest X6 paths are
\[
\begin{array}{c|c|c}
\beta &(s_1,s_2)&\text{intermediate Cell relative to pivot}\\
\mathrm{INNER}&(-a,b)&0\\
\mathrm{OUTER}&(b,-a)&a+b .
\end{array}
\]
In the integral observer algebra \(\Lambda^2\mathbb Z^6\),
\[
J_{\mathrm{INNER}}=-a\wedge b,\qquad
J_{\mathrm{OUTER}}=+a\wedge b.
\]
The bivector \`a∧b\` has a single nonzero coefficient, equal to \`+1\` or \`-1\`, in the coordinate for unordered axis pair \`{i,j}\`. Therefore the nonzero coordinate support identifies \`j\` among the four different available axes. With \`a\` and the fixed STAR cyclic order, this identifies the unique signed neighbor \`b\`, the STAR and whether it is the clockwise or counterclockwise adjacent macroedge. Comparing the sign with \`a∧b\` then identifies INNER or OUTER. This reconstructs the entire labeled local transition, proving injectivity.

Eight possible inputs impose a three-bit lower bound; the recovered transition may be encoded by one STAR choice bit, one sweep bit and one branch bit. This attains the lower bound. It is a *local* information claim: no past BRC prefix, unobserved packet decoration or future physical dynamics is silently erased.

The existing frozen Viète theorem establishes, within these two shortest paths, that demanding a **defined nonzero intermediate carrier phase** selects exactly OUTER; the pivot-crossing INNER has zero intermediate relative displacement. Under that additional operation lease the branch bit is fixed. The four remaining neighbors have four different unsigned bivector supports, providing a two-bit decoder and a matching cardinality lower bound.

**Necessary conditioning witness.** Without the known current Cell, the same \`J=a∧b\` is produced by the OUTER path \`a→a+b→b\` and the INNER path \`b→0→a\`: in the latter \`(-b)∧a=a∧b\`. Hence \`J\` by itself does not label the starting Cell. Within a known STAR atlas, this is a concrete failure of a stronger unconditional decoder claim.

## Exact executable check

Source: [Unit239 JS checker](https://github.com/awdawmip/enterprise-math/blob/b653e7d29305b1b833dafeb2f47aa90f5a40d52d/research_checks/X6_TIME_STAR_ATLAS_LOCAL_WEDGE_DECODER_CHECK_20261121_1800.js), Git blob \`c2e176a0c819671727fdce023cc1e51db7a41a5e\`.

Result: [Unit239 JSON certificate](https://github.com/awdawmip/enterprise-math/blob/792824b92f1103d08b9da72ff333cda82380773e/research_checks/X6_TIME_STAR_ATLAS_LOCAL_WEDGE_DECODER_RESULTS_20261121_1800.json), Git blob \`f11ac46b225017e1a7ab256cdf56c9af5b32e66d\`.

Local Node.js execution of the **identical bytecode source** (remote immutable blob readback matched the locally executed file) enumerated all \`6^4=1296\` independent positive-basis cyclic order assignments across four STARs, each of the twelve possible current signed Cells, and eight labeled next choices per Cell. This gives **124,416 directed branch cases, 808,704 exact integer assertions, zero failures**. It checks actual ordered \`±e_i\` microsteps, midpoints, endpoints, exterior products, 8-way injectivity, 4-way OUTER-support injectivity and a reverse-edge branch-swap ambiguity witness. Arbitrary consistent signed chart reorientations follow from the algebraic proof; the executable enumeration fixes the basis-positive convention. Neither this proof nor finite execution asserts that a native physical Port presently measures \`J\`.

## Native / BRC observer and unresolved physical criterion

The exact decoder contract is:
\[
\text{input: current relative shell Cell }a,\ \text{ordered two-event }J,\ \text{known STAR phase atlas}
\longmapsto
(\text{STAR},\text{sweep},b,\text{branch},\text{intermediate Cell}).
\]
The declared future horizon is one adjacent native macroedge and its immediate Cell/BRC provenance. Full history requires retaining the ordered stream and the earlier source distinctions from Units237–238.

A **physical** result still requires a frozen-Source-qualified Cell/Link/Port transition that exposes ordered primitive increments or an equivalent antisymmetric joint observable, with triadic resource guards, admitted branch choices and a same-Cell independent C12/C24 precision-fiber reading. This Unit239 supplies a precise minimal local readout target and a diagnostic for whether available Port data is sufficient; it does not replace that source evidence.

Control separation: original Units233–235 Native PROGRESS is terminal failed from lack of live Issue #240 CLAIM; the two original typed-continuation prepares failed \`NATIVE_INPUT_SCOPE_METADATA_BUDGET_EXCEEDED\`. Existing support [Issue #2903](https://github.com/awdawmip/enterprise-math/issues/2903) remains a separate engineering dependency. The original SID, RA, prior Source frontier and native request identities remain unchanged. The R063 six-file native benchmark stays with separate task RS-X6-LEGACY-PLANE-RECONCILIATION / #2416. **UNREVIEWED / NOT_ADMITTED / no new protected Native semantic PROGRESS claimed.**
