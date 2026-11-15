# R762AX — Token-feasible PASS languages and sharp positive-BRC growth

**2026-11-15, Enterprise Math / RS-X6-TRIADIC-CLOSURE-DYNAMICS.** Researcher \`EM-X6-44BACF\`; SID \`MCP-8b844b9054c94d40aaed0131426d3935\`; Activity \`RA-2BFD679DF2B3D27CAA0CB7D5\`. Frozen scientific source: \`enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`. This author-side theorem is conditional on the sequential token-PASS and V23/V25/V29 rules below; **NOT_REVIEWED**. It strengthens R762AW's six-order language by imposing actual resource availability.

## AX1. The complete legal language of one directed-cycle macro

Let m≥2; ports are labelled 0,…,m−1 (mod m). Each macro executes each distinct event e_i:i→i+1 **exactly once**, in a permutation order. The source must contain ≥1 token immediately before its event. That PASS decreases its source inventory by 1 and increases the target inventory by 1. No capacity constraints, extra edges, exogenous production, loss, simultaneous reservation or signed force cancellation are assumed. Start at K∈ℕ^m. Define S(K)={i:k_i>0}.

**Theorem.** A permutation word w is executable exactly when, for each i∉S(K), its incoming event e_(i−1) precedes its outgoing event e_i. If S=∅ there is no executable complete macro. Otherwise, list the occupied vertices in cyclic order s_1,…,s_h and let ℓ_j be the number of directed edges from s_j to the next occupied vertex; every ℓ_j≥1 and ∑ℓ_j=m. Then

\[
\boxed{q_m(K)=|\mathcal P(K)|=\frac{m!}{\prod_{j=1}^{h}\ell_j!}.}
\]

**Proof.** Prior to its single outgoing e_i, port i contains precisely k_i+1 if incoming e_(i−1) has executed, and k_i otherwise. Its outgoing event is enabled precisely if k_i>0 or incoming has already happened. This proves both directions for each event. When S is empty the resulting strict precedence inequalities form a directed cycle, impossible in a total order. With nonempty S, every intervening zero-inventory port forces an incoming-before-outgoing relation. These relations partition the m named edges into h disjoint fixed-order chains of lengths ℓ_j. Every linear extension is a shuffle of those chains and is executable by the established equivalence; the shuffle count is m!/∏ℓ_j!. QED.

Every complete macro restores K **exactly**, since one incoming and one outgoing occur at every port. Hence in an arbitrary sequence of r macros with a retained named PASS-word observer, there are q_m(K)^r permitted event-order histories when q_m(K)>0.

## AX2. Exact minimal sufficient inventory residual

For the observer family consisting of the legal named complete-macro word language at any finite future horizon, **S(K), the Boolean occupied-port support, is a minimal exact inventory quotient.** Sufficiency follows from AX1 and exact macro-end restoration of K. For necessity, the legal first-event set is exactly {e_i:i∈S(K)}: only a port initially occupied can fire first; for every such i, the clockwise word e_i,e_(i+1),…,e_(i+m−1) is legal. Thus differing supports have different languages, including empty versus nonempty supports. Consequently all inventory magnitudes >0 may be compressed to 1, but port identity, event order and within-macro branch provenance remain distinct. This quotient is proved for the stated scheduler and observers, not for arbitrary inventory readout, capacity checks, signed force state, or native Cell/Link/Port dynamics.

## AX3. Three-PASS phase diagram

Take p0=PASS(0→1), p1=PASS(1→2), p2=PASS(2→0). The rows use *event orders*, not V29 cumulative-mask traces:

| Initially occupied ports S | Executable named orders | q |
|---|---|---:|
| ∅ | none | 0 |
| {0} | 012 | 1 |
| {1} | 120 | 1 |
| {2} | 201 | 1 |
| {0,1} | 012,102,120 | 3 |
| {0,2} | 012,021,201 | 3 |
| {1,2} | 120,201,210 | 3 |
| {0,1,2} | 012,021,102,120,201,210 | 6 |

For example K=(2,0,0) permits only order 012 despite having two tokens, because the other outgoing ports initially have zero tokens. Thus R762AW's choice among six orders describes the fully-supported case, not all K.

## AX4. Resource-filtered typed BRC count

Reuse the **conditional** R762AW/R762AU selector on 20 active triples (3-subsets of {0,…,5}), with four V23 signed matching codes c(S), nine Johnson neighbors and V25 integer score

\[
\Phi(n,b;S,T)=u(n,b)\cdot c(T)+c(S)^\top\Omega(n,b)c(T).
\]

In a legal macro, for every PASS prefix update its V29 mask b and retain every tied maximizing successor. Take any integer prior complete-macro count n≥16. Let B_1^K(S) count all full *labelled* positive-BRC one-macro histories from S restricted to the PASS orders \(\mathcal P(K)\). For each r≥1 and K with q=q_3(K)>0,

\[
\boxed{B_r^K(S)=B_1^K(S)\,q^{r-1}.}
\]

For initial S on the previously identified six-state odd cycle C=(012,123,234,034,035,025), this simplifies to B_r^K(S)=q^r. With K=(0,0,0), no macro can execute and B_r^K(S)=0 for positive r.

**Proof.** By R762AW, every one of the six originally allowed three-PASS orders, together with all genuine intermediate V25 ties, ends in C after a macro. Filtering to the enabled sublanguage preserves this property. By R762AU, every stage mask produces the same unique next cyclic successor at every C state for each integer n≥2; hence each subsequent legal macro has exactly one cyclic triad trajectory per distinct event order. By AX1, the inventory returns to K at every macro boundary, leaving exactly q available orders for each successor macro. Keeping full noncommutative positive BRC provenance makes distinct order labels distinct histories, so B_(r+1)^K(S)=q B_r^K(S). Induction gives the result for arbitrary r. The n≥16 extension uses the exact previously established R762AU affine-dominance theorem; this theorem does not infer it from finite sampling. QED.

Exact integer enumeration of 20 initial triads, all 8 positive supports and all legal PASS permutations at n=16 gives:

| S(K) | q | B1(145) | B1(013) |
|---|---:|---:|---:|
| {0} | 1 | 1 | 2 |
| {1} | 1 | 1 | 1 |
| {2} | 1 | 1 | 1 |
| {0,1} | 3 | 3 | 4 |
| {0,2} | 3 | 3 | 5 |
| {1,2} | 3 | 3 | 3 |
| {0,1,2} | 6 | 6 | 8 |

Hence the inventory-limited counterexample K=(1,0,0) yields B_r^K(145)=1 for **all** r≥1, whereas unrestricted six-order R762AW gives 6^r. Yet B_r^K(013)=2 even with one initially occupied port, because the first macro contains a genuine **V25 state-tie**: event-order freedom and winning-state multiplicity are separate positive-BRC dimensions. For K=(1,1,0), B_r^K(145)=3^r and B_r^K(013)=4·3^(r−1).

## Verification and scope

Companion JavaScript checker uses exact integers: it reconstructs the four V23 matching codes, all nine Johnson neighbors, V29 ledger, every maximum including ties, 20 initial triads × all permitted words × 8 support masks, and checks six-cycle absorption. It independently enumerates token-resource constraints on directed m-cycles for m=2,…,7 (252 support cases), all event permutations, and inventories with the same support but magnitudes >1. The attached JSON certificate carries the complete m=3 first-macro table and resource tests. General AX1/AX2 and all-r AX4 are symbolic proofs, with finite testing as independent checking. All-n≥16 uses the saved R762AU proof.

Existing sources: R762AW, [PR #2458](https://github.com/awdawmip/enterprise-math/pull/2458) commit \`a71f4f4d72a27a013f46f41f87d2cb9785dd3820\`; R762AU, [PR #2451](https://github.com/awdawmip/enterprise-math/pull/2451) commit \`f42064096ba3014a63a8d75bbe9f4b7dcdaff447\`; R762AR/R762AS ordered token BRC and frame transport, PR #2436/#2440.

**Next scientific target:** establish the native P000 signed three-force Cell/Link/Port event and its legal PASS microstep schedule, and measure whether resource consumption is sequential or atomic. Then identify the V17 frame-to-port relabeling and V39 based-loop observer. Those actual interfaces determine whether AX1's token cycle is an admissible native scheduler or merely a precisely scoped comparator.

## AX5. Exact terminal-state distribution and two-step coarse period

Keep the same hypotheses as AX4 and index the six-cycle C by j∈ℤ/6ℤ. Let D_1^K(S)_j count the fully labelled one-macro histories ending at C_j (the 20×8 exact vectors are present in the JSON evidence). Then for every r≥1 with q(K)>0,

\[
\boxed{D_r^K(S)_j=q(K)^{r-1}\,D_1^K(S)_{\,j-3(r-1)\pmod 6}.}
\]

**Proof.** After the first macro, every labelled branch is on C. Each later macro consists of exactly three microsteps; on C each microstep advances one vertex, regardless of the chosen legal PASS order or mask. Thus the macro maps C_i to C_(i+3 mod 6), with precisely q(K) different retained PASS-order labels. Iterating r−1 times gives the coefficient and index shift. QED.

As a triad-only terminal observer, each endpoint has period at most two in the macro count (with positive scalar q(K)^(r−1) factored out). The **complete named-source histories still grow** by q(K) per macro: terminal readout and BRC provenance are distinct observers. Example, K=(1,0,0), root 145: terminal alternates C_2 then C_5 with one history each. Root 013 has D_1=(0,0,1,0,0,1), which is invariant under half-cycle shifting and therefore keeps that same two-point endpoint vector for every macro count. Root 145 with K=(1,1,0) has D_1=(2,0,1,0,0,0); after two macros, D_2=(0,0,0,6,0,3) under the C-index order (shift +3). For an observer that queries only weighted terminal triad counts, the six-component endpoint vector is a sufficient future macro state after absorption. It is not a sufficient state for a future query about original ordered PASS labels.

This extension follows from the already proven uniform cyclic successor property; it adds no assumption of a physical V17 frame return. Actual frame and V39 based-loop measurements require their own signed source/transport map.


## AX6. Exact periodic BRC word growth under finite frame-to-port transport

Suppose the named physical directed m-cycle edges are fixed, and after every complete macro an externally specified frame-port permutation \(\sigma\in S_m\) transports the port inventory according to \(K_{j+1}=\sigma K_j\), where \((\sigma K)_{\sigma(i)}=K_i\). This is a **conditional port-transport law**, not an assertion that P000/V17 already supplies such a permutation. Within each macro the AX1 source-token enabling rule still applies. Write \(q_j=q_m(\sigma^j K_0)\). Then the number of complete **named** PASS histories after r macros is exactly

\[
\boxed{\mathcal N_r(K_0,\sigma)=\prod_{j=0}^{r-1}q_j.}
\]

If the occupied support has \(\sigma\)-orbit period d, set \(Q=\prod_{j=0}^{d-1}q_j\). For any \(r=ad+b\) with \(a\geq0\) and \(0\leq b<d\),

\[
\boxed{\mathcal N_r(K_0,\sigma)
=Q^a\prod_{j=0}^{b-1}q_j.}
\]

**Proof.** A complete macro returns its input inventory exactly, so after frame transport the next starting inventory is \(\sigma K_j\). By AX1, every earlier named history has exactly \(q_m(K_j)\) one-macro extensions. Multiplying recursively gives the first identity. The support orbit of any permutation is periodic with period d, and AX1 depends only on support; splitting the product into a full d-period block and a remainder proves the second. Empty support yields zero histories for positive r, consistently with the formula. QED.

The frame permutation can change growth even while preserving the **number** of occupied ports. For m=4, take \(K_0=(1,1,0,0)\) and the transposition \(\sigma=(1\ 2)\). Before the first macro S={0,1}, cyclic gaps (1,3), so q0=4. Before the second S={0,2}, gaps (2,2), so q1=6. The frame restores the original S after two macros. Thus, for all r≥0,

\[
\boxed{\mathcal N_r=4^{\lceil r/2\rceil}6^{\lfloor r/2\rfloor}.}
\]

For r=1,…,8 this yields 4,24,96,576,2304,13824,55296,331776. This gives a concrete information-preserving distinction between **current positive-support cardinality** and **labelled support placement relative to an active frame**. In m=3, however, all positive supports of fixed cardinality have equal cyclic gap profiles, so any \(\sigma\in S_3\) leaves q3 unchanged. This last simplification holds for the token scheduler word count; a separate V17/V29 correspondence is required before transporting the conditional triad selector itself.

Exact independent integer verification covers every initial Boolean support and every frame permutation for m=4,5, enumerating 13,128 support-orbit cases against direct permutation-feasibility enumeration, with 33,792 periodic product checks for horizons r=1,…,8. The largest tested support-orbit period is 6. The proof applies to every m≥2, any finite permutation \(\sigma\), and all r≥0.
