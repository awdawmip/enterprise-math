"""Replay the frozen three-region codec. Run with --repo /path/to/enterprise-math."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator

COMMIT = "d2984d1a0c5c8221ee103084dd3da68dd039dfaa"
HASHES = {
    "src/enterprise_math/cell_address.py": "b0ec81867994146ad69e81f73c74cfe58071c361150a84749be7a852536f1329",
    "src/enterprise_math/_cell_slice_codec.py": "9eb64264a59e23402c51d8aa20ff9a21ff37dec5f8bd80a97da2f54bbb48a70b",
    "schemas/cell_address.schema.json": "68ff74fdeb78135cc5ddef9cd50cd223760c0a488831258a0c39ba7772981b0e",
    "EnterpriseMath/CellAddress/Contract.lean": "998c0e2b1de0f5ea573970f0639e86af4a7bb7a6c1ad9f4fe2352dfa6e25c0f2",
    "EnterpriseMath/CellAddress/ThreeRegionSlice.lean": "2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02",
    "tests/test_cell_address_contract.py": "519ab8e8fd9576bba2fbc0aabd29fc79a7b6070e1757a3049af92d903b58ca48",
}
DIRS = {"E1_FORWARD": (1, 0), "E1_REVERSE": (-1, 0),
        "E2_FORWARD": (0, 1), "E2_REVERSE": (0, -1)}


def three_values(x, y):
    return x, y, x - y


def from_codes(api, limit):
    points = {}
    for zero in range(3):
        for a, b in itertools.product(range(1, limit + 1), repeat=2):
            coords = [a, b]
            coords.insert(zero, 0)
            address = api.FinalCellAddress(tuple(coords + [0, 0, 0]))
            point = api.decode_raw_slice(address)
            assert point not in points and api.encode_raw_slice(point) == address
            points[point] = address
    return points


def triangle(t):
    return (t + 1) * (t + 2) // 2 if t >= 0 else 0


def word_count(limit, minima, maxima):
    lower = [1 - limit - v for v in minima]
    upper = [limit - v for v in maxima]
    if any(l > u for l, u in zip(lower, upper)):
        return 0
    a, b = (upper[i] - lower[i] + 1 for i in range(2))

    def at_most(h):
        s = h - lower[0] + upper[1]
        return triangle(s) - triangle(s-a) - triangle(s-b) + triangle(s-a-b)

    answer = at_most(upper[2]) - at_most(lower[2]-1)
    can_fit = max(lower[2], lower[0] - upper[1]) <= min(upper[2], upper[0] - lower[1])
    assert (answer > 0) == can_fit
    return answer


def minimum_capacity(lo, hi):
    # Integer ceiling for any signed numerator.
    def ceil_div(n, d):
        return -((-n)//d)
    singles = [ceil_div(1 + v-u,2) for u,v in zip(lo,hi)]
    return max(*singles, ceil_div(2+hi[0]-lo[1]-lo[2],3),
               ceil_div(1-lo[0]+hi[1]+hi[2],3))


def sharp_spans(api):
    results = []
    for d in range(9):
        raw_path = ([(i,0) for i in range(d+1)] + [(i,0) for i in reversed(range(d))]
                    + [(0,-i) for i in range(1,d+1)])
        threshold = (2*d+4)//3
        for t in {max(0,threshold-1),threshold}:
            fit = any(all(max(api.encode_raw_slice((x+i,y+j)).coordinates) <= t
                          for i,j in raw_path) for x,y in from_codes(api,t))
            assert fit == (t >= threshold)
        results.append(threshold)
    return results


def widths_formula(limit, lo, hi):
    widths = [v - u for u, v in zip(lo, hi)]
    alpha = -1 - hi[0] + lo[1] + hi[2]
    beta = lo[0] - hi[1] - lo[2]
    return (3*limit**2 - sum(widths)*limit + widths[0]*widths[1]
            - alpha*(alpha+1)//2 - beta*(beta+1)//2)


def audit_domain(api, limit):
    points = from_codes(api, limit)
    strip = {(x,y) for x in range(-limit-1, limit+2)
             for y in range(-limit-1, limit+2)
             if all(1-limit <= v <= limit for v in three_values(x,y))}
    assert set(points) == strip and len(strip) == 3*limit**2
    edges = {}
    for name, (dx, dy) in DIRS.items():
        edge = {}
        for p, address in points.items():
            q = api.step_cell(address, name)
            dest = api.decode_raw_slice(q)
            assert dest == (p[0]+dx, p[1]+dy)
            if max(q.coordinates) <= limit:
                edge[p] = dest
        assert len(points) - len(edge) == 2*limit
        edges[name] = edge

    safe = set(points)
    for r in range(1, limit+2):
        safe = {p for p in safe if all(edges[d].get(p) in safe for d in DIRS)}
        assert len(safe) == 3*max(0, limit-r)**2

    word_tests = 0
    # Each stored point represents exactly one distinct surviving start:
    # each fixed word transports by a translation.
    def walk(survivors, end, lo, hi, length):
        nonlocal word_tests
        word_tests += 1
        assert len(survivors) == word_count(limit, lo, hi)
        assert bool(survivors) == (minimum_capacity(lo,hi) <= limit)
        large_limit = 3*length + 3
        assert word_count(large_limit,lo,hi) == widths_formula(large_limit,lo,hi)
        if length == 5:
            return
        for name, (dx,dy) in DIRS.items():
            moved = (end[0]+dx, end[1]+dy)
            vals = three_values(*moved)
            edge = edges[name]
            walk([edge[p] for p in survivors if p in edge], moved,
                 tuple(map(min,lo,vals)), tuple(map(max,hi,vals)), length+1)

    walk(list(points), (0,0), (0,0,0), (0,0,0), 0)
    return {"integer_field_cap":limit, "states":len(points), "exits_each_direction":2*limit,
            "all_prefix_words_length_at_most_5":word_tests}


def branch_checks(api):
    count = 0
    probes = 0
    for zero in range(3):
        for base in itertools.product((1,2),repeat=2):
            pts = [base]
            for i in range(2):
                if base[i] == 2:
                    v = list(base)
                    v[i] += 1
                    pts.append(tuple(v))
            for name,(dx,dy) in DIRS.items():
                count += 1
                targets = set()
                for pos in pts:
                    z = list(pos)
                    z.insert(zero, 0)
                    address = api.FinalCellAddress(tuple(z+[0,0,0]))
                    x,y = api.decode_raw_slice(address)
                    shifted = api.step_cell(address,name)
                    assert api.decode_raw_slice(shifted) == (x+dx,y+dy)
                    targets.add(shifted.coordinates[:3].index(0))
                    probes += 1
                assert len(targets) == 1
    return {"affine_cells_with_direction":count,"affine_basepoint_and_unit_probes":probes}


def is_accepted(fun, arg):
    try:
        fun(arg)
    except (ValueError, TypeError):
        return False
    return True


def parser_examples(api, schema):
    validate = Draft202012Validator(schema)
    Draft202012Validator.check_schema(schema)
    addr = api.encode_raw_slice((0,0))
    text = addr.to_json()
    raw = "[0,1,1,0,0,0]"
    tests = {
        "canonical":(text,True,True),
        "negative_zero":(text.replace(raw,"[-0,1,1,0,0,0]"), True,True),
        "integer_as_decimal":(text.replace(raw,"[0,1.0,1,0,0,0]"), False,True),
        "integer_as_exponent":(text.replace(raw,"[0,1e0,1,0,0,0]"), False,True),
        "boolean":(text.replace(raw,"[0,true,1,0,0,0]"),False,False),
        "negative":(text.replace(raw,"[0,-1,1,0,0,0]"),False,False),
        "duplicate_version":(text.replace('"version":1','"version":1,"version":1'),False,True),
        "unknown_codec":(text.replace(api.CODEC,"unregistered"),False,False),
        "unknown_frame":(text.replace(api.FRAME,"other"),False,False),
        "unknown_version":(text.replace('"version":1','"version":2'),False,False),
        "invalid_zero_pattern":(text.replace(raw,"[0,0,1,0,0,0]"),False,False),
        "extra_key":(text.replace('"version":1','"version":1,"extra":0'),False,False)}
    result = {}
    for name,(s,expected_runtime,expected_ast) in tests.items():
        actual = is_accepted(api.FinalCellAddress.from_json,s)
        post_parse = validate.is_valid(json.loads(s))
        assert (actual,post_parse) == (expected_runtime,expected_ast)
        if actual:
            assert api.FinalCellAddress.from_json(s).to_json() == text
        result[name] = [actual, post_parse]
    assert not is_accepted(api.encode_raw_slice, (0,0,1,0,0,0))
    for label in ["E3_FORWARD","CROSS_AND_INCREMENT"]:
        assert not is_accepted(lambda d: api.step_cell(addr,d),label)
    return result


def decimal_boundaries(api, schema):
    validator = Draft202012Validator(schema)
    old = sys.get_int_max_str_digits()
    rows = []
    try:
        for digits in [640, 4300]:
            sys.set_int_max_str_digits(digits)
            t = 10**digits-1
            q = api.encode_raw_slice((t,1))
            assert q.coordinates[:3] == (t,1,0)
            good = q.to_json()
            assert api.FinalCellAddress.from_json(good) == q
            outside = api.step_cell(q,"E1_FORWARD")
            assert api.FinalCellAddress.from_wire(outside.to_wire()) == outside
            assert validator.is_valid(outside.to_wire())
            assert max(q.coordinates) <= t < max(outside.coordinates)
            # Build the incoming spelling as text, without relying on formatting an
            # out-of-budget integer. An explicit precheck suffices for a writer.
            incoming = good.replace("9"*digits,"1"+"0"*digits)
            reject = not is_accepted(api.FinalCellAddress.from_json,incoming)
            assert reject
            negative_q = api.encode_raw_slice((1-t,1-t))
            assert negative_q.coordinates[:3] == (0,1,t)
            assert api.FinalCellAddress.from_json(negative_q.to_json()) == negative_q
            negative_out = api.step_cell(negative_q,"E1_REVERSE")
            assert max(negative_out.coordinates) == t+1
            assert api.step_cell(outside,"E1_REVERSE") == q
            rows.append({"digits":digits,"upper_face_roundtrip":True,
                         "next_decimal_input_rejected":reject,
                         "lower_face_roundtrip":True,"first_negative_step_exceeds_budget":True,
                         "next_wire_and_schema_admit":True,"opposite_step_returns":True})
        sys.set_int_max_str_digits(0)
        p = api.encode_raw_slice((10**4300,1))
        assert api.FinalCellAddress.from_json(p.to_json()) == p
    finally:
        sys.set_int_max_str_digits(old)
    return {"common_settings":rows,"documented_unlimited_setting_roundtrip_4301_digits":True}


def cumulative_length(j):
    return 1+(9*j-10)*10**(j-1) if j >= 2 else 0


def byte_budget_checks(api):
    overhead = len(api.encode_raw_slice((0,0)).to_json().encode("ascii"))-2
    assert overhead == 132
    result = []
    for d in (1,2):
        t = 10**d-1
        histogram = Counter(len(q.to_json().encode("ascii")) - overhead
                            for q in from_codes(api,t).values())
        for b in range(2*d+3):
            count = 3*(cumulative_length(b) - 2*10**d*cumulative_length(b-d)
                       + 10**(2*d)*cumulative_length(b-2*d))
            assert count == sum(v for k,v in histogram.items() if k<=b)
        result.append({"digits":d,"full_population":sum(histogram.values()),
                       "active_digit_sum_histogram":dict(sorted(histogram.items()))})
    return {"ascii_fixed_overhead":overhead,"checks":result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path)
    args = parser.parse_args()
    roots = [args.repo] if args.repo else [Path.cwd(),*Path(__file__).resolve().parents,
                                          Path("/workspace/enterprise-math")]
    repo = next((r for r in roots if (r/"src/enterprise_math/cell_address.py").is_file()),None)
    if repo is None:
        parser.error("pass --repo pointing to the frozen source checkout")
    for rel, expected in HASHES.items():
        assert hashlib.sha256((repo/rel).read_bytes()).hexdigest() == expected, rel
    sys.path.insert(0,str(repo/"src"))
    from enterprise_math import cell_address as api
    assert Path(api.__file__).resolve() == (repo/"src/enterprise_math/cell_address.py").resolve()
    schema = json.loads((repo/"schemas/cell_address.schema.json").read_text())
    result = {"source_commit":COMMIT,"checked_source_sha256":HASHES,
              "branches":branch_checks(api),"decimal_interfaces":decimal_boundaries(api,schema),
              "wire_examples_runtime_then_schema_on_parsed_value":parser_examples(api,schema),
              "geometric_domains":[audit_domain(api,t) for t in (1,2,3,4,5,9)],
              "two_budgets":byte_budget_checks(api),
              "sharp_capacities_for_spans_0_to_8":sharp_spans(api)}
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
