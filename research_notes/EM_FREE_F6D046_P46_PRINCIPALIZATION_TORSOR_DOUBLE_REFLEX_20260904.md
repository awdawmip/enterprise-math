# Principalization torsor, stable-Jacobian boundary, and explicit double reflex

Status: `FREE_RESEARCH / DERIVED EXACT CONTINUATION / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units: `R49-PRINCIPALIZATION-TORSOR / R50-STABLE-JACOBIAN-DELTA2 / R51-DOUBLE-REFLEX-D4 / R52-REFLEX-DISCRIMINANT`.

## 1. Principalization scheme

For the p=7 Prym reduction, `ker(lambda_P)=E[2]`. The geometric degree-2 principalizations are indexed by the three maximal isotropic lines

\[
\mathscr L=\mathbf P(E[2]).
\]

The 2-division polynomial of `E:y^2=x^3-6x^2+36` reduces to the irreducible cubic `x^3+x^2+1` over `F7`. Frobenius is a 3-cycle on the three lines. Hence, as a finite etale scheme,

\[
\boxed{\mathscr L\simeq\operatorname{Spec}\mathbf F_{7^3}.}
\]

The three principal quotients form one Galois orbit. There is no distinguished quotient over `F7` or `F49`; over `F_{7^3}` the cubic point splits and all three appear.

## 2. Stable genus-4 realization

The explicit genus-2 curve `C7/F49` has 55 rational points. Choose `Q in C7(F49)` and, over `F49`, form

\[
D_{49}=C_7\cup_{Q\sim Q^{(7)}}C_7^{(7)}.
\]

Frobenius exchanges the two components and preserves the separating node, so the curve descends to a stable curve `D7/F7`. It has arithmetic genus `2+2=4`, and

\[
\boxed{\operatorname{Jac}(D_7)\simeq\operatorname{Res}_{\mathbf F_{49}/\mathbf F_7}\operatorname{Jac}(C_7)}
\]

as principally polarized abelian varieties. Therefore the canonical Weil-restriction polarization lies on the separating boundary

\[
\boxed{\Delta_2\subset\overline{\mathcal M}_4,}
\]

rather than in the smooth Jacobian locus represented by that polarization.

## 3. Reflex discriminant

For

\[
\eta^4+10\eta^3+123\eta^2+490\eta+1225=0,
\]

the polynomial discriminant is

\[
2^{10}3^3 5^2 7^4 139.
\]

The power order has index `5*7^2=245` in the maximal order. Hence

\[
\boxed{\operatorname{disc}(F^{\mathrm r})=2^{10}3^3 139=3843072.}
\]

Since `disc(Q(sqrt6))=24`,

\[
\boxed{N_{\mathbf Q(\sqrt6)/\mathbf Q}(\mathfrak d_{F^{\mathrm r}/\mathbf Q(\sqrt6)})=2^4\cdot3\cdot139=6672.}
\]

The factors `5^2*7^4` in the trace-generator discriminant are order-index artifacts, not field ramification.

## 4. Double-reflex return

The primitive type norm has polynomial

\[
R_\Phi(Z)=Z^4+98Z^3+6027Z^2+235298Z+5764801.
\]

Its reciprocal pair traces satisfy `y^2+98y+1225=0`, so

\[
y_{1,2}=-49\pm14\sqrt6.
\]

The corresponding CM radicands are

\[
e_1=-6027-1372\sqrt6,\qquad e_2=-6027+1372\sqrt6,
\]

and

\[
\boxed{e_1e_2=25030425=245^2\cdot417.}
\]

Thus the normal closure of the reflex field is `F^r(sqrt417)`, and applying the primitive-reflex construction returns the real quadratic field `Q(sqrt417)` and therefore the original quartic CM field/type up to conjugate-type equivalence:

\[
\boxed{(F,\Phi)^{\mathrm{rr}}\simeq(F,\Phi).}
\]

The explicit real-field exchange is

\[
\mathbf Q(\sqrt{417})\xleftrightarrow{\mathrm{reflex}}\mathbf Q(\sqrt6)
\]

inside one common `D4` normal closure.

## 5. Typed interpretation and boundary

The quadratic endomorphism character, cubic principalization torsor, and primitive CM-reflex involution are three different carriers. None is recoverable from the Boolean statement that a characteristic polynomial becomes a square.

Classification: `DERIVED_PRINCIPALIZATION_TORSOR / STABLE_JACOBIAN_BOUNDARY / EXPLICIT_DOUBLE_REFLEX / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 6. Next frontier

Identify the Rosati-hermitian lattice of the Prym polarization inside `M_2(F)`, enumerate the three cubic-field principal quotients, and test whether one becomes the decomposable `Delta_2` polarization over `F_{7^6}`. This is an integral lattice problem, not a Frobenius-polynomial problem.
