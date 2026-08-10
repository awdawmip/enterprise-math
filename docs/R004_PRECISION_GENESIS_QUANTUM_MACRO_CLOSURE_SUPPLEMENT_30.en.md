# R004 precision genesis — Supplement 30: joint witness coupling and lossless marginalization gate

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + A4/WEIGHTED-RELATION SPECIALIZATION`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_29.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplements 28–29 decomposed simultaneous **linear** target requirements using module presentations. This supplement moves back to arbitrary finite witness semantics and identifies the canonical object before any algebraic compression: the joint weighted coupling of all target coordinates over the same fine witnesses.

Relational projection, multivalued dependencies and lossless joins are prior database theory. The project-local point is only how this coupling surface plugs into the typed Representation Compiler and A4 escalation ladder.

## 1. Joint weighted coupling

Let q:X->Q be a finite source collapse. Let target maps

`t_i:X->T_i`, `i=1,...,m`,

share the same fine witness x. Let witness weight lie in a declared commutative monoid M.

For coarse state a and joint target tuple y=(y_1,...,y_m), define

`J_a(y)=op_{x:q(x)=a, t_i(x)=y_i for all i} w(x)`.

This is one typed weighted relation

`J: Q x (product_i T_i) -> M`.

Special cases:

- Boolean OR: joint MAY support;
- natural-number addition: joint witness-count tensor;
- finite-label union: joint witness-label coupling.

The generic weighted-relation machinery of Supplement 13 applies directly on the product target carrier. No new mother relation theory is required.

## 2. Marginals are pushforwards

For any finite map `f:Y->Z` from the joint target carrier, define

`(f_*J)_a(z)=op_{y:f(y)=z} J_a(y)`.

Associativity and commutativity give exact functoriality:

`(g o f)_*J = g_*(f_*J)`.

Every target marginal is just the pushforward along a coordinate projection

`pi_i: product T_j -> T_i`.

Likewise a coupled target predicate or target-side quotient is another pushforward.

Thus joint witness state can be transported through later deterministic target maps without reopening fine witnesses.

## 3. Marginals do not determine coupling

The erasure

`J -> (pi_1*J,...,pi_m*J)`

is generally many-to-one.

The smallest Boolean/count example uses two binary targets.

Diagonal coupling:

`{(0,0),(1,1)}`

and anti-diagonal coupling:

`{(0,1),(1,0)}`

have identical marginal MAY supports `{0,1}` on both coordinates.

With unit witness counts, the count tensors

`[[1,0],[0,1]]`

and

`[[0,1],[1,0]]`

also have identical row and column count marginals `(1,1)`.

Yet the coupled predicate `y_1=y_2` has count 2 in the first coupling and 0 in the second.

Therefore

`marginal semantics !=> joint witness semantics`.

A coupled future query is an exact witness that joint coupling information remains live.

## 4. Boolean uniqueness theorem

Let J be a nonempty finite relation inside `product_i T_i` and let `S_i=pi_i(J)` be its marginal supports.

The marginal supports uniquely determine J among all relations having those same projections **iff at most one S_i is non-singleton**.

Proof.

- If at most one marginal is non-singleton, every tuple is forced: all singleton coordinates are fixed and every value of the one varying coordinate must appear. Hence J is the full rectangular product.
- If at least two marginals contain at least two values, the full rectangular product and the same product with one tuple removed have identical coordinate projections: every coordinate value of the removed tuple still occurs in another tuple obtained by changing one of the two varying coordinates.

Thus nontrivial multi-coordinate coupling cannot be reconstructed from MAY marginals alone.

## 5. Rectangularity is a reconstruction certificate, not an inference rule

Define the rectangular hull

`Rect(J)=product_i pi_i(J)`

and the Boolean coupling obstruction

`C(J)=Rect(J)\J`.

Then

`C(J)=empty <=> J=Rect(J)`.

If an explicit lossless-factorization witness certifies `C(J)=empty`, joint MAY support can be reconstructed from marginals.

But after J itself has been erased, nontrivial marginals do not prove rectangularity: the same marginals are compatible with both the full rectangular relation and nonrectangular couplings.

Hence independence/lossless join is an extra reconstruction certificate, never an automatic consequence of marginal data.

This is another instance of Supplement 23's no-upward-lift rule.

## 6. COUNT and richer witness semantics

For witness counts, marginal row/column sums do not generally determine the joint contingency tensor. The 2x2 diagonal/anti-diagonal example is already minimal.

For label/witness identity, marginal label sets can likewise erase which labels occurred **together** in the same joint tuple.

Therefore the correct fallback is always the joint typed weighted relation at the declared semantic strength. A Boolean rectangularity certificate only justifies MAY-level reconstruction; it does not reconstruct COUNT, LABEL or witness transport.

## 7. Coupling state is itself a certificate carrier

Once J has been formed, later questions about marginals, coupled predicates or target transformations are deterministic observations/pushforwards of J.

Therefore Supplement 24 applies recursively: treat the finite joint-coupling table as certificate state and compile it against the **remaining coupled future language**.

This is the third recursive use of the same future-safe quotient principle:

1. compile world state;
2. compile retained certificate state;
3. compile joint-coupling state.

When the final coupled query has passed, J may be demoted to marginals if the remaining suffix uses only marginal semantics.

## 8. Validation

Independent finite checks include:

- every nonempty Boolean relation on product shapes `2x2`, `2x3`, `2x2x2`, and `2x2x3`: **120 distinct marginal-support profiles**; the uniqueness criterion above had zero violations, with 35 ambiguous profiles;
- all nonzero 2x2 natural-count tables with entries 0,1,2: 64 distinct row/column margin profiles, of which 15 admit multiple joint tensors; the diagonal/anti-diagonal pair is the smallest ambiguity;
- **1,296** count-table/component-map cases verified that pushforward to a target map commutes exactly with later marginalization/composition.

These are finite exact WIP checks, not fresh full-repository CI or canonical-main claims.

## 9. Prior-art and ownership boundary

Relational projection, multivalued dependencies, lossless joins and contingency-table marginal ambiguity are prior mathematics/computer science. Fagin's 1977 multivalued-dependency work is a direct classical prior for lossless reconstruction of relations from projections.

Generic support/correspondence semantics remain A4; generic weighted-relation aggregation remains the typed relation compiler/P023-A4 interface. R004's addition is only the fail-closed placement of **joint witness coupling before marginal erasure**, plus the explicit reconstruction/liveness rules.

## 10. Next frontier

The next question is no longer whether marginals lose coupling. It is **coupling cuts**: given a remaining family of coupled predicates, which joint witness distinctions are the minimal obstructions preventing demotion to cheaper marginal or factored certificates? This should be attacked by the same obstruction-cut method on coupling-certificate state rather than by introducing a separate correlation metric.
