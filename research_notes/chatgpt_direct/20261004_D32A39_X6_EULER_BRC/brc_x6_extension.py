"""Provisional provenance-retaining X6 observer extension of positive Weighted-BRC.

Model actions T/U are coordinate automorphisms, NOT native force/heartbeat laws.
The source CWM function bodies are loaded unchanged after full blob validation.
No floating-point, trigonometric, exponential, or external reference run is used.
See NOTE.md for the carrier, composition proof, observer scope and limitations.
"""
from __future__ import annotations
import ast
from dataclasses import dataclass, replace
from fractions import Fraction
import hashlib
from pathlib import Path
import sys
import types
from typing import Iterable

SOURCE_COMMIT = '165a57caf1050267ea8579ca82d384616341ac55'
SOURCE_BLOB = '3f205696709e847909958a153f8fe10d3f6b70f0'
SOURCE_PATH = 'src/enterprise_math/brc_weighted.py'
SOURCE_LOCAL = Path(__file__).parent / 'source/brc_weighted.py'
source_bytes = SOURCE_LOCAL.read_bytes()
assert hashlib.sha1(b'blob ' + str(len(source_bytes)).encode() + b'\0' + source_bytes).hexdigest() == SOURCE_BLOB

# Only the unmodified, dependency-closed positive CWM core is executed.
# Unused LN/DivisionExpr interfaces are not loaded or stubbed.
core_names = {'_fraction', '_positive_fraction', 'CWMState', 'cwm_edge',
              'cwm_recoalesce', 'cwm_propagate', 'cwm_from_positive_weights',
              'is_positive_path_realizable', 'boolean_support', 'effective_multiplicity'}
tree = ast.parse(source_bytes.decode('utf-8'))
selected = []
for node in tree.body:
    if isinstance(node, ast.ImportFrom) and node.level == 0:
        selected.append(node)
    elif isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in core_names:
        selected.append(node)
    elif isinstance(node, ast.Assign):
        names = {x.id for x in node.targets if isinstance(x, ast.Name)}
        if names & {'RationalInput', 'Target', 'CWM_ZERO', 'CWM_ONE'}:
            selected.append(node)
core_module = types.ModuleType('verified_source_cwm_core')
sys.modules[core_module.__name__] = core_module
exec(compile(ast.Module(body=selected, type_ignores=[]), str(SOURCE_LOCAL), 'exec'), core_module.__dict__)
CWM = core_module
CALL_COUNTS = {'cwm_edge': 0, 'cwm_propagate': 0, 'cwm_recoalesce': 0}

def call(name, *args):
    CALL_COUNTS[name] += 1
    return getattr(CWM, name)(*args)

Raw6 = tuple[int, int, int, int, int, int]
Coeff4 = tuple[int, int, int, int]

def raw6(values) -> Raw6:
    out = tuple(values)
    if len(out) != 6 or any(type(v) is not int for v in out):
        raise ValueError('X6 raw chart requires exactly six signed integers')
    return out

@dataclass(frozen=True)
class Branch:
    source_id: str
    x: Raw6
    cwm: object
    operation_history: tuple[str, ...] = ()
    def __post_init__(self):
        if not isinstance(self.source_id, str) or not self.source_id:
            raise ValueError('explicit nonempty provenance ID required')
        raw6(self.x)
        if not isinstance(self.cwm, CWM.CWMState) or self.cwm.count != 1:
            raise ValueError('one supported positive path per retained branch')
        if not CWM.is_positive_path_realizable(self.cwm):
            raise ValueError('invalid positive path weight')


def branch(source_id: str, x, weight=1) -> Branch:
    return Branch(source_id, raw6(x), call('cwm_edge', weight))


def transform(b: Branch, operation: str, edge_weight=1) -> Branch:
    """Serial BRC edge; retain source, raw label and complete operation word."""
    a = b.x
    if operation == 'T':
        x = (-a[5], a[0], a[1], a[2], a[3], a[4])
    elif operation == 'U':
        x = (a[0], a[1], a[2], a[3], -a[4], -a[5])
    else:
        raise ValueError('declared action alphabet is exactly {T,U}')
    return Branch(b.source_id, x,
                  call('cwm_propagate', b.cwm, call('cwm_edge', edge_weight)),
                  b.operation_history + (operation,))


def alternatives(*families: Iterable[Branch]) -> tuple[Branch, ...]:
    """Disjoint alternative composition; no source identity is discarded."""
    result = tuple(b for family in families for b in family)
    if len({b.source_id for b in result}) != len(result):
        raise ValueError('alternative branches require distinct IDs')
    return result


def positive_summary(family: Iterable[Branch]):
    state = CWM.CWM_ZERO
    for b in family:
        state = call('cwm_recoalesce', state, b.cwm)
    return state


def c12(b: Branch) -> Coeff4:
    """f(alpha), alpha^4-alpha^2+1=0, with coefficients retained exactly."""
    a = b.x
    return a[0]-a[4], a[1]-a[5], a[2]+a[4], a[3]+a[5]


def c4(b: Branch) -> tuple[int, int]:
    """f(beta), beta^2=-1; this is a second observer, not extra space."""
    a = b.x
    return a[0]-a[2]+a[4], a[1]-a[3]+a[5]


def decode(c, h) -> Raw6:
    c = tuple(c); h = tuple(h)
    if len(c) != 4 or len(h) != 2 or any(type(v) is not int for v in c+h):
        raise ValueError('integer branch-level observer coefficients required')
    n0, n1 = h[0]-c[0]+c[2], h[1]-c[1]+c[3]
    if n0 % 3 or n1 % 3:
        raise ValueError('incompatible integral gluing; no X6 preimage')
    s, t = n0//3, n1//3
    return c[0]+s, c[1]+t, c[2]-s, c[3]-t, s, t


def observed_T(c, h):
    return (-c[3], c[0], c[1]+c[3], c[2]), (-h[1], h[0])


def observed_U(c, h):
    # This division is exact on the proved integral image, not Cell division.
    x = decode(c, h); s, t = x[4], x[5]
    return ((c[0]+2*s,c[1]+2*t,c[2]-2*s,c[3]-2*t),
            (h[0]-2*s,h[1]-2*t))


def norm12_pair(c):
    """Exact algebraic squared modulus A+B*sqrt(3), without evaluating sqrt."""
    a, b, c2, d = c
    return (a*a+b*b+c2*c2+d*d+a*c2+b*d,
            a*b+b*c2+c2*d)


def native_length_square(b: Branch):
    return sum(x*x for x in b.x)


def decode_two_observations(c, uc):
    d0, d1 = uc[0]-c[0], uc[1]-c[1]
    if d0 % 2 or d1 % 2:
        raise ValueError('incompatible two-readout parity')
    s, t = d0//2, d1//2
    x = (c[0]+s, c[1]+t, c[2]-s, c[3]-t, s, t)
    if uc != (c[0]+2*s, c[1]+2*t, c[2]-2*s, c[3]-2*t):
        raise ValueError('incompatible full U readout')
    return x


def weighted_observer(family):
    """A signed/algebraic observer ONLY; never feeds back as positive mass."""
    return tuple(sum((b.cwm.total * c12(b)[j] for b in family), Fraction(0))
                 for j in range(4))


def observation(b: Branch):
    c, h = c12(b), c4(b)
    return {'source_id': b.source_id, 'raw_x6': b.x,
            'history': b.operation_history,
            'cwm': {'count': b.cwm.count, 'total': str(b.cwm.total),
                    'dominant': str(b.cwm.dominant)},
            'c12': c, 'c4': h, 'norm12_A_B': norm12_pair(c),
            'native_length_square': native_length_square(b)}
