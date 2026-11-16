# X6 Unit71 — operation-safe BRC observer fibers: a three-level exact classification

Date: 2026-11-17. Original Research lane `chatgpt-research-onhour-enterprise-math-20260923`, Researcher `EM-X6-FB6990`, Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. **AUTHOR-EXACT / FINITE-CHECKED / UNREVIEWED / NOT_ADMITTED.**

Scientific pins: signed-native X6 `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, P000 V5 ACTIVE_LOCKED. Preserve six named signed axes and three-axis selected registered slice, with other three *declared* coordinates zero. Fixed actual Cell start. Observer is `O(z)=(can3(z),G(z),T(z))`, where `G=Σ_{i≤3}z_i²`, `T=Σ_{i≤3}|z_i|`, and `can3(z)=z-min(z)(1,1,1)`. All comparisons here are between *complete global integer fiber* candidates; label retention changes future-operation equivalence.

## Theorem: three exact sufficiency levels on a two-element O fiber

Assume two distinct signed integer triples `z_-≠z_+` yield the same `O`. By Units69–70, they have the form `z_±=v±s(1,1,1)`, `s∈Z_{>0}`, `Σv_i=0`, and a shared shortest time `T`.

**(A) Uniform native all-length BRC count profile.** Let `C_L^{(6)}(z)` be the number of *ordered six-axis signed unit-step words of length L* with net displacement `(z_1,z_2,z_3,0,0,0)`, retaining all six native axes and allowing exact backtracks. Then
`C_L^{(6)}(z_+)=C_L^{(6)}(z_-)` **for every L≥0 iff** the three entries of `r=can3(z)` form an arithmetic progression. In that case, the entire series, not merely geodesic mass, is observer-safe.

**(B) Named-axis unsigned weight profile.** Attach independent formal commuting positive weights `w_1,w_2,w_3` to the first three named axis choices, ignoring direction. The weighted shortest-path polynomial is
`P_z(w)=N_BRC(z) w_1^{|z_1|}w_2^{|z_2|}w_3^{|z_3|}`, `N_BRC(z)=T!/∏_{i≤3}|z_i|!`.
The two polynomials agree **identically in independent weights iff** `r=(0,0,0)`. The same criterion holds for equality of all length-weighted six-axis profiles, since shortest length is one coefficient; when `r=0`, all six named absolute displacements agree.

**(C) Signed-direction-labeled native word counts.** Label steps separately as `+e_i,-e_i` (and preserve their source axis). For any two distinct candidates the signed shortest-path monomial exponents, hence the signed-direction-labeled profiles, differ. Restoring a signed native endpoint, directional response, or exact per-axis direction count therefore still requires the depth selector in every double fiber.

## Exact proof

For six-axis path count, put `a_i=|z_i|` for i≤3 and `a_4=a_5=a_6=0`. Every length `L=T+2k` word has `a_i+q_i` steps toward the required displacement on axis i and `q_i` opposite steps, where `q_i≥0` and `Σ_iq_i=k`. The ordered multinomial count is exactly
```
C_{T+2k}^{(6)}(z)
 =(T+2k)! Σ_{q_1+...+q_6=k} Π_{i=1}^6 1/(q_i!(a_i+q_i)!).
```
Odd excess lengths give zero by parity; lengths below T are impossible. This formula is symmetric under permutations of the six *absolute* axis counts. If `r` is an arithmetic progression, then `v` is a permutation of `(-d,0,d)`; the two triples `v+s` and `v-s` have the same **multiset of absolute components**, so every `C_L^{(6)}` agrees. Conversely equality for all L includes L=T, whose shortest-path count is unequal on any non-arithmetic double fiber by Unit70's exact factorial inequality. This proves (A).

At L=T, `P_z` is a single monomial with positive integral coefficient. Equality as polynomials in three independent named weights forces identical coordinatewise exponents and hence `|v_i+s|=|v_i-s|` for each i. Squaring gives `4sv_i=0`; since `s>0`, all `v_i=0`, equivalently `r=(0,0,0)`. Then coordinatewise unsigned counts coincide at every length; this proves (B). On a shortest path, the number of `+e_i` or `-e_i` steps is determined by the sign of `z_i` and its absolute value; the direction-labeled exponent vector reconstructs `z`. Distinct candidates yield distinct signed monomials, proving (C).

## Smallest distinguishing native witnesses

- `r=(0,1,2),G=5,T=3`: `z_-=(-2,-1,0)`, `z_+=(0,1,2)`. Equal **six-axis** native counts at lengths T,T+2,T+4 are respectively `3,290,26775`, even though their named-axis unsigned count polynomials are `3w_1²w_2` and `3w_2w_3²`. Setting `w=(2,1,1)` gives 12 versus 3 (same physical endpoint observation, different labeled response).
- `r=(0,0,0),G=3,T=3`: `z_-=(-1,-1,-1)`, `z_+=(1,1,1)`. All unsigned axis statistics agree, but positive versus negative direction labels differ.
- `r=(0,0,3),G=18,T=6`: `z_-=(-3,-3,0)`, `z_+=(1,1,4)`; the shortest native positive BRC counts are 20 and 30.

## Reproducible exact finite experiment

Companion integer checker enumerates all 9,261 signed input triples in `[-10,10]^3`, deduplicates 8,801 observed `(can3,G,T)` signatures, reconstructs the **complete global Z³ fiber** (including candidates outside the input box), and finds 8,239 singletons and 562 doubles: 280 arithmetic/equal-unsigned-global, 282 nonarithmetic/unequal-shortest; only 10 doubles are named-axis-unsigned equal (r=0). It compares exact six-axis word counts for each double at excess k=0,1,2,3: 2,248 equality decisions, zero failures. Ordinary Python, `-O`, and `-OO` outputs agree. The 562 global doubles differ from the 460 **within-box** collisions in Unit69 because this test retains 102 partners outside [-10,10]^3; the counting populations are different.

## Current parent-task effect and continuation

This is an operational extension of Units61,62,69,70: `(can3,G,T)` is sufficient for the full **uniform** path-return profile on arithmetic-progression double fibers, for **axis-labelled unsigned** path statistics only on `r=0` double fibers, and for a signed-axis-sensitive native operation on no double fiber. Consumers must explicitly declare which of these operation families they need before collapsing depth; a count-only adaptation does not automatically preserve axis-provenance or sign-sensitive dynamics.

The currently read `src/enterprise_math/diagonal_quotient.py` (main blob `a527e347e33d0a0039258a9b25f48b1f1466d149`) explicitly marks its canonical-min-zero operations as derived quotient, and `src/enterprise_math/p022_geodesic_multiplicity.py` (main blob `46373050168d2430b6cb3952aa763f3081284632`) is a separately typed graph metric. **No wrong native call is attributed to these inspected sources.** Historical LP011 bad argmax and LP019 signed-positive-BRC subtraction source:line remain UNRESOLVED_PROVENANCE; current 28-LP full dependency closure and independent Driver REQUEST_REVISION remain open. Original R063 and Helly benchmarks were not rerun.

Related exact prior results: [Unit69](https://github.com/awdawmip/enterprise-math/blob/b89055e5ea79b9dd4b6944567cc479baeff127ed/research_notes/X6_LP019_SIGNED_DEPTH_TWO_CANDIDATE_REPAIR_UNIT69_20261117.md), [Unit70](https://github.com/awdawmip/enterprise-math/blob/a396f46b0f86eec4c0346728f49ca0c63a4e2ee9/research_notes/X6_LP019_NATIVE_BRC_EQUAL_MASS_FIBER_CRITERION_UNIT70_20261117.md). Author-side proof and finite execution; not independent mathematical review or Result admission.


## Scoped native original-source executable crosscheck (post-theorem)

The exact **frozen** original `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` at scientific commit `59538f585d037d09ef687b28715c4bc1a3f9fe03` was fetched and its *actual local installed source bytes* independently checked as Git blob SHA-1 `300a96e3dc24bf6fff73743037a0347a8bc83176`. The actual original functions `endpoint_multiplicity`, `shortest_path_multiplicity`, `spatial_norm_squared` and `endpoint_weight` were executed for three selected genuine observer double-fibers, exact lengths \(T,T+2,T+4,T+6\), and named sign/axis weights. This is a **three-pair scoped import check**; it leaves the frozen R063 benchmark unmodified and does not rerun its full corpus.

| Shared observer-fiber type | Original native count profile on first point | On second point | Named independent-weight witness |
|---|---:|---:|---|
| r=(0,1,2), G=5, T=3 | 3, 290, 26,775, 2,570,904 | 3, 290, 26,775, 2,570,904 | shortest `w1=2` axis-unsigned: 12 versus 3 |
| r=(0,0,0), G=3, T=3 | 6, 540, 46,620, 4,210,920 | same | `+e1` weight 2, negative 1: 6 versus 12 |
| r=(0,0,3), G=18, T=6 | 20, 5,040, 918,540, 147,378,000 | 30, 7,056, 1,207,080, 183,245,040 | already different at shortest length |

The standalone locally executed original-source verifier returned `PASS` in Python ordinary/`-O`/`-OO`, with byte-identical JSON results (SHA256 `15d34db43070e1b93da1ec29e55ab8d3048af546c8d83a877a72a4d7a2e3df2d`). Reproduction [pinned-source adapter](https://github.com/awdawmip/enterprise-math/blob/110ea7d2e796a8d7fcfd2b81e2bdfd6d47c6f286/research_checks/X6_UNIT71_PINNED_ORIGINAL_BRC_WITNESS_CHECK_20261117.py) and [original-source output certificate](https://github.com/awdawmip/enterprise-math/blob/b263721b9be119044fadd5fd3b4ed9d19611e877/research_checks/X6_UNIT71_PINNED_ORIGINAL_BRC_WITNESS_RESULTS_20261117.json) preserve the scoped input/output, signed six-axis provenance and original-code blob guard. The returned data corroborate the theorem at these exact witnesses. Author-scoped, unreviewed.
