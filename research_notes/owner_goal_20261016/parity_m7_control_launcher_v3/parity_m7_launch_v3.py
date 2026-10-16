#!/usr/bin/env python3
"""CONTROL launcher candidate. No authority is conferred by this file.

Only the real Researcher consumes fresh authenticated Native/Source evidence.
This program additionally reruns the genuine canonical guard and binds that
answer to the entire original Native receipt. Never use synthetic evidence in
an actual run. Imports of the frozen science occur only inside the child job.
"""
import argparse
import ctypes
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import selectors
import signal
import subprocess
import sys
import time

TASK = 'RS-PARITY-M7-ORIGINAL-TRACE-COMPACT-7-8-EXACT-CERTIFICATE'
CAP = 8 * 1024 * 1024
RESERVE = 65536
MEMORY = 512 * 1024 * 1024
SECONDS = 300
SCIENCE_ATTEMPTED = False  # conservative: set before the only Popen attempt
PREP_END = dt.datetime(2026, 10, 16, 6, 53, 4, tzinfo=dt.timezone.utc)
FROZEN_SHA = '5ae056c2d670101cf64696b12364ce36c2efacbd96185269ada20d2c780ce41c'
PINS = {
 'resource_budget.py': (6123, '686fc6c25d07228e6aba0c92fdc9ef8f9992e0f6b71c8336c7465a430beead38'),
 'producer.py': (7035, 'db583e33fb1ded767f48a65fd5f654924c4cf9aea20d34497e2c73408310f439'),
 'checker.py': (10486, '8b65698f6ff2680e6ea1533afdb87d459b01b5097674cbc5b15f09df50d7e239'),
 'workload.py': (6239, '9ee260566efd348f329c62ead443ae57b6656b715773890e99c142b07e7d9388'),
 'FIXED_INPUT.json': (6803, 'eb589651c48be9d83d399871de2e52929a016bad22524b479ae2665bbce8808f'),
 'OUTPUT_SCHEMA.json': (6082, '50b7f657e4583df856252dc4d6fb85e78e6d27f0730e87212d6f50953deb13fc'),
 'EXECUTION_CONTRACT.json': (5007, '0f9fc6b15e508efd70b1fa86e393a0fa3e7848ffaddccef5dfc4d6a700e07cff'),
 'README.md': (9998, 'e2382111c632f148ce944d8b04795604def643313a5d55b32f1cd81813fa08c7'),
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=True, allow_nan=False,
                       separators=(',', ':')) + '\n').encode('ascii')


def read_bound(path, cap):
    with Path(path).open('rb') as f:
        data = f.read(cap + 1)
    if len(data) > cap:
        raise ValueError('input exceeds bound: ' + str(path))
    return data


def load_json(data):
    def pairs(items):
        result = {}
        for k, v in items:
            if k in result:
                raise ValueError('duplicate JSON key')
            result[k] = v
        return result
    return json.loads(data, object_pairs_hook=pairs)


def exclusive(path, data):
    with Path(path).open('xb') as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())


def sync_directory(path):
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def deny_network_and_limit():
    # Linux x86_64 only, fail closed on every other platform. Applied BEFORE
    # interpreter startup; OS syscall filter, not a Python socket monkeypatch.
    if sys.platform != 'linux' or platform.machine() != 'x86_64':
        raise RuntimeError('unsupported OS for frozen network filter')
    resource.setrlimit(resource.RLIMIT_AS, (MEMORY, MEMORY))
    resource.setrlimit(resource.RLIMIT_CPU, (SECONDS, SECONDS))
    resource.setrlimit(resource.RLIMIT_FSIZE, (CAP, CAP))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    class Filter(ctypes.Structure):
        _fields_ = [('code', ctypes.c_ushort), ('jt', ctypes.c_ubyte),
                    ('jf', ctypes.c_ubyte), ('k', ctypes.c_uint)]
    class Program(ctypes.Structure):
        _fields_ = [('len', ctypes.c_ushort), ('filter', ctypes.POINTER(Filter))]
    # Check audit arch first, then deny x32 and network creation/use syscalls.
    instructions = [(0x20, 0, 0, 4), (0x15, 1, 0, 0xc000003e),
                    (0x06, 0, 0, 0x80000000), (0x20, 0, 0, 0),
                    (0x45, 0, 1, 0x40000000), (0x06, 0, 0, 0x80000000)]
    for nr in (41, 42, 43, 44, 45, 46, 47, 49, 50, 53, 288, 299, 307):
        instructions += [(0x15, 0, 1, nr), (0x06, 0, 0, 0x00050001)]
    instructions.append((0x06, 0, 0, 0x7fff0000))
    array = (Filter * len(instructions))(*(Filter(*i) for i in instructions))
    program = Program(len(instructions), array)
    libc = ctypes.CDLL(None, use_errno=True)
    if libc.prctl(38, 1, 0, 0, 0) != 0 or libc.prctl(22, 2, ctypes.byref(program), 0, 0) != 0:
        raise OSError(ctypes.get_errno(), 'cannot install seccomp filter')


def validate_evidence(spec, canonical_root):
    """File consistency plus genuine guard; not authentication of local files.

    The real actor must first verify original receipts through the authorized
    connector, full current Source and latest run generation, then create this
    metadata binding. No allow_run/admitted field is accepted as authority.
    """
    raw = {}
    for key in ('native_receipt', 'events', 'run_state', 'execution_intent',
                'canonical_source_gate', 'static_review_gate', 'prep_ledger'):
        item = spec[key]
        data = read_bound(item['path'], 16 * 1024 * 1024)
        if sha(data) != item['sha256']:
            raise ValueError('changed bound evidence: ' + key)
        raw[key] = data
    receipt = load_json(raw['native_receipt'])
    run = receipt
    for component in spec['native_run_pointer']:
        run = run[component]
    if run['task_id'] != TASK or run.get('fenced_by_claim_id') is not None:
        raise ValueError('wrong or fenced Native run')
    if run.get('canonical_result_published') is not False:
        raise ValueError('Native run already has a result')
    state = load_json(raw['run_state'])
    if state != run['state']:
        raise ValueError('run.state differs from original Native receipt')
    for key in ('run_id', 'generation', 'revision', 'task_id', 'claim_id',
                'publication_id', 'researcher_id', 'session_id'):
        if run[key] != spec['expected_run'][key]:
            raise ValueError('wrong current Native binding: ' + key)
    if type(run['generation']) is not int or run['generation'] < 1:
        raise ValueError('invalid generation')
    authority = run['authorization']
    native = authority['result']
    if authority['authority'] != 'EXISTING_CANONICAL_SOURCE_PROGRAM' or native['authorized'] is not True:
        raise ValueError('no genuine Native authorization')
    if sha(raw['events']) != spec['events']['sha256']:
        raise ValueError('events mismatch')
    # The observation must be truly refreshed from Native/Source by the actor;
    # a user-edited timestamp is not a freshness/authentication credential.
    observed = dt.datetime.fromisoformat(spec['actual_fresh_observation_utc'])
    age = (dt.datetime.now(dt.timezone.utc) - observed).total_seconds()
    if not 0 <= age <= 60:
        raise ValueError('refresh current Native/Source observation before launch')
    source_gate = load_json(raw['canonical_source_gate'])
    for member in source_gate['verified_local_files']:
        path = (canonical_root / member['path']).resolve(strict=True)
        path.relative_to(canonical_root)
        data = read_bound(path, 4 * 1024 * 1024)
        if len(data) != member['bytes'] or sha(data) != member['sha256']:
            raise ValueError('canonical Source checkout no longer matches actual full readback')
    guard = canonical_root / 'tools/research_runtime_guard.py'
    if 'tools/research_runtime_guard.py' not in {m['path'] for m in source_gate['verified_local_files']}:
        raise ValueError('genuine canonical public guard not hash bound')
    verified = {m['path'] for m in source_gate['verified_local_files']}
    # This is an isolated verified canonical tree, not the dirty shared checkout.
    # Hash every project Python dependency in it before importing the guard.
    for path in canonical_root.rglob('*.py'):
        if path.relative_to(canonical_root).as_posix() not in verified:
            raise ValueError('unverified canonical Python dependency')
    guard_out, guard_err, guard_status, guard_stop, _ = collect(
        [sys.executable, '-B', str(guard), 'authorize',
         '--state-file', str(Path(spec['run_state']['path']).resolve()),
         '--events', str(Path(spec['events']['path']).resolve())],
        timeout=30, stdout_cap=2 * 1024 * 1024, stderr_cap=65536)
    if guard_status or guard_stop:
        raise ValueError('canonical runtime guard rejected or exceeded metadata bound')
    actual = load_json(guard_out)
    if actual.get('authorized') is not True or actual['task_id'] != TASK:
        raise ValueError('canonical runtime guard did not authorize exact Task')
    binding = actual['execution_binding']
    original = native['execution_binding']
    for key in ('claim_id', 'publication_id', 'researcher_id', 'session_id', 'ownership_epoch',
                'taskbook_blob_sha1', 'execution_branch', 'execution_branch_base', 'allowed_outputs'):
        if binding[key] != original[key]:
            raise ValueError('fresh guard differs from genuine Native authorization: ' + key)
    for key in ('claim_id', 'publication_id', 'researcher_id', 'session_id'):
        if binding[key] != run[key]:
            raise ValueError('run and claim differ: ' + key)
    intent = native['execution_intent_source']
    if intent['verification'] != 'ACTUAL_NATIVE_INTENT_FOR_WINNING_CLAIM':
        raise ValueError('unverified actual execution intent')
    if sha(raw['execution_intent']) != intent['sha256']:
        raise ValueError('execution intent bytes differ')
    if load_json(raw['execution_intent'])['execution_record_id'] != intent['execution_record_id']:
        raise ValueError('wrong execution intent ID')
    # The independent human review and full historical debt are consumed by
    # the actor, with their exact bytes sealed here. They are not truth flags.
    if not raw['static_review_gate'] or not raw['prep_ledger']:
        raise ValueError('missing consumed review or historical costs')
    if dt.datetime.now(dt.timezone.utc) >= PREP_END:
        raise ValueError('cumulative preparation deadline expired')
    return {'actual_fresh_observation_utc': spec['actual_fresh_observation_utc'],
            'run_id': run['run_id'], 'generation': run['generation'],
            'revision': run['revision'], 'claim_id': run['claim_id'],
            'session_id': run['session_id'], 'researcher_id': run['researcher_id'],
            'publication_id': run['publication_id'], 'ownership_epoch': binding['ownership_epoch'],
            'evidence_sha256': {k: sha(v) for k, v in raw.items()},
            'actual_guard_stdout_sha256': sha(guard_out)}


def clean_env():
    return {'PATH': os.defpath, 'LANG': 'C.UTF-8', 'PYTHONDONTWRITEBYTECODE': '1',
            'PYTHONHASHSEED': '0'}


def collect(command, *, timeout, stdout_cap, stderr_cap, before_exec=None):
    """Bounded child pipes + external whole-job watchdog; one process group."""
    started = time.monotonic()
    child = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, env=clean_env(), start_new_session=True,
                             preexec_fn=before_exec)
    selector = selectors.DefaultSelector()
    for stream, name in ((child.stdout, 'stdout'), (child.stderr, 'stderr')):
        os.set_blocking(stream.fileno(), False)
        selector.register(stream, selectors.EVENT_READ, name)
    data = {'stdout': bytearray(), 'stderr': bytearray()}
    caps = {'stdout': stdout_cap, 'stderr': stderr_cap}
    reason = None
    try:
        while selector.get_map():
            left = timeout - (time.monotonic() - started)
            if left <= 0:
                reason = 'WHOLE_JOB_TIMEOUT'
                break
            for key, _mask in selector.select(min(left, 0.1)):
                chunk = os.read(key.fd, 65536)
                if not chunk:
                    selector.unregister(key.fileobj)
                    key.fileobj.close()
                    continue
                name = key.data
                available = caps[name] - len(data[name])
                data[name].extend(chunk[:available])
                if len(chunk) > available:
                    reason = 'CHILD_OUTPUT_OVER_CAP'
                    break
            if reason:
                break
        if reason:
            os.killpg(child.pid, signal.SIGKILL)
        left = max(0.001, timeout - (time.monotonic() - started))
        try:
            status = child.wait(timeout=left)
        except subprocess.TimeoutExpired:
            os.killpg(child.pid, signal.SIGKILL)
            status = child.wait(timeout=2)
            reason = 'WHOLE_JOB_TIMEOUT'
        return bytes(data['stdout']), bytes(data['stderr']), status, reason, time.monotonic() - started
    finally:
        selector.close()
        if child.poll() is None:
            os.killpg(child.pid, signal.SIGKILL)
            child.wait(timeout=2)
        for stream in (child.stdout, child.stderr):
            stream.close()


# This bootstrap is executed ONLY after legitimate admission in the child.
# Child uses this CONTROL file itself, never an unpinned shell/module lookup.
def original_workload_binding_failure(error, workload_path):
    # The original workload bytes are pinned by PINS to 9ee26056... . Its
    # run_from_bytes lines1..86 are input/source/code binding only; line87
    # defines load_fixed and later lines compile/run science. This boundary
    # is a frozen textual interface, not inferred from exception wording.
    # Walk the ENTIRE traceback because OSError can originate in pathlib.
    if not isinstance(error, (ValueError, OSError, KeyError, TypeError)):
        return False
    cursor = error.__traceback__
    while cursor is not None:
        code = cursor.tb_frame.f_code
        if (code.co_filename == str(workload_path) and code.co_name == 'run_from_bytes'
                and 1 <= cursor.tb_lineno < 87):
            return True
        cursor = cursor.tb_next
    return False


def science_child(base, repository_root, started):
    stage = 'INPUT_HASH'
    try:
        frozen = read_bound(base / 'FROZEN_HANDOFF.json', 16384)
        if sha(frozen) != FROZEN_SHA:
            raise ValueError('wrong original freeze')
        cache = {}
        for name, (size, expected) in PINS.items():
            data = read_bound(base / name, size)
            if len(data) != size or sha(data) != expected:
                raise ValueError('frozen candidate changed: ' + name)
            cache[name] = data
        def load(name):
            path = base / name
            module = {'__name__': 'parity_fixed_' + name, '__file__': str(path)}
            exec(compile(cache[name], str(path), 'exec'), module)
            return module
        stage = 'CODE_CHECKER'
        budget_module = load('resource_budget.py')
        meter = budget_module['Budget'](started)
        # Reservation is external: preserve the frozen pre-serialization
        # snapshot=0. Never charge hypothetical bytes into the original meter.
        worker = load('workload.py')
        output = worker['run_from_bytes'](cache['FIXED_INPUT.json'], repository_root, meter)
        if len(output) > CAP - RESERVE:
            raise budget_module['BudgetStop']('insufficient combined output reservation')
        value = load_json(output)
        positive = value['algorithmically_independent_same_author_check']['all_strictly_positive']
        if type(positive) is not bool:
            raise ValueError('invalid worker outcome')
        meter.check_time()
        sys.stdout.buffer.write(output)
        sys.stdout.buffer.flush()
        return 0 if positive else 2
    except (MemoryError, TimeoutError):
        return 75
    except Exception as error:
        # Never serialize uncontrolled exception text or a giant traceback.
        if type(error).__name__ == 'BudgetStop':
            return 75
        binding_failure = (stage == 'INPUT_HASH' and isinstance(error, (ValueError, OSError))) or original_workload_binding_failure(error, base / 'workload.py')
        return 64 if binding_failure else 70


def final_start_clock(observed):
    # Called AFTER durable PREPARED and immediately before the sole launch.
    now = dt.datetime.now(dt.timezone.utc)
    monotonic = time.monotonic()
    age = (now - dt.datetime.fromisoformat(observed)).total_seconds()
    if now >= PREP_END or not 0 <= age <= 60:
        raise ValueError('final actual start expired prep or Native freshness')
    return now, monotonic


def attempt_path(parent):
    # This fixed scientific unit has ONE allowance across all RUNs/generations.
    # Resume/claim succession never clears its PREPARED/UNKNOWN fence.
    return parent / TASK


def main():
    global SCIENCE_ATTEMPTED
    parser = argparse.ArgumentParser()
    parser.add_argument('--binding', type=Path, required=True)
    parser.add_argument('--canonical-root', type=Path, required=True)
    parser.add_argument('--repository-root', type=Path, required=True)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--attempt-dir', type=Path, required=True)
    args = parser.parse_args()
    binding_raw = read_bound(args.binding, 65536)
    binding = load_json(binding_raw)
    evidence = validate_evidence(binding, args.canonical_root.resolve(strict=True))
    # One immutable fixed-unit fence across RUNs, claims and generations.
    # The actual actor must retain this same durable store across succession.
    parent = args.attempt_dir.resolve(strict=True)
    attempt = attempt_path(parent)
    attempt.mkdir(mode=0o700)  # Any prior/unknown attempt forbids re-execution.
    marker = {'schema': 'PARITY_M7_CONTROL_SINGLE_ATTEMPT_PREPARED_V1', 'task_id': TASK,
              'binding_sha256': sha(binding_raw), 'binding': evidence,
              'candidate_manifest_sha256': FROZEN_SHA, 'launcher_sha256': sha(Path(__file__).read_bytes()),
              'max_invocations': 1, 'retry_policy': 'NONE_EVEN_ON_UNKNOWN',
              'caps': {'seconds': SECONDS, 'address_space_bytes': MEMORY,
                       'combined_output_bytes': CAP, 'auxiliary_reserved_bytes': RESERVE}}
    marker_raw = encoded(marker)
    if len(marker_raw) > 16384:
        raise ValueError('marker over control bound')
    exclusive(attempt / 'PREPARED.json', marker_raw)
    sync_directory(attempt)
    sync_directory(parent)
    # This monotonic clock precedes Popen/preexec/interpreter/import/hash/compile.
    actual_start_utc, started = final_start_clock(evidence['actual_fresh_observation_utc'])
    command = [sys.executable, '-B', str(Path(__file__).resolve()), '_science_child',
               str(args.candidate.resolve(strict=True)), str(args.repository_root.resolve(strict=True)), repr(started)]
    SCIENCE_ATTEMPTED = True  # Even an unknown spawn outcome forbids retry.
    output, error, status, reason, elapsed = collect(command, timeout=max(0.001, SECONDS - (time.monotonic() - started)),
                                                   stdout_cap=CAP - RESERVE, stderr_cap=16384,
                                                   before_exec=deny_network_and_limit)
    summary = {'schema': 'PARITY_M7_CONTROL_SINGLE_ATTEMPT_OUTCOME_V1',
               'prepared_sha256': sha(marker_raw), 'run_id': evidence['run_id'],
               'generation': evidence['generation'], 'actual_job_start_utc': actual_start_utc.isoformat(),
               'worker_start_attempted': True, 'child_returncode': status,
               'external_stop_reason': reason, 'elapsed_whole_job_seconds': time.monotonic() - started,
               'whole_job_cpu_seconds': None, 'peak_RSS_bytes': None,
               'unmeasured_costs': 'CPU_AND_PEAK_RSS_UNKNOWN_NO_ZERO_OR_GLOBAL_RSS_ATTESTATION',
               'stdout_bytes': len(output), 'stdout_sha256': sha(output),
               'stderr_bytes': len(error), 'stderr_sha256': sha(error),
               'complete_scientific_candidate': reason is None and status in (0, 2),
               'mathematical_acceptance': False, 'Native_Task_completion': False,
               'observed_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
    summary_raw = encoded(summary)
    if len(marker_raw) + len(summary_raw) + len(error) > RESERVE:
        raise ValueError('auxiliary output reservation exceeded')
    exclusive(attempt / ('RESULT.json' if summary['complete_scientific_candidate'] else 'INCOMPLETE_STDOUT.bin'), output)
    exclusive(attempt / 'STDERR.bin', error)
    exclusive(attempt / 'OUTCOME.json', summary_raw)
    sync_directory(attempt)
    # No certificate duplication on stdout. The tiny path receipt is also
    # within the reservation; full artifact custody follows separately.
    tiny = encoded({'attempt_directory': str(attempt), 'child_returncode': status,
                    'external_stop_reason': reason, 'Native_Task_completion': False})
    if len(marker_raw) + len(summary_raw) + len(error) + len(tiny) > RESERVE:
        raise ValueError('receipt exceeds reservation')
    sys.stdout.buffer.write(tiny)
    return 124 if reason == 'WHOLE_JOB_TIMEOUT' else (75 if reason else status)


def entrypoint():
    if len(sys.argv) == 5 and sys.argv[1] == '_science_child':
        raise SystemExit(science_child(Path(sys.argv[2]), sys.argv[3], float(sys.argv[4])))
    try:
        raise SystemExit(main())
    except Exception:
        # Denied metadata never starts science. Full original external receipts
        # remain in the actor's custody; do not output unbounded error strings.
        if SCIENCE_ATTEMPTED:
            print('{"state":"POST_START_CONTROL_OR_CUSTODY_FAILURE_OUTCOME_UNKNOWN_NO_RETRY","worker_may_have_started":true}')
            raise SystemExit(70)
        print('{"state":"DENIED_BEFORE_WORKER_START_NO_RETRY","worker_may_have_started":false}')
        raise SystemExit(77)


if __name__ == '__main__':
    entrypoint()
