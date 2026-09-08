# #1162 — no-go for a naive positive roughness defect beyond the Basel inverse trace

Status: RESEARCH_NOTE / EXACT FINITE COUNTEREXAMPLE / NOT_PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-higher-m-positive-defect-nogo-20260908-b62d
Date: 2026-09-08

## 1. Question

The Basel/m=1 weighted-cycle readout has the exact form

`beta_1(rough)=beta_1(uniform)-D`, `D>=0`.

Does the same one-sided positive-defect picture extend to higher normalized inverse moments

`beta_m=2^(2m-1) Tr[(L^+)^m]/(N S)^m`?

The answer is no, already for a four-cycle and an arbitrarily small finite roughness perturbation.

## 2. Exact alternating C4 family

Fix total resistance S=1 and take the positive edge resistances

`g(t)=(1/4+t, 1/4-t, 1/4+t, 1/4-t)`,

with `|t|<1/4`.

Let `L(t)` be the corresponding weighted cycle Laplacian with conductances `1/g_i(t)`.

Direct finite characteristic-polynomial algebra gives

`det(lambda I-L(t))
 = lambda (4lambda t-lambda+8)(4lambda t+lambda-8)
   (16lambda t^2-lambda+16)/[(4t-1)^2(4t+1)^2]`.

No derivative in t is used to establish the formulas below; they are exact rational functions/polynomials in t.

## 3. m=1 versus m=2

For the scale-free first inverse moment,

`beta_1(t)=2 Tr(L(t)^+)/4 = (5-16t^2)/32
          =5/32 - t^2/2`.

Thus any nonzero alternating roughness lowers the Basel inverse-trace readout, consistent with the exact nonnegative defect theorem.

But the second inverse moment is

`beta_2(t)=8 Tr[(L(t)^+)^2]/16
          =(16t^2+3)^2/512`

or

`beta_2(t)=9/512 + 3t^2/16 + t^4/2`.

Hence for every `0<|t|<1/4`,

`beta_2(t)>beta_2(0)`.

The uniform cycle is therefore not a global upper envelope for the second inverse moment; in this direction it is a strict local minimum.

For completeness the third normalized inverse moment is

`beta_3(t)=17/8192 + 45t^2/512 + 3t^4/32 - t^6/2`,

so its leading roughness response is also upward.

## 4. Consequence

There cannot be a universal extension of the Basel formula of the form

`beta_m(rough)=beta_m(uniform)-D_m(rough)`

with one nonnegative defect `D_m>=0` for every positive weighted cycle when `m>=2`, because the explicit `C4` family already violates the required sign at `m=2`.

Thus the positive repair coordinate `D` from the Basel inverse trace is genuinely order-specific. Higher inverse moments require signed and/or higher-moment repair information.

This also blocks an invalid BRC shortcut: positivity proved for the m=1 roughness carrier must not be propagated to the m=2 or m=3 observers merely because they use the same underlying weighted cycle.

## 5. Why m=1 is structurally special

At m=1 the trace of the pseudoinverse is proportional to the Kirchhoff index, hence to a sum of pairwise effective resistances. On a cycle each pair resistance is the quadratic concave function `s(1-s)` of an arc-resistance fraction s. That exact quadratic concavity produced the sum-of-squares defect.

For `Tr[(L^+)^m]`, m>=2, this pairwise effective-resistance linearization is absent. The explicit C4 counterexample shows that no sign-preserving inheritance should be assumed.

## 6. BRC typing

REUSE_APPLIED: observer typing. The m=1 positive roughness repair coordinate is valid only for the declared m=1 output. Changing the future observer to higher inverse moments invalidates that collapse. The C4 family is an exact information-loss witness.

No positive weighted BRC compression is applied to the higher-m correction before its sign structure is resolved.

## 7. Next

1. Seek a finite signed/tensor roughness carrier for m=2 under equal subdivision.
2. Determine whether rooted-forest coefficients provide a natural finite hierarchy of repair coordinates for higher moments.
3. Preserve the m=1 positive defect as a special Basel theorem rather than a generic inverse-spectrum principle.
