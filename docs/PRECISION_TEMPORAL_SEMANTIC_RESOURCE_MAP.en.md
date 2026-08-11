# Temporal Semantic Precision versus Representation Resources

Status: `FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

The Stage131 line now provides a sharp warning against using “future horizon” or “rule count” as a scalar proxy for precision. Even for a tiny commuting-idempotent OR action family, changing **what temporal information the future language observes** changes the exact operation algebra before any implementation tradeoff begins.

This note adds no new Foundation Question. It consolidates the semantic/resource routing exposed by the prefix generations.

## 1. Declare temporal observation semantics before optimizing representation

A literal action word can be observed at several exact semantic levels.

### Terminal effect

Observe only the final transformation/state effect.

For k OR generators, the algebra is the finite Boolean semilattice of `2^k` masks.

### Discovery-event order

Observe the order in which new state distinctions/generator effects first appear, but not how long the state remains unchanged between discoveries.

The exact algebra is finite with first-occurrence normal forms.

### Full prefix timing

Observe every cumulative prefix state, including how many steps each level persists.

The exact algebra is infinite over unbounded horizon, but has a run-length normal form with at most k structural phases and integer durations.

### Literal provenance

Observe which named action was executed even when the represented state does not change.

This can restore the full literal word language.

These are different future theories, not different implementations of one theory.

## 2. Exact quotient maps form a temporal semantic ladder

For the OR pressure family:

`literal provenance`

`-> full prefix timing`

`-> discovery order`

`-> terminal set`.

Each arrow is a deterministic semantic quotient.

The lower layers intentionally erase:

- stutter action identity;
- then stutter duration;
- then first-discovery order.

No representation optimization can recover a distinction after the declared semantic quotient has erased it.

## 3. Semantic cardinality can have different growth types at different layers

At exact word length H and fixed k:

- literal words: `k^H` — exponential in H;
- full timing semantics: `Theta(H^(k-1))` — polynomial;
- discovery order: finite saturation once H>=k;
- terminal effect: finite saturation once H>=k.

Thus “one more future step” can create exponentially many new syntax strings, polynomially many new timing semantics, or no new terminal semantic effects at all.

## 4. Infinite semantic algebra can still have finite-parameter exact presentation

Full timing semantics is infinite because durations are unbounded.

Nevertheless its exact run-length form has at most k phases:

`((g_1,r_1),...,(g_s,r_s)), s<=k`.

Composition scans at most k phases and combines integer durations.

So

`infinite number of semantic operations`

does not imply

`unbounded structural parameter dimension`.

Finite algebra cardinality and compact law presentation must remain separate concepts.

## 5. Materialized history and compositional operation state are different interfaces

A compact run-length form can represent an H-step prefix operation using O(k log H) simple field bits for fixed k.

But if a consumer asks to observe all H prefix states, H outputs still need to be emitted/materialized.

Therefore:

`compact exact future state`

does not imply

`zero-cost observable history`.

This is another instance of the broader answer/state/interface distinction.

## 6. Cache growth depends on the semantic key

Caching all operations through horizon H gives radically different laws:

### Literal cache

`1+sum_(h=1)^H k^h` — exponential.

### Full timing cache

`1+sum_s P(k,s) C(H,s)` — degree-k polynomial in H for fixed k.

### Discovery cache

Finite saturation.

### Terminal cache

Finite saturation at `2^k`.

Thus the phrase “cache all future rules through H” is incomplete until one states which semantic quotient defines one cache entry.

## 7. Class count and workload information are different resources

Worst-case semantic state count is distribution-free.

Shannon entropy requires a workload distribution.

Under a uniform literal-word workload the exact quotient fibers yield

`H_literal`

`= H_terminal`

`+ first-discovery-order information`

`+ discovery-duration information`

`+ stutter-action provenance information`.

These are exact semantic information increments induced by the quotient ladder.

## 8. Cardinality can grow while entropy converges

For fixed k and H->infinity under uniform random actions:

- terminal entropy ->0;
- discovery entropy ->`log2(k!)`;
- full timing entropy -> a finite coupon-collector constant;
- literal entropy = `H log2 k` grows linearly.

Meanwhile the **number** of full timing classes continues polynomial growth.

So worst-case indexing/storage capacity and average workload information can move in qualitatively different directions.

Neither may substitute for the other without declaring the optimization objective.

## 9. Work, batch depth, streaming latency and reuse are also distinct

After prefix semantics is fixed:

- sequential scan uses minimum OR work and O(1) streaming state, but batch dependency depth is linear in H;
- parallel prefix scan can attain logarithmic batch depth with additional work/storage;
- a terminal-only balanced reduction has attractive work/depth but is semantically invalid for full-prefix observation.

Likewise, materializing a reusable terminal normal form can save repeated work under reuse while adding an avoidable one-shot pipeline layer.

Thus “execution depth” itself must be qualified by the execution model.

## 10. Expanded Stage131 resource vector

A precision-preserving compiler/executor may need to report at least:

`semantic observation layer`

`x semantic class cardinality`

`x exact normal-form parameter dimension`

`x parameter bit width`

`x bounded-horizon cache entries`

`x workload Shannon information`

`x output materialization volume`

`x preprocessing/design cost`

`x execution work`

`x batch critical-path depth`

`x online latency`

`x live working storage`

`x reuse/amortization profile`.

These are not one scalar precision coordinate.

## 11. Foundation routing order

For a temporal future language, the safe order is:

1. declare which temporal distinctions are semantically observable;
2. derive the exact semantic quotient / operation algebra;
3. find an exact normal form or compiler state;
4. declare workload and execution model;
5. compare storage/work/depth/coding/cache implementations only inside that semantic-equivalence fiber.

Skipping step1 can make a resource-optimal implementation semantically wrong.

Skipping step3 can make a finite/infinite cardinality statement look like an implementation lower bound when a compact formulaic presentation exists.

## 12. Relation to existing Foundation layers

This note refines, rather than replaces, the earlier distinction between:

- state detail and semantic capability;
- semantic law and generator presentation;
- semantics and execution representation;
- sufficient answer and executable continuation state.

Temporal observation adds another routing axis: **which parts of a future path are themselves part of the law to be preserved**.

## 13. Prior-art boundary

Trace semantics, left regular bands, run-length encoding, parallel prefix scans, coupon collector asymptotics and Shannon entropy are standard prior mathematics/CS.

The Enterprise Math value is the consolidated precision-first routing: semantic temporal observation must be fixed before representation resources are compared.

No canonical-main or `EXECUTABLE_CHECKED` claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
