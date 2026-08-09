# P022 — Low-Order Collision Identifiability Certificate Extended to Segment Length 66

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE CERTIFICATE EXTENSION`  
Owner: `program/p022-geometry-v2`  
Parent chain: low-order identifiability base theorem + length-65 supplement

## 1. One further exact column

The length-65 certificate is not the current mathematical boundary.

The segment generator

\[
\ell=66
\]

was factored and inserted into the same joint central-binomial/Franel valuation framework.

The unknown exponent vector now has 67 coordinates:

\[
(c_1,\ldots,c_{66},c_u).
\]

---

## 2. P022-LI06 — 67-dimensional determinant certificate

Using the selected valuation rows listed in the executable certificate, form the integer matrix

\[
V_{66}\in M_{67}(\mathbb Z).
\]

It contains:

- `32` selected central-binomial valuation rows;
- `35` selected Franel valuation rows;
- `66` observed-segment columns;
- one hidden-tail column.

Reduce modulo

\[
q=1000003.
\]

Exact modular elimination gives

\[
\boxed{
\det V_{66}
\equiv999999
\pmod{1000003}.
}
\]

Hence

\[
\boxed{
\det V_{66}\ne0.
}
\]

Therefore equality of the joint moment pair `(M_2,M_3)` forces all 66 segment multiplicity differences and the tail difference to vanish.

---

## 3. P022-LI07 — certified range

The exact low-order identifiability range is now

\[
\boxed{
1\le\ell\le66.
}
\]

For every selected-layer Barlow checkpoint geometry whose observed segments all satisfy that bound,

\[
\boxed{
(M_2,M_3)
\Longrightarrow
(t_1,\ldots,t_{66},u)
}
\]

and therefore

\[
\boxed{
(J_1,J_2,J_3)
\Longrightarrow
(t_1,\ldots,t_{66},u).
}
\]

The theorem still allows arbitrary multiplicities and arbitrary hidden-tail length.

---

## 4. Current boundary at 67

An attempt to fully factor the next Franel generator `F_67` exceeded the present exact factorization window.

No determinant dependence, low-order alias, or counterexample was found.

Thus the correct status is:

\[
\boxed{
\ell\le66:\text{ certified},
\qquad
\ell=67:\text{ factorization/certificate incomplete in this pass}.
}
\]

The research target is no longer “search more schedules”.  It is to replace full factorization by a structural method for producing enough independent p-adic rows, or to prove a global joint multiplicative-independence theorem.

---

## 5. Executable assets

Added:

- `src/enterprise_math/p022_barlow_low_order_identifiability_66.py`;
- `tests/test_p022_barlow_low_order_identifiability_66.py`.

The certificate is recomputed directly from the segment formulas and does not depend on a stored external factor database.
