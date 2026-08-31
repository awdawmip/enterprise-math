# R025 Multi-Layer Collapse Policy Dynamics and Precision-Exponent Phase Atlas — Research Return

Researcher-ID: `EM-R025-1B6E63`  
Task: `RS-R025-MULTILAYER-COLLAPSE-POLICY-DYNAMICS-ATLAS`  
Taskbook source: `e3cf4892b642d65f70f766eb517584cdd8a9a0eb`  
Status: `MULTILAYER_COLLAPSE_LAWS_FOUND / PRECISION_EXPONENT_PHASE_ATLAS_FROZEN / POLICY_DIFFERENCES_CLASSIFIED / UNBIASED_STOCHASTIC_COLLAPSE_LAW_FOUND / ALL_ENDPOINTS_RECOALESCENCE_REGIME_FOUND / DATASET_CHECKED / NOT_CANONICAL`

## 0. The eight required answers

| # | Question | Answer | Evidence status |
|---|---|---|---|
| 1 | What is the long-run gap between all-down and all-up? | Under identity precision lifts, all-down and all-up are the exact pointwise lower/upper envelopes of every endpoint-selector trajectory at every layer. Their terminal difference is the exact reachable endpoint-envelope width. There is no schedule-independent scalar closed form because phase and exponent/refinement words feed back into later basins. | `EXACT_PROVED_OR_DERIVED`; 240,480 exact small-box layer checks, 0 violations |
| 2 | Are nearest and farthest exact duals/complements? | Yes **one step**: they choose opposite endpoints, `|e_near|+|e_far|=G`, and `near+far=L+U`. Integer p-power basins have odd gap, so midpoint ties never occur. Multi-layer affine complementarity does not persist because the two outputs enter different later basins; exact later recoalescence occurs. | `EXACT_PROVED_OR_DERIVED`; 31,031 no-midpoint checks; 2,308 near/far recoalescence cases in reference box |
| 3 | Does 50/50 pseudorandom collapse have systematic bias? | Yes. For every nonexact input, `E[S_50]-n=G/2-d`. Because `G` is odd on the natural-state basin, this drift is **never exactly zero** at a nonexact integer state. The sign is state-phase dependent, so the bias is not uniformly upward or downward, but it is structurally nonzero. | `EXACT_PROVED_OR_DERIVED`; 150,015 exact one-step checks |
| 4 | Is distance-weighted stochastic collapse genuinely unbiased multilayer? | Yes for the pure identity precision tower. With `P(U)=d/G`, `P(L)=u/G`, `E[S|n]=n`, so the normalized physical state is a martingale for arbitrary deterministic exponent/refinement schedules. `Var(S|n)=d u`, and terminal variance is the sum of expected `d_t u_t/M_t^2` increments. | `EXACT_PROVED_OR_DERIVED`; 18,180 exact multilayer distribution cases, 0 violations |
| 5 | What does ×2 / ×10 precision do to error/spread? | There are two scales. **Inside one fixed root-index plateau**, basin physical width is exactly `G/M`, so ×2 halves it and ×10 divides it by ten. Across many plateau crossings, the sawtooth envelope follows `M^{-1/p}`: approximately ×`2^{-1/p}` or ×`10^{-1/p}`. Thresholds `Mx=(k+1)^p` create upward sawtooth jumps. | `EXACT_PROVED_OR_DERIVED`; exact plateau identity + binomial bounds; 60 cross-precision families through p=32 |
| 6 | What happens from p to p+1? | Root index never increases with p and enters the sparse `k=1` phase exactly when `n<2^p`. But gap, nearest/farthest error, and stochastic variance are **not monotone** in p: exact-power hits and root-index phase changes cause both increases and drops to zero. | `EXACT_PROVED_OR_DERIVED`; 310,031 root-monotonic checks, plus minimal increase/decrease witnesses |
| 7 | Is mixed-exponent order defect predictable? | Yes, but the correct classifier is **policy algebra × refinement insertion × exponent divisibility**, not divisibility alone. At `r=1`, DOWN has the existing divisibility commutation law and UP has the dual upper-closure law. Refinement can break both. NEAREST/FARTHEST can already fail for comparable exponents with `r=1`. | `EXHAUSTIVE_FINITE_CONFIRMED + EXACT SUBLAWS`; 85,017 UP comparable checks, 756 pair-regime table rows, minimal witnesses frozen |
| 8 | Does ALL_ENDPOINTS explode or recoalesce? | Both, separated by an exact phase law for constant `p,r`. If `r=a^p`, refinement is aligned and freezes after the first collapse. If `1<r<2^p`, support becomes a contiguous root-index interval and recoalesces heavily with subbinary growth. If `r>2^p` and `r` is not a p-th power, every positive parent remains ambiguous and different parents have disjoint child pairs, so cardinality doubles exactly with zero recoalescence. | `EXACT_PROVED_OR_DERIVED`; 431,361 funnel interval attacks + 179,140 binary-regime checks, 0 violations |

---

## 1. Exact model implemented

The executable laboratory is `experiments/r025_multilayer_collapse_atlas.py`.

For every integer state `n>=0` and exponent `p>=2`, it computes exact integer root index `k`, endpoints

`L=k^p`, `U=n` if exact and `(k+1)^p` otherwise,

plus `G=U-L`, `d=n-L`, `u=U-n`, and phase `d/G` as `fractions.Fraction` when nonexact.

Every layer explicitly carries `M_t`. A refinement ratio `r_t` performs the exact lift

`M_(t+1)=r_t M_t`, `s_(t+1)=r_t y_t`,

so normalized physical value is unchanged by the lift itself. The engine implements all frozen policies:

- `ALWAYS_DOWN`
- `ALWAYS_UP`
- `NEAREST`
- `FARTHEST`
- counter-based `PRNG_50_50`
- exact-rejection sampled `STOCHASTIC_UNBIASED`
- both alternating phases
- rational `PHASE_THRESHOLD(alpha)`
- exact set-valued `ALL_ENDPOINTS/BRC`

No hidden global RNG state is used. The probability theorem layer is additionally implemented by exact distribution propagation, independent of pseudorandom sampling.

### Dataset scale

- exhaustive deterministic reference: `n0=0..500`, `p=2..6`, `r=1..12`, depth prefixes `1..8` represented by full depth-8 paths: **240,480 exact layer-prefix rows**;
- compressed full reference raw dataset: **240,480 rows**, SHA-256 `ee5ebd11680ac9774496578af5629eb02f01429ba2a004bab3aeee0291cd1cc5`;
- broad deterministic sweep: **56,496 trajectories / 1,694,880 layer-equivalent operations**, `p=2..16` plus `17,20,24,28,32`, depths `8,16,32,64`, base ratios `2,3,4,5,8,9,10,16`, plus `2^p-1,2^p,2^p+1`;
- exact unbiased multilayer probability attack: **18,180 cases**;
- exact one-step random formula attack: **150,015 states**;
- fixed-family stochastic-observability p-sweep: `n0=1000,r=3,depth=16`, `p=2..32` probes;
- random implementation raw terminals: **10,240 records** = 5 cases × 2 policies × 1,024 seeds;
- BRC interval-funnel attack: **431,361 root-interval cases**;
- BRC binary-regime attack: **179,140 local/trajectory checks**;
- widest directly enumerated ALL_ENDPOINTS support: **4,096** at depth 12;
- broad sweep maximum integer bit length: **2,081 bits**.

The large raw reference file is streamed and compressed; it is not retained as a giant in-memory table.

---

## 2. H1/H2: endpoint envelope and physical monotonicity

### R025-LAW-001 — Endpoint envelope

Assume every layer applies the same monotone operation to every branch (identity in the main baseline), then a p-power lower selector and upper selector are monotone functions of their input. If at layer `t`:

`D_t <= z_t <= U_t`,

then after the common monotone operation, endpoint selection, and positive integer lift, the inequality remains. Therefore:

`ALL_DOWN_t <= ANY_ENDPOINT_SELECTOR_t <= ALL_UP_t`.

Because ALL_ENDPOINTS literally retains every legal endpoint word, its minimum and maximum are attained by the all-down and all-up words.

Reference attack: 240,480 layer-prefix checks, 0 H1 violations.

### R025-LAW-002 — Identity-tower monotonicity

For identity operation:

- DOWN gives `y_t <= s_t`, so `y_t/M_t <= s_t/M_t`; the lift preserves the latter physical value. Hence normalized trajectory is nonincreasing.
- UP gives `y_t >= s_t`, hence normalized trajectory is nondecreasing.

This law is **not operation-free**. `PHYSICAL_ADD_1` and `INTEGER_SCALE_2` both provide immediate counterexamples to raw DOWN nonincrease because the operation itself increases the state. H1 survives these tested operations because they are monotone; H2 does not.

---

## 3. H3 plus a new parity law: nearest/farthest

For a nonexact basin `L<n<U`, the nearest selector chooses one endpoint and farthest chooses the other. Therefore exactly:

`|e_near|+|e_far| = d+u = G`,

`S_near(n)+S_far(n)=L+U`.

### R025-LAW-014 — No integer midpoint

A stronger integer fact makes the tie convention irrelevant:

`G=(k+1)^p-k^p` is always odd.

Reason: one of `k,k+1` is even and the other odd; their positive powers preserve parity, so their difference is odd. Thus `d=u=G/2` cannot hold for integer `d,u`.

Consequences:

1. NEAREST and FARTHEST always select opposite endpoints on every nonexact natural state.
2. `PHASE_THRESHOLD(1/2)` is **exactly identical to NEAREST** on this natural-state model, regardless of the threshold equality rule.
3. Midpoint tie-up/tie-down variants are unreachable unless the state space is extended beyond integers.

Multi-layer paths are not affine complements because the first opposite outputs enter distinct next basins. They may later recoalesce. In the reference box, 2,308 parameter sets exhibited later near/far recoalescence; e.g. `n0=5,p=3,r=2` recoalesces at state `8` after the first lift/collapse feedback.

---

## 4. H4/H6 killed: p-power scale factors create microphases

### H4 p-power covariance is false

The candidate

`S_p(a^p n)=a^p S_p(n)`

fails for every geometric policy tested. Minimal witnesses include:

| Policy | p | a | n | left | right |
|---|---:|---:|---:|---:|---:|
| DOWN | 2 | 2 | 3 | `S_2(12)=9` | `4 S_2(3)=4` |
| UP | 2 | 2 | 2 | `S_2(8)=9` | `4 S_2(2)=16` |
| NEAREST | 2 | 2 | 2 | `9` | `4` |
| FARTHEST | 2 | 2 | 2 | `4` | `16` |

### R025-LAW-016 — exact scale microphase subdivision

The correct replacement is:

If `k=floorRoot_p(n)`, then for every integer `a>=1`,

`floorRoot_p(a^p n) = a k + j`

for a unique integer `0<=j<a`.

Proof: multiply the basin inequality by `a^p`:

`(ak)^p <= a^p n < (a(k+1))^p`.

So the scaled input does not stay in one scaled basin; it can occupy any of the `a` root-index microphases `ak,...,ak+a-1`. Exhaustive attack: 98,049 `(p,a,n)` cases, 0 bound violations.

### H6 p-power-free refinement kernel is false

Writing `r=a^p d` does **not** make `a` dynamically invisible. The p-power factor is exactly the resolution that exposes the microphase above. Minimal examples use `p=2,r=8=2^2*2`:

- DOWN at `k=2`: `S_2(8*4)/8=25/8`, but `S_2(2*4)/2=2`.
- UP at `k=1`: `9/8` versus `2`.
- NEAREST at `k=1`: `9/8` versus `1/2`.
- FARTHEST at `k=1`: `1/2` versus `2`.

A corrected asymptotic statement does survive: as the p-power scale factor `a` grows, geometric endpoint error after normalization is bounded by one consecutive p-power gap divided by `a^p`, hence decreases at `O(1/a)` for fixed underlying state. The factor is therefore **refining**, not removable.

---

## 5. H5/H7: aligned freeze and the sawtooth precision law

### R025-LAW-005 — aligned precision freeze

If exponent is constant `p` and every refinement is `r_t=a_t^p`, then after the first collapse output `k^p`, the next input is

`a_t^p k^p=(a_t k)^p`,

an exact p-th power. Every subsequent collapse is a no-op. This holds for every endpoint selector because every endpoint is itself a p-th power.

Reference attack: 240,480 H5 layer-prefix checks, 0 violations.

### R025-LAW-020 — plateau-then-jump precision law

Fix exact physical rational `x>0` and choose only precisions with integer `Mx`. Root index `k` is constant exactly on

`k^p <= Mx < (k+1)^p`.

Inside that plateau, the p-power basin width in physical units is

`W=((k+1)^p-k^p)/M = G_k/M`.

Thus inside a plateau:

- doubling `M` halves `W` exactly, if both points stay on the plateau;
- multiplying `M` by 10 divides `W` by 10 exactly, under the same condition.

At a root-index threshold, `G_k` jumps to `G_(k+1)`, producing a sawtooth. The smooth `M^{-1/p}` law is the large-scale envelope, not the exact finite trajectory.

Using

`p k^(p-1) <= (k+1)^p-k^p <= p (k+1)^(p-1)`

and `k^p <= Mx < (k+1)^p` yields

`W = p x^((p-1)/p) M^(-1/p) (1+o(1))`.

This also explains why high-p regressions over finite precision windows can look very unlike `-1/p`: they may not traverse enough root-index plateaus.

---

## 6. H8: exact high-exponent sparse phase

For fixed integer coordinate `n>0`, `floorRoot_p(n)` is nonincreasing in `p`.

For `n>1`, the first exponent with root index `1` is exactly

`p0 = bit_length(n) = floor(log2 n)+1`,

because `k_p=1` iff `1<=n<2^p`.

In the `k=1` phase, the endpoint geometry becomes explicit:

`L=1`, `U=2^p`, `G=2^p-1`, `d=n-1`, `u=2^p-n`.

So policy sensitivity is not merely qualitative: the DOWN-UP spread grows exactly as `2^p-1` while the coordinate remains in this phase.

However, the following are not monotone in p globally:

- selector gap (which is zero at exact powers under the frozen endpoint convention),
- nearest error,
- farthest error,
- stochastic variance.

Minimal direction changes include:

- gap increases: `n=2`, p 2→3: `3→7`;
- gap decreases: `n=8`, p 2→3: `5→0` because 8 becomes an exact cube;
- nearest error increases: `n=3`, p 2→3: `1→2`;
- nearest error decreases: `n=7`, p 2→3: `2→1`.

Thus the exponent atlas is a **root-index plateau/jump atlas**, not a monotone one-dimensional curve.

---

## 7. H9–H11: random versus truly unbiased stochastic collapse

### 7.1 50/50 is structurally phase-biased

For a nonexact input:

`E[S_50]=(L+U)/2`,

so

`E[S_50]-n = G/2-d`.

Since natural p-power gap `G` is odd, a nonexact integer state can never sit at the midpoint. Therefore uniform endpoint random is **never exactly locally unbiased** in this model.

This matters dramatically in the high-p `k=1` phase: 50/50 places half the mass at `2^p`, so expected local output is `(1+2^p)/2`, an exponentially large upward target relative to fixed small `n`.

### 7.2 distance weighting is exactly unbiased

For

`P(U)=d/G`, `P(L)=u/G`,

one step gives

`E[S|n]=(uL+dU)/G=n`,

and

`Var(S|n)=d u`.

Since integer lift preserves normalized physical value exactly, the identity-tower normalized state `X_t` is a martingale:

`E[X_(t+1)|F_t]=X_t`.

The martingale differences have zero conditional mean, so for deterministic initial state:

`Var(X_T)=sum_t E[d_t u_t / M_t^2]`.

The exact distribution propagator attacked 18,180 small multilayer cases and found no mean or variance-decomposition violation.

### 7.3 R025-LAW-021 — stochastic observability barrier

A new distinction appears at high exponent: **unbiased in law can become almost impossible to observe by finite Monte Carlo**.

Already in one `k=1` step:

`P(U)=(n-1)/(2^p-1)`,

`Var(S)=(n-1)(2^p-n)`.

For a sample mean of `N` independent realizations, the relative RMS error is exactly

`sqrt(Var(S)/N)/E[S]`.

Therefore reaching relative RMS target `epsilon` requires

`N >= Var(S)/(epsilon^2 n^2)`.

At fixed `n`, this is `Theta(2^p)` already for one step.

The multilayer martingale can amplify this much more strongly. For the fixed exact family `n0=1000, r=3, depth=16`:

| p | exact mean | CV | exact P(final < mean) | N for 10% relative RMS (display) |
|---:|---:|---:|---:|---:|
| 2 | 1000 | 0.0367 | 0.4986 | 0.135 |
| 4 | 1000 | 0.480 | 0.5862 | 23.0 |
| 8 | 1000 | 7.75 | 0.9217 | 6.01e3 |
| 12 | 1000 | 262.7 | 0.99848 | 6.90e6 |
| 16 | 1000 | 2.42e4 | 0.999980 | 5.87e10 |
| 20 | 1000 | 4.05e6 | 0.999999625 | 1.64e15 |
| 24 | 1000 | 8.26e8 | 0.999999892 | 6.81e19 |
| 32 | 1000 | 4.24e13 | 0.999999999984 | 1.80e29 |

All means and variances underlying this table are stored as exact integers/rationals; CV and sample-size columns are display conversions only.

This resolves an apparent paradox in finite seed tests. A 1,024-seed unbiased sampler can show a mean far from 1000 at `p=16` without any implementation bias: rare very large upper events carry the conserved expectation. The correct diagnostics must therefore separate:

1. exact law correctness;
2. exact variance/sample complexity;
3. finite-seed empirical convergence.

---

## 8. H12: mixed exponent order defects

The order defect observable is

`D_(p,q) = output(p then q) - output(q then p)`

in normalized physical units after the same refinement schedule.

### DOWN

At `r=1`, canonical collapse commutation survives when `p|q` or `q|p`. Minimal incomparable witness: `n=8,(p,q)=(2,3)` gives `1` versus `4`.

Inserting a refinement can destroy comparable commutation. Minimal frozen witness: `n=1,r=4,(2,4)` gives `1/4` versus `1`.

### UP: a dual closure law

Define `U_p(n)` as the least p-th power `>=n`. If `p|q`, q-th powers are a subset of p-th powers. `U_p` and `U_q` are closure operators onto nested sets, hence

`U_p(U_q(n))=U_q(n)`

and, by monotonicity plus nesting,

`U_q(U_p(n))=U_q(n)`.

So comparable UP operators commute at `r=1`. An 85,017-case attack through `n<=5000`, exponents `<=10` found zero violations.

Refinement again breaks this: `n=1,r=2,(2,4)` gives `8` versus `2`.

### NEAREST / FARTHEST

Distance selectors are neither interior nor closure operators. They can fail even under comparable exponents with no refinement:

- NEAREST: `n=7,r=1,(2,4)` gives `16` versus `1`;
- FARTHEST: `n=3,r=1,(2,4)` gives `1` versus `16`.

So the useful phase classifier is:

`policy algebra type × refinement insertion × exponent divisibility`.

---

## 9. H13 strengthened to an exact BRC trichotomy

For constant exponent `p`, constant refinement `r`, identity operation, and a positive p-power support state `k^p` after collapse, define

`c = r^(1/p)`.

After lift the exact real root coordinate is `c k`. If `r` is not a p-th power, `ck` is never an integer for positive integer `k`; each parent is therefore ambiguous and creates the root-index pair

`{ floor(c k), floor(c k)+1 }`.

This yields three exact regimes.

### Regime A — aligned freeze: `r=a^p`

`r k^p=(ak)^p` is exact. No new branch is created after refinement. This includes the threshold `r=2^p` and other perfect-pth-power islands such as `(p,r)=(2,9)`.

### Regime B — interval funnel: `1<r<2^p`

Then `1<c<2`. For consecutive parent root indices, `floor(c(k+1))-floor(ck)` is 1 or 2. The adjacent endpoint pairs therefore overlap or touch without holes. If current root-index support is an integer interval `[A,B]`, next support is exactly

`[ floor(cA), ceil(cB) ] ∩ Z`.

Hence the support remains an interval and branch collisions are structurally forced. Cardinality grows on the `c^t=r^(t/p)` scale, strictly below binary `2^t`.

Exhaustive attack: every integer `r` with `1<=r<2^p` for `p=2..8`, every interval `0<=A<=B<=40`: 431,361 cases, 0 counterexamples.

### Regime C — collision-free binary phase: `r>2^p`, non-pth-power r

Then `c>2`. Consecutive parent floors differ by at least 2, so their two-child pairs are disjoint. Nonalignment guarantees every positive parent has two children. Therefore support cardinality doubles **exactly** every layer and recoalescence count is zero.

Targeted attack: 68,900 local root checks plus 110,240 trajectory-layer checks across `p=2..8` and 100 super-threshold refinement ratios per p (excluding aligned pth powers), 0 counterexamples.

### The phase atlas

The line `r=2^p` is a sharp funnel/binary boundary, but it is itself an aligned freeze line. Above it lies a binary-expansion sea punctured by perfect-pth-power freeze islands `r=a^p`. Below it lies the interval-recoalescence funnel.

For fixed refinement `r`, increasing p eventually forces `r<2^p` and therefore moves the BRC system from potential binary expansion into the recoalescing funnel. This is an important inversion of the naive “higher p always means more branching” intuition.

---

## 10. PHASE_THRESHOLD family

### R025-LAW-017 — threshold antitonicity

If `alpha<=beta`, then pointwise

`S_beta(n) <= S_alpha(n)`

because increasing the threshold can only switch an endpoint choice from U to L, never L to U. With common monotone inter-layer dynamics, induction makes the entire finite-depth terminal trajectory antitone in alpha.

Attack: `n0=0..500`, `p=2..6`, `r=1..12`, depth 8, thresholds `0,1/4,1/2,3/4,1`: 240,480 layer comparisons, 0 violations.

For any fixed finite BRC execution, the output as a function of alpha is piecewise constant; all breakpoints are drawn from exact rational phases reachable in the BRC support. This gives a finite exact compression of the whole threshold-policy family.

---

## 11. Operation robustness boundary

Identity was the theorem baseline, as required. Two explicit monotone operation probes were then inserted:

- physical `+1` (`state -> state+M`);
- integer scale `×2`.

Observed boundary:

- H1 envelope survives both in the tested box because the common operations are monotone;
- H2 raw physical DOWN monotonicity fails immediately because the operation can add physical value;
- H5 aligned freeze fails because the operation moves an exact p-power before the next collapse;
- stochastic **collapse itself** remains conditionally unbiased relative to the post-operation input, but the raw state process is no longer a martingale unless the deterministic operation is compensated. For `+1`, subtract the predictable cumulative translations; for `×2`, rescale by the predictable multiplicative factor.

Thus the correct generic statement is not “unbiased collapse erases operations”; it is “collapse adds zero conditional drift relative to the operated state.”

---

## 12. Strongest theorem candidates to formalize next

1. **Endpoint envelope theorem** for arbitrary exponent/refinement words and common monotone operation layers.
2. **No-integer-midpoint theorem** and `NEAREST = PHASE_THRESHOLD(1/2)` corollary.
3. **Scale microphase theorem** `root_p(a^p n)=a root_p(n)+j`, `0<=j<a`.
4. **Aligned refinement freeze theorem**.
5. **Precision plateau/sawtooth theorem** plus finite binomial envelope and `M^{-1/p}` asymptotic.
6. **Upper p-power closure divisibility commutation theorem**, dual to existing lower-collapse absorption.
7. **Unbiased stochastic martingale + exact predictable quadratic variation theorem**.
8. **Sparse-phase stochastic observability theorem** with exact one-step `Theta(2^p)` sample requirement.
9. **PHASE_THRESHOLD antitonicity / reachable-phase breakpoint theorem**.
10. **BRC constant-(p,r) trichotomy theorem**: aligned freeze / subbinary interval funnel / exact binary explosion.

The highest leverage formalization is #10, followed by #7/#8 and #3. The BRC trichotomy gives an exact branch-complexity decision rule directly from `(p,r)` and can feed both R023 semantics and R024 runtime selection without changing either task's frozen semantics.

---

## 13. Validation and resource accounting

- focused unit tests: `17/17 PASS`;
- exact reference runtime (split p=2..6): about `38.61 s` total;
- broad deterministic fast sweep: about `12.21 s`;
- exact 18,180 stochastic distribution attack: about `2.00 s`;
- broad sweep maximum state size: 2,081 bits;
- maximum directly enumerated ALL_ENDPOINTS support: 4,096;
- raw exhaustive reference streamed to gzip, avoiding retention of 240,480 Python row objects;
- conservative implementation memory estimate `<128 MiB`; RSS was not separately instrumented, so this is marked an estimate rather than measured theorem evidence;
- full repository suite: `FULL_SUITE_PENDING` because the research runtime is a task-scoped synthetic worktree rather than a complete source checkout;
- source CI status: `CI_NOT_REQUIRED_FOR_RESEARCH` per Enterprise Math L1/L2/L3 remote-liveness rule; no workflow polling was performed.

The focused suite checks root/bracket correctness, fixed points, no midpoint, nearest/half-threshold equivalence, near/far complement, aligned freeze, H4/H6 witnesses, exact stochastic martingale/variance, counter PRNG reproducibility, BRC funnel and binary examples, monotone-operation envelope behavior, scale microphase bounds, threshold antitonicity, UP divisibility closure, and the high-p sparse unbiased formula.

---

## 14. Artifacts

Core:

- `experiments/r025_multilayer_collapse_atlas.py`
- `tests/test_r025_multilayer_collapse_atlas.py`
- `docs/R025_MULTILAYER_COLLAPSE_POLICY_DYNAMICS_REPORT.md`
- `R025_LAW_MATRIX.md`
- `R025_PRECISION_EXPONENT_PHASE_ATLAS.md`
- `data/r025/R025_MACHINE_SUMMARY.json`

Data (the source checkpoint carries the reproducible text sample/manifest; the two compressed binary raw files are returned as task attachments because the GitHub text connector is not used for multi-megabyte binary blobs):

- `R025_EXHAUSTIVE_REFERENCE_RAW.csv.gz` — 240,480 exact rows, SHA-256 above, task attachment;
- `R025_RANDOM_TERMINALS_1024.csv.gz` — 10,240 seed terminal records, task attachment;
- `R025_RAW_DATASET_MANIFEST.json` — row counts, hashes, byte sizes and reproduction provenance retained in source checkpoint;
- `R025_RAW_LAYER_SAMPLE.csv` — full layer schema sample covering deterministic, thresholds, PRNG and unbiased stochastic;
- `R025_PRECISION_SCALING.csv`;
- `R025_EXPONENT_PHASE.csv`;
- `R025_STOCHASTIC_OBSERVABILITY.csv`;
- `R025_BRC_PHASE.csv`;
- `R025_BRC_RAW_SAMPLE.csv`;
- `R025_ORDER_DEFECT.csv`;
- `R025_POLICY_COMPARISON.csv`;
- exact attack JSONs and minimal counterexample JSON.

---

## 15. Return recommendation

**Formalize now:** BRC trichotomy, stochastic martingale/variance + observability barrier, no-midpoint/threshold-half identity, scale microphase, UP divisibility closure.  
**Continue data:** variable `(p_t,r_t)` BRC words, where the constant-parameter trichotomy becomes a product of local phases; this is the natural next atlas layer.  
**Connect R024:** compile the BRC regime classifier into runtime choice: aligned → fixed-point shortcut, funnel → interval/cursor representation, binary → explicit branch budget/symbolic binary token rather than naive set materialization.  
**Connect R023/BRC:** use only support/recoalescence semantics already frozen; no multiplicity/probability semantics should be smuggled into the Boolean support theorem layer.  
**Kill route:** do not pursue H4 covariance or H6 p-power-free kernel in their frozen forms; replace both with the microphase refinement law.
