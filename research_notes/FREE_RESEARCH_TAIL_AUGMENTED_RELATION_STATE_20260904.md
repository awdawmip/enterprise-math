# Free Research — Tail-Augmented Relation State

Status: `FREE_RESEARCH_FRONTIER / COEFFICIENT_MISMATCH_LINEARIZED / MULTICHANNEL_S3_PROJECTION / HALF_SCALE_FORCING / COERCIVE_NORM_ESTIMATE_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_MOVING_CUTOFF_TAIL_RENORMALIZATION_20260904.md`

## 1. Executive advance

The moving-cutoff tail contains a same-scale coefficient term

\[
V_Y(a)f(m_a),
\qquad
m_a=\left\lfloor\frac{Y^2}{a}\right\rfloor.
\]

Expanding pairwise by averages produces the awkward expression

\[
\frac{V_a-V_b}{2}(x_a+x_b).
\]

That expression need not be estimated as a nonlinear error.  Introduce the scalar product channel

\[
\boxed{w_a:=V_Y(a)x_a.}
\]

Then the complete coefficient mismatch is simply another ordinary weighted relation field

\[
\boxed{Z^w_{ab}=u_au_b(w_a-w_b).}
\]

The tail equation therefore remains linear after a finite multichannel state augmentation.

---

## 2. Linear relation-field calculus

For capacities `m_i` and any total channels `c_i,d_i`,

\[
Z[c+d]=Z[c]+Z[d],
\]

\[
Z[c-d]=Z[c]-Z[d],
\]

and

\[
Z[sc]=sZ[c].
\]

For a scalar value channel `h_i`, use block totals

\[
c_i=m_ih_i.
\]

Then

\[
\boxed{
Z[h]_{ij}=m_im_j(h_i-h_j).
}
\tag{2.1}
\]

These linearity laws are now formalized in the accepted weighted relation-field carrier.

---

## 3. Exact augmented tail channels

At `n=Y^2`, let

\[
x_a=f(m_a),
\]

\[
R_a:=\rho_{m_a}(f;m_a),
\]

\[
V_a:=A(m_a)-A(Y),
\]

and

\[
E_a:=\sum_{Y<c\le m_a}u_cf(q_c(m_a)).
\]

The truncated residual is exactly

\[
\boxed{
\rho_Y(f;m_a)=R_a-V_ax_a-E_a.
}
\tag{3.1}
\]

Define four value channels on the first-action cloud:

\[
x=(x_a),
\qquad
R=(R_a),
\qquad
w=(V_ax_a),
\qquad
E=(E_a).
\]

By linearity,

\[
\boxed{
Z^{\rho_Y}=Z^R-Z^w-Z^E.
}
\tag{3.2}
\]

Thus the exact relation-field return equation becomes

\[
\boxed{
UZ^x+\sum_{c\le Y}u_cZ^x(q_c(n))
=Z^R-Z^w-Z^E.
}
\tag{3.3}
\]

No pair-dependent nonlinear remainder remains.

---

## 4. Half-scale endpoint channel

Every state contributing to `E_a` satisfies

\[
q_c(m_a)\le\left\lfloor\frac{Y-1}{a}\right\rfloor
\le\left\lfloor\frac{Y-1}{2}\right\rfloor.
\]

Therefore the entire channel `E` is assembled from values of `f` below the common half-scale threshold.

The only same-scale auxiliary channel is

\[
w_a=V_ax_a.
\]

This isolates the renormalization problem sharply:

\[
\boxed{
\text{current relation field }Z^x
\longleftrightarrow
\text{coefficient-weighted field }Z^w
\quad+\quad
\text{half-scale field }Z^E.
}
\]

---

## 5. Componentwise `S_3` projection

The transposition mixer acts only on first-history labels and is linear in the readout channel.  Consequently it applies simultaneously to

\[
x,\quad R,\quad V,\quad w=Vx,\quad E.
\]

For any three first labels `a,b,c`, uniform transposition averaging sends each channel to its three-point mean.  Hence every internal relation field of every channel is annihilated:

\[
\boxed{
\mathsf M_3Z^x
=\mathsf M_3Z^R
=\mathsf M_3Z^w
=\mathsf M_3Z^E
=0.
}
\tag{5.1}
\]

The gap remains exactly `1`; adjoining the coefficient product channel does not weaken it.

This answers the V11 state-extension question positively at finite algebraic strength.  The required augmentation is the product channel `w=Vx`, not merely the coefficient field `V` by itself.

---

## 6. Minimal augmented state

The moving-cutoff step can be represented by the finite state

\[
\boxed{
(m_a,\;x_a,\;V_a,\;w_a=V_ax_a,\;E_a,\;R_a,
\;Z^x,Z^w,Z^E,Z^R).
}
\]

Because relation fields are recoverable from capacities, totals and row sums, this state remains within the accepted capacity/total/relation architecture.  It is a multichannel specialization of T8, not a new tool family.

The state retains exactly what Boolean support erases and no infinite analytic object.

---

## 7. What the augmentation does and does not solve

It solves:

1. the apparent nonlinear coefficient mismatch;
2. compatibility of the coefficient channel with the same `S_3` gap-one projector;
3. separation of all remaining endpoint forcing into a strict half-scale region;
4. a completely linear relation-field return system.

It does not yet prove:

1. that the weighted mixer is an allowed primitive operation;
2. a norm estimate comparing `Z^w` to `Z^x` after centering;
3. decay of the half-scale cascade;
4. a quantitative prime-number-theorem remainder.

The next obstruction is now a finite block-norm question rather than a state-representation question.

---

## 8. Exact and formal status

Lean strengthening:

- `EnterpriseMath/Relation/WeightedQuotientRelationField.lean` now proves relation-field linearity and the weighted-value-channel identity.

Exact checker:

- `scripts/check_free_research_tail_augmented_relation.py`.

It verifies:

1. `rho_Y=R-w-E` for every finite test state;
2. the lifted return equation;
3. `Z^{rho_Y}=Z^R-Z^w-Z^E`;
4. half-scale support of `E`;
5. componentwise `S_3` projection for all augmented channels.

All structural checks use integers and `Fraction`.

---

## 9. Next discriminating theorem

The remaining finite estimate is a coercive bound for the two same-scale channels:

\[
\boxed{
\|Z^x\|^2
\le \alpha\,\|UZ^x+\mathcal T Z^x+Z^w\|^2
+C\,\|Z^R-Z^E\|^2,
}
\]

with a cutoff-uniform `alpha`, or an equivalent block singular-value bound after the `S_3` standard projection.

Since `E` is half-scale and `R` is the full local residual channel, such a bound would close the structural part of the dyadic cascade.  Only arithmetic estimates for the full residual and iteration of the half-scale forcing would remain.
