# BRC Weighted Projective / Gauge-Compensated Quotient — 2026-09-02

Status: `RESEARCH CANDIDATE / EXACT RATIONAL FINITE-DAG REPARAMETERIZATION / NOT ORDINARY QUOTIENT / NO TOOL PROMOTION`

Researcher-ID: `EM-BRCWLOG-6F42A1`  
Baseline: `main@8a05c2ad3d44d4f4aeb7040ad7213583061d669b`

Parent results:

- `research_notes/BRC_WEIGHTED_CWM_SAFE_QUOTIENT_20260902.md`
- `research_notes/BRC_WEIGHTED_LOCAL_BISIMULATION_BOUNDARY_20260902.md`
- `research_notes/BRC_WEIGHTED_CWM_REALIZABILITY_CORRECTION_20260902.md`

## 0. Executive result

Exact CWM future equality is the correct criterion for an ordinary all-prefix quotient that leaves incoming weights untouched.

There is, however, a strictly broader **representation-changing** equivalence.

For a CWM value

```text
X=(c,w,m)
```

and a positive rational scale `lambda`, define the mass-scaling action

```text
G_lambda(X)=(c, lambda*w, lambda*m).
```

Counts are unchanged while both mass coordinates receive the same factor.

Two live states `x,y` are projectively future-equivalent when:

1. their future path-count vectors to all declared targets are identical;
2. there exists one common `lambda>0` such that for every declared target `t`,

```text
W_t(y)=lambda*W_t(x)
M_t(y)=lambda*M_t(x).
```

Equivalently,

```text
F_T(y)=G_lambda(F_T(x))
```

componentwise across targets.

Such states are not ordinarily quotient-equivalent when `lambda != 1`. But `y` may be eliminated in favor of `x` if every incoming mass carrier to `y` is multiplied by `lambda`. The complete downstream CWM result of every path is then unchanged.

In log coordinates the same rule is

```text
ln W_t(y)=ln W_t(x)+g
ln M_t(y)=ln M_t(x)+g
```

with `g=ln(lambda)`, while incoming log weights gain the same additive constant `g`.

This is the precise form of the factor-relocation phenomenon found in the local-bisimulation counterexample.

## 1. Tool-reuse resolution

### T0_BRC

- coverage verdict: `EXTEND_EXISTING_TOOL`
- reuse state: `EXTEND_EXISTING_TOOL`
- use: branch result semantics remain the observable target; canonical Boolean R023 remains untouched.

### T6_OPERATION_SAFE_QUOTIENT

- coverage verdict: `EXTEND_EXISTING_TOOL / REPARAMETERIZING SPECIALIZATION`
- reuse state: `EXTEND_EXISTING_TOOL`
- use: future-observation equivalence remains the safety criterion.
- exact gap: ordinary T6 quotient keeps the operation representation fixed. The present construction permits a compensating rewrite of incoming weights while preserving the external future CWM semantics.

### T12_IDEMPOTENT_PATH_CLOSURE_BELLMAN

- coverage verdict: `REUSE_EXISTING_TOOL`
- reuse state: `REUSE_APPLIED`
- use: weighted path multiplication and the max-times/max-plus coordinate.
- boundary: the full CWM carrier remains non-idempotent in count and total-mass coordinates.

### T9_HOLONOMY_COCOYCLE_GLUING

- coverage verdict: `NOT_APPLICABLE_AS_EXISTING_SOLUTION`
- reuse state: `NOT_APPLICABLE`
- reason: T9 diagnoses route/gluing defects and holonomy. It does not provide the input/output contract “identify projectively proportional future CWM states and compensate incoming semiring weights.”

Repository source search found no current executable general-purpose state-gauge/reweighting method matching this contract.

This task therefore remains a narrow Weighted-BRC/T6 extension candidate rather than a new global gauge tool family.

## 2. PG-1 — central mass-scaling action

For `lambda>0` rational define

```text
G_lambda(c,w,m)=(c,lambda*w,lambda*m).
```

For CWM recoalescence `boxplus`:

```text
G_lambda(X boxplus Y)
 = G_lambda(X) boxplus G_lambda(Y),
```

because positive scaling commutes with ordinary addition and with `max`.

For CWM multiplication `boxtimes`:

```text
G_lambda(X boxtimes Y)
 = G_lambda(X) boxtimes Y
 = X boxtimes G_lambda(Y).
```

Thus a common positive mass scale can slide through either side of path composition.

Also

```text
G_1 = identity
G_lambda o G_mu = G_(lambda*mu).
```

**Status:** `PROVED`.

### Typing note

`G_lambda` is not called a unital semiring automorphism: unless `lambda=1`, it sends

```text
1_CWM=(1,1,1)
```

to `(1,lambda,lambda)`. It is a central positive mass-scaling action compatible with addition and with sliding across one multiplication factor.

## 3. PG-2 — projective future equivalence

Let `T` be the declared sink-target set and let

```text
F_t(x)=(C_t(x),W_t(x),M_t(x)).
```

For live states define

```text
x ~_proj y
```

iff:

1. `C_t(x)=C_t(y)` for all `t`;
2. their zero/support patterns therefore agree;
3. there exists one positive rational `lambda` such that for every supported target,

```text
W_t(y)=lambda*W_t(x),
M_t(y)=lambda*M_t(x).
```

The same `lambda` must work for every target and for both mass coordinates.

Dead states whose entire future signature is zero form their own exact class; no scale is required.

**Claim.** `~_proj` is an equivalence relation on live states.

- reflexive: `lambda=1`;
- symmetric: use `1/lambda`;
- transitive: multiply scale factors.

**Status:** `PROVED`.

## 4. PG-3 — incoming-weight compensation theorem

Suppose

```text
F_T(y)=G_lambda(F_T(x)).
```

Let an incoming CWM transition/prefix carrier into `y` be `A`.

Its original downstream contribution is

```text
A boxtimes F_T(y)
 = A boxtimes G_lambda(F_T(x)).
```

By PG-1 this equals

```text
G_lambda(A) boxtimes F_T(x).
```

Therefore redirecting that incoming contribution from `y` to representative `x` while replacing

```text
A -> G_lambda(A)
```

preserves every declared target CWM output exactly.

If multiple incoming contributions are redirected, add them at the representative using `boxplus`; distributivity preserves the full result.

**Status:** `PROVED`.

This is the gauge-compensated state-elimination rule.

## 5. Scalar-edge specialization

For a simple positive rational edge of mass `a`, its CWM lift is

```text
EDGE(a)=(1,a,a).
```

Then

```text
G_lambda(EDGE(a))=EDGE(lambda*a).
```

So the compensation rule reduces to the intuitive scalar rewrite

```text
incoming edge mass a -> lambda*a.
```

If eliminating states creates parallel edges, exact compression should allow a general CWM-valued transition:

```text
(k, sum edge masses, max edge mass)
```

rather than falsely replacing several parallel branches by one scalar edge and losing count multiplicity.

This is one reason the CWM product-semiring carrier is the natural quotient-level transition language.

## 6. PG-4 — exact canonical projective signature

For a live state, count support to declared targets is nonempty. Since projectively equivalent states have identical count vectors, they have the same first supported target under any fixed canonical target ordering.

Choose that anchor target `t0` and its positive max mass

```text
A(x)=M_t0(x).
```

Define normalized future coordinates

```text
C_hat_t(x)=C_t(x)
W_hat_t(x)=W_t(x)/A(x)
M_hat_t(x)=M_t(x)/A(x).
```

All values remain exact rationals.

Then

```text
x ~_proj y
iff
(C_hat_t,W_hat_t,M_hat_t)_t
are exactly equal for all t.
```

**Proof.**

If `F(y)=G_lambda(F(x))`, then `A(y)=lambda*A(x)` and every normalized ratio cancels the same factor.

Conversely, equality of normalized signatures gives

```text
lambda=A(y)/A(x)
```

and reconstructs the common proportionality for all target mass coordinates.

**Status:** `PROVED`.

So projective equivalence can be tested with rational cross multiplication only; no logarithm is needed.

## 7. PG-5 — logarithmic gauge form

For supported target coordinates define

```text
L_t=ln W_t
T_t=ln M_t.
```

Under mass scaling,

```text
L_t -> L_t + g
T_t -> T_t + g
```

where

```text
g=ln(lambda).
```

Therefore the following are gauge-invariant:

```text
C_t
Delta_t=L_t-T_t=ln(W_t/M_t)
T_t-T_t0
L_t-T_t0
```

for a chosen supported anchor `t0`.

The existing BRC LN runtime may materialize these log ratios when needed, but the native projective test remains exact rational arithmetic.

## 8. PG-6 — ordinary quotient versus gauge quotient

There are now three distinct equivalence levels.

### Boolean future equivalence

Keeps only reachability/support. It is generally too coarse for weighted semantics.

### Exact CWM future equivalence

Requires

```text
F_T(x)=F_T(y).
```

This is the coarsest all-prefix safe ordinary quotient when incoming weights remain unchanged.

### Projective/gauge CWM equivalence

Requires

```text
F_T(y)=G_lambda(F_T(x))
```

for one positive common `lambda`, and permits incoming-weight compensation.

It can be strictly coarser than exact CWM future equivalence while still preserving all external terminal CWM outputs after the declared reparameterization.

Do not call a `lambda!=1` projective merge an ordinary quotient: without the incoming compensation, absolute `W` and `M` outputs change.

## 9. Exact factor-relocation example

Use one terminal `t`.

Let

```text
A -> t with mass 1
B -> t with mass 2.
```

Then

```text
F(A)=(1,1,1)
F(B)=(1,2,2)=G_2(F(A)).
```

So `A` and `B` are projectively equivalent with `lambda=2`, though not exactly CWM-equivalent.

Any incoming edge

```text
u -> B with mass a
```

may be redirected to

```text
u -> A with mass 2a.
```

The resulting terminal path mass is unchanged:

```text
a*2 = (2a)*1.
```

In log coordinates:

```text
ln a + ln 2 = ln(2a) + 0.
```

This is the atomic gauge-slide identity behind the earlier local-bisimulation counterexample.

## 10. State-elimination boundary on a DAG

A graph rewrite that physically deletes `y` in favor of `x` must not invalidate the retained representative's own future signature.

A simple sufficient operational discipline on a topologically indexed DAG is:

1. choose a representative `x` that does not depend on deleted member `y` (no path `x -> ... -> y`);
2. redirect every incoming transition to `y` toward `x` with the projective scale compensation;
3. combine parallel redirected transitions with CWM `boxplus` rather than scalar-edge collapse;
4. delete `y` and its outgoing representation;
5. repeat in reverse topological order when eliminating several members.

The theorem in PG-3 is semantic and does not require this particular rewrite algorithm, but an implementation must respect an equivalent non-self-dependence condition.

For a fixed source carrying an immutable unit prefix, source-state scale cannot be silently discarded. Either the source representative must have `lambda=1` or the declared initial mass carrier must be compensated explicitly.

## 11. Relation to positive-path realizability

Scaling by positive rational `lambda` preserves exact positive-path realizability:

```text
(c,w,m) -> (c,lambda*w,lambda*m).
```

It preserves:

```text
c=1 <=> w=m,
c>=2 <=> m<w<=c*m.
```

Thus gauge compensation does not leave the exact realizability locus established in the correction note.

## 12. Exact checker target

The companion checker verifies:

1. central scaling/addition/slide identities on finite exact CWM samples;
2. projective-equivalence reflexive/symmetric/transitive witnesses;
3. canonical normalization equivalence using exact rational cross products;
4. incoming-transition compensation for multiple targets;
5. scalar-edge factor relocation;
6. strict separation among Boolean, exact-CWM, and projective equivalence;
7. preservation of the exact positive-path realizability conditions under scaling.

## 13. New structural interpretation

The BRC logarithm now plays two distinct roles:

```text
Delta = ln(W/M)
```

measures multiplicity surplus inside one future signature, while

```text
g = ln(lambda)
```

measures projective scale displacement between two future signatures.

`Delta` is gauge-invariant; `g` is the compensating gauge coordinate.

So the log layer separates naturally into:

```text
absolute log scale       -> representation-dependent / movable
relative surplus Delta   -> representation-invariant
relative target ratios   -> representation-invariant.
```

This distinction is stronger than merely saying “multiplication becomes addition.”

## 14. Next research frontier

The next exact questions are:

1. characterize the maximal projective quotient that can be realized by a canonical reverse-topological state elimination;
2. determine whether projective normalization materially reduces the all-terminal transfer-signature size on current BRC workloads;
3. study cycles separately, where a product of gauge factors around a loop may create a genuine holonomy/cocycle obstruction and T9 becomes relevant;
4. only after the cyclic case is typed, ask whether nontrivial loop gauge survives as a new BRC invariant.

The finite-DAG result does not pre-claim any cyclic holonomy theorem.
