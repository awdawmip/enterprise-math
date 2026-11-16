# EC49FRE — Twelve exact BRC seams, 98-node certificate, and rational-grid robustness theorem

Date: 2026-11-17. **Evidence level: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

Predecessor EC49FRD: [PR #2604](https://github.com/awdawmip/enterprise-math/pull/2604), immutable commit `5e753e49725947f18f202bd979e4861f396aac6a`. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Independent portable research; no RS-EC49AS formal CLAIM or Result.

## Fixed native finite BRC problem

BRC class 16943 consists of 310 source configurations, 141 **complete named root profiles** with positive multiplicities m_i (sum m_i=310), 228 **physically labeled** legal observations (144 terminal + 84 root, comprising 209 unique response partitions). The prior on the named profile i is
`p_i(lambda)=(1-lambda)/141 + lambda*m_i/310` for `lambda in [0,1]`.

Let t>0 be the terminal cost and r=xt the root cost with x>=1. The unrestricted V(x,lambda) minimizes expected sensing cost over **all finite adaptive separating trees**, preserving each legal physical action label. Three inherited feasible trees have costs normalized by t:

- A=(1-lambda)(6x+290)/141 + lambda(6x+751)/310
- B=(1-lambda)(5x+293)/141 + lambda(5x+704)/310
- C=(1-lambda)(5x+295)/141 + lambda(5x+685)/310.

Define K(x)=7557-169x, G(x)=310(3-x)/K(x), beta=620/3299.

## Theorem 1 — twelve new exact all-real prior price slices

For **every real** lambda in [0,1] and each x listed below, the exact unrestricted optimum is
`V(x,lambda)=t*min(A(x,lambda),B(x,lambda),C(x,lambda))`.

The entire physically labeled optimal first-query set is
- {32,34} for 0<=lambda<G(x);
- {32,34,140,142} for lambda=G(x);
- {140,142} for G(x)<lambda<beta;
- {140,142,16,23} for lambda=beta;
- {16,23} for beta<lambda<=1.

| x | G(x) | Exact unscaled weighted Bellman minimum | new full-certificate SHA256 prefix |
|---|---|---:|---|
| 153/64 | 4030/152597 | 924907329920 | b56a68790a53f32e |
| 151/64 | 12710/458129 | 2775622765440 | e50b024e4de92bff |
| 149/64 | 13330/458467 | 2776523541120 | a8b2b0652e4d925f |
| 147/64 | 930/30587 | 185161621120 | 7d6a4407347ebf6a |
| 145/64 | 310/9769 | 59113299840 | fa4707a90fb46ab9 |
| 143/64 | 15190/459481 | 2779225868160 | 1c341edc28e3cb30 |
| 141/64 | 5270/153273 | 926708881280 | 81308d23820af9f5 |
| 139/64 | 16430/460157 | 2781027419520 | d6fc779ea66bd142 |
| 137/64 | 3410/92099 | 556385639040 | dde39f087cba9230 |
| 135/64 | 5890/153611 | 927609656960 | ea2918e5f5dc9f55 |
| 133/64 | 18290/461171 | 2783729746560 | 7e93a27c197c7141 |
| 131/64 | 18910/461509 | 2784630522240 | a0a1a896054b16ba |

The unscaled value equals normalized expected cost multiplied by `x.denominator*310*141*lambda.denominator`; it is an integer Bellman accumulator, not units of t.

**Proof and exact dependency.** The frozen native loader constructs all 141 complete profiles and 228 permitted actions, retaining distinct first-query names even if response partitions coincide. The integer weighted-subset Bellman recursion tests every useful splitting action and every non-singleton response fiber. Because each informative observation strictly decreases the number of possible profiles and prices are positive, every finite adaptive separating tree reduces recursively to the same recursion; there is no imposed depth cutoff. At each new rational (x,G(x)), the primary native implementation and a second independently implemented DP produced equal integer optima and the exact tie set {32,34,140,142}; each tied root action has an actual replayed full separating tree. The independent DP visited 5,929 profile subsets at every new seam and checked all 228 physical first actions. Original 86-node source certification and **the inherited single-seam named-label exclusion lemma and endpoint anchors** are necessary to propagate these critical point computations to the full prior intervals: for fixed x every separating tree's expected cost is affine in lambda, the optimal value is their concave lower envelope, and equality with a feasible affine candidate at certified endpoints extends throughout their interval. The inherited source also establishes the shared second seam beta. Thus the all-real statement is conditioned on those actual inherited endpoint/exclusion certificates; merely checking 12 discrete critical points would not prove it.

## Theorem 2 — exact 98-node continuum enclosure

Let P86 denote the 86 previously certified x-nodes and adjoin all twelve x above to produce P98. For consecutive certified nodes a<b in [1,3], the possible uncertified region is enclosed in `G(b)<lambda<G(a)`. This is an enclosing strip, not a declaration of actual non-optimality.

For D=2185500, the total enclosed area is the exact rational identity
`S(P)=sum_(a,b) (b-a)*(G(a)-G(b)) = D*sum_(a,b) (b-a)^2/(K(a)*K(b))`.

The new exact geometry checker establishes
- `S98=296902200973874060795/160864097511408031554912`.
- `S86-S98=423000/1703822659>0`.
- Strictly certified fraction of the rectangle [1,3]x[0,1] at least
  `321431292821842189049029/321728195022816063109824 = 99.90771644960964%`.

Every one of the 97 intervals is bounded by
`R(a,b)=50(b-a)/(sqrt(K(a))+sqrt(K(b)))^2`.
Certified integer square-root brackets to 10^-40 separately compare the 97 bounds, with **unique maximal bound on [2,65/32]**. Combined with the unchanged inherited x>=3 tail certificate:

`0 <= t*min(A,B,C) - V(x,lambda) <= 0.00005413048225249587545*t`

holds for every real x>=1 and lambda in [0,1]. This numerical right endpoint is a rounded readout of the *exact algebraic upper bound* for [2,65/32], not an experimentally measured error. EC49FRD's previous upper guarantee was 0.00005461007501624838*t.

## Theorem 3 — rational implementability and quantitative stability of the ideal K-grid

Fix **any** 1<=a<b<=3 and integer m>=2. The EC49FRD unique joint area-minimizer and minimax-regret real grid has endpoints x*_0=a and x*_m=b, with
`K(x*_i) = K(a)^(1-i/m) K(b)^(i/m)`.
Let `rho=(K(a)/K(b))^(1/m)>1`, `h=log(rho)`. Consider any increasing real or rational grid `q_0=a<q_1<...<q_m=b`, whose interior knots lie in [a,b] and each satisfy `|q_i-x*_i|<=delta`. Put `eta=169delta/K(b)`. Let `S_min` and `R_minimax` denote the previous real-grid optimal area and maximal-interval-regret bound. Then

`0 <= S(q)-S_min <= (2185500/169^2)*(4m-6)*cosh(h+2eta)*eta^2`,
and
`R_minimax <= max_i R(q_i,q_(i+1)) <= R_minimax + 25delta/K(b)`.

**Proof.** Write eps_i=log K(q_i)-log K(x*_i). Monotonic K and the mean-value theorem on [a,b] yield |eps_i|<=eta and eps_0=eps_m=0. Let d_i=eps_i-eps_(i+1), y_i=log(K(q_i)/K(q_(i+1)))=h+d_i. Then sum d_i=0, |d_0|,|d_(m-1)|<=eta and |d_i|<=2eta for middle i; therefore sum d_i^2 <= (4m-6)eta^2. The *exact* area identity from the predecessor is
`S(q)=(2*2185500/169^2)*sum_i(cosh(y_i)-1)`.
Taylor's theorem for this auxiliary smooth real-valued area function implies
`cosh(h+d_i)<=cosh(h)+sinh(h)d_i+(1/2)cosh(h+2eta)d_i^2`.
The first derivatives cancel on summation and give the asserted **quadratic** area loss. The preceding strict-convexity optimum supplies the nonnegative lower difference.

For the maximal regret certificate the predecessor gives `R(q_i,q_(i+1))=(50/169)*tanh(y_i/4)`. Since tanh is increasing and has derivative <=1 on positive reals, each interval upper bound changes by at most (50/169)*|d_i|/4 <= 25delta/K(b); the inherited minimax optimum gives the lower inequality. These cosh/log/tanh quantities are *auxiliary real functions of sampling prices*; no classical propagation or trigonometry is used as a BRC-native sensing operator.

**Rational grid corollary.** Round each interior x*_i to its closest rational multiple of 1/H with integer H>=1 and keep exact endpoints. If
`1/H < K(b)*(rho-1)/169`,
the rounded grid remains strictly increasing and in [a,b], and `delta<=1/(2H)`. Its excess enclosed area is O(H^-2) with the **explicit coefficient above**, and its excess maximal interval regret bound is O(H^-1). The new rational prices require their own native Bellman certificates before being added to the *certified* BRC price grid.

**Concrete case.** The new certified rational seam `153/64=2.390625` in [19/8,77/32] differs from the exact continuous optimal cut `(7557-sqrt(K(19/8)*K(77/32)))/169` by about 0.0000028840945867956.

## Evidence and remaining question

The full immutable input, 12 freshly executed native Bellman JSON certificates, independent subset-DP implementation and logs, complete named first-query tree replay, exact 98-node geometry checker/JSON output, all inherited 86-node proofs, per-file sizes and SHA256 manifest are in the self-contained companion archive:

`EC49FRE_12_SEAMS_98NODE_RATIONAL_GRID_FULL_EVIDENCE_20261117.tar.xz` (archive SHA256 `3158b49a7e3775a728f6578942648c2b4f098a0b4bc3a8d0dd21499916a70148`).

Original frozen master SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; root CSV SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. These pins preserve source, not automatic peer review. The companion archive includes a 49-file integrity manifest; local re-open, each digest and size were checked. GitHub files are human-readable theory/checker/index; raw full native machine certificates are delivered in the companion archive, not represented as already in the PR.

**Next mathematical question:** On the remaining 97 parameter strips, construct a parameterized Bellman lower bound strong enough to establish global equality V=t*min(A,B,C), or exhibit an exact distinguishing tree with strictly smaller cost. The new largest *upper-certificate interval* is [2,65/32]. Independent further rational exact cut computations are useful, but full two-parameter closure needs a uniform proof or strict counterexample.

**Formal-control observation:** Exact native continuation request `r4-ec49fre-20261117-0730-continuation-01` returned `FAILED / CANONICAL_REJECTED: unknown current immutable task publication` for `RS-EC49AS`. Current native TASK_RESEARCH owner/CLAIM not authenticated; no invented Result/Review/Activity checkpoint. This draft follows the authorized independent portable research path, with no modification to P000 or the ACTIVE worldview.
