# P022 — Barlow Microscopic Counting Ensemble: Mean versus Typical Geometry

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE COUNTING + ASYMPTOTIC SEPARATION / NOVELTY_UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: exact Barlow shell-cardinality and geodesic-count formulas  
Boundary: the uniform counting measure is an analysis of the finite microscopic state set, not a physical or stochastic stacking law

## 1. Why average over microscopic histories?

At radius `n`, a finite two-sided Barlow environment consists of

- `n` interface signs above the root;
- `n` interface signs below the root.

Hence there are exactly

\[
\boxed{4^n}
\]

microscopic two-sided windows.

All results in this note simply count those finite windows with equal weight. No probability law is added to the geometry.

The purpose is to test a common compression hazard:

> does the arithmetic average of a coarse observable represent a typical microscopic history?

For Barlow coordination cardinality, essentially yes at leading polynomial scale. For geodesic witness multiplicity, no: rare drift sectors change the exponential rate of the mean.

## 2. Exact moments of one prefix imbalance

Let

\[
\delta=\sigma_1+\cdots+\sigma_n,
\qquad\sigma_j\in\{-1,+1\}.
\]

Summing over all `2^n` words gives

\[
\boxed{
\frac1{2^n}\sum\delta^2=n.}
\]

Expanding the fourth power, only index patterns in which every sign occurs an even number of times survive. Therefore

\[
\boxed{
\frac1{2^n}\sum\delta^4
=3n^2-2n.}
\]

Hence

\[
\boxed{
\operatorname{Var}(\delta^2)
=2n(n-1).}
\]

These are finite integer counting identities.

## 3. P022-CE01 — exact mean and variance of shell cardinality

For one two-sided window,

\[
4S_n=42n^2+8-\delta_n^2-\delta_{-n}^2.
\]

The two microscopic sides are independent in the Cartesian product count. Therefore

\[
\boxed{
\overline{Q_n}=2n,}
\]

and

\[
\boxed{
\operatorname{Var}(Q_n)=4n(n-1).}
\]

Consequently

\[
\boxed{
\overline{S_n}
=\frac{42n^2+8-2n}{4},}
\]

and

\[
\boxed{
\operatorname{Var}(S_n)
=\frac{n(n-1)}4.}
\]

The sum of shell cardinalities over all microscopic windows is therefore

\[
\boxed{
4^n\overline{S_n}.}
\]

No shell enumeration is required.

## 4. Counting-typical coordination is asymptotically balanced

Normalize by `n^2`.

The mean satisfies

\[
\frac{\overline{S_n}}{n^2}
=\frac{21}{2}-\frac1{2n}+\frac2{n^2}
\longrightarrow\frac{21}{2}.
\]

Meanwhile

\[
\operatorname{Var}\left(\frac{S_n}{n^2}\right)
=\frac{n(n-1)}{4n^4}
=O(n^{-2}).
\]

Therefore, for every fixed `epsilon>0`, the fraction of microscopic windows whose normalized shell cardinality differs from `21/2` by more than `epsilon` tends to zero.

So under uniform finite counting,

\[
\boxed{
\frac{S_n}{n^2}
\to\frac{21}{2}
\quad\text{in counting density}.}
\]

Most microscopic prefixes are coordination-wise close to the balanced/HCP leading coefficient even though they need not be periodic HCP and can have very different finite shell spectra.

## 5. Exact mean of shell-total geodesic multiplicity

The situation changes for witness multiplicity.

For a target height `q<n`, use the signed BG01 form

\[
L_n(q,\delta)
=\binom nq
\left[
3\cdot2^n
\left(
2^{-(q+\delta)/2}
+2^{-(q-\delta)/2}
\right)-6
\right].
\]

For all length-`q` microscopic prefixes,

\[
\sum_{\sigma}2^{\delta(\sigma)/2}
=\left(\sqrt2+\frac1{\sqrt2}\right)^q
=\left(\frac3{\sqrt2}\right)^q.
\]

The same identity holds with `delta -> -delta`. The unobserved suffix signs cancel against the uniform denominator.

Therefore the average non-extreme layer contribution is

\[
\boxed{
\overline{L_n(q)}
=6\binom nq
\left[
2^n\left(\frac34\right)^q-1
\right].}
\]

Sum the central layer once, positive/negative heights twice, and add the two extreme `3^n` layers. After the binomial theorem,

\[
\boxed{
\overline{T_n}
=
12\left(\frac72\right)^n
+2\cdot3^n
-18\cdot2^n
-12\left(\frac32\right)^n
+18
}
\]

for `n>=1`, with `T_0=1`.

Equivalently, the integer total over all `4^n` microscopic windows is

\[
\boxed{
\sum_{w}T_n(w)
=12\cdot14^n
+2\cdot12^n
-18\cdot8^n
-12\cdot6^n
+18\cdot4^n.}
\]

## 6. P022-CE02 — the arithmetic mean has growth base `7/2`

The exact closed form immediately gives

\[
\boxed{
\lim_{n\to\infty}\overline{T_n}^{1/n}
=\frac72.}
\]

Compare this with the balanced individual Barlow growth base

\[
\lambda_0=2+\sqrt2.
\]

Since

\[
\frac72>2+\sqrt2,
\]

the arithmetic mean grows exponentially faster than a balanced microscopic history.

This difference cannot occur for shell vertex cardinality, whose microscopic variation is only polynomial.

## 7. Counting-typical individual geodesic growth is still `2+sqrt(2)`

Let

\[
M_n
=
\max_{|k|\le n}|\delta_k|
\]

for one two-sided microscopic window.

For a one-sided simple ±1 walk, the reflection principle plus the second-moment bound gives, for positive integer `a`,

\[
\frac{\#\{\text{words}:\max_{q\le n}|\delta_q|\ge a\}}{2^n}
\le
\frac{C n}{a^2}
\]

for one universal constant `C`. Applying the union bound to the two sides and setting

\[
a=\epsilon n
\]

gives

\[
\boxed{
\frac{\#\{\text{two-sided windows}:M_n\ge\epsilon n\}}{4^n}
=O\left(\frac1{\epsilon^2n}\right)
\to0.}
\]

Thus a counting-density-one family of microscopic windows has

\[
M_n=o(n).
\]

For every window, the exact layer formula and AM-GM give the universal lower exponential rate

\[
T_n^{1/n}\gtrsim 2+\sqrt2.
\]

On the event `M_n<=epsilon n`, the same formula gives

\[
T_n
\le
\operatorname{poly}(n)
\left((2+\sqrt2)2^{\epsilon/2}\right)^n.
\]

Let `n -> infinity` and then `epsilon -> 0`. Therefore

\[
\boxed{
T_n(w)^{1/n}
\to2+\sqrt2
\quad\text{for a counting-density-one family of microscopic windows}.}
\]

So the **typical** individual exponential rate is `2+sqrt(2)`, while the **mean** exponential rate is `7/2`.

## 8. P022-CE03 — rare drift sectors raise the mean

The separation

\[
\boxed{
2+\sqrt2
<
\frac72
}
\]

proves that the arithmetic average is exponentially dominated by a vanishing-density family of atypically drifting microscopic histories.

This is not merely qualitative. The exact binomial weights locate the dominant tilted sector.

### Drift tilt inside a prefix

In

\[
\sum_{\sigma}2^{\delta(\sigma)/2}
=\left(\sqrt2+1/\sqrt2\right)^q,
\]

the plus sign receives relative weight `sqrt(2)` and the minus sign `1/sqrt(2)`. After normalization their proportions are

\[
\boxed{
\frac23
\quad\text{and}\quad
\frac13.}
\]

Hence the weighted dominant prefix drift density is

\[
\boxed{
\mu_{\mathrm{tilt}}=\frac13.}
\]

### Dominant target-layer height

After averaging the drift term, the layer-height sum contains

\[
\binom nq\left(\frac34\right)^q.
\]

Relative to

\[
\sum_q\binom nq(3/4)^q=(7/4)^n,
\]

the dominant binomial height fraction is

\[
\boxed{
\frac qn\to\frac{3/4}{1+3/4}=\frac37.}
\]

Combining the two tilts, the mean is mainly supported by sectors around

\[
\boxed{
q\sim\frac{3n}{7},
\qquad
|\delta_q|\sim\frac n7.}
\]

These histories are atypical under unweighted microscopic counting, yet their larger path multiplicities compensate for their smaller number.

## 9. Mean is not a typical-state quotient

The two exact results imply a general warning inside this finite model:

\[
\boxed{
\text{coarse arithmetic averaging can create a future-growth law that no counting-typical microscopic state exhibits}.}
\]

The mean observable is still mathematically legitimate. What fails is the inference

\[
\text{mean behavior}
\Rightarrow
\text{typical microscopic behavior}.
\]

This is the same structural caution seen elsewhere in Enterprise Math:

- cardinality shadows can lose witness identity;
- moments can lose distributions;
- quotient averages can overweight small but high-amplitude fibers.

No statistical-learning or physical claim is made from this finite combinatorial example alone.

## 10. Recurrence of the average sequence

The average geodesic total is itself C-finite. Its exact exponential modes are

\[
\frac72,
\quad3,
\quad2,
\quad\frac32,
\quad1.
\]

Multiplying by `2^n` if an integer recurrence is preferred removes denominators. The dominant mean mode `7/2` is not an individual periodic Barlow drift root at zero drift; it arises from summing over microscopic history fibers before taking the asymptotic root.

Thus the order of operations matters:

\[
\boxed{
\text{average first, then take growth}
\ne
\text{take typical individual growth first}.}
\]

## 11. Cross-route implications

### P011 / A4 count layer

The result is another example where fiber weights matter, not just which coarse states exist. Rare large-contribution fibers can dominate a weighted aggregate.

### P023/P024

`average`, `typical-growth`, and `individual exact value` are different future observables and therefore induce different legal summaries. They should not be silently identified.

### P022

P022 retains the exact Barlow finite formulas and the explicit tilted-sector calculation.

## 12. Executable assets

Added:

- `src/enterprise_math/p022_barlow_counting_ensemble.py`;
- `tests/test_p022_barlow_counting_ensemble.py`.

The tests compare the moment and mean formulas against complete enumeration of all short two-sided microscopic windows.
