# Design-Selection Complexity versus Execution-Algebra Complexity

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

A future-operation family can be extremely easy to execute and still be hard to **design minimally**. These are different computational questions.

The existing Set-Cover / monotone-capability compiler gives a sharp same-family witness: its action matrices commute, are idempotent, and admit a bitmask-OR word normal form, while minimum precision-preserving generator selection remains Minimum Set Cover and the generic preserving-family geometry can realize any finite monotone set system.

## 1. One compiled action family

For a Set Cover instance with universe elements j and candidate sets `S_a`, the parent compiler uses state coordinates `e_j,f_j`.

Action a acts by

- `e_j -> f_j` if `j in S_a`;
- `e_j -> e_j` otherwise;
- `f_j -> f_j` always.

The actions are 0/1, pairwise commuting and idempotent.

The parent theorem proves:

`selected actions preserve full STATE_KERNEL precision`

iff

`selected actions preserve full INTEGER_MODULE precision`

iff

`selected candidate sets cover the universe`.

Thus minimum preserving action selection is exactly Minimum Set Cover.

## 2. Exact word execution is only union

For one action a, represent its candidate set by a universe bitmask `m(a)`.

For any literal word w define

`U(w)=OR_(a occurring in w) m(a)`.

Then the exact compiled matrix effect of w depends **only** on U(w): universe coordinate j has been moved from `e_j` to `f_j` exactly when some action in w covers j.

Therefore

`U(uv)=U(u) OR U(v)`.

Action order and repetition disappear from the exact word effect.

The same matrices whose minimum generator design encodes Set Cover therefore have a formulaic commuting-idempotent execution algebra.

## 3. Word normalization has logarithmic parallel depth

A length-H action word is H set masks.

Balanced OR reduction gives

`normalization depth=ceil(log2 H)`.

If the universe has m elements and bit-level work is counted, normalization uses roughly

`m*(H-1)`

bit ORs.

No matrix multiplication is required by the formulaic executor.

Thus future execution is simple relative to the compiled instance size.

## 4. Given-subset feasibility is also easy

For a fixed selected action subset A, precision preservation is checked simply by OR-ing the corresponding set masks and asking whether the result is the full-universe mask.

So on this family:

- execute a declared word: easy OR normalization;
- verify one proposed preserving subset: easy union/full-mask test;
- find a minimum preserving subset: Set Cover optimization.

Verification/evaluation and optimization therefore separate cleanly.

## 5. Same-family NP-hardness boundary

The Set Cover reduction is polynomial-size. Consequently the minimum-design problem remains NP-hard in a family whose exact execution law is:

- commuting;
- idempotent;
- formulaic;
- semilattice-valued;
- parallel-normalizable by OR.

So difficult capability design cannot be attributed generically to difficult word dynamics, noncommutativity, long future closure, or complicated operation evaluation.

The combinatorial difficulty lies in **which generators must be retained**, not in how retained generators compose.

## 6. Stronger monotone universality survives the easy executor

The parent universality theorem starts from any nonempty upward-closed preserving family P on action set E.

Let `F_1,...,F_t` be its inclusion-maximal false subsets. Create one Set-Cover witness coordinate per `F_i`, and let action a cover witness i iff

`a notin F_i`.

The compiled action family is exactly the same Set-Cover matrix form.

Hence action a has a t-bit effect mask

`m(a)_i=1 iff a notin F_i`,

and every literal word again executes by bitwise OR.

Yet the preserving subsets are **exactly P**.

Therefore arbitrary finite monotone design geometry can coexist with one formulaic OR execution algebra.

## 7. Minimal preserving families can be arbitrary antichains

Because every finite monotone P is realizable, the inclusion-minimal preserving subsets can form any antichain.

They can:

- have unequal sizes;
- be exponentially numerous up to the Sperner bound;
- lack a unique least subset;
- defeat generic matroid/submodular/basis assumptions.

None of this forces the execution algebra itself to become complicated: it remains OR on the compiled maximal-false witness mask.

## 8. Complexity axes are orthogonal

The results identify at least three separate computational resources.

### Execution complexity

Given a word, compute its exact semantic operation/effect.

Here: OR masks, logarithmic parallel depth.

### Feasibility/evaluation complexity

Given a proposed capability subset, decide whether it preserves the declared target precision.

Here: union/full-mask check.

### Design/optimization complexity

Find a minimum-cost preserving subset, enumerate all minimal preserving subsets, or characterize the basis geometry.

Here: Set Cover / arbitrary monotone set-system complexity.

One axis cannot be inferred from another.

## 9. “Easy algebra” does not imply “easy basis”

A tempting but false generic heuristic is:

> if operations commute, are idempotent, and have a simple normal form, then a minimum precision-preserving generator basis should also be easy or canonical.

The same-family reduction refutes this.

Algebraic composition laws constrain how selected generators interact **during execution**. Minimum-basis structure asks which subsets meet a global semantic requirement. Those are different layers.

## 10. Relation to Stage131 representation Pareto

Stage131 now has another orthogonal distinction.

Even after choosing a particular action alphabet, one may optimize how its word law is represented: generators, caches, monoid tables, formulaic normal forms.

Before that, one may ask which generators should exist at all.

Thus a complete design problem has at least:

1. capability selection / semantic basis design;
2. exact execution-law representation;
3. runtime execution of the chosen representation.

Optimizing layer2 cannot solve layer1 in general.

## 11. Relationship to constrained modular sensors

The constrained modular-sensor Set Cover generation shows the same architecture on coefficient channels:

- evaluating the joint residue code is easy once sensors are selected;
- choosing a minimum sensor subset can be Set Cover-hard.

The action and coefficient examples together support a general routing rule:

> **do not infer design-selection complexity from the complexity of executing a fixed selected representation.**

## 12. Input-size caveat for arbitrary monotone families

The strong universality compiler may use one witness coordinate per maximal false subset. That witness universe can itself be exponentially large in the number of actions.

Therefore the universality statement is about realizable design geometry, not a claim that every monotone predicate has a polynomial-size OR compilation from a succinct description.

The polynomial NP-hardness statement comes from the ordinary explicit Set Cover specialization.

## 13. Executable evidence

The branch adds an OR-mask executor for the parent Set-Cover matrices and verifies:

- literal matrix word effect = formulaic union-mask effect;
- balanced normalization depth;
- exact preserving-subset equivalence at STATE_KERNEL and INTEGER_MODULE levels on the same matrices;
- all 3-action nonempty upward-closed preserving families (19 cases) retain their exact predicate while word execution remains OR through bounded horizons.

## Owner-local assets

- `src/enterprise_math/set_cover_formulaic_execution.py`;
- `src/enterprise_math/monotone_design_formulaic_execution.py`;
- corresponding tests;
- this bilingual theorem note.

The parent #375 generation retains ownership of the generic action-capability Set Cover and monotone-universality theorems.

## Prior art / status

Set Cover, monotone Boolean functions, semilattices and parallel OR reduction are standard prior mathematics/CS. This Draft owns only the cross-layer Enterprise Math result that minimum semantic design complexity and exact execution-algebra complexity are independent resources.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
