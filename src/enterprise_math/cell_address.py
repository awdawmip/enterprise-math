"""Versioned nonnegative final Cell addresses; no change to native operations.

Raw signed charts and displacement scalars are NOT final Cell addresses.
Only the formally specified fixed two-generator slice is registered here.
Unknown full-X6 codecs fail closed instead of silently discarding coordinates.
"""
from __future__ import annotations
from dataclasses import dataclass
import json
from . import _cell_slice_codec as _slice

SCHEMA = "EM_CELL_ADDRESS_V1"
CODEC = "three_region_slice_v1"
FRAME = "X6_FIXED_E1_E2_CHART"
_KEYS = {"schema", "codec", "version", "frame", "coordinates"}
_DIRS = {"E1_FORWARD":"E1+", "E1_REVERSE":"E1-",
         "E2_FORWARD":"E2+", "E2_REVERSE":"E2-"}

@dataclass(frozen=True)
class FinalCellAddress:
    """Spatial identity in one fixed registered chart, not all packet state.

    Not a Sequence: old coordinate APIs cannot accidentally subtract its fields.
    Public fields are never coerced from floating point, bool, or signed values.
    """
    coordinates: tuple[int, int, int, int, int, int]
    codec: str = CODEC
    version: int = 1
    frame: str = FRAME

    def __post_init__(self) -> None:
        if type(self.codec) is not str or self.codec != CODEC:
            raise ValueError("UNREGISTERED_CELL_CODEC")
        if type(self.version) is not int or self.version != 1:
            raise ValueError("UNSUPPORTED_CELL_ADDRESS_VERSION")
        if type(self.frame) is not str or self.frame != FRAME:
            raise ValueError("UNKNOWN_OR_CHANGED_CELL_FRAME")
        _slice.decode(self.coordinates)

    def to_wire(self) -> dict:
        return {"schema":SCHEMA,"codec":self.codec,"version":self.version,
                "frame":self.frame,"coordinates":list(self.coordinates)}

    def to_json(self) -> str:
        return json.dumps(self.to_wire(), separators=(",", ":"), sort_keys=True)

    @classmethod
    def from_wire(cls, value: object) -> "FinalCellAddress":
        if type(value) is not dict or set(value) != _KEYS:
            raise ValueError("MALFORMED_OR_UNTYPED_CELL_ADDRESS")
        if value["schema"] != SCHEMA or type(value["coordinates"]) is not list:
            raise ValueError("MALFORMED_CELL_ADDRESS_PAYLOAD")
        return cls(tuple(value["coordinates"]),value["codec"],value["version"],value["frame"])

    @classmethod
    def from_json(cls, value: str) -> "FinalCellAddress":
        def pairs(items):
            out = {}
            for key, val in items:
                if key in out:
                    raise ValueError("DUPLICATE_JSON_KEY")
                out[key] = val
            return out
        def reject_float(value):
            raise ValueError("NON_INTEGER_JSON_NUMBER")
        return cls.from_wire(json.loads(value, object_pairs_hook=pairs,
            parse_float=reject_float, parse_constant=reject_float))

def _address(value: object) -> FinalCellAddress:
    if type(value) is not FinalCellAddress:
        raise TypeError("CELL_ADDRESS_REQUIRED_NOT_DISPLAY_OR_RAW_COORDINATES")
    return value

def encode_raw_slice(point: tuple[int, int]) -> FinalCellAddress:
    """Explicit migration from the fixed two-coordinate raw chart only."""
    if type(point) is not tuple:
        raise TypeError("RAW_SLICE_TUPLE_REQUIRED")
    return FinalCellAddress(_slice.encode(point))

def decode_raw_slice(address: FinalCellAddress) -> tuple[int, int]:
    """Typed internal audit output. It is not a final public address."""
    return _slice.decode(_address(address).coordinates)

def step_cell(address: FinalCellAddress, direction: str) -> FinalCellAddress:
    address = _address(address)
    if type(direction) is not str or direction not in _DIRS:
        raise ValueError("UNKNOWN_OR_OUT_OF_SLICE_DIRECTION")
    return FinalCellAddress(_slice.code_step(address.coordinates,_DIRS[direction]))

def cell_squared_distance(left: FinalCellAddress, right: FinalCellAddress) -> int:
    p,q = decode_raw_slice(left),decode_raw_slice(right)
    return sum((x-y)**2 for x,y in zip(p,q))

def cell_step_distance(left: FinalCellAddress, right: FinalCellAddress) -> int:
    # Reuse the old native-coordinate backend; do not subtract public digits.
    from .geometry import l1_distance
    return l1_distance(decode_raw_slice(left),decode_raw_slice(right))

def validate_cell_address(value: object) -> FinalCellAddress:
    return FinalCellAddress.from_wire(value)
