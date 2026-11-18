"""Unit134 bounded replica of exact two guard differences in the pinned source.
This is NOT an execution of the original full frozen package / native benchmark.
"""
from __future__ import annotations
import itertools
import json


def legacy_as_triple(values):
    triple = tuple(values)
    if len(triple) != 3:
        raise ValueError("expected exactly three coordinates")
    if not all(isinstance(value, int) for value in triple):
        raise TypeError("diagonal quotient coordinates must be integers")
    return triple


def current_as_triple(values):
    triple = tuple(values)
    if len(triple) != 3:
        raise ValueError("expected exactly three coordinates")
    if not all(type(value) is int for value in triple):
        raise TypeError("diagonal quotient coordinates must be integers")
    return triple


def accepted(fn, values):
    try:
        fn(values)
        return True
    except (TypeError, ValueError):
        return False


def accepted_shift(old, coordinates, k):
    try:
        if (not isinstance(k, int)) if old else (type(k) is not int):
            raise TypeError("diagonal shift must be an integer")
        (legacy_as_triple if old else current_as_triple)(coordinates)
        return True
    except (TypeError, ValueError):
        return False


def require(predicate, detail):
    if not predicate:
        raise RuntimeError(detail)


def main():
    alphabet = (-1, 0, 1, False, True)
    coordinates = tuple(itertools.product(alphabet, repeat=3))
    old_accepted = new_accepted = invalid_old_only = 0
    for z in coordinates:
        old, new = accepted(legacy_as_triple, z), accepted(current_as_triple, z)
        valid = all(type(x) is int for x in z)
        require(old, f"unexpected legacy rejection: {z!r}")
        require(new == valid, f"new guard mismatch: {z!r}")
        old_accepted += old
        new_accepted += new
        invalid_old_only += old and not new
    old_shift = new_shift = 0
    for z in coordinates:
        for k in alphabet:
            old, new = accepted_shift(True, z, k), accepted_shift(False, z, k)
            valid = type(k) is int and all(type(x) is int for x in z)
            require(old, f"unexpected legacy shift rejection: {z!r} {k!r}")
            require(new == valid, f"new shift mismatch: {z!r} {k!r}")
            old_shift += old
            new_shift += new
    require((len(coordinates), old_accepted, new_accepted, invalid_old_only, old_shift, new_shift)
            == (125, 125, 27, 98, 625, 81), "coverage counts changed")
    report = {
        "schema": "X6_UNIT134_BOUND_GUARD_EXACT_INTEGER_REPLICA_V1",
        "source_semantics": "PINNED_FROZEN_TWO_GUARDS_REPLICATED_NOT_ORIGINAL_MODULE_IMPORT",
        "test_space": "(-1,0,1,False,True)^3 and shifts in (-1,0,1,False,True)",
        "tuple_cases": len(coordinates),
        "frozen_accepts_tuples": old_accepted,
        "current_accepts_tuples": new_accepted,
        "frozen_accepts_boolean_contaminated_tuples": invalid_old_only,
        "shift_cases": len(coordinates)*len(alphabet),
        "frozen_accepts_shift_pairs": old_shift,
        "current_accepts_shift_pairs": new_shift,
        "failure_count": 0,
        "mathematical_scope": "Python bool-is-int boundary; not an LP011/LP019 erroneous original consumer attribution",
        "mode": "always_on_checks"
    }
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, separators=(",",":")))


if __name__ == "__main__":
    main()
