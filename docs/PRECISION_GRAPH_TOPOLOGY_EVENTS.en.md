# Graph Topology Events as Precision Transfers

Status: `RESEARCH BRIDGE / NONCANONICAL`

This note is a corollary-level architectural companion to `PRECISION_GRAPH_EXACT_SEQUENCE.en.md`.  It adds no new graph theorem and does not compete with E001 topology-removal owners.

For a finite graph with fixed vertex count `V`, edge count `E`, component count `c`, and cycle rank

`beta=E-V+c`,

standard graph homology gives

`rank H_0=c`,
`rank H_1=beta`,

hence

`rank H_0 - rank H_1 = V-E`.

This equality can be read as an exact topology/precision ledger when one graph is used simultaneously to reason about edge-history fibers and vertex-ledger redistribution.

## Adding one edge

Exactly one of two cases occurs.

### Edge joins two previously disconnected components

`c -> c-1`, `beta` unchanged.

Precision interpretation:

- vertex-ledger side: one independent component-total invariant disappears because the new transfer path allows the two components to mix;
- edge-history side: no new cycle-history ambiguity is created.

### Edge lies inside one existing component

`c` unchanged, `beta -> beta+1`.

Precision interpretation:

- vertex-ledger side: component-total invariant rank is unchanged;
- edge-history side: one new independent cycle-history direction becomes invisible to the vertex incidence image.

## Removing one edge

The two cases reverse.

### Remove a bridge

`c -> c+1`, `beta` unchanged.

A new independent vertex-component total becomes policy-invariant, while no cycle-history direction is removed.

### Remove a non-bridge cycle edge

`c` unchanged, `beta -> beta-1`.

One hidden cycle-history direction disappears, while the vertex component-total invariant rank stays unchanged.

## Architecture consequence

A topology event should not be summarized only as “more connected” or “less connected”.  It changes different precision resources depending on whether the edge event acts across components or inside a component:

```text
bridge addition/removal
    <-> changes H0 / conserved component-ledger precision

cycle-edge addition/removal
    <-> changes H1 / hidden edge-history precision
```

If future laws also observe transfer-path history, then H1 of the **transfer** graph becomes relevant as hidden policy history even though ordinary vertex-ledger state only uses H0.  Thus the exact sequence provides one consistent place to add such future observables without confusing them with vertex component totals.

The identity above is standard Euler-characteristic graph theory.  The project value is only the precision interpretation and cross-routing between contact-history and material-ledger lines.
