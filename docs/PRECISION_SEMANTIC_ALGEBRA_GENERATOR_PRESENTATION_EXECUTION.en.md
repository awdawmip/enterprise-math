# Semantic Algebra, Generator Presentation, and Execution Representation

Status: `FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

The representation-Pareto synthesis separates semantic precision from runtime implementation resources. The latest capability-selection results require one additional layer: the **presentation by selectable primitive generators** is not determined by the generated semantic algebra.

This note adds no new Foundation Question. It refines the object model used for future-law design.

## 1. Three distinct future-law objects

For a declared task, keep separate:

### A. Generated semantic algebra

The exact operations/effects that exist after closure and their composition law.

This answers:

`what can the future law do?`

### B. Generator / capability presentation

The named primitive actions/channels available for selection, together with their costs, provenance and semantic ownership.

This answers:

`which atomic capabilities are available to build the law?`

### C. Execution representation

The operational encoding used after a generator set has been chosen: generator tables, caches, monoid tables, formulaic normal forms, CRT channels, circuits, etc.

This answers:

`how is the chosen exact law executed?`

The three objects can vary independently.

## 2. Same semantic algebra can have different minimum designs

The Set-Cover action family gives a sharp witness.

Fix universe size m. Compare two catalogues, both with m+1 named actions and both generating the full Boolean semilattice `2^[m]` under OR.

- Catalogue A: all singleton actions plus one duplicate singleton. Minimum full-precision subset size = m.
- Catalogue B: all singleton actions plus one full-universe action. Minimum size =1.

Thus the systems have:

- the same generated semantic effects;
- the same abstract OR composition law;
- the same named action count;

but different minimum precision-preserving generator designs.

So the semantic algebra does not determine its design presentation cost.

## 3. Easy execution does not imply easy capability design

On the parent Set-Cover compiled matrices, every action word executes by OR-ing set masks. The actions commute and are idempotent; word normalization has logarithmic parallel depth.

Yet minimum preserving action selection remains Minimum Set Cover.

Even stronger, the monotone-universality compiler realizes arbitrary finite upward-closed preserving geometry while the compiled executor remains an OR semilattice.

Therefore execution-algebra simplicity gives no generic matroid/basis/optimization guarantee for primitive capability selection.

## 4. Given-subset verification, optimization, and execution are separate

A fixed selected subset can often be checked cheaply even when finding the optimum is hard.

In the Set-Cover family:

- execute a word: OR masks;
- verify a proposed preserving subset: OR masks and test full target coverage;
- optimize the minimum preserving subset: Set Cover.

These are three distinct computational questions.

The word “law complexity” should not merge them.

## 5. Presentation is part of the resource contract

A generator is not merely a redundant name for an element of the generated algebra. It is an atomic selectable resource with its own:

- acquisition/storage cost;
- provenance;
- legality/domain;
- physical or semantic ownership;
- availability to the future language.

Replacing one generator presentation by another while keeping the generated algebra fixed can therefore change the design problem materially.

## 6. Execution representation is downstream of generator selection

After a generator/capability family is chosen, its exact future law can still be represented by many runtime schemes:

- sparse generators;
- literal word caches;
- semantic effect automata;
- Cayley tables;
- formulaic normal forms;
- coefficient factorizations / CRT channels.

These belong to the representation Pareto of the chosen law.

Optimizing them does not by itself answer which generators should have been selected upstream.

## 7. Revised architecture

A useful future-law design pipeline is:

`declared semantic target`

`-> choose / synthesize generator presentation`

`-> close to generated semantic algebra`

`-> choose exact runtime representation/compiler`

`-> execute declared futures`.

Different questions belong to different arrows.

## 8. Inverse design versus forward execution

The latest result suggests a particularly useful distinction:

- **forward execution:** given a word/subset of primitive generators, compute its semantic effect;
- **inverse design/synthesis:** given a target semantic requirement/effect, find a minimum-cost primitive expression that realizes it.

Forward computation can be formulaically trivial while inverse synthesis remains combinatorially hard.

This is the next research bridge and should not be hidden under one generic “operation complexity” label.

## 9. Foundation routing rule

When reasoning about a future law, ask separately:

1. What exact semantic algebra is required?
2. What primitive generator/capability presentation is available or allowed?
3. What semantic target must the selected presentation realize?
4. How hard is verifying / synthesizing a suitable generator subset?
5. After selection, what exact runtime representation minimizes the chosen resource vector?

Do not infer answers to 2–4 from the simplicity of 1 or 5.

## 10. Evidence routes

Current research evidence includes:

- action-alphabet Set Cover and monotone universality;
- formulaic OR execution of the same compiled action families;
- same generated monoid with minimum preserving basis sizes1 versus m;
- constrained modular-sensor Set Cover;
- semantic word-normalizer and formulaic-algebra Pareto generations.

All remain Draft/noncanonical research evidence.

## Prior art / status

Generating sets, presentations, semilattices, Set Cover and compiler/runtime distinctions are standard prior mathematics/CS. The Enterprise Math value is the precision-first architecture separating semantic algebra, primitive capability presentation and execution representation.

No new FQ. No canonical-main or `EXECUTABLE_CHECKED` claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
