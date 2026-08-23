# Prime-BRC Canonical MIN/MAX Birth Duality

Status: `L3 OWNER-LOCAL / PROVED STRUCTURAL THEOREM / NOT LEGENDRE`
Date: `2026-08-23`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

For a composite integer `n`, let

\[
\mathsf B(n)=\{d:d|n,\sqrt n\le d<n\}
\]

be its proper floor-birth fiber.

Define the two canonical extrema

\[
d_{\max}(n)=\max\mathsf B(n),
\qquad
 d_{\min}(n)=\min\mathsf B(n).
\]

## 1. MAX birth = least-factor provenance descent

The earlier max-birth theorem gives

\[
\boxed{
 d_{\max}(n)=\frac{n}{\operatorname{spf}(n)}.
}
\]

Thus MAX birth removes exactly one least prime factor, and repeated MAX birth recovers the ordered prime-factor provenance.

On a consecutive-square basin with root `K>=4`, canonical P017-L054 proves the MAX-child map is globally injective on composite basin states.

Hence MAX birth is the **provenance-preserving** canonical branch choice.

## 2. MIN birth = square-root-frontier descent

The MIN child is the least proper divisor at or above `sqrt(n)`.

### Theorem

For every composite `n`,

\[
\boxed{
 d_{\min}(n)\text{ is prime}
\quad\text{or}\quad
 d_{\min}(n)\le n^{2/3}.
}
\]

### Proof

If the largest prime factor

\[
q=P^+(n)>\sqrt n,
\]

then every divisor of `n` not involving `q` divides the complementary factor `n/q<sqrt(n)`, while every divisor involving `q` is at least `q`. Therefore `q` is the least upper proper divisor:

\[
d_{\min}(n)=q,
\]

which is prime.

Otherwise every prime factor of `n` is at most `sqrt(n)`. The balanced-divisor lemma provides a divisor

\[
a\in[n^{1/3},n^{1/2}],
\]

whose complement

\[
d=n/a
\]

belongs to the birth fiber and satisfies

\[
d\le n^{2/3}.
\]

Since `d_min` is the least birth child,

\[
d_{\min}(n)\le d\le n^{2/3}.
\]

∎

The exponent `2/3` is sharp: for `n=p^3`,

\[
\mathsf B(n)=\{p^2\},
\qquad
 d_{\min}(n)=p^2=n^{2/3}.
\]

## 3. MIN descent is canonical numerical compression

Repeated MIN-child evolution therefore gives a deterministic branch rule:

```text
if MIN child is prime -> terminate;
otherwise n -> d_min(n) <= n^(2/3).
```

Thus the earlier existential two-thirds descent can be implemented canonically on the exact birth support, without choosing a prime-factor subset externally.

The number of nonterminal numerical-scale steps is `O(log log n)`.

## 4. Provenance / compression tradeoff is real

MIN birth need not preserve the global identity of distinct square-basin roots.

Sharp small witness:

\[
K=4,
\qquad
18,24\in(4^2,5^2).
\]

Their proper birth fibers contain

\[
\mathsf B(18)=\{6,9\},
\qquad
\mathsf B(24)=\{6,8,12\},
\]

so

\[
\boxed{
 d_{\min}(18)=d_{\min}(24)=6.
}
\]

Thus MIN birth genuinely recoalesces two distinct basin states.

By contrast,

\[
d_{\max}(18)=9,
\qquad
 d_{\max}(24)=12,
\]

and the MAX rule is protected by the P017-L054 injectivity theorem for `K>=4`.

## 5. BRC interpretation

The same exact branch fiber supports two canonical but inequivalent operational readouts:

\[
\boxed{
\text{MAX birth}
=\text{provenance-preserving / least-factor path},
}
\]

\[
\boxed{
\text{MIN birth}
=\text{scale-compressing / square-root-frontier path}.
}
\]

This gives a concrete arithmetic example of a BRC design tradeoff:

```text
retain branch identity -> MAX / injective / deep provenance;
permit safe task-specific coalescence -> MIN / 2/3 scale contraction / shallow numeric depth.
```

MIN is not a valid replacement for MAX when downstream semantics require original-state provenance, because the `(18,24)->6` witness shows no-resurrection after coalescence.

Conversely, MAX needlessly preserves provenance when the downstream task only asks for rapid access to some prime leaf.

Freeze:

`MAX_BIRTH_IS_PROVENANCE_CANONICAL = true`.

`MIN_BIRTH_IS_NUMERIC_COLLAPSE_CANONICAL = true`.

`MIN_BIRTH_PRIME_OR_TWO_THIRDS = true`.

`MIN_MAX_OBJECTIVES_ARE_NOT_INTERCHANGEABLE = true`.
