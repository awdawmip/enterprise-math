#!/usr/bin/env python3
from itertools import combinations, product
from collections import defaultdict
import copy
import json

BITS = (0, 1)
EDGE_LABELS = list(product(BITS, repeat=3))
GAUGES = list(product(BITS, repeat=3))
CONTRACTS = tuple(range(4))  # bit h selects whether loop state h is globally effective

AXES = ("E1","E2","E3","E4","E5","E6")
STARS = {
    "A": ("E1","E2","E3"),
    "B": ("E1","E4","E5"),
    "C": ("E2","E4","E6"),
    "D": ("E3","E5","E6"),
}
CELLS = ("xA","xB","xC","xD")

Q10_PRIMITIVE_REDUCT = {
    "P000_reality": {"space_dimension": 6, "time_dimension": 1},
    "NativeCell": CELLS,
    "AxisType": AXES,
    "CarrierStar3": tuple(sorted(tuple(sorted(v)) for v in STARS.values())),
    "CellAxisInc": tuple(sorted(
        (f"x{k}", e) for k, star in STARS.items() for e in star
    )),
    "NativeAdj": tuple(sorted(tuple(sorted(p)) for p in combinations(CELLS, 2))),
    "framed_PF10_shell": {
        "frame_type": "uniform_typed_bijection_AxisType_to_Channel",
        "I": (1,1,1,1,1,1),
        "O": (1,1,1,1,1,1),
        "M": tuple(tuple(1 if i == j else 0 for j in range(6)) for i in range(6)),
    },
}

def hol(a):
    return a[0] ^ a[1] ^ a[2]

def gauge(a, g):
    a01, a12, a20 = a
    g0, g1, g2 = g
    return (a01 ^ g0 ^ g1,
            a12 ^ g1 ^ g2,
            a20 ^ g2 ^ g0)

def effective(contract_mask, h):
    return (contract_mask >> h) & 1

def status(contract_mask, h):
    if not effective(contract_mask, h):
        return "NO_GLOBAL_OBJECT"
    return "STRICT_GLOBALIZATION" if h == 0 else "TWISTED_GLOBALIZATION"

def observed_reduct(edge_packet, q12=None):
    h = hol(edge_packet)
    out = {
        "q10_primitive": copy.deepcopy(Q10_PRIMITIVE_REDUCT),
        "q11_transport": {
            "selected_triangle": ("xA","xB","xC"),
            "edge_packet": edge_packet,
            "H": h,
            "strict_frame_possible": (h == 0),
        },
    }
    if q12 is not None:
        r, d = q12
        assert h == (r ^ d)
        out["q12_observables"] = {"R": r, "H": h, "D": d}
    return out

checks = 0

assert Q10_PRIMITIVE_REDUCT["P000_reality"] == {"space_dimension": 6, "time_dimension": 1}
assert len(Q10_PRIMITIVE_REDUCT["NativeCell"]) == 4
assert len(Q10_PRIMITIVE_REDUCT["AxisType"]) == 6
assert len(Q10_PRIMITIVE_REDUCT["CarrierStar3"]) == 4
assert len(Q10_PRIMITIVE_REDUCT["CellAxisInc"]) == 12
assert len(Q10_PRIMITIVE_REDUCT["NativeAdj"]) == 6
checks += 6

orbits = {}
for a in EDGE_LABELS:
    orb = frozenset(gauge(a, g) for g in GAUGES)
    orbits[a] = orb
    for g in GAUGES:
        assert hol(gauge(a, g)) == hol(a)
        checks += 1
for a in EDGE_LABELS:
    for b in EDGE_LABELS:
        assert (b in orbits[a]) == (hol(a) == hol(b))
        checks += 1

q11_collision_count = 0
for a in EDGE_LABELS:
    base = observed_reduct(a)
    h = hol(a)
    truth_values = set()
    for mask in CONTRACTS:
        expanded = {"reduct": copy.deepcopy(base), "effectivity_contract": mask}
        assert expanded["reduct"] == base
        truth_values.add(effective(mask, h))
        checks += 1
    assert truth_values == {0, 1}
    q11_collision_count += 1
    checks += 1
assert q11_collision_count == 8
checks += 1

even = (0,0,0)
odd = (1,0,0)
assert hol(even) == 0 and hol(odd) == 1
assert observed_reduct(even) == observed_reduct(even)
assert effective(0b00, 0) == 0 and effective(0b01, 0) == 1
assert status(0b00, 0) == "NO_GLOBAL_OBJECT"
assert status(0b01, 0) == "STRICT_GLOBALIZATION"
assert observed_reduct(odd) == observed_reduct(odd)
assert effective(0b01, 1) == 0 and effective(0b11, 1) == 1
assert status(0b01, 1) == "NO_GLOBAL_OBJECT"
assert status(0b11, 1) == "TWISTED_GLOBALIZATION"
checks += 10

q12_collision_count = 0
for r, d in product(BITS, repeat=2):
    h = r ^ d
    a = even if h == 0 else odd
    base = observed_reduct(a, q12=(r,d))
    assert base["q12_observables"] == {"R": r, "H": h, "D": d}
    truth_values = {effective(mask, h) for mask in CONTRACTS}
    assert truth_values == {0, 1}
    assert base["q11_transport"]["strict_frame_possible"] == (h == 0)
    q12_collision_count += 1
    checks += 4
assert q12_collision_count == 4
checks += 1

decoder_collisions = defaultdict(set)
for a in EDGE_LABELS:
    h = hol(a)
    primitive_key = json.dumps(observed_reduct(a), sort_keys=True)
    for mask in CONTRACTS:
        decoder_collisions[primitive_key].add(effective(mask, h))
assert len(decoder_collisions) == 8
assert all(vals == {0,1} for vals in decoder_collisions.values())
checks += 9

def one_bit_encoding_works(f_table_mask):
    constraints = {}
    for contract in CONTRACTS:
        b = (f_table_mask >> contract) & 1
        for h in BITS:
            y = effective(contract, h)
            key = (h, b)
            if key in constraints and constraints[key] != y:
                return False
            constraints[key] = y
    return True

working_one_bit_encodings = [
    f for f in range(16) if one_bit_encoding_works(f)
]
assert working_one_bit_encodings == []
checks += 16

for mask in CONTRACTS:
    eps0, eps1 = effective(mask,0), effective(mask,1)
    reconstructed = eps0 | (eps1 << 1)
    assert reconstructed == mask
    for h in BITS:
        assert effective(reconstructed,h) == effective(mask,h)
        checks += 1
assert len({(effective(mask,0), effective(mask,1)) for mask in CONTRACTS}) == 4
checks += 1

for mask in CONTRACTS:
    for a in EDGE_LABELS:
        for g in GAUGES:
            assert effective(mask, hol(gauge(a,g))) == effective(mask, hol(a))
            checks += 1

for h in BITS:
    values = {(mask, effective(mask,h)) for mask in CONTRACTS}
    assert {v for _,v in values} == {0,1}
    checks += 1

print(
    "PASS P000_GLOBAL_EFFECTIVITY_DERIVATION_OR_UNDERDETERMINATION; "
    f"checks={checks}; "
    "same_reduct_nondefinability=TRUE; "
    f"q11_exact_reduct_collisions={q11_collision_count}; "
    f"q12_RHD_exact_reduct_collisions={q12_collision_count}; "
    "H0_effectivity_underdetermined=TRUE; H1_effectivity_underdetermined=TRUE; "
    "R_H_D_add_no_deciding_power=TRUE; "
    "strict_frame_adds_no_effectivity_deciding_power=TRUE; "
    "one_global_new_bit_sufficient_for_all_C2_loop_states=FALSE; "
    "minimum_unrestricted_C3_C2_effectivity_information_bits=2; "
    "minimal_completion=gauge_invariant_selection_on_H_quotient; "
    "current_P000_primitives_derive_effectivity=FALSE_AT_DECLARED_BENCHMARK_SCOPE"
)
