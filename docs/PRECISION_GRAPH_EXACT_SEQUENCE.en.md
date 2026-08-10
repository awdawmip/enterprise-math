# Graph Exact-Sequence Bridge for Precision State

Status: `RESEARCH BRIDGE / NONCANONICAL`  
Purpose: expose one standard graph-chain structure that simultaneously explains hidden contact-cycle history and conserved ledger-component totals.

## 1. One boundary operator, two precision roles

For a finite oriented graph `G`, let

`C_1(G;Z)=Z^E`

be the integer edge/event lattice and

`C_0(G;Z)=Z^V`

be the integer vertex/state-compartment lattice.  The signed incidence/boundary map is

`partial = B : C_1 -> C_0`.

Because an ordinary graph has no 2-cells, there is the standard exact sequence

`0 -> H_1(G;Z) -> C_1 --B--> C_0 -> H_0(G;Z) -> 0`.

For a graph with `c` connected components and cycle rank `beta=E-V+c`:

`H_1(G;Z) ~= Z^beta`,

`H_0(G;Z) ~= Z^c`.

This one sequence appears in two different Enterprise Math precision roles.

## 2. Edge history observed through vertices: H1 is hidden history

Suppose an integer edge history/impulse vector is `j in C_1` and the coarse body/vertex change is

`b=Bj`.

Two edge histories give the same coarse state exactly when their difference lies in

`ker_Z B = H_1(G;Z)`.

Thus first homology is the free hidden-history fiber of the edge->vertex observation.

This is the contact-network result behind cycle allocation ambiguity:

- forest -> `H_1=0`, so delivered edge history is identifiable from its incidence image;
- one cycle -> one free hidden circulation coordinate;
- general graph -> `beta` independent integer cycle-history directions.

A declared future witness `Cj` only needs repair on the image `C(H_1)`; coboundary witnesses kill H1 and telescope to vertex state.

## 3. Vertex ledger modulo internal transfers: H0 is the invariant coarse ledger

Now put the stored quantity on **vertices/compartments** instead.  An allowed internal transfer along an edge changes the vertex ledger by one incidence column, i.e. by an element of

`im_Z B`.

Therefore two vertex ledgers are equivalent under the group-completed internal-transfer language exactly when their difference lies in `im B`.

The quotient is

`C_0 / im B = H_0(G;Z)`.

So zeroth homology is the additive policy-invariant ledger state: one total per connected transfer component.

This is the abstract form of the applied/queued/expired transfer result:

- connected transfer graph -> only total content survives as an independent linear invariant;
- `c` transfer components -> `c` independent component totals.

## 4. Kernel and cokernel are not interchangeable

The same incidence map therefore gives two opposite precision questions:

```text
edge/event state --B--> vertex/body state
    hidden ambiguity = ker B = H1

vertex/ledger state modulo edge transfers
    invariant quotient = coker B = H0
```

The first asks:

> Which fine edge histories are invisible after projection to vertices?

The second asks:

> Which vertex-ledger quantities survive all allowed internal redistributions?

They use the same graph but live on opposite sides of the boundary map.

## 5. Why graph homology itself does not explain the observed torsion

For an ordinary finite graph, both `H_1(G;Z)` and `H_0(G;Z)` are free abelian.  The graph-chain exact sequence therefore explains free cycle ambiguity and free component totals, but **not** the finite torsion found elsewhere in the project.

Finite quantization/reachability torsion appears after forming additional integer lattice operators, for example:

`K = B^T D B`

for weighted contact coupling, or

`L = B B^T`

for the graph Laplacian / potential representation problem.

These second-order maps can have nontrivial finite cokernels / critical groups even though the underlying graph homology is torsion-free.

Hence the architecture should separate:

- **free topology from the chain complex** — H1 hidden cycles, H0 component totals;
- **integer quantization obstruction from induced lattice operators** — Gram/Laplacian cokernel torsion, Smith factors, critical-group denominators.

This is the graph-specialized form of the broader project rule:

`kernel/free homology -> ambiguity/history`,

`induced integer cokernel/torsion -> reachability/representation obstruction`.

## 6. Future policy families

If the future may switch among several transfer graphs, no single `H_0(G_i)` necessarily gives the minimal current additive state.  The correct joint future observation is obtained by stacking all future component-total maps.

Its hidden ledger difference lattice is

`intersection_i im B_i`,

which is the kernel of the joint component-sum observation matrix.

This is why the simple meet of pairwise connectivity partitions is only a safe combinatorial upper bound for an additive ledger: intersections of incidence images can contain balanced multi-compartment directions that no pairwise compartment identification captures.

## 7. Status / prior art

Graph homology, incidence exact sequences, Laplacians and critical groups are standard prior mathematics.  This note makes no novelty claim for the sequence.  Its project value is architectural: it identifies two previously separate precision mechanisms as the kernel and cokernel sides of the same boundary operator, while locating finite torsion in the induced integer operators rather than in graph homology itself.
