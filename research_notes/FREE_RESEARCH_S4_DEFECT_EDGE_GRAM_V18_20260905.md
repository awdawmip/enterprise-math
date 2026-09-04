# Free Research — The `S_4` Defect-Edge Gram Matrix

Status: `FREE_RESEARCH_FRONTIER / EXACT HOEFFDING GRAM / CENTERED FOUR-SLOT CONTRACTION / DEGENERATE CONSTANT 13 OVER 64 / ADDITIVE CONSTANT 293 OVER 576 / ARITHMETIC COMMON-LIFT INTERTWINER OPEN / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_FOUR_LEVEL_NORMAL_ORDERING_V18_20260905.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Executive advance

The six contexts in the depth-four normal-ordering formula are naturally indexed by the six two-slot choices in a four-history carrier. Their scalar coefficients are

\[
1,2,2,6,6,6,
\]

whose sum and sum of squares are

\[
\boxed{23},
\qquad
\boxed{117}.
\]

Separate scalar estimates see the sum `23`. A joint quadratic estimate sees the sum of squares `117` once the fold kernel is Hoeffding-degenerate in both of its active slots.

After the factorial normalization `4!=24`, the interaction-sector coefficient is therefore

\[
\boxed{
\frac{117}{24^2}=rac{13}{64}.
}
\]

For a symmetric kernel with only its constant removed, the first-order additive sector is also strictly contractive. For every assignment of the multiset `{1,2,2,6,6,6}` to the six edges of `K_4`, its worst possible energy coefficient is

\[
\boxed{
\frac{293}{576}<1.
}
\]

Thus the four-level coefficient problem is not obstructed on the centered factorial-slot carrier. The unresolved issue is now an exact arithmetic common-lift theorem placing the six transported parity-fold contexts into this one four-slot Hoeffding decomposition, with stopping/floor discrepancies routed to lower-scale channels.

---

## 2. Finite probability setup

Let `(X,p)` be a finite probability space and let

\[
h:X\times X\to\mathbb R
\]

be symmetric. Write its Hoeffding decomposition

\[
\boxed{
h(x,y)=m+g(x)+g(y)+h^\circ(x,y),}
\tag{2.1}
\]

where

\[
m=\mathbb E h(X_1,X_2),
\]

\[
g(x)=\mathbb E_yh(x,y)-m,
\]

and

\[
\mathbb E g(X)=0,
\qquad
\mathbb E_yh^\circ(x,y)=0
\]

for every `x`. Symmetry also gives column centering.

Let

\[
X_1,X_2,X_3,X_4
\]

be independent with law `p`. For every edge

\[
e=\{i,j\}\in\binom{[4]}2,
\]

put

\[
h_e=h(X_i,X_j),
\qquad
h_e^\circ=h^\circ(X_i,X_j).
\]

---

## S4G-T01 — Pairwise orthogonality of degenerate edge lifts

If `e` and `f` are distinct edges of `K_4`, then

\[
\boxed{
\mathbb E[h_e^\circ h_f^\circ]=0.
}
\tag{3.1}
\]

### Proof

If the edges are disjoint, the two variables are independent and both kernels have mean zero.

If they share one vertex, condition on that common variable. The expectation over either remaining endpoint vanishes by row/column centering. Hence the conditional product expectation is zero.

Therefore the six degenerate edge lifts form an orthogonal family and all have the same norm

\[
\mathbb E[(h^\circ)^2].
\]

Consequently, for arbitrary real edge coefficients `c_e`,

\[
\boxed{
\left\|
\sum_ec_eh_e^\circ
\right\|_2^2
=
\left(\sum_ec_e^2\right)
\|h^\circ\|_2^2.
}
\tag{3.2}
\]

---

## 4. Full symmetric-kernel Gram formula

Define

\[
C:=\sum_ec_e
\]

and the weighted degree at vertex `i`

\[
d_i:=\sum_{e\ni i}c_e.
\]

Using (2.1),

\[
\sum_ec_eh_e
=Cm+
\sum_{i=1}^4d_ig(X_i)+
\sum_ec_eh_e^\circ.
\]

The constant, additive and degenerate interaction sectors are mutually orthogonal. Hence

\[
\boxed{
\left\|
\sum_ec_eh_e
\right\|_2^2
=
C^2m^2+
\left(\sum_i d_i^2\right)
\|g\|_2^2+
\left(\sum_ec_e^2\right)
\|h^\circ\|_2^2.
}
\tag{4.1}
\]

The original pair-kernel norm is

\[
\boxed{
\|h\|_2^2
=m^2+2\|g\|_2^2+
\|h^\circ\|_2^2.
}
\tag{4.2}
\]

Equations (4.1)--(4.2) give the complete six-by-six Gram diagonalization by Hoeffding degree.

---

## S4G-T02 — Exact depth-four interaction coefficient

For the normal-ordering coefficient multiset

\[
\{c_e\}=\{1,2,2,6,6,6\},
\]

\[
\sum_ec_e^2
=1+4+4+36+36+36
=117.
\]

Therefore the factorial-normalized interaction lift

\[
\frac1{24}\sum_ec_eh_e^\circ
\]

has energy

\[
\boxed{
\left\|
\frac1{24}\sum_ec_eh_e^\circ
\right\|_2^2
=rac{13}{64}
\|h^\circ\|_2^2.
}
\tag{5.1}
\]

This is exact and independent of how the equal-multiplicity contexts are named.

The corresponding amplitude norm is

\[
\sqrt{13}/8<1/2.
\]

---

## S4G-T03 — Robust additive-sector bound

The three edges carrying coefficient `6` form, up to graph isomorphism, either:

1. a star;
2. a triangle; or
3. a length-three path.

Assigning the remaining weights `1,2,2` to the complementary three edges and enumerating these finite graph types gives

\[
\boxed{
\sum_{i=1}^4d_i^2\le586.
}
\tag{6.1}
\]

The bound is attained by the star and triangle types, with weighted-degree multiset

\[
\{18,10,9,9\}.
\]

For a centered symmetric kernel (`m=0`), the additive input sector has pair norm

\[
2\|g\|_2^2.
\]

Therefore its factorial-normalized output/input energy ratio is at most

\[
\boxed{
\frac{586}{24^2\cdot2}
=rac{293}{576}
<1.
}
\tag{6.2}
\]

The interaction ratio is only `13/64`, so every centered symmetric pair kernel obeys

\[
\boxed{
\left\|
\frac1{24}\sum_ec_eh(X_i,X_j)
\right\|_2^2
\le
\frac{293}{576}
\|h\|_2^2
\qquad(\mathbb Eh=0).
}
\tag{6.3}
\]

---

## 7. Constant sector and why centering is essential

The constant coefficient is

\[
\left(\frac C{24}\right)^2
=\left(\frac{23}{24}\right)^2
=rac{529}{576}.
\tag{7.1}
\]

This is still strictly below one, but it is much slower than the centered sectors. In the arithmetic problem the constant part is exactly the endpoint-mass mismatch, already known to be `O_k(1/log N)` for every fixed commutator order.

Thus the correct order of operations is:

1. separate the mass imbalance;
2. center the signed endpoint kernel;
3. apply the `293/576` or `13/64` Gram bound;
4. restore the scalar only once at the block boundary.

This is the four-slot analogue of the V15 parity covariance decomposition.

---

## 8. `S_4` representation interpretation

The six edges of `K_4` carry the permutation representation

\[
\mathbb R^{\binom42}
\cong
\mathbf1\oplus V_2\oplus V_3,
\]

of dimensions `1,2,3`.

For a fully degenerate pair kernel, the probabilistic Gram matrix is a scalar multiple of the identity on the entire six-edge coefficient space. Hence every `S_4` irreducible sector has the same edge norm, and only the coefficient-vector projection determines the energy.

For a symmetric nondegenerate kernel, Hoeffding degree supplies a finer and more useful decomposition:

- degree `0`: endpoint-mass imbalance;
- degree `1`: additive boundary mode;
- degree `2`: genuine relation/curvature field.

The degree-two sector is the one represented natively by the retained weighted relation field.

---

## 9. Exact remaining arithmetic lift

The six operators

\[
\Delta U^2,
J\Delta U,
\Delta JU,
J^2\Delta,
J\Delta J,
\Delta J^2
\]

are not automatically six copies of one pair kernel on independent slots. Quotient endpoints couple the slots through products and moving stopping boundaries.

The next theorem must construct a common four-action lift and prove that, after conditioning on each fixed validity/stopping chamber:

1. the degree-two component is exactly a bi-centered edge relation field;
2. the degree-one component is one of the already isolated tail-potential/boundary channels;
3. the degree-zero component is the fixed-order mass discrepancy;
4. product-label recoalescence occurs only after the edge Gram has been formed.

On the fully valid four-history core, action commutativity and product weights make the slot carrier permutation invariant, so S4G-T01 applies directly. The unresolved contribution is concentrated on mixed stopping chambers and is therefore compatible with a lower-scale tail audit.

---

## 10. Relation to the `58/625` block margin

The ideal two-channel depth-four multiplier at energy exponent `1/3` is

\[
567/625.
\]

The interaction Gram coefficient `13/64` and the centered full-kernel coefficient `293/576` are not additive corrections to `567/625`; they are norm constants for the commutator block that replaces six separate triangle estimates.

A valid coefficient audit must place the commutator vector and the Mellin transport in one block matrix before comparing with the margin. Adding `293/576` directly to `567/625` would double-count the same transported energy.

The present theorem therefore closes the finite Gram calculation but not yet the arithmetic block spectral radius.

---

## 11. Classification

Closed exactly:

1. pairwise orthogonality of bi-centered edge lifts;
2. full constant/additive/interaction Gram formula;
3. interaction coefficient `13/64`;
4. robust centered symmetric coefficient `293/576`;
5. constant coefficient `529/576`;
6. finite graph-type audit for every assignment of the multiplicity multiset.

Open:

1. common four-action lift of the six arithmetic contexts;
2. chamberwise Hoeffding decomposition under stopped quotient transport;
3. lower-scale control of the additive boundary sector;
4. assembly with the depth-four Mellin block;
5. a promoted native prime remainder.
