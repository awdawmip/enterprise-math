# EC49FQT — Five exact native-BRC phase slices; 30-node certified two-parameter region

2026-11-16 · `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`

**Scientific provenance:** frozen `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; predecessor EC49FQS [PR #2569](https://github.com/awdawmip/enterprise-math/pull/2569) at `21fd4a2b908b70331d44392e5c226e9e4188dab5`. Its 97 complete Bellman anchor certificates and proof scope are preserved.

## Model, definitions and scope

The frozen native category 16943 consists of 310 original configurations and 141 distinguishable full named-root profiles, with 228 legitimate physical observations (144 terminal / 84 root). A finite adaptive decision tree must identify its profile. Root-observation price is `r`, terminal price `t>0`, with ratio `x=r/t`; the exact profile prior is `p_lambda(i)=(1-lambda)/141 + lambda*m_i/310`, where `m_i` is the frozen multiplicity and `lambda in [0,1]`.

Put `beta=620/3299`, `K(x)=7557-169*x`, and `gamma(x)=310*(3-x)/K(x)`. The following are costs of actual feasible *complete* native adaptive trees, in terminal-price units:

```
A(lambda,x) = (1-lambda)*(6*x+290)/141 + lambda*(6*x+751)/310
B(lambda,x) = (1-lambda)*(5*x+293)/141 + lambda*(5*x+704)/310
C(lambda,x) = (1-lambda)*(5*x+295)/141 + lambda*(5*x+685)/310
F(lambda,x) = min(A,B,C)
```

## Theorem 1 — five full-prior price-slice solutions

For each `x` below and for **every real** `lambda in [0,1]`, the unrestricted finite-depth Bellman optimum among all native legitimate observations equals `t F(lambda,x)`:

| Exact x | First transition gamma(x) | Second transition |
|---|---|---|
| 25/16 | 7130/116687 | 620/3299 |
| 27/16 | 2170/38783 | 620/3299 |
| 29/16 | 5890/116011 | 620/3299 |
| 31/16 | 5270/115673 | 620/3299 |
| 33/16 | 310/7689 | 620/3299 |

Complete optimal physical first-query sets on each slice: `{32,34}` for `0<=lambda<gamma(x)`; `{32,34,140,142}` at `gamma(x)`; `{140,142}` strictly between `gamma(x)` and `beta`; `{16,23,140,142}` at `beta`; `{16,23}` on `beta<lambda<=1`.

**Full finite verification.** Four exact priors per price (`0, gamma(x), beta, 1`) give 20 new integer unrestricted Bellman certificates. They were recomputed by a separately authored weighted subset solver, including all 228 physical first-query labels and complete replays of every tied-first optimal decision tree over all 141 profiles. The two implementations agree at each anchor. Frozen input hashes, 97 inherited certificate hashes and all 20 new certificate hashes were checked. There are 117 complete Bellman certificates in the accompanying self-contained evidence archive.

For `lambda=a/b`, the exact integer Bellman weight of profile i is `310*(b-a)+141*a*m_i`, with denominator `310*141*b*t` for reporting terminal-price expected cost. The native solver uses the entire legal observation family and admissible lower bounds; it makes no decision-tree depth truncation. Representative full-tree aggregate counts `(uniform-root,uniform-terminal;multiplicity-root,multiplicity-terminal)` are `(6,290;6,751)` for A, `(5,293;5,704)` for B, and `(5,295;5,685)` for C.

**Continuous-prior proof.** For a fixed x, the global minimum of finite-tree costs is a concave function of lambda, being the infimum of affine functions. At both ends of each interval `[0,gamma(x)]`, `[gamma(x),beta]`, `[beta,1]`, its Bellman minimum equals the cost of a fixed complete A/B/C tree, respectively. The concavity chord is a lower bound, while that feasible tree supplies the same affine upper bound. Equality holds throughout. For any specified first physical label q, the restricted-first optimal cost minus this affine global value is nonnegative and concave on each interval; an interior zero would force zeros at both endpoints. Intersecting the exact endpoint first-label sets proves the claimed complete classification.

## Theorem 2 — full 30-price-node continuous certification

Add `25/16,27/16,29/16,31/16,33/16` to the inherited 25-node price grid in `[1,3]`. The resulting 30 nodes delimit 29 intervals `[a,b]`. On each interval, the global unrestricted optimum equals A over the **entire rectangle** `a<=x<=b, 0<=lambda<=gamma(b)`; B over `a<=x<=b, gamma(a)<=lambda<=beta`; and C over `a<=x<=b, beta<=lambda<=1`.

Indeed each fixed-tree cost difference against the selected A/B/C complete tree is bi-affine in `(x,lambda)`; the four corners of the indicated rectangles are exact optimality endpoints from Theorem 1 or the inherited certified price slices. The bi-affine interpolation is a convex combination of four nonnegative corner differences.

The 29 remaining potential-improvement bands are contained in `a<x<b, gamma(b)<lambda<gamma(a)`. Their total *bounding-strip* area is exactly

```
S30 = 43871554788230734445 / 7398811896183040660488
```

The established fraction of `[1,3]x[0,1]` is therefore at least

```
1-S30/2 = 14753752237577850586531 / 14797623792366081320976
        = 99.7035229750... %
```

## Theorem 3 — sharper global quantitative regret guarantee

For **every real** `lambda in [0,1]` and `x=r/t>=1`, the feasible A/B/C strategy on `[1,3]`, followed by the inherited exact strategy on `[3,infinity)`, obeys

```
0 <= C_strategy-C_optimal
  <= [ (25/6)/(sqrt(28369/4)+sqrt(42469/6))^2 ] * t
  < 0.000147020*t.
```

Compared with EC49FQS's `0.0002167599897633445*t`, the certified bound decreases by approximately 32.174%.

For each neighboring grid pair a<b, optimal value as a function of x is concave; its exact endpoint secant is a lower bound and F is a feasible upper bound. The inherited exact chord-envelope maximum is `M(a,b)=50*(b-a)/(sqrt(K(a))+sqrt(K(b)))^2`. Every current grid interval has width at most 1/12. Among all width-1/12 intervals, the maximum is at `[11/4,17/6]`, since K decreases strictly with x. Every other interval has width at most 1/16 and satisfies `M<=50/(16*4*K(3)) < 50/(12*4*K(11/4)) <= M(11/4,17/6)`, an exact rational comparison. `K(11/4)=28369/4` and `K(17/6)=42469/6` yield the bound. The prior high-price theorem gives exact optimality for `x>=3`.

## Reproduction and remaining question

A self-contained conversation archive named `EC49FQT_FIVE_NEW_PRICE_SLICES_30_GRID_COMPLETE_EVIDENCE_20261116.tar.xz` contains the two pinned original native sources, 117 complete anchor certificates, native generator, independent weighted Bellman verifier, all replays, proof, logs, machine summary and SHA256 manifest. Run the included `code/EC49FQT_INDEPENDENT_VERIFY.py` in ranges `0 5`, `5 10`, `10 12`, `12 16`, `16 20`; each finished `EC49FQT_ALL_CHECKS_PASS`. All arithmetic used for optimality decisions, strip areas and interval comparisons is integer or rational; decimal quantities are display approximations.

**Next mathematical question:** settle the global candidate phase boundary `gamma(x)` for all `1<x<3` by a parameterized native-BRC Bellman lower bound, or find a complete legal adaptive-tree counterexample within the 29 outstanding strips. The largest present chord envelope is at `[11/4,17/6]`, which also guides the next price test.

**Control/provenance:** This is independent portable scientific research. Current main has no `research_task_records/RS-EC49AS` immutable publication directory (bounded GitHub 404 check); therefore no formal CLAIM, Result, independent review or Activity checkpoint is asserted. Prior `EM-DIRECT-E78124` is retained as historical provenance only.