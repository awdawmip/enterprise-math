# P019 Supplement 09 — Fiber Roots, Slack Cascades, and Square-Layer Bulk/Detail Compression

Status: `RESEARCH WIP / INTEGER IDENTITIES PROVED + BOUNDED REGRESSION`

## 1. Goal

Supplements 07/08 separated contraction trace into minimum value, full fiber witness relation, selected boundary witness, and future-safe quotient.

This supplement asks whether a selected boundary step must still retain potentially large child totals.

For the square layer `s=2`, the answer is substantially stronger: **large proportional bulk and the history-sensitive deviation can be separated exactly.**

At the same time, each boundary selection itself can be expressed as a new integer root/collapse rather than arbitrary search.

## 2. P019-X16 — A directed fiber boundary is an integer root

Fix block sizes `m,n`, power `s`, and parent total `c`.

Let the rightmost argmin endpoint be

\[
a_0=\max\operatorname*{argmin}_{a\in\mathbb Z}
\bigl(\Psi_{m,s}(a)+\Psi_{n,s}(c-a)\bigr).
\]

For `a>=a_0`, define the right-branch excess energy

\[
G(a)
=
\Psi_{m,s}(a)
+
\Psi_{n,s}(c-a)
-
\Psi_{m+n,s}(c).
\]

Discrete convexity makes `G` strictly increasing on this branch.

For slack `omega>=0`, define

\[
\boxed{
R_G(\omega)
=
\max\{a\ge a_0:G(a)\le\omega\}.
}
\]

This is exactly the directed right-boundary receiver total. On the right branch,

\[
G(a)\le\omega
\iff
a\le R_G(\omega),
\]

so the construction has the same order-adjoint integer-root form already used by Enterprise Math.

Let

\[
\gamma=G(R_G(\omega)),
\qquad
\rho=\omega-\gamma.
\]

Then

\[
\boxed{
0\le\rho
<
G(R_G(\omega)+1)-G(R_G(\omega)).
}
\]

Thus boundary selection carries an exact bounded basin remainder. This aligns with the existing `R_p/C_p`, P008 right-adjoint, and P018 finite-detail/carry skeletons.

## 3. P019-X17 — Reverse contraction is a telescoping slack cascade

Let the global threshold be `T` and reverse-lift a selected boundary witness along a complete oriented contraction flag.

At reverse split `t`, let the current coarse partition minimum energy be `E_t` and define remaining slack

\[
\omega_t=T-E_t.
\]

The fiber root consumes excess `gamma_t` and produces remainder `rho_t`. After splitting,

\[
E_{t+1}=E_t+\gamma_t,
\]

hence

\[
\boxed{
\omega_{t+1}
=
\omega_t-\gamma_t
=
\rho_t.
}
\]

Therefore the entire reverse lift is an exact slack cascade:

\[
T
=
E_{final}+\omega_{final}
=
\sum_t\gamma_t+\omega_{final},
\]

because the root one-block zero-sum state has minimum energy zero.

Each level also satisfies

\[
0\le\omega_{t+1}<\text{next fiber gap}_t.
\]

A contraction trace can therefore be viewed as a finite sequence of

`fiber-root state + bounded remainder`,

not hidden-real approximation error and not an infinite-precision expansion.

## 4. The `s=1` extreme: binary fiber remainder

For `s=1`,

\[
\Psi_{m,1}(c)=|c|
\]

and is independent of block size.

Moving one more step outward along any directed two-block fiber increases the excess energy by exactly `2`. Hence

\[
\boxed{
\text{next gap}=2,
\qquad
\rho=\omega\bmod2.
}
\]

The directed fiber trace detail in the primitive graph-cost layer is therefore a binary remainder.

However, `rho=0` does not eliminate provenance ambiguity: `s=1` argmin witnesses can remain highly degenerate. Zero positive-excess detail is not the same as unique witness identity.

## 5. P019-X18 — Exact square-energy bulk/detail identity

Define

\[
\varepsilon_m(c)
=r(m-r),
\qquad
r=|c|\bmod m.
\]

Expanding the closed form for `Psi_(m,2)` gives the exact identity

\[
\boxed{
m\Psi_{m,2}(c)=c^2+\varepsilon_m(c).}
\]

Moreover,

\[
0\le\varepsilon_m(c)
\le\left\lfloor\frac{m^2}{4}\right\rfloor.
\]

Thus the square layer splits exactly into

- bulk: `c^2`;
- bounded residue detail: `epsilon_m(c)`.

This is not asymptotic.

## 6. P019-X19 — Exact two-block imbalance identity

Let block sizes be `m,n`, with

\[
M=m+n,
\qquad
a+b=c.
\]

Define the cross-multiplied deviation from proportional allocation

\[
\boxed{z=na-mb=Ma-mc.}
\]

Let the split excess above the merged fiber minimum be

\[
\omega
=
\Psi_{m,2}(a)
+
\Psi_{n,2}(b)
-
\Psi_{M,2}(c).
\]

Applying X18 to all three blocks and using

\[
nMa^2+mMb^2-mnc^2=(na-mb)^2
\]

gives

\[
\boxed{
mnM\omega
=
z^2
+nM\varepsilon_m(a)
+mM\varepsilon_n(b)
-mn\varepsilon_M(c).
}
\]

Every quantity is integer-valued.

## 7. P019-X20 — Integer-root bound for history-sensitive imbalance

The middle two correction terms are nonnegative, so

\[
z^2
\le
mn\bigl(M\omega+\varepsilon_M(c)\bigr).
\]

Therefore

\[
\boxed{
|z|
\le
R_2\!\left(
mn\bigl(M\omega+\varepsilon_M(c)\bigr)
\right).
}
\]

At the minimum layer `omega=0`,

\[
\boxed{z^2\le mn\varepsilon_M(c).}
\]

Since `epsilon_M(c)` depends only on `|c| mod M`, the parent total may grow arbitrarily while the history-sensitive minimum deviation does not grow with its bulk quotient.

## 8. P019-X21 — Minimum imbalance profile depends only on the remainder

Write

\[
|c|=Mq+r,
\qquad0\le r<M.
\]

At a square-energy minimum, let `h` be the number of the `r` extra `q+1` slots assigned to the left block. Then

\[
\max(0,r-n)
\le h\le
\min(m,r).
\]

With `sigma=sgn(c)`, the left total is

\[
a=\sigma(mq+h).
\]

Hence the imbalance coordinate is exactly

\[
\boxed{z_h=\sigma(Mh-mr).}
\]

with labeled multiplicity

\[
\boxed{
\binom mh\binom n{r-h}.
}
\]

The complete minimum imbalance profile therefore depends only on

`m,n, sign(c), |c| mod M`,

and not on the quotient `q`.

This is a strong finite-detail compression.

## 9. Use `z` instead of large child totals

Since

\[
z=Ma-mc,
\]

we recover

\[
\boxed{
a=(mc+z)//M,
\qquad b=c-a,}
\]

provided

\[
M\mid(mc+z).
\]

Thus a legal square-layer split need not store two potentially large child totals. Given parent total `c` and block sizes `m,n`, one legal integer deviation tag `z` reconstructs the split exactly.

A candidate square trace coordinate is therefore

`exactly transported parent bulk + bounded/controlled imbalance tag z`.

At minimum, the allowed `z` values themselves form a finite remainder-determined set.

## 10. Interface with P018

P018 has the generic form

`fine state = transported coarse state + bounded precision detail`.

Square contraction now gives

`child allocation = proportional parent bulk + integer imbalance detail`.

No true division is required because proportionality is encoded by the cross-multiplied coordinate `z=Ma-mc`.

Thus the history-sensitive component of P019 dimensional contraction can enter the P018 finite detail/carry language rather than creating a separate approximation-error ontology.

## 11. Interface with P011/P021

- P011: `fiber_witness_interval=[L,U]` gives block-total fiber multiplicity `U-L+1`;
- P021: exact witness relations cannot in general be replaced by cardinalities before multi-step composition;
- this supplement: in the square layer, the large numerical component of a one-step witness can be further coordinatized as parent total plus controlled imbalance `z`.

Retaining witness identity therefore does not imply storing the original high-dimensional large-integer state verbatim.

## 12. Implementation and validation

`src/enterprise_math/contraction_trace.py` adds:

- `directed_boundary_decomposition`;
- `BoundaryTraceStep` / `reverse_boundary_witness_with_trace`;
- `square_residue_correction`;
- `square_split_imbalance`;
- `square_split_from_imbalance`;
- `square_minimum_imbalance_profile`;
- `square_scaled_excess_identity`;
- `square_imbalance_bound`.

`tests/test_contraction_trace.py` exercises:

- fiber-root remainders for `s=1..4`;
- the `s=1` binary remainder;
- reverse slack telescoping;
- the exact scaled square identity;
- the imbalance integer-root bound;
- exact split recovery from `z`;
- invariance of the minimum imbalance profile under changes in the bulk quotient;
- boundedness of `epsilon_m`.

## 13. A deliberate non-generalization

The especially clean bounded-residue identity is special to `s=2`.

For example, for `s=3` and `|c|=mq+r`,

\[
m^2\Psi_{m,3}(c)
=
|c|^3
+r(m-r)(3mq+m+r).
\]

The correction retains the factor `r(m-r)` but now grows with the bulk quotient `q`.

Therefore P019 must not claim that every collision order has square-layer-style bounded detail. For `s>2`, the correct target is an exact lower-degree residue shell hierarchy, not a copied `s=2` statement.

## 14. Next step

Priorities:

1. study whether the full sequence of square-layer imbalance tags `z_t` along a contraction flag obeys stronger global constraints/conservation laws;
2. determine which future queries require only `z_t + rho_t` rather than full block-membership history;
3. apply Supplement 08 future-safe partition refinement directly to contraction traces and find the first nontrivial safely mergeable history class;
4. generalize X18–X21 to `s>2` as `bulk polynomial + lower-degree residue shell` rather than forcing bounded detail.
