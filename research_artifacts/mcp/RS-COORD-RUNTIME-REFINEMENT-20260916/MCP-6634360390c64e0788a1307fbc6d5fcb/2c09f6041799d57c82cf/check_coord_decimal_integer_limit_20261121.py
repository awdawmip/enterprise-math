"""Exact long-decimal wire regression for registered fixed two-generator Cell slice.

Use in a checkout with the project's src/ on PYTHONPATH. This is a
counterexample regression probe, not a formal Python interpreter proof.
"""
from __future__ import annotations

import sys
from enterprise_math.cell_address import (
    FinalCellAddress, decode_raw_slice, encode_raw_slice,
)

def check():
    if not hasattr(sys, "get_int_max_str_digits"):
        raise RuntimeError("CPython digit-limit API unavailable; classify environment explicitly")
    limit = sys.get_int_max_str_digits()
    if not limit:
        raise RuntimeError("Current interpreter decimal limit disabled; not the target runtime configuration")
    b = 10**limit
    address = FinalCellAddress((0, b, 1, 0, 0, 0))
    assert decode_raw_slice(address) == (0, b-1)
    assert encode_raw_slice((0, b-1)) == address

    long_digits = "1" + "0" * limit
    wire = (
        '{"schema":"EM_CELL_ADDRESS_V1","codec":"three_region_slice_v1",'
        '"version":1,"frame":"X6_FIXED_E1_E2_CHART",'
        '"coordinates":[0,' + long_digits + ',1,0,0,0]}'
    )

    observed = {}
    for name, operation in (
        ("parse", lambda: FinalCellAddress.from_json(wire)),
        ("serialize", lambda: address.to_json()),
    ):
        try:
            operation()
        except ValueError as err:
            if "Exceeds the limit" not in str(err):
                raise
            observed[name] = str(err)
        else:
            observed[name] = "ACCEPTED"
    print("CPython", sys.version.split()[0], "integer-decimal limit", limit)
    print("Valid slice address and raw-chart roundtrip: PASS")
    print("JSON parse:", observed["parse"][:140])
    print("JSON serialize:", observed["serialize"][:140])
    # The current expected failure is a declared non-totality witness.
    assert "Exceeds the limit" in observed["parse"]
    assert "Exceeds the limit" in observed["serialize"]
    print("RECORDED_COUNTEREXAMPLE_PRESENT")

if __name__ == "__main__":
    check()
