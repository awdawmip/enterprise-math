# BRC Weighted CWM Semiring and Safe Quotient — 2026-09-02

Status: `RESEARCH CANDIDATE / FINITE-DAG EXACT THEOREMS / T6 SPECIALIZATION / NO R023 MUTATION / NO TOOL PROMOTION`

Researcher-ID: `EM-BRCWLOG-6F42A1`  
Baseline: `main@889a0c10991fa9d8a70e273535ea0d1a21039f33`  
Parent results:

- `research_notes/BRC_WEIGHTED_LOG_SEMIRING_EXTENSION_20260902.md`
- `research_notes/BRC_WEIGHTED_MULTIPLICITY_TOWER_20260902.md`

## 0. Executive result

The previously derived path statistics

```text
C = supported path count
W = total non-negative path mass
M = strongest single-path mass
```

are not merely three parallel diagnostics. They form one exact product-semiring carrier.

Define

```text
S_CWM = N x Q_{>=0} x Q_{>=0}
```

with

```text
(c,w,m) boxplus (c',w',m')
    = (c+c', w+w', max(m,m'))

(c,w,m) boxtimes (c',w',m')
    = (c*c', w*w', m*m')

0_CWM = (0,0,0)
1_CWM = (1,1,1).
```

A supported edge of positive rational mass `a` lifts to

```text
EDGE(a) = (1,a,a),
```

and an absent/zero-mass edge lifts to `0_CWM`.

Then the ordinary finite-DAG semiring path sum in `S_CWM` returns exactly `(C,W,M)` in one evaluation.

The physically/path-coherent subset

```text
H = {(0,0,0)} union {(c,w,m): c>=1 and 0<m<=w<=c*m}
```

is closed under both operations. Therefore

```text
B = [C>0]
E = W/M
Delta = ln(E)
```

are derived coordinates of one closed exact carrier rather than separately propagated state.

For quotienting, define for every declared sink target `t` the future transfer value

```text
F_t(x) = CWM path-sum from x to t.
```

Two states are **all-prefix CWM-safe equivalent** iff their entire declared future signature agrees:

```text
x ~ y  iff  F_t(x)=F_t(y) for every declared target t.
```

This is necessary and sufficient when safety is required for arbitrary admissible prefix CWM states entering the quotient class. Hence the kernel of the future-signature map is the coarsest semantic quotient preserving the full `(C,W,M)` observable for all such prefixes.

This is a T6 operation-safe/predictive-quotient specialization to a non-idempotent weighted relation carrier; it is not promoted as a new global quotient tool.

## 1. Tool-reuse resolution

### T0_BRC

- coverage verdict: `EXTEND_EXISTING_TOOL`
- reuse state: `EXTEND_EXISTING_TOOL`
- reused law: branch propagation/recoalescence and support projection discipline.
- boundary: canonical R023 Boolean support remains unchanged and still cannot reconstruct erased multiplicity/weights.

### T12_IDEMPOTENT_PATH_CLOSURE_BELLMAN

- coverage verdict: `REUSE_EXISTING_TOOL`
- reuse state: `REUSE_APPLIED`
- reused law: semiring path-product / alternative-path aggregation.
- boundary: only the `M` coordinate is idempotent (`max-times`, or `max-plus` after logarithm). The full CWM addition is non-idempotent because count and total mass preserve multiplicity.

### T6_OPERATION_SAFE_QUOTIENT

- coverage verdict: `REUSE_EXISTING_TOOL`
- reuse state: `REUSE_APPLIED / DOMAIN SPECIALIZATION`
- reused law: quotient safety is future-observation compatibility, not superficial equality of current states.
- exact specialization: the declared future observation is the CWM transfer vector to the chosen terminal set.
- boundary: the current `operation_quotient.py` implementation is for finite deterministic endomaps. This weighted DAG/relation specialization uses the same future-equivalence principle but is not claimed to be directly executed by that deterministic module.

No new general-purpose quotient engine is introduced.

## 2. CWM-1 — product-semiring theorem

Use the three component semirings:

```text
S_C = (N, +, *, 0, 1)
S_W = (Q_{>=0}, +, *, 0, 1)
S_M = (Q_{>=0}, max, *, 0, 1).
```

`S_M` is a semiring because multiplication by a non-negative scalar preserves `max`:

```text
a*max(b,c) = max(a*b,a*c).
```

The direct product of semirings is a semiring under componentwise multiplication and componentwise additive operations. Therefore `S_CWM` with the operations in Section 0 is a semiring.

**Status:** `PROVED / DIRECT PRODUCT CONSTRUCTION`.

The coordinate projections

```text
pi_C : S_CWM -> S_C
pi_W : S_CWM -> S_W
pi_M : S_CWM -> S_M
```

are semiring homomorphisms.

## 3. CWM-2 — one path sum recovers count, total mass, and maximum

For every positive edge mass `a`, use edge carrier

```text
lambda(a)=(1,a,a).
```

For a path `p=e_1...e_k`, componentwise multiplication gives

```text
product_CWM lambda(a_e)
 = (1, product_e a_e, product_e a_e).
```

Thus one supported path contributes:

- count `1`;
- its ordinary multiplicative mass;
- the same mass to the max-times coordinate.

Recoalescing all source-to-target paths with `boxplus` gives

```text
(
  sum_p 1,
  sum_p w_p,
  max_p w_p
)
= (C,W,M).
```

**Status:** `PROVED`.

This replaces the conceptual picture of three independent evaluators by one product-semiring Weighted-BRC evaluator.

## 4. CWM-3 — coherent subcarrier closure

Define

```text
H = {(0,0,0)} union {(c,w,m): c>=1 and 0<m<=w<=c*m}.
```

Every finite positive path family evaluates into `H` by the multiplicity-tower sandwich theorem.

### Addition closure

Let `x_i=(c_i,w_i,m_i)` be nonzero coherent states and set

```text
c=c_1+c_2
w=w_1+w_2
m=max(m_1,m_2).
```

Then `m<=w` because `w` contains a summand at least `m`. Also

```text
w
 <= c_1*m_1 + c_2*m_2
 <= (c_1+c_2)*max(m_1,m_2)
 = c*m.
```

Hence `x_1 boxplus x_2` is coherent. Zero is the identity.

### Multiplication closure

For nonzero coherent states,

```text
m_1*m_2 <= w_1*w_2
```

and

```text
w_1*w_2
 <= (c_1*m_1)(c_2*m_2)
 = (c_1*c_2)(m_1*m_2).
```

Hence `x_1 boxtimes x_2` is coherent. Zero is absorbing.

Therefore `H` is a subsemiring of the CWM product semiring.

**Status:** `PROVED`.

## 5. CWM-4 — derived coordinates and Boolean projection

On nonzero coherent states define

```text
E(c,w,m)=w/m
Delta(c,w,m)=ln(w/m).
```

Coherence gives

```text
1 <= E <= c
0 <= Delta <= ln c.
```

Boolean support is

```text
sigma(c,w,m)=0 iff c=0,
sigma(c,w,m)=1 iff c>0.
```

Since the count projection lands in the natural-number semiring and natural nonzero support is a semiring homomorphism to Boolean OR/AND,

```text
sigma : H -> Boolean
```

is a semiring homomorphism.

For actual coherent path states the equivalent tests

```text
c>0 <=> w>0 <=> m>0
```

all give the same Boolean support bit.

## 6. CWM-5 — max-plus/T12 is an exact coordinate projection

The `M` coordinate is a max-times path semiring. On positive masses, logarithm gives

```text
ln(a*b)=ln a + ln b
ln(max(a,b))=max(ln a,ln b).
```

Thus

```text
M-coordinate --ln--> max-plus
```

is an exact semiring coordinate change on supported values, with zero mass typed as `-infinity`.

So the T12 dominant-path calculation is exactly the logarithmic image of the `pi_M` coordinate of CWM Weighted-BRC. It is not a heuristic replacement for the full `W` coordinate.

## 7. Future transfer signatures

Let `G` be a finite DAG with positive rational supported edges and a declared finite set `T` of sink targets.

For each state `x` and target `t`, define

```text
F_t(x) in H
```

as the CWM semiring sum of all paths from `x` to `t`, with the empty path at `t` valued as `1_CWM`.

If there is no path, `F_t(x)=0_CWM`.

Because targets are sinks and the graph is acyclic, these signatures are computed exactly backwards:

```text
F_t(t)=1_CWM
F_t(x)=boxplus_{e:x->y} lambda(a_e) boxtimes F_t(y).
```

Define the full future signature

```text
F_T(x)=(F_t(x))_{t in T}.
```

## 8. WQ-1 — sufficient condition for safe class aggregation

Suppose every state `x` in one quotient class `A` has the same future transfer `F_t(A)` to a target `t`.

Let an arbitrary admissible prefix family arrive separately at each `x` with coherent CWM state

```text
P_x=(c_x,w_x,m_x).
```

Before quotienting, the total contribution of class `A` to `t` is

```text
boxplus_{x in A} P_x boxtimes F_t(x).
```

Since every `F_t(x)` equals the same `F_t(A)`, distributivity gives

```text
(boxplus_{x in A} P_x) boxtimes F_t(A).
```

But

```text
boxplus_{x in A} P_x
 = (sum c_x, sum w_x, max m_x),
```

which is exactly the natural class-level prefix aggregation.

Therefore equal future CWM signatures are sufficient for quotienting a class while preserving every declared target's `(C,W,M)` result for every admissible incoming prefix family.

**Status:** `PROVED`.

## 9. WQ-2 — necessity under all-prefix safety

Assume a quotient class `A` is required to have one class-level future semantics independent of which member receives the incoming prefix, and safety must hold for all admissible prefix probes.

Take any two members `x,y in A` and any declared target `t`.

Probe the class once with the unit prefix entering only `x`:

```text
P_x=1_CWM,
P_z=0_CWM for z != x.
```

The pre-quotient target result is exactly `F_t(x)`. After quotienting, the class sees aggregate prefix `1_CWM`, so its class-level result must also equal `F_t(x)`.

Repeat with the unit prefix entering only `y`. The same class-level semantics must equal `F_t(y)`.

Hence

```text
F_t(x)=F_t(y).
```

Since `t` was arbitrary,

```text
F_T(x)=F_T(y).
```

Therefore equality of the entire declared future CWM signature is necessary.

**Status:** `PROVED`, under the explicitly stated all-prefix probe requirement.

### Boundary

If only one fixed source distribution is ever allowed, states with unequal future signatures may accidentally be safely merged because the distinguishing prefix probe is unreachable. Such source-specific compression is a different, weaker quotient problem.

## 10. WQ-3 — coarsest all-prefix CWM-safe quotient

Define

```text
x ~_CWM y  iff  F_T(x)=F_T(y).
```

By WQ-1 this equivalence is safe. By WQ-2 every all-prefix-safe quotient must refine it.

Therefore the kernel partition of the future-signature map is the **coarsest all-prefix quotient preserving the declared terminal CWM observations**.

**Status:** `PROVED / T6 PREDICTIVE-QUOTIENT SPECIALIZATION`.

No claim is made that a naive edge-identification quotient graph automatically realizes this semantic partition. A compressed implementation must retain class transfer semantics or construct transitions whose CWM series is exactly equivalent.

## 11. WQ-4 — CWM quotient refines Boolean-support quotient

Project each `F_t(x)` through Boolean support. If

```text
F_T(x)=F_T(y),
```

then their Boolean future support signatures are equal. Hence

```text
CWM-safe partition refines Boolean-future partition.
```

The refinement is generally strict.

Example to one terminal `t`:

```text
state x: one path of mass 1      -> F_t(x)=(1,1,1)
state y: one path of mass 2      -> F_t(y)=(1,2,2).
```

Both Boolean future supports are `1`, but they are not CWM-equivalent.

A stronger multiplicity example:

```text
state x: one path mass 1                 -> (1,1,1)
state y: two disjoint paths mass 1 each  -> (2,2,1).
```

Again Boolean future support agrees while count, total mass, and multiplicity surplus differ.

Thus a quotient proven safe only for R023 Boolean support may be too coarse for Weighted-BRC semantics.

## 12. WQ-5 — minimality of the scalar CWM state for the current tower

The tuple `(C,W,M)` determines the current scalar tower

```text
B=[C>0]
C
W
M
E=W/M
Delta=ln(W/M)
```

for reachable states.

None of the three primitive coordinates is generally determined by the other two.

### C is independent of W,M

```text
path masses (1,1)       -> (C,W,M)=(2,2,1)
path masses (1,1/2,1/2) -> (C,W,M)=(3,2,1).
```

### W is independent of C,M

```text
path masses (1,1)   -> (2,2,1)
path masses (1,1/2) -> (2,3/2,1).
```

### M is independent of C,W

```text
path masses (1,1)       -> (2,2,1)
path masses (3/2,1/2)   -> (2,2,3/2).
```

Therefore no coordinate can be dropped if the goal is to preserve all six current scalar observables for arbitrary positive path families.

This is a minimality statement relative to this declared observable family; it is not a claim that CWM contains all possible path provenance.

## 13. Operational algorithm on a finite DAG

For a fixed terminal set `T`:

1. lift each supported edge mass `a` to `(1,a,a)`;
2. compute every `F_t(x)` backwards in topological order using CWM semiring operations;
3. group states by exact vector `F_T(x)`;
4. retain one class-level future transfer vector per class;
5. aggregate incoming prefix CWM states with `boxplus`;
6. materialize `Delta=LN(W/M)` only if a logarithmic readout is requested.

All arithmetic before the optional LN readout can remain arbitrary-precision integer/rational carrier arithmetic.

## 14. Exact checker target

The companion experiment verifies:

- finite samples of CWM semiring laws;
- coherent-subcarrier closure;
- one-pass CWM DAG evaluation equals explicit path enumeration;
- all `4^6=4096` edge assignments on the complete four-vertex forward DAG for palette `{0,1/2,1,2}`;
- future-signature class aggregation on multiple terminal probes;
- strict failure of Boolean-only equivalence to preserve CWM observations;
- coordinate-minimality witnesses.

## 15. Next research frontier

The all-prefix future-signature quotient is exact but potentially expensive because it stores a transfer vector to every declared terminal.

The next question is compression **inside** the signature itself:

1. Can a smaller generator set of terminal/future probes determine the same CWM kernel?
2. When does local weighted bisimulation imply equality of all CWM future signatures?
3. Can acyclic structure yield a canonical minimal CWM automaton without enumerating every terminal transfer entry?
4. Which portions survive when cycles are admitted and finite path sums are replaced by a declared closure/star semantics?

These are the appropriate continuations. Naively merging states only because their Boolean supports agree is already refuted for the weighted target.
