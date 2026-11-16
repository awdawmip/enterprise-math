# EC49FQV — Two exact native-BRC price slices, 36-node continuum enclosure

Date: 2026-11-16. Evidence: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.
Frozen science: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Prior frontier: [EC49FQU PR #2574](https://github.com/awdawmip/enterprise-math/pull/2574) @ `f7cf7580d52ca8bb59645abb4f804593c8c5a549`; previously proven right-prior/high-price ray from [EC49FQM PR #2552](https://github.com/awdawmip/enterprise-math/pull/2552).

## Problem and fixed feasible native trees

BRC class 16943 has 310 original configurations, 141 full named-root profiles, 228 physical queries (144 terminal, 84 root; 209 unique partitions). Every adaptive finite decision tree must identify the complete named-root profile. Set `x=r/t`, `t>0`, `0<=lambda<=1`, with profile prior `p_lambda(i)=(1-lambda)/141+lambda*m_i/310`, where `m_i` is the original configuration multiplicity. The minimum cost normalized by terminal-query price t is `V(lambda,x)`.

Three *complete feasible native trees* have exact normalized costs:

- `A=(1-lambda)(6x+290)/141+lambda(6x+751)/310`, first labels 32,34, observation vector `(6,290;6,751)`.
- `B=(1-lambda)(5x+293)/141+lambda(5x+704)/310`, first labels 140,142, observation vector `(5,293;5,704)`.
- `C=(1-lambda)(5x+295)/141+lambda(5x+685)/310`, first labels 16,23, observation vector `(5,295;5,685)`.

The four components respectively sum root/terminal observation counts over the 141 equally weighted profiles and the 310 multiplicity-weighted configurations. Let `beta=620/3299`, `K(x)=7557-169x`, `gamma(x)=310(3-x)/K(x)`.

## Theorem 1 — two additional whole-prior exact slices

For each `x in {11/8,35/24}` and **every real** `lambda in [0,1]`, the unrestricted finite adaptive optimum is exactly `V(lambda,x)=min(A,B,C)`. The complete optimal first-label classification is:

| Prior range | Optimal physical first labels |
| --- | --- |
| `0<=lambda<gamma(x)` | 32,34 |
| `lambda=gamma(x)` | 32,34,140,142 |
| `gamma(x)<lambda<beta` | 140,142 |
| `lambda=beta` | 16,23,140,142 |
| `beta<lambda<=1` | 16,23 |

The new critical values are `gamma(11/8)=4030/58597` and `gamma(35/24)=11470/175453`.

**Independent integer Bellman witnesses.** The exact full-subset solver and a separately implemented unrestricted Bellman recurrence independently reproduced each objective and all 228 first-action costs. The native source hash pins are `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e` (master) and `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f` (profile CSV). For `lambda=a/b`, integer weights are `w_i=310(b-a)+141*a*m_i`; an integer cost divides by `310*141*b*t_num` for normalized cost.

| x | lambda | Bellman exact integer optimum | ALL minimizing first labels |
|---|---|---:|---|
| 11/8 | 0 | 739660 | 32,34 |
| 11/8 | 4030/58597 | 43812456240 | 32,34,140,142 |
| 35/24 | 0 | 2222700 | 32,34 |
| 35/24 | 11470/175453 | 393974315280 | 32,34,140,142 |

Complete replay of each tied-first native decision tree over all 141 profiles produced only the A/B vectors above.

**Proof beyond rational anchors.** Every fixed finite decision tree has cost affine in lambda. Endpoint Bellman optimality at 0 and gamma proves feasible A optimal for `[0,gamma]`. Feasible B is optimal at gamma and, by the inherited exact FQM right-prior theorem, at beta; hence it is optimal on `[gamma,beta]`. For `lambda>=beta`, the inherited global FQM region certifies C. For a *fixed first physical query*, the infimum over its feasible trees is a concave function of lambda. The difference above the corresponding affine A/B/C optimum is concave and nonnegative at both interval endpoints; for every unlisted first label it is strictly positive at least at one endpoint. Thus unlisted labels cannot tie in a strict interval interior. Explicit tied-first trees give precisely the listed labels at phase boundaries. This proves the unrestricted value and exhaustive first-label classification for all real priors, without an adaptive-depth cap.

## Theorem 2 — 36-node continuous certified region

Insert `11/8` and `35/24` into the previous 34-node exact-price grid. For each adjacent exact price interval `[a,b]`, bilinear interpolation of the gap between any fixed complete tree and A or B certifies global optimality of A for `lambda<=gamma(b)` and B for `gamma(a)<=lambda<=beta`. C is independently exact for `lambda>=beta`. The entire possible noncertified interior lies in **35 enclosing strips** `gamma(b)<lambda<gamma(a)`.

The total enclosing area is the **exact rational**

`S_36=3866402060924905195/766379559945117517848`,

and the certified area fraction of `[1,3] x [0,1]` is at least

`1-S_36/2=1528892717829310130501/1532759119890235035696`, or **99.7477488790801%**.

The inherited 34-node enclosing area was `928306751394905/174216767434670952`. All area calculations are exact rational arithmetic.

## Theorem 3 — improved rigorous all-price regret certificate

For every real `lambda in [0,1]`, `x>=1` and `t>0`, the best of these known feasible trees (and the inherited exact high-price strategy for `x>=3`) has expected cost no more than

`[50*(4/3-5/4)/(sqrt(29383/4)+sqrt(21995/3))^2]*t`

above the global optimum. This bound is approximately `0.0001419414506088826273*t`, improving the prior guarantee `0.000142488334760412*t`.

Proof: the true optimal value is the pointwise infimum of affine-in-x tree costs and thus concave in x. The certified endpoints provide a secant lower bound and the existing feasible trees provide an upper bound. The previously established sharp interval envelope is `M(a,b)=50*(b-a)/(sqrt(K(a))+sqrt(K(b)))^2`. Integer-square-root rational enclosures at denominator `10^13` show that the unique largest of 35 interval envelopes is attained at `[5/4,4/3]`; there `K(5/4)=29383/4` and `K(4/3)=21995/3`. The high-price ray `x>=3` has zero regret by the inherited theorem. QED.

## Reproduction, provenance, and open unit

The local complete evidence archive contains four new full Bellman machine certificates, their source input hashes, all 228 first-action values, all tied-first complete trees/replay counts, original generator, independent exact solver, rational enclosure checker and logs. It embeds the inherited FQU full evidence archive containing 129 previous complete certificates and frozen source. The index `EC49FQV_CERTIFICATE_INDEX_20261116.json` supplies each new certificate SHA256. The executable geometry checker is `EC49FQV_36GRID_GEOMETRY.py`. A complete verifier and source bytes are inside the separately delivered self-contained archive.

This is exact arithmetic in the frozen static BRC observer model. P000 / ACTIVE X6 worldview is retained unchanged. Formal shared Task publication/CLAIM and independent scientific review remain outstanding.

**Next science:** the largest enclosing regret interval is `[5/4,4/3]`; either certify a new price near its optimal log-K center or derive a parameterized Bellman lower bound proving the phase curve across the 35 strips. A concrete falsification target is a complete legal named-root BRC decision tree with cost strictly below `min(A,B,C)` inside one such strip.
