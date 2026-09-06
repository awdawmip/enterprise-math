# Free Research — Centered Tail-Potential Coercivity and Scale Localization

Status: `FREE_RESEARCH_FRONTIER / EXACT_CENTERED_IDENTITY / RECIPROCAL_KERNEL_EXCLUDED_BY_STANDARD_GAUGE / NEAR_MODE_SCALE_LOCALIZATION / FULL_CASCADE_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_TAIL_AUGMENTED_RELATION_STATE_20260904.md`

## 1. Executive advance

The same-scale coefficient channel from the moving-cutoff tail is

\[
w_a=V_a x_a,
\qquad
V_a:=A(m_a)-A(Y),
\qquad
m_a=\left\lfloor\frac{Y^2}{a}\right\rfloor.
\]

The relevant lifted value is

\[
(D_Vx)_a=(U+V_a)x_a,
\qquad
U=\sum_a u_a.
\]

On unrestricted value channels, `D_V` has a reciprocal kernel after passing to pair differences: choosing `x_a=C/(U+V_a)` makes `D_Vx` constant.  Thus no uncentered pair-energy coercivity is possible.

However, quotient relation fields live in the standard/mean-zero sector.  On that sector there is an exact positive identity:

\[
\boxed{
\mathcal E_u(D_Vx)
=U^2\mathcal E_u(x)
+4U^2\sum_a u_aV_ax_a^2
+\mathcal E_u(Vx).
}
\]

The tail coefficient is therefore a positive potential, not merely an error.  Any mode nearly saturating the baseline must concentrate where `V_a/U` is small, and those labels send the original scale `Y^2` down to approximately `Y`.

---

## 2. Finite pair-energy notation

For a finite action family `S`, positive weights `u_a`, and scalar values `x_a`, define

\[
U:=\sum_{a\in S}u_a,
\]

\[
M_1(x):=\sum_a u_ax_a,
\qquad
M_2(x):=\sum_a u_ax_a^2,
\]

and the complete weighted pair energy

\[
\mathcal E_u(x)
:=\sum_{a,b}u_au_b(x_a-x_b)^2.
\tag{2.1}
\]

A direct expansion gives

\[
\boxed{
\mathcal E_u(x)=2UM_2(x)-2M_1(x)^2.
}
\tag{2.2}
\]

This is twice the total mass times the unnormalized weighted variance.

---

## WTC-T01 — Exact centered coefficient-lift identity

Assume the standard gauge

\[
M_1(x)=0.
\tag{3.1}
\]

Let

\[
y_a=(U+V_a)x_a,
\qquad
w_a=V_ax_a.
\]

Then

\[
M_1(y)=M_1(w)
\]

and

\[
M_2(y)
=U^2M_2(x)+2U\sum_a u_aV_ax_a^2+M_2(w).
\]

Using (2.2) for `x`, `y`, and `w`, one obtains

\[
\boxed{
\mathcal E_u(y)
=U^2\mathcal E_u(x)
+4U^2\sum_a u_aV_ax_a^2
+\mathcal E_u(w).
}
\tag{3.2}
\]

Every term is finite and exact.

If `u_a>=0` and `V_a>=0`, then

\[
\boxed{
\mathcal E_u(y)
\ge U^2\mathcal E_u(x)
+4U^2\sum_a u_aV_ax_a^2
\ge U^2\mathcal E_u(x).
}
\tag{3.3}
\]

The second positive term is the tail-potential energy; the third term in (3.2) is the ordinary relation energy of the product channel `w=Vx`.

---

## WTC-N01 — Uncentered reciprocal-kernel no-go

If `U+V_a` is nonzero for every action, choose

\[
x_a=\frac{C}{U+V_a}.
\]

Then

\[
y_a=(U+V_a)x_a=C
\]

is constant, so

\[
\mathcal E_u(y)=0.
\]

Whenever `V` is nonconstant and at least two weights are positive,

\[
\mathcal E_u(x)>0.
\]

Therefore no estimate

\[
\mathcal E_u(x)\le C_0\mathcal E_u(D_Vx)
\]

can hold on the full value space.

This does not obstruct the relation-field program, because its physical fluctuation sector is values modulo constants.  It does show that the mean/trivial component must be split before invoking coefficient coercivity.

---

## 4. Gauge decomposition in the augmented state

Let

\[
\bar x=U^{-1}\sum_a u_ax_a,
\qquad
x_a^\circ=x_a-\bar x.
\]

Then

\[
\mathcal E_u(x^\circ)=\mathcal E_u(x)
\]

and `M_1(x^circ)=0`.

The coefficient channel decomposes as

\[
V_ax_a=V_ax_a^\circ+\bar xV_a.
\tag{4.1}
\]

By linearity of the weighted relation field,

\[
\boxed{
Z^{Vx}=Z^{Vx^\circ}+\bar xZ^V.
}
\tag{4.2}
\]

Thus standard-gauge coercivity does not discard the mean.  The mean couples only to the separately retained coefficient-field channel `Z^V`, which is already part of the tail-augmented relation state and is annihilated by the same `S_3` standard projection.

---

## WTC-T02 — Threshold localization

For a threshold `L>0`, define the high-potential set

\[
H_L:=\{a\in S:V_a\ge L\}.
\]

Equation (3.2) immediately yields

\[
\boxed{
\mathcal E_u(y)-U^2\mathcal E_u(x)
\ge4U^2L\sum_{a\in H_L}u_ax_a^2.
}
\tag{5.1}
\]

Suppose a centered mode is `epsilon`-near the baseline:

\[
\mathcal E_u(y)
\le(1+\varepsilon)U^2\mathcal E_u(x).
\tag{5.2}
\]

Since

\[
\mathcal E_u(x)=2U\sum_a u_ax_a^2,
\]

we obtain

\[
\boxed{
\sum_{a\in H_L}u_ax_a^2
\le\frac{\varepsilon U}{2L}
\sum_a u_ax_a^2.
}
\tag{5.3}
\]

Taking `L=eta U` gives

\[
\boxed{
\frac{\sum_{V_a\ge\eta U}u_ax_a^2}
{\sum_a u_ax_a^2}
\le\frac{\varepsilon}{2\eta}.
}
\tag{5.4}
\]

Therefore every near-baseline mode is quantitatively localized in the low-tail region

\[
V_a<\eta U.
\]

---

## WTC-T03 — Arithmetic scale localization

For prime-power weights

\[
u_a=\frac{\Lambda(a)}a,
\]

we already have

\[
A(X)=\log X+O(1),
\qquad
U=A(Y)=\log Y+O(1).
\]

At `n=Y^2`,

\[
V_a=A(m_a)-A(Y),
\qquad
m_a=\left\lfloor\frac{Y^2}{a}\right\rfloor.
\]

For every fixed `eta>0`, the condition

\[
V_a<\eta U
\]

forces, up to an `eta`-dependent constant,

\[
\boxed{
a\gg_\eta Y^{1-\eta}}
\tag{6.1}
\]

and hence

\[
\boxed{
m_a\ll_\eta Y^{1+\eta}.}
\tag{6.2}
\]

Since `n=Y^2`, this is

\[
\boxed{
m_a\ll_\eta n^{(1+\eta)/2}.}
\tag{6.3}
\]

Combining (5.4) and (6.3): an `epsilon`-near-baseline standard mode has all but at most `epsilon/(2eta)` of its weighted square mass on first actions whose intermediate quotient vertices lie below the power scale

\[
n^{(1+\eta)/2}.
\]

Thus the absence of a strict uniform same-scale gap is compensated by quantitative scale descent.

---

## 7. Structural dichotomy

The centered coefficient lift has the following exact alternative:

1. **bulk mode:** a positive fraction of the mode lies where `V_a` is comparable with `U`; then the tail-potential term gives a strict energy excess over the baseline;
2. **boundary mode:** the energy excess is small; then the mode is concentrated on large action labels and its intermediate states descend from `n` to approximately `sqrt(n)`.

This is the finite coercivity/localization mechanism needed by the dyadic cascade.  The gap need not be uniform at one scale because near-gap modes are forced onto a lower scale.

---

## 8. Formal and exact-computation status

Lean file:

- `EnterpriseMath/Relation/WeightedCoefficientCoercivity.lean`.

It formalizes:

1. the pair-energy moment identity;
2. the exact centered coefficient-lift identity;
3. the positive potential lower bounds;
4. the reciprocal-mode no-go.

Exact checker:

- `scripts/check_free_research_weighted_tail_coercivity.py`.

It verifies with `Fraction`:

1. the moment formula;
2. the centered identity;
3. threshold localization;
4. the uncentered reciprocal kernel.

Lean-green status is not claimed until the branch workflow succeeds.

---

## 9. Updated next theorem

The next target is to combine the bulk/boundary dichotomy with the exact relation-field return lift.

A suitable abstract cascade theorem would show that if the full local residual channel is small and every near-baseline mode descends from `n` to at most `n^theta` with `theta<1`, then repeated relation transport forces normalized relation energy to decay.

The remaining arithmetic input is control of the full local residual channel under that descent; the finite state, positivity, and localization geometry are now explicit.
