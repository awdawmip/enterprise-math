# P022 — Symmetry Quotients Turn Event Repair into Path-Lift Multiplicity

Status: `ACTIVE RESEARCH NOTE / GENERAL BRIDGE CANDIDATE / PRIOR-ART SENSITIVE`  
Owner of this specialization: `program/p022-geometry-v2`  
Potential mother-theorem homes: A2/P023 quotient safety, A4 count/equitability  
Prior art: group actions on graphs, equitable partitions, quotient/orbit graphs and path lifting are established mathematics

## 1. From event bits to a quotient-graph theorem

The Barlow two-sided repair theorem found two bit-producing events:

- leaving a zero boundary;
- splitting an equal absolute pair into unequal sides.

The exact fiber size was

\[
2^{E+B}.
\]

There is a more structural explanation.  The coordination observation is a symmetry quotient of the microscopic transition graph, and `E+B` is the base-two logarithm of the product of quotient-edge lift multiplicities.

## 2. Equitable transition quotient

Let `X` be a directed transition graph and let its vertices be partitioned into blocks.  Suppose the partition is **equitable** for outgoing transitions: for every source block `A`, target block `B`, and every two representatives `x,x' in A`,

\[
\#\{y\in B:x\to y\}
=
\#\{y\in B:x'\to y\}.
\]

Define the representative-independent edge multiplicity

\[
\boxed{
m(A,B)=\#\{y\in B:x\to y\}.}
\]

A group acting transitively on each block by graph automorphisms automatically gives this property, so orbit partitions are canonical examples.

## 3. P022-SQ01 — quotient-path lift product

Fix a microscopic start `x_0 in A_0` and a quotient path

\[
A_0\to A_1\to\cdots\to A_n.
\]

Every microscopic lift prefix ending at any vertex of `A_i` has exactly

\[
m(A_i,A_{i+1})
\]

valid continuations into `A_(i+1)`.  Induction therefore gives

\[
\boxed{
\#\{\text{microscopic lifts from fixed }x_0\}
=
\prod_{i=1}^{n}m(A_{i-1},A_i).
}
\]

If the initial microscopic state is itself unobserved inside an orbit, multiply additionally by the size of the admissible initial fiber.

This is established quotient/equitable graph mathematics; the project-specific role is the identification of finite repair with these integer lift multiplicities.

## 4. The Barlow microscopic symmetry

The two signed prefix drifts form

\[
(\delta^+,\delta^-)\in\mathbb Z^2
\]

with microscopic increments

\[
(\pm1,\pm1).
\]

The signed-permutation group

\[
\boxed{
G=(\mathbb Z_2)^2\rtimes S_2
}
\]

acts by changing the two signs and swapping the two channels.  It preserves the transition graph.

Its orbit is determined by the sorted absolute pair

\[
\boxed{
0\le a\le b,
}
\]

which is precisely the hidden state reconstructed by coordination history.

Thus the chamber `0<=a<=b` is not merely a convenient coordinate choice; it is a fundamental domain of the microscopic symmetry quotient.

## 5. P022-SQ02 — Barlow quotient-edge multiplicities

For a quotient edge

\[
(a,b)\to(c,d),
\]

the microscopic continuation multiplicity is always one of

\[
\boxed{1,2,4.}
\]

More precisely:

- every zero coordinate in `(a,b)` contributes one factor `2`, because leaving zero can choose either microscopic sign;
- if `a=b` and the successor is unequal, there is one additional factor `2`, because either labelled channel may take the larger absolute successor.

Hence

\[
\boxed{
m((a,b),(c,d))=2^{z+s},}
\]

where

\[
z=\mathbf1_{a=0}+\mathbf1_{b=0}
\]

and

\[
s=\mathbf1_{a=b,\ c\ne d}.
\]

The four cases are therefore:

- ordinary interior transition: `m=1`;
- one zero departure or one diagonal split: `m=2`;
- origin departure: `m=4`.

## 6. P022-SQ03 — event-repair theorem is the path-lift theorem

For one coordination history `P_0,...,P_N`, multiply the edge weights from SQ02:

\[
\prod_qm(P_{q-1},P_q)
=
2^{\sum_qz_q+\sum_qs_q}
=
2^{E+B}.
\]

By SQ01 this product is exactly the number of microscopic signed labelled word-pair lifts.

Therefore

\[
\boxed{
|O^{-1}(P)|=2^{E+B}
}
\]

is not an isolated combinatorial coincidence.  It is the orbit-path lift multiplicity of the symmetry quotient.

The repair bitstream simply indexes one lift among these microscopic branches.

## 7. Repair polynomial as a weighted quotient-path enumerator

The existing repair polynomial

\[
R_N(z)=\sum_hz^{r(h)}
\]

can now be read as a weighted quotient-path enumerator in which an edge of lift multiplicity

\[
2^c
\]

receives weight

\[
z^c.
\]

Then:

- `z=1` counts quotient paths;
- `z=2` replaces every edge weight by its microscopic lift multiplicity and reconstructs all microscopic paths;
- the derivative at `2` records lift-weighted repair load.

So the earlier repair polynomial is a symmetry-quotient path-lift polynomial.

## 8. Negative boundary — non-equitable partitions break the product state

The representative-independent edge weight is essential.

Take source block

\[
A=\{a_1,a_2\}
\]

and target block

\[
B=\{b_1,b_2\}
\]

with transitions

\[
a_1\to b_1,b_2
\]

but only

\[
a_2\to b_1.
\]

Then the same coarse edge `A->B` has microscopic continuation count `2` from `a_1` and `1` from `a_2`.

No quotient-edge multiplicity

\[
m(A,B)
\]

is well-defined.  A product of coarse edge weights therefore cannot represent exact future lift count.

This is the same structural boundary previously encountered in A4/A2 count-lumpability: **future count semantics descends only when the quotient is equitable for the transition algebra being queried.**

## 9. Cross-route consequence

The genuinely general statement is not specifically about Barlow geometry:

> For an equitable transition quotient, exact path-lift multiplicity factors locally through quotient-edge continuation counts; when the quotient is not equitable, representative identity remains future-relevant.

This should be audited against the existing A2/A4 equitability/lumpability work before any mother-theorem promotion.  P022 retains the signed-permutation/Barlow specialization and its discovery provenance.

## 10. Precision interpretation

The result supplies a sharper meaning of event-driven repair:

\[
\boxed{
\text{repair is required exactly on quotient edges with lift multiplicity }>1.
}
\]

Boundary events matter because the symmetry quotient ceases to have a unique microscopic continuation there.

The natural primitive quantity is the **integer branching multiplicity** `m`, not a logarithm.  In the Barlow case all multiplicities are powers of two, so one can equivalently count bits.

For more general quotients, non-power-of-two multiplicities should remain exact integer branch counts rather than being forced into real-valued information units.

## 11. Executable assets

- `src/enterprise_math/p022_symmetry_quotient_repair.py`;
- `tests/test_p022_symmetry_quotient_repair.py`.

The tests reconstruct Barlow short-horizon microscopic fibers from quotient-edge products, verify a generic equitable finite graph, and preserve an explicit non-equitable counterexample.
