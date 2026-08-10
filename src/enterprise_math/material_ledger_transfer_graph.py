"""Transfer-graph characterization of policy-invariant material ledgers.

The applied/queued/expired three-compartment theorem is one instance of a more
general finite conservation structure.

Let a ledger have named compartments ``V`` with integer contents ``ell_v``.  A
declared policy family permits whole-quantum transfers along a finite directed
edge set ``E``.  Moving ``d`` units along ``u->v`` changes the ledger by

    -d*e_u + d*e_v.

A scalar linear readout

    L_w(ell) = sum_v w_v ell_v

is invariant under every allowed transfer amount on every declared edge exactly
when

    w_u = w_v

for every transfer edge.  Equivalently, ``w`` is constant on each connected
component of the underlying transfer graph.

Therefore the space of independent scalar linear invariants has rank equal to
the number of transfer-graph connected components.  One canonical basis is the
component-total family

    H_C = sum_(v in C) ell_v.

For the material ledger ``P,Q,X``:

* scheduler edge ``P-Q`` only -> components ``{P,Q}``, ``{X}``, so canonical
  invariants are ``P+Q`` and ``X``;
* expiry edge ``Q-X`` only -> invariants ``P`` and ``Q+X``;
* both edges -> one connected component, so every fully policy-invariant scalar
  readout is a multiple of ``P+Q+X``;
* no transfer edges -> all three compartment coordinates are independently
  invariant.

This is standard graph-incidence linear algebra.  The project value is that a
material history observable can be classified directly from the declared policy
transfer graph: changing the allowed operation language changes the invariant
subspace, even when the stored ledger coordinates themselves are unchanged.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Iterable, Mapping, Sequence


Compartment = Hashable
TransferEdge = tuple[Compartment, Compartment]


def _compartments(values: Iterable[Compartment]) -> tuple[Compartment, ...]:
    result = tuple(values)
    if not result:
        raise ValueError("at least one ledger compartment is required")
    if len(set(result)) != len(result):
        raise ValueError("ledger compartment names must be unique")
    return result


def _edges(
    compartments: tuple[Compartment, ...],
    values: Iterable[TransferEdge],
) -> tuple[TransferEdge, ...]:
    allowed = set(compartments)
    result = tuple(values)
    for source, target in result:
        if source not in allowed or target not in allowed:
            raise ValueError("transfer edge references an undeclared compartment")
        if source == target:
            raise ValueError("self-transfer edges are algebraically null and must be omitted")
    return result


def transfer_graph_components(
    compartments: Iterable[Compartment],
    transfer_edges: Iterable[TransferEdge],
) -> tuple[frozenset[Compartment], ...]:
    """Connected components of the underlying undirected transfer graph."""
    vertices = _compartments(compartments)
    edges = _edges(vertices, transfer_edges)
    adjacency = {vertex: set() for vertex in vertices}
    for source, target in edges:
        adjacency[source].add(target)
        adjacency[target].add(source)

    unseen = set(vertices)
    components = []
    while unseen:
        root = next(iter(unseen))
        stack = [root]
        component = set()
        while stack:
            current = stack.pop()
            if current in component:
                continue
            component.add(current)
            unseen.discard(current)
            stack.extend(adjacency[current] - component)
        components.append(frozenset(component))
    return tuple(
        sorted(
            components,
            key=lambda component: tuple(sorted(map(repr, component))),
        )
    )


def scalar_weights_transfer_invariant(
    compartments: Iterable[Compartment],
    transfer_edges: Iterable[TransferEdge],
    weights: Mapping[Compartment, int],
) -> bool:
    """Exact edge-equality criterion for invariance under every declared transfer."""
    vertices = _compartments(compartments)
    edges = _edges(vertices, transfer_edges)
    if set(weights) != set(vertices):
        raise ValueError("weights must define exactly one integer per compartment")
    for value in weights.values():
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("ledger weights must be integers")
    return all(weights[source] == weights[target] for source, target in edges)


def weights_constant_on_transfer_components(
    compartments: Iterable[Compartment],
    transfer_edges: Iterable[TransferEdge],
    weights: Mapping[Compartment, int],
) -> bool:
    """Equivalent connected-component form of the transfer-edge criterion."""
    vertices = _compartments(compartments)
    edges = _edges(vertices, transfer_edges)
    if set(weights) != set(vertices):
        raise ValueError("weights must define exactly one integer per compartment")
    for value in weights.values():
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("ledger weights must be integers")
    return all(
        len({weights[vertex] for vertex in component}) == 1
        for component in transfer_graph_components(vertices, edges)
    )


def component_total_signature(
    compartments: Iterable[Compartment],
    transfer_edges: Iterable[TransferEdge],
    ledger: Mapping[Compartment, int],
) -> tuple[int, ...]:
    """Canonical basis of linear invariants: total content in each transfer component."""
    vertices = _compartments(compartments)
    edges = _edges(vertices, transfer_edges)
    if set(ledger) != set(vertices):
        raise ValueError("ledger must define exactly one value per compartment")
    for value in ledger.values():
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("ledger contents must be nonnegative integers")
    return tuple(
        sum(ledger[vertex] for vertex in component)
        for component in transfer_graph_components(vertices, edges)
    )


def apply_ledger_transfer(
    compartments: Iterable[Compartment],
    transfer_edges: Iterable[TransferEdge],
    ledger: Mapping[Compartment, int],
    edge: TransferEdge,
    amount: int,
) -> dict[Compartment, int]:
    """Apply one allowed whole-quantum transfer and preserve component totals."""
    vertices = _compartments(compartments)
    edges = _edges(vertices, transfer_edges)
    if edge not in edges:
        raise ValueError("edge is not in the declared transfer family")
    if set(ledger) != set(vertices):
        raise ValueError("ledger must define exactly one value per compartment")
    if isinstance(amount, bool) or not isinstance(amount, int):
        raise TypeError("transfer amount must be an integer")
    if amount < 0:
        raise ValueError("transfer amount must be nonnegative")
    result = dict(ledger)
    source, target = edge
    if result[source] < amount:
        raise ValueError("transfer amount exceeds source compartment")
    before_signature = component_total_signature(vertices, edges, result)
    result[source] -= amount
    result[target] += amount
    after_signature = component_total_signature(vertices, edges, result)
    if after_signature != before_signature:
        raise AssertionError("allowed transfer changed component-total invariant")
    return result


@dataclass(frozen=True)
class LedgerTransferInvariantReport:
    components: tuple[frozenset[Compartment], ...]
    independent_linear_invariant_rank: int
    weights_edge_invariant: bool
    weights_component_constant: bool


def ledger_transfer_invariant_report(
    compartments: Iterable[Compartment],
    transfer_edges: Iterable[TransferEdge],
    weights: Mapping[Compartment, int],
) -> LedgerTransferInvariantReport:
    vertices = _compartments(compartments)
    edges = _edges(vertices, transfer_edges)
    components = transfer_graph_components(vertices, edges)
    edge_check = scalar_weights_transfer_invariant(vertices, edges, weights)
    component_check = weights_constant_on_transfer_components(
        vertices,
        edges,
        weights,
    )
    if edge_check != component_check:
        raise AssertionError("edge and connected-component invariance criteria disagree")
    return LedgerTransferInvariantReport(
        components=components,
        independent_linear_invariant_rank=len(components),
        weights_edge_invariant=edge_check,
        weights_component_constant=component_check,
    )
