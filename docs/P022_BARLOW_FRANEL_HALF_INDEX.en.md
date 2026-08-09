# P022 — Half-Index Franel Divisors and an Infinite Composite-Boundary Witness Family

Status: `ACTIVE RESEARCH NOTE / PROVED INFINITE SUBFAMILY / PRIOR-ART INPUT EXPLICIT`  
Owner: `program/p022-geometry-v2`  
Depends on: Franel p-Lucas/rank analysis; low-order Franel-defect reduction  
Cross-route relevance: P011 collision identifiability; A2/P023 witness precision; P018 defect/holonomy language

## 1. Question

The low-order Barlow identifiability problem has been reduced to multiplicative independence of the pure Franel defects

\[
2,\qquad D_n\quad(2n-1\text{ composite}).
\]

A strong sufficient route would give a primitive prime divisor of every relevant `F_n`, but that is substantially stronger than what is presently proved.

This note establishes a weaker but genuinely infinite theorem: there are infinitely many **composite-boundary** indices `n` for which `F_n` has a canonical prime divisor of the form

\[
p=2n+1.
\]

The proof uses the classical Jarvis--Verrill Franel mirror congruence, not finite determinant extension.

---

## 2. Prior-art input: the Franel mirror congruence

Let

\[
F_k=\sum_{j=0}^k\binom{k}{j}^3.
\]

Jarvis and Verrill proved that for every prime `p` and `0<=k<=p-1`,

\[
\boxed{
F_k\equiv(-8)^kF_{p-1-k}\pmod p.
}
\]

This congruence is prior art.  It is recorded, for example, in the Franel-congruence literature following Jarvis--Verrill's work on Apéry-like/supercongruence sequences.

P022's contribution below is the use of the fixed midpoint and residue arithmetic to generate an infinite family of witnesses on the **composite defect side** of the Barlow identifiability reduction.

---

## 3. P022-LI12 — forced half-index zero

Let `p` be an odd prime and put

\[
n=\frac{p-1}{2}.
\]

The midpoint is fixed by reflection:

\[
p-1-n=n.
\]

Therefore the Jarvis--Verrill congruence gives

\[
F_n\equiv(-8)^nF_n\pmod p.
\]

By Euler's criterion,

\[
(-8)^n
=(-8)^{(p-1)/2}
\equiv\left(\frac{-8}{p}\right)
=\left(\frac{-2}{p}\right)
\pmod p.
\]

The standard quadratic-character evaluation is

\[
\left(\frac{-2}{p}\right)
=
\begin{cases}
+1,&p\equiv1,3\pmod8,\\
-1,&p\equiv5,7\pmod8.
\end{cases}
\]

Hence if

\[
p\equiv5,7\pmod8,
\]

the midpoint relation becomes

\[
F_n\equiv-F_n\pmod p.
\]

Because `p` is odd,

\[
\boxed{
p\mid F_{(p-1)/2}.}
\]

This is an exact theorem.

Important boundary: the converse is **not** claimed here.  For residue classes `1,3 mod 8`, the mirror identity has multiplier `+1` and therefore imposes no midpoint vanishing condition.

---

## 4. P022-LI13 — infinitely many witnesses land on composite defect indices

We now require the Barlow defect boundary

\[
2n-1
\]

to be composite.

Choose a prime

\[
p\equiv5\ \text{or}\ 23\pmod{24},
\qquad p>5,
\]

and again put

\[
n=\frac{p-1}{2}.
\]

Both residue classes satisfy

\[
p\equiv5,7\pmod8,
\]

so LI12 gives

\[
p\mid F_n.
\]

They also satisfy

\[
p\equiv2\pmod3.
\]

Therefore

\[
2n-1=p-2\equiv0\pmod3.
\]

Since `p>5`, we have `p-2>3`, hence

\[
\boxed{2n-1\text{ is composite}.}
\]

Thus every prime `p>5` in either progression `5 mod 24` or `23 mod 24` produces a genuine composite-boundary segment `n=(p-1)/2` with a canonical divisor

\[
\boxed{p=2n+1\mid F_n.}
\]

By Dirichlet's theorem on primes in arithmetic progressions, both reduced residue classes contain infinitely many primes.  Therefore:

\[
\boxed{
\text{There are infinitely many composite-boundary }n
\text{ with }(2n+1)\mid F_n.
}
\]

This is the first infinite arithmetic family produced on the density-one composite side of the current defect program; it does **not** solve all composite indices.

---

## 5. P022-LI14 — mirror symmetry of the Franel zero digits

The multiplier `(-8)^k` is nonzero modulo `p`.  Hence the same mirror congruence gives

\[
\boxed{
F_k\equiv0\pmod p
\iff
F_{p-1-k}\equiv0\pmod p.
}
\]

So the zero-digit set

\[
Z_p=\{1\le k\le p-1:p\mid F_k\}
\]

is symmetric under

\[
k\longmapsto p-1-k.
\]

For `p=5,7 mod 8`, the midpoint belongs to `Z_p`; hence the Franel rank of apparition satisfies

\[
\boxed{
r_p\le\frac{p-1}{2}.}
\]

Together with p-Lucas, this means every prime in those two residue classes is a non-Type-I Franel prime: its digit table has at least one zero.

---

## 6. The primitive-divisor boundary remains real

LI12 does **not** say that `p=2n+1` is primitive at `F_n`.

The smallest useful warning is

\[
p=29,\qquad n=14.
\]

The midpoint theorem gives

\[
29\mid F_{14},
\]

but in fact

\[
29\mid F_{12}
\]

already.  Therefore

\[
r_{29}=12<14.
\]

So the implications are only

\[
\text{forced half-index divisor}
\not\Rightarrow
\text{primitive divisor}.
\]

This distinction matters because the primitive-divisor criterion would triangularize the full defect family, whereas LI13 only supplies an infinite family of exact local divisibility witnesses.

---

## 7. Stronger defect-valuation pattern — conjectural only

Exact pressure tests suggest a stronger phenomenon for the LI13 family:

\[
\boxed{
v_p(D_{(p-1)/2})=1}
\]

for tested primes `p=5 or 23 mod 24`, even when `p` is not primitive for `F_n`.

For example `p=29` already divides `F_12`, yet the pure defect at `n=14` still has `29`-adic valuation one.

This would be much stronger than LI13 because it would say the canonical A-elimination fails to cancel the half-index witness.  At present P022 has **no global proof**, so the statement remains

`CONJECTURAL / PRESSURE-TEST TARGET`.

A proof should come from the Franel mirror/recurrence/p-Lucas structure or from the transfer-defect holonomy, not from extending the finite determinant cutoff.

---

## 8. Why this changes the global strategy

The composite side is no longer completely opaque.

We now have three arithmetic mechanisms:

1. `2n-1 prime`: automatic central-binomial A-pivot;
2. `2n+1 prime` in `5 or 23 mod 24`: forced Franel divisor at a composite A-boundary;
3. arbitrary composite indices: pure Franel defect `D_n`, with global independence still open.

The second mechanism supplies infinitely many exact anchors *inside* the composite regime.  It therefore gives a new route for studying how local Franel congruences interact with the defect transfer map.

The next high-value target is to decide whether the stronger one-unit defect valuation can be proved for this infinite family, and then whether analogous residue families exist beyond the midpoint construction.

---

## 9. Prior-art / novelty boundary

Established inputs:

- Jarvis--Verrill mirror congruence for Franel numbers;
- Euler's criterion and quadratic-character evaluation of `(-2/p)`;
- Dirichlet's theorem on primes in arithmetic progressions.

P022-specific content:

- routing the midpoint congruence into the composite-boundary Franel-defect program;
- isolating the residue classes `5,23 mod 24` as an infinite composite-boundary witness family;
- separating this exact divisibility theorem from the stronger primitive/defect-valuation conjectures.

Historical novelty of this packaging remains `NOVELTY_UNVERIFIED`.

## 10. Executable assets

Added:

- `src/enterprise_math/p022_barlow_franel_half_index.py`;
- `tests/test_p022_barlow_franel_half_index.py`.

The executable checks reconstruct the mirror congruence directly from exact Franel integers on small primes, verify the forced half-index residue classes, test the composite-boundary arithmetic, and retain `p=29` as the explicit nonprimitive boundary case.
