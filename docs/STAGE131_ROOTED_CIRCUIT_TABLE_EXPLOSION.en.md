# Stage131 — Rooted-Circuit Table Explosion in a Binary AND Tree (Corrected v2)

Status: `RESEARCH BRIDGE / NONCANONICAL`

This v2 replay corrects the hand-copied height-3 width histogram and the premise-literal totals in the superseded WIP. The generating recurrence, circuit-count recurrence, and exponential separation theorem are unchanged.

## 1. Compositional basis versus one-round premise table

A height-h balanced binary AND tree has `L=2^h` leaves and only `L-1` local binary Horn rules. The complete rooted-circuit table for one root instead enumerates every inclusion-minimal seed set P, excluding the root itself, such that the local closure derives the root from P.

The two objects represent the same closure law but satisfy different presentation contracts:

- local basis: recursive composition;
- rooted-circuit table: every minimal one-round premise alternative.

## 2. Exact generating recurrence

Let `A_h(z)` count minimal ways to make a height-h node available, allowing the node itself as a one-atom seed. Then

`A_0(z)=z`,

`A_h(z)=z+A_(h-1)(z)^2`.

The rooted-circuit width polynomial excludes the direct root seed:

`P_h(z)=A_(h-1)(z)^2=A_h(z)-z`.

Coefficient `[z^m]P_h` is exactly the number of inclusion-minimal root premises of width m.

## 3. Correct small width polynomials

`P_1(z)=z^2`.

`P_2(z)=z^2+2z^3+z^4`.

The corrected height-3 polynomial is

`P_3(z)=z^2+2z^3+5z^4+6z^5+6z^6+4z^7+z^8`.

Its coefficients sum to25. Explicit premise-set enumeration through height4 agrees with the polynomial.

## 4. Exact circuit-count recurrence

Let `M_h=P_h(1)`. Then

`M_1=1`,

`M_h=(1+M_(h-1))^2`.

The first values are

`1, 4, 25, 676, 458329, 210066388900, ...`.

These counts were not affected by the corrected width histogram.

## 5. Every premise width occurs

Inductively, `A_(h-1)` has positive coefficients at every degree `1,...,2^(h-1)`. Its square therefore has positive coefficients at every degree

`2,...,2^h`.

So one root has minimal premise sets of every width from two immediate children through all leaves.

## 6. Exponential separation from the local basis

With `L=2^h` leaves and h>=2:

`2^(L/2) <= M_h < 2^(L-1)`.

Thus the root circuit table is exponential in leaf count while the compositional local basis is only `L-1` rules.

## 7. All internal rooted-circuit rules

A height-h tree has `2^(h-t)` nodes of height t, so the full internal circuit table contains

`C_h=sum_(t=1)^h 2^(h-t) M_t`.

Exact values include:

- h=3: 37 circuits versus7 basis rules;
- h=4: 750 versus15;
- h=5: 459829 versus31;
- h=6: 210067308558 versus63.

## 8. Correct premise-literal totals

Total premise-literal storage for the root is

`P_h'(1)`.

Correct values are:

- h=1: 2;
- h=2: 12;
- h=3: 130;
- h=4: 6812;
- h=5: 9224802.

At h=5 the root has458329 circuits and average premise width

`9224802/458329`, approximately20.13,

with widths spanning2..32.

## 9. Why the squaring explosion occurs

For each child subtree, a minimal root premise may either include the child atom itself or replace it by any minimal premise that derives that child. Left and right choices combine independently, producing the square recurrence.

Rooted-circuit enumeration therefore expands recursive composition into all minimal one-round alternatives.

## 10. Stage131 consequence

The negative boundary is stronger than unary transitive redundancy:

> a one-round minimal-premise table can be exponentially larger than a compositional semantic basis even when the closure law is tree-shaped.

This is also an execution resource. Every stored circuit gives one-round access from exactly that premise set.

The operational problem is selective materialization: which minimal-premise macros deserve storage under premise-width, depth, workload and continuation constraints?

## 11. Ownership / prior art

Horn closure, minimal generators, antichain enumeration and generating functions are standard prior mathematics/CS. The Enterprise Math contribution is the Stage131 presentation interpretation and exact balanced-AND-tree pressure test.

Owner-local assets:

- `stage131_rooted_circuit_table_explosion.py`;
- corrected recurrence/width/enumeration/storage tests;
- this bilingual v2 note.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.