"""Future observation of the public Euler controller. Supply a public source checkout."""
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha1
from itertools import product
import json
from pathlib import Path
import sys

PINS = {
    'research_tasks/RS-EULER-RR-20261012-07.md': 'c3a45d6c6033f48136f532678db89cfe6c79428d',
    'research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md': '03cfdf23f8f1a6208b4ac4eb862a1b7ad3811d8b',
    'research_notes/chatgpt_direct/20261010_EULER_PASSIVE_SAMPLING_AND_NOISE.md': 'bd80290c259cc60995069613a5f4b5f5b41a13d1',
    'research_notes/chatgpt_direct/20261011_EULER_READOUT_BACKACTION.md': '5e00414f752d97d69cee9bf602fd6b5e50da4b05',
    'research_notes/chatgpt_direct/20261010_EULER_CONTROLLER_RELATIONAL_MEMORY.md': '22a7d072e54f40c52a94e91dac7f68f63371436c',
    'src/enterprise_math/partial_operation_quotient.py': 'd1f86491ce07279c058a4c99f40cabb1f96da0de',
    'src/enterprise_math/operation_quotient.py': '758a65de02a434446936cd7e37b2ae604eade863',
    'src/enterprise_math/brc_weighted.py': '3f205696709e847909958a153f8fe10d3f6b70f0',
    'src/enterprise_math/brc_logarithm.py': '4732e5fc381ce613d240c4381ccbef03c27a69c7',
    'src/enterprise_math/exact_arithmetic.py': '35ea95b0916494b83a92386e3e313928362dd79e',
}


def fused(z, action):
    j, s, f, w, theta, a, r = z
    if action in ('T', 'G'):
        target, mask, bit, incident = ((3, 3, 1, (1, 3)) if action == 'T'
                                      else (1, 6, 2, (1, 2)))
        if theta == 0 and w in (0, target):
            w = target - w
            f ^= mask
        s ^= (f >> bit) & 1
        theta ^= int(w in incident)
        j = (j + (-1)**s) % 3
        f ^= 7
    elif action == 'F':
        s ^= int(a == r)
    elif action == 'E':
        r = (r + j - a) % 3
    else:
        raise ValueError(action)
    return (j, s, f, w, theta, a, r)


def primitive(z, name, receiver_sheet):
    j, s, f, w, th, a, r = z
    if name in ('H01', 'H03'):
        dest = int(name[-1])
        if not th and w in (0, dest):
            w, f = dest - w, f ^ {1: 6, 3: 3}[dest]
    elif name in ('U1', 'U2'):
        face = int(name[-1])
        s ^= (f >> (3-face)) & 1
        f ^= 7
        th ^= int(w in ((1, 2) if face == 1 else (1, 3)))
    elif name == 'C':
        j = (j + (1 if s == 0 else -1)) % 3
    elif name == 'R':
        r = (r + (1 if receiver_sheet == 0 else -1)) % 3
    elif name != 'hold':
        raise ValueError(name)
    return (j, s, f, w, th, a, r)


def instructions(z, action, sheet):
    if action == 'T':
        return ('H03', 'U2', 'C')
    if action == 'G':
        return ('H01', 'U1', 'C')
    if action == 'F':
        return ('U1', 'U1') if z[5] == z[6] else ('hold',)
    count = ((1 if sheet == 0 else -1) * (z[0]-z[5])) % 3
    return ('R',) * count if count else ('hold',)


def read(z):
    return z[0], (z[-1] - z[0]) % 3


def sector(z):
    f, w = z[2], z[3]
    f1, f2, f3 = f >> 2, (f >> 1) & 1, f & 1
    return (2*(f1 ^ f2) + (f1 ^ f3)) ^ w


def passive(x):
    z = x + (0, 0)
    tr = []
    for _ in range(12):
        tr.append(z[0])
        z = fused(z, 'T')
    assert z == x + (0, 0)
    return tuple(tr)


def transcript(z, word):
    out = [read(z)]
    for letter in word:
        z = fused(z, letter)
        out.append(read(z))
    return tuple(out)


def hist(values):
    return dict(sorted(Counter(Counter(values).values()).items()))


def extended_protocol(tag, states, terminal):
    """Single input, no reset. Exhaust the remaining two-letter words on one necessary cell."""
    reps = {label:z for z,label in terminal.items()}
    initial = {}
    for i,z in reps.items():
        initial.setdefault(read(z), []).append(i)
    mixed = tag == 'mixed'
    out = set()
    for z in states:
        trace = [read(z)]
        z = fused(z,'E')
        trace.append(read(z))
        signs = []
        for j in range(6 if mixed else 5):
            if mixed:
                if j < 3:
                    action = 'T'
                elif j < 5:
                    action = 'T' if signs[0] == signs[2] else 'G'
                else:
                    action = 'T' if signs[0] != signs[2] and signs[0] == signs[4] else 'G'
            elif j < 3:
                action = 'TGT'[j]
            else:
                high = tag >> 1
                t_fourth = (signs[0] == signs[2]) ^ high
                if j == 3:
                    action = 'T' if t_fourth else 'G'
                else:
                    use_g = not t_fourth and ((signs[1] != signs[3]) ^ high)
                    action = 'G' if use_g else 'T'
            after = fused(z,action)
            signs.append((after[0]-z[0]) % 3)
            z = after
            trace.append(read(z))
        out.add(tuple(trace))
    assert len(out) == len(reps)
    depth = 8 if mixed else 7
    diagnostic_inputs = [z for z in states if z[0] == z[-1] == z[-2] == 0]
    short_hist = Counter()
    for word in product('TG', repeat=depth-2):
        n = len({transcript(z,word) for z in diagnostic_inputs})
        short_hist[n] += 1
    expected = {16:4,32:22,40:38} if mixed else {12:2,16:4,20:24,24:2}
    assert short_hist == expected
    witness = 'TTTTGGGE' if mixed else 'TTTTGGE'
    assert len({transcript(z, witness) for z in states}) == len(reps)
    assert len(set(map(len,initial.values()))) == 1
    return dict(classes_per_initial_read=len(initial[(0,0)]),
                shorter_source_word_histogram=dict(sorted(short_hist.items())), adaptive_minimum=depth-1,
                distinct_adaptive_transcripts=len(out), fixed_minimum=depth,
                fixed_word=witness, shorter_fixed_word_exists=False)


def main(repo):
    for name, pin in PINS.items():
        b = (repo / name).read_bytes()
        assert sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest() == pin, name
    sys.path.insert(0, str(repo/'src'))
    from enterprise_math import brc_weighted as brc
    from enterprise_math.partial_operation_quotient import (
        partial_family_future_partition_sequence, partitions_equivalent)
    old = list(product(range(3), range(2), range(8), range(4), range(2)))
    states = [x+(a,r) for x in old for a,r in product(range(3), repeat=2)]
    tau = {x: passive(x) for x in old}
    checks = 0
    for z, act, sheet in product(states, 'TFEG', range(2)):
        y = z
        for name in instructions(z, act, sheet):
            y = primitive(y, name, sheet)
        assert y == fused(z, act) and sector(y) == sector(z)
        checks += 1

    result = {}
    class_key = {}
    for tag in ('mixed', 0, 1, 2, 3):
        d = [z for z in states if tag == 'mixed' or sector(z) == tag]
        ops = {k: {z: fused(z, k) for z in d} for k in 'TFEG'}
        obs = {z: read(z) for z in d}
        tables = {}
        for lang in ('T', 'TF', 'TFE', 'TFEG'):
            stages = partial_family_future_partition_sequence(d, {k:ops[k] for k in lang}, obs)
            terminal = stages[-1]
            if lang != 'TFEG':
                keys = {z: (tau[z[:5]],z[-1]) +
                        (() if lang == 'T' else (int(z[-1] == z[-2]),)
                         if lang == 'TF' else (z[-2],)) for z in d}
                assert partitions_equivalent(d, keys, terminal)
            if lang == 'TFE':
                assert partitions_equivalent(d, {z: transcript(z, 'TTTTE') for z in d}, terminal)
                if tag == 'mixed':
                    class_key = terminal
            tables[lang] = dict(stages=[len(set(v.values())) for v in stages],
                                final_fibers=hist(terminal.values()))
        tables['extension_experiment'] = extended_protocol(tag,d,terminal)
        result[str(tag)] = tables

    representatives = {i:z for z,i in class_key.items()}.values()
    best = []
    for n in range(5):
        size, words = 0, []
        for w in product('TFE', repeat=n):
            k = len({transcript(z, w) for z in representatives})
            if k > size:
                size, words = k, []
            if k == size:
                words.append(''.join(w))
        best.append(dict(max_transcripts=size, first_winning_word=words[0],
                         count_of_maximizers=len(words)))
    same = {}
    pair = None
    for x in old:
        if sector(x) == 0:
            key = tau[x][:4]
            if key in same and tau[same[key]][4] != tau[x][4]:
                pair = (same[key], x)
                break
            same[key] = x
    assert pair
    assert len({transcript(z, 'TTTT') for z in states if z[-1] == z[-2]}) == 144

    x = (0, 0, 0, 1, 0)
    cwm = {}
    histograms = []
    for same_preparation in (True, False):
        buckets = {j:brc.CWM_ZERO for j in range(3)}
        for a in range(2):
            z = x + (a, a if same_preparation else 1-a)
            weight = brc.cwm_edge(Fraction(1,2))
            for act in 'FT':
                for name in instructions(z, act, 0):
                    z = primitive(z, name, 0)
                    weight = brc.cwm_propagate(weight, brc.CWM_ONE)
            buckets[z[0]] = brc.cwm_recoalesce(buckets[z[0]], weight)
        cwm[str(same_preparation)] = [[v.count,str(v.total),str(v.dominant)] for v in buckets.values()]
        histograms.append(tuple(v.total for v in buckets.values()))
    assert histograms == [(0,0,1),(0,1,0)]
    ready_laws = []
    for flip in (0,1):
        mass = [brc.CWM_ZERO for j in range(3)]
        for s in range(2):
            a = s ^ flip
            z = (0,s,0,1,0,a,a)
            path = brc.cwm_edge(Fraction(1,2))
            for act in 'EFT':
                for name in instructions(z, act, 1):
                    z = primitive(z, name, 1)
                    path = brc.cwm_propagate(path, brc.CWM_ONE)
            mass[z[0]] = brc.cwm_recoalesce(mass[z[0]], path)
        ready_laws.append([str(v.total) for v in mass])
    assert ready_laws == [['0','0','1'],['0','1','0']]
    for target in states:
        x, a, r = target[:5], target[5], target[6]
        z = x + (a, a)
        k = int(x[0] == a)
        y = fused(z, 'T') if k else z
        count = (r-a) * pow((y[0]-a)%3, -1, 3) % 3
        for step in 'T'*k + 'E'*count + 'T'*((-k)%12):
            z = fused(z, step)
        assert z == target
    extended_pair = [(2,0,0,1,th,0,0) for th in (0,1)]
    assert tau[extended_pair[0][:5]] == tau[extended_pair[1][:5]]
    extra = [fused(z, 'G')[0] for z in extended_pair]
    assert extra == [1,0]

    return dict(registration='RS-EULER-RR-20261012-07', git_blobs=PINS,
                compressed_old_atoms=len(old), joint_atoms=len(states),
                primitive_fused_comparisons_including_both_receiver_sheets=checks,
                passive_prefix_counts=[len({t[:i] for t in tau.values()}) for i in range(1,6)],
                partitions=result, best_single_words_through_four=best,
                adaptive_lower_bound_same_sector_sources=pair,
                adaptive_lower_bound_five_readings=[tau[x][:5] for x in pair],
                universal_single_word='TTTTE', ready_initial_transcripts=144,
                reachable_from_ready=len(states), ready_two_world_EFT_laws=ready_laws,
                source_diagnostic_G_outputs=extra, cwm_FT_count_total_dominant=cwm)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path.cwd())
    print(json.dumps(main(parser.parse_args().repo), sort_keys=True, indent=2))
