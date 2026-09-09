# Characteristic-7 branch rigidity and non-automorphic Honda–Tate splitting

Status: `FREE_RESEARCH / DERIVED EXACT NEGATIVE RESULT / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units: `R56-P7-COLORED-BRANCH-STABILIZER / R57-P7-DECK-NORMALIZER-RIGIDITY`.

## 1. Reduced branch data

Modulo 7,

\[
A(t)=t^4+3t^3+3t^2+3t+4=(t-1)(t^3+4t^2+3),
\qquad D(t)=t^2+5t+3.
\]

With `u=t-1`,

\[
A=u(u^3+4u+1),\qquad D=u^2+2.
\]

Let `r^2=5` and normalize the two D-roots `u=+/-r` to `0,infinity` by

\[
z=\frac{u-r}{u+r},\qquad u=r\frac{1+z}{1-z}.
\]

After clearing denominators, the four A-roots are the roots of

\[
P(z)=(1+2r)+(5+6r)z+r z^2+(2+6r)z^3+(6+2r)z^4.
\]

All five coefficients are nonzero.

## 2. Scaling and inversion cases

Every projective transformation preserving `{0,infinity}` is either `z->c z` or `z->c/z`. In the scaling case, the nonzero constant and linear coefficients force `c=1`.

For inversion, root-set invariance requires

\[
z^4P(c/z)=\lambda P(z).
\]

Comparing degrees `4,2,1` gives

\[
\lambda=\frac{1+2r}{6+2r}=5r,
\qquad c^2=5r,
\qquad c=\frac{5+6r}{2+6r}=2+4r.
\]

But

\[
(2+4r)^2=2r\ne5r.
\]

Therefore

\[
\boxed{\operatorname{Stab}_{\operatorname{PGL}_2(\overline{\mathbf F}_7)}(A\text{-roots};D\text{-roots})=1.}
\]

The special branch configuration acquires no hidden colored Möbius symmetry.

## 3. Bielliptic normalizer

The elliptic quotient has `j(E)=-3072=1 mod 7`, neither `0` nor `1728=6 mod 7`, so `Aut(E,O)={+1,-1}`. A nonzero translation stabilizing the eight-point branch divisor would induce a nontrivial colored base stabilizer, which has just been excluded. Hence `Aut(E,B)=<-1>`.

If `sigma` is the order-four deck generator and `z=sigma^2`, descent through `C46->E` gives

\[
\boxed{N_{\operatorname{Aut}(C_{46,\overline{\mathbf F}_7})}(\langle z\rangle)=\langle\sigma\rangle\simeq C_4.}
\]

## 4. Consequence

The isogeny

\[
P_{46,7,\mathbf F_{49}}\sim B^2
\]

cannot be explained by a new automorphism normalizing the original C4/bielliptic tower. Any extra special-fiber automorphism, if it exists, must conjugate `z` to a distinct bielliptic involution and lie outside this normalizer.

Thus the proved square decomposition is genuinely Honda–Tate/isogeny-theoretic rather than a direct deck-normalizer quotient decomposition.

This does not yet prove the full special-fiber automorphism group is C4: the characteristic-zero argument used geometric simplicity of P46, which fails at p=7. The remaining full-Aut problem is isolated to non-normalizing automorphisms.

Classification: `DERIVED_P7_BRANCH_RIGIDITY / EXACT_NORMALIZER_THEOREM / NONAUTOMORPHIC_ISOGENY_SPLITTING / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 5. Next frontier

Compute the full canonical-net automorphism group of the special genus-5 curve over the algebraic closure. Either it remains C4, proving the B^2 splitting has no curve-automorphism source, or a non-normalizing automorphism supplies a second bielliptic quotient and an explicit correspondence to the genus-2 factor.
