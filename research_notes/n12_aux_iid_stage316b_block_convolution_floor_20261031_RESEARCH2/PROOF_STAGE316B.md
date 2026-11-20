# Stage316-B — exact two-block infimal convolution and a 550× stronger universal three-visit public-TV floor

**Classification:** `PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED`. Research2 independent portable continuation, not a native CLAIM, Source Result, independent Driver acceptance, or P000-native X6 theorem.

**Frozen current reading (2026-10-31):** GLOBAL_KNOWLEDGE_V1 canonical `main@09284c3e3651bdfb4e92991b877ff0b1a5c70a10`, Enterprise Math canonical `main@42fae018032be0be1b496b749472ead751d624a2`; current global original P000 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`; Stage315-B authored evidence `388bd4f074dfba8a6e8ff9b9d242819822e85bee` in Draft PR #1736. GLOBAL_KNOWLEDGE_V1 ACTIVE worldview protects source/path/future-observation residuals; the present model is external and does **not** identify the binary variables with native Cell axes, triadic closure or time.

## Frozen mathematical model

S is a fair binary hidden source. Given S=s, private J copies S with probability 7/8, public W copies S with probability 3/4, and public Y is Bernoulli(p_s), all conditionally independent, p_0=1/4, p_1=3/4. The eight private histories h=(J,W,Y), ordered 000 through 111, have joint source masses 256·(Pr(S=0,h),Pr(S=1,h)):

`(63,1), (21,3), (21,3), (7,9), (9,7), (3,21), (3,21), (1,63)`.

A represented future F-access uses Bernoulli(t_h), with t_h∈[0,1] locked across future visits. Independent H-access is a fair bit. Public observation includes G=(W,Y) and future transcript; tagged observation additionally includes S and J. Presampling n F bits shows all public-history-adaptive H/F transcripts are common postprocessings of the all-F trace; the maximal public and tagged TV risks are exactly the respective all-F TVs. The exact reduction of Stage315-B proves every tagged-risk minimizer at any feasible public budget and finite n≥1 fixes the four central rates t_001=t_010=1/4, t_101=t_110=3/4. We invoke that theorem and preserve its proof scope.

For an ordered n-bit word w, let B_n(t;w)=t^{#1(w)}(1-t)^{#0(w)}, and D_n(s,t)=TV(Bern(s)^⊗n,Bern(t)^⊗n). Define two explicit functions on [0,1]^2:

```
b_n(u,v) = (1/512) Σ_{w∈{0,1}^n} |64 B_n(u;w) + 16 B_n(v;w)
                                    -72 B_n(1/4;w)-8 B_n(3/4;w)|,
c_n(u,v) = [63 D_n(1/4,u)+D_n(3/4,u)
             +9 D_n(1/4,v)+7 D_n(3/4,v)]/256.
```

Both are continuous piecewise-polynomial, with explicit rational coefficients and a finite word/sign partition for each declared n. Write `a_n=min_{[0,1]^2} b_n` and `C_n(s)=min{c_n(u,v): b_n(u,v)≤s}` for `s≥a_n` (compactness ensures attainment).

## Theorem A — the full eight-rate frontier is a scalar infimal convolution of one two-rate envelope

For every n≥1, put `d_n=D_n(1/4,3/4)` and `K_n=12 d_n/256`. For any four free rates `(t000,t100,t011,t111)`, define `(u,v)=(t000,t100)` and `(u',v')=(1-t111,1-t011)`. Exactly, with no relaxation,

```
P_n = b_n(u,v)+b_n(u',v'),
T_n = K_n+c_n(u,v)+c_n(u',v').                   (A1)
```

Consequently, for every *feasible* public-TV budget z≥2a_n the **full eight-rate** Pareto value is exactly

```
F_n(z) = min{T_n(t): t∈[0,1]^8, P_n(t)≤z}
       = K_n+ min_{s∈[a_n,z-a_n]} [C_n(s)+C_n(z-s)].   (A2)
```

Thus first-transition research needs only (i) a single two-rate semialgebraic envelope C_3(s), (ii) a scalar budget-allocation minimization, and (iii) the exact sign chambers of b_3 and c_3. One cannot infer a symmetric optimal allocation: the infimal convolution permits unequal allocations, and a nonconvex C_3 could favor a single altered outer group.

### Proof

At G=00 the true source masses are (72,8)/256, while the two private histories 000 and 100 carry total masses 64/256 and 16/256 and are represented by rates u,v. Their public TV is exactly b_n(u,v) by its definition. At G=11 the true masses are (8,72)/256, while histories 011 and 111 carry total masses 16/256 and 64/256. Complementing every future bit maps Bern(t) to Bern(1-t), and exchanges p0,p1. Therefore the G=11 residual is exactly b_n(1-t111,1-t011). The two other public groups G=01 and G=10 match word-by-word after the Stage315 central-MAP reset, so P_n is their outer-group sum.

Tagged TV separates over the disjoint (S,J,G) histories. The G=00 source mass table (63,1),(9,7) yields c_n(u,v). Complementation similarly yields c_n(u',v') for G=11. The four central histories contribute 3d_n each /256, hence K_n. This proves (A1).

The Stage315 strict-domination theorem ensures every full eight-rate constrained minimum is attained in this four-rate set; it also guarantees compactness and nonnegative costs. Given any feasible four-rate vector let s=b_n(u,v). Then a_n≤s≤z−a_n, and C_n(s)≤c_n(u,v), C_n(z−s)≤c_n(u',v') because the latter block has public TV≤z−s. This proves `F_n(z)≥` the right side of (A2). Conversely, take a minimizing s and the two two-rate minimizers defining C_n(s), C_n(z−s); concatenate the blocks by the inverse complemented-rate map. Their total public TV≤z and tagged cost is exactly the right side, proving `≤`. Continuity/compactness ensures a minimum exists, not merely an infimum. QED.

At MAP, `b_n(1/4,1/4)=c_n(1/4,1/4)=d_n/32` and thus `P_n^MAP=d_n/16`, `T_n^MAP=7d_n/64`. For n=3, `d_3=11/16`, giving exactly `P_3^MAP=11/256` and `T_3^MAP=77/1024`.

## Theorem B — quantitative public residual obstruction strengthened by factor 2,181,250/3,969

For **every** locked-port eight-rate vector `t∈[0,1]^8` and **every finite n≥3**,

```
                        P_n(t) > 5/7168 ≈ 0.0006975446.        (B1)
```

The conservative exact bound in Stage315 was `P_n≥567/446720000≈0.0000012693`; the new lower-bound constant is larger by exactly `2181250/3969≈549.57` (both are guaranteed lower bounds, not estimates of the actual minimum).

### Exact proof

It suffices to work on the public fiber G=00, whose common true/represented probability is 5/16. Conditional on G=00 the true latent Bernoulli rate has distribution

```
μ = (9/10)δ_(1/4) + (1/10)δ_(3/4),
```

while the represented rate has

```
ν = (4/5)δ_u + (1/5)δ_v
```

for arbitrary u,v∈[0,1]. Let δ be TV between their **ordered three-bit** mixture distributions. Define `m_j=E[U^j]`, `V=m_2−m_1²`, `C=m_3−3m_1m_2+2m_1³`, and `H=C²−(9/4)V³`. The represented two-atom fixed weights imply `V=(4/25)(u−v)²`, `C=−(12/125)(u−v)³` and thus `H(ν)=0` identically on the entire real square, including boundary and coincident rates. For μ, exact fractions yield

```
(m1,m2,m3)=(3/10,9/80,9/160),
V_μ=9/400, C_μ=9/1000, H_μ=567/10240000 >0.        (B2)
```

For each j=1,2,3, the event `F1=...=Fj=1` is observable from a three-bit word. Therefore `|m_j(μ)−m_j(ν)|≤δ`. Assume for contradiction that `δ≤d=1/896`. Along the straight segment joining the two raw-moment triples, `|m1−3/10|≤d` and `|m2−9/80|≤d`. The exact derivative bounds follow from the rational endpoints:

```
0 < 6(3/10-d)²−3(9/80+d)
  ≤ ∂C/∂m1 = 6m1²−3m2
  ≤ 6(3/10+d)²−3(9/80-d) < 21/100,
|∂C/∂m2| = 3m1 < 91/100,    ∂C/∂m3=1,
|∂V/∂m1| = 2m1 < 61/100,    ∂V/∂m2=1.
```

Integrating along the segment, with **rational** Lipschitz constants `L_C=53/25`, `L_V=161/100`, gives

```
|C_ν−C_μ|≤L_C δ,
|V_ν−V_μ|≤L_V δ.
```

Both V values are nonnegative (they are variances), and their magnitudes along the segment are at most `V_μ+L_V d`. The true C is positive, and `|C_ν|≤C_μ+L_C d`. Therefore

```
|H_μ−H_ν|≤L δ,
L=(2 C_μ+L_C d)L_C +(27/4)(V_μ+L_V d)^2 L_V
 =22750232429/458752000000.
```

But exact rational arithmetic gives the contradiction

```
H_μ−L d =9601171/411041792000000 >0,
```

since H_ν=0. Hence every represented G=00 conditional distribution has δ>d. The G=11 group becomes *the same* fixed-weight problem under bit complementation and source exchange, so its conditional δ also exceeds d. These public groups are disjoint and each has mass 5/16, implying

```
P_3≥(5/16)(δ_00+δ_11) > (5/8)(1/896)=5/7168.
```

Any n≥3 F trace marginalizes to the first three accesses, and TV contracts under marginalization, so P_n≥P_3. This proves (B1) for all eight real rates (the four central groups may add extra nonnegative TV and cannot erase either outer residual). QED.

## Executed evidence and limits

`REPRO_STAGE316B.py` uses only standard-library exact `fractions.Fraction`. It independently enumerates every ordered future word for horizons 1..5 and checks the full eight-hypothesis public/tagged TV against the two-block formula for five rational vectors each, confirms the MAP baselines, evaluates the mixing-weight polynomial invariant on representative rational rates, and verifies every rational endpoint/derivative/Lipschitz inequality and the strict gap in (B2). `REPRO_STAGE316B_EXECUTED_STDOUT.txt` is the executed stdout; it ends `STAGE316B_BLOCK_INFIMAL_CONVOLUTION_AND_STRONG_TV_FLOOR_EXACT_PASS`.

The all-real/all-horizon statements are supported by the analytic proofs, **not** by the finite word enumeration. The program does not compute the two-rate envelope C_3(s), the first true Pareto transition, or an independently reviewed P000 native bridge. Numerically discovered alternatives have not been promoted as certificates.

## Next exact problem

**Stage317-B:** compute and certify the two-rate lower envelope C_3(s) by exact rational sign-chamber decomposition of (u,v); then determine the first budget where the scalar infimal convolution in (A2) leaves the Stage312 single-fiber polynomial branch. Distinguish a distant competing chamber within one block from an asymmetric two-block allocation; seek a rational/algebraic strict competitor before the Stage314 one-fiber epsilon_c, or an interval certificate excluding all such competitors. A separate X6/three-dimensional-slice, ordered native-axis path, triadic force-closure, native-time/Cell-address observer-preserving map is still required before native P000 transfer.
