"""Experimental X6 address adapter. No native state/metric/adjacency changes.

Addresses are not integer sequences. Layer schemes are replaceable views, not
identity. Frame descriptors travel with addresses and must match the immutable
registry. The injected l1 backend is the existing native-coordinate routine.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from types import MappingProxyType
from typing import Callable, Iterable
import json

DIM = 6
ZERO = (0,) * DIM
IDENTITY = tuple(range(DIM))


def vector(x: object) -> tuple[int, ...]:
    if type(x) is not tuple or len(x) != DIM or any(type(t) is not int for t in x):
        raise ValueError('expected exactly six integers; booleans are not coordinates')
    return x


def name(x: object) -> str:
    if type(x) is not str or not x:
        raise ValueError('nonempty identifier required')
    return x


def positive(n: int) -> int:
    return 2*n + 1 if n >= 0 else -2*n


def signed(n: int) -> int:
    if type(n) is not int or n < 1:
        raise ValueError('address digits must be positive integers')
    return (n-1)//2 if n % 2 else -n//2


@dataclass(frozen=True)
class Frame:
    tag: str
    offset: tuple[int, ...] = ZERO
    order: tuple[int, ...] = IDENTITY

    def __post_init__(self):
        name(self.tag); vector(self.offset); vector(self.order)
        if sorted(self.order) != list(IDENTITY):
            raise ValueError('order must be a permutation of six axes')


@dataclass(frozen=True)
class CellKey:
    space: str
    native: tuple[int, ...]

    def __post_init__(self):
        name(self.space); vector(self.native)


@dataclass(frozen=True)
class Address:
    space: str
    frame: Frame
    digits: tuple[int, ...]
    version: int = 2

    def __post_init__(self):
        name(self.space)
        if type(self.frame) is not Frame or type(self.version) is not int or self.version != 2:
            raise ValueError('unknown frame type or address version')
        vector(self.digits)
        for d in self.digits:
            signed(d)


@dataclass(frozen=True)
class DisplayReference:
    label: str = 'O_ref'
    recess: str = 'display only'


@dataclass(frozen=True)
class LayerScheme:
    tag: str
    seeds: tuple[CellKey, ...]

    def __post_init__(self):
        name(self.tag)
        if type(self.seeds) is not tuple or not self.seeds or any(type(k) is not CellKey for k in self.seeds):
            raise ValueError('finite nonempty tuple of CellKey seeds required')
        if len(set(self.seeds)) != len(self.seeds) or len({k.space for k in self.seeds}) != 1:
            raise ValueError('seed identities must be unique and in one space')


@dataclass(frozen=True)
class LayerView:
    address: Address
    scheme: LayerScheme
    layer: int


class Adapter:
    def __init__(self, space: str, frames: Iterable[Frame], l1_backend: Callable):
        self.space = name(space)
        fs = tuple(frames)
        if not fs or any(type(f) is not Frame for f in fs) or len({f.tag for f in fs}) != len(fs):
            raise ValueError('unique immutable frame descriptors required')
        self.frames = MappingProxyType({f.tag: f for f in fs})
        if not callable(l1_backend):
            raise ValueError('inject the native coordinate distance backend')
        self._l1 = l1_backend

    def key(self, native: tuple[int, ...]) -> CellKey:
        return CellKey(self.space, vector(native))

    def encode(self, key: CellKey, frame_tag: str) -> Address:
        if type(key) is not CellKey or key.space != self.space:
            raise ValueError('not a CellKey in this space')
        if frame_tag not in self.frames:
            raise ValueError('unknown frame')
        f = self.frames[frame_tag]
        return Address(self.space, f, tuple(positive(key.native[i]-f.offset[i]) for i in f.order))

    def decode(self, address: Address) -> CellKey:
        if type(address) is not Address or address.space != self.space:
            raise ValueError('expected a Cell address, not display metadata or a layer view')
        f = address.frame
        if self.frames.get(f.tag) != f:
            raise ValueError('frame descriptor drift; never reinterpret an old address')
        out = list(f.offset)
        for i, digit in zip(f.order, address.digits, strict=True):
            out[i] += signed(digit)
        return self.key(tuple(out))

    def reframe(self, a: Address, tag: str) -> Address:
        return self.encode(self.decode(a), tag)

    def same_cell(self, a: Address, b: Address) -> bool:
        return self.decode(a) == self.decode(b)

    def displacement(self, a: Address, b: Address) -> tuple[int, ...]:
        p, q = self.decode(a).native, self.decode(b).native
        return tuple(y-x for x, y in zip(p, q, strict=True))

    def steps(self, a: Address, b: Address) -> int:
        return self._l1(self.decode(a).native, self.decode(b).native)

    def distance_squared(self, a: Address, b: Address) -> int:
        return sum(t*t for t in self.displacement(a, b))

    def move(self, a: Address, axis: int, sign: int, output_frame: str | None = None) -> Address:
        if type(axis) is not int or not 0 <= axis < DIM or type(sign) is not int or sign not in (-1, 1):
            raise ValueError('native axis 0..5 and sign +/-1 required')
        x = list(self.decode(a).native); x[axis] += sign
        return self.encode(self.key(tuple(x)), a.frame.tag if output_frame is None else output_frame)

    def view(self, a: Address, scheme: LayerScheme) -> LayerView:
        key = self.decode(a)
        if type(scheme) is not LayerScheme or scheme.seeds[0].space != self.space:
            raise ValueError('incompatible layer scheme')
        # Full unobstructed X6 unit-step lattice ONLY, not a bounded/obstacle graph.
        ell = 1 + min(self._l1(key.native, s.native) for s in scheme.seeds)
        return LayerView(a, scheme, ell)

    def dump(self, a: Address) -> str:
        self.decode(a)
        obj = {'version': 2, 'space': a.space, 'frame': {'tag': a.frame.tag,
               'offset': a.frame.offset, 'order': a.frame.order}, 'digits': a.digits}
        return json.dumps(obj, sort_keys=True, separators=(',', ':'))

    def load(self, data: str) -> Address:
        def unique(items):
            out = {}
            for k, v in items:
                if k in out:
                    raise ValueError('duplicate serialized field')
                out[k] = v
            return out
        obj = json.loads(data, object_pairs_hook=unique)
        if type(obj) is not dict or set(obj) != {'version','space','frame','digits'}:
            raise ValueError('invalid serialized address fields')
        f = obj['frame']
        if type(f) is not dict or set(f) != {'tag','offset','order'}:
            raise ValueError('invalid frame fields')
        if any(type(v) is not list for v in (f['offset'], f['order'], obj['digits'])):
            raise ValueError('serialized coordinates must be lists')
        a = Address(obj['space'], Frame(f['tag'], tuple(f['offset']), tuple(f['order'])),
                    tuple(obj['digits']), obj['version'])
        self.decode(a)
        return a


@dataclass(frozen=True)
class EdgeRecord:
    edge_id: str
    source: Address
    target: Address
    axis: int
    sign: int
    weight: Fraction


def canonical_edges(adapter: Adapter, records: Iterable[EdgeRecord]) -> dict:
    """Deduplicate declarations by physical edge identity, never just endpoints.

    Distinct edge IDs are distinct branch identities within this import context.
    They are not an authorization to add native transitions. Reusing an ID with
    conflicting endpoints, direction or weight is rejected, never averaged.
    """
    result = {}
    for r in records:
        if type(r) is not EdgeRecord:
            raise ValueError('expected labeled edge declaration')
        name(r.edge_id)
        if type(r.weight) is not Fraction or r.weight <= 0:
            raise ValueError('exact positive rational weight required')
        source, target = adapter.decode(r.source), adapter.decode(r.target)
        step = adapter.move(r.source, r.axis, r.sign)
        if adapter.decode(step) != target:
            raise ValueError('declared edge is not the labeled native unit step')
        canonical = (source, target, r.axis, r.sign, r.weight)
        if r.edge_id in result and result[r.edge_id] != canonical:
            raise ValueError('conflicting declarations for one physical edge')
        result[r.edge_id] = canonical
    return result
