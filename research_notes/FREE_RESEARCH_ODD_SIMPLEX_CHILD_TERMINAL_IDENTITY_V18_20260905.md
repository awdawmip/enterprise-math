# Free Research — Odd-Simplex Child-Terminal Identity

Status: `FREE_RESEARCH_FRONTIER / EXACT CONDITIONAL ANOVA IDENTITY / TERMINAL RECONSTRUCTION BRIDGE / RESIDUAL-FREE HALF DESCENT / ARITHMETIC BLOCK ASSEMBLY OPEN / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_TWO_STEP_ODD_SIMPLEX_HYPOCOERCIVITY_V18_20260905.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260905`
Research-Mode: `FREE_AXIOM_DISCOVERY`

## 1. Purpose

The V18 two-step mechanism retains two channels through a block and reconstructs a canonical odd-simplex energy only at the block boundary.  This note supplies an exact finite bridge for that terminal reconstruction.

Let `x` be the parent value, `Y` the first quotient value, and `Z` the second quotient value.  Condition on the first history and write

\[
z:=\mathbb E[Z\mid Y],
\qquad
v:=\operatorname{Var}(Z\mid Y),
\qquad
e:=Y+z.
\]

The conditional odd-triangle energy is

\[
\mathcal J(x,Y;Z)
:=(x+Y)^2+\mathbb E[(x+Z)^2\mid Y]
+\mathbb E[(Y+Z)^2\mid Y].
\]

The main identity is

\[
\boxed{
\mathcal J(x,Y;Z)
=2x^2+2(Y^2+v)+2e(e+x-Y).
}
\tag{1.1}
\]

Thus the odd simplex is exactly the sum of:

1. twice the parent root energy;
2. twice the child terminal energy `Y^2+Var(Z|Y)`;
3. one explicit scalar-residual correction.

No asymptotic argument or inequality is used in (1.1).

---

## 2. Direct algebra

By conditional variance,

\[
\mathbb E[(x+Z)^2\mid Y]=(x+z)^2+v,
\]

and

\[
\mathbb E[(Y+Z)^2\mid Y]=(Y+z)^2+v.
\]

Therefore

\[
\begin{aligned}
\mathcal J
&=(x+Y)^2+(x+z)^2+(Y+z)^2+2v\\
&=2x^2+2Y^2+2v+2(Y+z)(x+z).
\end{aligned}
\]

Since

\[
Y+z=e,
\qquad
x+z=e+x-Y,
\]

we obtain (1.1).

---

## OCT-T01 — Residual-free exact descent

If the conditional signless residual vanishes,

\[
e=Y+z=0,
\]

then

\[
\boxed{
\mathcal J(x,Y;Z)=2x^2+2(Y^2+v).
}
\tag{3.1}
\]

Consequently,

\[
\boxed{
Y^2+\operatorname{Var}(Z\mid Y)
=\frac12\mathcal J-x^2
\le\frac12\mathcal J.
}
\tag{3.2}
\]

The child terminal two-channel energy is therefore a positive half-subenergy of the parent odd simplex whenever the local signless return is exact.

This is the missing type conversion at a delayed block boundary: it does not reconstruct the root after every microstep, and hence does not invoke the one-step recanonicalization no-go.

---

## 3. Residual correction

For nonzero residual,

\[
\mathcal R:=2e(e+x-Y).
\]

For every `eta>0`, Young's inequality gives

\[
\begin{aligned}
|\mathcal R|
&\le2e^2+2|e||x-Y|\\
&\le(2+\eta^{-1})e^2+\eta(x-Y)^2.
\end{aligned}
\tag{4.1}
\]

Hence

\[
\boxed{
Y^2+v
\le
\frac12\mathcal J
+\frac{2+\eta^{-1}}2e^2
+\frac\eta2(x-Y)^2.
}
\tag{4.2}
\]

There are two possible uses.

1. **Fixed small `eta`.**  Absorb the last term into the already retained ordered relation/one-edge sector, while `e^2` is controlled by the uniformly bounded full residual.
2. **Scale-dependent `eta`.**  Choose `eta` to balance the residual square against the available strict two-step margin.

The formula keeps every correction positive and typed.  It avoids estimating the child energy by a scalar absolute-value supremum.

---

## 4. Weighted finite form

Let the first histories carry a finite probability measure `p(a)`.  For each first label `a`, let the second histories carry a conditional probability `p(b|a)`.  Put

\[
x=f(N),
\qquad
Y_a=f(q_a(N)),
\qquad
Z_{a,b}=f(q_b(q_a(N))).
\]

Define

\[
z_a=\mathbb E_bZ_{a,b},
\qquad
v_a=\operatorname{Var}_b(Z_{a,b}),
\qquad
e_a=Y_a+z_a.
\]

Averaging (1.1) gives

\[
\boxed{
\begin{aligned}
\mathbb E_{a,b}[&(x+Y_a)^2+(x+Z_{a,b})^2+(Y_a+Z_{a,b})^2]\\
={}&2x^2+2\mathbb E_a(Y_a^2+v_a)
+2\mathbb E_a[e_a(e_a+x-Y_a)].
\end{aligned}}
\tag{5.1}
\]

This is valid for arbitrary finite, adaptive second-step kernels.  The quotient action set may change with `a`; only the conditional expectation is used.

For prime-winding actions, `e_a` is the normalized adaptive signless residual at `q_a(N)`.  The V14/V17 residual estimates therefore enter exactly in the final term of (5.1), while the middle term is precisely the child root-plus-standard terminal state required by the V18 delayed block.

---

## 5. Relation to two-step hypocoercivity

The local two-step defect from the parent note is

\[
4(1-s_2)s_1(1-s_1)R
+(1-s_1s_2)\gamma^{-1}V.
\]

Equation (5.1) supplies the complementary terminal statement:

- the stopped/core split and `S_3` mixer propagate `(R,V)` without root reconstruction;
- after the prescribed number of levels, the odd-simplex frame measures the complete terminal state;
- the only mismatch is the explicitly displayed residual correction.

The key design rule is therefore

\[
\boxed{
\text{propagate by the two-channel matrix internally; reconstruct by (5.1) only at block endpoints.}
}
\]

This is compatible with the V18 no-go because no inverse mixer factor is paid between successive microsteps.

---

## 6. What this closes and what remains

Closed:

1. exact terminal conversion from an odd triangle to child root plus conditional variance;
2. residual-free child coefficient `1/2`;
3. a positive Young-inequality residual package;
4. validity for adaptive finite second-step kernels;
5. compatibility with delayed, rather than per-step, recanonicalization.

Open:

1. identify the exact repository normalization of the child `V` channel with the conditional variance `v_a` in (5.1);
2. show that the direct composite chord and transported chord in the canonical `mathfrak E_N` supply the three terms on the left with no multiplicity loss;
3. absorb the `eta(x-Y)^2` correction using the existing `U E_1` sector without exhausting the two-step spectral margin;
4. prove a complete two-level arithmetic block recurrence;
5. promote any logarithmic prime remainder.

The terminal side of the delayed block is now an exact identity rather than an unspecified comparison theorem.
