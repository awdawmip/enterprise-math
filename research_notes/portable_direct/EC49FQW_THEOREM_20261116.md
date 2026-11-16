# EC49FQW — Four exact native-BRC price slices; 40-node certified enclosure

Date: 2026-11-16. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.
Frozen scientific source: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Parent: EC49FQV, PR #2576, commit `34358d691d3b75df970caf3c0c47250f87fd9d43`.
P000 / ACTIVE worldview retained. This is the native **static BRC observation** experiment, not a physical-model upgrade.

## Domain, objective and exact feasible strategies

There are 310 original BRC configurations, 141 distinct complete named-root profiles, 228 legal physical queries (144 terminal and 84 named-root; 209 unique partitions). The adaptive finite decision tree must identify the entire named-root profile, without depth restriction. Let `t>0` be the terminal-query price, `r=x*t` the root-query price, `x>=1`, and `p_lambda(i)=(1-lambda)/141 + lambda*m_i/310`, where `0<=lambda<=1` and `m_i` is the frozen source multiplicity. Let `V(lambda,x)` be the optimum expected cost in units of `t`.

Native physical decision-tree replay already establishes feasible trees

```
A = (1-lambda)*(6*x+290)/141 + lambda*(6*x+751)/310 ; first queries 32,34
B = (1-lambda)*(5*x+293)/141 + lambda*(5*x+704)/310 ; first queries 140,142
C = (1-lambda)*(5*x+295)/141 + lambda*(5*x+685)/310 ; first queries 16,23
beta=620/3299, K(x)=7557-169*x, gamma(x)=310*(3-x)/K(x)
```

## Theorem 1: four new complete, unrestricted full-prior phase slices

For **every real** `lambda in [0,1]` and any `x` from the following table,
`V(lambda,x)=min(A,B,C)`.

| x | gamma(x) | all first physical queries at zero / gamma |
|---|---|---|
| 25/24 | 310/3769 | {32,34} / {32,34,140,142} |
| 9/8 | 310/3929 | {32,34} / {32,34,140,142} |
| 29/24 | 13330/176467 | {32,34} / {32,34,140,142} |
| 31/24 | 12710/176129 | {32,34} / {32,34,140,142} |

In full, the first-query classification for each x is: {32,34} on `[0,gamma)`; {32,34,140,142} at gamma; {140,142} on `(gamma,beta)`; {140,142,16,23} at beta; and {16,23} on `(beta,1]`.

**Proof.** From the two original frozen input tables (verified SHA256 hashes below), reconstruct all 141 distinct full named-root profiles and all 228 native response partitions. The unrestricted integer subset-Bellman recurrence, without a depth bound, is evaluated separately for `lambda=0` and `lambda=gamma(x)` at each price ratio (eight anchors). At zero, A achieves the exact global minimum and only 32 and 34 are optimal first queries. At gamma, A and B attain the same global minimum and only 32,34,140,142 are optimal first queries. An independently written integer dynamic program recomputes all eight exact results; every tied-first complete decision tree is replayed for all 141 profiles with original multiplicities.

For fixed price ratio, the expected cost of any complete finite tree is affine in lambda. Hence the optimum is an infimum of affine functions and concave. Endpoint equality with feasible A on `[0,gamma]` forces A to be optimum throughout; endpoint equality with feasible B on `[gamma,beta]` forces B throughout, using the inherited globally exact beta boundary. For `[beta,1]` use the inherited right-prior exact C/B classification. For each constrained first query the optimal expected cost is also concave; subtract the relevant affine optimum branch, and use endpoint nonnegativity together with at least one strict positive endpoint to exclude any extra first label in the open interval. The A/B/C witness trees attain all indicated endpoint and interior labels. QED.

Anchor integer optimal values (the native weighted objective before dividing by `310*141*prior_denominator*terminal_price`):

| x | lambda=0 | lambda=gamma(x) |
|---|---:|---:|
| 25/24 | 2204100 | 8418367440 |
| 9/8 | 735940 | 2928336880 |
| 29/24 | 2211540 | 394987687920 |
| 31/24 | 2215260 | 394649897040 |

## Theorem 2: 40-node continuum certification

The 36 certified x nodes of EC49FQV plus the four new prices yield 40 nodes and 39 adjacent pairs `a<b` on `[1,3]`. For any such pair, A is globally optimal in the rectangle `[a,b] x [0,gamma(b)]`, B in `[a,b] x [gamma(a),beta]`, and C in the beta-to-one strip. Indeed, the cost difference between any fixed competing tree and the candidate is bilinear in `(x,lambda)`, and is nonnegative at all corners by certified endpoint optimality. Bilinear interpolation preserves that nonnegativity inside each rectangle.

The remaining possible unproved region is contained in the 39 narrow strips `gamma(b)<lambda<gamma(a)`. Their **exact aggregate area** inside `[1,3]x[0,1]` is
`97662317051285/21777095929333869`.
Thus the certified-optimal fraction is at least
`43456529541616453/43554191858667738 = 99.775768271930755...%`.
The preceding 36-node fraction was `99.747748879080113...%`.

## Theorem 3: new all-prior, all-price regret enclosure

For every `t>0`, real `lambda in [0,1]` and `x>=1`, an available complete native tree satisfies

```
0 <= C_strategy-C_optimal
  <= 50*(3-47/16)/(sqrt(112969/16)+sqrt(7050))^2 * t
   = 0.000110732667027230763516... * t.
```

This tightens the prior upper bound `0.0001419414506088826273...*t` by 21.99%. Each certified price interval `[a,b]` has the inherited exact chord/concavity error enclosure `M(a,b)=50*(b-a)/(sqrt(K(a))+sqrt(K(b)))^2`. All 39 candidates are compared using exact rationals and integer-square-root lower/upper enclosures at scale `10^16`. The maximum bound is **uniquely** `[47/16,3]`; the high-price ray `x>=3` is previously certified exact. Square roots here describe the *analytic error constant*, not the native scientific arithmetic. QED.

## Verification, current control and next question

The eight complete native integer certificates, their exact SHA256 indexes, two independent exact Bellman implementations, full 141-profile native tree replays, both source input files, a rational grid-area verifier, integer interval comparisons, logs, and the complete inherited EC49FQV archive are preserved together in `EC49FQW_FOUR_SLICES_40GRID_COMPLETE_EVIDENCE_20261116.tar.xz`, SHA256 `bce41b3c4a31091fc001cade94603fe553fb162b4dc09408bfeb526e3c25e333`. This archive was saved in the ChatGPT research handoff and is not a GitHub attachment; this PR contains the theorem, the deterministic grid arithmetic, and the exact certificate-index metadata. Source hashes: master `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; profile CSV `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

Native read-only task lookup `r4-ec49fqw-20261116-2341-task-read-01` returned SUCCEEDED with `RS-EC49AS=NO_CANONICAL_PUBLICATION_DIRECTORY` at Source `4e5ffe5e156a4b6ad91fd5901b89dc973142fc10`, observed 2026-11-16T15:42:43Z; this is a publication-directory observation only. This portable result does not assert formal CLAIM/Result or independent peer review.

**Next research question:** Split `[47/16,3]` at a log-K-optimal rational approximation and recompute the two required exact Bellman phase anchors. In parallel, seek a parameterized Bellman lower-bound argument closing all 39 residual strips, or a complete legal native decision tree beating `min(A,B,C)` at an explicitly checked interior point.
