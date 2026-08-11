# Exact OR-Circuit Lower Bounds for Formulaic Future-Law Execution

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

The commuting-idempotent mask normal form removes exponential law tables, but resource analysis should still ask whether its remaining work/depth can be improved.

For the OR family, fan-in-two OR-only circuits admit exact lower bounds. They also expose a new distinction: **materializing a reusable normal form** and **executing one word once on one state** have different optimal depth.

## 1. Reusable word-effect materialization

A length-H word contributes H k-bit generator masks.

To materialize the exact semantic effect mask, output coordinate i is the OR of H input bits.

### Depth lower bound

A fan-in-two circuit node at depth d can depend on at most `2^d` inputs.

Therefore any output depending on all H inputs requires

`depth >= ceil(log2 H)`.

Balanced OR trees attain the bound.

### Work lower bound

One H-input OR requires at least H-1 binary OR gates.

Different output coordinates depend on disjoint variable sets. In an OR-only circuit, mixing coordinates would introduce a wrong positive dependency that cannot later be cancelled.

Hence the work lower bound adds across k coordinates:

`work >= k*(H-1)`.

Coordinatewise balanced trees attain it.

Thus the parent formulaic normalizer is jointly work/depth optimal **for the task of exposing the reusable effect mask itself**.

## 2. One-shot state execution can fuse the intermediate

Suppose the semantic effect does not need to be returned or stored. The task only asks for the updated state.

For each coordinate, the output is the OR of:

- the current state bit;
- H action-mask bits.

That is an `(H+1)`-input OR.

Therefore exact one-shot lower bounds are

`work >= k*H`,

`depth >= ceil(log2(H+1))`.

A balanced fused tree over the state bit and all action bits attains both.

## 3. Staged normalize-then-apply can have a depth tax

The staged implementation does:

1. normalize H action masks in `ceil(log2 H)` depth;
2. OR the reusable effect into the state in one more round.

So staged depth is

`ceil(log2 H)+1`.

Its total work is still exactly `kH`, equal to the fused one-shot lower bound.

The depth tax is

`ceil(log2 H)+1-ceil(log2(H+1))`.

This value is always0 or1.

It is0 exactly when H is a power of two; otherwise it is1.

Hence materializing an intermediate effect can cost one avoidable pipeline layer when the effect is only used once.

## 4. Sharp H=20 example

For k=5,H=20:

### Reusable effect materialization

- work:95 bit ORs;
- depth:5.

### Staged one-shot

- normalization+apply work:100;
- depth:6.

### Fused one-shot

- work:100;
- depth:5.

So fusion saves one full execution layer at no additional bit work.

## 5. Reuse reverses the preference

Now let the same word effect be applied to q states.

### Materialize once, reuse q times

Normalize once:

`k*(H-1)` work.

Apply to q states:

`k*q` work.

Total:

`W_materialized = k*(H-1+q)`.

### Independently fuse q executions

Each state pays kH work:

`W_fused = q*k*H`.

The exact work saving from materialization is

`W_fused-W_materialized = k*(q-1)*(H-1)`.

For q=1 the saving is zero. For every q>1 and H>1 it is strictly positive.

Thus reuse count is an independent resource coordinate.

## 6. Parallel depth under reuse

If the q state applications can run in parallel after one common normal form is available, materialized depth is still

`ceil(log2 H)+1`.

Independent fused executions can also run in parallel, with depth

`ceil(log2(H+1))`.

Therefore materialization may pay at most one extra parallel layer while saving large duplicated work across many consumers.

## 7. Intermediate state is neither automatically waste nor automatically value

The result gives a precise version of a broader project pattern:

- an intermediate representation can be unnecessary for a one-shot terminal computation;
- the same intermediate can be valuable or essential when continuation/reuse is part of the future language.

The correct comparison must therefore state whether a normal form is:

- ephemeral;
- externally observable;
- cached for repeated execution;
- reused across many states/queries.

## 8. Relationship to answer-versus-state continuation debt

The earlier continuation theorem distinguishes a terminal answer from an executable future state at the semantic level.

The current result is an implementation-level analogue inside one unchanged semantic law: even when the reusable effect mask and fused one-shot execution are semantically equivalent for one query, materializing the intermediate changes work/depth and enables reuse.

These two boundaries should not be conflated, but they share the same architectural lesson: whether an intermediate must persist depends on future continuation semantics.

## 9. Lower-bound scope

The exact work proof assumes fan-in-two **OR-only** circuits over the k independent coordinates.

It is not a generic Boolean-circuit lower bound and does not claim optimality under arbitrary word-RAM, SIMD, unbounded-fan-in, hardware lookup or compressed instruction models.

The model is intentionally narrow enough for the lower bounds to be exact and executable.

## 10. Stage131 consequence

Stage131 representation resources now include not only storage/work/depth, but also **materialization and reuse policy**.

One exact formulaic future law can be executed as:

- reusable normalized operation;
- fused one-shot state update;
- shared normalized operation reused across many states.

Their semantics may coincide for a particular query while their optimal execution circuits differ.

## Owner-local assets

- `src/enterprise_math/or_circuit_execution_lower_bound.py`;
- `src/enterprise_math/or_normal_form_reuse_tradeoff.py`;
- corresponding tests;
- this bilingual theorem note.

## Prior art / status

OR-tree lower bounds, circuit depth/work and common-subexpression reuse are standard prior CS. P023/A2 retains future-signature/precision ownership. This Draft owns only the exact Stage131 materialization/reuse specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
