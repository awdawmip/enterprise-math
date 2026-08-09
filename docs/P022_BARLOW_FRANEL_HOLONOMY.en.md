# P022 — Composite Franel Defects Are Multiplicative Holonomy Increments

Status: `ACTIVE RESEARCH NOTE / EXACT TELESCOPING STRUCTURE / INTERPRETIVE BRIDGE TO P018`  
Owner: `program/p022-geometry-v2`  
Depends on: Franel transfer `Psi`; unified boundary defect `Delta_n`  
Cross-route relevance: P018 defect/response/path dependence; P011 low-order collision identifiability

## 1. Two routes to the same central-binomial integer

For each segment index `N`, the central binomial integer

\[
A_N=\binom{2N}{N}
\]

can be treated in two different ways before replacing central-binomial generators by Franel generators.

### Direct generator route

Treat `A_N` as the distinguished segment generator and send it directly to

\[
F_N.
\]

### Canonical integer-factorization route

Forget that `A_N` was a distinguished generator.  Regard it only as an ordinary positive integer, recursively express its prime factors in the central-binomial basis, and then replace every resulting `A_j` by `F_j`.

The Franel transfer `Psi` performs the second operation.

These two routes need not agree.

---

## 2. P022-HO01 — cumulative transfer mismatch

Define

\[
\boxed{
Q_N
=
\frac{F_N}{\Psi(A_N)}.
}

Conceptually, `Q_N` measures the multiplicative mismatch between:

- the direct segment route `A_N -> F_N`;
- the canonical integer-factorization route `A_N -> Psi(A_N)`.

The expression `Psi(A_N)` need not be evaluated by factoring the very large integer `A_N`; the next theorem gives a local recurrence.

At `N=1`,

\[
A_1=F_1=2
\]

and hence

\[
\boxed{Q_1=1.}
\]

---

## 3. P022-HO02 — boundary defect is the multiplicative first difference of `Q`

The central-binomial recurrence is

\[
\frac{A_N}{A_{N-1}}
=
\frac{2(2N-1)}N.
\]

By multiplicativity of `Psi`,

\[
\frac{\Psi(A_N)}{\Psi(A_{N-1})}
=
\frac{2\Psi(2N-1)}{\Psi(N)}.
\]

Therefore

\[
\begin{aligned}
\frac{Q_N}{Q_{N-1}}
&=
\frac{F_N}{F_{N-1}}
\frac{\Psi(A_{N-1})}{\Psi(A_N)}\\
&=
\frac{F_N\Psi(N)}
{2F_{N-1}\Psi(2N-1)}.
\end{aligned}
\]

The right side is exactly the unified transfer defect `Delta_N`. Thus

\[
\boxed{
\Delta_N
=
\frac{Q_N}{Q_{N-1}}.
}
\]

So `Delta_N` is the discrete multiplicative derivative of the transfer mismatch state.

---

## 4. P022-HO03 — prime boundaries are flat, composite boundaries are jumps

The transfer-defect theorem proves

\[
\Delta_N=1
\]

whenever

\[
2N-1
\]

is prime.

Therefore

\[
\boxed{
Q_N=Q_{N-1}
\qquad(2N-1\text{ prime}).}
\]

At a composite odd boundary,

\[
\Delta_N=D_N,
\]

so

\[
\boxed{
Q_N=D_NQ_{N-1}.
}
\]

Hence the state `Q_N` changes **only** at the same composite indices where the central-binomial coordinate fails to supply a new prime pivot.

The hard low-order collision information is therefore a jump process over the composite odd boundaries.

---

## 5. P022-HO04 — telescoping product of all composite defects

Iterating HO02 from `2` through `N` gives

\[
Q_N
=
\prod_{n=2}^{N}\Delta_n.
\]

Prime-boundary factors are one, so

\[
\boxed{
Q_N
=
\prod_{
\substack{2\le n\le N\\
2n-1\text{ composite}}}
D_n.
}
\]

Thus the cumulative transfer mismatch is exactly the ordered cumulative product of all composite Franel defects.

This identity does not prove that the individual `D_n` are independent; it packages their cumulative effect.

---

## 6. P022-HO05 — factorial / odd-double-factorial form

Using the local defect definition directly,

\[
\prod_{n=2}^{N}\Delta_n
=
\frac{F_N}{F_1}
\frac{1}{2^{N-1}}
\frac{\prod_{n=2}^{N}\Psi(n)}
{\prod_{n=2}^{N}\Psi(2n-1)}.
\]

Since

\[
F_1=2,
\]

and `Psi` is multiplicative,

\[
\prod_{n=2}^{N}\Psi(n)=\Psi(N!),
\]

while

\[
\prod_{n=2}^{N}\Psi(2n-1)
=\Psi((2N-1)!!),
\]

where the omitted factor `1` is harmless.

Therefore

\[
\boxed{
Q_N
=
\frac{
F_N\Psi(N!)
}{
2^N\Psi((2N-1)!!)
}.}
\]

Because

\[
A_N
=
\frac{2^N(2N-1)!!}{N!},
\]

this is precisely equivalent to

\[
Q_N=F_N/\Psi(A_N).
\]

So the global telescoping identity and the direct-vs-canonical representation mismatch are the same structure.

---

## 7. Holonomy interpretation

The word “holonomy” here is an interpretation, not a claim of a new general holonomy theory.

There are two representation paths beginning from the same integer object `A_N`:

\[
A_N
\xrightarrow{\text{direct segment label}}
F_N
\]

and

\[
A_N
\xrightarrow{\text{canonical prime/integer expansion}}
(e_j(A_N))
\xrightarrow{A_j\mapsto F_j}
\Psi(A_N).
\]

Their ratio is `Q_N`.

The step ratio

\[
Q_N/Q_{N-1}
\]

is the local obstruction to path-independence at the new odd boundary.

Thus the pure Franel defect has a concise interpretation:

\[
\boxed{
D_N
=
\text{multiplicative path-mismatch increment at a composite boundary}.}
\]

This matches the **role** of defect/response quantities in P018, while remaining a P022-specific arithmetic construction.

---

## 8. Why this does not solve multiplicative independence

Knowing the cumulative product

\[
Q_N=\prod D_n
\]

does not recover the individual defect exponents in an arbitrary multiplicative relation.

The low-order identifiability problem still asks whether

\[
2,D_{n_1},D_{n_2},\ldots
\]

are multiplicatively independent.

The holonomy state supplies:

- a canonical cumulative invariant;
- an exact check on local defect formulas;
- a way to separate flat prime steps from composite jumps.

It does **not** replace the defect-lattice independence problem by a one-dimensional terminal statistic.

This is another example of a recurring project boundary: a valid aggregate can be insufficient for a richer history-sensitive future language.

---

## 9. New attack angle

The identities suggest studying the rational sequence

\[
Q_1,Q_2,Q_3,\ldots
\]

directly.

Questions include:

1. which primes enter or leave the support of `Q_N` at each composite jump;
2. whether `Q_N/Q_(N-1)` always has a primitive defect valuation;
3. whether the Franel three-term recurrence induces useful congruences for the jump sequence;
4. whether an eventual multiplicative relation among the `D_n` would force an unexpected return or periodicity property in the valuation path `v_p(Q_N)`.

These are more structured than extending a determinant cutoff.

---

## 10. Prior-art boundary

Central-binomial identities, Franel numbers, multiplicative arithmetic functions, factorial/double-factorial identities and path-independence language are established ingredients.

The P022-specific result is the exact identification of the composite Franel defects as the multiplicative first differences of the direct-vs-canonical transfer mismatch `Q_N`.

No claim is made that the term “holonomy” or the surrounding general concept is novel.

---

## 11. Executable assets

Added:

- `src/enterprise_math/p022_barlow_franel_holonomy.py`;
- `tests/test_p022_barlow_franel_holonomy.py`.

The tests verify:

- cumulative mismatch equals the product of composite defects;
- the factorial/double-factorial telescoping formula;
- `Delta_N=Q_N/Q_(N-1)`;
- exact flatness across prime odd boundaries.
