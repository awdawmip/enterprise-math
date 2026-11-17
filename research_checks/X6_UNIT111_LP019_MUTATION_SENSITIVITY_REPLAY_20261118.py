#!/usr/bin/env python3
"""Replay Unit111 LP019 true-native three-mode and mutation sensitivity, self-contained per repo.

Original Unit108 and frozen signed_brc.py are unchanged; all mutations live under
TemporaryDirectory. This is author verification, not R063/Helly or formal admission.
"""
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V2 = 'research_checks/X6_UNIT108_LP019_SIGNED_THICKNESS_ALWAYS_ON_NATIVE_V2_20261118.py'
V3 = 'research_checks/X6_UNIT111_LP019_FULL_ALWAYS_ON_NATIVE_V3_20261118.py'
NATIVE = 'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py'
BLOBS = {V2: 'c1842fbd34fb6fffa08a40a709b4838a6f2a5640',
         V3: '541c78d4cb639934939635274f96fce8e6ef0e4c',
         NATIVE: '300a96e3dc24bf6fff73743037a0347a8bc83176'}
MODES = ('normal', '-O', '-OO')
MUTATIONS = {
    'zero_word_formula': ('    return sum(', '    return 0 * sum('),
    'shift_hidden_histogram_count': (
        '    return 0 if residual < 0 or residual % 2 else residual // 2 + 1',
        '    return 0 if residual < 0 or residual % 2 else residual // 2 + 2')
}

def check(condition: bool, reason: str) -> None:
    if not condition:
        raise RuntimeError(reason)

def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def execute(path: Path, mode: str) -> dict:
    p = subprocess.run([sys.executable] + ([] if mode == 'normal' else [mode]) + [str(path)],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                       timeout=50, check=False)
    try:
        obj = json.loads(p.stdout)
    except json.JSONDecodeError:
        obj = None
    return {'exit': p.returncode,
            'status': obj.get('status') if isinstance(obj, dict) else None,
            'native_dp_comparisons': obj.get('native_six_axis_endpoint_comparisons')
                                     if isinstance(obj, dict) else None,
            'word_formula_comparisons': obj.get('signed_endpoint_formula_comparisons')
                                        if isinstance(obj, dict) else None,
            'stdout_sha256': hashlib.sha256(p.stdout.encode()).hexdigest(),
            'last_error': p.stderr.strip().splitlines()[-1] if p.stderr.strip() else ''}

def main() -> dict:
    source = {}
    for path, expected in BLOBS.items():
        data = (ROOT / path).read_bytes()
        check(blob(data) == expected, f'wrong exact native/checker blob {path}')
        source[path] = data
    with tempfile.TemporaryDirectory() as dirname:
        tmp = Path(dirname)
        paths = {}
        for path, data in source.items():
            dest = tmp / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            paths[path] = dest
        modes = {m: {'v2': execute(paths[V2], m), 'v3': execute(paths[V3], m)} for m in MODES}
        for mode in MODES:
            a, b = modes[mode]['v2'], modes[mode]['v3']
            check(a['exit'] == b['exit'] == 0 and a['native_dp_comparisons'] == b['native_dp_comparisons'] == 10364,
                  f'original real-native comparison failed {mode}')
            check(a['word_formula_comparisons'] == b['word_formula_comparisons'] == 2925,
                  f'two-axis count comparison changed {mode}')
            check(a['stdout_sha256'] == b['stdout_sha256'], f'unmutated JSON changed {mode}')
        check(len({modes[m]['v3']['stdout_sha256'] for m in MODES}) == 1, 'optimized output changed')
        original = {'v2': paths[V2].read_text(), 'v3': paths[V3].read_text()}
        faults = {}
        for name, (old, new) in MUTATIONS.items():
            faults[name] = {}
            for key, path in (('v2', paths[V2]), ('v3', paths[V3])):
                check(original[key].count(old) == 1, f'fault point not unique {name}/{key}')
                path.write_text(original[key].replace(old, new, 1))
            for mode in MODES:
                observed = {'v2': execute(paths[V2], mode), 'v3': execute(paths[V3], mode)}
                faults[name][mode] = observed
                check(observed['v3']['exit'] != 0, f'V3 silent false PASS: {name}/{mode}')
                check((observed['v2']['exit'] == 0) == (mode != 'normal'),
                      f'V2 expected failure distinction not found: {name}/{mode}')
                if mode != 'normal':
                    check(observed['v2']['status'] == 'PASS' and observed['v2']['native_dp_comparisons'] == 10364,
                          f'V2 mutated real-native counter changed: {name}/{mode}')
            for key, path in (('v2', paths[V2]), ('v3', paths[V3])):
                path.write_text(original[key])
    return {'schema': 'X6_UNIT111_MUTATION_REPLAY_V1', 'status': 'PASS',
            'source_blobs': BLOBS, 'baseline': modes, 'mutations': faults,
            'scope': 'original frozen signed BRC used; R063/Helly not executed; author only'}

if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True))
