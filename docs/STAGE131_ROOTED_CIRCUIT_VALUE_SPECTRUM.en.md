# Stage131 — Rooted-Circuit Materialization Value Spectrum

Status: `RESEARCH BRIDGE / NONCANONICAL`

The corrected rooted-circuit explosion theorem counts how many one-round minimal premise sets exist. Selective materialization needs one more coordinate: how many rounds does each premise set already need under the compositional local Horn basis?

That base derivation depth is the circuit's direct execution value.

## 1. Base depth of a rooted-circuit premise

For an inclusion-minimal premise set P of the root, let

`d(P)`

be the earliest synchronous round at which the local Horn basis derives the root from P.

If the exact rooted-circuit rule

`P=>root`

is materialized, that exact query becomes one round.

So its direct round saving is

`d(P)-1`.

Circuits of the same premise width can have different base depth, and circuits of the same base depth can have many widths. Width and execution value are therefore separate coordinates.

## 2. Joint width/depth recurrence

Let `A_h(m,d)` count minimal ways to make a height-h node available with premise width m and base derivation depth d, allowing the node itself as a direct seed.

At height0:

`A_0(1,0)=1`.

At each internal node:

- direct node seed contributes `(1,0)`;
- choosing one minimal availability set for each child combines as

`m=m_left+m_right`,

`d=1+max(d_left,d_right)`.

The rooted-circuit spectrum for the root is the derived part only, excluding `(1,0)`.

This is the width/depth refinement of the corrected generating recurrence `A_h(z)=z+A_(h-1)(z)^2`.

## 3. Correct height-3 joint spectrum

For height3 the exact nonzero `(width,depth):count` entries are

- `(2,1):1`;
- `(3,2):2`;
- `(4,2):1`;
- `(4,3):4`;
- `(5,3):6`;
- `(6,3):6`;
- `(7,3):4`;
- `(8,3):1`.

The width marginal is therefore the corrected polynomial

`z^2+2z^3+5z^4+6z^5+6z^6+4z^7+z^8`.

## 4. Host-height invariance of cumulative depth counts

Fix a host tree height h and a depth threshold d<=h.

A root premise derivable within d rounds can only descend through at most d levels of recursive Horn composition before every remaining required subtree root must be supplied directly as a seed.

The resulting combinatorics is exactly the same as the complete rooted-circuit table of a standalone height-d tree.

Hence

`# {P : d(P)<=d} = M_d`,

independent of h once h>=d.

The executable layer verifies this against the joint recurrence through multiple heights.

## 5. Exact depth-d circuit count

Let `M_0=0`. Then

`N_d=# {P:d(P)=d}=M_d-M_(d-1)`.

The first depth counts are therefore

- d1:1;
- d2:3;
- d3:21;
- d4:651;
- d5:457653;
- and so on.

The rapid explosion is concentrated in the deepest materialization class.

## 6. Height-5 opportunity distribution

The height5 root has458329 circuits total.

Depth counts:

`1,3,21,651,457653`.

Thus the depth5 class alone is

`457653/458329 > 0.99`

of all root circuits.

Every circuit in that class converts a five-round local-basis root derivation into a one-round materialized rule, saving four rounds for its exact premise query.

So complete rooted-circuit storage is dominated by a huge population of high-speedup candidates.

## 7. Width support at exact base depth

For every d>=1, rooted circuits with exact base depth d occur at every width

`d+1, d+2, ..., 2^d`.

This interval is also host-height invariant for h>=d.

Examples:

- depth1: width2 only;
- depth2: widths3..4;
- depth3: widths4..8;
- depth5: widths6..32.

So a high-value depth class still contains a wide storage/fan-in spectrum.

## 8. Why minimum width is d+1

To require d synchronous local rounds, at least one child subtree must itself require d-1 rounds. The opposite child must still contribute at least one seed atom.

Inductively this gives minimum width

`(minimum width at depth d-1)+1=d+1`.

## 9. Why maximum width is 2^d

A d-round derivation can expand at most d binary Horn levels before reaching explicit seed atoms. The complete depth-d leaf frontier has `2^d` premises and attains the maximum.

Intermediate mixtures of direct internal-node seeds and expanded subtrees realize every width between the two bounds.

## 10. Materialization value is not monotone in width

One might try to rank circuits by narrow premise width, but width alone is not execution value.

For example, depth5 circuits exist already at width6 and also at width32. Both save four rounds if their exact premise set occurs.

Conversely, a wide circuit at smaller base depth can save fewer rounds.

Hence selective caching must consider at least

`premise width x base depth x workload frequency`.

## 11. Candidate-level value model

For a circuit premise P with workload/query frequency `f(P)`, the simplest independent-query gross execution benefit is

`f(P) * (d(P)-1)`.

A storage model might charge by

- one rule;
- premise width `|P|`;
- premise-literal matching cost;
- or a hardware-specific fan-in cost.

This gives a first candidate score, but it is not yet a global optimizer because several materialized circuits can interact through the reusable closure state.

## 12. Why complete materialization is usually unreasonable

At height5, there are458329 root circuits for only32 leaves and31 local basis rules. More than99% lie in the deepest value class.

Materializing every high-saving circuit therefore remains impossible under ordinary storage budgets.

The value spectrum tells us where the opportunity lies but also proves the need for selective compilation.

## 13. Toward a selective circuit compiler

The next exact optimization problem can be stated as:

choose a subset of rooted-circuit macros under constraints on

- total rules;
- total premise literals;
- maximum fan-in;
- workload frequency;
- answer depth;
- reusable full-closure depth.

For independent one-shot root queries this begins as a knapsack-like selection problem. For reusable closure, circuit interactions make the objective nonadditive and require literal derivation simulation or proof-DAG structure.

## 14. Stage131 interpretation

The complete rooted-circuit table is a maximal one-round cache of all minimal premise alternatives.

The width/depth spectrum turns that monolithic table into an opportunity distribution:

- some circuits are cheap but save little;
- some are narrow and save many rounds;
- an enormous deep class offers large speedup but overwhelming aggregate storage.

This is the right input for selective materialization rather than blanket acceptance or blanket deletion of rooted circuits.

## Owner-local assets

- `stage131_rooted_circuit_value_spectrum.py`;
- corrected width/depth spectrum tests;
- `STAGE131_ROOTED_CIRCUIT_VALUE_SPECTRUM.{en,zh}.md`.

## Prior art / status

Horn proof depth, minimal generators and generating-function refinements are standard prior mathematics/CS. The Enterprise Math value is the Stage131 materialization-value interpretation and exact host-height-invariant depth spectrum.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.