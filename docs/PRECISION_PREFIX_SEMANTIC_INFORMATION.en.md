# Information Decomposition of the Prefix Semantic Ladder

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

The terminal/discovery/timing quotients remove different semantic distinctions. Under a uniform literal-word workload, the exact quotient fibers convert that hierarchy into an exact Shannon-information decomposition.

For a length-H word over k generator labels:

`literal provenance -> full timing -> discovery order -> terminal set`.

The total literal information splits into terminal-state information plus three independent quotient increments: first-discovery order, discovery timing, and stutter action provenance.

## 1. Uniform literal workload

Let W be uniform over the `k^H` literal words of exact length H.

Then

`H(W)=H log2 k`.

For any deterministic quotient Q of W, conditioning on a semantic class q leaves a uniform distribution over that class's literal fiber. Therefore

`H(W)=H(Q)+E[log2 |fiber(Q)|]`.

This identity turns the exact fiber formulas into semantic information budgets.

## 2. Entropy ladder

Let

- `H_T` = terminal-set entropy;
- `H_D` = discovery-order entropy;
- `H_P` = full prefix-timing entropy;
- `H_L` = literal-word entropy.

Because each layer is a deterministic quotient of the layer above:

`H_T <= H_D <= H_P <= H_L`.

The branch computes every term directly from exact quotient fibers and verifies the complete chain rule over bounded parameter grids.

## 3. Terminal-set entropy

For terminal support size s:

- number of terminal classes: `C(k,s)`;
- literal fiber of each class: `s! S(H,s)`.

Thus each such terminal class has probability

`s! S(H,s) / k^H`.

Summing the Shannon terms over s gives exact `H_T`.

## 4. Discovery-order entropy

For discovery length s:

- number of order classes: `P(k,s)`;
- literal fiber of each class: `S(H,s)`.

Thus each order class has probability

`S(H,s) / k^H`.

This gives exact `H_D`.

## 5. Exact first-discovery order information

Condition on using exactly S=s distinct generators.

One terminal set contains exactly `s!` discovery orders, and all have equal literal fiber size `S(H,s)`.

Therefore the conditional information added by restoring first-appearance order is exactly

`log2(s!)` bits.

Averaging over the random distinct-generator count S gives

`H_D-H_T = E[log2(S!)]`.

This identity is checked independently against direct entropy differences.

## 6. Duration information

Fix a discovery order of s generators.

A positive duration composition

`r=(r_1,...,r_s)`

has literal fiber

`f(r)=product_i i^(r_i-1)`.

The total literal fiber under the discovery order is `S(H,s)`, so the induced duration probability is

`P(r | S=s, order)=f(r)/S(H,s)`.

The conditional Shannon entropy of this duration distribution measures the information added by restoring **when** discoveries occur after their order is known.

Averaging over S gives

`H_P-H_D = E[H(duration | S)]`.

The branch computes this distribution exactly by positive compositions and verifies the entropy identity.

## 7. Stutter-action provenance information

Inside one full-timing class r, the remaining literal ambiguity is which already-seen generator was executed during each semantic stutter.

The class has `f(r)` literal words, so its conditional provenance entropy is

`log2 f(r)`.

Averaging over timing classes gives

`H_L-H_P = E[log2 f(r)]`.

This is precisely the action-label information that full prefix-state timing still does not observe.

## 8. Complete exact decomposition

Combining the quotient increments:

`H_L`

`= H_T`

`+ E[log2(S!)]`

`+ E[H(duration | S)]`

`+ E[log2 f(r)]`.

In words:

`literal action information`

`= terminal-set information`

`+ first-discovery order information`

`+ discovery-time information`

`+ stutter-action provenance information`.

The executable report asserts this equality numerically to tight floating tolerance after deriving every term independently.

## 9. Sharp k=2,H=2 witness

There are four equiprobable literal words:

`aa, ab, ba, bb`.

Literal entropy is2 bits.

Terminal semantics has classes

`{a}`, `{b}`, `{a,b}`

with probabilities `1/4,1/4,1/2`, giving

`H_T=1.5` bits.

Discovery order separates `ab` from `ba`, so

`H_D=2` bits.

At H=2 there is no additional duration or stutter ambiguity, hence

`H_P=H_L=2`.

The entire 0.5-bit terminal/discovery gap is

`E[log2(S!)]=1/2`.

## 10. Duration and provenance become separate positive resources at larger H

For k=2,H=3, words can have the same discovery order but different discovery times, and different literal stutter actions can share the same timing trace.

Consequently both

`H_P-H_D`

and

`H_L-H_P`

become strictly positive.

This is a minimal demonstration that timing information and action provenance are distinct semantic resources.

## 11. Conditional entropy equals quotient ambiguity

For each semantic layer Q:

`H(W|Q)=H_L-H(Q)`

is exactly the expected logarithm of the literal fiber size under the induced semantic workload.

Thus the semantic quotient has two simultaneous interpretations:

- a state-space partition;
- an exact expected ambiguity/information-loss channel under a declared workload.

The second requires a workload distribution; the quotient structure alone does not assign probabilities.

## 12. Semantic cardinality and semantic entropy are different resources

A layer can have many mathematically possible semantic classes while a workload concentrates on only a small fraction of them.

Therefore:

`log2(number of classes)`

is a worst-case index-size bound, not generally the Shannon information needed under the workload.

The next asymptotic generation pressure-tests this distinction for long random words.

## 13. Stage131 consequence

Representation design can now distinguish at least:

- worst-case semantic state count;
- information-theoretic minimum average code length under a workload;
- exact quotient ambiguity retained below a representation;
- runtime decode/materialization cost.

A semantic quotient may reduce class count and expected information by very different factors.

This is particularly relevant for cache compression and workload-aware coding after the semantic layer has been fixed.

## Owner-local assets

- `src/enterprise_math/prefix_semantic_information_decomposition.py`;
- `tests/test_prefix_semantic_information_decomposition.py`;
- this bilingual theorem note.

## Prior art / status

Shannon entropy, deterministic quotient chain rules, Stirling occupancy distributions and conditional entropy are standard prior information theory/combinatorics. P023/A2 retains future-signature/precision ownership. This Draft owns only the exact prefix semantic-information decomposition specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
