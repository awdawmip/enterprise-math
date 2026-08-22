# QRF-R2 Independent Foundation Verification — Transverse Scalar Independence

`VERIFY_R2_EQUIVALENT_BUT_FOUNDATION_USEFUL`

Researcher-ID: `EM-QRF2-BD143C`  
Task: `RS-QRF-R2-INDEPENDENT-FOUNDATION-VERIFICATION`  
Taskbook source: `41a1bbdf23831f9ad2af160df4a6bd5603f22547`  
Owner branch: `research/qrf-r2-independent-foundation-verification`

## 1. Executive finding

The candidate

\[
\Delta_a\Delta_bQ(a,b)
=Q(a+1,b+1)-Q(a+1,b)-Q(a,b+1)+Q(a,b)=0
\]

is **not** mathematically empty. Relative to weaker assumptions it excludes genuine two-channel interaction terms, and it has a target-free operational reading: the scalar increment produced by one channel is invariant under changing the background state of the transverse channel.

However, once the two frozen axis laws

\[
Q(a,0)=a^2,\qquad Q(0,b)=b^2
\]

are supplied, the candidate plus those boundary laws is theorem-equivalent to

\[
Q(a,b)=a^2+b^2.
\]

Therefore R2 does **not** earn a stronger claim that the full primitive package is logically weaker than the current scalar law. Its positive value is instead locality and factorization of explanatory burden: one-dimensional axis calibration is separated from a local no-interaction law.

The condition is invariant under independent relabeling of the two channel factors and under axis swap, but it is not invariant under transformations that mix the two channel foliations. Hence its foundation usefulness is **relative to a primitive two-channel product decomposition**. If a later admissibility contract treats channel-mixing changes of chart as genuine equivalences, this verdict must be downgraded to `REJECT_R2_SCOPE_OR_INVARIANCE_FAILURE` without changing the mathematics below.

No Gaussian product, `C4`, Euclidean geometry, Pythagoras, holonomy, positivity, homogeneity, continuity, or multiplicative structure is used.

---

## 2. A. Exact discrete theorem

### Theorem A1 — zero plaquette interaction iff additive separation

Let `I,J` be nonempty connected integer intervals and let `A` be an abelian group. Let

\[
Q:I\times J\to A.
\]

Assume that for every elementary rectangle whose four vertices lie in `I x J`,

\[
Q(i+1,j+1)-Q(i+1,j)-Q(i,j+1)+Q(i,j)=0.
\]

Choose any basepoint `(i_0,j_0) in I x J`. Then for all `(i,j) in I x J`,

\[
\boxed{Q(i,j)=Q(i,j_0)+Q(i_0,j)-Q(i_0,j_0).}
\]

Conversely, every function having this form has zero mixed second difference on every elementary rectangle.

### Proof

For every horizontal edge define

\[
h_i(j)=Q(i+1,j)-Q(i,j).
\]

The mixed-difference equation is exactly

\[
h_i(j+1)-h_i(j)=0.
\]

Because `J` is connected by unit steps, `h_i(j)` is independent of `j`. Hence, for every horizontal edge,

\[
Q(i+1,j)-Q(i,j)=Q(i+1,j_0)-Q(i,j_0).
\]

Telescope along the connected integer interval from `i_0` to `i` (using the inverse increment when traversing backwards). This gives

\[
Q(i,j)-Q(i_0,j)=Q(i,j_0)-Q(i_0,j_0),
\]

which rearranges to the claimed formula.

The converse follows by direct cancellation: if

\[
Q(i,j)=F(i)+G(j)-c,
\]

then the four terms on every elementary rectangle cancel pairwise. `QED`

### Equivalent rectangle identity

The local equation is also equivalent, on a connected product grid, to the global four-corner balance

\[
Q(i_1,j_1)-Q(i_1,j_0)-Q(i_0,j_1)+Q(i_0,j_0)=0
\]

for every pair of coordinates `i_0,i_1 in I` and `j_0,j_1 in J`.

This is obtained by finite telescoping of the elementary plaquette defects.

### Weakest-hypothesis audit

For the theorem in the syntax used by the taskbook:

- **Codomain:** an abelian group is sufficient. Integers, order, positivity, multiplication, division, norm, topology, or a ring structure are unnecessary.
- **Domain:** connectedness of each one-dimensional factor under the unit-step relation is the actual propagation hypothesis. `N_0^2` is more than sufficient.
- If either factor is disconnected, zero elementary mixed difference only propagates within connected components; one basepoint formula need not determine values across disconnected components. Thus some connectivity assumption is genuinely necessary for the global conclusion.
- Symmetry `Q(a,b)=Q(b,a)` is not used.
- Positivity is not used.
- Homogeneity is not used.
- Continuity is not used.
- Multiplicative structure is not used.

An affine torsor over an abelian group would also suffice after rewriting the statement entirely in terms of differences, but no such extra abstraction is needed for the present integer-valued sector.

### Frozen-boundary specialization

On `N_0^2`, choose basepoint `(0,0)`. The theorem gives

\[
Q(a,b)=Q(a,0)+Q(0,b)-Q(0,0).
\]

The frozen axis laws imply `Q(0,0)=0`, so

\[
\boxed{Q(a,b)=a^2+b^2.}
\]

Conversely, `Q(a,b)=a^2+b^2` satisfies both frozen axis laws and zero mixed second difference. Therefore

\[
\boxed{\{\text{two axis laws}\}+\{\Delta_a\Delta_bQ=0\}\iff Q(a,b)=a^2+b^2.}
\]

This equivalence is exact, not asymptotic and not heuristic.

---

## 3. B. Non-redundancy versus semantic circularity

Consider the required competitors

\[
Q_\tau(a,b)=a^2+\tau ab+b^2,\qquad \tau\in\{-1,0,1\}.
\]

All three have identical axis restrictions:

\[
Q_\tau(a,0)=a^2,\qquad Q_\tau(0,b)=b^2.
\]

But

\[
\Delta_a\Delta_b Q_\tau(a,b)=\tau
\]

for every `(a,b)` because the square terms contribute zero mixed difference and `ab` contributes exactly `1`.

| `tau` | Frozen axes satisfied? | Mixed defect | R2 satisfied? |
|---:|:---:|---:|:---:|
| `-1` | yes | `-1` | no |
| `0` | yes | `0` | yes |
| `1` | yes | `1` | no |

Thus the condition has genuine mathematical content relative to the axis laws: it kills nonzero bilinear interaction while leaving all one-dimensional axis information untouched.

But this non-redundancy does **not** prove primitive superiority. After both axis laws are frozen, Theorem A1 shows that the whole package is logically equivalent to the target scalar formula. The question therefore moves from logical strength to operational semantics and invariance.

---

## 4. C. Operational meaning test

Define the one-step marginal contribution of the `a`-channel at transverse background `b` by

\[
M_a(a\mid b)=Q(a+1,b)-Q(a,b).
\]

Then

\[
\Delta_a\Delta_bQ(a,b)=0
\]

is exactly

\[
\boxed{M_a(a\mid b+1)=M_a(a\mid b).}
\]

Because the `b`-axis is connected, this local equality is equivalent to

\[
M_a(a\mid b)=M_a(a\mid 0)\qquad\text{for all }b.
\]

Symmetrically, if

\[
M_b(b\mid a)=Q(a,b+1)-Q(a,b),
\]

then R2 is equivalent to `M_b(b|a+1)=M_b(b|a)`.

### Operational reading

> Perform the same one-step change in channel `a` in two states that differ only by one step of channel `b`. The scalar increment attributed to the `a`-step must be identical in both backgrounds.

This is a four-value local comparison protocol. It does **not** require computing, naming, or presupposing `a^2+b^2`. It measures the absence of transverse interaction directly as a difference-of-differences.

Equivalently define the elementary interaction observable

\[
I_Q(a,b)=Q(a+1,b+1)+Q(a,b)-Q(a+1,b)-Q(a,b+1).
\]

R2 is the statement `I_Q(a,b)=0` on every elementary plaquette. This observable is defined before any target extension formula is known.

This passes the taskbook's non-target operational-meaning requirement.

### Why this is more than a verbal renaming

The target formula fixes a global value at every two-dimensional point. The marginal-shell rule instead specifies only how a one-channel operation is allowed to respond to transverse background changes. The axis laws supply the one-dimensional calibration; the local rule supplies the absence of interaction. The two pieces compose to the global formula by a theorem rather than by substitution of the target itself.

The distinction is therefore structural/local, not a difference in global model class once the boundaries are fixed.

---

## 5. D. Coordinate and relabeling pressure

### D1. Product-structure covariance

From Theorem A1, R2 is equivalent to vanishing four-corner defect on **every** rectangle, not only unit rectangles.

Let `phi` and `psi` be arbitrary bijections of the two axis label sets and define

\[
\widetilde Q(u,v)=Q(\phi(u),\psi(v)).
\]

If `Q` satisfies R2, then for every elementary `(u,v)` rectangle the four images under `(phi,psi)` form a rectangle in the original product structure. The global rectangle identity therefore gives

\[
\Delta_u\Delta_v\widetilde Q(u,v)=0.
\]

Hence R2 is preserved under independent relabeling of the two factors, even when the relabeling does not preserve numerical unit spacing.

It is also preserved under axis swap

\[
\widetilde Q(u,v)=Q(\psi(v),\phi(u)).
\]

Thus the natural universal invariance group is the automorphism group of the two product foliations: independent relabeling of each channel, with optional exchange of the two channel families.

### D2. Boundary-law covariance is narrower

The equation itself survives independent relabeling. The literal frozen boundary formulas `a^2` and `b^2` do not survive arbitrary renaming unless the axis laws are transported with the chart.

If `phi(0)=psi(0)=0`, then the transported boundary data are

\[
\widetilde Q(u,0)=\phi(u)^2,\qquad \widetilde Q(0,v)=\psi(v)^2.
\]

Demanding instead the unchanged syntax `u^2` and `v^2` after an arbitrary relabeling would alter the calibrated axis problem rather than merely relabel it.

Because the two frozen axis laws have the same square form, plain axis swap preserves the full written package.

### D3. Channel-mixing transformations are a real invariance boundary

R2 is not invariant under arbitrary transformations that mix the two channel foliations.

A simple algebraic witness is the shear on an integer chart,

\[
(a,b)=(u,u+v).
\]

Starting from the R2 model

\[
Q(a,b)=a^2+b^2,
\]

one obtains

\[
\widetilde Q(u,v)=Q(u,u+v)=2u^2+2uv+v^2,
\]

so

\[
\Delta_u\Delta_v\widetilde Q=2\neq0.
\]

Even as a pure set-theoretic relabeling of `N_0^2`, a channel-mixing bijection need not preserve the class. For example, let `T` swap only the points `(1,0)` and `(2,0)` and fix every other point. For the separable R2 model `Q(a,b)=a^2+b^2`, the pullback `Q o T` has elementary defect `-3` on the plaquette at `(0,0)`.

Therefore the exact foundation-facing statement is:

- R2 is intrinsic **relative to a chosen two-factor/channel decomposition**;
- it is covariant under all relabelings that preserve those two foliations, including axis swap;
- it is not a scalar invariant under a larger chart group that is allowed to mix the two factors.

Accordingly, if channel-mixing charts are declared admissible equivalences by the native two-channel semantics, R2 fails the invariance gate. If admissible charts preserve the channel decomposition (possibly swapping the channels), R2 passes.

---

## 6. E. Boundary-strength audit

Three distinct logical objects must not be conflated.

### E1. R2 alone is strictly weaker than the target formula

Every function

\[
Q(a,b)=F(a)+G(b)-c
\]

with compatible base value satisfies R2, regardless of whether `F` or `G` is quadratic.

Examples:

\[
Q(a,b)=a^3-7b+11,
\]

or

\[
Q(a,b)=2a+5b.
\]

Both satisfy zero mixed second difference and neither is the frozen target.

Thus R2 by itself does not determine:

- either axis law;
- quadratic growth;
- positivity;
- symmetry;
- homogeneity;
- multiplication or norm structure;
- any specific normalization at the origin.

### E2. Frozen axes + R2 are theorem-equivalent to the target formula

Once both axis functions are fixed to squares, Theorem A1 leaves no remaining two-dimensional freedom. Therefore the full package is **not** strictly weaker in model-theoretic content than `Q(a,b)=a^2+b^2`.

### E3. The equivalence is operationally more local, not merely notational

Despite global equivalence, the package factors the statement into:

1. one-dimensional calibration on each axis; and
2. a four-point local no-interaction law.

The local rule can be tested without evaluating the target formula, and violations are localized to plaquettes via `I_Q(a,b)`. This is a genuine foundation-useful decomposition even though the completed theory has the same models as the target formula.

Hence the correct category is **theorem-equivalent but operationally more local**, not strictly weaker and not reformulation-only.

---

## 7. Required negative boundary

The strongest negative boundary is:

\[
\boxed{\Delta_a\Delta_bQ=0\text{ determines only additive separation, not the axis functions.}}
\]

For any functions `F,G:N_0->Z` and any constant `c` with `F(0)+G(0)-c` chosen consistently, the separable field `F(a)+G(b)-c` satisfies R2.

A second negative boundary is structural:

\[
\boxed{\text{R2 is not invariant under channel-mixing changes of chart.}}
\]

Thus it cannot be promoted to an unconditional coordinate-free two-dimensional primitive without separately freezing the two-channel product structure.

---

## 8. Kill-condition audit

### Kill: theorem fails at weak scope

**Not triggered.** The theorem holds on any product of connected integer intervals with values in an abelian group.

### Kill: condition has no mathematical content beyond weaker assumptions

**Not triggered.** The `tau=-1,0,1` competitors have identical frozen axes but mixed defect `tau`, so R2 excludes real interaction freedom.

### Kill / downgrade: no target-free operational meaning

**Not triggered.** Marginal-shell invariance / zero plaquette interaction is defined and testable without the target formula.

### Kill: admissible independence can hold while mixed defect is nonzero, or vice versa

**No such counterexample exists for the operational meaning used here**, because that meaning is proved exactly equivalent to the mixed-difference equation.

### Invariance kill

**Conditionally exposed, not triggered under channel-preserving semantics.** Product relabelings and axis swap preserve R2. Channel-mixing transformations do not. Therefore acceptance is scoped to a primitive two-channel product decomposition. A native admissibility rule that identifies sheared/mixed channel charts would trigger `REJECT_R2_SCOPE_OR_INVARIANCE_FAILURE`.

---

## 9. Final verdict rationale

Leading verdict:

`VERIFY_R2_EQUIVALENT_BUT_FOUNDATION_USEFUL`

Reason:

1. zero mixed second difference is exactly equivalent to additive separation on a connected discrete product;
2. with the two frozen square boundary laws it is exactly equivalent to the current sum-of-squares scalar law;
3. nevertheless it carries independent mathematical content relative to weaker assumptions and admits a non-target operational reading as transverse marginal invariance;
4. it is genuinely local and modular: the two-dimensional extension law is separated from the one-dimensional axis calibration;
5. its invariance is sufficient under independent channel relabeling and axis swap, but not under channel-mixing chart changes;
6. therefore it is foundation-useful as a **two-channel-structure-relative local law**, but the evidence does not justify the stronger claim of an unconditional coordinate-free primitive.

This is deliberately below `VERIFY_R2_LOCAL_PRIMITIVE`: the fixed-boundary package has exactly the target model class, and the local law depends on retaining the two-channel product structure as part of the semantics.
