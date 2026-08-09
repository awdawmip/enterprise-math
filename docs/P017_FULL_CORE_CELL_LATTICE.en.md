# P017 Full-Core Cell Lattice

Status: `ACTIVE DISCOVERY NOTE`  
Scope: partial/full smooth-core mirror cells, lcm intersection closure, divisor-poset inversion, and a negative boundary for overlap-only attacks  
Depends on: canonical P017 L020 full smooth-core decomposition, L053 full-core CRT capacity, L054 exact quotient-window separation, and the current residual hard-core program  
Novelty: `NOVELTY_UNVERIFIED`  
Discipline: divisor lattices, the Chinese remainder theorem, zeta transforms, and Möbius inversion are classical. This note does **not** prove Legendre's conjecture.

## 1. Why study cell intersections?

The current residual P017 hard core attaches to each anchor-surviving mirror radius

\[
1\le r<k,
\qquad M=k(k+1),
\]

two exact full `k`-smooth cores

\[
S_-(r),\qquad S_+(r).
\]

Canonical L053 uses the exact product `S_-(r)S_+(r)` as a full-core CRT modulus. The current hard-core discovery line then shows that a residual exact cell with product below `k` is a locally admissible affine two-linear-form problem. A natural next idea is to exploit overlaps among many *partial* core cells globally.

The purpose of this note is to test that idea before treating it as a new source of proof strength.

The outcome is sharp:

> **partial-cell overlaps are exactly lcm refinement, and their complete inclusion–exclusion is exactly the divisor-poset reconstruction of the already-existing exact full-core strata.**

So overlap bookkeeping by itself is not a new global coupling mechanism.

---

## 2. Partial oriented core cells

Call a positive odd integer `a` an admissible partial core when every prime factor of `a` is at most `k` and

\[
\gcd(a,M)=1.
\]

For two admissible partial cores `a,b` with

\[
\gcd(a,b)=1,
\]

define the oriented anchor-surviving cell

\[
\boxed{
C_k(a,b)
=
\{1\le r<k:
\gcd(r,M)=1,
\ a\mid M-r,
\ b\mid M+r\}.
}
\]

Because `M` is even and an anchor-surviving `r` is automatically odd, the unfiltered divisibility/parity condition is one CRT residue class modulo

\[
\boxed{2ab.}
\]

The anchor condition can only delete members of this arithmetic progression.

The exact full-core cell for a pair `(A,B)` is

\[
E_k(A,B)
=
\{r:S_-(r)=A,\ S_+(r)=B\}.
\]

The sets `E_k(A,B)` partition all anchor-surviving radii.

---

## 3. CC01 — Cell intersections are sidewise lcm promotion

Status: `PROVED`.

Take two admissible partial cells

\[
C_k(a,b),\qquad C_k(c,d),
\]

and put

\[
A=\operatorname{lcm}(a,c),
\qquad
B=\operatorname{lcm}(b,d).
\]

Then

\[
\boxed{
C_k(a,b)\cap C_k(c,d)
=
\begin{cases}
\varnothing,&\gcd(A,B)>1,\\
C_k(A,B),&\gcd(A,B)=1.
\end{cases}
}
\]

### Proof

A radius in both cells satisfies

\[
a,c\mid M-r,
\qquad
b,d\mid M+r,
\]

which is equivalent to

\[
A\mid M-r,
\qquad
B\mid M+r.
\]

If an odd prime `p` divided both `A` and `B`, then it would divide both mirror states and therefore their sum `2M`. All core primes are transverse to `M`, so this is impossible. Hence such a cross-side conflict makes the intersection empty.

When `gcd(A,B)=1`, the combined divisibility conditions are exactly the definition of `C_k(A,B)`, with the same anchor filter. ∎

### Strict refinement multiplies the modulus by at least three

Order labels componentwise by divisibility:

\[
(a,b)\preceq(A,B)
\iff a\mid A\text{ and }b\mid B.
\]

If the refinement is strict, then

\[
\frac{AB}{ab}
\]

is an odd integer larger than one, hence at least three. Therefore the raw radius modulus `2ab` grows by at least a factor of three at every strict refinement step.

---

## 4. CC02 — The exact full-core pair is the maximal represented label

Status: `PROVED`.

For every anchor-surviving radius `r`,

\[
\boxed{
r\in C_k(a,b)
\iff
a\mid S_-(r)\text{ and }b\mid S_+(r).
}
\]

### Proof

Every prime factor of `a` and `b` is at most `k`. Therefore divisibility by `a` on the lower side is exactly divisibility by `a` inside the canonical full `k`-smooth core `S_-(r)`, and similarly on the upper side. ∎

Consequently the pair

\[
\boxed{(S_-(r),S_+(r))}
\]

is the unique maximal partial-core label represented by `r`.

This is a finite-precision interpretation of the existing full-core state: partial cells remember only selected divisibility facts; lcm refinement accumulates those facts; the exact full-core pair is the terminal label.

---

## 5. CC03 — Partial counts are the two-dimensional zeta transform of exact strata

Status: `PROVED`.

Let

\[
c_k(a,b)=|C_k(a,b)|,
\qquad
e_k(A,B)=|E_k(A,B)|.
\]

CC02 gives the exact finite identity

\[
\boxed{
c_k(a,b)
=
\sum_{\substack{A:a\mid A\\B:b\mid B}}
e_k(A,B).
}
\]

Only finitely many exact labels occur because there are only `k-1` candidate radii.

This is the ordinary zeta transform on the product of two divisibility posets.

By ordinary Möbius inversion in each coordinate,

\[
\boxed{
e_k(a,b)
=
\sum_{u\ge1}\sum_{v\ge1}
\mu(u)\mu(v)\,
c_k(au,bv),
}
\]

with only finitely many nonzero terms.

Thus the entire family of exact full-core cell counts is information-equivalent to the entire family of partial-cell counts.

No new number-theoretic novelty is claimed for zeta/Möbius inversion itself.

---

## 6. CC04 — Residual refinement has logarithmic height

Status: `PROVED`.

Inside the residual hard-core region one retains only labels satisfying

\[
ab<k.
\]

Along any strict refinement chain

\[
(a_0,b_0)
\prec(a_1,b_1)
\prec\cdots\prec(a_h,b_h)
\]

that remains residual, CC01 implies

\[
\boxed{3^h a_0b_0<k.}
\]

Hence the number of strict refinement steps is finite and bounded by the largest integer `h` satisfying the displayed inequality.

This is useful as a precision-depth statement, but it is not a Legendre capacity deficit: branching among incomparable partial labels may still be large.

---

## 7. Negative boundary for the proposed cross-cell-overlap route

The previous sections close one tempting route.

Suppose one tries to obtain new global leverage solely by:

1. counting many partial candidate cells;
2. correcting their overlaps by pairwise/higher inclusion–exclusion;
3. interpreting overlap loss as a new cross-cell resource deficit.

CC01–CC03 show that this procedure does not create a new invariant. Every overlap is another lcm-refined cell, and complete inclusion–exclusion is exactly the Möbius reconstruction of the exact full-core strata already present in L020/L053.

Therefore

\[
\boxed{
\text{candidate-cell overlap algebra}
=
\text{full-core divisibility refinement in another coordinate.}
}
\]

The current affine hard-core result then applies separately to each exact residual stratum. Its local odd-prime wheel is admissible, so merely continuing the same divisor/CRT refinement cannot eliminate that exact cell.

This is a **route-pruning theorem**, not a failure of the broader hard-core program.

The next useful coupling must compare **different exact full-core strata after maximal refinement**. It must use information not contained in the product-divisibility zeta transform, for example:

- common-center relations among their large prime tails;
- the disjoint root-channel geometry exposed by the P017/P018 hard-core bridge;
- a global invariant linking several exact cells in the same original square basin;
- or an explicit nonlocal analytic input.

---

## 8. Relation to Enterprise Math foundations

This P017 specialization gives a clean bottom-layer pattern:

\[
\text{partial observable}
\to
\text{lcm/join refinement}
\to
\text{exact terminal label}
\to
\text{Möbius inversion between coarse and exact counts}.
\]

It also illustrates a central research discipline: a finer coordinate system is useful only if it changes what can be proved. Here the apparent cross-cell overlap structure collapses exactly to an already-known terminal state, so it should not be promoted as an independent source of explanatory power.

That lesson is reusable in P018/P023 precision work: before treating overlap corrections as a new state variable, first test whether they are simply the zeta transform of a known maximal refinement.

---

## 9. Executable validation

`src/enterprise_math/p017_core_cell_lattice.py` and `tests/test_p017_core_cell_lattice.py` check that:

- the raw partial-core cell is one odd CRT progression modulo `2ab`;
- CC01 lcm intersection closure holds, including cross-side conflict emptiness;
- exact full-core labels partition anchor-surviving radii;
- CC02 membership agrees with divisibility of exact full cores;
- CC03 partial counts equal exact-stratum zeta sums;
- double Möbius inversion reconstructs exact stratum counts;
- CC04 factor-three refinement depth is exact as an upper bound.

Finite tests audit the implementation. The mathematical statements follow from divisibility, CRT, the canonical full-core definition, and ordinary Möbius inversion.
