# Free Research — Weighted `S_3` Lift–Transpose–Project Mixer

Status: `FREE_RESEARCH_FRONTIER / LOCAL_GLOBAL_CORRECTION / EXACT_RELATION_CONTRACTION_ONE_THIRD / ENERGY_CONTRACTION_ONE_NINTH / WEIGHTED_PRIMITIVE_ADMISSION_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_WEIGHTED_TAIL_COERCIVITY_LOCALIZATION_20260904.md`

## 1. Correction and advance

On one fixed three-label provenance fiber, uniform averaging over the three position transpositions annihilates the local standard representation exactly.  It does **not** follow that the original global action-cloud relation field is annihilated after overlapping fibers are recombined.

The correct global operation is:

1. lift one action label to three independently weighted labels;
2. average the three position transpositions;
3. project back to the first action coordinate.

This induced Markov operator preserves the weighted mean and scales every global standard fluctuation by exactly `1/3`.  Hence it scales the weighted relation field by `1/3` and its quadratic energy by `1/9`.

This is a strict uniform contraction and a more precise realization of the six-history gap.

---

## 2. Product lift and local transposition action

Let `S` be a finite action family with weights `u_a>0`, total mass

\[
U=\sum_a u_a,
\]

and weighted mean

\[
\bar x=U^{-1}\sum_a u_ax_a.
\]

Lift a value channel `x` to the three-label product space by

\[
F(a,b,c):=x_a.
\]

Let

\[
\mathsf M_3
=\frac13(P_{12}+P_{13}+P_{23})
\]

act by position transpositions.  Then

\[
(\mathsf M_3F)(a,b,c)
=\frac{x_a+x_b+x_c}{3}.
\tag{2.1}
\]

On a fixed triple this is the local mean and the fixed-triple standard component vanishes.

---

## WSM-T01 — Global pushback formula

Project back to the first coordinate by averaging the two partner labels with product measure:

\[
(\mathcal K_3x)_a
:=\frac1{U^2}
\sum_{b,c}u_bu_c
(\mathsf M_3F)(a,b,c).
\]

Using (2.1),

\[
\boxed{
(\mathcal K_3x)_a
=\frac{x_a+2\bar x}{3}.
}
\tag{3.1}
\]

Therefore

\[
\boxed{
\mathcal K_3x-\bar x
=\frac13(x-\bar x).
}
\tag{3.2}
\]

The weighted mean is preserved exactly.

---

## WSM-T02 — Relation-field and energy contraction

For capacity-weighted totals

\[
c_a=u_ax_a,
\qquad
C=\sum_ac_a,
\]

the pushback update is

\[
\boxed{
c'_a=\frac13c_a+\frac23u_a\frac CU.}
\tag{4.1}
\]

The second term is a uniform-total channel and has zero internal relation field.  Hence

\[
\boxed{
Z'_{ab}=\frac13Z_{ab}.
}
\tag{4.2}
\]

For the complete weighted pair energy,

\[
\mathcal E_u(x)
=\sum_{a,b}u_au_b(x_a-x_b)^2,
\]

we obtain

\[
\boxed{
\mathcal E_u(\mathcal K_3x)
=\frac19\mathcal E_u(x).
}
\tag{4.3}
\]

Thus the global relation-energy gap is

\[
\boxed{1-1/9=8/9.}
\]

At the linear relation-field level the gap is `2/3`; at the quadratic energy level it is `8/9`.

---

## 5. General factorial degree

For `r>=2`, lift to `S^r`, average all position transpositions, and project the final function back to the first coordinate.  The fixed-fiber standard eigenvalue is

\[
\lambda_r=\frac{r-3}{r-1}.
\]

After product-measure pushback, the induced global operator is

\[
\boxed{
(\mathcal K_rx)_a
=\frac{r-2}{r}x_a+\frac2r\bar x.
}
\tag{5.1}
\]

Hence

\[
\boxed{
\mathcal K_rx-\bar x
=\frac{r-2}{r}(x-\bar x)
}
\tag{5.2}
\]

and

\[
\boxed{
\mathcal E_u(\mathcal K_rx)
=\left(\frac{r-2}{r}\right)^2\mathcal E_u(x).
}
\tag{5.3}
\]

For `r=3`, the factors are `1/3` and `1/9`.

For `r=2`, the pushback sends the first label to an independently sampled partner and therefore projects globally to the mean.  But the fixed two-history operation is only a deterministic swap, with no intrinsic local contraction.  Degree three remains the first provenance degree with an intrinsic convex local transposition average and a fixed-fiber gap before pushback.

---

## 6. State-level implementation

The capacity/total/relation carrier implements the mixer without retaining all triples explicitly.  For any `lambda`, define

\[
c'_a=\lambda c_a+(1-\lambda)u_a\bar x.
\]

Then

\[
Z[c']=\lambda Z[c].
\]

Taking `lambda=1/3` gives the exact `S_3` mixer.

This operation:

- preserves capacities;
- preserves grand total;
- preserves the weighted mean;
- contracts every internal relation coordinate by `1/3`;
- contracts relation energy by `1/9`;
- fixes uniform states.

It is therefore a valid finite Markov update on the accepted weighted relation state.

What remains open is its **primitive status**: current Boolean BRC does not contain convex numerical averaging after recoalescence, so this update must either be admitted explicitly as a weighted relation-state primitive or derived from a pre-recoalescence randomized/ensemble branch semantics.

---

## 7. Interaction with the moving-cutoff cascade

The tail-augmented state has several scalar channels:

\[
x,\quad V,\quad Vx,\quad E,\quad R.
\]

The same lift–transpose–project operator acts on each channel and contracts every corresponding internal relation field by `1/3`.  Therefore the coefficient-mismatch channel does not require a separate spectral analysis once the weighted mixer is admitted.

The half-scale endpoint channel remains as genuine interscale forcing.  The same-scale standard sector has a strict finite contraction.

This sharpens the cascade architecture to:

\[
\boxed{
\text{same-scale relation energy}
\xrightarrow{\mathcal K_3}
\frac19\text{ same-scale energy}
\quad+\quad
\text{half-scale endpoint forcing}.
}
\]

The remaining mathematical task is to show that the arithmetic return dynamics actually applies or simulates `K_3` with controlled positive frequency and to sum the resulting half-scale forcing.

---

## 8. Formal and exact-computation status

Lean file:

- `EnterpriseMath/Relation/WeightedRelationMixer.lean`.

It formalizes:

1. common-mean mixing of values and totals;
2. exact scaling of relation fields;
3. exact quadratic scaling of pair energy;
4. weighted-mean preservation;
5. the `1/3` and `1/9` `S_3` specializations.

Exact checker:

- `scripts/check_free_research_weighted_s3_lift_project.py`.

It verifies with `Fraction`:

1. the product-lift/transposition/pushback formula;
2. mean preservation;
3. relation scaling;
4. energy contraction;
5. the general degree-`r` formula;
6. the distinction between local fixed-fiber annihilation and global pushback contraction;
7. the capacity-weighted total update.

Lean-green status is not claimed until the branch workflow succeeds.

---

## 9. Updated boundary

Closed:

- exact local `S_3` standard projection;
- correct global lift–transpose–project operator;
- strict weighted relation-field contraction `1/3`;
- strict relation-energy contraction `1/9`;
- state-level capacity/total implementation.

Open:

- deriving this convex update from current primitive deterministic operations;
- proving that arithmetic branch dynamics samples the three transpositions with the required invariant product weights;
- bounding half-scale forcing in the moving-cutoff cascade;
- quantitative native prime remainder.

---

## 10. Next theorem

Construct a finite weighted branch semantics in which:

1. the three ordered position transpositions are exact measure-preserving branch maps;
2. their uniform Markov average descends to the capacity/total update (4.1);
3. support denotation remains unchanged;
4. the relation field contracts by `1/3` before exact support recoalescence.

This would promote the current algebraic mixer from an admissible state update to an explicitly generated Enterprise branch operation.
