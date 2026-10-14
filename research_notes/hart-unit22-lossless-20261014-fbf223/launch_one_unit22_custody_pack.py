#!/usr/bin/env python3
"""One custody process; no scientific invocation or automatic retry."""
import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent

def utc():
    return datetime.now(timezone.utc).isoformat()

def save(name, value):
    with (OUT / name).open('x') as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write('\n')
        f.flush()
        os.fsync(f.fileno())
    fd = os.open(OUT, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)

def main():
    started = utc()
    t0, c0 = time.perf_counter_ns(), time.process_time_ns()
    save('UNIT22_CUSTODY_LAUNCH_STARTED.json', {'started_utc': started, 'launcher_pid': os.getpid(), 'invocations': 1, 'scientific_invocations': 0})
    with (OUT / 'UNIT22_CUSTODY_PACK_STDOUT_STDERR.log').open('xb') as log:
        process = subprocess.Popen([sys.executable, str(OUT / 'package_unit22_streaming_losslessly_local_only.py')], stdout=log, stderr=subprocess.STDOUT)
        save('UNIT22_CUSTODY_PROCESS_START.json', {'started_utc': utc(), 'pid': process.pid, 'launcher_pid': os.getpid(), 'argv': process.args, 'scientific_invocations': 0})
        print(json.dumps({'phase': 'CUSTODY_PROCESS_STARTED', 'pid': process.pid, 'launcher_pid': os.getpid(), 'utc': utc()}), flush=True)
        code = process.wait()
        log.flush()
        os.fsync(log.fileno())
    value = {'started_utc': started, 'finished_utc': utc(), 'pid': process.pid, 'launcher_pid': os.getpid(), 'exit_code': code, 'invocations': 1, 'scientific_invocations': 0, 'wrapper_wall_ns': time.perf_counter_ns() - t0, 'wrapper_cpu_ns': time.process_time_ns() - c0, 'log_bytes': (OUT / 'UNIT22_CUSTODY_PACK_STDOUT_STDERR.log').stat().st_size}
    save('UNIT22_CUSTODY_NATURAL_TERMINAL.json', value)
    print(json.dumps(value), flush=True)
    return code

if __name__ == '__main__':
    raise SystemExit(main())
