# X6 R146 — complete three-witness Port-10 six-gap BRC optimizer for the unbounded B,D quadrant

Date: 2026-11-23 (Asia/Shanghai). Status: author exact finite integer certificate + analytic proof PASS; independent mathematical review NOT_REVIEWED.

## Scope and immutable scientific input

Continue R145 at `awdawmip/enterprise-math@bf0d90f0fb41a734aa90ea265d7068e270a1ca2f:research_notes/portable_direct/2026-11-23_r2_x6_r145_sharp_optimizer_plateau_B_ge_136.md` using its original R121/R122 pins:
- `awdawmip/enterprise-math@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd:research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md`.
- `awdawmip/enterprise-math@0687aa24f5402da3b35f914dd6907967a9805b94:research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json`.

P000 V5 and Heartbeat World remain the native basis; this is a **conditional static centered-three-axis joint BRC observer statement** within the X6 research setting, not a native time-evolution, physical residual or final Cell address result. No π, trigonometry or classical numerical fallback is used.

An unoriented direction is a nonzero integer triple `a=(x,y,z)` with `q(a)=max(sum positive components, sum absolute negative components)<=10`, identifying only `a` with `-a`, not nonzero multiples. There are exactly 1,935 such directions. Set `h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)`, and let `g=(|h1-h0|,|h2-h0|,|h3-h0|,|h2-h1|,|h3-h1|,|h3-h2|)` (the fixed ordered six pair gaps). For `w=(136,B,176,D)`, `B>=136,D>=528`, capacities are `s=(136+B,312,136+D,B+176,B+D,176+D)`. Define `F(a)=max_j g_j/s_j` and `eta_10=min_a F(a)`.

## Theorem R146 — global exact optimizer formula

For **every pair of real parameters** `B>=136, D>=528`,

```text
eta_10(B,D) = min {
  1/104,
  max(1/(136+B), 11/(136+D), 12/(B+D)),
  12/(136+D)
}.
```

Thus the global optimizer for all 1,935 Port-10 directions is determined by only **three fixed witness vectors**:

```text
a0=(9,-5,1)       g=(0,3,6,3,6,3)           F(a0)=1/104
b =(4,-1,0)       g=(1,0,11,1,12,11)        F(b)=max(1/(136+B),11/(136+D),12/(B+D))
c =(6,-4,1)       g=(0,0,12,0,12,12)        F(c)=12/(136+D)
```

The formula is a complete unbounded two-parameter result, not a finite-window extrapolation.

### Post-plateau exact winning-direction fan

Put `Dopt(B)=max(1008,1248-B)` (the R145 plateau boundary). For `D>Dopt(B)`, `eta<1/104`. Then:
- If `B>136`, the **unique** optimizer is `b` for `D<12B+1496`, both `b,c` tie at `D=12B+1496`, and the **unique** optimizer is `c` for `D>12B+1496`.
- If `B=136`, both `b,c` optimize for `1112<D<=3128`, and only `c` optimizes for `D>3128`.
At plateau equality `D=Dopt(B)`, further optimizers may tie at score `1/104`; the above complete optimizer-membership assertion concerns the strict post-plateau region.

## Exact proof

1. **High fixed-channel population.** `g_1=|h2-h0|=3|x+4y+10z|`. The exact enumeration of the prescribed Port-10 integer directions produces **1,920** directions with `g_1>=3`. Since `s_1=312`, every one satisfies `F>=3/312=1/104`, uniformly in `B,D`.

2. **Small fixed-channel population.** The remaining exactly **15** directions have `g_1=0`. They include `b,c`. For the remaining 13, coordinate-by-coordinate `g(a)>=g(b)` and `g(a)>=g(c)`; their `g_2` are all at least 22, versus `g_2(c)=12`. This is an exact finite integer dominance certificate; the companion verifier constructs all 1,935 directions and checks it directly. Consequently their scores cannot beat either `b` or `c`.

3. **Fixed ceiling witness.** The exact gaps for `a0` are `(0,3,6,3,6,3)`. At `B=136,D=528`, all six ratios are `<=1/104` and the fixed second ratio is exactly `3/312=1/104`. Other capacities are nondecreasing in the allowed quadrant. Therefore `F(a0)=1/104` everywhere in the quadrant.

4. **Global equality and simplification.** Every direction either has `F>=1/104` (1,920 cases), or is one of the two candidates `b,c`, or is componentwise dominated by both. Therefore `eta=min(F(a0),F(b),F(c))`. With `B>=136`, the dominated denominator ratios in `F(b)` are `1/(B+176)` and `11/(D+176)`, and in `F(c)` they are `12/(B+D),12/(D+176)`; the stated formula follows.

5. **Sharp post-plateau transition.** R145's exact boundary also follows from the formula. Past the plateau the `1/104` witness is above the optimum, and the 1,920 fixed-channel directions cannot tie. The other 13 have `F(a)>=22/(136+D)>12/(136+D)=F(c)>=eta`, so only `b,c` can optimize. Write `t=12/(136+D)=F(c)`. The other two D-dependent terms of `F(b)` are below `t` for `B>136`, while `1/(B+136) <,=,> t` precisely as `D <,=,> 12B+1496`. This proves unique/tied winning regions for `B>136`. At `B=136`, `12/(B+D)=t` and `F(b)=max(1/272,t)`, giving the stated exceptional tie interval.

## Validation and continuation

Exact standalone Python verifier: `research_notes/portable_direct/x6_r146_global_optimizer_reduction_verify.py`, tested with Python standard-library `Fraction` on 2026-11-23. Report:
```text
R146 EXACT THREE-WITNESS GLOBAL PORT-10 OPTIMIZER PASS
population 1935 fixed_lower_bound_directions 1920 zero_pair_directions 15 dominated_zero_pair 13
optimizer_candidate_witnesses (9, -5, 1) (4, -1, 0) (6, -4, 1)
exact_fraction_full_population_crosschecks 86
switch_for_B_gt_136 D=12 B + 1496; below b, tie at wall, above c
```

Arithmetic is exact and finite-population coverage is certified by the stated generator and integer dominance tests; continuum coverage follows from the proved pointwise inequalities. The 86 full-population rational replays crosscheck boundaries but are not the proof of real-parameter coverage. Independent mathematical review and native-time dynamics are not claimed.

Next scientific question: classify **all strict 3/2 near-direction memberships** across the post-plateau `B>=136,D>Dopt(B)` fan, especially changes at `D=12B+1496`, and then bridge `20<B<136`. Preserve the same R121/R122 scientific pins; no formal Result/Review or CLAIM is inferred from this Source publication.
