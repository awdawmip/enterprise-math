# Precision as Readout × Executable State × Presentation

Status: `FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

Recent A2/P023/A4 results show that a single word “precision” is being asked to perform three different jobs. A representation can be sufficient to answer a query, insufficient to continue the declared dynamics, yet still be reconstructible from a very small local code. Conversely, a lower-dimensional algebraic state can encode many exactly distinguishable discrete states.

This note adds no new Foundation Question and does not change the five diagnostic failure locations. It refines the **representation layer** used after those diagnostics.

## 1. Readout precision

A **readout** is enough information to answer a declared query family at the current boundary.

Examples include:

- terminal support for every literal word;
- terminal path-count traces;
- a static future-equivalence class label;
- a finite modular answer family.

Readout precision is task-specific and can intentionally forget how the answer was generated.

A readout need not be a reusable world state.

## 2. Executable-state precision

A representation is an **executable state** for future theory T when the declared operations/relations of T descend and can continue acting on the represented state without re-accessing erased fine detail.

This is stronger than readout sufficiency.

For finite weighted relation interfaces, there is a canonical operation-stability closure `C_T`. If

`E=C_T(P_0)`

is the minimal executable state below the original observation and an answer partition A satisfies

`E refines A refines P_0`,

then

`C_T(A)=E`.

Thus any underresolved answer in that interval repairs to the same executable state once continuation is required again.

## 3. Continuation debt

The gap between answer precision and executable-state precision is measurable.

For finite partitions one exact quantity is

`continuation debt = #blocks(executable state) - #blocks(answer)`.

A positive debt does not mean the answer was wrong. It means the answer discarded distinctions that become necessary only when the world must continue evolving.

This separates:

`correct one-shot answer`

from

`correct recursively reusable state`.

## 4. Local observation code is a different layer again

An executable exact model can sometimes be reconstructed from a much smaller finite local code.

Suppose a world law only uses local coefficients from a finite alphabet L. A code

`c:L->C`

need only be injective on L to recover those exact local values.

C need not itself support the future algebra.

The safe route is

`finite local code`

`-> exact local reflection / decode`

`-> exact executable law`

`-> future derivation in the exact algebra`.

## 5. Reflect generators before composing

A quotient can reflect every bounded local generator while failing to reflect large derived values.

Example pattern:

- local primitive coefficients are 1 and2;
- mod3 distinguishes every local value in `{0,1,2}`;
- two-step derived values4 and1 collide modulo3.

If composition occurs entirely in the coarse quotient, exact outputs are lost.

If local coefficients are decoded first, the exact transition law is recovered and later exact composition correctly produces4 and1.

Therefore:

`exact local code`

is not the same claim as

`exact direct code for every derived answer`.

## 6. Presentation precision

A **presentation** is a finite exact description of the generator/update law from which future semantics are computed.

Its quality should be judged by whether it presents the declared future theory exactly, not by whether every derived answer already appears explicitly in the representation.

This creates a third axis:

- readout representation stores answers;
- executable-state representation stores enough continuation structure;
- presentation representation stores exact generators/laws plus an evaluator.

The same future law may admit multiple exact presentations with different storage, numeric-range and execution-depth costs.

## 7. Representation type can change

Even after the exact discrete executable state has been recovered, a weaker future language can admit a different state type.

For an exact weighted machine with action matrices B_a and observation rows C, the complete terminal linear trace language lives in

`W=span_Q{C B_w}`.

If `r=dim_Q W`, there is an exact r-dimensional rational predictive state with induced actions T_a and decoder H.

This state is not generally a partition of the original discrete state set. It is a linear quotient of the vector-state space.

## 8. State-class count and algebraic dimension are different resources

A sharp weighted example has eleven trace-distinct discrete source states but a two-dimensional exact predictive state.

Nothing is being merged semantically: the eleven sources remain distinct vectors in Q^2.

The information has moved from

`number of discrete classes`

to

`exact coordinate values inside a lower-dimensional algebraic state`.

Therefore class count, vector dimension and numeric range are independent precision coordinates.

## 9. Minimality is representation-class relative

For terminal linear traces, the rational row-space rank r is minimal among **linear** predictive representations.

That does not make it universally minimal among every conceivable representation type.

Likewise, a coarsest partition stable for a relation interface is minimal inside the declared partition/quotient class, not necessarily inside linear, probabilistic, symbolic or witness-enriched state families.

So every minimality theorem must state its representation class.

## 10. Semantic precision now has at least four resource coordinates

The current architecture should not reduce these to one scalar:

1. **observational distinction** — which fine states remain distinguishable;
2. **continuation capability** — which declared operations/relations still descend;
3. **algebraic representation size/type** — class count, vector dimension, witness channels, etc.;
4. **numeric coefficient range / local code capacity** — how exact values are represented or reflected.

Execution depth/storage can be added when comparing presentations of the same law.

## 11. Structure can substitute for direct numeric range

A structurally richer exact machine can be reconstructed from a small local code and then generate large future values internally.

A structurally poorer direct-answer representation may instead require a much larger numeric modulus/range to reflect the same large answers directly.

Thus there is a genuine resource tradeoff:

`more compositional structure + smaller local numeric code`

versus

`less structure + larger direct answer range`.

This is not approximation; both routes can be exact under their own certificate conditions.

## 12. Readout joins and state joins are different

Combining two readouts only requires preserving both labels.

Combining two executable interfaces on one shared state may require an additional congruence/closure step because refining target states for one interface can reactivate unsafety in the other.

Therefore a “join of precisions” must declare whether it is joining:

- answers;
- reusable state interfaces;
- coefficient codes;
- or complete presentations.

The same algebraic product can be overprecision for one contract and exactly minimal for another.

## 13. Foundation routing rule

When a proposed coarse representation is claimed to be “exact enough,” ask three different questions:

### Readout

Does it answer the declared query family exactly?

### Continuation state

Can every declared future operation continue acting without hidden fine-state access?

### Presentation

If the representation is only a code for local generators, is there an exact decoder and an exact evaluator that generates the future semantics after decoding?

Do not infer one answer from another.

## 14. Relation to prior diagnostic layers

This note does not create a new failure location.

- DOMAIN still owns definedness/legality.
- RELATION still owns branching/witness multiplicity.
- IMAGE/FIBER still route existence versus hidden multiplicity.
- LEDGER still owns retained history/remainder state.

The new distinction concerns **how a sufficient representation is packaged after the required semantics have been identified**.

## 15. Prior-art boundary

Automata minimization, sufficient statistics, system realization, weighted quotients, closure operators and presentation/evaluation tradeoffs are standard prior mathematics/CS.

The project-specific synthesis is:

> **an exact answer, an exact reusable state, and an exact generator presentation are different precision contracts; one may be strictly smaller or larger than another depending on what future execution is declared.**

## Files

- `docs/PRECISION_READOUT_STATE_PRESENTATION.en.md`
- `docs/PRECISION_READOUT_STATE_PRESENTATION.zh.md`

Executable evidence remains in the A2/P023/A4 trace-to-state, bounded-local-law and linear-predictive child generations.

No canonical-main or `EXECUTABLE_CHECKED` claim. Hard block: `NONE`.