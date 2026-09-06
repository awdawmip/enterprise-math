# Free Research — Deep Full-Intermediate Variance Closure

Status: `FREE_RESEARCH_FRONTIER / FULL_INTERMEDIATE_KERNEL_CLOSED / HISTORY_BUNDLE_CURVATURE_IDENTITY / VECTOR_ANOVA_CLOSED / HISTORY_MEAN_NO_GO / NATIVE_QUANTITATIVE_REMAINDER_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_DEEPEST_COLORED_TRANSFER_20260904.md`

## 1. Problem resolved in this checkpoint

The previous deepest-chamber analysis showed that the scalar lower endpoint

\[
m=\left\lfloor\frac{Y^3}{abc}\right\rfloor<Y
\]

and the unique uncut-position color `j in Fin 3` are not sufficient for all transported readouts.  Even adding the uncut intermediate vertex does not recover the other two one-step branches.

This checkpoint identifies the complete finite carrier, proves the exact variance identities on it, and isolates the only remaining dynamical channel.  The result is partly a closure and partly a no-go:

- the missing conditional variance is no longer an unidentified boundary term;
- it is an exact positive relation/curvature energy on the complete history bundle;
- it splits orthogonally into an `S_3` standard channel and a common history-mean channel;
- the common history-mean channel cannot be controlled by the internal standard curvature alone.

Accordingly, any native quantitative remainder theorem must estimate the history-mean relation field in addition to the already available standard curvature field.

---

## 2. Full deepest-history kernel

At scale `n=Y^3`, let

\[
\mathcal D_Y
=\{(a,b,c):abc\le Y^3,\text{ exactly one of }a,b,c\le Y\}.
\]

For `h=(a,b,c) in D_Y`, write

\[
j(h)=\text{the unique uncut position},
\]

\[
\mathbf v(h)
=\left(
\left\lfloor\frac n a\right\rfloor,
\left\lfloor\frac n b\right\rfloor,
\left\lfloor\frac n c\right\rfloor
\right),
\]

and

\[
m(h)=\left\lfloor\frac n{abc}\right\rfloor<Y.
\]

With prime-winding action weights

\[
u_q=\frac{\Lambda(q)}q,
\qquad
w_h=u_au_bu_c,
\]

the complete descended kernel is

\[
\boxed{
\widetilde\kappa_Y(j,v_1,v_2,v_3,m)
=
\sum_{\substack{h\in\mathcal D_Y\\
(j(h),\mathbf v(h),m(h))=(j,(v_1,v_2,v_3),m)}}
w_h.
}
\tag{2.1}
\]

The previously constructed colored endpoint kernel is its forgetful pushforward:

\[
\kappa_Y(j,m)
=
\sum_{v_1,v_2,v_3}
\widetilde\kappa_Y(j,v_1,v_2,v_3,m).
\tag{2.2}
\]

The complete state may equivalently retain the ordered action triple `(a,b,c)`.  The intermediate-vector representation is the minimal readout-oriented form needed below.

---

## 3. Exact recoverability boundary

The following hierarchy is now strict.

### Scalar endpoint is insufficient

Different colors may share the same `m`; therefore `m` cannot recover the standard color representation.

### Color plus endpoint is insufficient

At `Y=10`, the deepest histories

\[
(2,17,19),
\qquad
(3,11,17)
\]

have the same color and final endpoint `m=1`, but their distinguished uncut intermediates are

\[
500,
\qquad
333.
\]

### Color, uncut intermediate and endpoint are still insufficient

The histories

\[
(2,17,19),
\qquad
(2,13,23)
\]

have the same color, the same uncut intermediate `500`, and the same final endpoint `1`, while another one-step branch is respectively

\[
58,
\qquad
76.
\]

Thus no decoder from the reduced key can recover arbitrary field readouts of all three branches.

### Complete key is sufficient

The key

\[
\boxed{
(j,v_1,v_2,v_3,m)
}
\tag{3.1}
\]

trivially recovers every observable declared as a function of these data.  In the current exact BRC semantics this is the first convenient sufficient state after the successive no-resurrection obstructions above.

---

## 4. Internal standard energy is ordered cubic curvature

For a scalar field `f` on quotient vertices, define the three retained branch values

\[
X_h
=\bigl(f(v_1(h)),f(v_2(h)),f(v_3(h))\bigr).
\]

Its internal `S_3` standard energy is

\[
e_{\mathrm{std}}(h)
=
|X_{h,1}-X_{h,2}|^2
+|X_{h,2}-X_{h,3}|^2
+|X_{h,3}-X_{h,1}|^2.
\tag{4.1}
\]

Recall the ordered common-suffix curvature

\[
\Omega_{a,b\mid c}(n)
=
\delta_{bc}f(q_a(n))-\delta_{ac}f(q_b(n))
=f(q_a(n))-f(q_b(n)).
\]

Consequently,

\[
\boxed{
 e_{\mathrm{std}}(a,b,c)
=
|\Omega_{a,b\mid c}|^2
+|\Omega_{b,c\mid a}|^2
+|\Omega_{c,a\mid b}|^2.
}
\tag{4.2}
\]

This is pointwise and finite.  No asymptotic estimate or scalar product-label collapse is used.

After summing over the permutation-invariant deepest chamber, its three cyclic orientations have equal mass.  Therefore the deepest internal standard packet is exactly three copies of one oriented restricted curvature channel.  Since all weights are nonnegative, each oriented deepest channel is a positive restriction of the full product-bounded degree-three ordered curvature energy.

---

## 5. Cross-history conditional variance is also curvature-valued

Fix a coarse fiber

\[
F_{j,m}
=\{h\in\mathcal D_Y:j(h)=j,\ m(h)=m\}
\]

with total mass

\[
W_{j,m}=\sum_{h\in F_{j,m}}w_h.
\]

For one retained branch position `r`, define

\[
\bar X_{j,m,r}
=
\frac1{W_{j,m}}
\sum_{h\in F_{j,m}}w_hX_{h,r}.
\]

Then the exact weighted pair identity gives

\[
\boxed{
\sum_{h\in F_{j,m}}w_h
|X_{h,r}-\bar X_{j,m,r}|^2
=
\frac1{2W_{j,m}}
\sum_{h,h'\in F_{j,m}}
w_hw_{h'}|X_{h,r}-X_{h',r}|^2.
}
\tag{5.1}
\]

Every difference on the right is itself an ordered curvature observable:

\[
X_{h,r}-X_{h',r}
=
\Omega_{\alpha_r(h),\alpha_r(h')\mid1}(n).
\tag{5.2}
\]

Thus the conditional variance erased by the endpoint projection is exactly a positive complete-graph relation field on the retained history bundle.  Its coefficients are products of cubic-history masses, so this cross-history packet is a higher coefficient lift of the same curvature observable; it must not be confused with the single-history degree-three scalar coefficient.

This distinction corrects the informal phrase “the missing variance is just the old cubic energy”.  The observable type is the same ordered curvature, while the induced coefficient measure is the pair measure on full histories.

---

## 6. Exact two-channel vector ANOVA

For two complete histories `h,h'`, let

\[
\mu_h=\frac{X_{h,1}+X_{h,2}+X_{h,3}}3
\]

and

\[
X_h^0=X_h-\mu_h(1,1,1).
\]

Then

\[
\boxed{
\|X_h-X_{h'}\|_2^2
=
3|\mu_h-\mu_{h'}|^2
+
\|X_h^0-X_{h'}^0\|_2^2.
}
\tag{6.1}
\]

Summing (6.1) against any nonnegative history-pair measure gives the exact finite ANOVA

\[
\boxed{
\mathcal V_{\mathrm{full}}
=
\mathcal V_{\mathrm{mean}}
+
\mathcal V_{\mathrm{std}}.
}
\tag{6.2}
\]

Here the normalization is chosen so that `V_mean` already includes the factor `3`.  The first channel is motion along the trivial `S_3` line; the second is motion in the two-dimensional standard representation.

The internal standard energy (4.1) controls the uncentered size of `X_h^0`, hence the standard cross-history variance is bounded by the corresponding internal standard second moment.  The common history-mean channel is independent of this control.

---

## 7. Arithmetic no-go for standard-energy-only control

At `Y=10`, consider the two deepest histories

\[
h=(2,13,13),
\qquad
h'=(3,11,11).
\]

They have the same color and final endpoint:

\[
m(h)=m(h')=2.
\]

Their intermediate vectors are

\[
\mathbf v(h)=(500,76,76),
\qquad
\mathbf v(h')=(333,90,90).
\]

Choose a field equal to `1` on `{500,76}` and `0` on the second vector.  Then

\[
X_h=(1,1,1),
\qquad
X_{h'}=(0,0,0).
\]

Therefore

\[
e_{\mathrm{std}}(h)=e_{\mathrm{std}}(h')=0,
\]

but

\[
\mu_h=1,
\qquad
\mu_{h'}=0,
\qquad
\|X_h-X_{h'}\|^2=3.
\]

It follows that there is no universal constant `C` such that, for every field,

\[
|\mu_h-\mu_{h'}|^2
\le
C\bigl(e_{\mathrm{std}}(h)+e_{\mathrm{std}}(h')\bigr).
\tag{7.1}
\]

This is not a weakness of the proof technique.  It is an exact arithmetic counterexample to every proposed cascade that keeps only internal `S_3` standard curvature and discards the history-mean relation field.

---

## 8. Corrected renormalization state

The deepest descended state must carry two orthogonal relation channels:

\[
\boxed{
\text{Deep relation state}
=
\text{history-mean relation field}
\oplus
\text{standard intermediate relation field}.
}
\tag{8.1}
\]

Equivalently, retaining the complete vector `(v_1,v_2,v_3)` carries both channels without choosing a basis.

The `S_3` history mixer contracts the standard channel by amplitude `1/3` and energy `1/9`.  It fixes the trivial history-mean line.  Therefore a complete cube-root cascade has the block form

\[
\boxed{
\begin{pmatrix}
\mathcal E_{\rm mean}'\\
\mathcal E_{\rm std}'
\end{pmatrix}
\preccurlyeq
\begin{pmatrix}
1&0\\
0&1/9
\end{pmatrix}
\begin{pmatrix}
\mathcal E_{\rm mean}\\
\mathcal E_{\rm std}
\end{pmatrix}
+
\text{lower-scale forcing}.
}
\tag{8.2}
\]

The previously solved scalar recurrence with coefficient `1/9` applies only after the mean channel has been separately controlled.  Treating the entire vector energy as if it inherited the `1/9` factor would be false by Section 7.

---

## 9. Formal and exact-computation state

Lean files:

- `EnterpriseMath/Relation/DeepChamberIntermediateNoGo.lean`;
- `EnterpriseMath/Relation/DeepChamberFullIntermediateVariance.lean`;
- `EnterpriseMath/Relation/DeepChamberHistoryMean.lean`;
- `EnterpriseMath/Relation/DeepChamberVectorANOVA.lean`.

They formalize:

1. strict failure of the colored endpoint and reduced uncut key;
2. sufficiency of the complete intermediate key for declared readouts;
3. pointwise identity between internal standard energy and cyclic ordered curvature;
4. exact realization of every selected cross-history branch variance as common-suffix curvature;
5. nonnegativity of the complete history variance;
6. exact trivial/standard vector decomposition;
7. the arithmetic no-go for controlling history means by internal standard energy.

Exact checkers:

- `scripts/check_free_research_deep_full_intermediate_variance.py`;
- `scripts/check_free_research_deep_history_mean.py`.

They verify with integers and `Fraction`:

- complete signatures and lower final endpoints;
- pointwise and aggregate curvature identities;
- fiberwise weighted laws of total variance;
- equality of cyclic deepest orientations;
- positive embedding of the deepest oriented packet in the product-bounded full packet;
- the explicit projection collisions;
- exact vector ANOVA and the history-mean counterexample.

Workflow success is reported separately and is not assumed by this note.

---

## 10. Updated boundary

Closed:

1. complete finite deepest-history kernel;
2. exact recoverability/no-resurrection hierarchy;
3. internal standard-energy/ordered-curvature identity;
4. cross-history conditional variance as an induced relation field;
5. exact trivial/standard vector ANOVA;
6. arithmetic no-go for standard-only control;
7. correct two-channel renormalization typing.

Open:

1. an arithmetic estimate for the history-mean relation energy;
2. coupling of that mean channel to the signless return residual or to a higher positive provenance packet;
3. a strict contraction or summable forcing estimate for the full two-channel cascade;
4. a native quantitative remainder for `psi(x)-x`;
5. any Riemann-hypothesis-scale conclusion.

---

## 11. Next discriminating theorem

Let

\[
\mu_h(f;n)
=
\frac13\sum_{r=1}^{3} f(q_{\alpha_r(h)}(n)).
\]

The next theorem must estimate the weighted relation field

\[
\boxed{
\mathcal M_Y(f;n)
=
\sum_{F_{j,m}}
\frac{3}{2W_{j,m}}
\sum_{h,h'\in F_{j,m}}
w_hw_{h'}
|\mu_h(f;n)-\mu_{h'}(f;n)|^2.
}
\tag{11.1}
\]

The target is not to bound it by internal standard curvature, which Section 7 disproves.  The valid possibilities are:

- derive `M_Y` from differences of signless return residuals on the three retained intermediate vertices;
- identify it as the positive part of a higher ordered provenance packet;
- or exhibit another scale-lowering no-go and enlarge the state once more.

This is now the unique unresolved finite-energy channel in the deepest cube-root descent.
