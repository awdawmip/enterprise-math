# R031 — Large-Scale Pi Collapse Divergence Atlas

**Researcher-ID:** `EM-R031-1B4E08`  
**Task:** `RS-R031-LARGE-SCALE-PI-COLLAPSE-DIVERGENCE-ATLAS`  
**Taskbook source:** `d8557f6d5df35b9816aa373d03ad49c450fde717`  
**Research status:** `LARGE_SCALE_COLLAPSE_PHASE_STRUCTURE_FOUND / MACHINE_FIELD_CROSSOVER_CLASSIFIED / DIRECTIONAL_FUTURES_MEASURED / ALGORITHM_RELATIVE_COLLAPSE / NOT_CANONICAL`

## 1. Executive result

R031 finds a real and sharply measurable field crossover, but not a single universal crossover point and not a canonical new value of pi.

The strongest result is that the ratio

\[
\chi_p(N)=\frac{\operatorname{ulp}_{64}(N)}{G_p(N)},\qquad
G_p(N)=(k+1)^p-k^p,\quad k=\lfloor N^{1/p}\rfloor,
\]

has an exact **dyadic staircase** structure. Within a binary64 binade, the ULP is constant while the p-th-power basin gap grows, so `chi_p` decreases across the binade. At the next binade boundary the ULP doubles and `chi_p` jumps upward. Therefore crossover has two useful exact notions:

- **onset binade:** some states in that binade satisfy `chi_p >= 1`;
- **permanent binade:** every state in that binade satisfies `chi_p >= 1`.

Along the concrete `N_d=floor(pi*10^d)` path, the first integer decades with `chi_p >= 1` are:

| p | first decade d on pi path | chi at first crossing |
|---:|---:|---:|
| 2 | 32 | 1.01635359929279620 |
| 3 | 48 | 1.00859085069104633 |
| 4 | 66 | 1.25347846097165281 |
| 5 | 82 | 1.35509310315250506 |
| 6 | 100 | 1.15785089925200162 |
| 8 | 134 | 1.04165083423311172 |
| 10 | 169 | 1.90060951382705178 |
| 12 | 203 | 1.67680283010990361 |
| 16 | 272 | 1.28347765779533792 |

So `10^36` is **not** the square-field crossover itself: p=2 crossed near `10^32`. But `10^36` is a very clean **phase-separation scale**: p=2 is already deeply sub-machine while p>=3 is still far coarser than the binary64 cell. At `10^48`, p=3 is just crossing; at `10^72`, p=4 is strongly sub-machine; at `10^100`, p=6 has just crossed.

The second major result is dynamical: collapse direction produces repeatable futures, but the observable ordering is **future-operation relative**. In Gauss–Legendre iteration-boundary injection at `D=36,p=2`, DOWN ends below the reference and UP above it. In Chudnovsky, where the collapsed partial sum enters the final result through a reciprocal, DOWN raises the final pi and UP lowers it. Thus “DOWN gives a lower final result” is false globally even though DOWN/UP remain meaningful local endpoint semantics.

The third major result is that ordinary algorithm stopping can hide long collapse dynamics. At fixed precision, UP/NEAREST/FAR often enter fixed points quickly; residual-only can enter its own absorbing state; DOWN can form a very long exact anchor ladder. For the `D=36,p=2` Gauss–Legendre iteration-boundary channel, the local recurrence shows an equal square anchor root decreasing by one every two boundary updates until a decimal divisibility condition is met. The candidate endpoint predicts only 7 stable fractional pi digits, far fewer than the 16–17 stable digits seen at ordinary algorithm stopping.

Finally, the geometry/formula channel does **not** currently support a noncontinuous universal policy-specific pi for ordinary endpoint selectors. Circumference, area and polygon recovered-pi values become formula-coherent as scale grows, but DOWN/UP/NEAREST/FAR all approach continuous pi under this output-collapse semantics. Residual-only, by contrast, produces a stable degenerate zero effective-pi attractor across these formula channels. That is a positive intrinsic dynamical result, not a failure caused by anchor non-reconstruction.

## 2. Frozen semantics and execution model

All theorem-critical collapse geometry uses exact integers/rationals.

For `p>=2` and non-exact state `n`, define

\[
L=k^p,\quad U=(k+1)^p,\quad G=U-L,\quad d=n-L,\quad u=U-n,\quad \phi=d/G.
\]

Policies implemented:

- `DOWN`: L;
- `UP`: U;
- `NEAREST`: closest endpoint, lower tie;
- `FAR`: farthest endpoint, upper tie;
- `PRNG_50_50`: deterministic SHAKE256 counter/rejection sampler, exact 1/2 endpoint sampling;
- `DISTANCE_WEIGHTED_STOCHASTIC`: exact `P(U)=d/G`, `P(L)=u/G` with rejection sampling and no modulo bias;
- `RESIDUAL_ONLY`: retains the lower-offset coordinate `d` and discards the anchor;
- `ANCHOR_PLUS_RESIDUAL`: explicit lossless control carrier `(L,d)` whose scalar reconstruction is `L+d=n`;
- `FIELD_PHASE`: dimensionless phase carrier `floor(phi*S)` at fixed-point scale S;
- `ALL_ENDPOINTS`: exact support `{L,U}` with literal-state deduplication.

Exact perfect powers are fixed points for every policy.

Binary64 geometry is computed from integer bit length and dyadic spacing, without converting the target integer through host floating point.

The arbitrary-precision pi coordinate is generated with stdlib Decimal Chudnovsky at two guard precisions and required to agree at the final integer coordinate. This reference is not used to define collapse geometry.

## 3. Independent `10^36` recomputation

\[
N=\lfloor \pi 10^{36}\rfloor
=3141592653589793238462643383279502884.
\]

The exact binary64 binade exponent is `e=121`, hence

\[
\operatorname{ulp}_{64}(N)=2^{121-52}=2^{69}
=590295810358705651712.
\]

The exact phase of N inside its containing dyadic cell is

\[
\frac{80551212002059080073}{147573952589676412928}
\approx 0.5458362440560806,
\]

so binary64 nearest-even chooses the upper dyadic endpoint.

Exact local p-th-power gaps:

| p | exact G_p(N) | chi_p(N) |
|---:|---:|---:|
| 2 | 3,544,907,701,811,032,055 | 166.519373708131732 |
| 3 | 6,435,088,191,332,872,375,248,847 | 9.17308034960186300e-5 |
| 4 | 9,438,921,963,269,664,714,442,100,655 | 6.25384776625725803e-8 |
| 5 | 788,296,993,587,766,588,692,281,658,781 | 7.48824129941304809e-10 |
| 6 | 15,575,545,772,893,908,620,080,696,000,567 | 3.78988845056072628e-11 |
| 8 | 688,808,889,845,173,892,731,048,318,278,975 | 8.56980534167305262e-13 |
| 10 | 7,032,017,087,523,428,469,355,068,536,140,127 | 8.39440238855561472e-14 |
| 12 | 34,409,107,286,800,103,091,812,942,399,873,201 | 1.71552201409524155e-14 |
| 16 | 273,372,782,392,416,681,237,934,731,972,873,215 | 2.15930717459413167e-15 |

One binary64 step at this location intersects exactly **167 square basins**: 165 are fully contained and the two edge basins are partial. For every tested `p>=3`, the same binary64 step remains inside a single p-th-power basin.

The information-spacing comparison is especially sharp:

- p=2: `log2(chi_2)=+7.3795`; binary64 discards about 7.38 more local low-order bits than square-basin spacing;
- p=3: `log2(chi_3)=-13.4122`; binary64 is about 13.41 bits finer than the cube-basin gap.

## 4. Main scale atlas

### 4.1 Binary64-cell coverage

The exact number of p-th-power basins touched by one binary64 cell around `floor(pi*10^d)` is:

| d | p=2 | p=3 | p=4 | p=5 | p=6 |
|---:|---:|---:|---:|---:|---:|
| 36 | 167 | 1 | 1 | 1 | 1 |
| 48 | 183,089,989 | 2 | 1 | 1 | 1 |
| 72 | 110,671,106,686,709,676,939 | 60,965,577 | 43 | 1 | 1 |
| 100 | 10,960,335,532,760,151,082,339,433,368,954,207 | 130,079,126,445,970,094 | 411,629,401 | 3,111 | 3 |

At `d=100,p=6`, the binary64 cell touches three sixth-power basins, with one full basin and two partial edge basins.

### 4.2 Exact binade crossover bands

| p | onset e | onset lower log10 magnitude | permanent e | permanent lower log10 magnitude |
|---:|---:|---:|---:|---:|
| 2 | 107 | 32.2102 | 107 | 32.2102 |
| 3 | 161 | 48.4658 | 163 | 49.0679 |
| 4 | 217 | 65.3235 | 219 | 65.9256 |
| 5 | 272 | 81.8802 | 276 | 83.0843 |
| 6 | 328 | 98.7378 | 333 | 100.2430 |
| 8 | 441 | 132.7542 | 447 | 134.5604 |
| 10 | 554 | 166.7706 | 563 | 169.4799 |
| 12 | 668 | 201.0880 | 679 | 204.3994 |
| 16 | 897 | 270.0239 | 911 | 274.2383 |

For p=3, for example, the onset binade `e=161` has `chi` ranging from about 0.6667 to 1.0583; the permanent binade is not reached until `e=163`, where the whole binade is above 1.

Binary64 itself ceases to provide a finite coordinate before the `pi*10^308` scale. The runner records `d=307` normally and marks `d=308,400,1000` as machine-field unavailable rather than extrapolating a fictitious ULP. Exact p-th-power collapse remains defined there.

## 5. Crossover law candidate

For `N` in the p-th-power basin of root k,

\[
G_p(N)=(k+1)^p-k^p.
\]

The binomial/mean-value bounds give

\[
p k^{p-1}\le G_p(N)\le p(k+1)^{p-1}.
\]

Because `k ~ N^(1/p)`, the gap satisfies

\[
G_p(N)=\Theta(N^{(p-1)/p}).
\]

Within binary64 binade `[2^e,2^(e+1))`,

\[
\operatorname{ulp}_{64}=2^{e-52}=\Theta(N).
\]

Therefore the envelope is

\[
\boxed{\chi_p(N)=\Theta(N^{1/p})}
\]

modulated by the exact dyadic staircase. This explains why every fixed p eventually becomes finer than the binary64 machine cell before binary64 overflows, while higher p crosses later.

A related relative-gap law is

\[
\frac{G_p(N)}{N}=\Theta(N^{-1/p}),
\]

so the collapse field becomes relatively denser with magnitude even though its absolute gaps increase.

## 6. Internal pi algorithms: policy-separated futures

### 6.1 `D=36,p=2`, iteration-boundary injection

Deltas below are integer fixed-point coordinate differences from `floor(pi*10^36)`.

| algorithm | policy | delta | stable fractional prefix |
|---|---|---:|---:|
| Gauss–Legendre | DOWN | -16,330,321,828,944,710,610 | 16 |
| Gauss–Legendre | UP | +19,831,015,503,978,293,604 | 16 |
| Gauss–Legendre | NEAREST | -7,474,069,468,117,245,459 | 17 |
| Gauss–Legendre | FAR | +97,686,308,184,657,752,101 | 15 |
| Chudnovsky | DOWN | +2,051,787,938,924,621 | 20 |
| Chudnovsky | UP | -3,061,130,703,652,861 | 19 |
| Chudnovsky | NEAREST | +347,481,724,732,127 | 21 |
| Chudnovsky | FAR | -1,356,824,489,460,367 | 20 |

This is a direct counterexample to a global H5-style claim `DOWN final <= UP final` across arbitrary future operations. The local endpoint order survives, but Chudnovsky applies the partial sum as a denominator, an antitone future map, so the final observable ordering reverses.

### 6.2 Injection boundary is semantically active

At the same `D=36,p=2`, changing from iteration-boundary injection to nonlinear-primitive injection changes even the sign pattern:

- Gauss–Legendre nonlinear: DOWN `+1.6668e19`, UP `+9.5777e18`, NEAREST `-8.1468e18`, FAR `-1.0570e18`;
- Chudnovsky nonlinear: DOWN/NEAREST `-1.0570e18`, UP/FAR `+2.4879e18`.

So “the collapse policy” does not determine a unique pi future without specifying the future operation language and injection boundary.

### 6.3 Finite-stop stable-prefix scaling

For the four deterministic endpoint selectors, iteration-boundary stable-prefix ranges are:

**Gauss–Legendre**

| p | D=36 | D=48 | D=72 | D=100 |
|---:|---:|---:|---:|---:|
| 2 | 15–17 | 21–22 | 33–34 | 47–49 |
| 3 | 9–10 | 12–14 | 22–23 | 30–31 |
| 4 | 6–8 | 9–10 | 16 | 22–23 |
| 6 | 3–4 | 5–8 | 9–11 | 14 |

**Chudnovsky**

| p | D=36 | D=48 | D=72 | D=100 |
|---:|---:|---:|---:|---:|
| 2 | 19–21 | 26 | 36–39 | 51–53 |
| 3 | 12–13 | 16–18 | 24–26 | 33–34 |
| 4 | 9–10 | 10–12 | 17–19 | 24–25 |
| 6 | 5 | 7–8 | 10–12 | 15–16 |

The finite-stop law is consistent with an algorithm-dependent `D/p + O(1)` scale, but R031 rejects treating that as a universal long-time law.

## 7. Long-horizon dynamics and attractors

With Gauss–Legendre iteration-boundary collapse at `D=36`:

- p=2: UP and NEAREST reach 1-cycles by iteration 4; FAR reaches a 1-cycle at iteration 58; RESIDUAL_ONLY reaches `(a,b,t)=(0,0,1)` at iteration 7 and stays there; FIELD_PHASE makes `t<=0`; DOWN has no cycle within 100 steps because it enters a long descending square-anchor ladder.
- p=3..5: UP/NEAREST/FAR again reach 1-cycles; RESIDUAL_ONLY reaches a 1-cycle; DOWN eventually makes `t<=0` within the 100-step probe.
- p=6: FAR exhibits a genuine 2-cycle; UP/NEAREST/RESIDUAL_ONLY reach 1-cycles; DOWN and FIELD_PHASE become singular under this algorithm future.

These are stable, reproducible policy-specific futures. They are not ranking errors against continuous pi; they are collapse dynamics.

### 7.1 p=2 DOWN anchor-ladder candidate

At `D=36`, DOWN first reaches an equal square anchor at iteration 3:

\[
a=b=k^2,
\quad k=920441787835590982,
\]

with frozen

\[
t=228473290522231809471746755847000064.
\]

For an equal square anchor `a=k^2` with `S/2<a<S`, the fixed-point geometric-mean primitive satisfies:

- if `S | a^2`, its integer square-root returns `a` exactly;
- otherwise the integer square-root returns `a-1`.

For p=2 DOWN, `a-1` then collapses to `(k-1)^2`. The next averaging/geometric-mean boundary update recoalesces both anchors at `(k-1)^2` while `t` stays unchanged because the squared difference truncates to zero at scale S. Hence the square root decreases by one every two boundary updates while the ladder conditions remain valid.

For `S=10^36`, `S | k^4` exactly when `10^9 | k`. The first lower such root is

\[
k_*=920441787000000000.
\]

The candidate requires 835,590,982 root decrements, or 1,671,181,964 additional boundary updates. Its predicted endpoint is

\[
\pi_{\text{DOWN,long}}
\approx 3.141592642181851889084753336400758943,
\]

which shares only 7 fractional digits with continuous pi. The local transition and divisibility condition are exact; the full billion-step conclusion is a theorem candidate contingent on preserving the ladder hypotheses through the interval.

This is the clearest R031 example of a “future” that is invisible at ordinary algorithm stopping.

## 8. Stochastic policies

At `D=36,p=2`, 256 deterministic seeds:

| algorithm | policy | mean delta | std delta | unique outputs |
|---|---|---:|---:|---:|
| Gauss–Legendre | PRNG 50/50 | +1.0467e19 | 1.8373e19 | 43 |
| Gauss–Legendre | distance-weighted | -6.7167e17 | 1.0314e19 | 12 |
| Chudnovsky | PRNG 50/50 | -5.9122e14 | 1.4964e15 | 4 |
| Chudnovsky | distance-weighted | +1.4609e13 | 6.7566e14 | 2 |

Distance-weighted endpoint selection is exactly unbiased for a single coordinate conditional on the current bracket, but nonlinear future operations need not preserve that expectation. The Monte Carlo results are therefore diagnostic rather than theorem evidence; nevertheless their final-output means are much smaller than their spreads in both algorithms.

## 9. ALL_ENDPOINTS / recoalescence

The exact support channel shows genuine branch growth followed by observable recoalescence.

Gauss–Legendre `D=36,p=2`, 8 iterations:

- state support sizes: `1, 8, 24, 48, 80, 95, 121, 143, 172`;
- 172 terminal internal states;
- only 129 distinct final pi coordinates;
- 43 internal branches recoalesce at the final observable.

Chudnovsky p=2:

- `D=36`: support sizes `1,2,3,4,4,4`, four final pi values;
- `D=72`: `1,2,3,4,5,6,6,6,6`, six final pi values;
- `D=100`: `1,2,3,4,5,6,7,8,8,8,8`, eight final pi values.

This makes the endpoint support itself a measurable object rather than an averaged rounding surrogate.

## 10. Large-circle / formula channel

For radius `R=10^d+delta` with `delta in {-1,0,1}`, R031 tested:

- circumference `C=2*pi*R`;
- area `A=pi*R^2`;
- regular-polygon lower and upper pi bounds, then perimeter reconstruction;
- small exact lattice-circle sanity counts at `R=1000,10000`.

### 10.1 Formula coherence

For endpoint selectors, the recovered-pi formula defect decays approximately as

\[
\boxed{\text{defect}=O(10^{-2d/p})}
\]

because circumference output has coordinate magnitude `Theta(10^(2d))` and its p-th-power collapse relative disturbance is `Theta(N^{-1/p})`; area decays faster (`Theta(10^{-3d/p})`) and therefore does not dominate the cross-formula defect.

Observed `log10(defect)` for DOWN:

| p | D=36 | D=48 | D=72 | D=100 |
|---:|---:|---:|---:|---:|
| 2 | -35.601 | -47.601 | -71.601 | -99.601 |
| 3 | -23.348 | -31.387 | -47.313 | -66.123 |
| 4 | -17.337 | -24.563 | -35.280 | -49.361 |
| 6 | -10.952 | -15.012 | -23.275 | -32.223 |

Thus DOWN/UP/NEAREST/FAR do produce finite-scale policy-specific effective pi values, and those values become consistent across circumference/area/polygon formulas. But their common asymptotic limit under this channel is continuous pi, not a distinct policy-specific constant.

### 10.2 Residual-only as a positive result

At `D=36,p=2`, residual-only recovered effective pi values are approximately:

- circumference: `2.32697e-36`;
- area: `1.08013e-54`;
- polygon lower: `1.32697e-36`;
- polygon upper: `1.82034e-36`.

Their formula defect is about `10^-35.63` and shrinks with scale. Residual-only therefore exhibits a coherent **zero-attractor family** in this geometry channel. It is irreversible and loses the anchor by construction, but that does not make the dynamics invalid.

FIELD_PHASE also collapses toward zero in recovered-pi geometry, with a still faster scale-normalized defect in these probes.

Residual dynamics are not universal across algorithm futures: Gauss–Legendre iteration-boundary residual collapses to the `(0,0,1)` fixed point, while Chudnovsky iteration-boundary residual can drive the denominator-like carrier into a radically different large-output regime. So the correct classification is **algorithm-relative residual dynamics**, not failure.

### 10.3 Radius perturbation and discrete sanity

The `R=10^d-1,10^d,10^d+1` probes show formula-specific phase sensitivity even when recovered pi remains coherent. In particular, square-root indices in area coordinates can move by many roots under `R -> R+1` while circumference indices move by only O(1), because the coordinate magnitudes differ by one extra power of R.

Exact lattice disk counts give:

- `R=1000`: 3,141,549 lattice points, `count/R^2 = 3.141549`;
- `R=10000`: 314,159,053 lattice points, `count/R^2 = 3.14159053`.

This channel is retained only as a discrete sanity calibration; exhaustive `R=10^d` lattice enumeration is infeasible for the large scales and is not substituted by a fake extrapolation.

## 11. Scale covariance: naive phase invariance is false

A minimal counterexample kills naive p-th-power phase preservation:

- p=2, n=2 lies in `[1,4)` with phase `1/3`;
- scaling by `q^p=4` gives n'=8, which lies in `[4,9)` with phase `4/5`.

So `phi(q^p n)=phi(n)` is false.

What survives is a **refinement law**. If `k^p <= n < (k+1)^p`, then after scaling by `q^p`,

\[
(qk)^p \le q^p n < (q(k+1))^p,
\]

hence

\[
qk \le \lfloor (q^p n)^{1/p}\rfloor \le q(k+1)-1.
\]

The original basin is refined into at most q child p-th-power root intervals rather than carrying a single invariant phase.

## 12. H1–H12 disposition

| Hypothesis | R031 disposition | Reason |
|---|---|---|
| H1 binary64 is a dyadic collapse/quantization field | **SURVIVES at representation level** | exact binade lattice and endpoint cells; not claimed equivalent to every floating arithmetic pipeline |
| H2 chi_p has a machine-field crossover law | **SURVIVES, strengthened** | exact onset/permanent binades plus `Theta(N^(1/p))` staircase envelope |
| H3 `10^36` is p2-submachine but p>=3 not | **SURVIVES strongly** | chi2=166.52 vs chi3=9.17e-5 and smaller for higher p |
| H4 relative collapse gap shrinks with scale | **SURVIVES** | `G/N=Theta(N^-1/p)` |
| H5 direction creates ordered futures | **PARTIAL / global ordering killed** | local direction persists; Chudnovsky reciprocal future reverses final DOWN/UP order |
| H6 stable prefix scales with d/p | **SURVIVES as finite-stop law** | both algorithms show algorithm-dependent `D/p+O(1)` bands; long-horizon ladder prevents universal claim |
| H7 policies converge to distinct stable pi-like constants | **ALGORITHM-RELATIVE / not universal** | finite fixed-precision attractors exist; endpoint formula channel converges back to pi; long-horizon GL can differ |
| H8 one policy yields cross-formula coherent effective pi | **SURVIVES asymptotically** | endpoint defects shrink as about `10^-2d/p`; residual/phase yield coherent zero attractors |
| H9 phase is scale-covariant | **NAIVE VERSION KILLED** | `n=2,p=2,q=2` gives `1/3 -> 4/5`; refinement law survives |
| H10 residual-only can form an intrinsic attractor | **SURVIVES, algorithm-relative** | exact zero fixed point in GL and zero family in formula channel; Chud behavior differs |
| H11 information loss can expose simpler structure | **SURVIVES as measurable phenomenon** | chi/log2 spacing, fixed points, support recoalescence and zero attractors become visible after collapse |
| H12 low-dimensional phase diagram exists | **SURVIVES** | magnitude/binade, exponent p, policy, and future-operation boundary explain observed transitions |

## 13. Minimal counterexamples / kill tests

1. **Global direction ordering:** `D=36,p=2`, iteration-boundary Chudnovsky has DOWN above reference and UP below it, opposite Gauss–Legendre.
2. **Naive scale-phase invariance:** `p=2,n=2,q=2`: phase `1/3 -> 4/5`.
3. **Finite-stop = long-time future:** `D=36,p=2` Gauss–Legendre DOWN has ~16 stable digits at ordinary stopping but enters a long exact anchor ladder whose candidate endpoint has only 7.
4. **Residual-only = invalid:** false. Gauss–Legendre residual reaches an exact `(0,0,1)` fixed point and formula residual has a stable zero-attractor family.
5. **Policy alone determines future:** false. Changing the injection boundary changes sign/order and can change regular trajectories into singular ones.

## 14. Strongest theorem candidates

### T1 — Exact binade staircase crossover
For every p>=2, inside one normal binary64 binade the ULP is fixed while `G_p` is nondecreasing, so `chi_p` is nonincreasing. At each binade boundary the ULP doubles. Exact onset/permanent binades can therefore be characterized by endpoint inequalities.

### T2 — Crossover envelope
`chi_p(N)=Theta(N^(1/p))` before binary64 overflow, with explicit constants obtainable from the binomial bounds on `G_p` and the two-sided binade bounds on N.

### T3 — Basin refinement under p-th-power scale lift
If n lies in the k-th p-power basin, scaling by `q^p` sends its root index into `[qk,q(k+1)-1]`. Phase is not invariant; the old basin refines into q root-index slots.

### T4 — p=2 DOWN equal-anchor ladder
Under the fixed-point Gauss–Legendre equal-square-anchor conditions stated above, a non-divisible equal square anchor maps through the geometric-mean primitive and DOWN boundary collapse to the preceding square; two boundary updates recoalesce at that preceding square while t stays frozen. Decimal scale then imposes the divisibility attractor condition `10^ceil(D/4) | k`.

T1–T3 are close to formalization-ready. T4 needs the ladder-domain hypotheses stated and discharged carefully before promotion.

## 15. Recommendation: proceed to finite-field / ECC collapse calibration

**Recommendation: YES — proceed, but as an independent, non-attack calibration lane.**

R031 gives enough positive evidence to justify it:

1. collapse fields can become strictly finer than binary64 by enormous factors at large magnitude;
2. policy choices generate stable, repeatable future structures that are not reducible to ordinary error magnitude;
3. those futures are strongly operation-language dependent, so a domain with native discrete algebra is preferable for the next calibration;
4. finite fields remove the ambiguous continuous-reference benchmark that made R026-style scoring inappropriate here;
5. anchor/residual and branch-support semantics have natural analogues in field-coordinate representations and group operations.

The ECC task should **not** be cryptanalytic. It should benchmark exact public algebraic operations only: field reduction, coordinate representations, point addition/doubling, scalar-multiplication execution traces on public test vectors, representation/storage costs, branch/recoalescence behavior, and whether collapse carriers preserve declared group-operation futures. No key recovery, attack construction or security bypass belongs in the calibration task.

A discrete-geometry lane is also justified, especially for circle/lattice boundary structure, but ECC/finite-field calibration is the higher-value next test because it is natively discrete and directly stresses future-operation compatibility.

## 16. Limitations and non-claims

- R031 does **not** prove a canonical replacement for pi.
- It does **not** claim that endpoint selectors approach noncontinuous constants in the large-circle output-collapse channel; the observed limit there is pi.
- Internal algorithm results depend materially on the chosen fixed-point representation and collapse injection boundary; this is recorded as a result, not hidden as noise.
- The binary64 comparison is an exact representation-field comparison around large integer coordinates, not a complete emulation of every hardware floating arithmetic instruction sequence.
- ALL_ENDPOINTS Gauss–Legendre was exhaustively propagated for 8 iterations at the frozen sanity point; support growth, not arithmetic precision, is the practical limiter.
- Polygon bounds use high-precision Decimal square-root recurrence and are a numerical geometry channel, not theorem-critical evidence for the machine crossover law.
- The p=2 long DOWN endpoint is a theorem candidate derived from an exact local recurrence; a formal proof still needs to show the ladder hypotheses persist for the entire interval to the divisibility attractor.

## 17. Reproducibility

Runner:

`experiments/r031_large_scale_pi_collapse.py`

Focused tests:

`tests/test_r031_large_scale_pi_collapse.py`

Generated artifacts:

- `research/r031_generated/R031_MACHINE_FIELD_CROSSOVER.json`
- `research/r031_generated/R031_PI_POLICY_DIVERGENCE.json`
- `research/r031_generated/R031_FORMULA_COHERENCE.json`
- `research/r031_generated/R031_SCALE_P_POLICY_PHASE_ATLAS.csv`
- `research/r031_generated/R031_RUN_MANIFEST.json`

Focused test gate: **12/12 PASS**.

No CI is required for this research task; no workflow status was used as evidence.
