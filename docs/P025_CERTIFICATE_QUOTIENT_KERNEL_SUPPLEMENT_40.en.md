# P025 Supplement 40 — Transform-Free Exact Kernel of a Labelled Certificate Lattice

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-certificate-index-stage34`  
Depends on: P025 Supplements 35, 39  
Hard block: `NONE`

## 1. Explicit normal-form coordinates are not necessary for the quotient kernel

Stage 39 gives an explicit adjugate residue code when the complete certificate lattice is square and full rank in its labelled ambient `Z^q`.

For a general certificate image

\[
C=\langle g_1,\ldots,g_m\rangle_{\mathbb Z}
\subseteq\mathbb Z^q
\]

of rank

\[
d\le q,
\]

one could compute Hermite/Smith transformation matrices. That is standard mature integer linear algebra, not a project research target.

For the **kernel/equivalence relation itself**, even those transformations are unnecessary.

## 2. P025-T99 — saturation membership is rank preservation

Let

\[
\operatorname{Sat}(C)
=
\operatorname{span}_{\mathbb Q}(C)\cap\mathbb Z^q.
\]

For an integer target `y`,

\[
\boxed{
y\in\operatorname{Sat}(C)
\iff
\operatorname{rank}_{\mathbb Q}\langle C,y\rangle
=
\operatorname{rank}_{\mathbb Q}C.
}
\]

This is immediate from rational span membership.

Thus the first exact guard is purely a rational-rank test.

## 3. P025-T100 — exact lattice membership by one determinantal-divisor comparison

Assume

\[
y\in\operatorname{Sat}(C).
\]

Then

\[
C
\subseteq
C'=\langle C,y\rangle
\subseteq
\operatorname{Sat}(C)
\]

and all three groups have the same rational rank.

Let

\[
\delta(C)
=
[\operatorname{Sat}(C):C]
\]

and similarly for `C'`. Because `C subseteq C'`,

\[
\delta(C)
=
\delta(C')\,[C':C].
\]

Therefore

\[
\boxed{
y\in C
\iff
\delta(C')=\delta(C).
}
\]

Combining with Stage 35, both indices are computed exactly by gcds of maximal minors.

Hence

\[
\boxed{
 y\in C
\iff
\begin{cases}
\operatorname{rank}\langle C,y\rangle=\operatorname{rank}C,\\
\gcd(\text{maximal minors of }[C;y])
=
\gcd(\text{maximal minors of }C).
\end{cases}}
\]

No normal-form transformation matrix is needed.

## 4. P025-D25 — exact quotient kernel on the saturated target space

For

\[
y,z\in\operatorname{Sat}(C),
\]

define

\[
\boxed{
y\sim_C z
\iff
y-z\in C.}
\]

Then

\[
\operatorname{Sat}(C)/{\sim_C}
\cong
\operatorname{Sat}(C)/C.
\]

By P025-T100, equality of quotient classes is decidable using only exact integer rank/minor data.

This is the quotient **kernel**. It does not choose a canonical representative of each class.

That distinction matters for P023:

- a kernel/equivalence relation can already be sufficient for deciding whether two exact targets are indistinguishable modulo the complete certificate lattice;
- a canonical residue encoding is an additional representation choice, not part of the abstract quotient itself.

## 5. Low-rank example

Let

\[
C=\langle(2,4)\rangle
\subset\mathbb Z^2.
\]

Its rational span is the line

\[
y=2x.
\]

The saturation is

\[
\operatorname{Sat}(C)
=
\langle(1,2)\rangle,
\]

and

\[
[\operatorname{Sat}(C):C]=2.
\]

For target `(1,2)`, adjoining it preserves rational rank but lowers the maximal-minor gcd from two to one, hence it lies in the saturation but not in `C`.

For `(6,12)`, adjoining it does not change either rank or index, hence it lies in `C`.

For `(1,3)`, rational rank increases, so it lies outside even the saturated target space.

This separates:

\[
\boxed{
\text{wrong rational direction}
\quad/\quad
\text{right direction but wrong congruence class}
\quad/\quad
\text{actual certificate lattice}.
}
\]

## 6. Same Smith type, different labelled kernel

The two full-rank sublattices

\[
C_1=\langle(2,0),(0,1)\rangle,
\]

and

\[
C_2=\langle(1,1),(1,-1)\rangle
\]

both have Smith invariant factors `(1,2)`.

But

\[
(0,1)\in C_1,
\qquad
(0,1)\notin C_2.
\]

Thus Stage 35's abstract defect-group signature is not the labelled quotient kernel. Stage 40 retains the latter exactly.

## 7. Scalar `eta_min` specialization

For

\[
C=\eta_{\min}\mathbb Z,
\]

rank is automatically one for every nonzero target. The maximal-minor gcd is simply the ordinary integer gcd.

Hence

\[
y\sim_C z
\iff
\eta_{\min}\mid(y-z),
\]

which is exactly equality modulo `eta_min`.

So the familiar scalar congruence code is the rank-one specialization of the transform-free kernel theorem.

## 8. Relation to Stage 39

For a square full-rank lattice with basis matrix `G`, Stage 39 provides the explicit finite code

\[
\rho_G(y)
=
\operatorname{adj}(G)y
\pmod{|\det G|}.
\]

Its kernel is exactly `C`.

Stage 40 is more general but less representational:

- Stage 39: explicit finite labelled code, square full-rank slice;
- Stage 40: exact kernel/membership calculus, arbitrary rank and arbitrary finite generator set.

No claim is made that either encoding is P023-coarsest for every possible declared future language.

## 9. Prior-art / ownership boundary

Rank tests, determinantal divisors, subgroup indices and lattice membership are standard integer linear algebra. Mature computer-algebra systems already implement HNF/SNF algorithms; P025 does not reproduce that general theory.

The project-side result is the precision layering exposed by the pressure test: exact quotient kernels may require strictly less representational structure than canonical normal forms, and abstract Smith type may require strictly less information than the labelled quotient kernel.

## 10. Executable assets

Added:

- `src/enterprise_math/certificate_lattice_kernel.py`;
- `tests/test_certificate_lattice_kernel.py`.

The executable path uses only exact integer rank and determinantal-divisor calculations already present in the owner generation.

## 11. Next frontier

No hard block exists. Continue with:

1. selected finite target-query languages and their P023-coarsest specializations;
2. radius-dependent labelled kernels `C_R`, not only complete `C`;
3. whether ABC quality correlates with any of the new intrinsic/access congruence coordinates after the earlier simple `quality => eta_min=1` conjecture failed;
4. Foundation feedback for the hierarchy `rank -> index -> Smith type -> labelled kernel`.
