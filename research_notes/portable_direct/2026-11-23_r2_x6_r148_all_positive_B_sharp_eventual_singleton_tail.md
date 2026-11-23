# X6 R148 — All-positive-B sharp eventual Port-10 singleton tail

Date: 2026-11-23 (Asia/Shanghai). Status: author exact analytic proof + finite integer/rational replay PASS. Independent mathematical review NOT_REVIEWED.

## Source and scope

Continue [R147](https://github.com/awdawmip/enterprise-math/blob/e3818eaa254807f4810e442c983e90152e3af4fa/research_notes/portable_direct/2026-11-23_r2_x6_r147_complete_post_plateau_near_fan.md) and R146, using the original **frozen** R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@0687aa24f5402da3b35f914dd6907967a9805b94 six-pair conditional BRC observation model. The Port-10 population comprises exactly 1,935 integer directions modulo sign, with no identification of nonzero multiples. For `w=(136,B,176,D)`, the six capacities are `(136+B,312,136+D,B+176,B+D,176+D)` and `F(a)=max(g_j/s_j)`; `eta=min_a F(a)`; `N={a:F(a)<(3/2)eta}`. Full gap map and Port convention are in R147. P000 V5 and ACTIVE Heartbeat World are the native context; no native time dynamics claim is made.

## Theorem R148 — exact unbounded two-to-one tail for every B>0

For **every positive real** `B>0`, define

```text
L(B) = 1872 - min(B,136)
T(B) = { 2448 + 17B  if 0<B<=136,
         2312 + 18B  if B>=136 }.
b = (4,-1,0)
c = (6,-4,1)
```

For **every real D>=L(B)**, the complete set of strict `3/2`-near Port-10 directions is

```text
N(B,D) = {c} union ({b} if D<T(B) else empty).
```

Thus there are exactly two near directions for `L(B)<=D<T(B)` and **exactly one**, namely `c`, for `D>=T(B)`. Equalities are handled by the strict threshold. The piecewise boundary `T(B)` is continuous with a genuine slope change at `B=136`: both pieces give `T(136)=4760`. It is the **sharp eventual singleton onset**: any smaller proposed upper-tail threshold fails at parameters immediately below `T(B)`, where `b,c` are both near.

This covers the previously unclassified `20<B<136` at all `D>=1872-B`, while agreeing with R137's high-D `0<B<=20` result and R147's `B>=136` result. No claim is made about the full lower-D membership fan for `20<B<136`.

## Proof

1. Let `m=min(B,136)`. The exact gap vector of `c=(6,-4,1)` is `(0,0,12,0,12,12)`; hence **for every B>0** its score is `F(c)=12/(D+m)`. Since `D>=L(B)=1872-m`, we have `eta<=F(c)<=12/1872=1/156`. Every integer direction with nonzero second gap has `g_1=3|x+4y+10z|>=3` and therefore `F>=3/312=1/104>=(3/2)eta`. The strict near condition excludes all such directions, including equality at `D=L(B)`.

2. The complete Port-10 enumeration from R146/R147 leaves precisely 15 directions with `g_1=0`. The exact gap vectors identify `b,c` plus 13 others with third gap `g_2>=22`. For `B>=136`, `F(other)>=22/(D+136)>(3/2)*12/(D+136)=(3/2)F(c)`. For `0<B<136`, the inequality `22/(D+136)>=(3/2)*12/(B+D)` reduces to `4D+22B>=2448`, which holds strictly since `D>=1872-B>1736`. All 13 are excluded. Thus the only possible near directions anywhere in the stated domain are `b,c`.

3. For `0<B<=136`, `F(c)=12/(B+D)`, while direct gap comparison gives `F(b)=max(1/(B+136),11/(D+136),12/(B+D))`. Hence `eta=F(c)`: `c` is optimal. The last ratio in `F(b)` automatically lies below `(3/2)F(c)`. The middle ratio also does because
```text
11/(D+136) < 18/(B+D)   <=>   7D+2448>11B,
```
and `D>=1872-B`, `B<=136` make this strict. The first ratio satisfies `1/(B+136)<18/(B+D)` exactly when `D<2448+17B`. This proves the stated membership boundary for `B<=136`, with equality excluded.

4. For `B>=136`, the domain `D>=L(B)=1736` lies inside R147's post-plateau range `D>=max(1008,1248-B)`. R147's complete near-set formula gives `c` always, `b` exactly for `D<2312+18B`, and its four old directions only for `D<max(1580,1872-B)<=1736`. Thus those four are absent at and above `L(B)`, leaving precisely the stated two-to-one tail.

5. `L(B)<T(B)` for every `B>0`: when `B<=136`, the gap is `576+18B>0`; when `B>=136`, the gap is `576+18B` as well (`2312+18B-1736`). Therefore both tail cells are nonempty, and just below `D=T(B)` the two directions `b,c` remain, establishing sharpness of this eventual singleton onset.

## Verification

Companion standalone-on-repository verifier: `research_notes/portable_direct/x6_r148_all_B_eventual_singleton_verify.py` imports the finite Port generator and exact score function from `x6_r147_post_plateau_near_fan_verify.py` in the same directory. Uses Python standard-library `Fraction` exclusively.

Actual local execution on 2026-11-23:

```text
R148 ALL-POSITIVE-B HIGH-D EXACT TWO-TO-ONE TAIL PASS
full Port-10 unoriented population 1935 zero-fixed-gap 15 dominated-zero 13
tail start 1872-min(B,136); singleton onset 2448+17B (B<=136) or 2312+18B (B>=136)
full_fraction_population_crosschecks 98
```

98 exact full-population replays cover positive fractional B, B=136, both threshold equalities, open sides, very large B and D. The continuum conclusion follows from the displayed inequalities plus R147 for the B>=136 branch, not from extrapolating samples. All evidence is author-produced; independent proof review and native Task Result remain separate.

**Next problem:** complete the `20<B<136` lower-D fan, especially the first entry/exit surfaces below `D=1872-B`, and determine how its optimizer witnesses splice into the R147 high-B fan.
