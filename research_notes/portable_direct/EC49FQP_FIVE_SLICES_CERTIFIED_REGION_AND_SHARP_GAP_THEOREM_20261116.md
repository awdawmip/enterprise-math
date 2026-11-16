# EC49FQP — Five complete price sections and an exact two-parameter certification theorem

Date 2026-11-16. Frozen input: `enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (native BRC class 16943). Prior frontier: EC49FQO PR #2559, 41 exact integer Bellman certificates. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Exact model and reusable witnesses

310 original configurations induce 141 distinct complete named-root states, observed by 144 terminal and 84 named-root queries (228 physical labels, 209 distinct cost-preserving partitions). Every finite correct adaptive decision tree identifies the complete state, not only the terminal quotient. Let `x=r/t>=1` (positive root/terminal query prices), and `p_lambda(i)=(1-lambda)/141+lambda*m_i/310`, with `0<=lambda<=1` and `sum m_i=310`. Normalize optimum by t: `v=V/t`. For any fixed tree, expectation is bilinear in `(lambda,x)`.

Three inherited and replayed feasible tree families have exact costs

```text
A=(1-lambda)*(6*x+290)/141 + lambda*(6*x+751)/310
B=(1-lambda)*(5*x+293)/141 + lambda*(5*x+704)/310
C=(1-lambda)*(5*x+295)/141 + lambda*(5*x+685)/310
F=min(A,B,C); beta=620/3299
gamma(x)=310*(3-x)/(7557-169*x), 1<=x<=3
```

The exact algebraic witness envelope selects A at `lambda<gamma(x)`, B at `gamma(x)<lambda<beta`, and C at `lambda>beta`, for `1<x<3`. These are candidate costs until the unrestricted Bellman bound is supplied.

## Theorem 1 — Five new fully exact all-prior price slices

For every real `lambda in [0,1]` and each new price `x in {13/8,15/8,17/8,19/8,23/8}`, the unrestricted finite adaptive Bellman optimum is **exactly v=F**, with the following *entire* first physical query sets:

| lambda range | All optimal first labels |
|---|---|
| `0<=lambda<gamma(x)` | `{32,34}` |
| `lambda=gamma(x)` | `{32,34,140,142}` |
| `gamma(x)<lambda<beta` | `{140,142}` |
| `lambda=beta` | `{16,23,140,142}` |
| `beta<lambda<=1` | `{16,23}` |

The five exact first transitions respectively are `3410/58259`, `930/19307`, `2170/57583`, `310/11449`, `310/56569`.

**Proof.** At each of the five prices, unrestricted exact integer Bellman recursion was performed at `lambda=0,gamma(x),beta,1`, using all 228 physical query labels, all 141 full states and weights `310(b-a)+141*a*m_i` for rational `lambda=a/b`. Twenty new machine certificates contain each exact global value, all first-label ties and replayable full decision trees. A distinct independent weighted Bellman implementation reconstructed the 209 partitions from the frozen source, calculated each global value and all 228 first-label competitors, and replayed each tied first-index tree. All 20 anchors agree exactly with F. At fixed x, every fixed tree's cost minus the applicable A/B/C witness is *affine in lambda*. Nonnegativity at adjacent anchor priors extends across the entire real interval. An interior optimum first label must occur at both anchor endpoints, since the difference of any optimal interior tree and the witness is an affine nonnegative function vanishing inside; the endpoint intersections give exactly the displayed sets. Each retained label is realized by an inherited full-tree witness. QED.

## Theorem 2 — Certified optimality on 99.41%+ of the two-parameter rectangle

Combine the five new prices with eleven previously proven all-prior sections:

```text
G16 = {1,7/6,4/3,3/2,13/8,7/4,15/8,2,17/8,9/4,
       19/8,5/2,8/3,17/6,23/8,3}.
```

For every consecutive `a<b` in G16, the **unrestricted global** optimum is:

- `v=A` throughout `a<=x<=b, 0<=lambda<=gamma(b)`;
- `v=B` throughout `a<=x<=b, gamma(a)<=lambda<=beta`;
- `v=C` throughout `a<=x<=b, beta<=lambda<=1`.

On the corresponding strict interiors, the entire optimal first action sets are respectively `{32,34}`, `{140,142}` and `{16,23}`. Along `lambda=beta` and `1<x<3`, the set `{16,23,140,142}` is attained. All `x>=3`, all priors, are already certified exactly by EC49FQM.

**Proof.** For each claimed subrectangle and its relevant fixed witness, all four corners have verified unrestricted Bellman optimality from Theorem 1 and the eleven inherited price slices. Every other fixed complete decision tree T has a **bilinear** cost difference `cost(T)-cost(witness)` in `(lambda,x)`. A bilinear function is the convex combination of its four corner values with nonnegative weights. Hence all competing trees have nonnegative cost difference everywhere within the rectangle; the witness attains the optimum. If a competitor ties strictly inside, bilinear nonnegativity and positive barycentric coefficients force it to tie at all four corners. The intersection of their exhaustive optimal first-label sets excludes every other physical label. Previously replayed tree witnesses attain the listed labels. QED.

The remaining potentially uncertified part of `[1,3]x[0,1]` is contained in the fifteen narrow strips `a<x<b, gamma(b)<lambda<gamma(a)`. Their exact total parameter area is

```text
S = sum_(a,b adjacent G16) (b-a)*(gamma(a)-gamma(b))
  = 43591107646076555945 / 3699405948091520330244
  ≈ 0.011783272303101716.
```

Since the full parameter rectangle has area 2, its uncertified fraction is at most `S/2 ≈ 0.005891636151550858`, so **at least 99.4108363848% of the rectangle by ordinary parameter-area measure** is now exactly solved. This geometric percentage is not a prior probability.

## Theorem 3 — An exact radical certificate for the global policy gap

For all real `0<=lambda<=1, x=r/t>=1`, with both prices positive, use F on `1<=x<=3` and the already proven high-price exact policies for `x>=3`. The resulting feasible full-query policy satisfies

```text
0 <= C_policy - V <= t * M16,
M16 = (25/3) / (sqrt(21319/3)+sqrt(42469/6))**2
    ≈ 0.00029374815990118765.
```

This bound improves the prior `25/57076 ≈ 0.000438012` guarantee by approximately **32.936%**. The constant is *exactly the maximum of the present certified secant-gap envelope*; it is not a claim that the true global Bellman gap attains the bound.

**Proof.** For fixed lambda, v is concave in x because it is the pointwise infimum of costs affine in x. With exact endpoints `v(a)=F(a)` and `v(b)=F(b)`, the chord `L_ab(x)=((b-x)*F(a)+(x-a)*F(b))/(b-a)` satisfies `L_ab<=v<=F`. Outside the gamma band, F is affine and the gap is zero. Inside the band, for fixed x, `F-L_ab` is affine on either side of `lambda=gamma(x)` and zero at the two band limits, so its maximum occurs exactly at gamma(x). The algebraic identity `(1-gamma(x))/141+gamma(x)/310=50/(7557-169*x)` yields

```text
D_ab(x)=50*(x-a)*(b-x)/((b-a)*(7557-169*x)).
```

Write `d=b-a`, `K_a=7557-169*a`, `K_b=7557-169*b`. Differentiating gives its maximizing x:

```text
x* = a + d*sqrt(K_a)/(sqrt(K_a)+sqrt(K_b)),
M_ab = 50*d/(sqrt(K_a)+sqrt(K_b))**2.
```

Exactly five G16 intervals have width 1/6. At fixed width, M_ab strictly increases with a; their rightmost `[8/3,17/6]` maximizes M. All other intervals have width <=1/8 and therefore `M_ab<=50*(1/8)/(4*(7557-169*3))=1/4512`, while `M_[8/3,17/6]>25/85276>1/4512`. Hence the global maximum is the interval `[8/3,17/6]`; substitute `K_a=21319/3`, `K_b=42469/6`. For x>=3 the inherited optimum is exact, completing the claim. QED.

## Reproduction / provenance / next open problem

Twenty new complete exact Bellman JSONs, primary integer solver logs, an independent separately implemented Bellman checker split into five completed batches, all 41 inherited SHA256-verified JSONs, both frozen input files, full paper, exact geometry verification and a master machine index are in the accompanying self-contained local evidence package `EC49FQP_FIVE_SLICES_CERTIFIED_REGIONS_EVIDENCE_20261116.tar.xz`. The independent checker verified the 20 optimal values, all tied first labels and every full decision-tree replay; it verified the inherited 41 certificates by SHA256 without wasting computation on an old solved unit. Full bundle contains a `SHA256SUMS` manifest. GitHub counterpart includes this proof, an executable exact geometry/anchor verifier and 20 case hashes.

Further mathematical work should either find a full native correct tree with a four-component count vector and a rational point beating F inside one of the narrow bands, or prove a parametric Bellman lower bound on all bands. These results retain unchanged P000, frozen scientific pins and the distinct author / independent-review / task-admission boundaries.