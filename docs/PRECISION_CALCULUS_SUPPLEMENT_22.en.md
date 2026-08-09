# Precision Calculus — Supplement 22

Status: `ACTIVE RESEARCH NOTE`  
Scope: quotient-path flatness and strict square-root descent after P018-T182  
Depends on: P018-T182, P007 discrete division, and the canonical natural-number quotient law `Nat.div_div_eq_div_mul`  
Discipline: the floor-division composition identity is established arithmetic and is **not** claimed as new. The project-specific content is its use with T182 to collapse apparent multi-stage root branching, together with the square-basin strict-descent consequence.

> **Concurrent-numbering resolution.** This note entered `main` from the same concurrent QuotientBasin route under provisional labels `Supplement 13 / T111–T112`, while PR #68 already had earlier validated T111–T112 results. The integrated branch preserves that established #68 numbering and relabels only this later concurrent continuation as **Supplement 22 / T195–T196**. Its mathematics and formal theorem names are unchanged.

## 1. Why T182 does not create a binary-tree explosion

T182 says that a single nontrivial quotient of one square basin can meet at most two adjacent square-root indices.

A naive recursive reading could suggest that after `h` successive factor extractions the number of possible final square-root indices might grow like `2^h`.

That is false already at the quotient-state level.

For natural-number floor division,

\[
\boxed{
\left\lfloor
\frac{\left\lfloor n/a\right\rfloor}{b}
\right\rfloor
=
\left\lfloor\frac{n}{ab}\right\rfloor.
}
\]

This is the standard Euclidean quotient identity formalized in mathlib as `Nat.div_div_eq_div_mul`. It is established mathematics.

Its significance here is structural: a sequence of quotient steps has an exact one-step representative given by the product divisor.

---

## 2. P018-T195 — Quotient-path flatness

Status: `PROVED / CLASSICAL QUOTIENT IDENTITY + PROJECT CONSEQUENCE`.

For all natural numbers `n,a,b`,

\[
\boxed{
Q_b(Q_a(n))=Q_{ab}(n),
}
\]

where `Q_d(n)=floor(n/d)`.

By induction, for any finite list of nonzero divisors

\[
d_1,\ldots,d_h,
\]

one has

\[
\boxed{
Q_{d_h}\circ\cdots\circ Q_{d_1}
=
Q_{d_1\cdots d_h}.
}
\]

The identity itself is prior arithmetic. The P018 consequence comes from combining it with T182.

Suppose

\[
k^2\le n<(k+1)^2,
\qquad a,b\ge2,
\]

and set

\[
D=ab,
\qquad
j=R_2\!\left(\left\lfloor\frac{k^2}{D}\right\rfloor\right).
\]

Then

\[
\boxed{
R_2\!\left(
\left\lfloor
\frac{\left\lfloor n/a\right\rfloor}{b}
\right\rfloor
\right)
\in\{j,j+1\}.
}
\]

Thus two quotient stages do **not** create four final root-index branches. They flatten to one quotient by `ab`, to which T182 applies once.

The same logic holds for any finite quotient path: its final quotient state depends only on the total product divisor, so the final square-root image is still controlled by one two-basin T182 bound.

This does not say that intermediate states are identical across different factorizations. It says that the final quotient projection is path-flat with respect to factorization of the total divisor.

---

## 3. P018-T196 — Actual quotient root strictly descends for k >= 3

Status: `PROVED`.

T182 gives a base root `j<k` but formally allows the actual quotient root to be `j+1`, which in principle could equal `k`.

For square basins from `k>=3`, that edge case cannot occur.

Let

\[
k\ge3,
\qquad d\ge2,
\qquad n<(k+1)^2.
\]

Then

\[
(k+1)^2\le2k^2\le dk^2.
\]

Hence

\[
n<dk^2,
\]

so exact floor division gives

\[
\left\lfloor\frac nd\right\rfloor<k^2.
\]

Therefore

\[
\boxed{
R_2\!\left(\left\lfloor\frac nd\right\rfloor\right)<k.
}
\]

This is strict descent of the **actual transported state**, not merely of T182's base index.

The cases `k=1,2` remain finite base cases and need no asymptotic or recursive treatment.

---

## 4. Combined well-founded quotient skeleton

T182, T195, and T196 now give a compact operation-level picture.

For every square basin with `k>=3` and every nontrivial divisor `d>=2`:

1. quotient transport is exact and integer-only;
2. a whole basin meets at most two adjacent target root indices;
3. the actual target root index is strictly smaller than `k`;
4. splitting `d` into several quotient stages does not multiply the number of possible final root indices, because the stages flatten to one quotient by the product.

Symbolically,

\[
\boxed{
B_k
\xrightarrow{Q_{d_1}}
\cdots
\xrightarrow{Q_{d_h}}
Q_D(B_k),
\qquad
D=\prod_i d_i,
}
\]

with

\[
\boxed{
Q_D(B_k)
\text{ meeting at most two adjacent root indices, while the actual final root is below }k
}
\]

for `k>=3`.

The essential point is not that quotienting is small in magnitude. It is that the square-root precision coordinate carries a **well-founded descent** while quotient factorization itself is flat at the final state.

---

## 5. P017 lower-band implication

Return to a square-basin composite

\[
n=pq,
\]

where `p` is its least prime factor.

T182 gives

\[
j=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right),
\qquad
R_2(q)\in\{j,j+1\}.
\]

If `k>=3`, T196 strengthens this to

\[
\boxed{R_2(q)<k.}
\]

If `q` is still composite and `ell` is its least prime factor, the ordinary root-factor horizon at the lower state gives

\[
\ell\le R_2(q).
\]

Because `p` was the least prime factor of `n`, also `p<=ell`. Hence

\[
\boxed{
p\le\ell\le R_2(q)<k.
}
\]

So least-factor extraction simultaneously lowers the root scale and shrinks the range available to the next least prime factor.

This is the intended bridge back to the P017 lower band. It is still not a Legendre proof: a useful recursive **mass bound** must be derived from this shrinking state space rather than merely enumerating the recursive branches.

---

## 6. What is and is not new

Not claimed:

- Euclidean floor division;
- `floor(floor(n/a)/b)=floor(n/(ab))`;
- `Nat.div_div_eq_div_mul` or its formalization;
- generic well-founded induction on natural numbers.

Project-specific content under test:

- using quotient-path flatness to show that repeated T182 transport does not create exponential final root-scale branching;
- the exact square-basin strict-root descent of T196;
- the coupling of this descent to the least-factor horizon in the P017 lower band.

Historical novelty remains `NOVELTY_UNVERIFIED`.

---

## 7. Executable and formal validation

The Python layer extends `src/enterprise_math/quotient_basin.py` with:

- `iterated_quotient_flatness`;
- `square_basin_iterated_quotient_transport`;
- `strict_square_root_descent`.

The tests verify bounded multi-step paths, factorization-independent final quotients, the retained two-root bound, and strict descent from `k>=3`.

The Lean module extends `EnterpriseMath.Precision.QuotientBasin` with:

- `quotient_path_flat_two`;
- `square_basin_two_step_div_root_pair`;
- `square_basin_div_root_strict`.

The formal layer intentionally proves the minimal two-stage path identity and its T182 consequence. Longer paths follow by ordinary induction and should not be expanded into redundant theorem families unless later applications require them.

---

## 8. Next target

The next meaningful QuotientBasin research step is no longer to prove that lower-band factor extraction descends; T182/T195/T196 already supply that skeleton.

The remaining problem is quantitative:

> Can the shrinking root scale and shrinking admissible least-factor interval be converted into a recursive upper bound on the total lower-band composite mass that is genuinely stronger than standard Buchstab/least-factor bookkeeping?

A candidate recursion must be pressure-tested against established sieve theory. If it merely rewrites ordinary least-factor recursion in square-root coordinates, it should be demoted rather than expanded.
