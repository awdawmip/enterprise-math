"""Exact original-command horizon comparison for the two-cluster family."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import check_region_certificate as regional


def check():
    rows = []
    comparisons = 0
    for slots in (6, 14):
        C = regional.prior.Compiler(slots=slots)
        half = slots//2
        crossover = 8*(half-1)
        rounds = crossover+2
        codes = (2,)*half+(3,)*half
        table = ((None,)*C.d, tuple(divmod(code-1, C.colors) for code in codes))
        operations = (('reserve', 0), ('bind', 0, 0), ('release', 1))*rounds
        outputs = {}
        semantic = None
        for strategy, runner in (('single_point', regional.directed.run_case),
                                 ('tracked_region', regional.run_case)):
            _, mass, result = runner(C, table, operations)
            assert mass.count == 1
            if semantic is None:
                semantic = result['semantic_prefixes']
            else:
                assert result['semantic_prefixes'] == semantic
            cumulative = 0
            by_round = []
            for index in range(rounds):
                reserve, bind, release = result['entries'][3*index:3*index+3]
                cumulative += sum(entry['commands'] for entry in (reserve, bind, release))
                expected_key = 1 if index % 2 == 0 else (4 if strategy == 'single_point' else 5)
                assert reserve['key'] == expected_key
                assert reserve['physical_last_before_create'] == 1
                reads = 3*half if index == 0 else (half-1 if index == 1 and strategy == 'single_point' else 0)
                assert reserve['vacancy_bit_reads'] == reads
                assert len(C.reads[0, 0]) == 8
                expected_reserve = (len(C.free_reads[0])+8*reads+
                                    len(C.create_words[0, expected_key-1, 1]))
                assert reserve['commands'] == expected_reserve
                by_round.append(dict(round=index+1, key=reserve['key'],
                                     create_with_conflict_and_query=reserve['commands'],
                                     bind=bind['commands'], release=release['commands'],
                                     vacancy_bit_reads=reads, cumulative_commands=cumulative))
            outputs[strategy] = dict(commands=result['commands'],
                                     vacancy_bit_reads=result['vacancy_bit_reads'],
                                     by_round=by_round)
        differences = []
        for index in range(rounds):
            a = outputs['single_point']['by_round'][index]
            b = outputs['tracked_region']['by_round'][index]
            horizon = index+1
            expected = 0 if horizon == 1 else 2*(horizon//2)-8*(half-1)
            actual = b['cumulative_commands']-a['cumulative_commands']
            assert actual == expected
            if index % 2:
                assert b['bind']-a['bind'] == 1
                assert b['create_with_conflict_and_query']-a['create_with_conflict_and_query'] == (
                    1-8*(half-1) if index == 1 else 1)
            assert b['release'] == a['release']
            comparisons += 1
            differences.append(dict(horizon=horizon, difference=actual,
                                    single_point=a['cumulative_commands'],
                                    tracked_region=b['cumulative_commands']))
        wanted = set(range(1, 6)) | {crossover-1, crossover, crossover+1, crossover+2}
        rows.append(dict(slots=slots, width=C.color_bits, full_key_bits=C.bits,
                         initial_codes=codes, completed_rounds=rounds,
                         first_query_bits=3*half, extra_point_bits=half-1,
                         equal_cost_horizons=[crossover, crossover+1],
                         selected_horizons=[row for row in differences if row['horizon'] in wanted],
                         all_horizon_differences=differences,
                         primitive_word_lengths=outputs,
                         members=C.members, candidates=len(C.H)))
    return dict(status='PASS', mode='horizon_costs', formula='T=1: 0; T>=2: 2*floor(T/2)-8*(r/2-1)',
                difference_direction='tracked_region minus single_point',
                family='r=2^b-2, b>=3; half of initial request keys 2, half 3; overwrite slot 0 each round',
                actual_prefix_comparisons=comparisons, completed_original_kernel_runs=4,
                rows=rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = check()
    text = json.dumps(result, ensure_ascii=False, indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')
