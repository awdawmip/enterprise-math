# X6 Unit157 — exact BRC-weighted root shells and signed-native lift

Date: 2026-11-19. Mother objective: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task: RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. Research lane: chatgpt-research-onhour-enterprise-math-20260923. Author provenance: EM-X6-FB6990, original SID MCP-082892eb480e45dea6d4b9fcc0491034. Status: AUTHOR_PROVED / FINITE_EXACT_EXECUTED / UNREVIEWED / NOT_ADMITTED. No Result, Driver acceptance, or P000 change.

## Actual immutable source-to-consumer relation

Task scientific input stays pinned at `59538f585d037d09ef687b28715c4bc1a3f9fe03`; separate historical comparison pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

* Historical `src/enterprise_math/lattice_geometry.py` blob `825ee26c918a4d7007e280aeaa1d7b750cd46aba`: `a_graph_distance` (lines 25–45) uses the derived A_p root e_i-e_j; `a_coordinator_shell_count` (lines 62–72) returns the **number of endpoints** at exact root radius m.
* Actual consumer `tests/test_lattice_geometry.py` blob `304ff8e769f93fa0e96a03c1ffe89960ea5dd622`, `test_low_dimensional_coordinator_shells` (lines 43–53) checks these endpoint shell counts, while `test_graph_distance_is_half_l1_on_a_lattice` (lines 64–70) checks the primitive-type relationship.
* Historical signed-native `src/enterprise_math/geometry.py` blob `a1a8dc4d1ca53fde2ca00d9b944c1b8aa346a152`, `l1_distance` (lines 95–101), represents standard-axis ±e_i unit motion. Its test consumer `tests/test_p012_geometry.py` blob `e1a8988169f12d4294e29446fb1a8558c412c77b` checks the native L1 meaning.

These source/test callers have **no claim** to path-weighted shell counts; the new result supplies the correctly typed bridge a downstream consumer would need. This is a new quantitative link, not a claim that an existing caller already has a bug.

## All-integer statement

Let n=p+1≥2 and A_p={x∈Z^n: Σ_i x_i=0}. A_p primitive root step is e_i−e_j (i≠j), and signed-native step is ±e_i. For m≥0 define shell S_m={x∈A_p: Σ_{x_i>0} x_i=m}. Let B_A(x) count **shortest labeled root words** ending at x; let B_N(x) count **shortest labeled native standard-axis signed words** ending at the same x. Define weighted shell totals

  W_A(n,m)=Σ_{x∈S_m} B_A(x),    W_N(n,m)=Σ_{x∈S_m} B_N(x).

Let T(m,a)=Σ_{j=0}^a (−1)^j binom(a,j)(a−j)^m be the number of surjections from a labeled m-slot word to a specified a-label alphabet, with T(0,0)=1 and T(m,0)=0 for m>0. For every n≥2 and m≥1,

  W_A(n,m)=Σ_{a=1}^{min(n,m)} Σ_{b=1}^{min(n−a,m)}
      binom(n,a) binom(n−a,b) T(m,a) T(m,b),

and W_A(n,0)=1. Moreover,

  **W_N(n,m) = binom(2m,m) W_A(n,m)**

including m=0. No approximation or real-valued length assumption is used.

### Proof

Any shortest root word to x∈S_m consists exactly of m ordered pairs (i,j) with i in the positive support P={i:x_i>0} and j in the disjoint negative support N={j:x_j<0}. Otherwise an axis undergoes both positive and negative increments and the root walk contains cancellations, so it has length greater than Σx_i^+=m. Conversely, an ordered sequence of m positive-axis labels and m negative-axis labels with disjoint nonempty supports, zipped positionwise, is a shortest root word to its endpoint; the endpoint is in S_m. This is a bijection across the union of all S_m endpoints, with path labels retained.

For support sizes a=|P| and b=|N| choose disjoint P,N in binom(n,a)binom(n−a,b) ways. Their two ordered label words each use every designated support label, hence there are T(m,a)T(m,b) choices. Summing proves the displayed W_A formula. At m=0 the only shortest empty word yields 1.

For every x∈S_m the Unit156 signed/native root-word shuffle bijection gives B_N(x)=binom(2m,m)B_A(x). Summing over S_m proves W_N. The factor is constant on the shell but **not** on the union of shells with differing m. Root shell cardinality |S_m|, W_A, and W_N are separate observers; none may silently substitute for another.

## Six-coordinate actual integer witness (n=6, p=5)

| Root radius m | Endpoint shell | A5 root shortest words W_A | Signed-native shortest words W_N | shuffle |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 1 |
| 1 | 30 | 30 | 60 | 2 |
| 2 | 240 | 630 | 3,780 | 6 |
| 3 | 1,010 | 9,750 | 195,000 | 20 |
| 4 | 2,970 | 121,590 | 8,511,300 | 70 |

At m=2, 30 endpoints have B_A=1, 120 have B_A=2, and 90 have B_A=4. Thus there are 240 endpoints but 630 root shortest paths, and 3,780 signed-native shortest paths. The path observer carries true extra multiplicity beyond the endpoint observer.

## Independent exact execution and limits

The local independent Python checker used direct shortest-root dynamic programming (retaining only transitions that increase actual root radius by one), separately computed signed standard-axis shortest-path counts by deletion of required unit steps, compared the pinned historical shell-count formula, and compared the surjection formula. It checked all p=1..5, m=0..4: 25 full shells and 5,881 individual zero-sum endpoints. Normal Python, -O and -OO each returned the identical canonical JSON stdout SHA256 `1cb87135af4532f0a22ee569a6a7429ef984f9bc3f240552975c896e48342dde`; every mathematical validation uses explicit exceptions, not Python asserts. This tests the reconstructed exact generator semantics, **not** an execution of the historical upstream tests or the R063 original benchmark. The proof is valid beyond the finite test range.

This is an author/source-typed theorem and a correctly-scoped new path-counting consumer bridge, not evidence that LP011/LP019's alleged historical erroneous call sites have now been located. Those precise commit:path:line origins, remaining 28-LP live consumers, independent Driver review and Units149–152 native semantic association remain open. Preserve all frozen pins, original failed Unit149 request, and Unit50 executed R063 benchmark.
