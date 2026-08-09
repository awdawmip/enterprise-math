# A3 Guard-Image Lattice Supplement 11 — Two-Guard Rank-One Quotient Coordinates: One Integer Plus One Finite Residue

Status: `RESEARCH WIP / COMPLETE INTEGER COSET COORDINATES + SYMBOLIC COARSE MAP`

## 1. Goal

For two integer guards, suppose the current partition has rank-one hidden guard image

\[
L_G=\mathbb Z h\subseteq\mathbb Z^2,
\qquad h\neq0.
\]

Every fine guard-score vector in one coarse fiber lies in the affine coset

\[
g+\mathbb Z h.
\]

The goal is to give this coset a complete, integer-only, coarse-readable finite-information coordinate system without choosing a fine representative.

Write

\[
h=d p,
\qquad d=\gcd(|h_1|,|h_2|),
\]

with primitive `p`. Then

\[
\boxed{\mathbb Z^2/\mathbb Z h\cong\mathbb Z\oplus\mathbb Z/d\mathbb Z.}
\]

Thus the complete quotient state consists of one free integer and one finite residue.

## 2. Primitive direction and unimodular transform

Write

\[
p=(p_1,p_2),
\qquad \gcd(|p_1|,|p_2|)=1.
\]

Bezout gives integers `u,v` with

\[
\boxed{u p_1+v p_2=1.}
\]

Define

\[
\boxed{
T=
\begin{pmatrix}
 u & v\\
 -p_2 & p_1
\end{pmatrix}.
}
\]

Its determinant is one, so it is unimodular, and

\[
Th=(d,0)^T.
\]

The hidden lattice therefore becomes step `d` along the first transformed axis and zero along the second.

## 3. A3-G40 — Complete two-guard coset coordinates

For a score vector `x=(x_1,x_2)`, define

\[
\boxed{
\tau(x)=(u x_1+v x_2)\bmod d
}
\]

and

\[
\boxed{
\phi(x)=-p_2x_1+p_1x_2.
}
\]

If `x'=x+n h`, then both `tau` and `phi` are unchanged.

Conversely, if two score vectors have the same `tau` and `phi`, the transformed difference has second coordinate zero and first coordinate divisible by `d`; hence the original difference is an integer multiple of `h`.

Therefore

\[
\boxed{
 x,x'\text{ lie in the same hidden coset}
\iff
(\tau,\phi)\text{ are identical}.
}
\]

This is a complete invariant, not merely a statistic.

## 4. Deterministic canonical representative

Because

\[
T^{-1}=
\begin{pmatrix}
 p_1 & -v\\
 p_2 & u
\end{pmatrix},
\]

a quotient coordinate `(tau,phi)` with `0<=tau<d` has the canonical integer representative

\[
\boxed{
 x_{can}=(p_1\tau-v\phi,\ p_2\tau+u\phi).
}
\]

Every real fine score vector in that quotient class differs from `x_can` by an integer multiple of `h`.

Hence exact branch reachability can be reconstructed directly from the quotient coordinate by running the rank-one threshold sweep on

\[
x_{can}+\mathbb Z h.
\]

## 5. A3-G41 — Symbolic coarse map

Let the two fine guard scores be

\[
s_1=w^{(1)}\cdot c+b_1,
\qquad
s_2=w^{(2)}\cdot c+b_2,
\]

and let a coordinate partition have coarse blocks `B_1,...,B_ell`. Assume the hidden guard image has rank one.

Choose one anchor in each coarse block. If `y_a` is the block total, the anchor section gives one score representative

\[
\tilde s(y)=b+\sum_a y_a
\begin{pmatrix}
 w^{(1)}_{i_a}\\
 w^{(2)}_{i_a}
\end{pmatrix}.
\]

Changing an anchor changes this representative by a within-block hidden generator and therefore does not change its quotient coordinate.

Thus the quotient coordinates are exact symbolic functions of coarse totals:

\[
\boxed{
\phi(y)=\phi_b+\sum_a\alpha_a y_a,
\qquad \alpha_a\in\mathbb Z,
}
\]

and

\[
\boxed{
\tau(y)=\left(\tau_b+\sum_a\beta_a y_a\right)\bmod d.
}
\]

So the global symbolic chain is

\[
\boxed{
\text{coarse block totals}
\to(\tau,\phi)
\to\text{exact hidden-fiber branch geometry}.
}
\]

No fine-state reconstruction is required.

## 6. Quotient precision interpretation

Even when neither guard descends individually, the future branch geometry may need only

\[
\boxed{\text{one free integer}+\text{one finite torsion residue}.}
\]

This is coarser than storing two exact guard scores but more complete than storing only hidden rank.

Predicate precision therefore naturally includes typed quotient information: free coordinates plus finite torsion residues.

## 7. Special simplification for support-type opposite guards

The finite-band predicate

\[
|z|\le R
\]

can be encoded as

\[
s_-=R-z,
\qquad s_+=R+z.
\]

If the hidden scalar relation changes by step `q`, the two-guard hidden step is proportional to `(-q,q)`. Its primitive direction is parallel to `(1,-1)`, so the free row is parallel to `(1,1)`.

Therefore

\[
\boxed{
\phi=\pm(s_-+s_+)=\pm2R.
}
\]

The free integer is constant for the whole support query; the only varying hidden-fiber information is a finite torsion residue, which is a deterministic affine transform of the hidden relation residue including the guard bias.

Thus an A3-generated pairwise radius-support query reduces to

\[
\boxed{\text{constant radius invariant}+\text{finite hidden residue}.}
\]

Supplement 09's least-absolute-residue support certificate is the scalar form of this quotient state.

## 8. Do not identify unrelated gcd scales

The torsion modulus

\[
d=\gcd(|h_1|,|h_2|)
\]

belongs to the hidden guard-score lattice. It is not automatically the same as the structural relation quantum `gcd(m_i)` of the weighted relation state.

Those arithmetic scales may be related under a particular observable map, but they remain distinct typed quantities unless a theorem proves otherwise.

## 9. Implementation

Added:

- `src/enterprise_math/two_guard_coset.py`;
- `tests/test_two_guard_coset.py`.

The tests cover the unimodular transform, complete hidden-coset invariance, canonical representatives, section-independent symbolic coarse maps, quotient-coordinate branch reconstruction, and the support-guard specialization including the deterministic affine bias shift in torsion.

## 10. Prior-art boundary

The decomposition of `Z^2/Zh` by Smith normal form / unimodular basis change is standard integer-module theory. A3 does not claim it as new mathematics.

The project-specific interface is

\[
\boxed{
\text{partition kernel}
\to\text{hidden guard quotient module}
\to\text{typed predicate precision state}
\to\text{branch reachability}.
}
\]

Novelty of that integrated interface remains unverified.

## 11. Next

1. construct free/torsion quotient profiles for arbitrary guard count and hidden rank using Smith/Hermite tools;
2. compile branch effects symbolically on quotient coordinates rather than fine scores;
3. let the A3-to-A4 bridge consume only the `(radius,residue)` support specialization;
4. combine quotient torsion with relation rank/quantum in typed precision certificates;
5. pressure-test P021 multi-predicate witness queries for low free rank and small torsion representations.
