"""Finite exact checks for weighted mask-region selection; control-only scope.

The original-word section inspects actual compiler-produced word lengths.
Physical BRC execution is recorded by the companion kernel integration.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from itertools import product, combinations
from pathlib import Path
import json
import random
import sys

from selector import (MaskSpec, WeightedFreeIndexTree, WeightedRegionEvidence,
                      MaskedRegionEvidence, TargetWindow, minimum_in_mask,
                      choose_empty_prefix, choose_observed_prefix,
                      round_key_cost, fixed_region_schedule)

ROOT = Path(__file__).resolve().parents[1]
COUNTS = Counter()


def check(value, label):
    COUNTS[label] += 1
    if not value:
        raise AssertionError(label)


def all_specs(width):
    for pattern in product((-1, 0, 1), repeat=width):
        mask = sum(1 << bit for bit, value in enumerate(pattern) if value >= 0)
        value = sum(1 << bit for bit, value in enumerate(pattern) if value == 1)
        yield MaskSpec.make(width, mask, value)


def reference_key(free, width, start, colors):
    candidates = (key for key in range(start, start+colors) if key % (1 << width) in free)
    return min(candidates, key=lambda key: (round_key_cost(key, width), key), default=None)


def check_profiles():
    profiles = queries = ranks = transitions = 0
    max_query_visits = 0
    for width in range(1, 4):
        B = 1 << width
        windows = [TargetWindow.make(width, start, colors)
                   for start in range(1, 4*B+1) for colors in range(1, B+1)]
        for spec in all_specs(width):
            residues = [spec.unpack(j) for j in range(spec.size)]
            check(residues == sorted(residues), 'free-bit unpacking is monotone')
            check([spec.pack(x) for x in residues] == list(range(spec.size)), 'pack/unpack inverse')
            for bound in range(-1, B+1):
                check(spec.rank_le(bound) == sum(x <= bound for x in residues), 'rank_le exact')
                ranks += 1
            for occupancy in range(1 << spec.size):
                tree = WeightedFreeIndexTree(len(spec.free_positions),
                                              negative_top=spec.negative_top)
                free = set(residues)
                for index, residue in enumerate(residues):
                    if occupancy >> index & 1:
                        before = tree.events['update_visits']
                        tree.set_free(index, False)
                        check(tree.events['update_visits']-before <= tree.width+1,
                              'point update visits <= d+1')
                        free.remove(residue)
                        transitions += 1
                check(tree.free_count == len(free), 'available count exact')
                for window in windows:
                    before = tree.events['query_visits']
                    got = minimum_in_mask(tree, spec, window)
                    visits = tree.events['query_visits']-before
                    check(got == reference_key(free, width, window.start, window.colors),
                          'all small-mask interval minima exact')
                    check(visits <= len(window.pieces)*(4*tree.width+1),
                          'range minimum visits <= 4d+1 per piece')
                    max_query_visits = max(max_query_visits, visits)
                    queries += 1
                for index, residue in reversed(list(enumerate(residues))):
                    tree.set_free(index, True)
                    free.add(residue)
                    check(tree.free_count == len(free), 'restoration count exact')
                    transitions += 1
                check(tree.root is None, 'complete restoration coalesces to implicit free root')
                profiles += 1
    return dict(widths=[1, 2, 3], mask_class_occupancy_profiles=profiles,
                complete_positive_key_intervals=queries, rank_comparisons=ranks,
                point_updates=transitions, max_observed_query_node_visits=max_query_visits,
                domain='Every ternary fixed/free-bit mask, every occupied subset, start=1..4B, colors=1..B')


def check_large_windows():
    rng = random.Random(20261110)
    profiles = queries = 0
    carries = []
    for width in range(4, 10):
        B = 1 << width
        for _ in range(80):
            mask = rng.randrange(B)
            spec = MaskSpec.make(width, mask, rng.randrange(B) & mask)
            tree = WeightedFreeIndexTree(len(spec.free_positions), negative_top=spec.negative_top)
            free = set()
            for index in range(spec.size):
                if rng.randrange(3):
                    free.add(spec.unpack(index))
                else:
                    tree.set_free(index, False)
            for quotient in (0, 1, 3, 7, 31, 127):
                colors = rng.randrange(1, B+1)
                start = max(1, (quotient+1)*B-rng.randrange(colors))
                window = TargetWindow.make(width, start, colors)
                got = minimum_in_mask(tree, spec, window)
                want = reference_key(free, width, start, colors)
                check(got == want, 'larger windows and high-quotient carries exact')
                queries += 1
                if len(window.pieces) == 2 and got is not None and len(carries) < 8:
                    carries.append(dict(width=width, mask=mask, value=spec.value,
                                        start=start, colors=colors, key=got,
                                        key_cost=round_key_cost(got, width)))
            profiles += 1
    return dict(seed=20261110, widths=list(range(4, 10)), profiles=profiles,
                queries=queries, representative_carries=carries)


def check_prefix_adapters():
    empty_queries = observed_queries = states = 0
    for width in range(1, 5):
        B = 1 << width
        for level in range(width+1):
            for prefix in range(1 << level):
                free = {residue for residue in range(B) if residue % (1 << level) == prefix}
                for start in range(1, 2*B+1):
                    for colors in range(1, B+1):
                        got = choose_empty_prefix(width, level, prefix, start, colors)
                        check(got == reference_key(free, width, start, colors),
                              'empty-low-prefix adapter exact across carry')
                        empty_queries += 1
    sys.path.insert(0, str(ROOT / 'directed'))
    from check_directed_vacancy import PrefixTree
    for width in range(1, 4):
        B = 1 << width
        partials = [(level, prefix) for level in range(width+1) for prefix in range(1 << level)]
        for slots in (1, 2):
            for rows in product(partials, repeat=slots):
                tree = PrefixTree(slots, width)
                for slot, (level, prefix) in enumerate(rows):
                    for bit in range(level):
                        tree.observe_next(tree.labels[slot], (prefix >> bit) & 1)
                free = {residue for residue in range(B)
                        if all(residue % (1 << level) != prefix for level, prefix in rows)}
                for start in range(1, 2*B+1):
                    for colors in range(1, B+1):
                        got = choose_observed_prefix(tree, start, colors)
                        check(got == reference_key(free, width, start, colors),
                              'observed-prefix chooser uses exactly provable absence')
                        observed_queries += 1
                states += 1
    return dict(empty_prefix_queries=empty_queries, observed_partial_label_states=states,
                observed_prefix_queries=observed_queries,
                domain='Empty low prefixes b=1..4; all one/two-label prefix states b=1..3; all positive windows start=1..2B, colors=1..B')


def check_region_updates():
    states = updates = 0
    for width in (1, 2):
        B = 1 << width
        for spec in all_specs(width):
            for codes in product(range(2*B+1), repeat=2):
                ops = ([('bind', slot, code) for slot in range(2) for code in range(2*B+1)]
                       + [('copy', a, b) for a in range(2) for b in range(2)]
                       + [('drop', slot) for slot in range(2)])
                for op in ops:
                    region = MaskedRegionEvidence(2, width)
                    region.acquire_mask(spec.mask, spec.value)
                    table = list(codes)
                    for slot, code in enumerate(codes):
                        region.bind(slot, code)
                    if op[0] == 'bind':
                        region.bind(op[1], op[2]); table[op[1]] = op[2]
                    elif op[0] == 'copy':
                        region.copy(op[1], op[2]); table[op[1]] = table[op[2]]
                    else:
                        region.drop(op[1]); table[op[1]] = 0
                    marks = [code % B if code and spec.contains(code % B) else None for code in table]
                    counts = Counter(x for x in marks if x is not None)
                    check(region.members == marks, 'masked slot marks exact after update')
                    check(region.refs == counts, 'masked reference multiplicities exact')
                    free = {x for x in range(B) if spec.contains(x) and x not in counts}
                    check(region.tree.free_count == len(free), 'masked free cardinality exact')
                    for start in (1, B, B+1, 2*B-1):
                        got = region.select_key(start, B)
                        check(got == reference_key(free, width, start, B), 'masked choice after slot update exact')
                    updates += 1
                states += 1
    return dict(widths=[1, 2], slots=2, states=states, one_step_updates=updates,
                domain='All masks; all two-slot full codes 0..2B; bind/copy/drop, including aliases and nonempty residue zero')


def check_original_word_weights():
    sys.path.insert(0, str(ROOT / 'future'))
    import check_prefix_certificate as inherited
    rows = []
    constructions = 0
    for slots in (1, 2, 3, 6, 7, 14):
        C = inherited.prior.Compiler(slots=slots)
        b, q = C.color_bits, C.bits
        for target in range(C.d):
            release = len(C.programs[('release', min(C.targets[target]))])
            for color in range(C.colors):
                K = C.key(target, color)
                bind_last = (K >> (b-1)) & 1
                binding = (len(C.presence_reads[target])+sum(len(C.cache_reads[target, bit]) for bit in range(b))
                           + len(C.address_writes[0, K, bind_last]))
                check(binding == 8*b+q+10+K.bit_count()+4*(1-bind_last), 'compiler binding cost exact')
                for physical_last in (0, 1):
                    actual = len(C.free_reads[target])+len(C.create_words[target, color, physical_last])+binding+release
                    fixed = len(C.free_reads[target])+8*b+2*q+12+release+4*(1-physical_last)
                    check(actual == fixed+round_key_cost(K, b), 'full compiler word cost decomposes exactly')
                    constructions += 1
        rows.append(dict(slots=slots, targets=C.d, key_width=q, residue_width=b,
                         legal_keys=C.d*C.colors))
    return dict(kind='COMPILER_WORD_LENGTH_CHECK', constructed_round_words=constructions, rows=rows,
                physical_execution='Companion kernel runs, not this component check')


def check_fixed_schedules():
    cases = 0
    for width in (1, 2, 3):
        universe = range(1, 1 << width)
        for size in range(1, min(4, len(universe))+1):
            for keys in combinations(universe, size):
                @lru_cache(None)
                def optimum(rounds, previous):
                    if not rounds:
                        return 0
                    costs = [round_key_cost(key, width)+optimum(rounds-1, key)
                             for key in keys if key != previous]
                    return min(costs, default=float('inf'))
                for previous in (None, *keys):
                    for rounds in range(9):
                        seq = fixed_region_schedule(keys, width, rounds, previous)
                        cost = float('inf') if seq is None else sum(round_key_cost(key, width) for key in seq)
                        check(cost == optimum(rounds, previous), 'two-cheapest greedy equals exact fixed-target DP')
                        cases += 1
    return dict(cases=cases, widths=[1, 2, 3], max_safe_keys=4, horizons=list(range(9)),
                domain='All positive legal-key subsets of size <=4; initial previous absent or any key')


def future_target_witness():
    width, colors = 2, 3
    free = frozenset((2, 3))
    targets = (0, 1)
    @lru_cache(None)
    def optimum(position, previous):
        if position == len(targets):
            return 0, ()
        start = 1+targets[position]*colors
        choices = []
        for key in range(start, start+colors):
            residue = key % (1 << width)
            if residue not in free or residue == previous:
                continue
            suffix, seq = optimum(position+1, residue)
            choices.append((round_key_cost(key, width)+suffix, (key,)+seq))
        return min(choices, default=(float('inf'), ()))
    greedy = []
    previous = None
    for target in targets:
        candidates = [key for key in range(1+target*colors, 1+(target+1)*colors)
                      if key % (1 << width) in free and key % (1 << width) != previous]
        if not candidates:
            greedy.append(None)
            break
        key = min(candidates, key=lambda key: (round_key_cost(key, width), key))
        greedy.append(key); previous = key % (1 << width)
    best, sequence = optimum(0, None)
    check(greedy == [2, None] and sequence == (3, 6) and best == 8,
          'future-target DP avoids a myopic regional miss')
    return dict(width=width, colors=colors, certified_region=sorted(free), targets=list(targets),
                myopic_keys=greedy, optimal_no_read_keys=list(sequence),
                optimal_key_dependent_commands=best,
                interpretation='At the second target myopic regional evidence misses; a planner keeps coverage without a new observation')


def carry_witness():
    region = MaskedRegionEvidence(7, 3)
    region.acquire_mask(1, 0)
    key = region.select_key(57, 8)
    check(key == 64 and round_key_cost(60, 3) == 8 and round_key_cost(64, 3) == 6,
          'complete-key carry changes the least-cost choice')
    return dict(width=3, colors=8, target=7, certified_mask=1, certified_value=0,
                legal_interval=[57,64], selected_key=key,
                alternatives=[{'key':60,'residue':4,'cost':8},{'key':64,'residue':0,'cost':6}])


def examples():
    rows=[]
    for width in (3, 4, 5, 6):
        H=1 << (width-1);B=2*H
        for name,mask,value in [('odd_low_class',3,1),('even_low_class',3,0),('high_half',H,H)]:
            region=MaskedRegionEvidence(B-2,width);region.acquire_mask(mask,value)
            seq=[]
            for _ in range(8):
                key=region.select_key(1,B-1)
                if key is None:break
                seq.append(key);region.bind(0,key)
            rows.append(dict(width=width,region=name,mask=mask,value=value,keys=seq,
                             key_costs=[round_key_cost(k,width) for k in seq]))
    return rows


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',default=str(Path(__file__).with_name('selector_results.json')))
    args=parser.parse_args()
    result={'status':'PASS','arithmetic':'exact Python integers','scope':'FINITE_CONTROL_AND_COMPILER_WORD_LENGTHS',
            'profiles':check_profiles(),'larger_carries':check_large_windows(),
            'prefix_adapters':check_prefix_adapters(),
            'updates':check_region_updates(),'word_weights':check_original_word_weights(),
            'fixed_target_DP':check_fixed_schedules(),'future_target_witness':future_target_witness(),
            'carry_witness':carry_witness(),
            'constructive_examples':examples(),'checks':dict(COUNTS)}
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({key:value for key,value in result.items() if key not in ('checks','constructive_examples')},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
