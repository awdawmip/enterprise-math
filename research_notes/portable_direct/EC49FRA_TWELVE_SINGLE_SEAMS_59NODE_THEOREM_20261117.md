# EC49FRA: 12 new exact BRC price slices, 59-node global enclosure

Date: 2026-11-17. Mathematical status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Inputs and inheritance

Immutable scientific input: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Scope: class 16943, 310 original configurations, 141 distinct complete named-root profiles, 144 terminal observations and 84 root observations (228 physically labeled actions, 209 distinct output partitions). Exact native source SHA256: master `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, profiles `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. This is finite positive-weighted BRC, not a theorem of native spatial dynamics. P000 is unchanged.

Inherits the 47-node full-prior slice proofs and single-seam theorem of [EC49FQZ PR #2591](https://github.com/awdawmip/enterprise-math/pull/2591) at commit `5bd4853e9f02cabbd3a1b995af72110ea26ffa16`, plus its complete archive SHA256 `ad0b4e53a0feac5e5b9f177c45147bdc7ab03996208a8a3bbcaf43aeafc1b5ff`.

With root price `x*t`, terminal price `t>0`, and prior `p_i(lambda)=(1-lambda)/141+lambda*m_i/310`, define the unrestricted finite adaptive Bellman value `V(x,lambda)`. The existing three complete legal trees have normalized costs

```
A=(1-lambda)*(6*x+290)/141 + lambda*(6*x+751)/310
B=(1-lambda)*(5*x+293)/141 + lambda*(5*x+704)/310
C=(1-lambda)*(5*x+295)/141 + lambda*(5*x+685)/310
K(x)=7557-169*x; G(x)=310*(3-x)/K(x); beta=620/3299.
```

## Theorem A: exact full-prior optimum at twelve new prices

For every price `x in {49/32,51/32,...,71/32}` and **every real** `lambda in [0,1]`, `V(x,lambda)=min(A,B,C)`. The complete optimal first-query sets are exactly `{32,34}` for `lambda<G(x)`, `{140,142}` for `G(x)<lambda<beta`, and `{16,23}` for `lambda>beta`. The seam at G(x) ties exactly `{32,34,140,142}`; the seam at beta ties exactly `{16,23,140,142}`.

Each new price lies between its already certified neighboring prices `k/16` and `(k+1)/16` for `k=24,...,35`. The table records the one necessary exhaustive integer Bellman computation at the new first seam, independently recomputed with a separately structured subset Bellman implementation.

| x | G(x) | unnormalized weighted Bellman optimum | independent visited subsets |
|---|---|---:|---:|
| 49/32 | 310/4969 | 14890921920 | 5904 |
| 51/32 | 930/15547 | 46628196160 | 5908 |
| 53/32 | 13330/232867 | 698972554560 | 5909 |
| 55/32 | 12710/232529 | 698522166720 | 5911 |
| 57/32 | 4030/77397 | 232690592960 | 5912 |
| 59/32 | 11470/231853 | 697621391040 | 5912 |
| 61/32 | 2170/46303 | 139434200640 | 5914 |
| 63/32 | 3410/77059 | 232240205120 | 5915 |
| 65/32 | 9610/230839 | 696270227520 | 5927 |
| 67/32 | 8990/230501 | 695819839680 | 5929 |
| 69/32 | 2790/76721 | 231789817280 | 5929 |
| 71/32 | 310/9193 | 27796762560 | 5929 |

**Proof.** Every complete finite labeled adaptive tree has cost affine in x at fixed lambda and affine in lambda at fixed x. Neighboring certified prices establish all-tree lower bounds for candidate A in `lambda<=G(b)`, B in `G(a)<=lambda<=beta`, and C in `lambda>=beta`. These inequalities interpolate in x for *every* competing complete tree, not just a library of selected policies. At the new price c, the exact Bellman equality at `lambda=G(c)` supplies the missing all-tree optimum exactly at A=B. Since V(c,lambda) is the infimum of affine tree costs, it is concave in lambda; coupled with V<=A/B it equals A on `[G(b),G(c)]` and B on `[G(c),G(a)]`. This proves the entire prior interval, including boundaries. For complete physical first labels, each constrained-first value V_q is likewise a concave envelope; strict positive constrained-first gaps at neighboring certified boundaries and at the new full labeled seam prohibit interior extra ties, while the given complete A/B/C witness trees retain all asserted labels. All physically labeled tied-first full decision trees have been replayed on the 141 profiles. QED.

## Theorem B: 59-node global continuum enclosure

Insert the 12 distinct prices into the verified 47-node grid. The resulting 59 nodes form 58 intervals on `[1,3]`. By bilinear full-tree interpolation, an adjacent certified pair `a<b` leaves only the possible uncertified strip `G(b)<lambda<G(a)`. As
`G(a)-G(b)=2185500*(b-a)/(K(a)*K(b))`, exact summation gives

```
Total containing-strip area S_59 = 469038291667513006195/157330981467832904648352
Certified fraction on [1,3] x [0,1] >= 314192924643998296290509/314661962935665809296704
Certified percent >= 99.8509389926600660662244304549%
Exact area reduction S_47-S_59 = 182125/186365844
```

The inherited theorem for `x>=3` remains in force. For **all** real `lambda in [0,1]`, `x>=1`, `t>0`, the explicit three-tree policy has a rigorously bounded regret:

```
0 <= C_policy - C_opt <=
 t * 50*(23/8-17/6)/(sqrt(7557-169*(17/6))+sqrt(7557-169*(23/8)))^2
 < 0.000073619708725015*t.
```

The worst 58-interval certificate is uniquely `[17/6,23/8]`, compared to predecessor `0.000108778433066686*t`. The executable geometry checker uses *only exact fractions* for strip areas and directed rational square-root brackets at 10^-24 resolution to establish the strict ordering of all 58 interval bounds. For each inserted c in (a,b), the exact area gain equals `2185500*(c-a)*(b-c)/K(c)*(1/K(a)+1/K(b)) > 0`. Summing the twelve gains yields the above exact reduction. QED conditional only on inherited valid exact Bellman endpoint certificates and error-envelope theorem.

## Evidence and next problem

Twelve new raw native certificates include 228 first-query cost entries and all tied optimal-first full separating decision trees. Twelve independent weighted subset-DP runs match the integer optima, all tied physical first labels and replayed tree cost vectors (5910-range states each); neither uses floating arithmetic for mathematical comparisons. Reproduction scripts and original frozen source are contained in the self-contained attached evidence archive `EC49FRA_12_SEAMS_59NODE_COMPLETE_EVIDENCE_20261117.tar.xz` (SHA256 `ada6150122ff866fb91e71c972430aef1b7ba79c501b23ab4da0a23557125263`), 61 files checked by per-file SHA256 and size after extraction. The repository stores this complete theorem, certificate index and exact geometry checker; the raw witness package accompanies the research conversation as an artifact.

Next: either certify the remaining 58 narrow bands through a parameterized **unrestricted** Bellman lower bound, or produce a strictly improving fully labeled native decision tree at a precise rational point in one band. For additional geometric refinement, prioritize the new worst interval `[17/6,23/8]`.

Control scope: portable independent research; the current Task `RS-EC49AS` has no verified immutable publication directory. This paper creates neither formal CLAIM/Result nor Activity checkpoint. No project-level review or admission is asserted.
