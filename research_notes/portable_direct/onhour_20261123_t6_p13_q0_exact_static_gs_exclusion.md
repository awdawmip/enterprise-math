# T6 / maximal-p13 valuation-one q0: exact global mixed-congruence obstruction

Date: 2026-11-23 (Asia/Hong_Kong). This is an author-executed **TASK_RESEARCH scientific unit** for the existing T6 mother objective, not a new task/owner or independent review. Original logical research lane: \`chatgpt-research-onhour-enterprise-math-20260923\`; existing attributed Researcher \`EM-X6-FB6990\` / public SID \`MCP-082892eb480e45dea6d4b9fcc0491034\`. Status **AUTHOR_PROVED / EXACT_GS_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Native winning T6 CLAIM/PROGRESS not established by this mathematical file.

## Frozen question and precise statement

The immutable scientific task is \`research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md\` at \`d84bd940cfb093cdc60e569f15cad58772a51dca\` (blob \`87b3a6f38e9350f7a3f56624b27bff2a7778a439\`). Side exponent masses are each at most 2331; signed exponents, named denominators \(a=e+1\) and the six original moment equalities \(H_0,\dots,H_6\) are preserved. P000 remains ACTIVE_LOCKED.

After the separately saved author p13²-and-p13³ cancellation lemma, suppose the only residual valuation-one denominators divisible by 13 are \`a=13r\`, \`r=1,...,12\`, with arbitrary 13-free denominators permitted. Let \`u_r\` be their signed multiplicity after cancellation of common named atoms.

**Author exact q0-only proposition.** Under these hypotheses the signed p13 q0 vector is \`u=0\`. In particular, no primitive, nonidentical maximal-p13 collision with zero positive-order p13 vertical atoms can satisfy all six globally necessary 13-adic mixed congruences while respecting the true two side budgets.

This conclusion is model-scoped: p13 vertical orders \(q\ge1\), lower-prime completion, independent review and the global \(T_6=2332\) proof remain open.

## Proof: an exact saturated 12-dimensional congruence lattice

The binomial transform between \(H_j\) and \(S_j=\sum a^{-j}\) gives equal \(S_j\), \(j=1,\dots,6\). Multiplying the difference of each \(S_j\) by \(13^j\) and reducing modulo \(13^j\) leaves only the valuation-one p13 atoms. Since all 13-free terms vanish modulo \(13^j\), the necessary congruences are

\[
\sum_{r=1}^{12}u_r r^{-j}\equiv0\pmod{13^j},\qquad j=1,\dots,6.
\]

Each row equation has a unit coefficient modulo 13. Starting from \(\mathbb Z^{12}\), successively intersecting with the six equation kernels gives a full-rank integer lattice \(\Lambda\) of index \(\prod_{j=1}^6 13^j=13^{21}=\mathbf{247064529073450392704413}\). For each step, the exact checker selects a pivot row of nonzero 13-residue, scales it by \(13^j\) and eliminates the other rows modulo \(13^j\). Consequently each intermediate step is an exact basis operation, and the final determinant equals the complete kernel index; no candidate vector is lost.

The original exponent mass of q0 atom \(13r\) is \(w_r=13r-1\). Form \(\Lambda W\), with diagonal weights

\[
W=\operatorname{diag}(12,25,38,51,64,77,90,103,116,129,142,155).
\]

The checker takes the exact row Hermite normal form, then LLL-reduces the weighted integral basis, checks determinant \(13^{21}\prod_r w_r\) and verifies *each* reduced basis row against all six congruences. Exact rational Gram–Schmidt of this full basis yields the minimum diagonal square

\[
d_{\min}=
\frac{78577530278042129705264382752517501995032553011464356025}
{4243983974238642688103181306691645151538473248349}
\approx 18{,}515{,}039.35.
\]

For a nonzero integer coefficient vector, choose the highest nonzero Gram–Schmidt index. Its orthogonal projection has squared norm at least \(d_{\min}\), hence every nonzero \(u\in\Lambda\) satisfies \(\lVert Wu\rVert_2^2\ge d_{\min}\).

Meanwhile the original *separate* nonnegative side mass caps give

\[
\lVert Wu\rVert_2^2
\le \bigl(\sum_r w_r(u_r)_+\bigr)^2+
     \bigl(\sum_r w_r(-u_r)_+\bigr)^2
\le2(2331)^2=\mathbf{10867122}.
\]

The exact strict inequality \(d_{\min}>10867122\) is a contradiction for any nonzero integer q0 vector. Thus \(\boxed{u=0}\). The argument is independent of 13-free lower-prime contributions, which are annihilated in the necessary modular readout.

## Executed checker, provenance, and next frontier

A local Python/SymPy exact-arithmetic run established \(|\det\Lambda|=13^{21}\), validated the LLL basis's congruences and determinant, recomputed all twelve rational Gram–Schmidt squares, and asserted the exact rational value above and its strict budget separation. Reproducible compact checker: \`research_checks/T6_P13_Q0_STATIC_GS_EXACT_CHECK_20261123.py\`. Its local executed SHA-256 is \`ed0786958ca95be8539ab446028130aa4a37644a332217789efb964529c02dd7\`. It uses SymPy exact arithmetic without floating equality tolerances. The initial lattice experiment used a separate longer local implementation; the compact checker itself was also executed locally successfully before its GitHub publication. It is an author check, not a nonauthor verification.

Previously saved p17 q0–q16 and p13 high-valuation work are reused at their author/Source scopes, without replay. The smallest scientific next unit for maximal p13 is valuation-one positive vertical order \(q=1\), alongside any actually existing canonical q1 evidence and the full p13 congruences. Enumerate its named atoms, retain both separate side budgets, solve the affine 12-dimensional q0 cosets, and preserve any surviving candidate for lower-prime completion; do not infer global p13 closure from q0 alone.

Control: the current T6 owner/claim still requires a fresh native Source authorization. Scientific GitHub preservation and later own Activity linkage do not publish a protected semantic PROGRESS or alter the T6 Task, frozen input or its selector.
