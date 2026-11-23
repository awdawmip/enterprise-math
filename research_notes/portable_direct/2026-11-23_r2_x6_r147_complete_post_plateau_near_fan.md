# X6 R147 — Complete strict-near fan beyond the Port-10 optimizer plateau

Date: 2026-11-23 (Asia/Shanghai). Status: author analytic proof and exact integer/rational checker PASS; independent mathematical review NOT_REVIEWED.

## Frozen input and interpretation

This continues R146 [three-witness optimizer](https://github.com/awdawmip/enterprise-math/blob/488f0a8d88026dde77500dd8a61a30905a3b5314/research_notes/portable_direct/2026-11-23_r2_x6_r146_global_optimizer_three_witnesses.md), preserving the scientific pins R121 `8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd` (small-Port optimizer) and R122 `0687aa24f5402da3b35f914dd6907967a9805b94` (`x6_r122_small_port_near_exclusion_certificate.json`). P000 V5 and the ACTIVE Heartbeat World provide the native context. The statement is about the *conditional static centered-three-axis, six-pair BRC observer*, not a native X6 time dynamics or final Cell-address theorem.

Unoriented integer triples `a=(x,y,z)` obey `q(a)=max(sum(max(a_i,0)),sum(max(-a_i,0)))<=10`; identify `a` with `-a`, not multiples. There are 1,935 directions. Put `h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)`; the six ordered gaps are `g=(|h1-h0|,|h2-h0|,|h3-h0|,|h2-h1|,|h3-h1|,|h3-h2|)`. For `w=(136,B,176,D)`, set `s=(136+B,312,136+D,B+176,B+D,176+D)`, `F_w(a)=max_j g_j/s_j`, `eta=min_a F_w(a)`, and the strict `3/2`-near set `N={a:F_w(a)<(3/2)eta}`.

## Theorem R147 (complete unbounded post-plateau near-direction atlas)

For *every pair of real parameters* `B>=136`, `D>=E(B):=max(1008,1248-B)` (including equality), define

```text
P = {(1,0,0), (5,-4,1), (5,-1,0), (9,-5,1)}
b = (4,-1,0)
c = (6,-4,1)
H(B) = max(1580,1872-B)
K(B) = 18B+2312.
```

Then the entire strict-near set, with every direction understood modulo sign, is exactly

```text
N(B,D) = {c}
       union ({b} if D<K(B) else empty)
       union (P   if D<H(B) else empty).
```

In particular, `E(B)<H(B)<S(B):=12B+1496<K(B)`. Thus the complete cardinality law is

| Domain | Exact near count |
|---|---:|
| `E(B)<=D<H(B)` | 6 |
| `H(B)<=D<K(B)` | 2 |
| `D>=K(B)` | 1 |

The four old directions exit **simultaneously** at the sharp boundary `D=H(B)`; `b` exits exactly at `D=K(B)`; `c` survives throughout the whole unbounded domain. The optimizer switches from `b` to `c` at `D=S(B)` (R146, with its exceptional `B=136` tie interval), strictly between the two membership-change boundaries, **without changing the near-direction set there**. Equality at a near threshold excludes that member.

The first boundary has one kink: `H(B)=1872-B` for `136<=B<=292` and `H(B)=1580` for `B>=292`. This gives a three-cell atlas on a genuinely unbounded two-parameter domain; neither finite sampling nor a candidate-only upper bound is being substituted for the classification.

## Proof

1. **A complete population filter, independent of `B,D`.** For every Port-10 direction the second gap is `g_1=3|x+4y+10z|`. Exactly 1,890 of the 1,935 directions have `g_1>=6`; hence `F>=6/312=1/52`. By R146 `eta<=1/104`, so `F>(3/2)eta` for all 1,890. Exactly 45 remain with `g_1<=3`. Among them, exactly 37 have the third gap `g_2>=18`; using `eta<=F(c)=12/(D+136)`, these satisfy `F>=18/(D+136)>=(3/2)eta`. The remaining *eight and only eight* directions are the six named above, `u=(1,-3,1)` with `g(u)=(2,3,16,1,18,19)`, and `v=(9,-2,0)` with `g(v)=(3,3,15,0,18,18)`. All finite enumeration counts and the complete generator are in the companion exact checker.

2. **Exclude the two final outsiders for the entire continuum.** Since `D>=E(B)>=1008>720`, `F(u)>=19/(D+176)>=(3/2)*12/(D+136)>=(3/2)eta`: the middle inequality is exactly `D>=720`. For `v`, let `f_b=max(1/(B+136),11/(D+136),12/(B+D))` (the R146 score of `b`). Its first, sixth, and fifth gaps separately give
   ```text
   F(v) >= 3/(B+136)  >= (3/2)/(B+136)
   F(v) >= 18/(D+176) >= (3/2)*11/(D+136)  (D>=304)
   F(v) >= 18/(B+D)   =  (3/2)*12/(B+D).
   ```
   Therefore `F(v)>=(3/2)f_b>=(3/2)eta`. No other direction can be near.

3. **The four old directions.** At `B=136,D=1008`, direct six-gap comparison gives `F(a)=1/104` for each `a` in `P`, attained at the second gap `3/312`. All six capacities are nondecreasing in `B,D`; their second capacity stays 312. Hence `F(a)=1/104` for all four throughout `B>=136,D>=1008`. Thus `a in N` iff `eta>1/156`.

   R146 gives `eta=min(1/104,f_b,12/(D+136))`. On the specified domain `D>=E(B)`, R145/R146 give `eta=min(f_b,12/(D+136))`. Since `B>=136`, the term `1/(B+136)` is at most `1/272<1/156`; `f_b>1/156` exactly when `D<1580` or `B+D<1872`. The condition `12/(D+136)>1/156` is `D<1736`, automatically implied by either previous alternative (using `B>=136`). Consequently `eta>1/156` iff `D<max(1580,1872-B)=H(B)`, with the strict equality case excluded.

4. **The last two candidates.** `F(c)=12/(D+136)`. Whenever `eta=F(c)`, `c` is near. Otherwise `eta=f_b`, and `f_b>=11/(D+136)` gives `F(c)/eta<=12/11<3/2`. So `c` is always near. For `b`, R146 proves `b` is optimizing up to `S=12B+1496` (possibly jointly, including the `B=136` exception). For `D>=S`, its three defining ratios reduce to `F(b)=1/(B+136)` (since `D>=12B+1496>=11B+1632` for `B>=136`) and `eta=12/(D+136)`. Thus `b` is near exactly when `D+136<18(B+136)`, i.e. `D<K(B)`. Since `S(B)<K(B)`, this remains the equivalent membership condition on the full domain.

5. **Order and exact boundaries.** For `B>=136`, `E<=1112<H<=1736<S=12B+1496<K=18B+2312`. At `D=H,K` the corresponding strict inequalities become equalities and the direction(s) leave. Steps 1–4 exclude simultaneous outsiders and establish the stated exact fan.

## Exact reproducibility and limitations

Standalone checker: `research_notes/portable_direct/x6_r147_post_plateau_near_fan_verify.py`. Standard Python `fractions.Fraction`, fully enumerating 1,935 directions by the stated Port/sign rule. Executed on 2026-11-23, result:

```text
R147 POST-PLATEAU COMPLETE STRICT-NEAR FAN CERTIFICATE PASS
population 1935 g1>=6 excluded 1890 g1<=3 candidates 45
g1<=3 and g2>=18 excluded 37 two_special_excluded 2 surviving 6
old four iff D<max(1580,1872-B); b iff D<18B+2312; c always
all_fraction_population_crosschecks 238
```

The 238 full-population exact rational replay points include both boundary equalities, nearby open sides, optimizer switches, noninteger weights and large parameters. Continuous real coverage is proven by the inequalities above, relying on the already author-proven R146 optimizer formula. Independent mathematical review and any formal adoption remain outstanding.

**Next research question:** bridge `20<B<136` where R146's fixed-high-channel reduction no longer forces the same three-witness optimizer, then classify any newly entering directions around the lower-weight optimizer walls. No modification of native P000/Heartbeat ontology or formal Task control is asserted.
