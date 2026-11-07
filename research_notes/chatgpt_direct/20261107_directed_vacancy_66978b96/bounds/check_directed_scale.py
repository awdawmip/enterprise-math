"""Control-only scaling of the actual PrefixTree and the old quota search.

Known full request values are confined to this test harness as observation
callbacks and invariant oracles.  No physical BRC cost is inferred here.
"""
from __future__ import annotations

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / 'directed'))
import check_directed_vacancy as implementation

old = implementation.old
prior = old.prior


def retained_prefixes(r: int, rounds: int, *, empty: bool = False) -> dict:
    b, B, M = r.bit_length(), 1 << r.bit_length(), r + 1
    values = [0]*r if empty else list(range(1, r+1))
    labels = [old.Prefix(initial_slot=i) for i in range(r)]
    holes = None
    queries = cached = classifications = color_tests = certifications = 0
    entries = []
    pairs = set()
    for turn in range(rounds):
        q0, c0 = queries, cached
        covered = False
        if holes is not None:
            for c in range(M):
                color_tests += 1
                if (1+c) % B in holes:
                    covered = True
                    break
        if not covered:
            state = prior.start_search(r)
            while state.task is not None:
                slot, bit = state.task.active[state.at], state.task.level
                label = labels[slot]
                if bit < label.depth:
                    value = (label.value >> bit) & 1
                    cached += 1
                else:
                    # The callback supplies exactly the queried low bit.
                    value = (values[slot] >> bit) & 1
                    assert label.initial_slot is not None
                    pair = (label.initial_slot, bit)
                    assert pair not in pairs
                    pairs.add(pair)
                    label.accept(bit, value)
                    queries += 1
                state = prior.accept_bit(state, value, b)
                classifications += 1
            holes = state.holes
            certifications += 1
        for c in range(M):
            color_tests += 1
            if (1+c) % B in holes:
                break
        else:
            raise AssertionError('No target color in quota certificate')
        code = 1+c
        assert code % B not in {x % B for x in values}
        # Existing bind supplies this known code. No simulated BRC command cost.
        values[0] = code
        labels[0] = old.Prefix(b, code % B)
        holes = tuple(h for h in holes if h != code % B)
        assert queries <= r*b
        entries.append(dict(round=turn+1, selected_key=code,
                            additional_reads=queries-q0, cached_bit_replays=cached-c0))
    return dict(strategy='retained_prefixes_with_rebuilt_quota_search',
                initial_labels=r, cumulative_additional_reads=queries,
                cached_bit_replays=cached, partition_label_events=classifications,
                certificate_color_tests=color_tests, certificates=certifications,
                known_slot_writes=rounds,
                callback_business_low_bits=rounds*b, entries=entries)


def maintained_tree(r: int, rounds: int, *, empty: bool = False) -> dict:
    b, B, M = r.bit_length(), 1 << r.bit_length(), r + 1
    values = [0]*r if empty else list(range(1, r+1))
    tree = implementation.PrefixTree(r, b)
    queries = node_visits = candidate_queries = selected_branches = 0
    entries, pairs = [], set()
    for turn in range(rounds):
        q0, v0, p0 = queries, node_visits, tree.events['business_path_touches']
        level = prefix = first = 0
        cap = M
        while True:
            node_visits += 1
            index = tree.index(level, prefix)
            n = tree.count[index]
            assert cap > n
            if not n:
                break
            assert level < b
            while tree.head[index] is not None:
                label = tree.head[index]
                assert label.initial_slot is not None
                pair = (label.initial_slot, level)
                assert pair not in pairs
                pairs.add(pair)
                # The production tree receives only this actual requested bit.
                value = (values[label.representative] >> level) & 1
                tree.observe_next(label, value)
                queries += 1
            eligible = []
            for bit in (0, 1):
                child = prefix | (bit << level)
                count = tree.count[tree.index(level+1, child)]
                capacity, initial = implementation.Controller.capacity(1, M, level+1, child)
                candidate_queries += 1
                if count < capacity:
                    eligible.append((count, bit, capacity, initial))
            count, bit, cap, first = min(eligible)
            selected_branches += 1
            prefix |= bit << level
            level += 1
        code = 1+first
        assert 0 <= first < M
        assert code % B not in {x % B for x in values}
        # Original business interface has already supplied the known code.
        tree.known_write(0, code)
        values[0] = code
        assert queries <= r*b

        # Verification scans are not charged to the production controller.
        want = [0]*len(tree.count)
        live = set(tree.labels)
        for label in live:
            assert label.value == values[label.representative] % (1 << label.depth)
            for ell in range(label.depth+1):
                want[tree.index(ell, label.value % (1 << ell))] += 1
        assert tree.count == want
        assert len(live) == tree.live_labels <= r
        entries.append(dict(round=turn+1, selected_key=code,
                            additional_reads=queries-q0,
                            query_node_visits=node_visits-v0,
                            business_path_touches=tree.events['business_path_touches']-p0))
    return dict(strategy='actual_PrefixTree_with_test_observation_callbacks',
                cumulative_additional_reads=queries,
                cached_bit_replays=0,
                query_node_visits=node_visits,
                candidate_count_queries=candidate_queries,
                selected_branches=selected_branches,
                tree_events=dict(tree.events),
                final_tree_metrics=tree.metrics(),
                callback_business_low_bits=rounds*b,
                entries=entries)


def main() -> None:
    rows = []
    cases = [(r, False) for r in (14, 30, 62)] + [(r, True) for r in (7, 31, 127)]
    for r, empty in cases:
        old_result = retained_prefixes(r, 32, empty=empty)
        new_result = maintained_tree(r, 32, empty=empty)
        assert [x['selected_key'] for x in old_result['entries']] == [
            x['selected_key'] for x in new_result['entries']]
        assert all(x['additional_reads'] == 0 for x in old_result['entries'][2:])
        assert all(x['additional_reads'] == 0 for x in new_result['entries'][2:])
        if empty:
            b = r.bit_length()
            assert old_result['cumulative_additional_reads'] == new_result['cumulative_additional_reads'] == r
            assert old_result['cached_bit_replays'] == 31*(r+1)
            assert new_result['query_node_visits'] == 95
            assert new_result['candidate_count_queries'] == 126
            assert new_result['tree_events']['business_path_touches'] == 63*b+65
            assert [x['selected_key'] for x in new_result['entries']] == [1,3]*16
        rows.append(dict(slots=r, rounds=32, pattern='reserve target0; bind slot0; release source',
                         preparation='all_empty' if empty else 'retained_keys_1_to_r',
                         old=old_result, directed=new_result))
    result = dict(status='PASS', physical_BRC_execution=False,
                  scope='Control callbacks and exact bookkeeping; stated initial requests; same selected full keys',
                  production_tree_source='directed/check_directed_vacancy.py:PrefixTree',
                  baseline_search_source='parent_bundle/check_batch_vacancy.py:start_search/accept_bit',
                  accounting='Separate event counts, not a combined time or primitive-command score; test invariant scans excluded',
                  rows=rows)
    out = ROOT/'directed_scale_checks.json'
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', rows=[dict(
        r=x['slots'], preparation=x['preparation'], old_extra_reads=x['old']['cumulative_additional_reads'],
        new_extra_reads=x['directed']['cumulative_additional_reads'],
        old_cached_replays=x['old']['cached_bit_replays'],
        new_query_nodes=x['directed']['query_node_visits'],
        new_candidate_queries=x['directed']['candidate_count_queries'],
        new_update_paths=x['directed']['tree_events']['business_path_touches'])
        for x in rows]), ensure_ascii=False))


if __name__ == '__main__':
    main()
