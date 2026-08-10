# P022 — Franel p-Lucas Divisibility Basins

Status: `ACTIVE RESEARCH NOTE / EXACT DIGIT COUNT / PRIOR-ART INPUT EXPLICIT`  
Owner: `program/p022-geometry-v2`  
Depends on: Franel p-Lucas factorization; half-index witness theorem  
Cross-route relevance: P011 collision fibers; P018/P023 predictive quotients; P024 observation-language precision

## 1. Setup

For a prime `p`, define the Franel digit-zero set

\[
Z_p=\{1\le d\le p-1:F_d\equiv0\pmod p\},
\qquad
z_p=|Z_p|.
\]

The p-Lucas factorization for Franel numbers says that if

\[
N=n_0+n_1p+\cdots+n_{L-1}p^{L-1},
\qquad0\le n_i<p,
\]

then

\[
\boxed{
F_N\equiv\prod_{i=0}^{L-1}F_{n_i}\pmod p.
}
\]

The p-Lucas property is established prior art for this Apéry-like/Franel sequence.  P022 uses it here as an exact finite-state counting law.

---

## 2. P022-LI15 — exact block count

Because

\[
F_0=1,
\]

a base-`p` digit contributes a zero factor exactly when it belongs to `Z_p`.

Therefore

\[
p\nmid F_N
\]

if and only if **every** base-`p` digit of `N` avoids `Z_p`.

Among the complete block

\[
0\le N<p^L,
\]

there are `L` independent digit positions, and each has exactly

\[
p-z_p
\]

allowed nonzero digits.  Hence

\[
\boxed{
\#\{0\le N<p^L:p\nmid F_N\}
=(p-z_p)^L.
}
\]

Equivalently,

\[
\boxed{
\#\{0\le N<p^L:p\mid F_N\}
=p^L-(p-z_p)^L.
}
\]

This is an exact integer identity for every `L>=0`.

---

## 3. P022-LI16 — Franel prime-divisibility zero--one law

There are only two possibilities.

### Type I: no zero digit

If

\[
Z_p=\varnothing,
\]

then p-Lucas gives

\[
\boxed{p\nmid F_N\quad\text{for every }N\ge0.}
\]

So a prime that is absent from the first digit table `F_1,...,F_(p-1)` is absent from the entire Franel sequence.

### Type II: at least one zero digit

If

\[
z_p\ge1,
\]

then the fraction of nonzero terms in a complete `p^L` block is

\[
\left(1-\frac{z_p}{p}\right)^L,
\]

which tends to zero exponentially in digit depth.  Therefore

\[
\boxed{
\frac{\#\{0\le N<p^L:p\mid F_N\}}{p^L}
\longrightarrow1.
}
\]

The same digit bound between consecutive powers of `p` shows that the full natural density exists and equals one:

\[
\boxed{
\operatorname{dens}\{N\ge0:p\mid F_N\}=1.
}
\]

Thus Franel divisibility exhibits a sharp p-Lucas dichotomy:

\[
\boxed{
\text{never appears}
\quad\text{or}\quad
\text{appears on a density-one set of indices}.}
\]

This statement concerns divisibility by a **fixed prime** while the index tends to infinity.

---

## 4. P022-LI17 — forced half-index primes generate density-one basins

The half-index theorem proves that for

\[
p\equiv5,7\pmod8,
\]

we have

\[
\frac{p-1}{2}\in Z_p.
\]

Hence

\[
z_p\ge1,
\]

and LI16 immediately yields

\[
\boxed{
\operatorname{dens}\{N:p\mid F_N\}=1
\qquad(p\equiv5,7\pmod8).}
\]

Even the single forced midpoint digit gives the explicit finite lower bound

\[
\boxed{
\#\{0\le N<p^L:p\mid F_N\}
\ge p^L-(p-1)^L.}
\]

If additional zero digits exist, the exact LI15 count is stronger.

Example:

\[
Z_{29}=\{12,14,16\}.
\]

Therefore on every `29^L` block,

\[
\boxed{
\#\{N<29^L:29\nmid F_N\}=26^L,
}
\]

not merely `28^L`.

---

## 5. Mirror symmetry refines the digit basin

Jarvis--Verrill gives

\[
F_d\equiv0\pmod p
\iff
F_{p-1-d}\equiv0\pmod p.
\]

Thus `Z_p` is reflection invariant.

For `p=5,7 mod 8`, the midpoint `(p-1)/2` is a fixed zero digit.  All other zero digits occur in reflected pairs, so

\[
\boxed{z_p\text{ is odd}.}
\]

The midpoint family is therefore the minimal odd zero-set case `z_p=1`; primes such as `29` exhibit larger odd digit alphabets.

---

## 6. Consequence for primitive divisors

A primitive prime divisor of `F_n` is only the **first opening event** of its p-Lucas basin.

Once a prime `p` first appears at digit `r_p`, every integer whose base-`p` expansion contains any digit in `Z_p` is subsequently divisible by `p`.  In particular a primitive marker is not expected to remain globally private.

This explains, structurally, why finite private-marker rows in the length-150 valuation certificate can be extremely useful even though p-Lucas guarantees eventual recurrence.

The right distinction is:

\[
\boxed{
\text{first-appearance information}
\neq
\text{long-run divisibility frequency}.}
\]

---

## 7. Precision interpretation

The theorem is an exact example of a small local state controlling a huge future language.

For fixed `p`, the complete future divisibility observable

\[
N\longmapsto\mathbf1_{p\mid F_N}
\]

is determined by the finite digit alphabet `Z_p`.  One does not need the full Franel integers at future indices; it is enough to inspect the base-`p` digits and ask whether any digit belongs to the zero set.

So the p-Lucas quotient turns a global infinite sequence question into a finite-state language-recognition problem:

\[
\boxed{
\text{finite zero-digit set}
\to
\text{exact infinite divisibility language}.}
\]

This is a P022 specialization of task-relative future-compatible state compression.  Any generic automaton/quotient theorem belongs upstream in A2/P023 rather than being duplicated here.

---

## 8. Prior-art / novelty boundary

Prior art includes Lucas' theorem and the p-Lucas factorization known for Franel/generalized Apéry sequences.

P022-specific content is the exact block-count/density interpretation within the current Franel-defect and precision program, together with its combination with the new forced half-index witness family.

Historical novelty of this packaging remains `NOVELTY_UNVERIFIED`.

## 9. Executable assets

Updated/added:

- `src/enterprise_math/p022_barlow_franel_lucas_rank.py`;
- `tests/test_p022_barlow_franel_lucas_rank.py`.

The implementation uses only integer Franel values and base-`p` digit products.  The tests verify the p-Lucas factorization on small blocks and the exact counts for `p=5` and `p=29`.
