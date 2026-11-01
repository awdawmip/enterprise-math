# EC49DB — Uniform all-h saturation of the signed-X6 positive-BRC future observer

2026-11-01 Asia/Shanghai. Status: **AUTHOR_ANALYTIC_PROOF / EXACT_MODULAR_SEED_AND_LIFT_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED**. No native CLAIM, Research-Activity registration, Result, independent Driver review or canonical acceptance has been obtained.

## Source pins and exact domain

GLOBAL_KNOWLEDGE_V1 canonical main **29d3846bdbcc3490fefec252f6095c6ddd6ff77f**; Enterprise Math canonical main **9c7b0f5cdb347c8651e94463387cab95fb031273**; predecessor EC49DA Draft PR #1730 **0219d0d3f0b6bd2aabf2863c10dbe5773e38cba6**. Current P000, ACTIVE worldview, native signed X6, joint-relation preservation, BRC arithmetic and portable research protocol were consulted. Neither P000 nor worldview is modified.

A native prefix is an ordered word in the twelve signed six-axis directions ±E1,...,±E6 with six-coordinate signed endpoint D relative to a chosen Cell; a chart coordinate is not a global ontic origin or a final Cell address. The ordered adjacent tags are A=(+E1,+E2) and B=(+E2,+E1). For each future operation word and resulting A/B final tag observe three *separate* additive channels (W0,W1,count), using native positive-step weights W0=(2,3,3,2,1,1), W1=(3,2,3,2,1,1) and weight 1 on all negative steps. This is exact positive-branch BRC, not signed-amplitude interference.

The complete operations on *signed ordered steps* are
a=(-1,-1), b=(-2,-2), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1), e=(+3,+1,+1,-3).
The **exact** future language comprises words of precisely h complete operations; the **cumulative** language has 1 through h operations. Only suffixes ending back at the chosen Cell are observed. Minimal sufficient dimension is the rational-linear rank of these prefix-versus-complete-future observation rows, *in this declared finite additive model*.

## Theorem — all integers h≥2

Let D=(2s,2v,0,0,0,0), s∈Z, v≥0, k=|s|+v≤h, and defect δ=h−k. On real ordered signed-X6 prefix paths of length n=2h+8, the exact and cumulative observers achieve all their possible rational ranks:

| Defect | Exactly h operations | One through h operations |
| --- | ---: | ---: |
| δ=0 | 12 | 12 |
| δ odd | 15 | 18 |
| δ even and δ≥2 | 18 | 18 |

For **every h≥2**, consequently,

\[
\dim O_{\mathrm{exact},h}=\frac{3(11h^2+15h+8)}{2}, \qquad
\dim O_{\mathrm{cumulative},h}=18h^2+24h+12.
\]

The first simultaneous saturation length is **n_sat(h)=2h+8**, and all larger even prefix lengths also saturate. This is a theorem for arbitrarily large finite h inside the specified BRC observer, not an inference from a finite numerical grid, a physical propagation theorem, or a fixed-memory statement for unbounded horizons.

## Proof 1: exact six-feature future-safe quotient and upper bounds

Every complete operation ends with a negative step; concatenation of complete operations creates no new adjacent positive-positive A/B pair across an operation boundary. Among individual complete operations only c contains A, only d contains B. A boundary B can be created when the first operation is c and the prefix ends +E2, and a boundary A when the first is d and the prefix ends +E1.

On each prefix define the four mutually exclusive final-tag indicators F00,F01,F10,F11, together with p_A=1[no A yet, last step is +E1] and p_B=1[no B yet, last step is +E2]. For *every* complete-suffix future word, every resulting tag indicator is a rational-linear combination of these SIX functions. Indeed with no c/d it preserves tags; with both c and d it produces tag11; with only c the result depends on past B plus a possible first-boundary p_B, with only d symmetrically on past A plus p_A. This proves the six-feature quotient is sufficient *for the declared complete-operation futures*, without erasing the original nine-state DFA before this factorization has been established.

For returning suffixes in fiber D, the operation counts obey N_b=v, N_e−N_a=−s, and N_a+N_b+N_e=k+2t for t≥0. Let j=N_c+N_d; precisely h operations force δ=2t+j. If δ=0 then j=0 and four tag indicators suffice, yielding 4×3=12. If δ odd then j≥1, and every result lies in the five-dimensional tag span (1,A_exists,B_exists,p_A,p_B), yielding ≤5×3=15. At positive even δ, or on cumulative interior fibers, six tag functions times the three independent BRC/count channels give the universal upper bound 18. These are *observer-specific* bounds and do not erase signed path provenance.

## Proof 2: nine literal native seed certificates

Each seed prefix begins with a neutral gate (-E3,+E3), followed by a genuine ordered signed-X6 core. Each seed row specifies a complete suffix word, final tag, and one of the three independent channels. The nine cases use only 150 total literal prefix witnesses. Their actual complete six-axis words and future row selections are stored in the adjacent **EC49DB_SEEDS.json.zlib.b64**, zlib-compressed UTF-8 JSON encoded with base64. The adjacent standard-library checker **VERIFY_EC49DB_GITHUB.py** reconstructs each literal path, native endpoint, ordered adjacent tag and exact positive BRC weights, then recomputes nonzero square integer minors modulo prime 1,000,003.

| Language | h | Endpoint (E1,E2; all others zero) | Minor size | Determinant mod 1000003 |
| --- | ---: | --- | ---: | ---: |
| cumulative | 2 | (+2,0) | 18 | 165905 |
| cumulative | 2 | (−2,0) | 18 | 285218 |
| cumulative | 2 | (0,+2) | 18 | 46019 |
| cumulative | 2 | (0,0) | 18 | 949109 |
| exact | 2 | (+2,0) | 15 | 405253 |
| exact | 2 | (−2,0) | 15 | 828162 |
| exact | 2 | (0,+2) | 15 | 61410 |
| exact | 2 | (0,0) | 18 | 338530 |
| exact | 3 | (0,0) | 15 | 98859 |

All nine nonzero modular determinants imply nonzero integer determinants and thus full rational ranks; the checker does *not* trust stored determinant claims.

## Proof 3: uniform tag-safe endpoint and horizon lift

Start with seed prefix (-3,+3) concatenated with its core. To shift endpoint by +2E1 or −2E1, insert two corresponding signed E1 letters **before** -3; to shift by +2E2 insert two +E2 letters **between** -3 and +3. Repeating insertions any nonnegative number of times leaves the complete prefix's A/B tag and its relevant last-letter state unchanged, because -3 separates all positive E1 from positive E2. Every seed path's W0 and W1 products are multiplied by the *same two strictly positive constants*; its count is unchanged.

For each stored complete suffix append a compensation a for +2E1, e for −2E1, and b for +2E2. Each appended operation is tag-safe, including at its first-step boundary; the endpoint returns and suffix length increases by one. Every output tag remains unchanged and each BRC channel receives a fixed path-independent factor. Each shift increases prefix literal length by 2 and future horizon by 1, preserving n=2h+8.

For cumulative depth, further increase the horizon by any nonnegative q without changing D by prepending q neutral pairs (-3,+3) to every prefix; leave future rows unchanged. For exact depth, add any number of *two-step horizon increments*: prepend two such neutral pairs and append the displacement-zero, tag-safe two-operation word ae to each future row. As required, all selected suffixes have precisely the new h operations.

Every interior fiber falls into one of the following lift families: cumulative nonzero endpoint from its sign/axis-specific h=2 seed, cumulative zero endpoint from h=2 zero seed; exact odd defect, nonzero endpoint from its h=2 seed and zero endpoint from its h=3 seed; exact positive even defect from exact h=2 zero seed followed by endpoint shifts. The parity condition in each family guarantees the stated horizon increments exist.

If the square seed minor is M and has r future rows (thus 3r columns and rows), its lifted minor M' is obtained by multiplying each of the three channel rows of every seed future row by (g0,g1,1), **with the same row factors independent of which prefix column is chosen**. It follows directly that

\[
\det M'=(g_0g_1)^r\det M\ne0.
\]

The constants g0,g1 are products of powers of 2 and 3. In particular the same prime 1,000,003 never divides these factors: the finite nine-seed certificate itself proves all-h nonvanishing. This explicit construction establishes *all* interior-fiber lower bounds; no enumeration of 5^h future words is required.

## Proof 4: boundary, dimension sum, earliest length

The EC49DA author-side analytic determinant construction already covers *all* 2h+1 boundary fibers at n=2h+8 with rank12, in both languages. Combined with Proof 3, all (h+1)^2 endpoint fibers reach their upper bound. Of these, h² are interior. Thus the cumulative rank is 12(2h+1)+18h², and summing the exact ranks 3r(δ)(2k+1) over k=0..h yields 3(11h²+15h+8)/2.

To prove minimality independently, take the extreme endpoint D=(-2h,0,0,0,0,0). Its *only* returning complete h-operation suffix is e^h. At length n=2h+6, a prefix ending there can contain at most three positive E1/E2 letters. To have both A and B, it must contain exactly the positive sequence 121 or 212. Their W0,W1 weights are respectively (12,18) and (18,12). After suffix e^h the tag-both outputs satisfy the universal identity

\[
R_{\mathrm{count}}=
\frac{R_{W0}}{30\cdot12^h}
+\frac{R_{W1}}{30\cdot27^h}.
\]

Hence this fiber has rank at most 11 rather than 12 at length 2h+6. Any shorter feasible even saturated length could be extended by neutral signed X6 (-3,+3) pairs to 2h+6, contradicting that rank deficiency. Odd prefix lengths cannot reach the specified even endpoint. Therefore n_sat(h)≥2h+8; Proof 3 and inherited boundary determinants give the matching upper bound.

## Actual verification, limits, next

Execute Python 3 standard library: **python3 VERIFY_EC49DB_GITHUB.py** in this folder. Actual local execution returned PASS on all 9/9 seed minors, 150 literal seed paths, and **1,298 independently reconstructed lifted interior minors** for both exact and cumulative languages at all h=2,...,12, including verification of both dimension sums. A separate longer source checker confirmed ten exact-integer, entry-by-entry lift/scaling equalities. The *all-h* inference is the symbolic determinant-lift argument, not the finite test range. The native signed-X6 positive BRC kernel and prior EC49CZ/DA sources remain unchanged. No false physical/signed-amplitude transfer is asserted.

Contextual references (not proofs of this special result): Laure Daviaud and coauthor Johnson, *Logical Methods in Computer Science* 21(3), 2025, DOI 10.46298/lmcs-21(3:15)2025; Lopez, *STACS 2025*, DOI 10.4230/LIPIcs.STACS.2025.67.

Native service returned research_authority_granted=false / CODE_REVIEW_REQUIRED; live owner lookup returned CONTROL_QUOTA. This GitHub artifact is durable author-side PORTABLE_DRAFT, *not* a Source-native publication, activity registration, CLAIM, Result, Driver review, or admitted theorem.

**Next EC49DC:** independently formalize the six-feature quotient and the universal lift in a proof checker (Lean where possible), derive certificate-generation bit bounds, and perturb the positive BRC weights/alphabet to find sharp generalization conditions or an exact counterexample. See NEXT_EC49DC.md.
