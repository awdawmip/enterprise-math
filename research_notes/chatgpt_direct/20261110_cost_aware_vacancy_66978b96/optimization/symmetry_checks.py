"""Finite exact checks and original-BRC witnesses for the symmetry quotient.

The four inherited small domains compare every labelled nonterminal state
visited by the old planner, then replay every static input.  Larger single-round
domains solve the exact quotient with proved lower-bound cuts and execute one
attaining static input through the original primitive kernel.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import itertools
import json
from pathlib import Path
import time

from bellman_planner import Planner, control_replay
from planner_checks import verify_events
from symmetry_planner import SymmetryPlanner, worst_static_witness


SMALL_CASES = ((2, (0,)), (2, (0, 1)), (2, (0, 0, 0, 0)), (3, (0, 1, 2, 0)))


def small_case(slots, targets):
    started = time.perf_counter()
    blank = ((0, 0),) * slots
    labelled = Planner(slots, targets)
    quotient = SymmetryPlanner(slots, targets, pruning=False)
    cut_quotient = SymmetryPlanner(slots, targets, pruning=True)
    expected = labelled.value(blank, 0)
    assert quotient.value(blank, 0) == cut_quotient.value(blank, 0) == expected
    labelled_metrics = labelled.metrics()
    quotient_metrics = quotient.metrics()
    labelled_states = tuple(labelled._decisions)
    for knowledge, position in labelled_states:
        value = labelled.value(knowledge, position)
        assert quotient.value(knowledge, position) == value
        assert cut_quotient.value(knowledge, position) == value
    assert quotient.metrics()['states'] == quotient_metrics['states']
    cost_hist = Counter()
    read_hist = Counter()
    table_count = 0
    for initial in itertools.product(range(quotient.modulus), repeat=slots):
        replay = control_replay(quotient, initial)
        verify_events(quotient, initial, blank, replay)
        assert replay['cost'] <= expected
        cost_hist[replay['cost']] += 1
        read_hist[replay['vacancy_bit_reads']] += 1
        table_count += 1
    assert max(cost_hist) == expected
    witness = worst_static_witness(quotient)
    verify_events(quotient, witness['initial_residues'], blank, witness)
    return dict(slots=slots, target_sequence=targets,
                minimax_variable_commands=expected,
                labelled_metrics=labelled_metrics,
                labelled_nonterminal_states=len(labelled_states),
                labelled_terminal_states=labelled_metrics['states'] - len(labelled_states),
                quotient_metrics_without_pruning=quotient_metrics,
                all_labelled_nonterminal_values_compared=len(labelled_states),
                pruned_and_unpruned_values_agree=True,
                initial_tables_exhausted=table_count,
                cost_histogram=dict(sorted(cost_hist.items())),
                read_histogram=dict(sorted(read_hist.items())),
                worst_static_witness=witness,
                elapsed_seconds=time.perf_counter() - started)


def distinguished_slot_check():
    left = ((0, 0), (1, 0))
    right = tuple(reversed(left))
    quotient = SymmetryPlanner(2, (0, 1))
    labelled = Planner(2, (0, 1))
    a = quotient.value(left, 0)
    b = quotient.value(right, 0)
    assert a == labelled.value(left, 0) == 28
    assert b == labelled.value(right, 0) == 20
    assert sorted(left) == sorted(right)
    # Swapping the same two patterns is valid once only the last round remains.
    c = quotient.value(left, 1)
    d = quotient.value(right, 1)
    assert c == d
    return dict(status='PASS', targets=(0, 1), left=left, right=right,
                multi_round_values=(a, b), final_round_values=(c, d),
                explanation='Identical whole-slot multisets need different values before slot zero is overwritten; only the last round merges every slot.')


def seeded_check():
    planner = SymmetryPlanner(2, (0, 1))
    knowledge = ((2, 0), (2, 0))
    value = planner.value(knowledge, 0)
    assert value == 8
    schedules = set()
    total = 0
    for initial in itertools.product((0, 1), repeat=2):
        replay = control_replay(planner, initial, knowledge)
        verify_events(planner, initial, knowledge, replay)
        assert replay['vacancy_bit_reads'] == 0 and replay['cost'] == value
        schedules.add(tuple(event['key'] for event in replay['events']
                            if event['kind'] == 'create'))
        total += 1
    assert schedules == {(3, 6)}
    return dict(status='PASS', initial_knowledge=knowledge,
                minimax_variable_commands=value, additional_bit_reads=0,
                key_schedules=sorted(schedules), initial_tables_exhausted=total)


def original_kernel_witness(planner, witness):
    import check_cost_aware_kernel as kernel
    compiler = kernel.prior.Compiler(slots=planner.slots)
    assert compiler.color_bits == planner.width
    codes = tuple(residue or compiler.modulus for residue in witness['initial_residues'])
    table = ((None,) * compiler.d,
             tuple(divmod(code - 1, compiler.colors) for code in codes))
    operations = tuple(op for target in planner.targets for op in (
        ('reserve', target), ('bind', 0, target),
        ('release', compiler.targets[target][0])))
    constant = sum(len(compiler.free_reads[target]) + (compiler.bits + 2)
                   + (8 * compiler.color_bits + compiler.bits + 10)
                   + len(compiler.programs[('release', compiler.targets[target][0])])
                   for target in planner.targets)
    checks_before = kernel.CHECKS
    _, mass, result = kernel.run_case(compiler, table, operations,
        controller_factory=lambda core: kernel.CostAwareController(core, planner=planner))
    assert mass.count == 1
    assert result['commands'] == constant + witness['cost']
    assert result['vacancy_bit_reads'] == witness['vacancy_bit_reads']
    actual_keys = [row['key'] for row in result['entries'] if row['op'][0] == 'reserve']
    planned_keys = [event['key'] for event in witness['events'] if event['kind'] == 'create']
    assert actual_keys == planned_keys
    assert all(row['physical_last_before_create'] == 1 for row in result['entries']
               if row['op'][0] == 'reserve')
    return dict(status='PASS', original_kernel_runs=1,
                initial_full_codes=codes, initial_residues=witness['initial_residues'],
                full_key_width=compiler.bits, business_constant=constant,
                variable_commands=witness['cost'], actual_commands=result['commands'],
                vacancy_bit_reads=result['vacancy_bit_reads'], selected_keys=actual_keys,
                kernel_assertions=kernel.CHECKS - checks_before,
                result=kernel.compact(result, len(operations)))


def large_case(slots):
    started = time.perf_counter()
    planner = SymmetryPlanner(slots, (0,), pruning=True)
    blank = ((0, 0),) * slots
    planning_started = time.perf_counter()
    value = planner.value(blank, 0)
    planning_seconds = time.perf_counter() - planning_started
    initial_metrics = planner.metrics()
    witness = worst_static_witness(planner)
    verify_events(planner, witness['initial_residues'], blank, witness)
    assert witness['cost'] == value
    # A b=3 comparison verifies the cuts against a fully expanded exact quotient.
    cut_check = None
    if slots == 4:
        unpruned = SymmetryPlanner(slots, (0,), pruning=False)
        check_started = time.perf_counter()
        assert unpruned.value(blank, 0) == value
        compared = 0
        for histogram, exact_value in tuple(planner.last_values.items()):
            assert unpruned._last(histogram) == exact_value
            compared += 1
        cut_check = dict(status='PASS', all_pruned_states_compared=compared,
                         unpruned_metrics=unpruned.metrics(),
                         elapsed_seconds=time.perf_counter() - check_started)
    kernel_started = time.perf_counter()
    kernel_result = original_kernel_witness(planner, witness)
    kernel_seconds = time.perf_counter() - kernel_started
    return dict(slots=slots, colors=planner.colors, width=planner.width,
                target_sequence=planner.targets,
                initial_residue_table_count=planner.modulus ** slots,
                initial_tables_exhausted=False,
                minimax_variable_commands=value,
                planner_metrics=initial_metrics,
                final_metrics=planner.metrics(),
                worst_static_witness=witness,
                exact_pruning_crosscheck=cut_check,
                original_kernel_witness=kernel_result,
                elapsed_seconds=dict(planning=planning_seconds, kernel=kernel_seconds,
                                     total=time.perf_counter() - started))


def save(output, result):
    temporary = output.with_suffix(output.suffix + '.tmp')
    temporary.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(output)


def run(output):
    started = time.perf_counter()
    result = dict(status='RUNNING', model='EXACT_SLOT_SYMMETRY_BELLMAN_QUOTIENT',
        generated_at_utc=datetime.now(timezone.utc).isoformat(),
        checked_implementation='symmetry_planner.py',
        variable_units='8 per newly observed request bit plus complete-key-dependent creation/binding weight',
        preservation='Slot zero is distinguished before the final round; every histogram query reads exactly one physical slot.',
        pruning='Final-round exact lower bounds only; every old small-domain state is compared with the labelled recurrence, and r=4 is also compared with the unpruned b=3 quotient.',
        scope='Exact quotient solutions; exhaustive static control inputs only for the four inherited small domains and the seed. One attaining original-BRC execution for each of r=4,5,6.',
        small_cases=[], larger_single_round_cases=[])
    save(output, result)
    try:
        for slots, targets in SMALL_CASES:
            row = small_case(slots, targets)
            result['small_cases'].append(row)
            save(output, result)
            print(json.dumps(dict(kind='small', slots=slots, targets=targets,
                                  value=row['minimax_variable_commands'],
                                  labelled_states=row['labelled_metrics']['states'],
                                  quotient_states=row['quotient_metrics_without_pruning']['states'])), flush=True)
        result['distinguished_slot_regression'] = distinguished_slot_check()
        result['observed_high_bit_seed'] = seeded_check()
        save(output, result)
        for slots in (4, 5, 6):
            row = large_case(slots)
            result['larger_single_round_cases'].append(row)
            save(output, result)
            print(json.dumps(dict(kind='single_round', slots=slots,
                                  value=row['minimax_variable_commands'],
                                  states=row['planner_metrics']['nonterminal_states'],
                                  actual_commands=row['original_kernel_witness']['actual_commands'],
                                  planning_seconds=row['elapsed_seconds']['planning'])), flush=True)
    except Exception as error:
        result['status'] = 'FAILED'
        result['error'] = dict(type=type(error).__name__, message=str(error))
        result['elapsed_seconds'] = time.perf_counter() - started
        save(output, result)
        raise
    result['status'] = 'PASS'
    result['total_small_initial_tables_exhausted'] = sum(
        row['initial_tables_exhausted'] for row in result['small_cases']) + result['observed_high_bit_seed']['initial_tables_exhausted']
    result['total_labelled_nonterminal_values_compared'] = sum(
        row['all_labelled_nonterminal_values_compared'] for row in result['small_cases'])
    result['original_kernel_runs'] = len(result['larger_single_round_cases'])
    result['elapsed_seconds'] = time.perf_counter() - started
    save(output, result)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('symmetry_results.json'))
    args = parser.parse_args()
    outcome = run(args.output)
    print(json.dumps(dict(status=outcome['status'],
                          small_tables=outcome['total_small_initial_tables_exhausted'],
                          labelled_states_compared=outcome['total_labelled_nonterminal_values_compared'],
                          original_kernel_runs=outcome['original_kernel_runs'],
                          elapsed_seconds=outcome['elapsed_seconds'])), flush=True)
