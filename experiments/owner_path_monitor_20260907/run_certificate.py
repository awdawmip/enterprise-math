"""Emit a compact exact finite certificate; no remote or publication effects."""
from fractions import Fraction
from dataclasses import replace
import json

from examples import blind_pair, branching_hidden_cycle_graph, suffix_context_graph
from path_monitor import (
    HIT, START, coefficient, compose_port_series, enumerate_port_walks,
    port_excursion_series, reverse_step_monitor, verify_port_series,
)


def histogram_record(histogram):
    return [[str(weight), count] for weight, count in histogram.entries]


def certificate():
    monitor = reverse_step_monitor()
    pair = []
    for word_name, graph in zip(("u", "v"), blind_pair()):
        excursions = port_excursion_series(graph, ("P",), 8)
        walks = compose_port_series(excursions)
        enumerated = enumerate_port_walks(graph, ("P",), 8)
        if not all(result.complete for result in (excursions, walks, enumerated)):
            raise ArithmeticError("finite certificate unexpectedly exceeded its budget")
        if walks.coefficients != enumerated.coefficients:
            raise ArithmeticError("product/port composition disagrees with explicit words")
        audit = verify_port_series(graph, ("P",), 8, walks)
        if audit["status"] != "VERIFIED":
            raise ArithmeticError("independent finite verifier did not verify the correct coefficient family")
        pair.append({"word": word_name, "horizon": 8,
                     "endpoint_length4": [0] * 6,
                     "unmonitored_histogram_length4": histogram_record(coefficient(walks, "P", "P", 4)),
                     "hit_histogram_length4": histogram_record(coefficient(walks, "P", "P", 4, final=HIT)),
                     "all_monitor_blocks_equal_independent_enumeration": True,
                     "independent_verifier_status": audit["status"],
                     "complete_coefficient_blocks": len(walks.coefficients)})
    forged_audit = verify_port_series(graph, ("P",), 8, replace(walks, coefficients={}))
    budget_audit = verify_port_series(graph, ("P",), 8, walks, enumeration_budget=0)
    if forged_audit["status"] != "REJECTED" or budget_audit["status"] != "UNVERIFIED":
        raise ArithmeticError("independent verifier accepted forged or unverified coefficients")
    suffix = suffix_context_graph()
    suffix_e = port_excursion_series(suffix, ("P", "Q", "R"), 2)
    suffix_k = compose_port_series(suffix_e)
    if coefficient(suffix_k, "P", "R", 2, final=HIT).total_mass != Fraction(2, 5):
        raise ArithmeticError("future suffix failed to preserve the monitor boundary")
    cyclic = branching_hidden_cycle_graph()
    cyclic_k = compose_port_series(port_excursion_series(cyclic, ("P",), 8))
    cyclic_enum = enumerate_port_walks(cyclic, ("P",), 8)
    if cyclic_k.coefficients != cyclic_enum.coefficients:
        raise ArithmeticError("hidden-cycle finite coefficients disagree")
    incomplete = port_excursion_series(blind_pair()[0], ("P",), 4, budget=0)
    refused = False
    try:
        coefficient(incomplete, "P", "P", 4)
    except ValueError:
        refused = True
    if incomplete.status != "INCOMPLETE" or not refused:
        raise ArithmeticError("partial empty dictionary was accepted as a zero transfer")
    return {
        "schema": "OWNER_NATIVE_PATH_MONITOR_FINITE_CERTIFICATE_V1",
        "scope": "noncanonical T0/T6 consumer; raw signed X6, declared finite horizons only",
        "t6_partition_sizes": monitor.partition_sizes,
        "excursion_minimum_length": 1,
        "length_zero_semantics": "complete-walk identity only",
        "blind_pair": pair,
        "future_suffix": {
            "ports": ["P", "Q", "R"], "prefix": [1], "suffix": [-1],
            "suffix_hit_with_initial_plus_E1": histogram_record(coefficient(suffix_e, "Q", "R", 1, 1, HIT)),
            "suffix_hit_with_reset_initial": histogram_record(coefficient(suffix_e, "Q", "R", 1, START, HIT)),
            "composed_hit": histogram_record(coefficient(suffix_k, "P", "R", 2, final=HIT)),
        },
        "hidden_cycle": {"horizon": 8, "complete_monitor_blocks": len(cyclic_k.coefficients),
                         "explicit_port_path_witnesses": len(cyclic_enum.witnesses), "all_blocks_equal": True},
        "independent_verification_boundary": {
            "forged_complete_empty_coefficients": forged_audit["status"],
            "enumeration_budget_zero": budget_audit["status"],
            "enumeration_budget_zero_process_status": budget_audit["enumeration_status"],
            "complete_label_alone_is_not_verification": True,
            "coefficient_function_is_convenience_readout_only": True,
        },
        "budget_exhaustion": {"status": incomplete.status, "coefficient_count": len(incomplete.coefficients),
                              "incomplete_readout_refused": refused},
    }


if __name__ == "__main__":
    print(json.dumps(certificate(), ensure_ascii=False, indent=2))
