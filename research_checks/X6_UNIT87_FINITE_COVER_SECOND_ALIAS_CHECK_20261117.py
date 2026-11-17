#!/usr/bin/env python3
"""Independent exact six-axis signed-BRC convolution; Unit87 author experiment.

P000 frozen native object: 12 labeled +/- e_i operations on a chosen Z^6 Cell.
This enumerates exact endpoint multiplicities by axis interleaving, not a full
6D endpoint-table traversal, and distinguishes derived finite-depth cover
return predicates from exact native Cell return.
"""
from functools import lru_cache
from math import comb, factorial
import hashlib
import json


@lru_cache(None)
def signed_endpoint_count(axis_count: int, length: int, signed_coordinate: int) -> int:
    """Count labeled +/- axis words ending at h*(1,...,1) in Z^axis_count."""
    h = signed_coordinate
    if axis_count < 1 or length < 0:
        raise ValueError("invalid axis count or length")
    if axis_count == 1:
        return (comb(length, (length + h) // 2)
                if abs(h) <= length and (length-h) % 2 == 0 else 0)
    return sum(
        comb(length, used)
        * signed_endpoint_count(1, used, h)
        * signed_endpoint_count(axis_count-1, length-used, h)
        for used in range(abs(h), length+1, 2)
    )


def cover_return(modulus: int, length: int) -> int:
    """C_m return: sum all signed diagonal endpoints h with h mod m == 0."""
    if modulus < 1 or length < 0:
        raise ValueError("positive modulus and nonnegative length required")
    return sum(
        signed_endpoint_count(6, length, h)
        for h in range(-length//6, length//6+1)
        if h % modulus == 0
    )


def native_return(length: int) -> int:
    return signed_endpoint_count(6, length, 0)


def run():
    cases = []
    all_horizon_comparisons = 0
    for m in range(1, 6):
        a = 6*m
        first = 2 * factorial(a) // factorial(m)**6
        second = 12 * factorial(a+2) // (factorial(m+1) * factorial(m)**5)
        first_direct = cover_return(m, a)-native_return(a)
        second_direct = cover_return(m, a+2)-native_return(a+2)
        assert first_direct == first
        assert second_direct == second
        assert second == first * (6*(a+2)*(a+1)//(m+1))
        for length in range(a):
            assert cover_return(m, length) == native_return(length)
            all_horizon_comparisons += 1
        assert cover_return(m,a+1) == native_return(a+1)
        all_horizon_comparisons += 1
        cases.append({
            "modulus":m, "first_length":a,
            "first_alias_extra":first,
            "next_even_length":a+2,
            "next_even_alias_extra":second,
            "native_return_first":native_return(a),
            "cover_return_first":cover_return(m,a),
            "native_return_next_even":native_return(a+2),
            "cover_return_next_even":cover_return(m,a+2),
            "counted_by":"independent_integer_six_axis_convolution"
        })
    assert len(cases)==5
    return {
        "schema":"EM_X6_UNIT87_SECOND_ALIAS_EXACT_V1",
        "status":"AUTHOR_EXACT_EXECUTED_UNREVIEWED_NOT_ADMITTED",
        "native_axes":6,
        "primitive_operations":12,
        "model":"signed Z6 BRC, C_m=(min-zero, common-depth mod m)",
        "first_alias_formula":"2*(6*m)!/(m!)**6",
        "next_even_alias_formula":"12*(6*m+2)!/((m+1)!*(m!)**5)",
        "checked_moduli":[1,2,3,4,5],
        "prealias_and_odd_horizon_compares":all_horizon_comparisons,
        "test_cases":cases,
        "coverage_note":"exact axis-interleaving DP at all stated lengths; not full six-dimensional endpoint table; no native benchmark reexecution",
        "failures":0
    }


if __name__=="__main__":
    result=run()
    print(json.dumps(result,sort_keys=True,separators=(",",":"),ensure_ascii=False))
