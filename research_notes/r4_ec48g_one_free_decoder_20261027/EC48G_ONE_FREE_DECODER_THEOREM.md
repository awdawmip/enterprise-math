# EC48G — One free decoder, collision chains, and exact seedless BRC ROC preservation

**Research status:** author-side proof and exact verification (2026-10-27 Asia/Shanghai); proposed auxiliary-model result, not a Source-native Result or an independently reviewed/promoted Enterprise Math theorem. **Research Activity:** `RA-EMR4-20261027-1035-EC48G-ONEFREE` (local researcher `EM-R004-EC48G-20261027-1035-LOCAL`, no native CLAIM).

**Frozen inputs:** GLOBAL_KNOWLEDGE_V1 `main@b4e5b0531b2d2acd9b3905dcadc0384672d5a544`, including `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, ACTIVE worldview, P000 V4/projection, math/code/BRC rules, TASK bootstrap; Enterprise Math control source `main@1c67bd8d61e22b95275b742e196df18868065a3f`, including `docs/PORTABLE_RESEARCH_PROTOCOL.md` and `research_persistence_policy.json`; previous EC48F proof/next-task source `795f9beabbd4fb10c973b3bd2976acaf76064aa4`. The EC48G mathematical question is independent author-side continuation after a live owner query returned `CONTROL_QUOTA` and session creation returned `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`).

## 1. Exact question, carrier, and model

Work exclusively with **finite strictly positive normalized real (in examples rational) two-stage BRC source laws** `p(h,y)>0`, `q(h,y)>0` on `H × Y`, each summing to one. First read history `h`, encode privately into one of `K` memory labels with conditional probabilities `π_h(m)`. Later read `y`, then declare `P` with decoder probability `u_m(y)∈[0,1]`. There is no persistent public/common random seed. The effective decision array is `w(h,y)=Σ_m π_h(m)u_m(y)`, and its ROC coordinates are `α=Σp w`, `β=Σq w`. Let `S_K` be the achievable `(α,β)` points; the complete-history set is the zonotope `Z=Σ_(h,y)[0,(p(h,y),q(h,y))]`. Set

```
K_hull = min {K: conv(S_K)=Z},
K_seed = min {K: S_K=Z}.
```

**No X6 transfer is asserted.** `h` is positive-weight branch/source provenance, `y` a later observation, and memory an intermediate observer state, not a native spatial axis, two-dimensional slice, or extra physical time dimension. `p-rq` is an auxiliary signed support functional, not a signed BRC amplitude. Exact result applies only to this observer/operation horizon.

At a critical likelihood ratio `r=p(h,y)/q(h,y)>0`, let `T_r={h: some y has p(h,y)=r q(h,y)}` and `N_r=H\T_r`. For `h∈N_r` define its forced binary row `c_h(y)=1{p(h,y)>r q(h,y)}`; let `C_r={c_h:h∈N_r}` and `c_r=|C_r|`. For `h∈T_r`, the two extremal optimal rows are

```
a_h(y)=1{p(h,y)>=r q(h,y)},
b_h(y)=1{p(h,y)> r q(h,y)}.
```

Define `A_r={a_h:h∈T_r}`, `B_r={b_h:h∈T_r}`, and `t_r=K_hull-c_r`. (Some `a_h` or `b_h` may be members of `C_r`; this is central to the proof.) `a_h=b_h` is impossible for a truly tied history; on strictly signed cells they agree, and on tied cells `a_h=1, b_h=0`.

## 2. Theorem EC48G.1 — One free decoder suffices for arbitrary tied-history multiplicity

**Theorem.** If at a critical ratio `r` the two endpoint sets satisfy

```
|A_r \ C_r| <= 1    and    |B_r \ C_r| <= 1,                   (SF_r)
```

then the *entire* exposed optimal face `F_r={x∈Z: α-rβ=max_Z(α-rβ)}` is attainable with at most `c_r+1` decoder states (and with only `c_r` if both set differences are empty). The history encoder may randomize privately; no persistent common seed is used. The number of tied histories and the number of distinct ordered collision pairs `(a_h,b_h)` are unrestricted.

**Constructive proof.** Allocate one decoder row `u_c=c∈{0,1}^Y` for each `c∈C_r`. If needed allocate a single **free row** `u_*`. When `A_r\C_r` is nonempty, its unique member is `a_*`; when `B_r\C_r` is nonempty, its unique member is `b_*`. At every phase the nontied histories encode to their fixed row `c_h`. Every tied history can encode to either endpoint row whenever that row occurs among current decoders. A stochastic encoder between two available decoder rows `v,w` implements `(1-s)v+s w`, `0≤s≤1`.

Three phases yield one continuous *ROC-coordinate* path from all `b_h` to all `a_h`:

1. **C-ending histories.** With free row held at `b_*` if it exists, process each tied history with `a_h∈C_r`, one at a time, using a private encoder interpolation from its `b_h` row (either in `C_r` or equal to `b_*`) to its `a_h∈C_r` row. Histories not yet processed stay at their `b_h`; previously processed histories stay at their `a_h`. Both endpoints obey all strict sign constraints.
2. **Shared free-row bridge.** Histories with both endpoints outside `C_r` necessarily share the *same ordered pair* `(a_*,b_*)`. All are still using the free row `b_*`. Move this single decoder row continuously from `b_*` to `a_*` by `u_*(s)=(1-s)b_*+s a_*`, keeping each such history deterministically encoded to it. Histories with `a_h∈C_r` have completed phase 1; histories with `b_h∈C_r` still use `b_h`. If no history depends on the free row in this phase, move it while unused; the effective decision array does not change.
3. **C-starting histories.** Hold the free row at `a_*` if it exists, and process each remaining tied history with `b_h∈C_r`, `a_h=a_*`, one at a time, by privately interpolating from the available decoder `b_h` to the free row `a_*`.

If one of `a_*`, `b_*` is absent, omit its irrelevant phase. If both are absent all tied histories interpolate between available `C_r` endpoints and no free state is needed. All three phases preserve `w=1` where `p>rq`, and `w=0` where `p<rq`; on tied cells every interpolation changes `w` monotonically from zero to one. For the optimal support value `V_r=Σ max(p-rq,0)`, all points of the path satisfy `α-rβ=V_r`. The path's total tied `q`-mass is a continuous nondecreasing function, starting at `0` and ending at `Q_r=Σ_{p=rq}q(h,y)`. Its image is therefore **the entire interval `[0,Q_r]`**, which parametrizes the exposed face `F_r` because all tied generators have the same slope `r`. This establishes the assertion. □

**Important distinction.** The decoder can be reconfigured between *different feasible policies* along a continuous path, and the procedure needs at most one freely variable decoder in any policy. Nothing assumes that a single policy dynamically changes its decoder after observing `h` or `y`. The interpolating path is a parameterization of attainable *points*, not a persistent seed shared across decisions.

## 3. Theorem EC48G.2 — A general sufficient criterion and the two-tied-history corollary

**Theorem.** Fix `K=K_hull`. If for **every** critical ratio `r` at least one of the following conditions holds,

```
(A) |T_r| <= K - |C_r|,    or
(B) |A_r \ C_r|<=1 and |B_r \ C_r|<=1,
```

then `K_seed=K_hull`.

**Proof.** Under condition (A), retain the `c_r` fixed non-tied decoder rows and allocate one additional decoder row per tied history. For each tied `h`, set its row to `(1-s)b_h+s a_h`; all these histories can use the *same* scalar `s∈[0,1]` because their decoder rows are distinct. This uses `c_r+|T_r|≤K` states and exactly traverses `F_r` with tied total `q`-mass `sQ_r`. Under (B), Theorem EC48G.1 uses at most `c_r+1` states. If an outside endpoint exists, the binary strict row set at an arbitrarily close noncritical threshold includes `C_r` and that outside endpoint, giving `K_hull≥c_r+1`; otherwise `c_r` decoders already suffice. Thus each exposed face is achievable by `K` states.

For completeness, the EC48A threshold criterion follows directly: at a noncritical threshold `λ`, maximizing `α-λβ` fixes a binary decision row per history. A convex combination of decoder rows that equals a binary row must use decoder rows equal to that row in every coordinate. Therefore its support maximum is attainable with `K` states exactly when the number of *distinct* strict binary rows is ≤K. Sampling all intervals between the finite critical ratios gives `K_hull`. At a critical threshold, taking a neighboring strict decision also attains the support maximum.

All nontrivial edges of positive-generator planar zonotope `Z` are the critical support faces `F_r` and their centrally reflected counterparts. Reflection follows from complementing every decoder probability `u↦1-u`, which maps `(α,β)↦(1-α,1-β)` since `Σp=Σq=1`. The remaining vertices, including `(0,0)` and `(1,1)`, are trivially reachable. Hence every boundary point of `Z` lies in `S_K`. Scaling every decoder probability by `τ∈[0,1]` scales `(α,β)` by `τ`, so `S_K` is star-shaped at `(0,0)`; every point of `Z` is on such a radial segment from `(0,0)` to a boundary point. Therefore `Z⊆S_K`, while `S_K⊆Z` by the definition of `Z`. The reverse inequality `K_hull≤K_seed` is automatic. □

**Corollary (at most two tied histories).** If `|T_r|≤2` for every critical ratio, then `K_seed=K_hull` for **all** finite strictly positive two-stage models, including cases with two distinct unabsorbed ordered transition signatures `|D_r|=2`. Indeed, set `t_r=K_hull-|C_r|≥0`. If `t_r≥2`, apply (A). If `t_r≤1`, the adjacent strict-threshold signature sets `C_r∪A_r` and `C_r∪B_r` have cardinality at most `K_hull`, forcing both set differences to have size at most `t_r≤1`, so apply (B). □

This closes the EC48F next-question for the **two-tied-history case**: an extra state is not required even when the EC48F signature-bank construction uses `K_hull+1`. For more than two tied histories, (B) can still succeed despite `|D_r|≥3`.

## 4. Exact rational witnesses, including a three-signature collision

Normalize integer arrays by their separate total sums. Use `Q_raw` consisting entirely of `2`.

### EC48G-W2 — two tied histories, two different unabsorbed pairs

```
P_raw = [[4,1], [2,1], [4,2]],     sum(P_raw)=14
Q_raw = [[2,2], [2,2], [2,2]],     sum(Q_raw)=12
```

The only critical ratios are `3/7, 6/7, 12/7`. The maximum count of distinct strict rows is `K_hull=2`. At `r=6/7`, the nontied history `h0` has `C_r={(1,0)}`. The tied histories have endpoint pairs

```
h1: (a,b)=((1,0),(0,0))
h2: (a,b)=((1,1),(1,0))
```

so `D_r` has exactly 2 different unabsorbed pairs; `a_*=(1,1)`, `b_*=(0,0)`. With decoder rows `c=(1,0)` and `u_*`, stage 1 privately moves `h1` from `u_*=(0,0)` to `c`; stage 2 moves the then-unused free decoder to `(1,1)`; stage 3 privately moves `h2` from `c` to `u_*=(1,1)`. Every point of the face is obtained from the two exact segments

```
Stage I:    alpha=4/7+t/7,  beta=1/3+t/6,
Stage III:  alpha=5/7+s/7,  beta=1/2+s/6,       0<=t,s<=1.
```

Both satisfy `alpha-(6/7)beta=2/7`; their `beta` ranges join without a gap at `beta=1/2`. Thus `K_seed=K_hull=2`.

### EC48G-W3 — THREE distinct collision pairs but only TWO memory states

```
P_raw = [[4,1], [2,1], [4,2], [2,2]],  sum(P_raw)=18
Q_raw = [[2,2], [2,2], [2,2], [2,2]],  sum(Q_raw)=16
```

Here `K_hull=2` again. At `r=8/9`, the nontied history `h0` has `C_r={(1,0)}`, while `h1,h2,h3` all have tied ratios, and

```
h1: (a,b)=((1,0),(0,0))
h2: (a,b)=((1,1),(1,0))
h3: (a,b)=((1,1),(0,0))
```

Hence `|D_r|=3` (the EC48F bank uses `|C_r|+|D_r|=4` states at that face). Yet the one-free-row construction uses exactly **2** states and traverses three consecutive segments:

```
Stage I:    alpha=4/9+t/9,   beta=1/4+t/8,
Stage II:   alpha=5/9+2s/9, beta=3/8+s/4,
Stage III:  alpha=7/9+v/9,  beta=5/8+v/8,     t,s,v in [0,1].
```

These share endpoints and each has `alpha-(8/9)beta=2/9`; their `beta` values exactly cover `[1/4,3/4]`, a face with tied mass `Q_r=1/2`. All other critical faces satisfy the same one-free criterion, proving `K_seed=K_hull=2` for this complete normalized source model. Thus the EC48F bank size is a **sufficient allocation, not a necessary memory bound**, even when three distinct unabsorbed collision signatures occur.

## 5. Executed exact verification and limitations

`EC48G_VERIFY.py` is a standalone standard-library `fractions.Fraction` checker. It derives the exact likelihood ratios, enumerates open chambers to calculate `K_hull`, constructs actual decoder rows and history-dependent stochastic encoder probabilities at five exact interpolation parameters in each phase, and asserts `0≤w≤1`, row-stochastic encoders, the forced optimal bits, exact support equality and monotonic full `[0,Q_r]` face coverage. The construction's all-parameter validity follows from the symbolic proof, not from five sample parameters.

The complete declared finite integer test box takes all `3^6+3^8=7,290` matrices `P_raw` of size `3×2` and `4×2`, with every element chosen independently from `{1,2,4}`, and fixes every `Q_raw` entry at `2`. **2,510** matrices satisfy the stated per-face sufficient conditions; for these the verifier checked **7,302** exact critical faces and **394,030** exact cell-level arithmetic assertions. There were **3,876** checked faces with `|D_r|≥2`, and **876** eligible models with maximal `|D_r|≥3`. All selected construction tests passed. The remaining 4,780 matrices are outside this particular sufficient-condition test and are **not** classified as gaps/counterexamples. This is not a numerical estimate or an exhaustive check over all positive rational inputs.

- Reproduce: `python EC48G_VERIFY.py > EC48G_REPORT.json` (Python 3 standard library).
- Arithmetic: exact rational normalization and comparison only; no floating-point rounding.
- Files: `EC48G_ONE_FREE_DECODER_THEOREM.md`, `EC48G_VERIFY.py`, `EC48G_REPORT.json`, `NEXT_TASK.md`.
- `EC48G_VERIFY.py` output SHA-256 and report SHA-256 are recorded in the associated source-commit evidence; no trust is inferred from self-reported hashes alone.
- Source-based reuse: EC48A exact noncritical signature count, EC48F transition bank and code interface, typed positive BRC provenance and support/observer semantics (`REUSE_APPLIED`); phasewise one-free decoder construction is a *narrow extension of existing EC48F verification*, classified `EXTEND_EXISTING_TOOL`, **not** a new global toolbox family. Native X6/three-dimensional-slice embedding or stopping-depth dynamics remain separate unproved transfers.

## 6. Next EC48H — genuine multi-free obstruction or universal factorization

At a critical ratio `r` with `t_r=K_hull-|C_r|≥2`, more than `t_r` tied histories and at least two distinct extra endpoint signatures on **both** sides, conditions (A) and (B) need not apply. Determine whether the two endpoint decoder configurations can always be connected by a continuous ROC-face path with only `t_r` free decoders, allowing private history-dependent encoders; if not, produce a strictly positive rational `P_raw,Q_raw` with its exact normalization, critical `r`, the complete connected-component interval witness from EC48C, and an uncovered rational open interval. Do not infer a gap merely from disconnected parameter/strategy graphs or a bank requiring more states. Preserve precise two-stage scope and no-persistent-seed semantics.
