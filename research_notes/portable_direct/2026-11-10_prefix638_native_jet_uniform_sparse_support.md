# PREFIX-638 — Uniform sparse support of native BRC second-moment transfers

**2026-11-10, author-side exact finite-state theorem; independent mathematical review pending.**  
Task family: `RS-X6-NATIVE-ROTATION-DYNAMICS`; frozen scientific input `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. This continues PREFIX-635–637, preserving the original 48 STAR phases, 96 ports, 576 individually labelled native BRC actions and positive rational path observer. P000, ACTIVE six-axis ontology and physical time semantics are unchanged.

## The exact theorem

Let the two original labelled patterns be `P0=(485,316,52,174)` and `P1=(52,174)`. Their Aho–Corasick automaton has seven states, so the joint port/automaton state set has `D=96×7=672` states.

Let `B` be the **Boolean adjacency matrix** of the original BRC action transfer at strictly positive gate `g=1`, with an edge from `(port,q)` to `(new_port,new_q)` iff an original labelled action of positive weight connects them. Boolean matrix powers refer to walks of exactly the stated length. Let `M(g1,...,gk)` denote the six-component PREFIX-637 exponential-jet transfer representing raw total mass, first and second occurrence-count moments `(Z,U0,U1,V00,V01,V11)`, where every gate `gi≥0` is rational.

**Theorem.**

1. An exhaustive *complete finite 672-state Boolean computation* verifies `B^5 = B^9` entrywise. Therefore `B^(k+4)=B^k` for every integer `k≥5`. There are four distinct eventual support classes (not merely two equal-count classes).
2. The support of `M(g1,...,gk)` is a subset of `B^k` for every nonnegative gate sequence; it equals `B^k` when every gate is strictly positive. The six-component jet tuple is nonzero iff its constant mass coefficient is strictly positive.
3. Hence **every nonempty consecutive-step jet product has at most 4,284 nonzero positions, 448 nonempty source rows, and 14 nonzero targets per source row**, for *arbitrarily large* window length `k`. These maxima are attained by the positive support class.
4. Multiplication of **any two consecutive positive-length** such jet matrices by sparse row-join evaluates at most **10,500** six-tuple pair-products, regardless of the two block lengths or the nonnegative rational gate choices.

This is an exact graph-support and arithmetic-operation theorem for the specified frozen two-pattern typed native BRC observer; numerical moment values themselves need not be periodic.

### Proof and reproducible finite certificate

Construct all 576 original BRC actions using the 48 STAR phases and original numbered-action enumeration. Build the seven-state failure-link automaton, preserving every original action identity and its hit mask. Represent Boolean matrices by sets of destinations for each source state, and multiply with set union. The standalone checker constructs `B^1` through `B^12`, verifies the **full** equality `B^5=B^9`, and checks the following exact table:

| k | Positive support positions | Nonempty rows | Maximum targets per row |
|---:|---:|---:|---:|
| 1 | 2,688 | 448 | 6 |
| 2 | 4,130 | 448 | 13 |
| 3 | 3,311 | 448 | 9 |
| 4 | 4,249 | 448 | 14 |
| 5 | 3,388 | 448 | 10 |
| 6 | 4,284 | 448 | 14 |
| 7 | 3,388 | 448 | 10 |
| 8 | 4,284 | 448 | 14 |

Since `B^5=B^9`, multiplying on the right by `B^r` proves `B^(5+r)=B^(9+r)` for every `r≥0`. Thus the finite first-eight-power table bounds all later powers. In the nonnegative labelled-path model no positive mass contributions cancel, so a jet's constant coefficient `Z` is positive precisely when an original positive-weight path exists; its higher moments share that support. A zero gate may remove paths, but cannot create new support.

For block lengths `i,j≥1`, the number of candidate pair-products of a sparse row-join is bounded by
`
J(i,j) = sum_x sum_{y in B^i(x)} |B^j(y)|.
`
By four-periodicity, each argument `i,j` can be reduced to `1..8` without changing its Boolean support. The verifier checks **all 64** such pairs and computes `max_{1≤i,j≤8}J(i,j)=10500`; `i=j=8` attains the maximum. This finite graph calculation, followed by the algebraic induction, establishes the universal multiplication constant.

**Bit-complexity qualifier.** Write `g_r=a_r/b_r` in nonnegative rational lowest terms. The common denominator of each length-`k` transfer coefficient divides `∏b_r`; every labelled path contributes at most `∏max(a_r,b_r)` to its common numerator, at most `6^k` paths originate from one product state, and an occurrence-count second moment is at most `k²` times the mass term. Hence numerator and denominator bit lengths are bounded by
`O(k + log(k+1) + Σ_r log₂(max(a_r,b_r)+1))`.
The two-stack PREFIX-637 queue makes `O(L+W)` matrix compositions across a length-`L` initial window and `W` shifts, and the new uniform 10,500 term bound refines that into `O(L+W)` *base-rational arithmetic operations* for its fixed frozen transfer kernel, with `O(L×4284)` stored six-tuples. Exact bit costs and the native entrance-state update remain chargeable.

## Executed original-native evidence

The attached **standalone** Python 3 checker constructs the original 48/96/576 action system and seven-state automaton without an external mathematical kernel, proves the Boolean finite certificate, checks all 64 join cases, and carries out **32 exact Fraction comparisons**: four gate families (all-one, positive rational, periodic zero, all-zero), lengths 1 through 8. The six raw moments produced by composed jet matrices equal a **separate original-action per-layer DP** in every case. The original phases, ports, numbered actions and all 4,032 AC transitions were also compared exactly against the pre-existing PREFIX-636 native implementation.

Execution: `ALL_ASSERTIONS_PASS AC 7 boolean power B5=B9 True matrix max entries 4284 max row 14 join max 10500 exact oracle comparisons 32`; execution JSON SHA256 `8929282141ad2b0d2609cac12dda25b4e578ec73627cb4990964c9cf05cdb309`.

A separate direct wall-clock comparison of the existing PREFIX-637 two-stack queue versus original-action forward DP at `n=20` produced these **single-run** times in seconds (the queue figure includes setup, shifts and queries; the independent DP figure recomputes all windows; both exclude common entrance-state work):

| L | Gate class | Windows | Rolling queue | Original-action DP |
|---:|---|---:|---:|---:|
| 4 | all ones | 13 | 3.35326 | 0.12231 |
| 4 | rational | 13 | 3.61273 | 0.12463 |
| 8 | all ones | 9 | 3.66523 | 0.18747 |
| 8 | rational | 9 | 3.59471 | 0.18289 |
| 12 | all ones | 5 | 3.98014 | 0.14647 |
| 12 | rational | 5 | 4.06903 | 0.15148 |

The test demonstrates that the dictionary-based Python rolling implementation is substantially slower than fresh DP for these small windows despite the strong asymptotic support certificate; implementation costs must be measured before using it for optimization claims.

## Complete reproducible artifacts

- `PREFIX638_native_jet_support.py.gz.b64`: gzip+base64 of the actual executed standalone Python checker, decoded with `base64 -d ... | gzip -d > PREFIX638_native_jet_support.py`. Actual source SHA256 `48d6521bab630f7f2d9de8ac7158ff074ff448267c1893a0dd064e4335c264f1`.
- `PREFIX638_native_jet_support_results.json.gz.b64`: gzip+base64 of complete original execution JSON; SHA256 of decoded JSON `8929282141ad2b0d2609cac12dda25b4e578ec73627cb4990964c9cf05cdb309`.
- Companion local handoff bundle contains the human-readable expanded proof, `benchmark_rolling.py`, full timing JSON, and precedent verification sources.

**Next discriminating study:** exploit the four-periodic support classes to precompile sparse row-join indices for the 64 block-length classes. Compare precise integer/Fraction multiplication counts, exact bit lengths, allocation overhead and RSS against the current dictionary queue and native DP; then examine how support periodicity changes with additional AC patterns. No current native CLAIM, independent Driver review, or official Result is asserted by this author-side artifact.
