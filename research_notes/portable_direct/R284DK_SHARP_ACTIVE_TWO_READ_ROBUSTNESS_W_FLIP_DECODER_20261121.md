# R284DK — 冻结 Port 双读数的锐噪声半径与 w 翻转模增量恢复

Date: 2026-11-21 (Asia/Shanghai)
Status: AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / SAMPLE_DECODER_EXECUTED / NOT_REVIEWED
Scope: Frozen auxiliary 34-bit Port observer only; not a native X6 theorem. Independent portable research; no formal CLAIM/Review asserted.

## 1. Scientific source and setup

Frozen exact source: awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py
Git blob SHA-1: b46e0f682b58e47c27094b4bea6fa4e55119a3ee
Verified 65,536-word digest: b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4.

There are 65,536 lexicographically indexed binary source states, their distinct residues g(i) modulo P=17,179,869,143, and 64 labeled oriented integer circular arcs. Let D(x) be the maximal circular distance to the arc family. For a source flip q define E_q(i)=(D(g(i)),D(g(i xor 2^q))). R284DI already found that only q=0 (lower r) and q=6 (lower w) yield injective two-read maps among the 16 single-bit flips. This work measures their *precision margins* and constructs a practical w-flip decoder.

## 2. Sharp Chebyshev separation and precision theorem

For q in {0,6}, define
δ_q = min_{i != j} max(|E_q(i)_0-E_q(j)_0|, |E_q(i)_1-E_q(j)_1|).

**Exact theorem for the frozen model:**

| Source flip | Minimum L-infinity separation | Number of minimizing unordered pairs | Exact worst-case integer-coordinate error radius | Largest collision-free floor-quantization step 2^k |
|---|---:|---:|---:|---:|
| r, q=0 | 14 | 4 | 6 | 16 |
| w, q=6 | 53 | 2 | 26 | 32 |

The minimizing pairs for q=0 are (25808,25815), (25809,25814), (25810,25813), (25811,25812). For q=6 they are (61333,65493), (61397,65429). A q=6 explicit sharp pair has E_6(61333)=(8343605786,8343605727) and E_6(65493)=(8343605839,8343605674), differing by (53,-53).

Proof of computational exactness: enumerate the frozen words with the original digest assertion, evaluate each of their 64 integer arc distances, and construct all 65,536 two-read pairs. For each of the two q values, sort E_q by its first coordinate, sweep an active window ordered by the second coordinate, and examine **every** active point whose two coordinate gaps are below the current best bound. Upon a smaller distance the bound decreases. This never omits a better pair: a better L-infinity neighbor must have both coordinate gaps below the incumbent. A second exact sorted sweep enumerates **all** unordered pairs with first-coordinate gap at most δ_q and counts those with L-infinity gap equal to δ_q. No floating-point or approximate nearest-neighbor result is used in the published verifier. The resulting minima and complete minimizing-pair lists are in the certificate.

If both observed integer coordinates may independently be perturbed by at most ε in absolute value, different source states remain distinguishable whenever 2ε < δ_q. Conversely, the exhibited minimizing pairs have overlapping coordinatewise ε-neighborhoods as soon as ε=ceil(δ_q/2). Thus the sharp guaranteed integer error-correction radii are 6 and 26. For real bounded errors the uniqueness guarantee is |error| < δ_q/2 (strict inequality).

With fixed, zero-origin floor quantization Q_k(d)=floor(d/2^k), exhaustive exact checks show E_0 remains injective for k=4 but not k=5 (witness 25811/25812), while E_6 remains injective for k=5 but not k=6 (witness 1072/5168). Coarser powers remain noninjective by refinement monotonicity. This is a result for the stated grid origin and both readings quantized by the same power of two, not a universal rounding scheme or physical-noise model.

## 3. Exact w-increment derivative and finite kernel

Write the 12 lower source entries as (u1,a,x,y,u2,w,b,z,u3,g,h,r), all in {1,2}, and upper bits β0,...,β3 in {0,1}. The original determinant polynomial is affine in w. Collecting its coefficient exactly yields

κ_w =
 (D0-1-β0)(-x D3+r x-y h)
 +(-Z2-1-β2)(u1 D3-r u1+y u3)
 +(-Z3-1-β3)(-x u3+u1 h).

For the flip w ↦ 3-w, its residue increment satisfies

g(T_w σ)-g(σ) ≡ (3-2w) κ_w (mod P).

The coefficient depends on exactly nine specified binary choices: upper (β0,β2,β3), and lower (u1,x,y,u3,h,r). Enumerating their 2^9=512 possible settings gives 366 distinct raw κ_w integers, ranging from -5,003,907,149,232 to -2,501,945,035,417. Keeping the flip-origin w in {1,2}, the 1,024 core assignments produce exactly 732 distinct **modular** increment residues. Their bucket multiplicities are 1:608, 2:72, 4:36, 6:8, 8:4, 12:4. These finite counts were checked directly, and the increment identity was separately evaluated at all 65,536 frozen source states. No assumption that a modular difference uniquely fixes w or the nine core bits is made.

## 4. Constructive w-flip decoder

For each observed distance d>0, form all possible residue roots using the 64 arc endpoints:
S(d) = union_j { a_j-d, a_j+w_j+d } mod P,
and retain just those x in S(d) with D(x)=d. Since the 64 arcs have empty common intersection (indeed two specified frozen arcs are disjoint), D(x)>0 everywhere. The endpoint-distance identity proves that this procedure obtains **all** roots D^-1(d), at most 128 each.

Given the two readings (d0,d1), enumerate at most 128^2 residue pairs (x,x'). Look up Δ=(x'-x) mod P in the precomputed 732-key modular increment index. For each matching record (partial upper, six specified lower values, w), enumerate the remaining six binary choices: upper β1 and lower (a,u2,b,z,g), i.e. 64 completions; check the original exact determinant equals x mod P. Return each matching original 16-bit source state.

Correctness proof: the actual state contributes a pair of endpoint roots, its exact determinant increment belongs to the modular index, and its remaining six bits are enumerated; therefore it is returned. Conversely a returned state has residue x and flipped residue x' by the exact affine derivative, so it produces the supplied two distances. The all-state injectivity of E_6, independently rechecked in this work, implies at most one return. Therefore every *valid frozen-model input* is decoded uniquely. Arbitrary off-model or noisy inputs are not claimed to be accepted by this exact decoder.

The index holds 1,024 assignments distributed among 732 residue keys, with a maximum bucket length 12; no 65,536-entry residue-to-source inverse index is used. The upper bound of 128^2 root comparisons remains; this is an index/storage and sample-work result, not a proved universal time advantage.

## 5. Reproduction, comparison, and evidence boundary

Published Python checker and JSON certificate:
- R284DK_sharp_robust_w_decoder_checker.py
- R284DK_sharp_robust_w_decoder_certificate.json

Both depend on the exactly pinned R284CO generator, already available in the same research_notes/portable_direct directory. Run Python 3 standard library only. The original frozen input digest is asserted, exact nearest-pair distances and quantized collisions are reconstructed, the modular index counts are asserted, and all 65,536 w-flip determinant increments and all w-flip two-read signatures are checked.

An independent deterministic run with Random(20261121) chooses the same 109 source indices used by prior R284DJ (nine explicit indices and 100 fixed random indices). The w decoder recovered all 109 exactly. It inspected 472,888 candidate residue pairs, matched 446 modular assignments and made 28,544 determinant evaluations. Under the same sampling convention, R284DJ's r-flip decoder recorded 276,800 determinant evaluations. The ~9.69x smaller determinant-call count is **sample-specific**, not a measured wall-clock or unconditional complexity gain. The full 65,536-state decoder was not directly run; its correctness is an exact mathematical implication of the derivative, finite complete enumeration and all-state E_6 injectivity. All checks are author-controlled; independent review remains NOT_REVIEWED.

## 6. Relation to Enterprise Math and continuation

This is a model-local residual-fidelity statement: two-read operation selection changes the noise and quantization budget for recovering hidden source state, even when both operations are losslessly separating in exact arithmetic. It retains source bits and arc provenance. The Port circle and determinant here are auxiliary finite algebraic tools and do not automatically become native six-dimensional dynamics, BRC operations, or a full three-dimensional research slice.

Next: derive a directly updateable compact w-state code without enumerating both endpoint-root sets, compare total preprocessing/precision/operation/recovery costs against the r decoder and quadratic static label code, and test whether the sharp δ=53 separation survives a declared family of allowed downstream operations. Native Activity linkage requires separate verified original-session capability and CAS; scientific publication is independent of CLAIM, PROGRESS and REVIEW.
