#!/usr/bin/env python3
"""R284EJ exact finite two-bit source tag and RW-invariant ceiling.
Execute beside frozen R284CO_spectral_witness_checker.py (immutable GitHub pin).
Integer-only, no external dependencies.
"""
import json
from collections import Counter
from pathlib import Path
from R284CO_spectral_witness_checker import P, FROZEN_SHA, arcs, words, dist

N = 1 << 16
Q = 65

def tag(i):
    return ((i >> 12) & 1, (i >> 14) & 1)

def read(f, i):
    return (f[i], f[i ^ Q])

def label_distance(f):
    order = sorted(range(N), key=lambda i: (f[i], i))
    best = P
    witnesses = []
    comparisons = 0
    for rank, i in enumerate(order):
        pos = rank - 1
        while pos >= 0 and f[i] - f[order[pos]] <= best:
            j = order[pos]
            if tag(i) == tag(j):
                comparisons += 1
                d = max(abs(f[i] - f[j]), abs(f[i ^ Q] - f[j ^ Q]))
                pair = (min(i,j), max(i,j))
                if d < best:
                    best, witnesses = d, [pair]
                elif d == best:
                    witnesses.append(pair)
            pos -= 1
    return best, sorted(witnesses), comparisons

def code(f, i, width, phase):
    return tuple((x - phase) // width for x in read(f, i))

def same_fiber(f, group, width, phase):
    return [code(f, i, width, phase) for i in group]

def direct_collision_count(f, width, phase, with_tag=True):
    seen = {}
    collision_count = 0
    first = None
    for i in range(N):
        key = (tag(i), code(f, i, width, phase)) if with_tag else code(f, i, width, phase)
        if key in seen:
            collision_count += 1
            if first is None: first = [seen[key], i]
        else:
            seen[key] = i
    return collision_count, first

def main():
    xs = words()  # checks all 65,536 original residues and frozen SHA-256
    aa = arcs()
    assert len(aa) == 64
    f = [max(dist(x, arc) for arc in aa) for x in xs]
    best, winners, comparisons = label_distance(f)
    assert best == 17313 and winners == [(36912, 36977)], (best, winners)
    assert all(tag(i) == tag(i ^ q) for i in range(N) for q in (1, 64, 65))
    delta = min(abs(f[i] - f[i ^ Q]) for i in range(N) if i < (i ^ Q))
    forced = [(i, i ^ Q) for i in range(N) if i < (i ^ Q) and abs(f[i] - f[i ^ Q]) == delta]
    assert delta == 17313 and forced == [(36912, 36977)]

    # A triple collision proves no arbitrary one-bit side label can cover width 9395 at phase 58.
    triple = (17336, 37542, 33446)
    assert len(set(same_fiber(f, triple, 9395, 58))) == 1
    assert len({tag(i)[0] for i in triple}) == 2

    # Forced RW-pair collision obstructs every RW-invariant tag, regardless of tag alphabet size.
    pair = (36912, 36977)
    assert len(set(same_fiber(f, pair, 17314, 10733))) == 1
    assert tag(pair[0]) == tag(pair[1])

    direct_checks = []
    for s,t,expected in ((60,0,0),(9394,58,0),(9395,58,0),
                         (17313,10733,0),(17314,10733,1)):
        count, first = direct_collision_count(f,s,t)
        assert (count == 0) if expected == 0 else (count >= 1)
        direct_checks.append({'width':s,'phase':t,'collisions':count,'example':first})

    data = {
       'schema': 'R284EJ_TWO_BIT_RW_INVARIANT_OBSERVER_V1',
       'frozen_commit': 'acba2d8667903434aaa2a10720f43637fcc2421b',
       'frozen_path': 'research_notes/portable_direct/R284CO_spectral_witness_checker.py',
       'frozen_blob_sha1': 'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
       'frozen_residue_sha256': FROZEN_SHA,
       'state_count': N, 'arc_count': len(aa),
       'tag': ['(i >> 12) & 1', '(i >> 14) & 1'],
       'read_offsets': [0, 65],
       'same_tag_minimum_Linf': best,
       'same_tag_minimizer_pairs': [list(p) for p in winners],
       'same_tag_pruned_pair_comparisons': comparisons,
       'RW_forced_pair_minimum': delta,
       'RW_forced_pair_minimizers': [list(p) for p in forced],
       'all_phase_width_prefix': 17313,
       'first_two_bit_failure': {'width':17314,'phase':10733,'pair':list(pair),
                                 'common_code':list(code(f,pair[0],17314,10733))},
       'arbitrary_one_bit_no_go': {'width':9395,'phase':58,'triple':list(triple),
                                  'common_code':list(code(f,triple[0],9395,58))},
       'two_port_integer_error_radius': 8656,
       'direct_checks': direct_checks,
       'status': 'AUTHOR_EXACT_CHECKED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED'
    }
    dest=Path(__file__).with_name('R284EJ_two_bit_invariant_ceiling_certificate.json')
    dest.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(data, ensure_ascii=False))

if __name__ == '__main__':
    main()
