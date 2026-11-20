# Stage315-B — global 8→4 source-fiber reduction and a horizon-three public-information obstruction

**Classification:** `PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED` (Research2 author; no implied native CLAIM, Result or independent Driver acceptance). Independent mathematical research in an **external finite BRC-inspired observer model**, not a derivation of P000's native X6 dynamics.

**Verified input pins (2026-10-31):** `GLOBAL_KNOWLEDGE_V1 main@1d5bd4c6be5c619a34b0566003364b34ac25e088`; Enterprise Math `main@ad49ba522a5bacb0d654e9a26dc9e62ff4a83903`; predecessor Research2 Stage314-B `aa1e868ad25cab7bf8aa2370c5b980b75c16e7ae` in Draft PR #1736. Original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. The relevant P000/ACTIVE worldview constraints retain six native spatial axes, independent time, source/path/triadic relations, and observer preservation; those are not identified with the eight binary auxiliary variables.

## Model, observers, and risks

Let `S∈{0,1}` have equal priors. Conditional on `S=s`, the binary variables `J,W,Y` are independent: `Pr(J=S)=7/8`, `Pr(W=S)=3/4`, `Y~Bern(p_s)` with `p_0=1/4,p_1=3/4`. For `h=(J,W,Y)` in increasing binary order the strictly positive joint masses `(Pr(S=0,h),Pr(S=1,h))` are `(a_h,b_h)/256`:

| h | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
|---|---|---|---|---|---|---|---|---|
| `(a,b)` | (63,1) | (21,3) | (21,3) | (7,9) | (9,7) | (3,21) | (3,21) | (1,63) |

A representation chooses one real `t_h∈[0,1]` per private `h`, **locked across all future visits**. An `F` operation emits `Bern(t_h)` versus the true source's `Bern(p_S)`; an `H` operation emits a common independent fair bit. The **public** observer sees `G=(W,Y)` and the operation/output transcript; the **source-tagged** observer also sees `(S,J)`.

Let `P_n(t),T_n(t)` be the worst total variations over public-history-adaptive strategies using at most `n` future F accesses. We may presample `n` F bits and all H randomness, because any adaptive transcript is a common Markov postprocessing; TV contracts, and all-F attains the presampled bound. Thus these risks equal total variations of `(G,F_1,...,F_n)` and `(S,J,G,F_1,...,F_n)`, respectively. This is the same reduction used in Stages 304–314 and is limited to this declared access model.

The **MAP** rates are `t_h^0=p_0` for `a_h>b_h` and `p_1` otherwise. At `n=3`, direct rational atom enumeration yields `P_3(t^0)=11/256`, `T_3(t^0)=77/1024`.

## Theorem 1 — exact full-horizon four-rate sufficiency for every public constraint

For **every integer `n≥1`**, every eight-rate vector `t∈[0,1]^8`, and the vector `r(t)` that replaces

```
t_001=t_010=1/4;    t_101=t_110=3/4
```

while retaining the other four entries, we have

```
P_n(r(t)) ≤ P_n(t),      T_n(r(t)) ≤ T_n(t).
```

The second inequality is **strict whenever any of the four replaced entries differs from its MAP rate**. Consequently, for every achievable public budget `v`, every minimizer of

```
F_n(v) = min {T_n(t): t∈[0,1]^8, P_n(t)≤v}
```

lies in the **four-dimensional** cube of rates `(t_000,t_100,t_011,t_111)` with the other four rates fixed at MAP. This is an exact **global** statement over all eight real parameters, all budgets with a feasible set, and all positive finite horizons. In particular the first full-eight-rate Pareto transition sought in Stage314 reduces, with no relaxation gap, to a four-rate transition.

### Proof

The public variable `G=(W,Y)` has four disjoint values. For `G=01`, the corresponding histories are `001` and `101`. Their total masses are `(21+3)/256=24/256` each, so when their locked rates equal `(p_0,p_1)` the represented public `n`-word law equals the true public law **word by word**: both have unnormalized mass `(24 B_w(p_0)+24 B_w(p_1))/256`. Likewise, for `G=10` the histories `010,110` have exactly the same totals and MAP rates and also give **zero** public residual at every horizon. Resetting these two disjoint public fibers to MAP removes two nonnegative summands from the public TV error; it cannot alter the `G=00` or `G=11` summands. Therefore `P_n(r(t))≤P_n(t)`.

The tagged TV separates by private history: letting `D_n(a,b)` denote TV between `Bern(a)^{⊗n}` and `Bern(b)^{⊗n}`, its contribution for `h` is

```
[ a_h D_n(p_0,t_h) + b_h D_n(p_1,t_h) ] / 256.
```

If `a_h>b_h`, the triangle inequality gives

```
a_h D_n(p_0,t_h)+b_h D_n(p_1,t_h)
 ≥ b_h D_n(p_0,p_1) + (a_h-b_h)D_n(p_0,t_h).
```

Since `n≥1`, `D_n(p_0,t_h)=0` exactly when `t_h=p_0`, so the minimum is **unique** at `p_0`. If `b_h>a_h`, exchange labels and obtain the unique minimum at `p_1`. All four central histories have unequal source masses. Hence resetting any non-MAP central rate strictly lowers tagged TV and establishes the second inequality. The continuous feasible set is compact; an optimum exists, and strict tagged improvement prohibits non-MAP central rates in any optimum. QED.

## Theorem 2 — an explicit universal three-visit public-TV floor

For **every** `t∈[0,1]^8` and every integer `n≥3`,

```
                  P_n(t) ≥ 567 / 446720000 > 0.          (2)
```

Thus the full eight-rate **deterministic locked-port class** cannot produce an exact public three-visit quotient, even if the observer never sees the true source. The lower bound is deliberately conservative, is rational, and has **no optimization or numeric grid dependency**.

### Proof: a two-atom rate-mixture invariant and its TV stability

Condition on `G=00`. This public event has total mass `80/256=5/16`. Under the true process the (latent) Bernoulli rate is distributed as

```
                 μ = (9/10)δ_(1/4) + (1/10)δ_(3/4),
```

whereas under the represented process, for arbitrary `t_000,t_100`, it is distributed as

```
                 ν = (4/5)δ_(t_000) + (1/5)δ_(t_100).
```

Let `M_j=E[U^j]`, `j=1,2,3`, for such a two-rate mixing measure on `U∈[0,1]`. The observable three-bit law determines these moments because `M_j=Pr(F_1=...=F_j=1 |G=00)` for `j≤3`. Define `V=M_2-M_1²` (rate variance), `C=M_3-3M_1M_2+2M_1³` (third central moment), and `H=C²-(9/4)V³`.

For any two-point mixing measure with fixed weights `(4/5,1/5)` and any real rates, writing their difference `d` gives `V=(4/25)d²`, `C=±(12/125)d³`, hence **identically** `H(ν)=0`, including coincident or boundary rates. (The sign of `C` depends on which rate is larger.) For the true measure,

```
V(μ)=9/400,   C(μ)=9/1000,
H(μ)=(9/1000)^2-(9/4)(9/400)^3 = 567/10240000.
```

Let `δ=TV(Law_μ(F_1,F_2,F_3),Law_ν(F_1,F_2,F_3))`. Each moment `M_j` is the probability of a three-bit event, so `|ΔM_j|≤δ`. Since all raw moments belong to `[0,1]`,

```
|ΔV|≤3δ;     |ΔC|≤13δ.
```

For every probability distribution on rates in `[0,1]`, `0≤V≤1/4` (because `U²≤U`) and `|C|≤1` (because `C=E[(U-EU)^3]`). Accordingly,

```
|Δ(C²)|≤26δ,
(9/4)|Δ(V³)|≤(9/4)*3*(1/4)^2*(3δ)=81δ/64.
```

Thus `|H(μ)-H(ν)|≤(1745/64)δ`. Since `H(ν)=0`,

```
δ_00 ≥ (567/10240000)*(64/1745) = 567/279200000.
```

For `G=11`, the source weights reverse and the true rate mixture is `(1/10)δ_(1/4)+(9/10)δ_(3/4)`. Its variance and squared third central moment, hence `H`, are identical; the representation again has two fixed weights `(1/5,4/5)`, for which `H=0`. Therefore `δ_11≥567/279200000` too. Since the public marginal `Pr(G=g)` is identical in the true and represented systems and both outer groups have probability `5/16`, public TV decomposes by disjoint `G`:

```
P_3(t) = Σ_g Pr(G=g) δ_g
       ≥ (5/16)(δ_00+δ_11)
       ≥ (5/8)*(567/279200000) = 567/446720000.
```

Marginalizing any `n≥3` trace to its first three bits is a Markov map, so data processing gives `P_n(t)≥P_3(t)` for the same locked rate vector. This proves (2). QED.

## Corollary — three visits are the first horizon that can force a public residual

The lower bound cannot hold at one or two accesses: choose the **entirely rational** port vector with central four rates at MAP and

```
t_000 = 9/40,  t_100 = 3/5,
t_011 = 2/5,   t_111 = 31/40.
```

In `G=00`, the represented rate mix `(4/5)δ_(9/40)+(1/5)δ_(3/5)` has the same first two moments `M_1=3/10,M_2=9/80` as the true `(9/10,1/10)` mix. `G=11` is its bit complement; the two central public groups already match exactly. An ordered `n≤2` Bernoulli-mixture law is completely determined by moments up to order `n`. Hence **`P_1=P_2=0`**, while direct exact 128-atom enumeration returns

```
P_3 = 63/6400,    T_3 = 861051/8192000.
```

This explicit construction also independently corroborates the horizon-three moment obstruction. Its tagged risk is not claimed Pareto-optimal.

## Actual verification and limits

`REPRO_STAGE315B.py` uses standard-library `Fraction` and complete enumeration of the 128 positive source/private-history/ordered-three-bit atoms. It independently computes MAP TV, the rational two-visit exact representation, the polynomial moment invariant and its exact rational lower-bound constants. It tests central-MAP reset on several rational rate assignments at horizons 1–4. Actual output is preserved in `REPRO_STAGE315B_EXECUTED_STDOUT.txt` and ends `STAGE315B_UNIVERSAL_FOUR_FIBER_AND_MOMENT_OBSTRUCTION_EXACT_PASS`. These finite tests are **cross-checks**; the quantifiers over all real locked rates, all feasible budgets and all finite `n` follow from the analytic proofs above. This is not a Lean proof or a native physical calibration.

**BRC reuse:** the theorem explicitly retains positive source/label joint mass and distinguishes public vs source-tagged observer fibers. It gives an exact projection certificate (`8→4` for a declared public constraint), and a certified nonzero third-order residual for the remaining two outer observation fibers. Neither result erases original source relationships in the native model. The unchanged P000 transfer obligation is a typed embedding into X6 paths, triadic closure, native time and registered Cell-address semantics that preserves the declared future observer; there is no such embedding supplied here.

**Next exact question (Stage316-B):** Prove the first global Pareto transition in the remaining four-rate cube `(t_000,t_100,t_011,t_111)` or give a rational/algebraic four-rate competitor before the Stage314 one-fiber cusp `epsilon_c`. Use this reduction before any eight-variable interval exhaustion; retain both observer errors and exact Source histories. A complementary useful target is sharpening the conservative positive public-TV floor using a four-variable rational interval certificate.
