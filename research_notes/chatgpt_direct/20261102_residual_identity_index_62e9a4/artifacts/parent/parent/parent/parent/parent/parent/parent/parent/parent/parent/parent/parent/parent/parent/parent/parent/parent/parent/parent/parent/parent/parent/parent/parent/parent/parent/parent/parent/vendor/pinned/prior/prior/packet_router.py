"""Typed positive-BRC packet circuit, not an admitted native material law.

A packet is a JOINT three-port payload. Its CWM weight is its total budget;
its three equal leg budgets sum to that budget. Different packet IDs remain
available. The default signed incidence is deliberately a permissive candidate,
not an inferred P000 force-incidence table. Unit path weights and routing shares
are declared circuit operations, not calibrated force/energy/probability.
"""
from __future__ import annotations
import ast
import hashlib
import sys
import types
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'sources/brc_weighted.py'
if not SOURCE.exists():
    SOURCE = ROOT.parents[2] / 'src/enterprise_math/brc_weighted.py'
RAW = SOURCE.read_bytes()
BLOB = hashlib.sha1(b'blob ' + str(len(RAW)).encode() + b'\0' + RAW).hexdigest()
if BLOB != '3f205696709e847909958a153f8fe10d3f6b70f0':
    raise RuntimeError('BRC source pin mismatch')
tree = ast.parse(RAW.decode())
removed = [n.module for n in tree.body if isinstance(n, ast.ImportFrom) and n.level]
if removed != ['brc_logarithm', 'exact_arithmetic']:
    raise RuntimeError('unexpected relative imports')
original = [ast.dump(n) for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
tree.body = [n for n in tree.body if not (isinstance(n, ast.ImportFrom) and n.level)]
if original != [ast.dump(n) for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))]:
    raise RuntimeError('BRC function/class AST changed')
brc = types.ModuleType('cell_u2_pinned_brc')
sys.modules[brc.__name__] = brc
exec(compile(tree, str(SOURCE), 'exec'), brc.__dict__)
CALLS = Counter()

def edge(weight):
    CALLS['cwm_edge'] += 1
    return brc.cwm_edge(weight)

def serial(a, b):
    CALLS['cwm_propagate'] += 1
    return brc.cwm_propagate(a, b)

def merge(a, b):
    CALLS['cwm_recoalesce'] += 1
    return brc.cwm_recoalesce(a, b)

def total(states):
    ans = brc.CWM_ZERO
    for value in states:
        ans = merge(ans, value)
    return ans

PORTS = tuple(range(12))
ZERO = (0,) * 6

def axis(p: int) -> int:
    if p not in PORTS:
        raise ValueError('port must be in 0..11')
    return p // 2

def direction(p: int) -> tuple[int, ...]:
    return tuple((1 if p % 2 == 0 else -1) if j == axis(p) else 0 for j in range(6))

def advance(z, p):
    if len(z) != 6 or not all(type(v) is int for v in z):
        raise ValueError('an X6 signed integer raw chart is required')
    return tuple(a + b for a, b in zip(z, direction(p)))

def triples_at(p: int):
    """All 40 candidate signed triples containing the actual incoming port."""
    i = axis(p)
    return tuple(tuple(sorted((p, 2*j+sj, 2*k+sk)))
                 for j, k in combinations([v for v in range(6) if v != i], 2)
                 for sj, sk in product(range(2), repeat=2))

@dataclass(frozen=True)
class Packet:
    tag: tuple
    born_at: tuple[int, ...]
    incoming: int
    ports: tuple[int, int, int]
    budget: object
    leg: object

    def paths(self):
        # Three separate one-step paths, NOT a three-edge spatial closed triangle.
        return tuple((self.born_at, advance(self.born_at, p)) for p in self.ports)

THIRD = edge(Q(1, 3))
UNIT = edge(Q(1))


def packets(incoming: int, state, tag=(), born_at=ZERO, incidence=None):
    """Positive response partition with source/parent/triple identity retained.

    A zero source creates no packets. Missing legal incidence is an error, not
    permission to invent a third force. Nonzero weights are divisible RESPONSE
    shares; no indivisible force-quantum realization is claimed.
    """
    axis(incoming)
    hs = tuple(triples_at(incoming) if incidence is None else incidence)
    if not hs:
        raise ValueError('no supplied anchored three-port incidence')
    if len(set(hs)) != len(hs):
        raise ValueError('duplicate incidence')
    for h in hs:
        if len(h) != 3 or incoming not in h or len({axis(p) for p in h}) != 3:
            raise ValueError('invalid three-distinct-axis incidence')
    if not state.live:
        return ()
    part = edge(Q(1, len(hs)))
    budget = serial(state, part)
    leg = serial(budget, THIRD)
    return tuple(Packet(tuple(tag)+(h,), born_at, incoming, h, budget, leg) for h in hs)


def marginals(ps):
    out = {p: brc.CWM_ZERO for p in PORTS}
    for packet in ps:
        for p in packet.ports:
            out[p] = merge(out[p], packet.leg)
    return out


def gate(ps, blocked):
    """All-or-none packet valve. Blocked packets are STORED, not cancelled."""
    blocked = frozenset(blocked)
    if not blocked <= set(PORTS):
        raise ValueError('invalid blocking port')
    ready, held = [], []
    for packet in ps:
        (held if blocked.intersection(packet.ports) else ready).append(packet)
    return tuple(ready), tuple(held)


def histogram(ps):
    """Exact CWM histogram sufficient for this source-blind packet-valve language."""
    h = {}
    for packet in ps:
        h[packet.ports] = merge(h.get(packet.ports, brc.CWM_ZERO), packet.budget)
    return h


def axis_totals(port_states):
    return tuple(total((port_states[2*j], port_states[2*j+1])).total for j in range(6))


def transport_tables(rho=Q(1, 4)):
    """Primitive-edge bulk propagation plus explicit material scattering.

    rho is relation-depth attenuation, not time. Bulk edges each weigh rho/12.
    Material edges include the ACTUAL packet-choice/leg multiplicities.
    """
    if not Q(0) < rho < Q(1):
        raise ValueError('requires 0 < rho < 1')
    attenuation = edge(rho)
    material = {}
    for p in PORTS:
        marginal = marginals(packets(p, brc.CWM_ONE, tag=('basis', p)))
        material[p] = tuple((q, serial(value, attenuation))
                            for q, value in marginal.items() if value.live)
    bulk_edge = edge(rho/12)
    bulk = tuple((q, bulk_edge) for q in PORTS)
    return material, bulk


def field_prefix(material_cells, depth=4, rho=Q(1, 4), check=None):
    """Exact finite BRC field/contact feedback, with material positions FIXED.

    A state key (source, z, incoming_port) is an exact quotient only for subsequent
    unary propagation by these same tables. The packet association is accessible
    at its emission and in its path grammar, not asserted recoverable from unary
    marginals. This is NOT material motion or a complete native heartbeat.
    """
    cells = tuple(tuple(z) for z in material_cells)
    if len(cells) != len(set(cells)) or depth < 0:
        raise ValueError('distinct material cells and nonnegative depth required')
    occupied = set(cells)
    mat, bulk = transport_tables(rho)
    seed = edge(Q(1, 12))
    layer = {(b, z, p): seed for b, z in enumerate(cells) for p in PORTS}
    layers = []
    for n in range(depth+1):
        value = total(layer.values())
        if check:
            check(value.total == len(cells)*rho**n, 'exact layer response conservation')
        self_returns = [total(v for (s,z,p),v in layer.items() if s==b and z==cells[b])
                        for b in range(len(cells))]
        local = {str(b): {str(p): total(v for (s,z,q),v in layer.items()
                                         if z==cells[b] and q==p)
                         for p in PORTS} for b in range(len(cells))}
        layers.append({'depth': n, 'states': len(layer), 'CWM': value,
                       'self_return': self_returns, 'material_ports': local})
        if n == depth:
            break
        nxt = {}
        for (source, z, p), state in layer.items():
            for q, transition in (mat[p] if z in occupied else bulk):
                zz = advance(z, q)
                key = (source, zz, q ^ 1)
                contribution = serial(state, transition)
                nxt[key] = merge(nxt.get(key, brc.CWM_ZERO), contribution)
        layer = nxt
    CALLS['one_state_recurrent_cwm'] += 1
    comparison = brc.one_state_recurrent_cwm([rho])
    tail = serial(edge(len(cells)), comparison.depth(depth+1)).total * comparison.total_mass_closure
    return {'cells': cells, 'depth': depth, 'rho': rho,
            'layers': layers, 'tail_total_bound': tail,
            'infinite_total_response': Q(len(cells), 1)/(1-rho)}


def to_json(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, brc.CWMState):
        return {'count': x.count, 'total': str(x.total), 'dominant': str(x.dominant)}
    if isinstance(x, dict):
        return {str(k): to_json(v) for k,v in x.items()}
    if isinstance(x, (tuple, list)):
        return [to_json(v) for v in x]
    return x
