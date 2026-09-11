"""One fixed arithmetic observation on each of three published RSA puzzles.

Only the literal RSA Inc / MysteryTwister mathematical challenge integers
below are used. There is no target-input port, parameter sweep, retry search,
key handling, network execution or factorization fallback.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
from math import isqrt
from pathlib import Path
from time import perf_counter_ns
import json
import platform
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enterprise-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    sys.path.insert(0, str(args.enterprise_root / "src"))
    from enterprise_math.brc_multiplier_basin import point_cost_state
    from enterprise_math.brc_square_gap_prefilter import ceiling_completion_square_witness
    from enterprise_math.brc_neighbor_square_lift_shortcut import neighbor_square_parameters

    source_expectations = {
        "brc_multiplier_basin.py": "6fe4551f053e6427c67aef1e70e837615d75aa5a52b7477bf6c9cb96fb9a7d3a",
        "brc_square_gap_prefilter.py": "f8e178771a25221eaab16002b9ffacd188dc5f39be4948ec2b40ee3e22c9f716",
        "brc_neighbor_square_lift_shortcut.py": "fdf1e5c4ee4a032fb732d9653f0a7fd9cf738bd62b1a7af50eb53588e7864490",
    }
    for name, expected in source_expectations.items():
        assert sha256((args.enterprise_root / "src" / "enterprise_math" / name).read_bytes()).hexdigest() == expected

    # Transcribed decimal blocks from page 3 of the cited author-attributed PDFs.
    # Keeping original block boundaries makes transcription reviewable.
    fixtures = (
        ("RSA-270", "09", 270, (
            "2331085303444075445276376569106805241456198124803054",
            "4904294861196849591824513578286788836931857711641821",
            "3919268572658314913060672626911354027609793166341626",
            "6939465961964277442738866018768963134687040590667469",
            "0312391074827760654864915192081269930976658751473545",
            "6594993207")),
        ("RSA-896", "10", 270, (
            "4120234369866595438555313653325759481798116998443279",
            "8284545562643387644556524842619809887042316184187926",
            "1420247188869492560931776375033421130982397485150944",
            "9091069102698610318627041148808669705649029036536588",
            "6743373172081310410519086425479328260139125762403394",
            "6373269391")),
        ("RSA-2048", "38", 617, (
            "251959084756578934940271832400483985714292821262040320277",
            "771378360436620207075955562640185258807844069182906412495",
            "150821892985591491761845028084891200728449926873928072877",
            "767359714183472702618963750149718246911650776133798590957",
            "000973304597488084284017974291006424586918171951187461215",
            "151726546322822168699875491824224336372590851418654620435",
            "767984233871847744479207399342365848238242811981638150106",
            "748104516603773060562016196762561338441436038339044149526",
            "344321901146575444541784240209246165157233507787077498171",
            "257724679629263863563732899121548314381678998850404453640",
            "23527381951378636564391212010397122822120720357")),
    )

    # Check the two unchanged interfaces on previously certified positive
    # constructions. This warms imports/caches and is outside puzzle timings.
    assert ceiling_completion_square_witness(299, 1) == (18, 5)
    assert neighbor_square_parameters(17473, 8, 1) == (273, 15, 4096)

    records = []
    for label, source_id, digits, blocks in fixtures:
        decimal = "".join(blocks)
        assert decimal.isdecimal() and len(decimal) == digits
        n = int(decimal)
        assert n % 2 == 1
        started = perf_counter_ns()
        state = point_cost_state(n, 1)
        state_ns = perf_counter_ns() - started
        j, r, gap = state.target_root, state.subtraction_cost, state.addition_cost
        assert j*j < n < (j+1)*(j+1) and r == n-j*j and gap == 2*j+1-r
        direction = "D" if r <= j else "U"

        # One existing immediate-completion call. No advancing of the ceiling.
        started = perf_counter_ns()
        direct_witness = ceiling_completion_square_witness(n, 1)
        direct_ns = perf_counter_ns() - started
        gap_root = isqrt(gap)
        assert (direct_witness is not None) == (gap_root*gap_root == gap)
        direct_result = {"status": "NO_WITNESS_THIS_OBSERVATION", "call_ns": direct_ns,
                         "ceiling_positions_tested": 1, "independent_square_check_agrees": True}
        if direct_witness is not None:
            a, b = direct_witness
            u, v = a-b, a+b
            assert u*v == n
            direct_result.update(status="CERTIFIED_SQUARE_WITNESS", proper_product=(1 < u < v), pair=[str(u), str(v)])

        # One previously fixed low-bit gate. The lifted parameter square is
        # only observed if that gate qualifies. No other a is attempted.
        started = perf_counter_ns()
        low = n & 63
        neighbor_result = {"status": "GATE_NOT_MET", "a": 8,
                           "N_mod_64": low, "parameter_square_tests": 0}
        if low in (1, 63):
            epsilon = 1 if low == 1 else -1
            t, m, z = neighbor_square_parameters(n, 8, epsilon)
            c = isqrt(z)
            neighbor_result.update(status="PARAMETER_SQUARE_OBSERVED", epsilon=epsilon,
                multiplier=m, parameter_square_tests=1, is_square=(c*c == z))
        neighbor_ns = perf_counter_ns() - started
        neighbor_result["observation_ns"] = neighbor_ns

        records.append({"label": label,
            "source_pdf": f"https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-{source_id}-en.pdf",
            "source_page": 3, "source_read_date": "2026-09-08", "decimal_blocks": blocks,
            "N": decimal, "decimal_sha256": sha256(decimal.encode("ascii")).hexdigest(),
            "decimal_digits": len(decimal), "bits": n.bit_length(),
            "state_annotation": {"direction": direction, "J": str(j), "R": str(r),
                "next_square_gap": str(gap), "state_api_ns": state_ns},
            "direct_completion": direct_result, "fixed_a8_parameter_condition": neighbor_result,
            "complete_fiber_recurrence": {"status": "NO_MULTIPOSITION_REUSE",
                "reason": "one puzzle supplies no multi-position fiber interval; a singleton gives the same immediate-completion predicate"},
            "bounded_gap_lookup": {"status": "INPUT_CONTRACT_NOT_MET", "required_gap_max": 510,
                "observed_gap_exceeds_bound": gap > 510}})

    output = {
        "status": "COMPLETED_FIXED_PUBLIC_MATHEMATICAL_PREDICATE_OBSERVATIONS",
        "researcher": "EM-HME-0CE4FD / TASK_RESEARCH",
        "global_snapshot": "e76fdc883f9f4a3a93c1284340e38c55aeba0a6a",
        "parent_project_frontier": "e0b6dcdf746a93b652c32d23db913c6e9f9dbf86",
        "source_sha256": source_expectations, "python": sys.version, "platform": platform.platform(),
        "controls": {"previous_direct_positive": {"N": 299, "witness": [18, 5]},
                     "previous_neighbor_parameter_positive": {"N": 17473, "parameters": [273, 15, 4096]}},
        "budget": {"puzzle_integers": 3, "direct_positions_per_puzzle": 1,
                   "fixed_neighbor_a": 8, "neighbor_signs_per_puzzle_max": 1,
                   "reruns_for_timing": 0, "search_fallbacks": 0},
        "cost_contract": {"timing": "single observations on a warmed imported runtime; descriptive latency, not a stable benchmark",
            "state_annotation": "separate existing-API call, not a required prerequisite of the low-bit gate",
            "direct_call": "unchanged API call only; independent exact audit is outside its timer",
            "neighbor_observation": "low-bit gate and result-record construction; qualifying parameter test if any",
            "setup_and_source_acquisition": "outside observation timings",
            "net_factorization_speedup": "UNMEASURED"},
        "records": records,
        "interpretation": "A non-hit describes only this fixed observation; retain the prior positive families. No general route verdict follows.",
        "goal_status": "ACTIVE; this is the requested first fixed public-puzzle shortcut verification, not a complete library or factoring result",
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    destination = args.output_dir / "brc_public_rsa_fixed_predicates_20260908.json"
    destination.write_text(json.dumps(output, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(destination), "records": [{"label": row["label"],
        "bits": row["bits"], "direction": row["state_annotation"]["direction"],
        "state_ns": row["state_annotation"]["state_api_ns"],
        "direct": row["direct_completion"], "a8": row["fixed_a8_parameter_condition"]}
        for row in records]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
