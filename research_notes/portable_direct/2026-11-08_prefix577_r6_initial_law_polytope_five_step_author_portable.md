# PREFIX577-R6: complete symmetry-preserving initial-law polytope and a sharp five-step test

**Date:** 2026-11-08 UTC. **Evidence status:** AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Neutral author-side mathematical evidence; not a native Source CLAIM, checkpoint, Result or Driver review.

**Frozen scientific source:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; original native `PREFIX565_positive_marginal_certificate.py` Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`. Scope is the **zero-root** native 96-port/six-labeled-action BRC-X6 model with complete path rewards `(R1,R2,R3,R4,R5,R6,K)`; `n` is the discrete path-depth index.

**Predecessor used, not re-claimed:** `research_notes/portable_direct/2026-11-08_prefix577_r6_full_axis_gate_c2_rank49_author_portable.md`, Git blob `311caef8c2a7f651f29a8248ad21c23458a22e5c`. It established full-axis exchange symmetry for uniform starts, a 51-state common weighted quotient, 165 transfer terms, two exact seven-label annihilators and response rank49. The present result completely classifies arbitrary starting laws and independently obtains a sharp decision horizon.

## Theorem A: all real initial probability laws

For an arbitrary probability vector `μ=(μ0,...,μ95)` on the 96 original native ports, define the full seven-variable path polynomial
[
F_n^{mu}(x_1,ldots,x_6;y)=mathbb E_mu!left[y^{K_n}prod_{i=1}^6 x_i^{R_i(n)}ight].
]
Let `τ` exchange only `x5,x6`. Then **`F_n^μ=τF_n^μ` coefficientwise for every integer `n≥0` if and only if** each of the 16 disjoint four-port blocks `A|B` below satisfies `Σ_(u∈A) μu=Σ_(u∈B) μu`:

| Block | A | B |
|---:|---|---|
| 1 | 20,21 | 44,45 |
| 2 | 16,17 | 40,41 |
| 3 | 88,89 | 64,65 |
| 4 | 92,93 | 68,69 |
| 5 | 18,19 | 66,67 |
| 6 | 22,23 | 70,71 |
| 7 | 90,91 | 42,43 |
| 8 | 94,95 | 46,47 |
| 9 | 34,35 | 82,83 |
| 10 | 38,39 | 86,87 |
| 11 | 62,63 | 14,15 |
| 12 | 58,59 | 10,11 |
| 13 | 54,55 | 78,79 |
| 14 | 50,51 | 74,75 |
| 15 | 26,27 | 2,3 |
| **16** | **6,7** | **30,31** |

The remaining **32 individually symmetric ports** are
`0,1,4,5,8,9,12,13,24,25,28,29,32,33,36,37,48,49,52,53,56,57,60,61,72,73,76,77,80,81,84,85`.
Every point mass on one of those ports already has exact full seven-variable swap symmetry for all depths; for instance **the one-port start `μ=δ0`**.

The invariant-law set is a convex rational polytope of **affine dimension 79**, with **exactly 96 vertices**: the 32 symmetric single-port measures `δu`, plus for each of the 16 blocks the four equal-weight two-port measures `(δa+δb)/2`, `a∈A,b∈B` (64 vertices). Every invariant probability law is a convex combination of these explicitly described vertices.

## Exact proof of the complete classification

Use the prior *row-equitable* 51-state full-label weighted quotient of the tagged union of the native and swapped 96-state automata. Each original port `u` maps to normal/swapped classes `(a_u,b_u)`, and has exact full-observer response `d_u(n)=q_(a_u)(n)-q_(b_u)(n)`. For every depth `n`, the two previously certified integer relations, checked again against all seven distinct labeled-transfer operators, are

`q40-q41-q46+q48=0`, and `q40-q42-q46+q50=0`.

Their difference proves `q50-q48=q42-q41` **for all n**. The 96 original port-class pairs partition into 32 fixed pairs, 15 reciprocal ordinary 2+2 blocks, and two reciprocal singleton class pairs whose response identity combines them into the exceptional 2+2 block `{6,7}|{30,31}`. This yields the **exact full-observer all-depth response factorization**

`F_n^μ-τF_n^μ = Σ_(j=1)^16 ( μ(A_j)-μ(B_j) ) H_j(n)`.

The `H_j` are 16 exact integer path-response families, not a numerically fitted basis; original six-axis/gate increments, parallel native action multiplicities and original ports are retained. An integer coefficient matrix for their monomials at path lengths `0,...,5` has an explicit **16×16 minor**
[
det M equiv 681390811 pmod{1000000007}
e 0.
]
The reproducer records the 16 selected depth/monomial rows and recomputes the determinant, so the 16 response families are linearly independent over `Q`; hence all-depth invariance forces precisely the 16 displayed balances.

For each four-port block, nonnegative left/right masses `l_a,r_b` share a total `t`; if `t>0`, coupling `γ_ab=l_a r_b/t` gives its contribution as `Σ_(a,b)2γ_ab(δa+δb)/2`. Add the 32 unconstrained singleton masses. This constructs every feasible law from the 96 vertices. Support arguments show each listed law is extreme. The 16 disjoint independent block equations, one normalization and an interior strictly positive uniform law give dimension `96-16-1=79`.

## Theorem B: finite five-step test, and sharpness

For **every** initial real probability vector on the 96 ports, the full seven-variable exchange identity holds at **all** depths if and only if it holds at the six depths `n=0,1,2,3,4,5`. The preceding 16×16 nonzero integer minor enforces all 16 block balances from these finite tests, and Theorem A gives the all-depth extension.

The bound **5 is minimal in general**. With the genuine native initial law

`μ*=(δ16+δ22+δ38+δ44+δ66+δ68+δ82+δ88)/8`,

an independent integer recurrence directly on the original 96 native ports gives **complete coefficientwise exchange equality at each depth n=0..4**. At depth 5, from exactly `8·6^5=62208` labeled native paths, monomial `(R1,R2,R3,R4,R5,R6,K)=(1,1,1,0,0,2,0)` occurs **1,096** times, while its exchanged monomial `(1,1,1,0,2,0,0)` occurs **1,080** times. The corresponding exact probability coefficient difference is `16/62208=1/3888`.

The successive ranks of all accumulated response observations modulo the prime `1000000007` at depths 0 through 5 are `0,1,6,10,14,16`. The exact eight-port witness, not a rank inference from modular reduction, establishes the sharp four-step counterexample.

## Executed author certificate and provenance

An independently rerunnable standard-library Python program reconstructed all `96×6=576` frozen zero-root labeled native transitions, matched the historical 576-row port/target/gate/R5/R6 edge snapshot, reconstructed the 192-tagged-state quotient with class-refinement `1→7→36→47→51`, checked its 165 terms and both seven-label annihilators, generated all 16 blocks and 96 polytope vertices, produced the explicit nonzero minor, and separately enumerated the eight-port depth-5 witness.

Local expanded proof: `PREFIX577_R6_INITIAL_LAW_SYMMETRY_POLYTOPE_THEOREM_20261108.md`. Executed Python: `prefix577_r6_initial_law_polytope_exact.py`. Exact 23,200-byte JSON certificate: `PREFIX577_R6_INITIAL_LAW_POLYTOPE_CERTIFICATE.json`, SHA-256 `215f02c55b6815a613cb3a78739474bb040da7ac08d8806b07234dbaab58c0ea`. Full six-file conversation-local reproducible ZIP SHA-256 `0a0630e3e21cd45b814a66e926cb423ccb9a9dfe0dfd873836ba40c0e86f429a`; clean extraction and re-execution yielded byte-identical certificate. The script also matched all 576×7 native edge entries of the previous author-side frozen-kernel derivation. ZIP is **local**, not claimed as a published Git object or Source artifact.

**Exact research scope:** zero-root, specified 96 ports/six labeled transitions, complete seven-variable joint-law observer and arbitrary real nonnegative initial weights. No arbitrary-root or physical-time assertion is made. This is author-checked finite-state mathematics and awaits independent Source review/admission.

**Native execution status (2026-11-08 06:45 UTC):** `em_status` returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE`, `operation_sent=false`; Sites `CONFIGURED_NOT_LIVE_VERIFIED`, `backend_connected=false`, `research_authority_granted=false`. No native session/claim/open/checkpoint/Result/review has been performed under this author note.

**Separate existing UR V2 obligation:** exact 94,687-byte four-file bundle, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; still missing as original bytes, not replaced by existing historical predecessor evidence. Native writer/provenance only after authorized Source continuation.

**Next discriminating scientific action:** inspect one admissible separately pinned nonzero native root and test which initial-law blocks survive, retaining original full joint reward labels and provenance. Before formal execution first read own recovery_status, original target_request_id receipt/reconcile, exact Source continuation and active CLAIM; for current-input seeds read every input artifact and set predecessor `completed_units=[]`. Scheduler remains unchanged.
