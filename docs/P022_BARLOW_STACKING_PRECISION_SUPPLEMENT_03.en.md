# P022 Barlow Stacking Precision Supplement 03 — Aperiodic Drift Theorem

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE FORMULA + ASYMPTOTIC GENERALIZATION / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: Barlow BG01 exact target-layer contribution  
Scope: arbitrary bi-infinite Barlow interface words with asymptotic one-sided absolute drift densities

## 1. Periodicity is stronger than the growth theorem needs

Periodic Barlow stacking supplied two different benefits:

1. the prefix imbalance had a linear drift plus bounded phase, which was enough to determine the exponential shell-total geodesic growth rate;
2. the finite phase repeated exactly, which was strong enough to produce a rational generating function and constant recurrence.

Only the first ingredient is needed for the growth exponent.

Therefore the drift-controlled growth law extends to aperiodic and disordered stacking words whenever their long-run absolute prefix drift is well defined.

## 2. Arbitrary two-sided stacking word

Let every upward interface `j -> j+1` carry a sign

\[
\sigma_j\in\{-1,+1\},
\qquad j\in\mathbb Z.
\]

Define the effective root-to-layer imbalance by

\[
\delta_0=0,
\]

\[
\delta_k=\sum_{j=0}^{k-1}\sigma_j
\qquad(k>0),
\]

and, because downward traversal reverses interface offsets,

\[
\delta_{-q}
=-\sum_{j=-q}^{-1}\sigma_j
\qquad(q>0).
\]

No periodicity, stationarity, probability law, or frequency assumption is imposed at this stage.

For every finite graph shell radius `n`, only the finite imbalance window

\[
(\delta_{-n},\ldots,\delta_n)
\]

is required.

## 3. P022-BGA01 — BG01 is fully aperiodic

For target layer `k`, put

\[
q=|k|,
\qquad d=|\delta_k|,
\qquad c=(q-d)/2.
\]

The Barlow prefix normal form

\[
P_k=(A+3)^cB_\pm^d
\]

used only commutativity of the finite interface polynomial product. It did not use periodicity.

Therefore the exact layer-shell formula remains valid for every arbitrary stacking word.

For `q=n`,

\[
\boxed{L_n(k)=3^n.}
\]

For `q<n`,

\[
\boxed{
L_n(k)=\binom nq
\left(
3\cdot2^{n-q+c}(1+2^d)-6
\right).
}
\]

Hence

\[
\boxed{
T_n=\sum_{k=-n}^{n}L_n(k)
}
\]

for the whole shell.

This is an exact finite theorem for arbitrary two-sided Barlow stacking.

## 4. One-sided asymptotic drift densities

Assume the following two limits exist:

\[
\boxed{
\mu_+=\lim_{k\to+\infty}\frac{|\delta_k|}{k},
}
\]

and

\[
\boxed{
\mu_-=\lim_{q\to+\infty}\frac{|\delta_{-q}|}{q}.
}
\]

Because every increment is `±1`,

\[
0\le\mu_+,\mu_-\le1.
\]

The two limits are allowed to differ. The stacking can have different asymptotic drift on the two sides of the chosen root layer.

Define

\[
\boxed{
\mu_*=\max(\mu_+,\mu_-).}
\]

## 5. P022-BGA02 — one-sided shell-growth law

Consider only positive target layers. Let

\[
T_n^+=\sum_{k=1}^{n-1}L_n(k)
\]

and ignore the single extreme layer for the moment.

For every `epsilon>0`, there exists `Q` such that for all `q>=Q`,

\[
(\mu_+-\epsilon)q
\le
|\delta_q|
\le
(\mu_++\epsilon)q.
\]

The factor

\[
2^{-q/2}
\left(2^{|\delta_q|/2}+2^{-|\delta_q|/2}\right)
\]

is monotone in `|delta_q|`. Therefore the exact BG01 layer contributions for all sufficiently high positive layers are squeezed between the same binomial sums obtained by replacing the actual drift by `mu_+-epsilon` and `mu_++epsilon`.

The finitely many layers `q<Q` contribute at most a polynomial in `n` times `2^n`, whose exponential base is `2` and is therefore negligible.

The periodic proof's binomial identity applies directly to the comparison sums. Thus

\[
\liminf_{n\to\infty}(T_n^+)^{1/n}
\ge
2+2^{(1+\mu_+-\epsilon)/2},
\]

and

\[
\limsup_{n\to\infty}(T_n^+)^{1/n}
\le
2+2^{(1+\mu_++\epsilon)/2}.
\]

Let `epsilon -> 0`:

\[
\boxed{
\lim_{n\to\infty}(T_n^+)^{1/n}
=2+2^{(1+\mu_+)/2}.}
\]

The negative half-shell has the identical theorem with `mu_-`.

## 6. P022-BGA03 — aperiodic two-sided growth theorem

The full shell total is the sum of:

- the positive half-shell;
- the negative half-shell;
- the central layer;
- the two extreme target layers.

The central triangular-layer contribution has exponential base `2`; the extreme vertical layers have base `3`.

For any `mu in [0,1]`,

\[
2+2^{(1+\mu)/2}
\ge
2+\sqrt2
>3.
\]

Therefore neither central nor extreme layers can dominate the asymptotic shell total.

The sum of the two half-shells is dominated exponentially by the larger of their two rates. Hence

\[
\boxed{
\lim_{n\to\infty}T_n^{1/n}
=
2+2^{(1+\mu_*)/2},
\qquad
\mu_*=\max(\mu_+,\mu_-).
}
\]

This removes periodicity entirely from the growth-rate theorem.

## 7. Consequences

### Balanced but nonperiodic stacking

If

\[
|\delta_k|=o(|k|)
\]

in both directions, then

\[
\mu_+=\mu_-=0
\]

and therefore

\[
\boxed{
\lim T_n^{1/n}=2+\sqrt2.}
\]

So HCP's geodesic-growth exponent is shared by every asymptotically balanced Barlow word, not merely by periodic zero-drift stackings.

The finite shell spectra can remain completely different.

### Fully drifting stacking

If

\[
|\delta_k|/|k|\to1
\]

in the dominant direction, then

\[
\boxed{
\lim T_n^{1/n}=4,}
\]

the FCC constant-drift exponent.

### Asymmetric root environment

If the two sides have different limits, only the larger absolute drift determines the total exponential rate. The lower-drift side survives in finite/subdominant structure but not in the leading growth exponent.

## 8. Precision hierarchy after removing periodicity

The distinction between finite and asymptotic future languages becomes sharper.

### Exact finite radius `n`

State required:

\[
(|\delta_{-n}|,\ldots,|\delta_n|).
\]

### Infinite asymptotic growth rate

If one-sided drift limits exist, the entire infinite trajectory collapses to just

\[
\boxed{(\mu_+,\mu_-)}
\]

and the total growth language then collapses further to

\[
\boxed{\mu_*=\max(\mu_+,\mu_-).}
\]

For periodic words, each `mu` is rational and may be stored exactly as integer numerator/denominator. For arbitrary aperiodic words the limit can be irrational or otherwise not finitely representable by one integer pair; the theorem is about the mathematical quotient, not a claim that every asymptotic drift value has a finite exact encoding.

This is an important precision boundary:

> **finite exact geometry remains integer and finite at every radius, while an infinite asymptotic observable can legitimately introduce a limit object that is not itself a finite integer state.**

The project should not confuse those two levels.

## 9. Periodicity is exactly what buys recurrence closure

The aperiodic drift theorem retains the dominant exponential rate but generally loses the finite constant recurrence of BG04.

Periodic stacking gives exact affine imbalance on finitely many residue classes:

\[
\delta_{mL+r}=mD+\delta_r,
\]

which is what makes root-of-unity filtering possible and yields a rational generating function.

An arbitrary sequence with only

\[
|\delta_k|/|k|\to\mu
\]

need not have repeating phase coefficients, so no constant recurrence follows from the drift limit alone.

Thus there is another exact hierarchy:

\[
\text{drift limit}
\Rightarrow
\text{growth exponent},
\]

but

\[
\boxed{
\text{periodic finite phase}
\Rightarrow
\text{rational generating function / C-finite recurrence}.}
\]

The converse is not claimed.

## 10. Relation to disordered close packing

This theorem makes the P022 invariant applicable to deterministic nonperiodic and disordered close-packed stackings without first replacing them by a periodic approximant.

It does **not** impose a probability model. If a later application introduces a stochastic stacking law and independently proves an almost-sure drift density, BGA03 can be applied pathwise to almost every realized stacking word.

Any probabilistic law remains external to the present integer graph geometry.

## 11. Executable support

Added:

- `src/enterprise_math/p022_barlow_aperiodic.py`;
- `tests/test_p022_barlow_aperiodic.py`.

The finite executable layer exposes BG01 directly as a function of `(radius, target_layer, imbalance)` and reconstructs whole-shell totals from an arbitrary finite two-sided imbalance trajectory. Periodic stackings are verified to factor through this generic finite state exactly.
