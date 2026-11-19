# X6 Unit160 — Exact cardinality of partial Barlow-prefix observation fibers

**Date:** 2026-11-19. **Task:** RS-X6-LEGACY-PLANE-RECONCILIATION, publication TP2-B4A441B23DA3159232C2. **Author:** EM-X6-FB6990, Research lane \`chatgpt-research-onhour-enterprise-math-20260923\`. **Status:** AUTHOR_PROVED / EXACT_INTEGER_EXECUTED / GITHUB_AUTHOR_EVIDENCE / UNREVIEWED / NOT_ADMITTED.

## Actual frozen producer → consumer edge

Historical comparison commit **\`fd2bcff10ca6e147348b6c1236027fc0d2877df3\`**, separate from scientific task input pin **\`59538f585d037d09ef687b28715c4bc1a3f9fe03\`**:

- \`src/enterprise_math/p022_barlow_stacking.py\`, Git blob \`cfa12c17671692d1fe0371b7d80e4cc019fbcf54\`: \`stacking_prefix_counts\` L133ff., \`vertical_witness_polynomial\` L145ff., \`vertical_witness_polynomial_from_counts\` L155ff., \`barlow_distance_and_geodesic_count\` L188ff.
- \`src/enterprise_math/p022_barlow_precision.py\`, blob \`34f351f55f25c115a872a9cbaf1a6dd7212089af\`: \`selected_layer_imbalance_state\` L137ff., \`recover_upward_sign_word_from_full_trajectory\` L153ff.
- Direct existing consumers: \`tests/test_p022_barlow_stacking.py\`, blob \`e0b6e3c4df5db0db0f8d238d527df72a3e4ca510\`, L102–135; and \`tests/test_p022_barlow_precision.py\`, blob \`1bf1cfb09b0f16b1964dc9c62011f9cf85bd415e\`, L56–125.

The existing P022 code **already proves** that the selected-layer imbalance determines the root-to-that-layer Laurent polynomial and that observing every prefix recovers the original sign word. This unit does not claim either result as new; it determines the **exact cardinality and bit cost of each resulting residual observation fiber**, including omitted terminal interfaces.

## New exact fiber-size theorem

Let \(n\ge 1\) and let the upward interface word be \(\sigma=(\sigma_1,\ldots,\sigma_n)\in\{-1,+1\}^n\). Its observed prefix imbalance at time \(t\) is \(\Delta_t=\sum_{i=1}^t \sigma_i\), with \(\Delta_0=0\). Fix a selected-layer language \(T=\{t_1<\cdots<t_m\}\subseteq\{1,\ldots,n\}\), where \(m\) may be zero. The observation is \(O_T(\sigma)=(\Delta_{t_1},\ldots,\Delta_{t_m})\), with the target layers included as query context.

For a proposed observation vector \(\delta\), set \(t_0=0,\delta_0=0\), \(L_j=t_j-t_{j-1}\), \(d_j=\delta_j-\delta_{j-1}\). Then the number of **distinct ordered sign words** consistent with this observation is exactly

\[
\boxed{F_{n,T}(\delta)
=2^{\,n-t_m}\prod_{j=1}^{m}
\binom{L_j}{(L_j+d_j)/2}.}
\]

Take \(t_m=0\) and empty product \(1\) for \(m=0\). A factor is defined to be zero if \(|d_j|>L_j\) or if \(L_j+d_j\) is odd. For a feasible vector, the lower bound on *additional fixed-length binary information needed to distinguish all ordered words within that fiber* is

\[
\boxed{b_{n,T}(\delta)=\lceil \log_2 F_{n,T}(\delta)\rceil,}
\]

achievable by indexing the \(F_{n,T}(\delta)\) words. The total number of distinct feasible selected-prefix observation vectors is
\[
\boxed{C(T)=\prod_{j=1}^{m}(L_j+1).}
\]

Proof: in each sampled interval of length \(L_j\), the observed increment \(d_j\) fixes exactly \((L_j+d_j)/2\) plus signs. Their placements can be chosen in \(\binom{L_j}{(L_j+d_j)/2}\) ways independently between disjoint blocks. Any unobserved tail of \(n-t_m\) signs remains free, giving the factor \(2^{n-t_m}\). Distinct increment choices are the \(L_j+1\) parity-correct values \(-L_j,-L_j+2,\ldots,L_j\), independently across blocks. The indexing lower bound follows because \(b\) bits distinguish at most \(2^b\) words. All are integer-exact.

**Sharp witnesses.** A single selected final layer \(T=\{n\}\) with observed \(\Delta_n=d\) retains exactly \(\binom{n}{(n+d)/2}\) possible interface orders; for \(n=8,d=0\), this is \(70\) words and requires **7 additional bits** for lossless order recovery. For \(n=8,T=\{2,5,8\}\) with \(\delta=(0,1,0)\), the successive block multiplicities are \(2,3,3\), so \(F=18\) and the sharp extra bit cost is **5**. For the complete prefix trajectory \(T=\{1,\ldots,n\}\), every \(L_j=1\), giving \(F=1\). For no sampled layer, \(F=2^n\).

## Relation to BRC, residual and frozen P000

At the **derived P022 periodic Barlow contact-graph observer** (triangular horizontal coordinates and vertical layer), the already proved source map \(\Delta_t\mapsto P_t\) makes the selected-layer Laurent coefficients, shortest contact distances and path counts invariant over each fiber. The new theorem quantifies how many source-distinct ordered interface histories this correct observer hides. Those words need not have the same local contact neighborhoods or intermediate-layer observations; asking for all intermediate layers makes the fiber singleton.

The fiber cardinality counts **stacking words compatible with an observer**, **not** native X6 N-BRC paths, not a signed cancellation of positive path masses, and not a two-dimensional native plane. Keep the derived contact carrier, original word/order provenance, the declared observation scope and the separate six-axis signed Cell task input pinned. This adds one actual producer→test consumer typed edge to 28-LP coverage but does **not** establish LP011's hypothetical wrong native argmax or LP019's hypothetical positive-count subtraction; both remain UNRESOLVED_PROVENANCE.

## Independently executed exact certificate

A separate Python verifier enumerates every ordered word of lengths \(n=1,\ldots,9\) against **every subset** of sampled positive layers (including empty \(T\)), groups words by their exact observed imbalance vectors, checks the product formula for each group and verifies the count \(\prod(L_j+1)\).

- **349,524** word–selection checks and **76,095** distinct observed fibers checked; maximum enumerated fiber size \(512\).
- Normal Python, \`python -O\` and \`python -OO\` each return exactly the same canonical JSON and SHA256 **\`a43e4afe1e123d4064060710cd15e666ed643bd3a2ea9d21f397ce5aee680610\`** (newline included).
- Checker: \`research_checks/X6_UNIT160_BARLOW_SELECTED_LAYER_FIBER_CHECK_20261119.py\`; result: \`research_checks/X6_UNIT160_BARLOW_SELECTED_LAYER_FIBER_RESULTS_20261119.json\`.
- This executes the independent integer formulation. It does **not** rerun historical P022 tests, the original R063 benchmark, or an original signed-X6 native experiment.

**Next substantive step:** inspect a distinct real frozen/current P022-to-native or 28-LP production consumer with actual source:line and transfer map, and test whether it requires only a sampled-layer Barlow observer or an ordered source trajectory. Reuse all previously verified proofs and benchmarks. Native Units149–152 linkage and independent Driver review remain outstanding; no Result/freeze admission is inferred.
