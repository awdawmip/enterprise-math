# P022 Barlow Coordination Precision Supplement 03 — Binomial-Weighted Sum-of-Two-Squares Fibers

Status: `ACTIVE RESEARCH NOTE / EXACT ARITHMETIC FIBER SPECTRUM / NOVELTY_UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: BC04 shell drift-energy quotient and P022 precision-fiber methodology

## 1. Shell cardinality is itself a many-to-one quotient

At fixed radius `n`, the whole-shell cardinality depends only on

\[
Q_n=\delta_n^2+\delta_{-n}^2
\]

through

\[
4S_n=42n^2+8-Q_n.
\]

A finite two-sided stacking window contains two independent length-`n` microscopic ±1 words, one on each side of the root layer. So there are

\[
4^n
\]

microscopic two-sided windows before the shell-cardinality observation is applied.

This note computes exactly how those windows collapse into the possible `Q_n` / `S_n` states.

## 2. One-sided absolute-drift fibers

A length-`n` word has signed imbalance

\[
a\in\{-n,-n+2,\ldots,n\}.
\]

The number of words with that signed imbalance is

\[
\binom n{(n+a)/2}.
\]

Shell cardinality forgets the sign, so for an admissible absolute drift `d>=0`,

\[
\boxed{
W_n(d)=
\begin{cases}
\binom n{n/2},&d=0,\\
2\binom n{(n+d)/2},&d>0.
\end{cases}}
\]

Only values with

\[
0\le d\le n,
\qquad
d\equiv n\pmod2
\]

occur.

## 3. P022-CF01 — shell-energy fiber spectrum

For a represented drift energy

\[
Q=d_+^2+d_-^2,
\]

the microscopic two-sided fiber size is

\[
\boxed{
F_n(Q)
=
\sum_{\substack{d_+^2+d_-^2=Q\\
0\le d_\pm\le n\\
d_\pm\equiv n\pmod2}}
W_n(d_+)W_n(d_-).}
\]

Equivalently, without first quotienting signs,

\[
\boxed{
F_n(Q)=
\sum_{\substack{a^2+b^2=Q\\
a,b\equiv n\pmod2\\
|a|,|b|\le n}}
\binom n{(n+a)/2}
\binom n{(n+b)/2}.}
\]

This is a **binomial-weighted sum-of-two-squares spectrum**.

Because `Q -> S_n` is injective at fixed `n`, the shell-cardinality fiber spectrum is exactly the same spectrum with the energy labels relabelled by

\[
S_n=(42n^2+8-Q)/4.
\]

The fibers sum correctly:

\[
\boxed{
\sum_QF_n(Q)=4^n.}
\]

## 4. Generating polynomial

Define the one-sided weighted square polynomial

\[
\boxed{
\Phi_n(z)
=
\sum_{d\equiv n\ (2)}W_n(d)z^{d^2}.}
\]

Then the complete two-sided shell-energy spectrum is encoded by

\[
\boxed{
\Phi_n(z)^2
=
\sum_QF_n(Q)z^Q.}
\]

Thus shell-cardinality quotient fibers form a finite non-negative coefficient layer whose exponents are quadratic drift energies.

This is an arithmetic shadow of the same count-enriched philosophy seen in A4/P011: Boolean shell existence has already forgotten how many microscopic stacking histories produced each represented coordination state.

## 5. P022-CF02 — exact shell-cardinality extrema

The maximum possible drift energy occurs when both prefixes have constant sign:

\[
Q_{\max}=2n^2.
\]

Therefore the minimum possible Barlow shell cardinality is

\[
\boxed{
S_n^{\min}=10n^2+2.}
\]

FCC attains this bound at every radius.

The minimum admissible absolute one-sided drift is parity-forced:

\[
d_{\min}=
\begin{cases}
0,&n\text{ even},\\
1,&n\text{ odd}.
\end{cases}
\]

Hence

\[
Q_{\min}=
\begin{cases}
0,&n\text{ even},\\
2,&n\text{ odd}.
\end{cases}
\]

and the maximum possible shell cardinality is

\[
\boxed{
S_n^{\max}
=\left\lfloor\frac{21n^2}{2}\right\rfloor+2.}
\]

HCP attains this upper bound at every radius.

Thus every Barlow shell obeys the sharp interval

\[
\boxed{
10n^2+2
\le
S_n
\le
\left\lfloor\frac{21n^2}{2}\right\rfloor+2.}
\]

Neither extremizer is unique as a finite window: any two-sided prefix with the corresponding extreme drift magnitudes attains the same bound.

## 6. P022-CF03 — parity and arithmetic holes

The represented energies are far from arbitrary integers.

### Even radius

Every signed imbalance is even, so

\[
\boxed{Q\equiv0\pmod4.}
\]

Writing `a=2u`, `b=2v`, represented energies are

\[
Q=4(u^2+v^2).
\]

### Odd radius

Every signed imbalance is odd. Every odd square is `1 mod 8`, hence

\[
\boxed{Q\equiv2\pmod8.}
\]

These congruences are necessary but not sufficient. As the radius grows, additional holes remain because not every admissible integer in the congruence class is a sum of two bounded parity-compatible squares.

Therefore the possible shell-cardinality states form a discrete arithmetic subset of the sharp interval, not a contiguous set of integers.

This creates a direct bridge from finite precision geometry to classical sum-of-two-squares structure, but no classical number-theory novelty is claimed.

## 7. The shell-cardinality quotient is much coarser than final signed drift

For coordinate-sensitive extreme-layer support, the signed pair

\[
(\delta_n,\delta_{-n})
\]

is recoverable from first moments.

Whole-shell cardinality applies two successive losses:

1. each side is squared, erasing sign;
2. the two squares are added, erasing their allocation between sides.

The resulting quotient is

\[
\boxed{
(\delta_n,\delta_{-n})
\longmapsto
Q_n=\delta_n^2+\delta_{-n}^2
\longmapsto
S_n.}
\]

CF01 quantifies exactly how many microscopic ±1 histories survive inside every final fiber.

## 8. P011 / P023 / P024 relation

### P011

The shell-cardinality map is another finite functional quotient with an explicit fiber spectrum. Its generic collision statistics belong to P011; P022 supplies the weighted sum-of-two-squares specialization.

### P023/P024

Changing the observable from signed coordinate support to whole-shell cardinality changes the sufficient state from a signed drift pair to one quadratic energy. The coarsening is legal precisely because the future language no longer asks where or in which orientation the drift occurred.

### P022

P022 retains the Barlow-specific arithmetic constraints, sharp coordination bounds, and exact microscopic fiber weights.

## 9. Executable assets

Added:

- `src/enterprise_math/p022_barlow_coordination_fibers.py`;
- `tests/test_p022_barlow_coordination_fibers.py`.

The tests enumerate all short two-sided microscopic ±1 windows, verify the weighted sum-of-two-squares fiber formula, check total mass `4^n`, verify the sharp shell extrema, and confirm the existence of arithmetic holes beyond the parity congruences.
