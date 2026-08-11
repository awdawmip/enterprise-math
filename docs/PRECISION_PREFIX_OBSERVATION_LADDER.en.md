# Prefix Observation Ladder: Terminal Set, Discovery Order, and Full Timing

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

“Prefix-visible” is not one binary semantic choice. Even inside the commuting-idempotent OR language there are at least three exact future-observation levels:

1. final set of generators that ever appeared;
2. order in which new generators were first discovered;
3. full timing/duration of every cumulative prefix state.

These levels form exact quotient homomorphisms with distinct finite/infinite behavior.

## 1. Level T — terminal-set semantics

Keep only the final mask

`{generators appearing at least once}`.

Composition is set union / bitwise OR.

Including identity, the semantic monoid has exactly

`2^k`

elements.

At exact nonempty word length H, the number of reachable terminal effects is

`sum_(s=1)^min(k,H) C(k,s)`.

Once H>=k this saturates at `2^k-1` nonidentity effects.

## 2. Level D — discovery-order semantics

Keep the distinct generators in first-appearance order:

`delta(w)=(g_1,...,g_s)`.

Repeated uses of already-discovered generators are erased, but the order of first introduction remains visible.

Composition is:

- keep the complete left discovery list;
- scan the right list and append only generators not already present on the left.

This is the standard first-occurrence / free-left-regular-band style product.

The executable compiler verifies

`x*x=x`

and

`x*y*x=x*y`

on bounded complete families.

## 3. Level D is finite but much finer than terminal set

Including identity, discovery-order monoid size is

`1 + sum_(s=1)^k P(k,s)`

where

`P(k,s)=k!/(k-s)!`.

At exact length H the count is

`sum_(s=1)^min(k,H) P(k,s)`.

Once H>=k it saturates at the finite monoid size minus identity.

For k=5 the full discovery monoid has326 elements including identity, compared with only32 terminal masks.

## 4. Strict terminal/discovery witness

Words

`ab`

and

`ba`

have the same terminal set `{a,b}`.

But discovery orders are

`(a,b)`

and

`(b,a)`.

Therefore observing **which new capability appeared first** strictly refines terminal-set semantics even though stutter timing is still ignored.

## 5. Level P — full prefix timing

The parent run-length form stores

`((g_1,r_1),...,(g_s,r_s))`.

Projection to discovery semantics simply drops the run lengths:

`((g_i,r_i)) -> (g_i)`.

The branch verifies that this projection is a monoid homomorphism.

Unlike Level D, Level P remains infinite over unbounded horizon because the durations `r_i` are unbounded integers.

## 6. Strict discovery/timing witness

Words

`aab`

and

`abb`

have:

- the same terminal set `{a,b}`;
- the same discovery order `(a,b)`;
- different timing forms:
  `((a,2),(b,1))` versus `((a,1),(b,2))`.

Thus **when** the second discovery occurs is an additional semantic coordinate beyond **which** discovery occurs first.

## 7. Exact quotient ladder

There are exact surjective semantic maps

`full timing -> discovery order -> terminal set`.

They commute with word composition:

- timing composition projects to discovery composition;
- discovery composition projects to terminal OR.

Hence this is not merely a counting hierarchy; it is a hierarchy of exact operation algebras.

The kernels increase downward, so semantic precision decreases from timing to discovery to terminal.

## 8. Event-mask observation is equivalent to discovery order

Instead of generator identities, one may observe only the sequence of **distinct cumulative masks when they change**.

Each event adds exactly one new bit. The newly added bit recovers the introduced generator uniquely.

Therefore:

`discovery order <-> change-event mask sequence`

is an exact bijection.

So Level D is the minimal exact state for an observation language that reports state-change events but not the duration of stuttering between them.

## 9. Exact class-count ladder

For exact nonempty word length H:

### Terminal

`N_T=sum C(k,s)`.

### Discovery order

`N_D=sum P(k,s)`.

### Full timing

`N_P=sum P(k,s) C(H-1,s-1)`.

with all sums over `s=1..min(k,H)`.

Always

`N_T <= N_D <= N_P <= k^H`.

Strict inequalities occur as soon as the corresponding observation resource becomes available.

## 10. Sharp k=5,H=5 ladder

At k=5,H=5:

- literal words:3125;
- full timing traces:1045;
- discovery orders:325;
- terminal effects:31.

Thus different observation interfaces remove different kinds of literal redundancy:

- terminal quotient removes order and timing;
- discovery quotient restores first-introduction order but still removes stutter timing;
- full timing restores durations while still forgetting which already-seen generator caused a stutter.

## 11. Even full prefix timing is still a quotient of literal syntax

Two literal words can produce the same full cumulative-mask trace if they differ only in which already-seen generator is used during a stutter.

Example after both a and b are already present: choosing a versus b next leaves the same prefix state.

Therefore Level P is exact for full prefix-state observation but is still coarser than literal action provenance.

If the future language observes action labels themselves, costs per action, provenance, or branch-specific events, the semantic state must be enriched again.

## 12. Semantic dimension versus resource representation

The three semantic levels should not be mixed with implementation choices.

Once a level is declared, it may have many resource-equivalent representations:

- terminal masks can use bitsets, tables or circuits;
- discovery orders can use generator lists or event masks;
- full timing can use raw H-step traces or compact run-length forms.

The semantic ladder comes first; representation Pareto comes second.

## 13. Stage131 consequence

Future-language precision can depend on multiple temporal observation coordinates:

- final reachable state/effect;
- order of newly visible distinctions;
- exact timing/duration between changes;
- literal action/witness provenance.

There is no safe generic “prefix precision” scalar covering all of them.

Each observation contract induces its own semantic quotient and operation algebra.

## Owner-local assets

- `src/enterprise_math/prefix_observation_semantic_ladder.py`;
- `tests/test_prefix_observation_semantic_ladder.py`;
- this bilingual theorem note.

## Prior art / status

Left regular bands, first-occurrence word reductions, event traces and quotient homomorphisms are standard prior algebra/CS. P023/A2 retains future-signature/precision ownership. This Draft owns only the explicit terminal/discovery/timing observation-ladder specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
