# X6 R77 — 任意四通道正权精度下的 125-Port 严格赢家区域及三见证定理

Date: 2026-11-21 (Asia/Shanghai). Scientific status: CONDITIONAL_AUTHOR_PROOF / EXACT_RATIONAL_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json` (P000 V5). Lineage: R68, R72, R76. This is a conditional positive-count BRC histogram observer theorem, not a native X6 update/dynamics claim.

## Model and complete statement

Fix `D=4`, population `p>=4`, positive measurement error weights `w=(A,B,C,Dw)` (the last symbol `Dw` denotes channel-4 precision weight, not the maximum degree). For integer differences `a=(a2,a3,a4)`, let `q(a)=max(sum(a_i positive),sum(-a_i positive))`, `z1=0` and `z_t=sum_{d=2}^4 a_d(d^t-d)`. The shared-offset pair collision radius is

`F(a;w) = (1/2) max_{i<j} |z_i-z_j|/(w_i+w_j)`.

Define the three independent fine-channel obstruction radii

`mL=max(1/(A+Dw),1/(C+Dw))`,
`mH=max(3/(A+C),3/(C+Dw))`,
`mM=max(3/(A+C),3/(A+Dw))`,
`m=min(mL,mH,mM)`, `delta=min(A,C,Dw)`, and `E=12/(B+delta)`.

Let `S=(114,-56,11)` with `q(S)=125`, `z(S)=(0,24,0,0)`. The three fine-channel witnesses are:

| ID | Difference a | q | z=(z1,z2,z3,z4) | fine-channel radius |
|---|---|---:|---|---|
| L | (10,-5,1) | 11 | (0,2,0,2) | mL |
| H | (45,-21,4) | 49 | (0,12,6,0) | mH |
| M | (39,-20,4) | 43 | (0,6,-6,-6) | mM |
| S | (114,-56,11) | 125 | (0,24,0,0) | 0 |

**Theorem (all four positive real weights).** For every `A,B,C,Dw>0` and `p>=125`, the only global minimizers of `F` among nonzero feasible integer differences are `S,-S` **if and only if**

`E < m`, equivalently `B > Bcrit := 12/m - delta`.

At `B=Bcrit`, `S` ties at least one of `L,H,M`. For `B<Bcrit`, at least one of `L,H,M` has strictly smaller radius than `S`. In the strict region `B>Bcrit`, for all integer `49<=p<=124` the exact optimum is `eta*(p)=m`, and for every `p>=125` it is `eta*(p)=E`. In particular, the 125-Port transition is strict and has exact step size `m-E`.

**Further corollary using the author-certified R72 complete 28-vector atlas:** For every four positive weights, `eta*(125)<eta*(124)` iff `B>Bcrit`. The converse no-drop direction uses R72's atlas completeness; the strict-winner theorem and strict-region plateau above are independent symbolic proofs.

## Proof

Write `H(a)` for the maximum of the three pairs among channels `{1,3,4}`:

`H(a)=max(|z3|/[2(A+C)], |z4|/[2(A+Dw)], |z3-z4|/[2(C+Dw)])`.

For any integer difference, `z3=6r`, `z4=2s` with integers `r,s`. If `(z3,z4)!=(0,0)`, split into exhaustive cases:

1. `z3=0`, `z4!=0`: `H>=mL`.
2. `z4=0`, `z3!=0`: `H>=mH`.
3. `z3=z4!=0`: `H>=mM`.
4. All `z3,z4,z3-z4` nonzero: their absolute values are at least `6,2,2` respectively, giving `H>=max(3/(A+C),1/(A+Dw),1/(C+Dw))>=mL`.

Thus every nonkernel difference satisfies `F(a)>=H(a)>=m`. The three explicit vectors attain the three respective `H` bounds with `q<=49`, so `m` is the **exact** nonkernel fine-channel minimum.

If `z3=z4=0`, divide the moment equations to get `a2+4a3+10a4=0` and `7a2+39a3+126a4=0`. Elimination yields `11a3+56a4=0`; hence `a=kS` for some integer `k`. Nonzero such differences require `q>=125`, and `F(kS)=|k|E`.

For the witness `L`, all channel-2 pairs have radius at most `E/12`. For `H` and `M`, all channel-2 pairs have radius at most `E/2`: each numerator after the `1/2` factor is no larger than `6` and each denominator is at least `B+delta`. Hence a witness achieving `H=m` has total `F<=max(m,E/2)`. If `E<m`, every nonkernel competitor costs at least `m>E`, and nonprimitive kernel competitors cost at least `2E>E`, proving unique optimality of `+-S`. If `E=m`, a fine-channel witness has `F=m=E`, giving a tie. If `E>m`, the witness satisfies `F<=max(m,E/2)<E`, proving strict suboptimality of `S`. When `E<=m` and `49<=p<125`, all feasible differences are nonkernel and a fine-channel witness attains `F=m`, proving the stated plateau. QED.

For the atlas-dependent corollary, R72's declared 28-vector sufficient atlas has only one vector requiring 125 Ports, namely `S`; its other 27 entries have `q<=71`. At `E>=m`, `S` cannot produce a strict decrease, so `eta*(125)=eta*(124)` by that certificate. At `E<m` the strict drop follows from the independent argument.

## Relation to R76, checks and next question

On restriction `A=Dw=1`, `C=u`, the new `M` obstruction is never smaller than the minimum of `L,H`; the criterion becomes exactly R76's three-piece boundary `B>12+11u` for `u<=1`, `B>23` for `1<=u<=5`, and `B>4u+3` for `u>=5`.

A genuinely new winner mechanism appears when `A=100,C=Dw=1`: then `mM=3/101` beats `mL=1/2`, `mH=3/2`, giving `Bcrit=403`. At `w=(100,403,1,1)`, `eta*(124)=eta*(125)=3/101`; at `w=(100,404,1,1)`, `eta*(124)=3/101`, `eta*(125)=4/135`. The governing 124-Port witness is the 43-Port vector `M`, rather than R76's `L` or `H`.

The companion Python `Fraction` verifier checked 15,624 signed nonzero triples in `[-12,12]^3` for parity/divisibility, 1,296 exact rational four-weight profiles against all 28 R72 vectors, and the boundary/step formula. Exact finite checks passed; general real-weight theorem rests on the above proof. R72 completeness is an existing author certificate and has not received independent project review.

Next: classify which of the 28 sufficient R72 vectors can win a nonempty open region of full positive four-weight space; independently test the Pareto atlas completeness; explore source-native named Port/Cell/Link and full TRIADIC_CLOSURE_E observer-fiber preservation without treating the conditional histogram as a native update law. Historical contributor `EM-X6-214D9C` / Activity `RA-545183ADD4EF71C3E4698AEE` is provenance, not asserted live CLAIM or mutation authority.
