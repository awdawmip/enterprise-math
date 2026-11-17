#!/usr/bin/env python3
"""LP011 Unit110: immutable-source, three-mode mutation-sensitivity replay.

Run in the enterprise-math repo; original Unit108 and frozen native sources are
read-only. This is an opt-in author check, not R063 or independent admission.
"""
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V2 = 'research_checks/X6_UNIT108_LP011_TYPED_DOMINANT_CONSUMER_ALWAYS_ON_NATIVE_V2_20261118.py'
V3 = 'research_checks/X6_UNIT110_LP011_FULL_ALWAYS_ON_NATIVE_V3_20261118.py'
NATIVE = 'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py'
EXPECTED = {V2: '296e4cdb8b5710a6b2017f24e4b6059a2554714e',
            V3: '8d45dc1c88fd8dc897b6abe6d538de3185a135cd',
            NATIVE: '300a96e3dc24bf6fff73743037a0347a8bc83176'}
MODES = ('normal', '-O', '-OO')

def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def run(script: Path, mode: str) -> dict:
    cmd = [sys.executable] + ([] if mode == 'normal' else [mode]) + [str(script)]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=35, check=False)
    try:
        output = json.loads(p.stdout)
    except json.JSONDecodeError:
        output = None
    return {'exit': p.returncode,
            'status': output.get('status') if isinstance(output, dict) else None,
            'native_calls': output.get('existing_native_brc_calls') if isinstance(output, dict) else None,
            'stdout_sha256': hashlib.sha256(p.stdout.encode()).hexdigest(),
            'error': p.stderr.strip().splitlines()[-1] if p.stderr.strip() else ''}

def check(value: bool, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def main() -> dict:
    originals = {}
    for path, expected in EXPECTED.items():
        raw = (ROOT / path).read_bytes()
        actual = blob(raw)
        check(actual == expected, f'wrong pinned Git blob: {path} {actual}')
        originals[path] = raw

    with tempfile.TemporaryDirectory() as dirname:
        base = Path(dirname)
        native = base / NATIVE
        native.parent.mkdir(parents=True)
        native.write_bytes(originals[NATIVE])
        scripts = {}
        for tag, filename in (('v2', V2), ('v3', V3)):
            dest = base / filename
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(originals[filename])
            scripts[tag] = dest
        reference = {m: {name: run(path, m) for name, path in scripts.items()} for m in MODES}
        for m, records in reference.items():
            check(all(r['exit'] == 0 and r['native_calls'] == 3375 for r in records.values()),
                  f'original native integration failed: {m}')
            check(records['v2']['stdout_sha256'] == records['v3']['stdout_sha256'],
                  f'v2/v3 output changed: {m}')
        check(len({reference[m]['v3']['stdout_sha256'] for m in MODES}) == 1,
              'strict consumer output differs across optimization modes')
        original_text = {k: scripts[k].read_text() for k in scripts}
        mutation_specs = {
            'erased_embedded_axes': ('        out[k] = x', '        out[k] = 0'),
            'erased_negative_observer': ('        return frozenset(negative)',
                                         '        return frozenset()'),
        }
        mutants = {}
        for kind, (before, after) in mutation_specs.items():
            mutants[kind] = {}
            for tag, script in scripts.items():
                text = original_text[tag]
                check(text.count(before) == 1, f'mutation location missing {kind} {tag}')
                script.write_text(text.replace(before, after, 1))
            for mode in MODES:
                outcomes = {tag: run(script, mode) for tag, script in scripts.items()}
                mutants[kind][mode] = outcomes
                check(outcomes['v3']['exit'] != 0, f'V3 silent acceptance {kind}/{mode}')
                check((outcomes['v2']['exit'] == 0) == (mode != 'normal'),
                      f'V2 failure signature changed {kind}/{mode}')
            for tag, script in scripts.items():
                script.write_text(original_text[tag])
        missing, tampered = {}, {}
        native.unlink()
        for mode in MODES:
            missing[mode] = run(scripts['v3'], mode)
            check(missing[mode]['exit'] != 0, f'missing native accepted {mode}')
        native.write_bytes(originals[NATIVE] + b'\n# tampered pin\n')
        for mode in MODES:
            tampered[mode] = run(scripts['v3'], mode)
            check(tampered[mode]['exit'] != 0, f'tampered native accepted {mode}')
    return {'schema': 'X6_UNIT110_MUTATION_REPLAY_V1', 'status': 'PASS',
            'pinned_github_blobs': EXPECTED, 'modes': MODES,
            'reference': reference, 'mutations': mutants,
            'negative_input_controls': {'missing_source': missing, 'wrong_blob': tampered},
            'scope': 'author integration only; original R063/Helly not executed'}

if __name__ == '__main__':
    print(json.dumps(main(), ensure_ascii=False, sort_keys=True))
