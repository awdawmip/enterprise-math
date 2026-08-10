# Relation-Support Stable Refinement versus Terminal Support Traces

Status: `RESEARCH BRIDGE / NONCANONICAL`

For deterministic total or partial actions, “make the operation descend on the quotient” and “preserve every future output trace” naturally lead to the same stable state refinement. For genuinely multivalued A4 relations, these two semantic requirements split.

This note isolates the exact boundary.

## 1. Support-level relation descent

Let X be a finite state set, `E_0` an initial observation equivalence, and `{R_a}` a finite family of labelled relations.

For a current equivalence E and source x, define the support quotient image

`B_a^E(x)={ [y]_E : x R_a y }`.

The empty set is retained exactly and means that action a has no admissible target from x.

A relation family is **support-stable** on E when

`x E y -> B_a^E(x)=B_a^E(y)`

for every action a.

Then each fine relation descends to a well-defined relation between quotient classes: the set of successor quotient classes depends only on the source quotient class.

## 2. Coarsest support-stable refinement

Starting from `E_0`, split each current block by the tuple

`(B_a^E(x))_a`

and iterate.

Every strict round splits at least one finite block, so the process terminates.

At the fixed point `E_*`, every declared relation is support-stable.

Moreover `E_*` is the unique largest support-stable equivalence contained in `E_0`.

Indeed, if F refines `E_0` and is already stable for every relation, then by induction F refines every iteration stage: equal F-states have equal sets of F-target classes, and every F-class lies inside a current E-class, so their sets of current E-target classes also agree. Thus F refines the fixed point.

This is standard labelled-transition-system / bisimulation-style partition refinement.

## 3. Total and partial deterministic specializations

If every source has exactly one target under action a, the support set is a singleton:

`B_a^E(x)={ [u_a(x)]_E }`.

The refinement is exactly ordinary total-operation congruence refinement.

If every source has zero or one target, the support is either

`empty`

or

`{target block}`.

Equality of these supports is exactly FQ-006's pair of requirements:

- identical definedness;
- identical target quotient class when enabled.

So total and deterministic-partial semantic repairs are the singleton/empty special cases of relation-support stability.

## 4. Terminal observed-support trace semantics is weaker

A different future language may refuse to expose quotient successor classes themselves. It may ask only:

> for every literal action word w, what set of **terminal observation labels** is reachable?

This is the support-trace language compiled by the A4 powerset / Boolean-semimodule route.

Two sources are trace-equivalent when every literal word has the same terminal observed support.

Support-stability always implies this trace equivalence: stable equivalent sources reach the same sets of E-classes after every word by induction, and E refines the original observation.

Therefore

`relation-support-stable precision`

always refines

`terminal observed-support trace precision`.

The converse fails for multivalued relations.

## 5. Six-state choice-timing witness

Use six states

`p,q,r,s,t,z`

with one constant present observation.

Let relation a encode two different timings of nondeterministic choice:

`p -> r`,

`q -> {s,t}`.

Then let

`r --b--> z`, `r --c--> z`,

`s --b--> z`,

`t --c--> z`.

This is the classical shape

`p = a.(b+c)`

versus

`q = a.b + a.c`.

At the initial constant partition, p and q both merely have a nonempty a-support into the single class.

The first support-stability refinement separates r,s,t,z because they have different enabled support sets for b/c. Once those behavioural classes exist, action a exposes

`B_a(p)={ [r] }`

versus

`B_a(q)={ [s],[t] }`,

so the second refinement splits p from q.

## 6. Yet every terminal support trace merges p and q

With constant observation, terminal observed support records only whether the final support is empty or nonempty.

Both p and q admit exactly the same relevant literal traces:

- a is reachable;
- `ab` is reachable;
- `ac` is reachable;
- every other continuation has the same empty/nonempty result in the fixture.

After choosing b or c, the other alternative cannot be queried on the same predecessor branch. The terminal language therefore forgets **when the nondeterministic choice occurred**.

The Boolean-semimodule support compiler leaves `{p,q}` merged at its exact fixed point, while relation-support stability separates them.

The missing information is branching correlation / choice timing, not terminal reachability.

## 7. This is a future-language distinction, not a contradiction

The two quotients answer different questions.

### Trace/support future language

Observable object:

`word -> union of terminal observation labels`.

Branch structure not jointly queryable by one word is intentionally forgotten.

### Relation-operation language

Observable/executable object:

`source quotient class -> set of successor quotient classes`.

To run the multivalued relation directly in the quotient world, successor behavioural types must remain correlated with the branching structure.

Therefore the relation-stable quotient can legitimately be finer than the P023 terminal-support quotient.

Neither is universally “the” minimal precision without declaring which future operation/observation language is required.

## 8. Relation to A4 witness precision

Support-stability still remembers only **which quotient target classes occur**.

It does not remember:

- multiplicity of several raw targets in one quotient class;
- literal path identity;
- provenance/source labels inside a target class;
- which branch died when aggregate support survives;
- per-branch costs or histories.

If the future theory can reactivate any of those distinctions, even support-bisimulation is too coarse and the A4 witness state must be enriched again.

Thus the hierarchy is task-relative:

`terminal observed support trace`

`<= relation target-class support / bisimulation-like state`

`<= richer witness/provenance state`,

with strict inequalities possible.

## 9. Semantic-precision consequence

The partial-operation line suggested that adding operation capability can be repaired by canonical state splitting. The multivalued relation case shows that the required split depends on **what it means to execute the relation after collapse**.

Demanding only terminal support traces may need less state than demanding a quotient relation whose target-class support is itself well-defined.

So semantic capability requirements must name the operation interface, not merely say “preserve relation futures.”

## 10. Prior-art boundary

Bisimulation, trace equivalence, labelled transition systems, nondeterministic automata and partition refinement are standard prior mathematics/computer science. A4 retains raw correspondence/witness ownership; P023/A2 retains declared future-signature and precision ownership.

The project value here is the explicit precision routing:

> **multivalued relation descent preserves successor branching structure and can require strictly more state than terminal observed-support traces.**