# P018 — Finite-Precision Proof Calculus, Supplement 04

Status: `ACTIVE RESEARCH NOTE`  
Scope: abstract finite precision systems, ambiguity multiplicity, first-decision shells, and the partition-order relation between precision and time  
Depends on: P018 Stages 1–4 and P010/T012  
Discipline: inverse/projective systems, equivalence relations, and partition refinement are established mathematics. P018 does not claim those general structures as inventions.

## 1. Why the scale coordinate is no longer fundamental

P018 now has two genuinely different precision axes:

- **scale precision**, whose observations are Euclidean coarse states;
- **factor precision**, whose observations are visible divisor witnesses.

Their arithmetic details are different, but their proof structure is the same.

That common structure is more primitive than either coordinate.

Let `X` be one finite set of terminal states. A precision level `lambda` is represented by an observation

\[
O_\lambda:X\to Y_\lambda.
\]

Two terminal states are indistinguishable at precision `lambda` exactly when they have the same observation.

For `x in X`, define its precision fiber

\[
[x]_\lambda
=
\{y\in X:O_\lambda(y)=O_\lambda(x)\}.
\]

The observation induces a partition of `X` into these fibers.

No inverse limit, infinite terminal precision, metric, or hidden continuum is required.

## 2. P018-T35 — Abstract refinement criterion and projection map

Status: `PROVED`

Say that `mu` is finer than `lambda` when equality at the fine level implies equality at the coarse level:

\[
O_\mu(x)=O_\mu(y)
\Longrightarrow
O_\lambda(x)=O_\lambda(y).
\]

For finite observations this is equivalent to the existence of a unique map on the image of the fine observation,

\[
p_{\mu\to\lambda}:\operatorname{im}(O_\mu)\to\operatorname{im}(O_\lambda),
\]

such that

\[
\boxed{
O_\lambda
=
p_{\mu\to\lambda}\circ O_\mu.
}
\]

Proof: if a fine observation value is shared by several terminal states, the refinement condition guarantees that all of them have the same coarse observation; hence the projection is well-defined. Uniqueness follows because every value in `im(O_mu)` is represented by at least one terminal state. The converse is immediate from composition. ∎

This is the finite observation form of the compatible transition maps familiar from inverse/projective systems. P018 deliberately uses only the finite maps actually present in the problem.

## 3. P018-T36 — Precision fibers are nested

Status: `PROVED`

If `mu` refines `lambda`, then for every `x in X`,

\[
\boxed{
[x]_\mu\subseteq[x]_\lambda.
}
\]

Proof: if `y` is in the fine fiber, then `O_mu(y)=O_mu(x)`. Refinement implies `O_lambda(y)=O_lambda(x)`, so `y` lies in the coarse fiber. ∎

Thus precision refinement is exactly refinement of the observation partition.

## 4. P018-T37 — Ambiguity multiplicity is nonincreasing

Status: `PROVED`

Define the **ambiguity multiplicity** at precision `lambda` by

\[
A_\lambda(x)=|[x]_\lambda|.
\]

Then `mu` finer than `lambda` implies

\[
\boxed{
A_\mu(x)\le A_\lambda(x).
}
\]

This is the cardinal form of T36.

The quantity has a direct finite interpretation: it is the number of terminal states still compatible with the current observation.

No logarithm or probability is required.

## 5. P018-T38 — Exact strict-refinement criterion

Status: `PROVED`

For `mu` finer than `lambda`, the following are equivalent:

1. `A_mu(x) < A_lambda(x)`;
2. `[x]_mu` is a proper subset of `[x]_lambda`;
3. there exists `y in X` such that

\[
O_\lambda(y)=O_\lambda(x)
\]

but

\[
O_\mu(y)\ne O_\mu(x).
\]

So ambiguity decreases strictly exactly when the next precision observation actually **splits the current coarse fiber containing x**.

Global additional detail elsewhere in the state space is irrelevant to `x` if it does not split this particular fiber.

This is the precision-direction counterpart of P010's reachable-collision criterion for strict history merging.

## 6. P018-T39 — Ambiguity gains telescope

Status: `PROVED`

For a finite refinement chain

\[
\lambda_0\preceq\lambda_1\preceq\cdots\preceq\lambda_m,
\]

define

\[
g_i(x)=A_{\lambda_{i-1}}(x)-A_{\lambda_i}(x).
\]

Then

\[
\boxed{g_i(x)\ge0}
\]

and

\[
\boxed{
\sum_{i=1}^m g_i(x)
=A_{\lambda_0}(x)-A_{\lambda_m}(x).
}
\]

Thus ambiguity reduction itself has a finite shell decomposition by precision step.

A zero shell means the new level carries no distinguishing information for the current terminal state; a positive shell measures exactly how many previously compatible alternatives are removed.

## 7. P018-T40 — General predicate certificate persistence

Status: `PROVED`

Let

\[
P:X\to\{\text{true},\text{false}\}
\]

be any Boolean predicate.

At precision `lambda`, define the certificate for `x` by the predicate values on its whole fiber:

- `TRUE` if `P` is true on every state in `[x]_lambda`;
- `FALSE` if `P` is false on every state in `[x]_lambda`;
- `UNRESOLVED` otherwise.

If `mu` refines `lambda`, then a TRUE or FALSE certificate at `lambda` remains the same at `mu`.

Proof: the fine fiber is a subset of the coarse fiber by T36, so any predicate constant on the coarse fiber is constant with the same value on the fine fiber. ∎

This is the abstract version of Stage 3. It no longer requires order, monotonicity, intervals, or homogeneous operations.

The only required structure is nested finite fibers.

## 8. P018-T41 — First-decision precision shells partition the terminal set

Status: `PROVED`

Fix a finite refinement chain and a Boolean predicate `P`.

For each terminal state `x`, let

\[
d_P(x)
\]

be the first precision index at which the predicate certificate becomes TRUE or FALSE, if such a level exists.

Then the sets

\[
D_j(P)=\{x:d_P(x)=j\}
\]

and, if necessary, the terminal unresolved set

\[
D_\infty(P)=\{x:d_P(x)\text{ is undefined}\}
\]

form a disjoint partition of `X`.

These are **first-decision precision shells**.

T33's least-prime-factor shells are one arithmetic instance: the first decision index is the first factor precision at which a compositeness witness appears, while terminal primes decide at the finite completeness horizon.

## 9. P018-T42 — Finite injective terminal precision is universally complete

Status: `PROVED`

Suppose the final observation `O_*` is injective on `X`.

Then every terminal fiber is a singleton:

\[
\boxed{[x]_* = \{x\}.}
\]

Hence

\[
\boxed{A_*(x)=1}
\]

for every `x`, and for **every Boolean predicate** `P`, the terminal certificate is TRUE or FALSE rather than UNRESOLVED.

Therefore any finite precision system with an injective terminal observation has a finite universal decision horizon.

This is a foundational P018 boundary:

> proof completeness on a finite problem does not require an infinite precision limit; it requires only a finite precision level that distinguishes all terminal states relevant to that problem.

A weaker problem-specific terminal precision may decide one predicate even when the final observation is not injective, as factor precision does for primality on a square basin.

## 10. P018-T43 — Product precision fibers are intersections

Status: `PROVED`

Let two precision observations on the same finite terminal set be

\[
O_1:X\to Y_1,
\qquad
O_2:X\to Y_2.
\]

Define their product observation

\[
O_{1\times2}(x)=(O_1(x),O_2(x)).
\]

Then

\[
\boxed{
[x]_{1\times2}
=[x]_1\cap[x]_2.
}
\]

Therefore

\[
\boxed{
A_{1\times2}(x)
\le
\min\{A_1(x),A_2(x)\}.
}
\]

This gives an exact algebra for combining distinct precision axes.

In particular, scale precision and factor precision can be applied simultaneously without pretending they are the same kind of detail. Their joint information is simply the intersection of the two compatible terminal-state fibers.

This result points toward adaptive multi-axis proofs: refine whichever observation axis removes the most relevant ambiguity.

## 11. P018-T44 — Time and precision move oppositely in the same partition order

Status: `PROVED ORDER-THEORETIC RELATION`, **not a categorical duality claim**.

Every map

\[
f:X\to Y
\]

induces a kernel equivalence relation on `X` and therefore a partition

\[
\Pi(f).
\]

Order partitions by refinement: `P <= Q` means every block of `P` is contained in a block of `Q`.

### Precision direction

If `O_mu` refines `O_lambda`, then

\[
\boxed{
\Pi(O_\mu)\le\Pi(O_\lambda).
}
\]

Precision moves **downward toward finer partitions**. Ambiguity fibers split and their cardinalities are nonincreasing.

### Time direction

Let

\[
F_{t+1}=T_{t+1}\circ F_t.
\]

If two histories are already equal under `F_t`, they remain equal after postcomposition. Hence

\[
\boxed{
\Pi(F_t)\le\Pi(F_{t+1}).
}
\]

Time moves **upward toward coarser partitions**. History fibers merge and their cardinalities are nondecreasing, exactly as T012 and P010 state.

Thus precision refinement and deterministic forward time are opposite monotone motions on the same mathematical type of object: the partition lattice of a finite state set.

This is stronger than the earlier verbal analogy, but weaker than a categorical duality. No inverse functor, adjunction, or equivalence of categories has been proved.

The exact current statement is:

\[
\boxed{
\text{precision: partition refinement / ambiguity loss},
\qquad
\text{time: partition coarsening / history merging}.
}
\]

## 12. Two canonical examples

### 12.1 Scale precision

Fix a finite terminal scale `D`. For every divisor scale `d|D`, let

\[
O_d(x)=x//(D/d).
\]

If `d|e|D`, then `O_e` refines `O_d`, reproducing the Euclidean precision cells of Stages 1–3.

At `d=D`, the observation is the identity and is therefore injective, so T42 gives universal finite completeness on the chosen finite terminal domain.

### 12.2 Factor precision

On a fixed square basin, let

\[
O_y(n)=D_y(n).
\]

Increasing the cutoff refines the observation by adding visible divisibility witnesses. The terminal factor observation at `y=k` need not be injective, but Root-Factor Horizon guarantees that it is complete for the particular predicate “is prime?”.

This distinguishes two notions:

- **state completeness**: the observation is injective;
- **predicate completeness**: the observation need only separate the truth classes relevant to one predicate.

P018 proof design should seek the weaker predicate completeness whenever possible, because it may require substantially less precision.

## 13. Prior-art boundary

Compatible transition maps in inverse/projective systems are established category-theoretic language; equivalence relations, kernels of functions, and partition refinement are elementary established mathematics. P018 does not claim those objects or their lattice ordering as new.

The project-specific research package under test is the finite synthesis:

\[
\boxed{
\text{finite terminal state set}
+
\text{precision observations}
+
\text{compatible forgetting maps}
+
\text{ambiguity multiplicity}
+
\text{persistent predicate certificates}
+
\text{first-decision shells}
+
\text{multi-axis product precision}
+
\text{opposite partition motion under time}.
}
\]

Most importantly, the theory does **not** require passage to an inverse limit. A finite terminal observation or a finite predicate-complete horizon is enough for the theorems above.

Historical novelty of this synthesis remains `NOVELTY_UNVERIFIED`.

## 14. Stage-5 status

- P018-T35 abstract refinement / projection criterion: `PROVED`
- P018-T36 fiber nesting: `PROVED`
- P018-T37 ambiguity multiplicity monotonicity: `PROVED`
- P018-T38 strict ambiguity-drop criterion: `PROVED`
- P018-T39 telescoping ambiguity gains: `PROVED`
- P018-T40 arbitrary-predicate certificate persistence: `PROVED`
- P018-T41 first-decision shells: `PROVED`
- P018-T42 finite injective terminal completeness: `PROVED`
- P018-T43 product precision fiber intersection: `PROVED`
- P018-T44 precision/time opposite monotonicity on the partition order: `PROVED`
- categorical time/precision duality: `NOT CLAIMED / OPEN`
- adaptive optimal precision selection: `NEXT`
- nonmonotone multi-axis proof search: `OPEN`

Executable checks live in `src/enterprise_math/precision_system.py` and `tests/test_precision_system.py`.
