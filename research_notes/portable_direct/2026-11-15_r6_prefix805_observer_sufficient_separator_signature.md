# PREFIX-805 — Observer-sufficient separator signatures and exact quotient convolution

Date: 2026-11-15 (Asia/Shanghai). Enterprise Math / 进取数论, BRC auxiliary named-source integer model. Frozen science input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Continuation: PREFIX-804. Historical Researcher-ID: \`EM-DIRECT-4660FF\`; Activity: \`RA-63E1066C3056A93898BE8E18\`. Status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / NOT_INDEPENDENTLY_REVIEWED.

## Exact problem

Let G=(U∪V,E) be a finite bipartite graph with individually named edges, integer capacities K_e≥0 and specified nonnegative integer vertex demands d_v. A valid named table x has 0≤x_e≤K_e and ∑_{e∋v}x_e=d_v. Give each edge a signed integer observer vector w_e∈Z^q. Its exact multivariate Laurent histogram is

H_G(d;z)=∑_{x valid} z^(∑_e x_e w_e),

with integer coefficients counting distinct named tables. Partition the vertices into A and B; denote their internal edges by E_A,E_B and the crossing edges by X. A crossing assignment t∈∏_{e∈X}{0,...,K_e} leaves residual demands ρ_v(t)=d_v−∑_{e∈X,e∋v}t_e and contributes signed observer exponent ω(t)=∑_{e∈X}t_e w_e.

Define the **observer-sufficient boundary signature**

s(t)=(ρ|_A(t),ρ|_B(t),ω(t)).

Let m_s count the distinct crossing assignments having this exact signature, subject to capacities, nonnegative residual demands and signed cut balance. This signature is scoped to the declared final additive observer W; the pre-quotient named allocations remain distinct.

## Theorem 805.1 (exact signature quotient)

For every finite G, integer capacities and demands, and additive signed integer vector observer W,

H_G(d;z)=∑_s m_s z^(ω_s) H_A(ρ_A,s;z)H_B(ρ_B,s;z)

as an equality of Laurent polynomials over the integers. This permits exact aggregation of distinct crossing assignments with equal signatures, preserving all coefficients for the declared observer.

**Proof.** The map x↦(x|_X,x|_{E_A},x|_{E_B}) bijects full named tables with compatible crossing assignments and independent internal completions having the residual demands of that crossing assignment. Both capacities and vertex balances are preserved by the restriction/gluing maps. Because the observer is edge-additive, every table has exponent ω(t)+ω(x_A)+ω(x_B). Summing over the internal completion sets yields z^ω(t)H_A(ρ_A(t))H_B(ρ_B(t)). This product depends on t only through the displayed signature; collecting equal-signature summands gives the coefficient m_s exactly. All arithmetic is integral, with arbitrary signed exponents. QED.

## Theorem 805.2 (one cut variable eliminated)

Let D_A=∑_{v∈U∩A}d_v−∑_{v∈V∩A}d_v and ε_e=+1 for crossing edges whose row endpoint lies in A, ε_e=−1 otherwise. For every valid table, ∑_{e∈X}ε_e t_e=D_A, since each internal edge cancels between its row and column in A. If X≠∅, fix any e*∈X. Its value is uniquely forced by the other crossing variables:

t_e* = ε_e* (D_A − ∑_{e∈X\{e*}} ε_e t_e).

Thus a complete separator search needs at most ∏_{e∈X\{e*}}(K_e+1) candidate prefixes before capacity and component feasibility rejection. If X=∅, component feasibility decides the fiber directly. QED.

## Observer-relative compression and exact counterexample

An old signature remains sufficient for a newly added observer w' only if the new crossing contribution is constant within each old signature, or a separate exact descent certificate covers the extended observation. Thus the compression is conditioned on the declared observation scope and cannot silently erase named source distinctions.

Construct a 4×4 unit-capacity graph: all 2×2 internal edges within the {rows0,1;cols0,1} block and {rows2,3;cols2,3} block, plus the four crossing edges (0,2),(0,3),(1,2),(1,3). Demands: R=(2,2,1,1), S=(1,1,2,2). Exactly 16 named tables exist. Six crossing allocations satisfy the early cut and nonnegative-demand checks. With zero observer, they yield five signatures and H=16: two source-distinct crossings share identical component residual demands and equal observation. Add the named-source weight w_(0,2)=(1,0), all other weights zero. The six crossing allocations now yield six signatures and

H(z_1,z_2)=8+8z_1.

Both Laurent coefficients are verified by direct enumeration. This establishes the future-observer dependence of the quotient.

## Verified exact computation

\`PREFIX805_R6_SEPARATOR_SIGNATURE_CHECK.py\` implements independent (1) bounded Cartesian DFS for named full tables, (2) memoized suffix Laurent DP for the uncut graph, and (3) cut-balance-constrained crossing enumeration, exact grouping by signature, component suffix DP and Laurent coefficient convolution. It uses arbitrary-precision integers, signed exponent tuples and no floating-point mathematical test.

Exhaustive families: every 2×2 capacity vector in [0,2]^4 (81 patterns), and every 2×3 capacity vector in [0,1]^6 (64 patterns), with **every attainable row/column margin**. Totals: 145 capacity patterns, 1,919 margin fibers, 2,025 named full tables. Both exact algorithms agreed on every fiber. A fixed-seed (80520261115) set of 100 additional 3×3 configurations in [0,2]^9 with planted feasible margins was checked by all three algorithms. The 4×4 source-sensitive witness and two 4×4 benchmark configurations were also checked against independent direct DFS. Full source and structured results provide the exact input vectors, polynomial coefficients and counters.

For a 4×4 sparse two-block/two-crossing example, the verified fiber has 21 tables and 7 observable exponents; baseline memoized DP visited 4,429 distinct states, versus 244 aggregated component-DP states plus crossing search and signature processing in the separator implementation. For a dense 4×4 unit-capacity example, there were 90 tables, 11 exponent vectors and 70 viable crossing assignments. In nine local repetitions the median complete-operation wall times in this specific Python environment were approximately baseline 7.653 ms vs separator 0.595 ms (sparse), and baseline 9.932 ms vs separator 5.296 ms (dense). This is implementation-specific measurement, not a universal time-complexity claim.

Reproduce the exact data:

\`\`\`bash
python PREFIX805_R6_SEPARATOR_SIGNATURE_CHECK.py > PREFIX805_R6_SEPARATOR_SIGNATURE_RESULTS.json
\`\`\`

Runtime seconds vary per run, while exact integer counts, observer exponents and histogram coefficients remain invariant.

## Position and next unit

PREFIX-804 supplied exact crossing convolution; PREFIX-805 adds an exact observer-conditional quotient of crossing allocations, saving repeated component work where signatures coincide. PREFIX-802 supplied suffix memoization, PREFIX-803 bridges, PREFIX-800/801 Hall certificates. These are auxiliary combinatorial source-flow models; their native Cell/Link/Port and event-time correspondence remains a separate open scientific problem under the frozen P000/ACTIVE worldview and observer-preservation contract.

Next unit: maintain reusable component boundary messages and incremental Hall residual feasibility across neighboring signatures; evaluate complete time, memory, generated support and readback on larger sparse/dense ensembles, including adversarial large crossing separators. Separately derive a legitimate native X6 operation/readout map before any dynamical interpretation. No new shared CLAIM, Result, Review or P000 revision is made by this independent scientific note.
