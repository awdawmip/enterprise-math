# Proper Witness Projection Preserves Profinite Exactness

Status: `RESEARCH BRIDGE / NONCANONICAL`

The finite-branch and witness-compactness results admit a more structural formulation. Existentially forgetting a witness preserves profinite exactness when the **witnessed relation is exact**, the **completed unlabelled semantics is still the same existential projection**, and the **witness projection is closed/proper**.

## 1. Exact witnessed relation

Let W be a compact Hausdorff witness space that is not itself changed by the arithmetic completion.

Let

`R_Z subseteq Z^n x W`

be the exact witnessed-state relation.

The exact unlabelled state set is

`S_Z = pi(R_Z)`

for the projection

`pi: Z^n x W -> Z^n`.

Examples include a finite labelled relation, where W is a finite discrete set.

## 2. Complete the witnessed relation before forgetting the witness

Embed the integer state into the profinite state space and suppose the completed witnessed relation satisfies

`R_hat = closure(R_Z) subseteq Z_hat^n x W`.

This is **joint profinite exactness** of the state+witness relation.

Separately require that the completed unlabelled world law is semantically still

`S_hat = pi(R_hat)`.

This is the **projection-faithfulness** condition. It says completion/coefficient collapse has not created unlabelled states outside all completed witness branches.

The coefficient ghost product fails precisely here: its completed product-zero set is larger than the projection of the completed finite factor-labelled relation.

## 3. Compact witness makes existential projection closed

Because W is compact and `Z_hat^n` is Hausdorff, the projection

`pi: Z_hat^n x W -> Z_hat^n`

is a closed map.

For any relation R:

- continuity gives
  `pi(closure(R)) subseteq closure(pi(R))`;
- closedness of pi gives the reverse inclusion because `pi(closure(R))` is closed and contains `pi(R)`.

Hence

`closure(pi(R)) = pi(closure(R))`.

This is the exact topological commutation law needed for existential witness elimination.

## 4. Proper-witness exactness theorem

Under the three hypotheses:

1. `R_hat=closure(R_Z)` — joint witnessed relation is profinite-exact;
2. `S_hat=pi(R_hat)` — completed unlabelled semantics is the same witness projection;
3. W compact — witness projection is closed/proper;

we obtain

`closure(S_Z)`

`= closure(pi(R_Z))`

`= pi(closure(R_Z))`

`= pi(R_hat)`

`= S_hat`.

Therefore the existentially quantified unlabelled law is itself profinite-exact.

## 5. Finite disjunction is the simplest corollary

For a finite branch set Lambda, take W=Lambda with the discrete topology.

W is compact automatically.

If each labelled branch is profinite-exact, the finite witnessed relation is profinite-exact. If the completed law remains the literal union of those branches, projection-faithfulness holds.

The theorem then recovers the finite-disjunction exactness result.

## 6. Three independent failure modes

The theorem locates three different ways existential descent can fail.

### A. Witnessed relation itself is not exact

A fixed nonlinear branch may have completion-only state solutions. Then

`R_hat != closure(R_Z)`.

This is the branch-level profinite ghost/descent failure.

### B. Unlabelled completion is not witness-faithful

The witnessed relation may be perfectly exact, but coefficient collapse can enlarge the unlabelled syntax.

The product ghost with finite factor labels is the sharp example: each fixed labelled factor has a local blocker, yet the completed product equation acquires mixed-component roots.

Then

`S_hat != pi(R_hat)`.

### C. Witness projection is not proper/closed

With a noncompact witness space, projection need not commute with closure. Witnesses can escape to infinity.

The infinite-label support

`S_M={k:M|k}`

is the discrete arithmetic pressure test: every finite precision has witnesses, but no fixed witness survives all precisions.

## 7. Relation to quantifier order

The topological theorem is the structural form of the quantifier exchange

`forall precision exists witness`

`=> exists coherent witness in the completion`.

Compact/proper witness projection is what prevents the existential witness from disappearing under the limit.

State descent from the completed witnessed relation back to exact integer states remains encoded in hypothesis1.

So the earlier two-stage routing can be compressed, when appropriate, into one exact commutative diagram:

`exact witnessed relation --closure--> completed witnessed relation`

`          | projection                 | projection`

`          v                            v`

`exact unlabelled set --closure--> completed unlabelled set`.

Profinite exact descent means this square commutes and its horizontal arrows introduce no ghost components.

## 8. Why the semantic projection hypothesis matters

One must not define the completed unlabelled law by reducing an algebraic encoding and then assume it equals the projection of the completed witnessed relation.

That equality is itself a theorem to be checked.

A product encoding of a finite union is faithful over an integral domain, but after coefficient collapse into a zero-divisor ring its zero set can become strictly larger than the branch projection.

Thus **semantic projection should be primary; algebraic encoding is secondary unless proven to preserve it.**

## 9. General witness spaces

Compactness is a clean sufficient condition, not the only possible one. More generally, what is needed is that the witness projection behave as a closed/proper map on the relevant completed relation.

A route-specific theorem may establish this without global compactness of every conceivable witness value.

The project should therefore record the weakest property actually used:

`projection of relevant closed witnessed-state sets remains closed`.

## 10. Prior-art boundary

Closed projections with compact fibers, proper maps, topological closure and existential projection are standard prior topology. The Enterprise Math value is the precision-routing theorem:

> **existentially forgetting a witness is safe through completion only when witnessed-state exactness, semantic projection faithfulness, and witness-projection properness are all preserved.**