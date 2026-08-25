# Diagonal Gauge Refoundation — Phase C endpoint forgetful groupoid

Status: `RAW REFOUNDATION CANDIDATE / EXACT DERIVED STRUCTURE`
Date: `2026-08-25`
Researcher-ID: `EM-DGR-8C2D41`
Owner branch: `research/diagonal-gauge-refoundation`

Primary disposition:

`DERIVED_DISPLACEMENT_ACTION_GROUPOID_CLASSIFIED__COMPOSITION_SAFE_ENDPOINT_FORGETFUL_MAP_ESTABLISHED__TRACE_AND_BRC_REMAIN_STRICTLY_RICHER`

## 1. Why bare displacement is insufficient

The frozen translated native line identity is

`T_{P;a,b}^{(ij)}=(P,[X_i^aX_j^b])`.

The start `P` is required to distinguish parallel translated segments.

Therefore the bare diagonal gauge element `g in G_D` cannot be the full endpoint object globally: the same displacement occurs at many placements.

The correct derived coordinate-endpoint object is an **action groupoid / displacement arrow** retaining start placement.

---

## 2. Derived displacement action groupoid

Let `V_E` denote the current integer-addressed coordinate vertices at the derived translation/carrier layer, and let `G_D` be the Phase-A diagonal displacement group.

Current Stage 2 already supplies a translation-covariant integer difference `delta_I(P,Q) in Z^2`; Phase A identifies this exactly with `G_D ~= Z^2`.

Define an arrow

`(P,g): P -> P·g`.

Composition is

`(P,g) ; (P·g,h) = (P,g+h)`.

Identity is

`(P,0)`.

Inverse is

`(P,g)^(-1)=(P·g,-g)`.

### Theorem DG-C1 — derived action groupoid

At the current translated integer-vertex layer, these arrows form a groupoid isomorphic to the ordinary endpoint-pair translation groupoid encoded by Stage-2 carrier differences.

Freeze candidate:

`DERIVED_ENDPOINT_DISPLACEMENT_OBJECT = START_TYPED_DIAGONAL_GAUGE_ARROW`.

The algebraic rank of `G_D` is not promoted to a native-dimension claim.

---

## 3. Forgetful map from paths

For any native path witness `p` from `P` to `Q`, define

`F_D(p)=(P,delta_D(P,Q))`.

This forgets the internal path history and keeps only start plus endpoint displacement.

### Theorem DG-C2 — composition safety

For composable paths `p:P->Q` and `q:Q->R`,

`F_D(p;q)=F_D(p);F_D(q)`.

Reason: Stage-2 displacement differences telescope in the `Z^2` chart, and Phase A transports that addition exactly to `G_D`.

Hence endpoint displacement is an operation-safe quotient for **path concatenation**.

Freeze candidate:

`PATH_TO_DERIVED_DISPLACEMENT_ARROW = CONCATENATION_HOMOMORPHIC_FORGETFUL_MAP`.

It is deliberately non-injective.

---

## 4. Non-injectivity is required, not a defect

Examples already frozen/current:

1. `X_iX_j` and `X_jX_i` are distinct path witnesses with the same displacement arrow;
2. the reverse-third carrier shortcut reaches the same endpoint displacement as `T_{1,1}^{(ij)}` but is not the same native line;
3. Phase-B length-3 closed loops have zero displacement arrow but nonzero path count.

Therefore

`SAME_DISPLACEMENT_ARROW != SAME_PATH`.

Also

`SAME_DISPLACEMENT_ARROW != SAME_NATIVE_LINE_TRACE`.

This is exactly the intended semantic strength of the quotient.

---

## 5. Forgetful map from native traces

For a translated trace define

`End_D(T_{P;a,b}^{(ij)})=(P,a g_i+b g_j)`.

### Theorem DG-C3 — trace composition descends

Because current native trace composition is component addition,

`T_{a,b}^{(ij)} * T_{c,d}^{(ij)}=T_{a+c,b+d}^{(ij)}`,

we have

`End_D(T_1*T_2)=End_D(T_1);End_D(T_2)`

whenever placement typing makes the traces composable.

Thus the diagonal displacement arrow is also an operation-safe quotient of the trace composition law.

But it is coarser than trace identity, since different component traces/carrier shortcuts may share the same endpoint arrow.

Freeze candidate:

`TRACE_TO_DISPLACEMENT_ARROW = COMPOSITION_SAFE_BUT_NOT_LINE_CLASSIFYING`.

---

## 6. Current trace inverse versus canonical reverse

Current Stage 3 distinguishes:

- `T(P->Q)^(-1)`: groupoid inverse traversal of the same trace/path fiber;
- `T(Q->P)`: independently decoded canonical positive-axis reverse trace.

They are not equal as trace objects for nonzero segments.

Let `g=delta_D(P,Q)`.

### Theorem DG-C4 — endpoint coequalization of the two reversals

Both objects map under `End_D` to the same displacement arrow

`(Q,-g)`.

Therefore

`End_D(T(P->Q)^(-1)) = End_D(T(Q->P))`

while

`T(P->Q)^(-1) != T(Q->P)` upstream.

This precisely identifies what information is lost by the diagonal endpoint quotient.

Freeze candidate:

`ENDPOINT_DISPLACEMENT_FORGETS_TRACE_REVERSE_VS_CANONICAL_REVERSE_DISTINCTION`.

The current Stage-3 bidirectional trace pair remains necessary whenever that distinction matters.

---

## 7. Directed gauge on arrows

Attach to `(P,g)` the Phase-A gauge

`ell_D(P,g)=ell_E(g)`.

It depends only on displacement and is translation invariant.

Its inverse arrow has

`ell_D((P,g)^(-1))=ell_E(-g)`,

which may differ from `ell_E(g)`.

Thus the current directed line gauge is naturally a left-translation-invariant asymmetric gauge on the displacement action groupoid.

The current orientation-free spectrum is

`{ell_D(P,g), ell_D(P·g,-g)}`.

This is an exact reinterpretation of R061 Stage 2/3, not a new metric.

---

## 8. Path-formal / N-valued endpoint pushforward

For a fixed start `P`, let a path-formal object be

`X=sum_p n_p[p]`.

Define the endpoint-displacement pushforward into the natural-number group semiring

`F_{D,*}(X)=sum_p n_p [delta_D(p)] in N[G_D]`.

### Theorem DG-C5 — semiring pushforward

Because endpoint displacement is additive under path concatenation,

- formal addition pushes forward by coefficient addition;
- concatenation pushes forward by convolution on `G_D`.

Hence `F_{D,*}` is a natural-number semiring homomorphism on a fixed compatible typed path skeleton.

For one line trace fiber `T_{a,b}^{(ij)}`, every realization has the same displacement `g`, so

`F_{D,*}(Realize_E(T_{a,b})) = binom(a+b,a) [g]`.

This reproduces the numerical multiplicity before Boolean support while discarding internal word order.

---

## 9. Endpoint displacement quotient is not canonical Boolean BRC

Do not identify the new quotient with historical Boolean BRC.

Canonical BRC support lives on **typed terminal states/cells** on an explicitly declared skeleton.

The displacement arrow forgets, depending on the domain:

- line component trace;
- sector/terminal-cell realization data;
- path provenance;
- reverse-vs-canonical-reverse distinction.

In particular, the current R062 definition already warns that trace quotient and Boolean support quotient are globally distinct.

Freeze candidate:

`DIAGONAL_ENDPOINT_QUOTIENT != BOOLEAN_BRC_SUPPORT_QUOTIENT`.

`DIAGONAL_ENDPOINT_QUOTIENT != NATIVE_TRACE_QUOTIENT`.

These are different forgetful maps from richer path data.

---

## 10. Candidate commuting diagram

The safe Phase-C diagram is

```text
CONCRETE NATIVE PATH WITNESS
        |\
        | \ component-preserving trace quotient
        |  -> TRANSLATED NATIVE TRACE
        |          |
        |          | End_D
        v          v
DERIVED DISPLACEMENT ARROW (P,g)

PATH-FORMAL / N-BRC on declared typed skeleton
        |
        | endpoint-displacement coefficient pushforward
        v
N[G_D]
```

Historical Boolean BRC remains a separate support projection on its typed terminal skeleton.

No inverse is claimed from displacement arrows back to native lines or path provenance.

---

## 11. Canonicity status

Within the current **derived translated displacement layer**, the diagonal gauge arrow is canonical in the following limited sense:

- the gauge kernel is exactly `Z(1,1,1)`;
- the min-zero section is unique;
- the construction is permutation/cyclic covariant;
- no reference axis is required by the quotient itself;
- it exactly recovers the frozen Stage-2 `Z^2` decoder and composition.

Native-semantics verdict:

`CANONICAL_DERIVED_G1_ENDPOINT_OBJECT`, not `DECLARED_N0_PRIMITIVE`.

A future N0 promotion would require a separate definability certificate from packet/adjacency structure and is not attempted here.

---

## 12. Phase-C verdict and next

Freeze candidate verdicts:

- `DERIVED_DIAGONAL_DISPLACEMENT_ACTION_GROUPOID = ESTABLISHED`;
- `PATH_CONCATENATION_DESCENDS = ESTABLISHED`;
- `TRACE_COMPOSITION_DESCENDS = ESTABLISHED`;
- `TRACE_REVERSE_AND_CANONICAL_REVERSE_COEQUALIZE_DOWNSTREAM = ESTABLISHED`;
- `N_VALUED_ENDPOINT_PUSHFORWARD = ESTABLISHED`;
- `ENDPOINT_DISPLACEMENT_IS_NOT_LINE_MEMBERSHIP = ESTABLISHED`;
- `ENDPOINT_DISPLACEMENT_IS_NOT_BOOLEAN_BRC = ESTABLISHED`;
- `N0_PROMOTION = NOT_CLAIMED`.

Next Phase D: perform a dependency/regression audit on current canonical files and classify the smallest source correction required if Driver integration is pursued. The audit must identify which current statements are truly contradicted, which only need retyping, and which remain untouched.
