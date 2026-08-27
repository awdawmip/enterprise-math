# Perfect Prime Table Critical Cofactor All-m Proof — Research Return

Status: `RESEARCHER_HANDOFF / HARD_TARGET_OPEN`

Hard target: `CRITICAL_COFACTOR_ALL_M_NONVANISHING_PROVED_OR_EXACT_COUNTEREXAMPLE`

## Execution binding

- Task: `RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF`
- Publication: `TP2-5547117E54D7A556279B`
- Taskbook: `research_tasks/PERFECT_PRIME_TABLE_CRITICAL_COFACTOR_ALL_M_PROOF_20260826.md`
- Taskbook blob: `sha1:d8c242ea1744056b2130ac989cf18866e08db4d5`
- Claim: `chatgpt-pptcc-20260826-2036`
- Researcher-ID: `EM-FREE-5K7N2Q`
- Execution record: `ER-F37E7D2B1430DA3E41FE`
- Execution branch: `research/perfect-prime-table-critical-cofactor-all-m-proof-em-free-5k7n2q`
- Base: `5b7a1f4e1826f32d0ff1708350bc613e58710848`

This return resumed the still-live owner claim after the prior session became stale. No second CLAIM was issued.

## 1. Exact critical matrix and shifted-Newton reduction

For `m >= 2`, put

\[
A_{ij}=\prod_{k=0}^{m-1}(1+i+mj+k m^2),\qquad 1\le i,j\le m.
\]

At critical degree `d=m-2`, the row-plus-column condition for
`D_{ij}=A_{ij}c(i,j)` gives the square matrix

\[
M_m[(i,j),(a,b)]
=
A_{ij}i^aj^b-A_{i1}i^a-A_{1j}j^b+A_{11},
\]

with rows `(i,j) in {2,...,m}^2` and columns `(a,b) in {0,...,m-2}^2`.

Let

\[
X_m(u)=\prod_{\nu=1}^{m}(u-\nu),\qquad
\mathcal A_m=\mathbf Q[x,y]/(X_m(x),X_m(y)),
\]

and use the shifted Newton basis

\[
e_{r,s}=(x-1)^{\underline r}(y-1)^{\underline s}.
\]

Define

\[
I=\{0,\ldots,m-2\}^2,\qquad
J=\{1,\ldots,m-1\}^2,
\]

\[
Z=x+my,\qquad
P_m(z)=\prod_{k=0}^{m-1}(z+1+k m^2),\qquad
T=P_m(Z).
\]

Multiplication by `Z` obeys

\[
Ze_{r,s}
=
e_{r+1,s}+m e_{r,s+1}
+[r+1+m(s+1)]e_{r,s}.
\]

The exact determinant identity is

\[
\boxed{
\det M_m
=
\left(\prod_{p=1}^{m-1}p!\right)^{2(m-1)}
\det T[J,I].
}
\]

Thus the original hard target is exactly `det T[J,I] != 0` for every `m >= 2`.

## 2. Prior boundary reduction retained

The full operator `T` is invertible because in grid-evaluation coordinates its eigenvalues are `A_{ij}>0`. With

\[
I^c=\{(r,s):r=m-1\text{ or }s=m-1\},
\qquad
J^c=\{(r,s):r=0\text{ or }s=0\},
\]

Jacobi gives

\[
\boxed{
\det T[J,I]
=
(-1)^{m+1}\det(T)\det B_m,
\qquad
B_m=T^{-1}[I^c,J^c].
}
\]

Hence the quadratic-size determinant is equivalent to a `(2m-1) x (2m-1)` hook determinant.

For `p>=r`, `q>=s` the inverse entries have the exact moment formula

\[
(T^{-1})_{(p,q),(r,s)}
=
\frac{C_m}{(p-r)!(q-s)!}
\int_0^1
t^{r+1+m(s+1)}
(t-1)^{p-r}(t^m-1)^{q-s}
(1-t^{m^2})^{m-1}\,dt,
\]

where

\[
C_m=\frac{m^{2(1-m)}}{(m-1)!}.
\]

They vanish outside that reachability support and satisfy strict checkerboard sign there.

The reciprocal kernel `K_{ij}=1/A_{ij}` is strictly totally positive, but generic STP is not enough: the already-frozen exact `m=2` Cauchy counterexample shows that STP alone does not force the corresponding signed bipartite Laplacian to have only the gauge kernel. That shortcut remains closed.

## 3. New exact mixed-forward-difference formula

Let

\[
d_{r,s}=r+1+m(s+1).
\]

For every polynomial `P`, if `a=p-r>=0` and `b=q-s>=0`, then

\[
\boxed{
[P(Z)]_{(p,q),(r,s)}
=
\frac{\Delta_1^a\Delta_m^b P(d_{r,s})}{a!b!},
}
\]

and the entry is zero if either index decreases.

This follows by expanding powers of `Z`: east raises increase the diagonal argument by `1`, north raises increase it by `m`, and Newton coefficient extraction on the resulting rectangular difference lattice is exactly the mixed forward difference above.

For the associated-graded pure raising operator `N=E_x+mE_y` and

\[
P_\beta(u)=\prod_{k=0}^{m-1}(u+\beta_k),
\]

one gets the closed entry formula

\[
\boxed{
[P_\beta(N)]_{(p,q),(r,s)}
=
\binom{a+b}{a}m^b e_{m-a-b}(\beta)
}
\]

when `a,b>=0` and `a+b<=m`, and zero otherwise.

This isolates the graded determinant as a concrete Schur/LGV candidate without asserting an unproved all-`m` coefficient-positivity theorem.

## 4. New symmetric Frobenius reduction

On

\[
A_x=\mathbf Q[x]/(X_m(x))
\]

define the Frobenius trace `tau_x` as the coefficient of `e_{m-1}` in the shifted-Newton representative. Equivalently,

\[
\boxed{
\tau_x(f)
=
\sum_{i=1}^{m}w_i f(i),
\qquad
w_i=\frac1{X_m'(i)}
=
\frac{(-1)^{m-i}}{(i-1)!(m-i)!}.
}
\]

The pairing `(f,g) -> tau_x(fg)` is nondegenerate because all evaluation weights `w_i` are nonzero.

Put

\[
U=\operatorname{span}\{e_0,\ldots,e_{m-2}\},
\qquad
V=\operatorname{span}\{e_1,\ldots,e_{m-1}\}.
\]

The restricted pairing `U x V -> Q` is perfect. Indeed, if `u in U` pairs to zero with all of `V`, then `tau_x(u)=0` as well, so `u` is orthogonal to `Qe_0 + V=A_x`, and Frobenius nondegeneracy forces `u=0`.

Let `tau=tau_x tensor tau_y`. Then `I=U tensor U`, `J=V tensor V`, and the matrix

\[
H_{I,J}=[\tau(e_a e_j)]_{a\in I,j\in J}
\]

is invertible.

Define on `I`

\[
\boxed{
G_m(c,d)=\tau\!\left(c\,P_m(x+my)\,d\right).
}
\]

If `Te_b` is expanded in the full Newton basis, every component outside `J` has `p=0` or `q=0` and is annihilated when paired with `I`. Therefore

\[
\boxed{
[G_m]=H_{I,J}\,T[J,I].
}
\]

Hence

\[
\boxed{
\det M_m\ne0
\iff
\det T[J,I]\ne0
\iff
G_m\text{ is nondegenerate on }U\otimes U.
}
\]

The form is symmetric. In evaluation coordinates it is

\[
\boxed{
G_m(c,d)
=
\sum_{i,j=1}^{m}
w_iw_jP_m(i+mj)c(i,j)d(i,j).
}
\]

This is the strongest new reduction in this checkpoint: the remaining problem is a symmetric signed-quadrature inertia/nondegeneracy theorem, rather than an opaque non-symmetric hook determinant.

Full proof details are frozen in:

`research_artifacts/PERFECT_PRIME_TABLE_CRITICAL_COFACTOR_ALL_M_PROOF/HOOK_NEWTON_FROBENIUS_CHECKPOINT_20260827.md`.

## 5. Exact finite guard retained

The exact standard-library checker remains at

`scripts/check_perfect_prime_table_critical_cofactor_all_m.py`

with machine-readable certificate

`research_artifacts/PERFECT_PRIME_TABLE_CRITICAL_COFACTOR_ALL_M_PROOF/finite_certificate_m2_m6.json`.

It verifies the original matrix, the shifted-Newton transfer minor, the exact determinant scale identity, and a signed-Laplacian cofactor for `m=2,...,6`. All are nonzero there. These finite checks are regression guards only and are not promoted to an all-`m` proof.

## 6. Hard-target disposition and next frontier

No exact counterexample was found in the retained finite guard, but this return does **not** prove the all-`m` theorem.

The durable unfinished unit is now sharpened to

\[
\boxed{
\texttt{FROBENIUS_NONDEGENERACY_LEMMA}:
\quad
G_m(c,d)=\tau(cP_m(x+my)d)
\text{ is nondegenerate for every }m\ge2.
}
\]

The recommended proof route is no longer generic total positivity. The shifted-Newton law

\[
x e_r=e_{r+1}+(r+1)e_r
\]

is a filtered/equivariant deformation of the truncated complete-intersection raising law, while `I=U tensor U` and `J=V tensor V` are Frobenius-dual rectangles. The next attack should therefore target a Hodge–Riemann / mixed-Lefschetz signature theorem or an equivalent sign-controlled factorial-Schur/LGV expansion for `det G_m`.

## Terminal verdict

`PARTIAL_EXACT_PROGRESS / BOUNDARY_REDUCTION_STRENGTHENED_TO_FROBENIUS_NONDEGENERACY / HARD_TARGET_OPEN`

No Working Truth, Foundation promotion, or `DONE` state is requested. This return is ready for Driver review as a researcher HANDOFF.
