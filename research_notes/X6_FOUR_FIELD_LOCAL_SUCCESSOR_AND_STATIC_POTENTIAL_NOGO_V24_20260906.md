# X6 upper V24: four-field local successor capacity and a static-potential holonomy no-go

Status: `FREE_RESEARCH / EXACT FINITE CAPACITY THEOREM + GENERAL DYNAMICAL NO-GO / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`, `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_FOUR_FIELD_ACTIVE_TRIAD_CODE_V23_20260906.md`;
- `X6_PURE_TRIADIC_FIELD_COUPLING_V20_20260906.md`;
- `X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md`;
- BRC / Joint Relation Observer Preservation.
Checker: `experiments/x6_dynamic_law_holonomy_v24_20260906/check_dynamic_law_holonomy.py`.

## 1. Question

V23 proves that four labeled minimal pure-triadic fields are necessary and sufficient, within the current 30-state minimal field orbit, to identify all twenty active three-axis subsets from their field readings.

A weaker but more directly dynamical question is:

> how many such fields are needed so that, for every current active triad `S`, the nine adjacent candidates `T~S` in `J(6,3)` already have pairwise distinct context signatures?

This is the minimum observer capacity needed even to rank all next-step branches without endpoint collision.

A second question is then unavoidable:

> if the nine candidates can be distinguished, is a static destination-potential rule enough to generate the nontrivial active-frame holonomy of V17?

The answers are: four fields are again minimal, but every fixed destination-potential law is holonomy-flat at recurrent scale.

## 2. Local successor code

Let the 30 oriented minimal fields be

`H_min={+v_M,-v_M : M a perfect matching of K6}`.

For a labeled field set

`H=(h_1,...,h_r)`

define the reading code

`Code_H(T)=(h_1(T),...,h_r(T))`.

For a current active triad `S`, let

`N(S)={T: |S intersect T|=2}`.

`|N(S)|=3*3=9`.

Call H **locally successor-separating** iff, for every S, the restriction

`Code_H | N(S)`

is injective.

This is weaker than V23 global injectivity on all twenty triads.

## 3. Exact minimum is again four fields

Exhaustive exact enumeration over the 30 oriented minimal fields gives:

- r=1: 0 locally successor-separating field sets;
- r=2: 0;
- r=3: 0;
- r=4: exactly 13,440 unordered four-field sets.

Therefore

`MINIMAL MINIMAL-TRADE FIELD COUNT FOR ALL-STATE LOCAL SUCCESSOR SEPARATION = 4`.

The V23 globally injective four-field sets form a strict subset:

- 480 four-field sets globally identify all 20 triads;
- every globally injective set is locally successor-separating;
- 12,960 additional four-field sets separate every nine-neighbor fiber without globally identifying all twenty states.

Thus the local dynamical capacity threshold and the global object-identification threshold have the same minimum arity but different admissible families.

## 4. Exact scalarization once source-specific couplings are admitted

Suppose four source fields H are locally successor-separating and their source identities remain typed.

Choose four positive rational coupling bases with independent prime valuations, for example

`p=(2,3,5,7)`.

Define the exact positive-rational candidate weight

`W_H(T)=product_a p_a^(h_a(T))`.

Because prime valuations recover the full exponent vector `Code_H(T)`, distinct field signatures have distinct rational weights.

Hence, on every N(S), all nine branch weights are distinct and a unique dominant branch exists.

This is a valid exact Weighted-BRC scalarization of the labeled source code. It is **not** derived from P000: the source-specific coupling bases are additional dynamical/calibration data.

The result separates two issues cleanly:

`FOUR FIELDS -> ENOUGH INFORMATION TO DISTINGUISH BRANCHES`,

but

`SOURCE COUPLINGS / LAW -> NEEDED TO RANK THEM`.

## 5. General theorem: fixed destination potentials cannot generate cycles of length >=3

Let G be any finite simple undirected graph and let

`V:Vertices(G)->R`

be any scalar potential.

Assume a deterministic update chooses the unique maximizing neighbor:

`f(x)=unique argmax_{y~x} V(y)`.

Claim: f has no directed periodic orbit of length `m>=3`.

Proof. Suppose

`x_0 -> x_1 -> ... -> x_{m-1} -> x_0`

is such a cycle.

At each x_i, both x_{i-1} and x_{i+1} are distinct neighbors. Unique maximization gives

`V(x_{i+1}) > V(x_{i-1})`.

Summing these m strict inequalities yields

`sum_i V(x_{i+1}) > sum_i V(x_{i-1})`,

but the two sums are the same cyclic sum. Contradiction.

Therefore every recurrent cycle of such a deterministic potential update has length at most two.

## 6. Consequence for active-triad holonomy

Apply the theorem to the Johnson graph `J(6,3)`.

A one-edge active-triad transition followed immediately by its inverse is a two-cycle. Under the V17 shared-axis replacement connection, the backward transport is the inverse of the forward transport, so every two-cycle has identity S3 holonomy.

There are no self-loop active-triad replacements in the declared graph.

Hence every recurrent orbit of a unique static destination-potential update has

`ACTIVE_FRAME_HOLONOMY = identity`,

and therefore

`ORI6_CHARGE = 0`.

So **no fixed destination-potential law can generate the V17 nontrivial holonomy control**, regardless of whether its potential came from one field, four fields, a nonlinear scalarization, or any other static vertex score.

This strictly generalizes the V21 observation that one static minimal destination field has no aggregate flat/curved triangle bias.

## 7. Source-neutral separable response also fails before the global no-go

For the explicit V23 four-field identity code, consider the same-type source-neutral separable family

`Phi_f(S,T)=sum_a f(h_a(S))*h_a(T)`

where the same response function f is used for all four source slots.

For each of the eight active triads whose four-field code has exactly one nonzero coordinate, the nine neighbors collapse into three score classes of cardinality three for **every** f.

Thus no such source-neutral separable response can even define a unique total successor, before the static-potential cycle no-go is invoked.

This gives a concrete observer witness that labeled source context or additional edge/history data is operationally meaningful.

## 8. What type of law is now forced

To produce a recurrent active-triad loop with nontrivial V17 holonomy, the transition score cannot be only a function of the destination state.

At least one of the following must enter:

- an edge-sensitive coupling `A(S,T)` not reducible to a destination potential;
- changing/time-dependent context fields;
- incoming-edge / active-frame memory;
- path/holonomy state;
- another explicitly declared relational datum.

The next stage tests the smallest exact edge-sensitive extension of the four-field code.

No claim is made that nature uses the prime scalarization, a max rule, or any particular field law. The theorem only identifies the information threshold and rules out the entire static destination-potential class as a generator of nontrivial active-frame holonomy.
