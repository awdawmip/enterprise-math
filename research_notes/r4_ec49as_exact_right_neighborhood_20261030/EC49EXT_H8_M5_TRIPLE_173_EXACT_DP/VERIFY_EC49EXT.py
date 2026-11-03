#!/usr/bin/env python3
"""EC49EXT H8/M5/S<=6: reproduce exact primitive-prefix E<80 certificates.
Reads frozen same-PR EC49EXS triple candidate catalogue and EC49EXJ
native signed-X6 candidate generation/OR-mask DP. Stdlib Python 3 + C++17.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
EXJ = ROOT / 'EC49EXJ_H8_M4_S6_GLOBAL_EXACT'
EXS = ROOT / 'EC49EXS_H8_M5_OBSERVER_SIGNED_MATCH'
sys.path.insert(0, str(EXJ))
from SCREEN_H5_EC49EXJ import build_input, words


def catalog():
    lines = (EXS / 'EC49EXS_TRIPLE_CANDIDATES.tsv').read_text().splitlines()
    assert len(lines) == 947
    cases = []
    for idx, row in enumerate(lines[1:]):
        q = list(map(int, row.split()))
        assert len(q) == 20
        lb, old_lb, a, b, c = q[:5]
        keys = [tuple(q[5 + 3 * j:8 + 3 * j]) for j in range(5)]
        tri = (a, b, c)
        rem = [h for h in range(2, 9) if h not in tri]
        mapping = {h: keys[0] for h in tri}
        mapping.update({h: k for h, k in zip(rem, keys[1:])})
        schedule = tuple((mapping[h], 4 if mapping[h][0] + mapping[h][1] - h - 1 >= 1 else 2) for h in range(2, 9))
        counts = [len(words(h, k, t)) for h, (k, t) in enumerate(schedule, 2)]
        assert all(counts) and len(set(keys)) == 5
        cases.append(dict(index=idx, lb=lb, prior_lb=old_lb, triple=tri,
                          keys=keys, schedule=schedule, words=sum(counts), counts=counts))
    cases.sort(key=lambda a: (a['words'], max(a['counts']), a['index']))
    assert len(cases) == 946
    assert sum(a['words'] <= 400 for a in cases) == 92
    assert sum(a['words'] <= 575 for a in cases) == 265
    assert all(400 < a['words'] <= 575 for a in cases[92:265])
    return cases


def run():
    cases = catalog()
    exe = HERE / 'exact_dp'
    subprocess.run(['g++', '-O3', '-std=c++17', str(EXJ / 'EXACT_OR_MASK_DP.cpp'), '-o', str(exe)], check=True)
    outputs = []
    for case in cases[92:265]:
        stdin, nodes, nwords = build_input(case['schedule'])
        assert nwords == case['words']
        p = subprocess.run([str(exe), '80'], input=stdin, capture_output=True, text=True, check=True)
        regex = r'BOUND_PASS minimum_total_at_least=80 nodes=(\d+) colors=(\d+)'
        match = re.fullmatch(regex, p.stdout.strip())
        assert match is not None and int(match[1]) == nodes, (case['index'], p.stdout)
        outputs.append(dict(index=case['index'], words=nwords, nodes=nodes,
                            colors=int(match[2]), input_sha256=hashlib.sha256(stdin.encode()).hexdigest(),
                            stdout=p.stdout.strip()))
    assert len({row['index'] for row in outputs}) == 173
    return dict(status='PASS', threshold=80, number_of_cases=173, previous_92=92,
                subset='triple key-collision EXS survivors with 400 < eligible native words <= 575',
                results=outputs)


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, separators=(',', ':')))
