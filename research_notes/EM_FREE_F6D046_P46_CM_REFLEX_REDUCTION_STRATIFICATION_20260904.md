# P46 at p=7: explicit Jacobian descent, quartic CM reflex, and reduction stratification

Status: `FREE_RESEARCH / DERIVED EXACT CONTINUATION / CORRECTION-AWARE / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units:

- `R40-P46-P7-EXPLICIT-GENUS2-WEIL-RESTRICTION`
- `R41-P46-QUARTIC-CM-PRIMITIVE-REFLEX`
- `R42-P46-SPLIT-INERT-REDUCTION-STRATIFICATION`
- `R43-P46-POLARIZATION-ISOGENY-BOUNDARY`
- `R44-P46-P7-ALMOST-ORDINARY-NEWTON-DECOMPOSITION`

## 1. Fixed input

The p=7 characteristic polynomial is

\[
f_7(X)=X^8+5X^6+245X^2+2401=h(X^2),
\]

where

\[
h(T)=T^4+5T^3+245T+2401.
\]

The polynomial \(h\) is irreducible. Its associated abelian-surface isogeny class over \(\mathbf F_{49}\) is absolutely simple, and the earlier Honda--Tate calculation gives

\[
P_{46,7}\otimes_{\mathbf F_7}\mathbf F_{49}\sim B^2,
\qquad
\operatorname{End}^0_{\overline{\mathbf F}_7}(P_{46,7})\simeq M_2(F),
\]

with \(F=\mathbf Q(\alpha)\), \(h(\alpha)=0\).

## 2. Explicit genus-2 and Weil-restriction realization

A deterministic exact search over

\[
\mathbf F_{49}=\mathbf F_7(w),\qquad w^2=-1,
\]

produces a squarefree monic quintic defining a genus-2 curve \(C_7/\mathbf F_{49}\). Its exact equation is stored in the companion search certificate. Direct point counting gives

\[
\#C_7(\mathbf F_{49})=55,
\qquad
\#C_7(\mathbf F_{49^2})=2377.
\]

Therefore \(\operatorname{Jac}(C_7)\) has Weil polynomial \(h(T)\), and hence

\[
\boxed{B\sim\operatorname{Jac}(C_7).}
\]

Consequently

\[
\boxed{P_{46,7}\otimes\mathbf F_{49}\sim\operatorname{Jac}(C_7)^2.}
\]

The characteristic polynomial of the Weil restriction is \(h(X^2)=f_7(X)\). Tate's isogeny theorem therefore gives

\[
\boxed{P_{46,7}\sim_{\mathbf F_7}\operatorname{Res}_{\mathbf F_{49}/\mathbf F_7}\operatorname{Jac}(C_7).}
\]

This gives a concrete principally polarizable fourfold in the exact \(\mathbf F_7\)-isogeny class.

## 3. Polarization boundary

The Jacobian polarization is principal, and Weil restriction carries it to a principal polarization. Thus the unpolarized isogeny class of \(P_{46,7}\) is principally polarizable.

The geometric Prym construction, however, carries polarization type \((1,1,1,2)\), of degree \(4\), whereas a principal polarization has degree \(1\). Therefore the displayed isogeny cannot be promoted without additional data to an isomorphism of polarized abelian varieties:

\[
\boxed{\text{same isogeny class}\ne\text{same polarized object}.}
\]

## 4. The quartic CM field

Write the roots as \(\alpha_1,49/\alpha_1,\alpha_2,49/\alpha_2\), and put \(x_j=\alpha_j+49/\alpha_j\). Then

\[
(x-x_1)(x-x_2)=x^2+5x-98,
\]

so

\[
\boxed{F^+=\mathbf Q(\sqrt{417}).}
\]

For \(x_1=(-5+\sqrt{417})/2\),

\[
F=\mathbf Q\!\left(\sqrt{417},\sqrt{\frac{-171-5\sqrt{417}}2}\right).
\]

Both real conjugates of the radicand are negative, so \(F\) is a quartic CM field. Moreover

\[
\frac{-171-5\sqrt{417}}2\cdot\frac{-171+5\sqrt{417}}2=4704=28^2\cdot6.
\]

Hence

\[
\boxed{N=F(\sqrt6),\qquad \operatorname{Gal}(N/\mathbf Q)\simeq D_4.}
\]

Thus \(F\) contains no imaginary-quadratic subfield and its quartic CM types are primitive; modulo complex conjugation there are two type classes.

The integral-basis certificate gives

\[
\operatorname{disc}(F)=4173336=2^3 3^3 139^2,
\qquad \operatorname{disc}(F^+)=417,
\]

so \(N_{F^+/\mathbf Q}(\mathfrak d_{F/F^+})=24\).

## 5. Primitive reflex field

Choose \(\Phi=\{\alpha_1,\alpha_2\}\). If \(\eta=\alpha_1+\alpha_2\), elimination gives

\[
\boxed{\eta^4+10\eta^3+123\eta^2+490\eta+1225=0.}
\]

Equivalently, with \(u=2\eta+5\),

\[
u^2=-171+56\sqrt6.
\]

Thus

\[
\boxed{F^{\mathrm r}=\mathbf Q\!\left(\sqrt6,\sqrt{-171+56\sqrt6}\right),\qquad (F^{\mathrm r})^+=\mathbf Q(\sqrt6).}
\]

The type norm \(\beta=N_\Phi(\alpha)=\alpha_1\alpha_2\) has polynomial

\[
\boxed{R_\Phi(Z)=Z^4+98Z^3+6027Z^2+235298Z+5764801.}
\]

Its real-trace polynomial is \(y^2+98y+1225\), with discriminant \(4704=28^2\cdot6\). This independently recovers the reflex real subfield. The reflex field has the same \(D_4\) normal closure as \(F\), but a different distinguished real quadratic subfield.

## 6. Split/inert reduction theorem

Let \(p\ne2,3\) be a rational prime of good reduction. The geometric endomorphism field is \(K=\mathbf Q(i)\), and Frobenius acts on \(K\) through the Artin symbol of \(p\).

If \(p\equiv1\pmod4\), Frobenius commutes with \(i\), and

\[
P_p(X)=g_p(X)\overline{g_p(X)},\qquad \deg g_p=4.
\]

No evenness or quadratic base-change splitting is forced.

If \(p\equiv3\pmod4\), Frobenius conjugates \(i\) to \(-i\). Its eigenvalues occur in \(\lambda,-\lambda\) pairs, hence

\[
\boxed{P_p(X)=H_p(X^2)}
\]

for a monic degree-four integer polynomial \(H_p\), and every odd Frobenius trace vanishes. After base change to \(\mathbf F_{p^2}\), each squared eigenvalue occurs twice, so

\[
\boxed{P_{p,\mathbf F_{p^2}}(T)=H_p(T)^2.}
\]

Honda--Tate reduces geometric decomposition at an inert prime to the factorization and local invariants of \(H_p\). If \(H_p\) is an irreducible surface Weil polynomial of exponent one, then

\[
P_{46,p}\otimes\mathbf F_{p^2}\sim B_p^2.
\]

If \(P_p(X)=H_p(X^2)\) is also irreducible, the original reduction is simple over \(\mathbf F_p\) and lies in the quadratic Weil-restriction isogeny class of \(B_p\). The p=7 computation realizes exactly this stratum.

## 7. The p=7 Newton and prime decomposition

Modulo \(7\),

\[
x^2+5x-98\equiv x(x-2).
\]

The prime with \(x\equiv2\) splits in \(F/F^+\), producing root valuations \(0\) and \(2\). The prime with \(x\equiv0\) remains degree two and produces two roots of valuation \(1\). Hence

\[
7\mathcal O_F=\mathfrak p_0\mathfrak p_{1/2}\mathfrak p_1,
\]

with residue degrees \(1,2,1\), and

\[
v_{\mathfrak p_0}(\alpha)=0,\qquad v_{\mathfrak p_{1/2}}(\alpha)=1,\qquad v_{\mathfrak p_1}(\alpha)=2.
\]

Complex conjugation exchanges \(\mathfrak p_0\) and \(\mathfrak p_1\) and fixes \(\mathfrak p_{1/2}\).

Relative to \(q=49\), the Newton slopes of \(B\) are

\[
\boxed{0,\tfrac12,\tfrac12,1.}
\]

Thus \(B\) is almost ordinary, with p-rank \(1\); for an abelian surface this forces a-number \(1\). The Newton slopes of \(P_{46,7}\) are doubled:

\[
\boxed{0,0,\tfrac12,\tfrac12,\tfrac12,\tfrac12,1,1,}
\]

and its p-rank is \(2\).

## 8. Scope and classification

The exact conclusions are

\[
\boxed{P_{46,7}\sim\operatorname{Res}_{\mathbf F_{49}/\mathbf F_7}\operatorname{Jac}(C_7),}
\]

\[
\boxed{F^+=\mathbf Q(\sqrt{417}),\quad(F^{\mathrm r})^+=\mathbf Q(\sqrt6),\quad\operatorname{Gal}(N/\mathbf Q)=D_4.}
\]

None supplies a new Enterprise Math axiom. None alters P000, and none identifies an unpolarized isogeny with a polarized isomorphism.

Classification:

`DERIVED_EXPLICIT_FINITE_FIELD_MODEL / DERIVED_CM_REFLEX_THEOREM / DERIVED_REDUCTION_STRATIFICATION / EXACT_POLARIZATION_BOUNDARY / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 9. Next frontier

1. determine the Shimura--Taniyama CM polarization class for each primitive type of \(F\);
2. decide whether the explicit finite-field principal polarization lifts to a characteristic-zero Jacobian with the prescribed reflex type;
3. classify the integral isogeny degree between the principal Weil-restriction polarization and the type \((1,1,1,2)\) Prym polarization;
4. extend the split/inert theorem from isogeny decomposition to integral p-divisible and polarization strata.
