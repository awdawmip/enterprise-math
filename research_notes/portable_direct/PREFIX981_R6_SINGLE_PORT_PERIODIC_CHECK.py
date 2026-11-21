#!/usr/bin/env python3
"""PREFIX-981: exact singleton-port periodic source-word extinction and counts.

One source for each fixed residual, port and required input bit;
port 0 excluded, odd x; all calculations are integers.
"""
from collections import defaultdict, Counter
from itertools import product
import json


def source_dictionary(p):
    d = defaultdict(list)
    for i in range(p):
        for j in range(p):
            for s in (1, -1):
                d[(1 << i) - s * (1 << j)].append((i, j, s))
    return d


def singleton_types(p):
    d = source_dictionary(p)
    types = {}
    for residual, sources in d.items():
        ports = {j for i, j, s in sources if j > 0}
        if len(ports) == 1:
            j = next(iter(ports))
            eligible = {int(s == -1) for i, jj, s in sources if jj == j}
            assert len(eligible) == 1, (p, residual, eligible)
            types[residual] = (j, next(iter(eligible)))
    return types


def closed_form_survivors(p, word, types, steps):
    # Factorizes independent initial bits; free bits multiply by 2.
    conditions = defaultdict(set)
    occurrences = Counter()
    for t in range(steps):
        port, required_bit = types[word[t % len(word)]]
        initial_required = required_bit ^ (occurrences[port] & 1)
        conditions[port].add(initial_required)
        occurrences[port] += 1
    if any(len(v) > 1 for v in conditions.values()):
        return 0
    return 1 << (p - 1 - len(conditions))


def periodic_survivors(p, word, types):
    per_port = defaultdict(list)
    for residual in word:
        j, bit = types[residual]
        per_port[j].append(bit)
    for required in per_port.values():
        if len(required) % 2:
            return 0
        if any(bit != (required[0] ^ (i & 1)) for i, bit in enumerate(required)):
            return 0
    return 1 << (p - 1 - len(per_port))


def original_named_survivors(p, word, sources, steps):
    # Deliberately does NOT invoke the singleton mask/factorization code.
    total = 0
    for x0 in range(1, 1 << p, 2):
        x = x0
        for t in range(steps):
            residual = word[t % len(word)]
            valid = [(i, j, s) for i, j, s in sources[residual]
                     if j > 0 and ((x >> j) & 1) == int(s == -1)]
            if len(valid) != 1:
                assert len(valid) == 0, (p, word, x, valid)
                break
            x ^= 1 << valid[0][1]
        else:
            total += 1
    return total


def infinite_word_counts_triples(p, types):
    count = defaultdict(Counter)
    for j, bit in types.values():
        count[j][bit] += 1
    n = len(types)
    full_five_words = sum(2*c[0]*c[1]*(n - c[0] - c[1]) for c in count.values())
    full_five_initial_states = full_five_words * (1 << (p - 3))
    return {'singleton_residues':n,
            'ordered_singleton_triples':n**3,
            'persistent_triples':0,
            'five_step_surviving_triples':full_five_words,
            'five_step_named_paths_all_odd_inputs':full_five_initial_states,
            'port_required_bit_counts':{str(j):{'requires_0':c[0], 'requires_1':c[1]}
                                        for j,c in sorted(count.items())}}


def main():
    exhaustive = {}
    for p in (3, 4, 5, 6):
        sources = source_dictionary(p)
        types = singleton_types(p)
        num = 0
        five_words = 0
        five_mass = 0
        best_finite = 0
        for word in product(sorted(types), repeat=3):
            num += 1
            # Compare each possible first five steps against raw named-source transitions.
            for n in range(0, 6):
                factored = closed_form_survivors(p, word, types, n)
                raw = original_named_survivors(p, word, sources, n)
                assert factored == raw, (p,word,n,factored,raw)
                if raw:
                    best_finite = max(best_finite,n)
                if n == 5:
                    five_mass += raw
                    five_words += int(raw>0)
            assert closed_form_survivors(p,word,types,6) == 0
            assert periodic_survivors(p,word,types) == 0
        formula = infinite_word_counts_triples(p,types)
        assert formula['ordered_singleton_triples'] == num
        assert formula['five_step_surviving_triples'] == five_words
        assert formula['five_step_named_paths_all_odd_inputs'] == five_mass
        exhaustive[str(p)] = {'enumerated_triples':num,'raw_checks':num*6,
              'max_surviving_finite_steps':best_finite,'five_step_words':five_words,
              'five_step_named_paths_all_odd_inputs':five_mass}

    # A full four-phase check on the smallest sample, plus explicit persistent even cycle.
    p=4;src=source_dictionary(p);typ=singleton_types(p)
    four_count=0;infinite_four=0
    for word in product(sorted(typ), repeat=4):
        expected=periodic_survivors(p,word,typ)
        actual=original_named_survivors(p,word,src,8)
        assert expected==actual,(word,expected,actual)
        four_count+=1
        infinite_four+=int(expected>0)

    # Sharp five-step witness: three singleton residuals (-1,3,-4).
    p=19;src=source_dictionary(p);typ=singleton_types(p)
    sharp=(-1,3,-4);assert all(a in typ for a in sharp)
    for n in (5,6):
        assert closed_form_survivors(p,sharp,typ,n)==(1<<(p-3) if n==5 else 0)
    p19=infinite_word_counts_triples(19,typ)
    print(json.dumps({'schema':'PREFIX981_R6_EXACT_V1',
     'theorem':'single-port residue words have a 2L-step survival-to-infinity decision; odd L always extinct',
     'full_p_3_to_6_raw_checks':exhaustive,
     'four_phase_p4_exhaustive_words':four_count,
     'four_phase_p4_persistent_words':infinite_four,
     'p19_analytic_all_singleton_triples':p19,
     'sharp_p19_word':sharp,
     'sharp_five_step_all_odd_inputs':1<<(19-3),
     'sharp_six_step_all_odd_inputs':0,
     'original_named_transition_verified':True,
     'native_x6_embedding':'NOT_ESTABLISHED',
     'review':'NOT_REVIEWED'},ensure_ascii=False,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
