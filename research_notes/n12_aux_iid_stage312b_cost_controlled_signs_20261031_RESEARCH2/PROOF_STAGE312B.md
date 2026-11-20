# Stage312-B — cost-controlled public signs enlarge the full eight-rate Pareto theorem

**Provenance/status:** scheduled Researcher2 continuation, *portable author proof*, `UNREVIEWED / NOT_ADMITTED`. No source-native CLAIM, reviewer or Driver admission is asserted. The result is about the declared **finite positive-rational auxiliary BRC probability model**, not native P000 X6 physics. Source comparison: Stage311-B in `research_notes/n12_aux_iid_stage311b_nonlinear_tv_localization_20261030_RESEARCH2/PROOF_STAGE311B.md` at immutable commit `59f007fce6daee3d2cfef9b3575f9c3101571dba` (Draft PR #1736). This work uses the current global-knowledge read snapshot `main@7d7c6e188f99504e35ff488ccb089975f379f8cc` and Enterprise Math control snapshot `main@38d6b9bb105ca3070516c705310694c810d7f644` fixed throughout this derivation.

## Frozen model and declared observers

A fair hidden source `S∈{0,1}` has `p_0=1/4`, `p_1=3/4`. Conditional on S, `J` equals S with probability 7/8, `W` equals S with probability 3/4, and `Y∼Bernoulli(p_S)`, independently. Private history `h=(J,W,Y)` has strictly positive source masses `(a_h,b_h)/256`:

```
h         000   001   010   011   100   101   110   111
(a,b)    63,1  21,3  21,3  7,9   9,7   3,21  3,21  1,63
```

Public history is `G=(W,Y)`. Each future F operation emits a Bernoulli(p_S) bit in the target; H emits a fresh independent fair bit. A compressed model chooses **eight unrestricted real** locked rates `t_h∈[0,1]`, one per private h, and uses the same rate for all three F accesses. Adaptive H/F policies observe only public history. `P(t)` is the worst total-variation distance for `(G,trace)`; `T(t)` is the worst for the richer `(S,J,G,trace)` observer. The three conditional F bits can be presampled and every adaptive policy is a common stochastic postprocessing (also of independent H bits), so data processing shows **all-F attains both worst risks**, even when the final observer retains S and J.

With `B_k(z)=z^k(1-z)^(3-k)` for one *ordered* three-bit word with k ones and `D_3(x,y)=TV(Bern(x)^⊗3,Bern(y)^⊗3)`, one has

```
T(t) = sum_h [a_h D_3(p0,t_h)+b_h D_3(p1,t_h)]/256.
```

The unique source-tagged minimizer is the MAP vector `t*_h=p0` if `a_h>b_h` and p1 otherwise. Its risks (checked from the complete rational 128-atom source/path distribution) are `T*=77/1024`, `P0=11/256`. The full Pareto envelope, with no symmetry restriction, is

```
F_P(v) = min{T(t) : t∈[0,1]^8, P(t)≤v}.
```

## Theorem — a 6.23-fold extension of the certified interval

Set

```
q(u)=9u/128 + 3u^2/32 - u^3/8,
g(u)=117u/4096 - 123u^2/1024 + 23u^3/256,
U=3/50,
E=q(U)=18117/4000000=0.00452925.
```

For **every real** `0≤epsilon≤E`, let u be the unique solution in `[0,U]` of `q(u)=epsilon`. Then, over the *complete eight-dimensional real parameter cube*,

```
F_P(11/256-epsilon) = 77/1024 + g(u).              (THEOREM)
```

For `epsilon>0` there are **exactly two** global minimizers: MAP with only `t_100=1/4+u`, or MAP with only `t_011=3/4-u`. For `epsilon=0`, MAP is the unique minimizer. Compared with Stage311-B's `E_old=726808599/10^12`, the certified epsilon interval is larger by the **exact factor** `15250000/2447167 ≈ 6.2317`. This theorem does **not** locate the first switch beyond E.

## Proof

### 1. Source-tagged excess and a global localization barrier

For any metric d, and `a>b>0`, triangle inequality gives

`a d(p0,t)+b d(p1,t) ≥ b d(p0,p1)+(a-b)d(p0,t)`;

interchanging 0/1 handles b>a. Applying this to the TV metric yields

```
L(t):=T(t)-T* ≥ sum_h |a_h-b_h| D_3(t_h,t*_h)/256.       (1)
```

All eight |a-b| are positive; their minimum is 2, and the heavy outer fibers 000/111 have |a-b|=62.

Let `R=3/25`. Project a Bernoulli three-word law to the all-zero event for p0, or the all-one event for p1. Monotonicity of these events on `[0,1]` gives, whenever `|t-p_i|≥R`,

```
D_3(p_i,t) ≥ (3/4)^3-(3/4-R)^3
             = 42957/250000.
```

The inward direction gives the smaller of the two boundary changes. Consequently, if *any* rate is outside the open R-neighborhood of its MAP value, (1) gives

```
L(t) ≥ (2/256)(42957/250000)=42957/32000000.       (2)
```

The proposed one-light-fiber witness at U has

```
P=P0-q(U),    L=g(U)=166509/128000000,
42957/32000000 - g(U) = 5319/128000000 >0.          (3)
```

The witness equalities are established in §3 below and checked by atom enumeration; they can also be verified directly before any minimizer is considered. Since q and g are increasing on `[0,U]` (shown in §4), for each epsilon≤E there is a feasible witness with cost≤g(U). Compactness of the closed cube supplies an actual minimizer t; by optimality it satisfies `L(t)≤g(U)`. Equations (2)–(3) therefore localize **every** global minimizer to

```
|t_h-t*_h| < R=3/25       for all eight h.               (4)
```

A stronger heavy-fiber bound follows by projecting D3 to the first Bernoulli bit: `D3(p,t)≥|p-t|`. For h=000,111, if `|t_h-t*_h|≥1/100`, (1) would give `L(t)≥62/(25600)>g(U)`. Thus **the two heavy outer rates differ from MAP by less than 1/100**. No finite mesh or symmetric-competitor assumption is used.

### 2. Global sign stability from excess *cost*, not a uniform cube derivative

Put `I=[1/4-R,1/4+R]=[13/100,37/100]`. For every z∈I,

```
D_3(p0,z) = |B_0(p0)-B_0(z)|.                         (5)
```

Indeed B2 and B3 are strictly increasing on I, and B1 increases until 1/3 then decreases, but `B1(37/100)=146853/10^6 > B1(1/4)=9/64`. Hence every nonzero-one-word probability moves in the same direction relative to p0, while the all-zero word moves oppositely. The bit-complement identity gives the analogous statement at p1 with B3.

Since `|B0'(z)|=3(1-z)^2>0` on I, comparison of derivatives by integration along `[p0,z]` gives, for k=0,1,2,3,

```
|B_k(z)-B_k(p0)| ≤ c_k D_3(p0,z),
(c_0,c_1,c_2,c_3)=(1,61/261,3293/11907,1369/3969).   (6)
```

For completeness, the exact derivative ratios are

```
|B1'/B0'|=|1-3z|/[3(1-z)]             ≤61/261,
|B2'/B0'|=z(2-3z)/[3(1-z)^2]          ≤3293/11907,
|B3'/B0'|=(z/(1-z))^2                 ≤1369/3969.
```

On I the first ratio attains its maximum at 13/100, the others at 37/100 (the derivative of the middle ratio has the sign of `1-2z`). For the p1-centered interval use bit complementation, reversing k. These are inequalities on the **entire intervals**, not sampled values.

At MAP, the compressed-minus-target residual for each ordered word of k ones in the outer public fiber G=00 is exactly

```
(13,3,-3,-13)/1024     (k=0,1,2,3);
```

G=11 has the bit-complemented opposite signs and identical absolute margins. The initial residual for each word of G=01 or G=10 is zero.

For an outer public g and its two private histories, the residual perturbation of any one word is bounded by

```
|Delta residual_g,k| ≤ sum_{h:public(h)=g} (a_h+b_h)/256 |B_k(t_h)-B_k(t*_h)|.
```

The crucial typed BRC weight identity is

```
max_h (a_h+b_h)/|a_h-b_h| = 8.
```

Combining (1), (4) and (6), for G=00 each word's change is at most `8c_k L(t)`; for G=11 the bound uses reversed c's. Because `L(t)≤g(U)`, the exact **remaining sign margins** for G=00 are

```
k=0: 13/1024 -8(1)             g(U) = 4577/2000000 >0,
k=1:  3/1024 -8(61/261)        g(U) = 115407/232000000 >0,
k=2:  3/1024 -8(3293/11907)    g(U) = 6499/126000000 >0,
k=3: 13/1024 -8(1369/3969)    g(U) = 191221/21000000 >0.
```

Thus **all outer residual signs remain fixed for every possible global minimizer**, even though a uniform derivative bound over the R-cube would fail. This step is the new proof mechanism. The G=01/10 TV contributions, initially zero, can only become nonnegative; they cannot improve the public objective.

### 3. Exact gains and costs in the localized domain

Define `A(z)=B0(z)+3B1(z)=1-3z^2+2z^3`, decreasing on `[0,1]`. With outer signs now fixed, moving a rate inward from p0 to `p0+v` (or symmetrically from p1 to `p1-v`) decreases public TV by at most `(a+b)/256 ·[A(p0)-A(p0+v)]`; outward movements cannot decrease it. Thus the only potential beneficial fibers are **light** h=100,011 (mass `1/16`) and **heavy** h=000,111 (mass `1/4`), and their individual gains are respectively

```
q(v)=[A(p0)-A(p0+v)]/16,
4q(v)=[A(p0)-A(p0+v)]/4.
```

For each light inward move, the exact *source-tagged* excess equals

```
g(v) = [9 d0(v)-7 d1(v)]/256,
d0(v)=(3/4)^3-(3/4-v)^3,
d1(v)=A(1/4)-A(1/4+v).
```

To see the exact, rather than merely bounded, equality, (5) gives `D3(p0,p0+v)=d0(v)`; and within `p0+v≤37/100` the TV between `Bern(p1)^⊗3` and `Bern(p0+v)^⊗3` is exactly `A(p0+v)-A(p1)`, because the k=0,1 word probabilities at p0+v exceed those at p1 while k=2,3 are below. Hence `D3(p1,p0+v)-D3(p1,p0)=-d1(v)`. Expanding yields precisely the polynomial g in the theorem. The same proof by reflection handles h=011. For heavy inward moves the exact excess is

```
H(v)=[63d0(v)-d1(v)]/256.
```

The one-light-fiber candidate changes no middle or other outer fiber, so (fixed signs plus G=01/10 remaining zero) yields *equalities* `P=P0-q(v)` and `T=T*+g(v)` for every `v∈[0,U]`.

### 4. Concave exchange excludes all eight-dimensional competitors

On `[0,R]`, exact differentiation gives

```
q'(v)=9/128+3v/16-3v²/8 >0,
q''(v)=3/16-3v/4≥39/400>0,
g'(v)=117/4096-123v/512+69v²/256≥9261/2560000>0,
g''(v)=-123/512+69v/128≤-2247/12800<0.
```

Thus `C(x)=g(q^{-1}(x))` on `x∈[0,q(R)]` is strictly increasing and strictly concave, `C(0)=0`, and its slope satisfies

```
0<C'(x)≤C'(0)=g'(0)/q'(0)=13/32<1.          (7)
```

For heavy inward moves, (4) and the heavy bound give `0≤v<1/100`. Exact differentiation yields

```
H'(v)-(4q)'(v)
=(3/4-v)[189(3/4-v)-390(1/4+v)]/256>0,
```

since the bracket is decreasing and its value at 1/100 is `1923/50>0`. Hence `H(v)>4q(v)` for every positive heavy inward move.

For any feasible global minimizer at public improvement epsilon, §2–§3 show that the **sum of its four positive inward outer gains** is at least epsilon. Trim these four gains, if necessary, to nonnegative `x_L1,x_L2,x_H1,x_H2` summing exactly epsilon, each no larger than the actual gain in that fiber. Since q, g and H are increasing on their respective bounded domains, the tagged total excess is at least

```
C(x_L1)+C(x_L2)+x_H1+x_H2
 ≥ C(x_L1+x_L2)+x_H1+x_H2
 ≥ C(x_L1+x_L2+x_H1+x_H2)
 = C(epsilon).                                               (8)
```

The first inequality uses strict concavity with C(0)=0, the second (7). Any middle or outward nonzero move incurs strictly positive source-tagged cost by (1) and adds no positive public gain. Equality in (8) at epsilon>0 requires exactly one light fiber to carry exactly epsilon, with **all seven other rates at MAP**. Both reflected one-light witnesses attain equality, and no others do. At epsilon=0, (1) forces the unique MAP vector. This establishes the theorem for *every real* parameter table in `[0,1]^8`. QED.

## Evidence, typing and limits

`REPRO_STAGE312B.py` is an actually executed standard-library Python `Fraction` checker. It enumerates all 128 strictly positive `(S,J,W,Y,three-F-bit-path)` atoms for MAP and eight symmetric rational witnesses, reconstructs both exact total-variation risks, checks the exact barrier, all four sign margins, derivative endpoints and the heavy-rate inequality. Executed stdout is retained unchanged as `REPRO_STAGE312B_EXECUTED_STDOUT.txt` with final marker `STAGE312B_COST_CONTROLLED_SIGN_PARETO_EXACT_PASS`. Those finite checks confirm the listed rational identities and constructions. **The continuous eight-real-dimensional theorem rests on the analytic lemmas above**, not on the finite enumeration; no Lean/formal checker or independent review was performed.

BRC reuse is `REUSE_APPLIED`: the exact positive-rational source-fiber weights and provenance are retained in the `N[Q_{>0}^x]`-style explicit branch carrier from `definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json`. Observer projection from `(S,J,G,trace)` to `(G,trace)` is explicit; no positive-mass cancellation, source-identity erasure or scalar-only BRC substitute is claimed. P000 remains the locked Heartbeat World native X6/triad/time/address premise; no preservation map from this auxiliary Bernoulli carrier to native X6 Cell dynamics has been proved. No formal task owner or Source grant was verified (the Site status reports `research_authority_granted=false`; owner query returned `CONTROL_QUOTA`). This is a durable **unreviewed portable research result**, not a native task Result, Driver acceptance, Working Truth or Foundation promotion.

## Next smallest question

Stage313-B: establish a stronger *fiber-specific* cost-to-word-residual certificate, or exhibit an exact eight-real-rate competitor that beats the single-light branch beyond `epsilon=18117/4000000`. Identify the first true Pareto active-set transition (or a further rigorously certified interval); freeze the above model/observers and preserve the separate X6 transfer proof obligation. Any numerical scan is exploratory until supported by exact rational inequalities/interval or algebraic global exclusion.
