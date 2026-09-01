# P021 Multistep Direction Identity / Witness-Join Continuation

Status: `RESEARCH RETURN / P021-LOCAL FINITE-HORIZON CLASSIFICATION FROZEN`  
Task: `RS-P021-FOCUSING-DIRECTION`  
Researcher-ID: `EM-P021-4B8E2D`  
Claim: `chatgpt-p021-20260901-1142-4b8e2d`  
Execution branch: `research/p021-multistep-unique-matching-em-p021-4b8e2d`  
Execution base: `bd8781924b8423e18ef3d7b3a37d86ebc71fc1a6`  
Owner: `program/p021-causal-focusing-v3`

## 1. Executive verdict

The prior P021 correction proved that one-step global support-compatible direction identity is canonical exactly when the one-step bipartite composability support has a unique perfect matching.

That property is **not closed under time composition**.

Even if every adjacent time slice has a unique perfect matching, erasing the exact middle witness identity can make the endpoint direction identity ambiguous after only two steps and two direction classes.

The exact finite-horizon repair is a common-order criterion.

After transporting every time slice into the labels forced by its unique one-step matching, let `Gamma_r` be the directed graph of noncanonical support edges at step `r`. Then for every finite horizon `h`,

`endpoint class-level identity is unique`

if and only if

`Gamma_1 union ... union Gamma_h is acyclic`.

Equivalently, all noncanonical one-step support edges admit **one common topological order** across the whole horizon.

This condition is also the exact robust boundary for erasing fine middle witness identity: assuming the canonical matched chains are actually realizable, every fine witness refinement compatible with the same one-step supports preserves the canonical endpoint identity if and only if the common-order condition holds.

Terminal class:

`P021_MULTISTEP_DIRECTION_IDENTITY_COMMON_ORDER_EXACT`.

This is a bounded P021 direction-identity theorem. It is not a physical focusing/GR theorem and does not re-own generic relation composition or matching theory from their existing homes/prior art.

## 2. Frozen one-step input

At times `0,1,...,h`, suppose there are `n` direction classes.

For each step `r=1,...,h`, let

`S_r subset D^{r-1} x D^r`

be the Boolean class-level composability support.

Assume `S_r` has a unique perfect matching

`mu_r : D^{r-1} -> D^r`.

This is precisely the previously frozen P021 global support-compatible one-step identity criterion.

The present task asks a new question:

> If all one-step identities are individually canonical, when is the identity from time `0` to time `h` still canonical after composition, and when may the exact middle witness identity be erased safely?

The answer is not “always”.

## 3. Normalize all one-step matchings to the identity

Choose the time-0 label set `[n]={1,...,n}` and define cumulative canonical labels

`lambda_0=id`,

`lambda_r = mu_r o lambda_{r-1}`.

Thus `lambda_r(i)` is the time-`r` direction class reached from initial label `i` by following the forced one-step matchings.

Pull each support back to `[n] x [n]`:

`A_r(i,j)=1`

iff

`S_r(lambda_{r-1}(i), lambda_r(j))=1`.

By construction, every `A_r` contains the diagonal and has the identity permutation as its **unique** perfect matching.

Define the normalized ambiguity digraph

`Gamma_r = {(i,j): i != j and A_r(i,j)=1}`.

For a matrix with the diagonal matching fixed, the prior alternating-cycle theorem says:

`identity is the unique perfect matching of A_r`

iff

`Gamma_r is acyclic`.

Hence every individual `Gamma_r` is a DAG. The new issue is whether these DAGs are compatible with each other across time.

The construction is label-invariant: changing the initial labeling conjugates all `Gamma_r` by the same permutation, so acyclicity of their union is unchanged.

## 4. P021-MDI-T01 — Exact finite-horizon common-order theorem

Let Boolean matrix multiplication be relational composition:

`(P * Q)(i,k)=1`

iff there exists `j` with `P(i,j)=Q(j,k)=1`.

Define the class-level horizon envelope

`C_h = A_1 * A_2 * ... * A_h`.

This is the endpoint support obtained if only class-level support is retained and every class-compatible middle join is treated as realizable.

### Theorem

For every finite horizon `h>=1`,

`C_h has the identity as its unique perfect matching`

if and only if

`Gamma = Gamma_1 union ... union Gamma_h`

is acyclic.

Equivalently:

> There exists one ordering of the normalized direction labels such that every noncanonical support edge at every time step points forward in that same ordering.

### Proof

Every `A_r` contains all diagonal edges.

First, every edge of every `Gamma_r` already occurs as an endpoint edge of `C_h`: before step `r` follow the diagonal of the source label, use that noncanonical edge at step `r`, and after step `r` follow the diagonal of the target label. Therefore

`Gamma subseteq Gamma(C_h)`.

Second, suppose `C_h(i,j)=1` with `i!=j`. Then there is a class path

`i=x_0 -> x_1 -> ... -> x_h=j`

with `A_r(x_{r-1},x_r)=1` at every step. Delete the stationary diagonal moves `x_{r-1}=x_r`. Every remaining move is an edge of some `Gamma_r`. Thus `i -> j` is reachable in the union graph `Gamma`, so

`Gamma(C_h) subseteq transitive_closure(Gamma)`.

Consequently:

- if `Gamma` is acyclic, its transitive closure is acyclic, hence `Gamma(C_h)` is acyclic;
- if `Gamma` contains a directed cycle, all of its edges lie in `Gamma(C_h)`, hence `Gamma(C_h)` contains that directed cycle.

The identity diagonal is a perfect matching of `C_h`. For a bipartite support containing the diagonal matching, a second perfect matching exists exactly when the associated off-diagonal digraph contains an alternating/directed cycle. Therefore

`C_h unique identity <=> Gamma(C_h) acyclic <=> Gamma acyclic`.

QED.

## 5. P021-MDI-C01 — Minimal cross-time failure

Take two direction classes and two time steps:

`A = [[1,1],
      [0,1]]`

and

`B = [[1,0],
      [1,1]]`.

Each matrix has a unique perfect matching: the diagonal.

- `Gamma_A` has the single edge `1 -> 2`;
- `Gamma_B` has the single edge `2 -> 1`.

Each one-step ambiguity graph is acyclic, but their union is the directed 2-cycle

`1 -> 2 -> 1`.

Boolean composition gives

`A * B = [[1,1],
         [1,1]]`.

The endpoint support therefore has two perfect matchings: the diagonal and the swap.

Thus

`ONE_STEP_CANONICAL_IDENTITY`

does **not** imply

`MULTISTEP_CANONICAL_IDENTITY`.

The example is minimal in both parameters:

- with one direction class, ambiguity is impossible;
- with only one time step, the hypothesis already assumes unique identity.

Hence the smallest failure is exactly `n=2`, horizon `h=2`.

## 6. P021-MDI-T02 — Common topological order is the compositional certificate

Each individual unique-matching support admits at least one topological order of its ambiguity DAG. The counterexample above shows that choosing an order independently at each time is insufficient.

The exact reusable certificate is stronger:

> one permutation/order of the normalized labels must topologically order **all** step ambiguity digraphs simultaneously.

This is equivalent to acyclicity of their union.

Operationally, the finite-horizon test is therefore simple:

1. recover the unique one-step matchings;
2. transport all steps into the cumulative matching labels;
3. collect every off-diagonal support edge;
4. topologically sort the union graph.

If the sort succeeds, class-level identity is canonical for the whole horizon. If it fails, the returned directed cycle is an explicit ambiguity certificate.

This is strictly stronger than “every step is individually uniquely matchable” and strictly weaker than requiring every one-step support to be a permutation matrix.

## 7. Exact witness-join boundary

Historical P021 already established that class counts/support do not in general determine exact multi-step composition: the primitive object is the middle-incidence witness relation, and adjacent witnesses compose only when their exact middle incidence agrees.

The common-order theorem does **not** erase that distinction. Instead it identifies exactly one future observable for which the distinction can become irrelevant: endpoint canonical identity.

Let an exact fine witness realization of the same one-step supports be given. Compose the witness relations through exact equality of the middle incidence tokens, and let `J_h` be the resulting endpoint **class support**.

Assume the canonical matched chain for each label is actually realizable through the fine witnesses. Then

`I subseteq J_h subseteq C_h`,

where `I` is the diagonal identity support.

- `J_h subseteq C_h` because a fine witness chain can only follow class-level support edges;
- `I subseteq J_h` is the declared canonical-chain realizability condition.

### P021-MDI-T03 — Universal witness-refinement safety

Under those assumptions, the following are equivalent:

1. every fine witness realization compatible with the one-step class supports preserves a unique canonical endpoint identity;
2. the class-level horizon envelope `C_h` has unique identity;
3. the union `Gamma_1 union ... union Gamma_h` is acyclic;
4. all normalized noncanonical step edges admit a common topological order.

### Positive direction

If `C_h` has unique identity, then every exact fine endpoint support satisfies

`I subseteq J_h subseteq C_h`.

Any alternative perfect matching in `J_h` would also be an alternative perfect matching in `C_h`. None exists. Hence every compatible fine realization preserves the unique identity.

### Negative direction

If `C_h` is ambiguous, use a join-saturated fine realization. At every time boundary and direction class, choose one boundary token. For every class support edge, include the witness pair connecting the source class token to the target class token.

Then every class-level path in the Boolean product is realized as an exact witness chain, so

`J_h=C_h`.

Since `C_h` has an alternative perfect matching, at least one fine witness realization consistent with all the one-step supports destroys endpoint canonicality.

Therefore the common-order condition is not merely sufficient: it is the exact “safe under all witness refinements” boundary for this declared endpoint identity observable.

## 8. P021-MDI-C02 — Same one-step supports, opposite exact endpoint verdicts

The minimal `A,B` pair admits two explicit fine witness realizations with **identical** one-step class supports and the same unique one-step matchings.

### Saturated realization

At each middle class use one shared token for every incoming and outgoing support edge through that class.

For middle class `2`, the noncanonical incoming edge `1->2`, the diagonal incoming edge `2->2`, the noncanonical outgoing edge `2->1`, and the diagonal outgoing edge `2->2` all share the same middle token.

All four endpoint pairs become realizable. Thus

`J_sat = [[1,1],[1,1]]`,

so endpoint identity is ambiguous.

### Filtered realization

Keep a shared diagonal token for each canonical diagonal chain, but give every noncanonical incoming witness a private token not used by any outgoing witness, and every noncanonical outgoing witness a private token not used by any incoming witness.

The one-step class supports are still exactly `A` and `B`: every declared support edge has a witness. The canonical diagonal chains remain realizable. But the noncanonical middle witnesses do not join.

Hence

`J_filter = [[1,0],[0,1]]`,

so endpoint identity is unique.

Therefore the same one-step support data can yield two different exact multistep identity verdicts once the middle witness identity is varied.

This gives a direct P021-local proof that fine witness identity is genuinely load-bearing outside the common-order-safe regime.

## 9. P021-MDI-T04 — Finite template-family corollary

Suppose a finite family of normalized one-step support templates each has unique identity. Consider arbitrary finite words in those templates.

Then every word has unique class-level endpoint identity if and only if the union of the ambiguity digraphs of **all templates in the family** is acyclic.

The positive direction is immediate from the main theorem.

For the negative direction, if the family union contains a directed cycle, take a finite word containing the templates that contribute the cycle edges. Because every template contains the identity diagonal, every contributed cycle edge is present in the word product: all other positions may be traversed diagonally. The endpoint support therefore contains the cycle and has an alternative perfect matching.

Thus a single common order is also the exact all-finite-words certificate for a finite P021 direction-transition template family.

No novelty claim is made for Boolean relation composition itself; the result here is the P021 interpretation of that structure as persistence of forced direction identity.

## 10. First-failure semantics

Let

`U_r = Gamma_1 union ... union Gamma_r`.

Then the canonical endpoint identity survives through time `r` exactly while `U_r` remains acyclic.

Therefore the first horizon at which direction identity becomes support-ambiguous is exactly the first horizon at which the accumulated normalized ambiguity edges close a directed cycle.

This gives a finite, inspectable obstruction certificate rather than a scalar proxy:

`FIRST_IDENTITY_LOSS = FIRST_CROSS_TIME_AMBIGUITY_CYCLE`.

This must not be renamed physical focusing, caustic formation, curvature, or a GR observable without a separate P016-style semantics/validation task.

## 11. Deterministic finite verification

Checker:

`scripts/check_p021_multistep_direction_identity.py`

Exact local run before persistence:

`PASS`.

The checker enumerates every normalized square support with diagonal identity as its unique perfect matching through `n=4`.

Counts of such one-step supports are:

- `n=1`: 1;
- `n=2`: 3;
- `n=3`: 25;
- `n=4`: 543.

It then checks the common-order theorem on every ordered pair through `n=4`:

| n | ordered pairs | safe/common-order | unsafe/cross-time-cycle |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 |
| 2 | 9 | 7 | 2 |
| 3 | 625 | 289 | 336 |
| 4 | 294,849 | 63,487 | 231,362 |

For every pair it also verifies the proof inclusions

`union Gamma_r subseteq Gamma(C_2) subseteq transitive_closure(union Gamma_r)`.

The checker separately exhausts every ordered triple through `n=3`:

| n | ordered triples | safe/common-order | unsafe/cross-time-cycle |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 |
| 2 | 27 | 15 | 12 |
| 3 | 15,625 | 2,689 | 12,936 |

It freezes the minimal `n=2,h=2` counterexample and verifies the saturated-versus-filtered fine witness separation with identical one-step supports.

The pre-persistence exact checker-source digest is

`sha256:de7ca2d03b943e0c50c2a375e6803a1ceda1d52031265429717a50236519c36d`.

The finite enumeration is regression evidence; the theorem is the symbolic argument in Sections 4 and 7.

## 12. Prior-art / ownership audit

This result deliberately does not claim generic novelty for:

- perfect matchings;
- unique matching iff no alternating cycle;
- DAG/topological sorting;
- Boolean matrix / relation composition;
- relational witness joins.

Those are standard mathematics or already owned elsewhere in Enterprise Math. In particular, generic relation/support composition remains outside this P021-local result.

The P021-specific residue is:

1. normalize changing direction labels by the previously forced one-step matchings;
2. identify the union of normalized noncanonical support edges as the exact finite-horizon identity obstruction;
3. prove that a common topological order is necessary and sufficient for persistent canonical direction identity;
4. identify the same condition as the exact universal safety boundary for forgetting fine middle witness identity for this endpoint observable;
5. isolate the minimal cross-time counterexample and same-support witness-refinement split.

No new general Toolbox family is requested.

## 13. Frozen boundaries

The result does **not** say:

- one-step unique matching is compositionally sufficient by itself;
- Boolean class support equals exact fine witness composition in general;
- count matrices are composition-complete;
- middle witness identity may always be discarded;
- unique direction matching is a physical focusing scalar;
- P021 now owns generic quotient, relation, matching, or automata theory;
- this Researcher return has canonical/Foundation/Working-Truth status.

The old P021 witness-vs-cardinality negative result is preserved and sharpened: exact witness identity is unnecessary for this particular endpoint identity observable exactly in the common-order-safe regime, and remains potentially decisive outside it.

## 14. Driver recommendation

Driver review should audit four points:

1. the cumulative-matching normalization and label invariance;
2. the proof sandwich
   `union Gamma_r subseteq Gamma(C_h) subseteq TC(union Gamma_r)`;
3. the universal fine-witness safety theorem `I subseteq J_h subseteq C_h` plus join-saturated necessity construction;
4. ownership wording, so the P021-local semantic result does not duplicate generic A4/R015/P023 relation theory.

If accepted, the natural P021 continuation is no longer “does uniqueness compose?”; that question is closed. A later task should only be opened for a genuinely stronger declared observable, such as identity-sensitive multiplicity/provenance along the common-order-safe class regime, or for a separately typed physical/focusing interpretation behind the P016 validation boundary.
