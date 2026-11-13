# Wallis / sine discrete-rotation spectral precision theorems

Status: `FREE_RESEARCH / INDEPENDENTLY_REVERIFIED / EXACT_FINITE_CORE + ANALYTIC_COMPLETION / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Primary durable sources:
- issue comment `5525992157`;
- continuation comment `5526329654`;
- corrected quartic-certificate comment `5526379609`.
Cross-family current source:
- `research_notes/VIETE_WALLIS_INTERNAL_COMPLETION_EQUALITY_20260903.md`.

## 0. Validation verdict and scope

The #1159 theorem-candidate packet was independently rederived before extraction.

Verified independently:
- exact continuant/determinant coefficient formula for `F_M`;
- the stated compact-set `O(M^-2)` coefficient-error bound;
- discrete elliptic transfer typing;
- doubled-chain reflection parity;
- Hamming-shell integer spectrum and reflection parity;
- exact rational Wallis determinant ratio;
- target-free Wallis squeeze;
- common parity-curvature observer;
- exact doubled-chain parity-curvature collapse;
- even-site spectral decimation `u -> u(4-u)`;
- dyadic inverse branch and nested radicals;
- strict fourth-order Richardson lower bound;
- explicit `2/(15 q^4)` target-free width for dyadic `q>=2`;
- rational-function conjugacy no-go at finite spectrum strength.

Corrections made during verification:
1. every theorem using the smallest positive eigenvalue `a_q` is stated for `q>=2`;
2. `tau<4` is certified by the explicit rational alternating-series sign
   `S(4) < -268/405 < 0`, not by the earlier shorthand “spectral upper certificate at q=2”;
3. the numerical diagnostics in issue comment `5526379609` were recomputed and corrected.
No symbolic theorem below depends on those diagnostic decimals.

Classical Chebyshev/path-Laplacian formulas agree with the finite recurrence and spectrum.
No historical novelty is claimed for Chebyshev polynomials, path spectra, Krawtchouk modes,
Wallis inequalities, or Richardson extrapolation. The extracted content is the typed
Enterprise synthesis and the exact finite observer/decimation/certificate interface.

## 1. Native finite Dirichlet carrier

For integer `M>=2`, let `L_M^D` be the `(M-1)x(M-1)` tridiagonal matrix

```text
 2 -1  0  ...
-1  2 -1  ...
 0 -1  2  ...
...
```

and define

`F_M(x) = det(L_M^D - (x^2/M^2) I)/M`.

No circle, `pi`, continuous Sturm-Liouville operator, or Fourier basis appears in this
finite definition.

### WSR-T01 — exact normalized determinant coefficients

For every `M>=2`,

\[
\boxed{
F_M(x)=
\sum_{j=0}^{M-1}
\frac{(-1)^j x^{2j}}{(2j+1)!}
\prod_{r=1}^{j}\left(1-\frac{r^2}{M^2}\right).
}
\]

Proof kernel: the continuant recurrence

\[
D_0=1,\quad D_1=2-z,\quad D_n=(2-z)D_{n-1}-D_{n-2}
\]

for `z=x^2/M^2`, together with induction on the coefficients.

Classification: `EXACT_FINITE_ALGEBRA`.

### WSR-T02 — explicit compact-set convergence certificate

Let

\[
F(x)=\sum_{j=0}^\infty\frac{(-1)^j x^{2j}}{(2j+1)!}.
\]

Whenever

\[
1-\frac{R^2}{(2M+2)(2M+3)}>0,
\]

one has

\[
\boxed{
\sup_{|x|\le R}|F_M(x)-F(x)|
\le
\frac{R^2\cosh R+3R\sinh R}{24M^2}
+
\frac{R^{2M}}{(2M+1)!}
\frac{1}{1-\frac{R^2}{(2M+2)(2M+3)}}.
}
\]

Finite coefficient defect uses

\[
1-\prod_{r=1}^{j}(1-a_r)\le\sum_{r=1}^{j}a_r
\]

with `a_r=r^2/M^2`, and

\[
\sum_{j\ge0}\frac{j(j+1)(2j+1)R^{2j}}{(2j+1)!}
=
\frac{R(R\cosh R+3\sinh R)}4.
\]

Classification: `EXACT_ANALYTIC_CERTIFICATE_FROM_FINITE_COEFFICIENTS`.

## 2. Rotation-mode semantics

The interior eigenmode equation is

\[
v_{j+1}=(2-u)v_j-v_{j-1},
\]

with transfer matrix

\[
T(u)=
\begin{pmatrix}
2-u&-1\\
1&0
\end{pmatrix},
\qquad
\det T(u)=1.
\]

### WSR-T03 — finite elliptic-transfer interpretation

For `0<u<4`, `|tr T(u)|<2`, hence the real `SL_2` transfer is elliptic and real-conjugate
to a planar rotation. Dirichlet endpoints select the finite boundary-compatible modes.

This is a finite transfer interpretation. It does not identify the carrier with primitive
G0 Cell rotation.

Classification: `FINITE_EFFECTIVE_ROTATION_READOUT / NO_CONTINUOUS_SPECTRUM_INPUT`.

## 3. Power-series completion and Euler product

Define

\[
S(x)=\sum_{j=0}^\infty\frac{(-1)^j x^{2j+1}}{(2j+1)!},
\qquad
C(x)=S'(x),
\]

and let `tau` be the first positive zero of `S`.

The power-series ODE/addition laws give

\[
S'=C,\qquad C'=-S,\qquad S^2+C^2=1,
\]

and `S(tau/2)=1`.

For the finite Dirichlet chain, define the mode radius

\[
\rho_{k,M}=M\sqrt{u_{k,M}}.
\]

After analytic identification within the power-series completion,

\[
\rho_{k,M}=2M\,S\!\left(\frac{k\tau}{2M}\right).
\]

### WSR-T04 — determinant-to-Euler product

The finite determinant convergence plus fixed-mode convergence and the tail estimate
`rho_(k,M)>=2k` imply

\[
\boxed{
\frac{S(x)}x=
\prod_{k=1}^\infty
\left(1-\frac{x^2}{k^2\tau^2}\right).
}
\]

The tail control used for real `|x|<=R`, `K>=R`, is

\[
\left|
\log\prod_{k=K+1}^{M-1}
\left(1-\frac{x^2}{\rho_{k,M}^2}\right)
\right|
\le\frac{R^2}{3K}.
\]

Classification: `ANALYTIC_COMPLETION_THEOREM`.
Boundary: do not reclassify the infinite product as a primitive finite state.

## 4. Exact rational Wallis carrier

For `m` binary local orientation labels, explicitly pass to the permutation-invariant
Hamming-shell quotient `j=0,...,m`. Define

\[
(A_mf)(j)=j f(j-1)+(m-j)f(j+1),
\qquad
K_m=(mI-A_m)/2.
\]

The Krawtchouk coefficient states

\[
g_k(j)=[z^k](1-z)^j(1+z)^{m-j}
\]

satisfy

\[
K_mg_k=kg_k,\qquad k=0,\ldots,m.
\]

Complement reflection `Jf(j)=f(m-j)` gives

\[
Jg_k=(-1)^kg_k.
\]

### WSR-T05 — exact Wallis parity determinant

For `m=2n+1`,

\[
\det{}'K_m^+=2\cdot4\cdots(2n),
\qquad
\det K_m^-=1\cdot3\cdots(2n+1),
\]

so

\[
\boxed{
W_n
=
m\left(\frac{\det{}'K_m^+}{\det K_m^-}\right)^2
=
\prod_{r=1}^{n}\frac{(2r)^2}{(2r-1)(2r+1)}.
}
\]

The Hamming shell quotient is material. Restoring full hypercube multiplicities changes
the determinant ratio.

Classification: `EXACT_FINITE_RATIONAL_SPECTRAL_INVARIANT`.

### WSR-T06 — target-free Wallis squeeze

Let

\[
Q_n=W_n\frac{4n+2}{4n+1}.
\]

Then `W_n` is strictly increasing and `Q_n` strictly decreasing, because

\[
\boxed{
\frac{Q_{n+1}}{Q_n}
=
1-\frac1{(2n+1)^2(4n+5)}
<1.
}
\]

Moreover `Q_n/W_n -> 1`; hence both converge to the same internally defined `W_infty`,
and

\[
\boxed{
1<\frac{W_\infty}{W_n}\le\frac{4n+2}{4n+1}.
}
\]

No `pi` is needed for convergence or this finite tail certificate.

Classification: `EXACT_RATIONAL_LIMIT_CERTIFICATE`.

## 5. Common parity-curvature observer

For any positive mode-radius list `s_1,...,s_(2q-1)`, `q>=2`, define

\[
\boxed{
\operatorname{Curv}_q(s)
=
\prod_{r=1}^{q-1}
\frac{s_{2r}^2}{s_{2r-1}s_{2r+1}}.
}
\]

This observer is invariant under common rescaling of all radii.

### WSR-T07 — integer-mode specialization

For `s_k=k`,

\[
\boxed{
\operatorname{Curv}_q(1,2,\ldots,2q-1)=W_{q-1}.
}
\]

Thus the Wallis factors are the local multiplicative curvature of the integer mode ladder.

### WSR-T08 — doubled Dirichlet parity-curvature collapse

For the doubled Dirichlet mode radii `rho_(k,2q)`,

\[
\boxed{
\operatorname{Curv}_q(\rho)
=
\frac{\rho_{2,2q}}4
=
\frac{\rho_{1,q}}2.
}
\]

Pure finite proof:
- even squared-eigenvalue product:
  \[
  \prod_{r=1}^{q-1}u_{2r,2q}=q;
  \]
- odd squared-eigenvalue product:
  \[
  \prod_{r=1}^{q}u_{2r-1,2q}=2;
  \]
- spectral reflection:
  \[
  u_{2q-1,2q}=4-u_{1,2q};
  \]
- even-site decimation:
  \[
  u_{1,2q}(4-u_{1,2q})=u_{1,q}.
  \]

Hence a full-spectrum parity-curvature observer collapses exactly to one coarse
fundamental mode.

Classification: `EXACT_FINITE_SPECTRAL_RENORMALIZATION`.

## 6. Spectral decimation

### WSR-T09 — exact even-site decimation polynomial

If a sequence obeys

\[
v_{j+1}+v_{j-1}=(2-u)v_j,
\]

then its even subsequence obeys

\[
v_{2r+2}+v_{2r-2}
=
(2-R(u))v_{2r},
\]

where

\[
\boxed{R(u)=u(4-u).}
\]

This follows by eliminating the odd sites and is independent of trigonometric notation.

Classification: `EXACT_LOCAL_ALGEBRA / REUSABLE_REFINEMENT_OPERATOR`.

### WSR-T10 — inverse first-mode branch

For the smallest positive Dirichlet eigenvalue `a_q=u_(1,q)`, `q>=2`,

\[
\boxed{
a_{2q}=2-\sqrt{4-a_q}.
}
\]

For dyadic `q`, beginning from `a_2=2`, this produces a target-free nested-radical tower.

Current #1158 independently realizes the same dyadic radical state through finite
binary rotation refinement. The carriers must remain typed separately:
#1159 supplies the Dirichlet spectral origin; #1158 supplies the G1 finite orientation
refinement semantics.

Classification: `EXACT_FINITE_ALGEBRAIC_REFINEMENT`.

## 7. Fourth-order completion certificate

Define for `q>=2`

\[
T_q=q\sqrt{a_q},
\qquad
R_q=\frac{4T_{2q}-T_q}{3}.
\]

For dyadic `q`, both are constructible using only integers, rational arithmetic and
nested square roots.

Let `y=tau/(4q)` and

\[
h(y)=3y-S(y)(4-C(y)).
\]

### WSR-T11 — Richardson sign kernel

Using `S'=C`, `C'=-S`, `S^2+C^2=1`,

\[
\boxed{
h'(y)=2(1-C(y))^2.
}
\]

On the relevant positive interval this gives `R_q<tau`.

### WSR-T12 — explicit target-free quartic bracket

The elementary bound

\[
1-C(y)\le y^2/2
\]

implies

\[
0<\tau-R_q
\le\frac{\tau^5}{7680q^4}.
\]

To remove `tau` from the right side, use the finite rational sign certificate

\[
\boxed{
S(4)
<
4-\frac{4^3}{3!}
+\frac{4^5}{5!}
-\frac{4^7}{7!}
+\frac{4^9}{9!}
=
-\frac{268}{405}<0.
}
\]

Thus `tau<4`, and for every dyadic `q>=2`,

\[
\boxed{
R_q<\tau<R_q+\frac{2}{15q^4}.
}
\]

Classification: `FINITE_ALGEBRAIC_ENDPOINT + ANALYTIC_PROOF_CERTIFICATE`.

## 8. Internal completion bridge

From WSR-T04 at `x=tau/2` and `S(tau/2)=1`,

\[
W_\infty=\tau/2.
\]

Current cross-family work in
`VIETE_WALLIS_INTERNAL_COMPLETION_EQUALITY_20260903.md`
independently identifies the #1158 intrinsic finite-radical completion `Pi_rot` with
this same `tau`:

\[
\boxed{\Pi_{\rm rot}=\tau=2W_\infty.}
\]

This equality is internal to the project-defined completion systems. Naming that common
constant classical `pi` is a later compatibility layer.

## 9. Finite no-go boundary

### WSR-N01 — no universal rational functional conjugacy of the two finite spectra

The Hamming mode operator has rational/integer eigenvalues `0,...,m`. Any rational
functional calculus with rational coefficients and no poles on those eigenvalues produces
only rational eigenvalues.

Already `L_4^D` has eigenvalues

\[
2-\sqrt2,\quad2,\quad2+\sqrt2.
\]

Therefore no universal rational functional calculus of the Hamming integer-mode operator
can be similar to the finite Dirichlet rotation operator.

Consequence:

\[
\boxed{
\text{common observer/completion} \ne \text{finite spectral identity}.
}
\]

The correct bridge is observer-level and renormalization-level, not carrier identity.

## 10. Tool-harvest resolution

Current reuse gate result:

- `T5_PRECISION_REFINEMENT`: `EXTEND_EXISTING_TOOL`.
  - reused role: finite coarse/fine precision typing;
  - exact missing capability: algebraic finite-spectrum decimation, parity-curvature readout,
    and certified completion brackets.
  - boundary retained: the executable tool remains finite; analytic completion enters only
    through separately stated theorems.
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED`.
  - reflection/complement parity is treated as a declared finite involution;
  - no absolute orientation/sign is inferred.
- `T10_LOCAL_REDISTRIBUTION_TOPPLING`: `NOT_APPLICABLE`.
  - sharing a Laplacian-shaped matrix does not make the spectral problem a toppling system.
- `T8_RELATION_OBSERVABLE_SPECTRUM`: `NOT_APPLICABLE`.
  - “spectrum” there is relation-observable branching, not matrix eigenmode spectrum.

No new top-level tool family is justified.

Extracted executable candidate:
`src/enterprise_math/spectral_precision.py`

Harvest record:
`research_method_inventory_addenda/WALLIS_SINE_SPECTRAL_PRECISION_20260903.json`

## 11. Lean plan

Formalization is staged from the algebraic kernel outward.

Stage L1:
1. local spectral-decimation identity;
2. inverse-decimation algebraic identity;
3. Richardson derivative algebraic kernel;
4. exact rational `S(4)` partial-sum certificate.

Stage L2:
5. continuant determinant recurrence;
6. `det L_M^D=M`;
7. even/odd product identities on doubled chains;
8. parity-curvature collapse.

Stage L3:
9. Hamming-shell integer-mode eigenbasis/parity;
10. exact Wallis determinant ratio and rational squeeze.

Stage L4:
11. power-series completion and first-positive-zero infrastructure;
12. Euler product;
13. quartic interval theorem;
14. internal `Pi_rot=tau=2W_infty` bridge after importing the #1158 completion theorem.

No `sorry`, `admit`, custom axiom, or target value of `pi` is permitted in the formalization.
