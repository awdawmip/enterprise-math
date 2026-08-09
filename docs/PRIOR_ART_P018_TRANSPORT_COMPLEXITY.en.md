# Prior Art Boundary — P018 Transport Complexity

Status: `PRIOR-ART NOTE`  
Scope: deterministic one-message function computation, communication complexity, coding for computing, decoder side information, and the boundary around P018 transport branching capacity

## Established neighboring mathematics

Yao's 1979 distributed-computing paper is a foundational source for communication-complexity models: the cost of computing a function can be studied through the information that separated parties must exchange. [SRC-YAO-1979-DISTRIBUTIVE]

Orlitsky and Roche's *Coding for Computing* studies coding rates for computing functions when the decoder has correlated side information. [SRC-ORLITSKY-ROCHE-2001-CODING]

Accordingly, P018 does **not** claim as inventions:

- communication complexity as a field or model;
- minimizing communication needed to compute a function;
- zero-error / exact function computation with side information;
- coding specifically for a requested function rather than reconstructing all hidden inputs;
- the general observation that a decoder's side information can reduce the message alphabet or rate;
- generic product protocols obtained by concatenating/factoring messages through an operation tree.

## Enterprise Math-specific specialization

P018 asks a narrower finite-state question after the exact state-sufficiency problem has already been solved by contextual congruence closure:

> given only the original coarse input classes, how many distinct coarse output classes can one operation still produce inside the worst coarse input cell, and what is the exact minimum alphabet for a deterministic correction token that makes the coarse output exact?

The project packages that finite cardinality as `B_E(mu)`, the **transport branching capacity**. Its elementary minimum-token theorem is not claimed as a new communication-complexity result. The project-specific use is the integration with:

- precision equivalence/congruence from P018-T169–T181;
- minimum persistent detail from P018-T176/T178;
- carry/defect transport from the earlier precision calculus;
- operation-tree composition bounds;
- integer-only fixed-length bit costs;
- explicit arithmetic examples showing that radix addition has a two-symbol minimum token while radix multiplication can saturate the full residue-pair information bound.

## Important distinction

`B_E(mu)` measures **one-step deterministic transport ambiguity given coarse input classes**. It is not the number of states in the minimal exact contextual quotient.

These two quantities answer different questions:

1. persistent state complexity: what detail must each operand retain so every declared operation is well-defined?
2. transport complexity: once the decoder already knows the coarse input cells, what additional operation-specific message is minimally required to identify the exact coarse output?

Radix addition is the canonical separation: full residue is unavoidable persistent detail, while a single carry bit is enough for one-step coarse-output transport.

## Claim discipline

The minimum-cardinality token result in Supplement 24 is an elementary finite counting theorem and should be read as a project coordinate/contract, not as a historical first in communication complexity or functional compression.

The genuinely open project question is stronger: characterize when minimal or near-minimal tokens admit **structured composable laws** (carry/cocycle-like or otherwise) across operation trees, rather than arbitrary cell-dependent codebooks. No claim is made that every efficient transport structure is cohomological.
