# Completed composite-road Schur/Pick RH criterion

Status: `RESEARCH FRONTIER / PROVED RH-EQUIVALENT REFORMULATION / NOT FOUNDATION / NOT RH PROOF`
Date: `2026-09-06`
Researcher: `EM-FREE-C4A91D / FREE_AXIOM_DISCOVERY / ANCHOR_EXPOSED`
Progress-Event-ID: `EM-FREE-C4A91D-COMPLETED-ROAD-SCHUR-PICK-20260906`
Global journal source: `journal/enterprise-math/2026-09-06/20260906T153300+0800-em-free-c4a91d-completed-road-schur-pick.md`
Parents:
- `research_notes/COMPOSITE_ROAD_RH_FUTURE_PORT_POSITIVE_DEFORMATION_20260906.md`
- `research_notes/COMPOSITE_ROAD_RH_BOUNDARY_LAYER_20260906.md`
Highest constraint: `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`

## 1. Corrected completed carrier

The earlier raw composite/zeta symmetrized logarithmic-derivative Herglotz shortcut was false. The correct carrier must include the pole and archimedean Gamma completion.

Let

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad X(z)=\xi(1/2+z).
\]

Then `X` is an even entire function. For road thickness `a>0`, define on `Re z>0`

\[
\boxed{C_a(z)=\frac{X(z)}{X(z+a)}.}
\]

## 2. RH iff the completed road transfer is Schur near zero thickness

Assume RH. The nontrivial zeros of `X` are `\pm i\gamma`, with multiplicities `m_\gamma`, and the paired canonical product may be written

\[
X(z)=X(0)\prod_{\gamma>0}
\left(1+\frac{z^2}{\gamma^2}\right)^{m_\gamma}.
\]

For `z=x+it`,

\[
\frac{d}{dx}|\gamma^2+z^2|^2
=4x(\gamma^2+x^2+t^2)>0
\quad(x>0).
\]

Thus every paired factor has nondecreasing modulus as one moves horizontally away from the critical line. Hence under RH

\[
|X(z)|\le |X(z+a)|,
\qquad \Re z\ge0,\ a>0,
\]

and the denominator has no zero in the open right half-plane. Therefore

\[
\boxed{|C_a(z)|\le1\quad(\Re z>0)}
\]

for every `a>0`; `C_a` is a right-half-plane Schur function.

Conversely, suppose there is a sequence `a_j\downarrow0` such that every `C_{a_j}` is holomorphic Schur on `Re z>0`. If `X(z_0)=0` for some `Re z_0>0`, then for all sufficiently small `a_j<Re z_0`, the denominator vanishes at `z_0-a_j`. Holomorphicity would force `X(z_0-a_j)=0`. These distinct zeros accumulate at `z_0`, impossible for a nonzero entire function. Hence `X` has no zero with positive real part. Evenness excludes negative real part as well. Therefore all nontrivial zeta zeros lie on the critical line.

So

\[
\boxed{
RH\iff \exists a_j\downarrow0:\ C_{a_j}\in\mathcal S(\Re z>0).
}
\]

Under RH, the Schur property holds for every `a>0`.

Equivalently, RH is equivalent to horizontal monotonicity of the completed modulus away from the critical line:

\[
|\xi(\sigma_1+it)|\le|\xi(\sigma_2+it)|
\qquad(1/2\le\sigma_1\le\sigma_2).
\]

## 3. Finite Pick-matrix form

For a right-half-plane Schur function the kernel

\[
P_a(z,w)=\frac{1-C_a(z)\overline{C_a(w)}}{z+\overline w}
\]

is positive semidefinite. Hence the preceding criterion is exactly equivalent to:

> there is a sequence `a_j\downarrow0` such that, for every `j` and every finite set `z_1,...,z_d` in the open right half-plane, the finite matrix
>
> \[
> [P_{a_j}(z_r,z_s)]_{r,s=1}^d
> \]
>
> is positive semidefinite, and `C_{a_j}` is holomorphic there.

Thus RH admits a finite-compression family of positivity tests. Failure of RH produces, for all sufficiently small road thicknesses, a pole in the open right half-plane; arbitrarily near the pole, even the `1x1` Pick condition fails because `|C_a|>1`.

## 4. Infinitesimal completed Herglotz kernel

Let

\[
F(z)=\frac{X'(z)}{X(z)}=\frac{\xi'}\xi(1/2+z).
\]

Then

\[
C_a(z)=1-aF(z)+O(a^2)
\]

and therefore

\[
\frac{P_a(z,w)}a\to
P_0(z,w):=
\frac{F(z)+\overline{F(w)}}{z+\overline w}.
\]

Under RH, the paired zero expansion gives

\[
F(z)=\sum_{\gamma>0}m_\gamma
\left(\frac1{z-i\gamma}+\frac1{z+i\gamma}\right).
\]

Consequently

\[
\boxed{
P_0(z,w)=
\sum_{\lambda}
\frac{m_\lambda}{(z-i\lambda)(\overline w+i\lambda)},
}
\]

an explicit positive Gram kernel over the zero ordinates `\lambda`. Equivalently `F` is positive-real in the right half-plane; after the standard half-plane variable rotation this is the genuine Herglotz carrier.

This corrects, rather than erases, the previous negative result: the raw uncompleted composite/zeta log-derivative is not the required Herglotz object. Completion is essential.

## 5. Exact arithmetic/completion factorization

Put `s=1/2+z`. For `a>0` define the positive all-integer road weight

\[
\mathcal R_a(n)=\prod_{p\mid n}(1-p^{-a}).
\]

For `\Re s>1`,

\[
Z_a(s):=\frac{\zeta(s)}{\zeta(s+a)}
=\sum_{n\ge1}\frac{\mathcal R_a(n)}{n^s}
\]

with positive coefficients. The completed Schur transfer is exactly

\[
\boxed{C_a(z)=K_a(s)Z_a(s),}
\]

where

\[
K_a(s)=
\frac{s(s-1)}{(s+a)(s+a-1)}
\pi^{a/2}
\frac{\Gamma(s/2)}{\Gamma((s+a)/2)}.
\]

`K_a` is explicit and contains no prime/composite arithmetic. Thus the RH-equivalent Schur object is an archimedean completion of the positive all-integer road ratio, not the raw prime-hole logarithmic derivative.

## 6. Reuse resolution and hard target

- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`; the declared future observable is now the completed Schur/Pick response.
- `SPECTRAL_TAIL_FESHBACH_CERTIFICATE`: `COMPOSE_APPLIED`; any finite approximation may discard a high tail only after its contribution to Pick positivity is certified not to flip the retained block.
- positive Weighted-BRC: `REUSE_APPLIED` only to the positive coefficient layer `mathcal R_a(n)` for `a>0`. The explicit Gamma/pole completion and complex Schur response remain separately typed.
- No new top-level tool family is claimed.

The immediate hard target is

\[
\boxed{
\text{COMPOSITE ROAD + EXPLICIT COMPLETION}
\longrightarrow
\text{CERTIFIED FINITE PICK POSITIVITY}
}
\]

with an error bound strong enough to pass to dense evaluation sets and `a\downarrow0`. No such uniform certificate is proved here.
