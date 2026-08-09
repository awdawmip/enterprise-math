# P022 — Exact Bounded Identifiability from the First Three Collision Coefficients

Status: `ACTIVE RESEARCH NOTE / COMPUTER-ASSISTED EXACT FINITE THEOREM / GLOBAL EXTENSION OPEN`  
Owner: `program/p022-geometry-v2`  
Depends on: selected-layer moment factorization; P011 collision polynomial; collision-geometry inverse  
Cross-route relevance: P011 low-order completeness questions; P023/P024 minimal observation language

## 1. Question

The complete P011 collision polynomial identifies the Barlow checkpoint segment multiset and hidden tail exactly.

Pair collision `J_2` alone does not.  P022 already has the exact alias

\[
(1,5,5,10)
\quad\text{versus}\quad
(2,2,6,11),
\]

which occurs at total segment length `21` with four checkpoints.

The next question is sharper:

> how much of the collision polynomial is actually required before the structured checkpoint geometry becomes identifiable?

A global answer is still open.  This note proves a large bounded theorem for the first three coefficients.

---

## 2. Moment factorization

For observed segment length `ell`, define

\[
\boxed{
A_\ell=\binom{2\ell}{\ell}
}
\]

and the Franel-type integer

\[
\boxed{
F_\ell=\sum_{j=0}^{\ell}\binom{\ell}{j}^3.
}
\]

If `t_ell` is the number of observed segments of length `ell` and `u` is the unobserved tail length, the ordered equal-observation moments factor as

\[
\boxed{
M_2
=4^u\prod_{\ell\ge1}A_\ell^{t_\ell},
}
\]

and

\[
\boxed{
M_3
=8^u\prod_{\ell\ge1}F_\ell^{t_\ell}.
}
\]

This is the `r=2,3` specialization of the existing generalized binomial-power-sum factorization.

---

## 3. Collision coefficients and moments are equivalent through order three

Let

\[
M_1=|X|=J_1.
\]

The falling-factorial/Stirling identities give

\[
\boxed{
J_2=\frac{M_2-M_1}{2},
}
\]

and

\[
\boxed{
J_3=\frac{M_3-3M_2+2M_1}{6}.
}
\]

Conversely,

\[
\boxed{
M_2=2J_2+J_1,
}
\]

and

\[
\boxed{
M_3=6J_3+3M_2-2J_1.
}
\]

Thus the truncated collision state

\[
(J_1,J_2,J_3)
\]

contains exactly the same information as

\[
(M_1,M_2,M_3).
\]

For geometry identifiability below, only `M_2,M_3` are actually needed once the input is known to lie in the certified Barlow class.

---

## 4. Valuation linearization

Take two checkpoint geometries and let

\[
c_\ell
=t_\ell-t'_\ell,
\qquad
c_u=u-u'.
\]

If their `M_2` values agree, then for every prime `p`,

\[
\boxed{
\sum_\ell c_\ell v_p(A_\ell)
+2c_u\,\mathbf1_{p=2}
=0.
}
\]

If their `M_3` values agree, then

\[
\boxed{
\sum_\ell c_\ell v_p(F_\ell)
+3c_u\,\mathbf1_{p=2}
=0.
}
\]

So multiplicative identifiability becomes an ordinary integer linear-algebra problem on p-adic valuation vectors.

---

## 5. P022-LI01 — exact 51-dimensional determinant certificate

Restrict observed segment lengths to

\[
1\le\ell\le50.
\]

There are 51 unknown multiplicity differences:

\[
(c_1,c_2,\ldots,c_{50},c_u).
\]

Choose 51 valuation equations:

### `M_2` / central-binomial rows

\[
p\in
\{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97\}.
\]

### `M_3` / Franel rows

\[
p\in
\{2,5,7,13,23,29,31,37,41,47,53,59,61,67,71,73,79,101,109,131,151,157,173,389,421,563\}.
\]

Let `V` be the resulting `51 x 51` integer matrix whose first 50 columns are the selected valuations of `A_ell` or `F_ell` and whose last column is the tail contribution:

\[
2\mathbf1_{p=2}
\]

on an `A` row and

\[
3\mathbf1_{p=2}
\]

on an `F_3` row.

The executable certificate recomputes every matrix entry directly from

\[
A_\ell=\binom{2\ell}{\ell},
\qquad
F_\ell=\sum_j\binom{\ell}{j}^3
\]

using repeated integer division only.

Now reduce the matrix modulo the prime

\[
q=1000003.
\]

Exact modular Gaussian elimination gives

\[
\boxed{
\det V\equiv22\pmod{1000003}.
}
\]

Since the residue is nonzero,

\[
\boxed{
\det V\ne0
}
\]

as an integer.

Therefore `V` has full rank over `Q`.

This is a finite exact certificate, not a random search and not a numerical-rank statement.

---

## 6. P022-LI02 — bounded multiplicative identifiability

Suppose two selected-layer Barlow geometries have

- arbitrary hidden tails `u,u'`;
- every observed segment length at most `50`;
- equal second moments `M_2`;
- equal third moments `M_3`.

Then the difference vector

\[
c=(c_1,\ldots,c_{50},c_u)
\]

satisfies every valuation equation used in `V`, hence

\[
Vc=0.
\]

Since `det V != 0`,

\[
c=0.
\]

Thus

\[
\boxed{
(M_2,M_3)
\Longrightarrow
(t_1,\ldots,t_{50},u)
}
\]

uniquely throughout the certified class.

Equivalently, there are **no** distinct Barlow checkpoint geometries with maximum observed segment length at most 50 that share both `M_2` and `M_3`.

This is stronger than any bounded enumeration over total horizon or checkpoint count: multiplicities are unrestricted, because the determinant proves there is no nonzero integer multiplicative relation among the 51 certified generators.

---

## 7. P022-LI03 — first three collision coefficients suffice on the certified class

If two certified geometries have equal

\[
(J_1,J_2,J_3),
\]

then the finite inverse formulas give equal `M_2,M_3`.

LI02 therefore yields

\[
\boxed{
(J_1,J_2,J_3)
\Longrightarrow
(t_1,\ldots,t_{50},u).
}

So in this entire bounded segment-length class, the **first three coefficients** of the P011 collision polynomial already recover the same unordered checkpoint geometry that the complete collision polynomial recovers.

By contrast `J_2` alone is globally insufficient even at much smaller total horizon.

Hence the low-order hierarchy has a real transition:

\[
\boxed{
J_2\text{ alone: insufficient},
\qquad
(J_1,J_2,J_3):\text{ exactly sufficient through segment length }50.
}
\]

---

## 8. Why the theorem is bounded

The certificate proves multiplicative independence only for the finite generator family

\[
\ell=1,\ldots,50
\]

plus the hidden-tail generator.

It does **not** prove that the infinite family

\[
\{(A_\ell,F_\ell):\ell\ge1\}
\]

is multiplicatively independent.

A segment length above 50 could introduce an exact multiplicative relation invisible to the finite determinant.

Therefore the global question remains open:

> does `(J_1,J_2,J_3)` identify arbitrary Barlow checkpoint segment multisets and hidden tail, or does a first exact low-order alias occur at some larger segment length?

Both a proof of infinite independence and one explicit counterexample would be valuable.

---

## 9. Prior-art boundary

Central binomial coefficients, Franel numbers, p-adic valuations, multiplicative relations, and modular determinant certificates are established mathematics and computational number-theory tools.

No claim is made that these sequences or methods are new.

The P022 contribution is the exact reduction of checkpoint low-order collision identifiability to the joint multiplicative independence of these two segment-factor sequences, together with the explicit 51-dimensional certificate for the first 50 segment lengths plus hidden tail.

External historical-priority search for stronger Franel/primitive-divisor results was unavailable during this research pass, so global novelty and possible known infinite theorems remain **unverified**.

---

## 10. Executable certificate

Added:

- `src/enterprise_math/p022_barlow_low_order_identifiability.py`;
- `tests/test_p022_barlow_low_order_identifiability.py`.

The certificate code:

1. computes `A_ell` and `F_ell` exactly from binomial formulas;
2. computes only the selected p-adic valuations by repeated integer division;
3. builds the exact `51 x 51` matrix;
4. recomputes the determinant modulo `1,000,003`;
5. requires residue exactly `22`;
6. separately regression-checks the collision/moment transforms and small schedule geometry.

No floating rank, random prime selection, external factor database, or probabilistic primality test is needed for the stored certificate.
