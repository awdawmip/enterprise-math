"""Actual v3 source-bound runner; it is not the earlier v1 inline runner."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import subprocess
import sys
import time


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_new(path, data):
    with path.open('xb') as stream:
        stream.write(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    root, output = args.root.resolve(), args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    rel = 'research_artifacts/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909'
    names = ('check_exact_map.py', 'test_exact_map.py', 'exact_map_proof.md')
    inputs = {name: root.joinpath(rel, name).read_bytes() for name in names}
    for name, raw in inputs.items():
        write_new(output.joinpath(name + '.frozen'), raw)
    commands = [
        ('certificate', [sys.executable, '-B', '-X', 'utf8', str(root.joinpath(rel, names[0])),
                         '--root', str(root), '--output', str(output.joinpath('certificate.json')), '--write']),
        ('focused-tests', [sys.executable, '-B', '-X', 'utf8', '-m', 'unittest',
                           'research_artifacts.RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909.test_exact_map', '-v']),
        ('selected-static', [sys.executable, '-B', '-X', 'utf8', 'tools/check_exact_arithmetic_policy.py',
                             rel + '/' + names[0], rel + '/' + names[1]]),
    ]
    receipts = []
    for label, argv in commands:
        start = datetime.now(timezone.utc).isoformat()
        tick = time.monotonic_ns()
        try:
            process = subprocess.run(argv, cwd=root, capture_output=True, timeout=600)
            stdout, stderr, code, timeout = process.stdout, process.stderr, process.returncode, False
        except subprocess.TimeoutExpired as exc:
            stdout, stderr, code, timeout = exc.stdout or b'', exc.stderr or b'', None, True
        write_new(output.joinpath(label + '.stdout'), stdout)
        write_new(output.joinpath(label + '.stderr'), stderr)
        receipt = {'label': label, 'argv': argv, 'cwd': str(root), 'started_at': start,
                   'finished_at': datetime.now(timezone.utc).isoformat(),
                   'elapsed_nanoseconds': time.monotonic_ns() - tick, 'outer_timeout_seconds': 600,
                   'exit_code': code, 'timed_out': timeout,
                   'stdout_sha256': sha(stdout), 'stderr_sha256': sha(stderr)}
        receipts.append(receipt)
        print(json.dumps(receipt, ensure_ascii=False), flush=True)
        print(stdout.decode('utf-8', errors='replace'), flush=True)
        print(stderr.decode('utf-8', errors='replace'), flush=True)
        if code != 0 or timeout:
            break
    preserved = all(root.joinpath(rel, name).read_bytes() == raw for name, raw in inputs.items())
    result = {'schema': 'RB_CM24_ACTUAL_V3_RUNNER_RECEIPT_V1',
              'source_pins': {name: {'sha256': sha(raw), 'bytes': len(raw)} for name, raw in inputs.items()},
              'runner_sha256': sha(Path(__file__).read_bytes()),
              'commands': receipts, 'selected_sources_unchanged': preserved,
              'complete': len(receipts) == len(commands),
              'all_pass': preserved and len(receipts) == len(commands) and all(r['exit_code'] == 0 for r in receipts),
              'memory_boundary': 'Each mathematics child applies its existing Windows Job 4096 MiB cap; this runner records no measured peak.',
              'earlier_evidence': 'This new stored runner was not the runner for v1 or the initial v3 explorations. Their original inline execution provenance remains separate.'}
    certificate = output.joinpath('certificate.json')
    if certificate.is_file():
        result['certificate_sha256'] = sha(certificate.read_bytes())
        result['certificate_bytes'] = len(certificate.read_bytes())
    encoded = (json.dumps(result, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    write_new(output.joinpath('receipt.json'), encoded)
    print(json.dumps({'receipt_sha256': sha(encoded), 'all_pass': result['all_pass']}, ensure_ascii=False))
    return 0 if result['all_pass'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
