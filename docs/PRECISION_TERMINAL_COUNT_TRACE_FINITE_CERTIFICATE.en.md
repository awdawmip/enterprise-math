# Finite Certificate for Infinite Terminal Path-Count Traces

Status: `RESEARCH BRIDGE / NONCANONICAL`

Exact natural terminal path-count traces can grow without bound along long words, but a fixed finite-state relation system still has a finite exact certificate.

The certificate uses **two resources**:

1. a finite word-depth bound from rational observability closure;
2. a finite coefficient modulus large enough to reflect all counts needed before that closure.

This differs sharply from exact count-branching state, whose coefficient cutoff depends only on one-step outdegree and needs no growing trace range.

## 1. Linear form of terminal path counts

Order the n states and represent each relation action a by its integer adjacency matrix

`A_a[target,source]=1[source R_a target]`.

For each current observation class, let C contain its indicator row.

For a literal word w, the terminal observation path-count rows are

`C A_w`

(up to the harmless convention of reversing written word order according to matrix composition).

Thus the entire terminal count language is an integer linear observation family on the initial basis-state vector.

## 2. Rational row-space closure

Let

`W_h = span_Q { C A_w : |w|<=h }`.

Then

`W_(h+1)=W_h + sum_a W_h A_a`.

If one horizon has

`dim W_(h+1)=dim W_h`,

then `W_h` is right-invariant under every action matrix, so no later word can increase the row space.

Hence one equal-rank step is a permanent rational stop certificate.

## 3. Universal finite word-depth bound

Observation-class indicator rows are linearly independent. If the current observation has `c_0` classes, then

`dim W_0=c_0`.

Every strict pre-stabilization horizon increases rational rank by at least one, while the ambient state dimension is n.

Therefore

`h_* <= n-c_0`.

So every exact infinite terminal trace distinction already has a witness word of length at most `n-c_0`.

This is the multi-relation weighted-automaton analogue of finite-dimensional observability closure.

## 4. The horizon bound can be sharp

Take an n-state deterministic countdown chain ending in one absorbing terminal state. Observe only

- terminal;
- nonterminal.

Then `c_0=2`.

Each additional future action reveals exactly one more distance-to-terminal layer. The rational row ranks are

`2,3,4,...,n`,

so stabilization occurs exactly at

`h_*=n-2=n-c_0`.

Thus the finite-depth theorem is not merely a loose dimension bound.

## 5. Exact infinite trace partition from the final row basis

Once the row space has stabilized, choose any rationally independent integer rows spanning it.

Two source states x,y have identical exact natural terminal traces for **every literal word** iff every basis row has the same x- and y-coordinate.

Therefore the infinite exact trace partition is computed directly from the final finite row basis.

The executable branch cross-checks this partition against literal exact path-count traces through the certified stabilization horizon.

## 6. Finite arithmetic certificate at the actual closure horizon

Let Delta be the maximum raw one-step outdegree.

A word of length k has at most

`Delta^k`

raw paths from one source. Therefore every terminal observation count needed through actual closure horizon `h_*` lies in

`[0,max(1,Delta^h_*)]`.

Any modulus

`M > max(1,Delta^h_*)`

is injective on all those exact count values.

Consequently:

`mod-M terminal traces through h_*`

have exactly the same state partition as

`all infinite exact natural terminal traces`.

This is a finite exact certificate of an infinite trace language.

## 7. Universal state-count-only certificate

Without first computing the actual closure horizon, use

`h_* <= n-c_0`.

A safe uniform modulus is therefore

`M > max(1,Delta^(n-c_0))`.

Together with word depth `n-c_0`, this certifies exact infinite terminal count equivalence for every relation system with the given finite state count, observation class count and outdegree bound.

This is a worst-case theorem bound, not necessarily a realized minimum.

## 8. Realized minimum modulus can be smaller

For one fixed world, a smaller modulus may induce the same exact state partition even if some individual path-count coefficients collide.

Only collisions that merge states which exact traces need to distinguish matter.

Because the theorem modulus is guaranteed to work, the branch searches finitely from modulus2 upward and returns the smallest modulus whose terminal trace partition through `h_*` equals the exact infinite partition.

Thus we distinguish:

- coefficient-value reflection bound;
- realized state-precision modulus.

The latter can be strictly smaller.

## 9. Fixed branching-versus-trace witness revisited

The earlier Delta=2 acyclic world has:

- exact count-branching cutoff mod3;
- exact terminal trace row-space stabilization at `h_*=2`;
- safe terminal coefficient cutoff mod5.

Exact terminal counts distinguish p/q by

`a^2: 4 versus 1`.

mod3 merges those values, so mod3 terminal traces are wrong even though mod3 branching state is already exact.

mod5 reflects both values and recovers the exact infinite terminal trace partition at horizon2.

Thus one fixed world displays:

`branching state exact at M=3`

while

`direct terminal trace certificate uses M=5`.

## 10. Structural memory can substitute for arithmetic range

The branching state recursively stores which successor behavioural types occur and how many one-step successors have each type.

Its local coefficients never exceed Delta.

Terminal traces erase that structure and accumulate path multiplicities across future steps. Their coefficient values can reach Delta^h before the finite-dimensional row space closes.

So recursive structural state can trade memory organization for smaller arithmetic range.

This is not a generic compression slogan; it is an exact theorem on the two declared interfaces.

## 11. Relation to the N-semimodule non-Noetherian boundary

The literal natural-count **reconstructive semimodule** can keep acquiring new positive generators forever, as shown by the earlier unipotent path-count example.

That does not contradict the present finite state-equivalence theorem.

Rational row-space closure asks only which initial states the entire count language can distinguish. The positive N-semimodule asks whether every future count row can be reconstructed by nonnegative integer combinations of a finite basis.

Therefore three notions remain separate:

- finite exact state-equivalence trace certificate;
- finite rational/integer-linear envelope;
- finite positive-semimodule reconstructive basis.

The first can be finite even when the third is infinite.

## 12. Prior-art boundary

Weighted automata equivalence, rational invariant subspaces, observability matrices and path-count bounds are standard prior mathematics/computer science. A4 retains relation/witness ownership; P023/A2 retains future-signature precision ownership.

The project value is the exact resource theorem:

> **a fixed finite relation system has a finite depth × finite modulus certificate for its infinite exact terminal path-count state partition, but the required arithmetic range can scale with trace depth while branching-state exactness needs only one-step outdegree precision.**