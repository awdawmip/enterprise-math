"""Exact integer-control checks for target-directed absence search.

This checker uses residue tables as an oracle solely to check the search rule.
It does not execute or replace the original triadic/BRC reader. Physical runs
belong to directed/check_directed_vacancy.py in the sibling implementation.
"""
from __future__ import annotations

from itertools import combinations_with_replacement, product
from pathlib import Path
import argparse
import json


def capacity(start: int, size: int, level: int, prefix: int) -> tuple[int, int]:
    """Number of legal colors in this low-prefix node and the first color."""
    modulus = 1 << level
    first = (prefix - start) % modulus
    count = 0 if first >= size else 1 + (size - 1 - first) // modulus
    return count, first


def bound(labels: int) -> int:
    return 2 * labels - labels.bit_count()


def search(residues: tuple[int, ...], start: int, r: int,
           depths: tuple[int, ...] | None = None, policy: str = "min_count") -> dict:
    """Oracle simulation of one directed branch, counting new observations.

    `depths` supplies already observed prefix lengths of the source labels.
    All exact residue access occurs here as test oracle feedback.
    """
    b = r.bit_length()
    size = r + 1
    depths = (0,) * len(residues) if depths is None else depths
    assert len(residues) <= r and len(depths) == len(residues)
    assert all(0 <= d <= b for d in depths)
    active = tuple(range(len(residues)))
    level = prefix = queries = logical_bits = 0
    trace, pairs = [], []
    while True:
        count, first = capacity(start, size, level, prefix)
        assert count > len(active), (count, len(active), level, prefix)
        assert len(active) <= r // (1 << level)
        if not active:
            return dict(reads=queries, logical_partition_bits=logical_bits,
                        color=first, residue=(start + first) % (1 << b),
                        depth=level, trace=trace, queried_pairs=pairs)
        assert level < b
        groups = [tuple(i for i in active if (residues[i] >> level) & 1 == v)
                  for v in (0, 1)]
        capacities = [capacity(start, size, level + 1,
                               prefix | (v << level))[0] for v in (0, 1)]
        assert sum(capacities) == count and abs(capacities[0] - capacities[1]) <= 1
        eligible = [v for v in (0, 1) if len(groups[v]) < capacities[v]]
        assert eligible
        if policy == "min_count":
            chosen = min(eligible, key=lambda v: (len(groups[v]), v))
            assert len(groups[chosen]) <= len(active) // 2
        elif policy == "max_count":
            chosen = max(eligible, key=lambda v: (len(groups[v]), -v))
        else:
            raise ValueError(policy)
        new = [(i, level) for i in active if depths[i] <= level]
        queries += len(new)
        logical_bits += len(active)
        pairs.extend(new)
        trace.append(dict(level=level, prefix=prefix, capacity=count,
                          labels=len(active), new_reads=len(new),
                          child_capacities=capacities,
                          child_labels=[len(g) for g in groups],
                          eligible=eligible, chosen=chosen))
        active = groups[chosen]
        prefix |= chosen << level
        level += 1


def best_deficit_path(residues: tuple[int, ...], start: int, r: int,
                      level: int = 0, prefix: int = 0) -> tuple[int, tuple[int, ...]]:
    """Clairvoyant comparison: best eligible branch with full test-table access.

    This is an explanatory oracle, not a proposed implementable decision rule.
    """
    if not residues:
        return 0, ()
    choices = []
    for v in (0, 1):
        child = tuple(x for x in residues if (x >> level) & 1 == v)
        p = prefix | (v << level)
        if len(child) < capacity(start, r + 1, level + 1, p)[0]:
            cost, path = best_deficit_path(child, start, r, level + 1, p)
            choices.append((len(residues) + cost, (v,) + path))
    return min(choices)


def check_candidate_formula(max_r: int = 31) -> dict:
    cells = 0
    for r in range(1, max_r + 1):
        b = r.bit_length()
        for start in range(1 << b):
            for level in range(b + 1):
                for prefix in range(1 << level):
                    count, first = capacity(start, r + 1, level, prefix)
                    actual = [c for c in range(r + 1)
                              if (start + c) % (1 << level) == prefix]
                    assert count == len(actual)
                    assert not actual or first == actual[0]
                    assert count <= r // (1 << level) + 1
                    cells += 1
    return dict(max_r=max_r, all_target_start_residues=True,
                all_low_prefix_nodes=True, checked_cells=cells)


def exhaustive(max_r: int = 7) -> dict:
    rows = []
    total = full_initial = cached = 0
    for r in range(1, max_r + 1):
        b, maximum, cases, full_cases = r.bit_length(), 0, 0, 0
        by_q = []
        for q in range(r + 1):
            qmax = qcases = 0
            for residues in combinations_with_replacement(range(1 << b), q):
                for start in range(1 << b):
                    result = search(residues, start, r)
                    assert 0 <= result['color'] < r + 1
                    assert result['residue'] not in residues
                    assert result['reads'] <= bound(q) <= bound(r)
                    assert len(result['queried_pairs']) == len(set(map(tuple, result['queried_pairs'])))
                    qmax = max(qmax, result['reads'])
                    maximum = max(maximum, result['reads'])
                    qcases += 1
                    if q == r:
                        full_cases += 1
                    if r <= 3:
                        for depths in product(range(b + 1), repeat=q):
                            partial = search(residues, start, r, depths)
                            assert partial['color'] == result['color']
                            assert partial['reads'] <= result['reads'] <= bound(q)
                            assert all(level >= depths[label]
                                       for label, level in partial['queried_pairs'])
                            cached += 1
            assert qmax <= bound(q)
            cases += qcases
            by_q.append(dict(source_labels=q, cases=qcases, maximum_reads=qmax,
                             folding_bound=bound(q)))
        assert maximum == bound(r)
        total += cases
        full_initial += full_cases
        rows.append(dict(request_slots=r, low_width=b, cases=cases,
                         full_initial_slot_cases=full_cases,
                         maximum_reads=maximum, exact_worst_bound=bound(r),
                         source_label_counts=by_q))
    return dict(max_r=max_r, query_cases=total,
                full_initial_slot_cases=full_initial,
                cached_prefix_cases=cached, rows=rows)


def attaining_witnesses(max_r: int = 255) -> dict:
    cases, selected = 0, []
    for r in range(1, max_r + 1):
        b = r.bit_length()
        for start in sorted({0, 1, (1 << b) - 1, 12345}):
            # All but the last legal color are retained; the last is free.
            residues = tuple((start + c) % (1 << b) for c in range(r))
            result = search(residues, start, r)
            assert result['reads'] == bound(r)
            assert result['color'] == r
            assert [step['labels'] for step in result['trace']] == [
                r // (1 << j) for j in range(b)]
            # Any choice among deficient children follows the same unique path.
            assert all(len(step['eligible']) == 1 for step in result['trace'])
            assert search(residues, start, r, policy='max_count')['reads'] == bound(r)
            cases += 1
            if start == 1 and r in (1, 2, 3, 6, 7, 14, 15, 20, 30, 31, 62, 63, 126, 127, 254, 255):
                selected.append(dict(request_slots=r, target_start=start,
                                     request_key_interval=[start, start+r-1],
                                     free_key=start+r, reads=result['reads'],
                                     layer_counts=[x['labels'] for x in result['trace']]))
    return dict(max_r=max_r, checked_witnesses=cases, selected=selected)


def local_choice_examples() -> list[dict]:
    examples = [
        ('equal_child_counts_hide_different_future_costs',
         14, tuple(sorted((1, 5, 9) + (2,) * 8 + (3,) * 3))),
        ('strictly_smaller_child_can_have_more_total_reads',
         20, tuple(sorted((1,) * 5 + (2,) * 11 + (3, 7, 11, 15)))),
    ]
    rows = []
    for name, r, vals in examples:
        greedy = search(vals, 1, r)
        optimal, path = best_deficit_path(vals, 1, r)
        assert greedy['reads'] > optimal
        rows.append(dict(name=name, slots=r, target_start=1,
                         request_residues=vals, greedy_reads=greedy['reads'],
                         best_deficit_path_reads=optimal,
                         greedy_trace=greedy['trace'],
                         oracle_best_path=path,
                         comparison_scope='Pointwise full-information oracle only; no implementable superiority claim'))
    assert (rows[0]['greedy_reads'], rows[0]['best_deficit_path_reads']) == (24, 23)
    assert (rows[1]['greedy_reads'], rows[1]['best_deficit_path_reads']) == (36, 34)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-r', type=int, default=7)
    parser.add_argument('--out', default=str(Path(__file__).with_name('directed_bounds_checks.json')))
    args = parser.parse_args()
    result = dict(status='PASS', physical_BRC_execution=False,
                  scope='Exact integer control, full residue tables used only as test oracle',
                  candidate_formula=check_candidate_formula(),
                  exhaustive=exhaustive(args.max_r),
                  attaining_witnesses=attaining_witnesses(),
                  local_choice_examples=local_choice_examples())
    Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(status=result['status'],
                          candidate_cells=result['candidate_formula']['checked_cells'],
                          query_cases=result['exhaustive']['query_cases'],
                          full_initial_slot_cases=result['exhaustive']['full_initial_slot_cases'],
                          cached_prefix_cases=result['exhaustive']['cached_prefix_cases'],
                          witnesses=result['attaining_witnesses']['checked_witnesses'],
                          counterexamples=[(x['slots'], x['greedy_reads'], x['best_deficit_path_reads'])
                                           for x in result['local_choice_examples']]), ensure_ascii=False))


if __name__ == '__main__':
    main()
