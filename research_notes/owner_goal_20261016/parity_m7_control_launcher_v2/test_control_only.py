"""Synthetic CONTROL tests ONLY. Never load/hash/parse any frozen science file."""
import importlib.util
import contextlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock

BASE = Path(__file__).resolve().parent

def control_module(name):
    spec = importlib.util.spec_from_file_location(name, BASE / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

launcher = control_module('parity_m7_launch_v2')
codec = control_module('parity_m7_source_codec_v2')

class ControlTests(unittest.TestCase):
    def test_child_bytes_and_status(self):
        out, err, status, why, elapsed = launcher.collect(
            [sys.executable, '-B', '-c', "import sys;sys.stdout.buffer.write(b'synthetic');sys.stderr.write('metadata')"],
            timeout=2, stdout_cap=100, stderr_cap=100,
            before_exec=launcher.deny_network_and_limit)
        self.assertEqual((out, err, status, why), (b'synthetic', b'metadata', 0, None))

    def test_os_network_denied_before_interpreter(self):
        code = 'import socket,sys\ntry: socket.socket()\nexcept PermissionError: sys.exit(0)\nsys.exit(99)'
        out, err, status, why, elapsed = launcher.collect(
            [sys.executable, '-B', '-c', code], timeout=2, stdout_cap=100, stderr_cap=100,
            before_exec=launcher.deny_network_and_limit)
        self.assertEqual((status, why), (0, None))

    def test_memory_before_interpreter(self):
        code = 'import resource;assert resource.getrlimit(resource.RLIMIT_AS)==(536870912,536870912)'
        self.assertEqual(launcher.collect([sys.executable, '-B', '-c', code], timeout=2,
                         stdout_cap=100, stderr_cap=100, before_exec=launcher.deny_network_and_limit)[2], 0)

    def test_external_timeout(self):
        out, err, status, why, elapsed = launcher.collect(
            [sys.executable, '-B', '-c', 'import time;time.sleep(5)'], timeout=0.15,
            stdout_cap=100, stderr_cap=100)
        self.assertEqual(why, 'WHOLE_JOB_TIMEOUT')
        self.assertLess(elapsed, 2)

    def test_pipe_overflow_retains_bounded_prefix(self):
        out, err, status, why, elapsed = launcher.collect(
            [sys.executable, '-B', '-c', "import sys;sys.stdout.buffer.write(b'x'*10000)"],
            timeout=2, stdout_cap=123, stderr_cap=100)
        self.assertEqual(len(out), 123)
        self.assertEqual(why, 'CHILD_OUTPUT_OVER_CAP')

    def test_missing_metadata_denies_without_science(self):
        with tempfile.TemporaryDirectory(dir=BASE) as temp:
            root = Path(temp)
            (root / 'binding.json').write_text('{}')
            p = subprocess.run([sys.executable, '-B', str(BASE/'parity_m7_launch_v2.py'),
                                '--binding', str(root/'binding.json'), '--canonical-root', str(root),
                                '--repository-root', str(root), '--candidate', str(root),
                                '--attempt-dir', str(root)], capture_output=True)
            self.assertEqual(p.returncode, 77)
            self.assertFalse(any(p.name.startswith('RUN-') for p in root.iterdir()))

    def test_resume_generation_cannot_clear_unit_fence(self):
        with tempfile.TemporaryDirectory(dir=BASE) as temp:
            parent = Path(temp)
            first = launcher.attempt_path(parent)
            first.mkdir()
            (first/'PREPARED.json').write_text('{"run_id":"RUN-synthetic-g1","generation":1}')
            # The successor's run_id/generation are deliberately not keys in
            # the unit path. An existing UNKNOWN attempt remains exclusive.
            with self.assertRaises(FileExistsError):
                launcher.attempt_path(parent).mkdir()

    def test_final_start_rechecks_expired_observation_and_cutoff(self):
        with mock.patch.object(launcher, 'PREP_END', launcher.dt.datetime.now(launcher.dt.timezone.utc) + launcher.dt.timedelta(seconds=60)):
            old = (launcher.dt.datetime.now(launcher.dt.timezone.utc)-launcher.dt.timedelta(seconds=61)).isoformat()
            with self.assertRaises(ValueError):
                launcher.final_start_clock(old)
        with mock.patch.object(launcher, 'PREP_END', launcher.dt.datetime.now(launcher.dt.timezone.utc)-launcher.dt.timedelta(seconds=1)):
            fresh = launcher.dt.datetime.now(launcher.dt.timezone.utc).isoformat()
            with self.assertRaises(ValueError):
                launcher.final_start_clock(fresh)

    def test_post_start_control_failure_is_unknown_not_denial(self):
        with tempfile.TemporaryDirectory(dir=BASE) as temp:
            root = Path(temp)
            (root/'binding.json').write_text('{}')
            fake = {'run_id':'RUN-SYNTHETIC', 'generation':1,
                    'actual_fresh_observation_utc':launcher.dt.datetime.now(launcher.dt.timezone.utc).isoformat()}
            args = ['control-test', '--binding', str(root/'binding.json'),
                    '--canonical-root', str(root), '--repository-root', str(root),
                    '--candidate', str(root), '--attempt-dir', str(root)]
            output = io.StringIO()
            # No guard/Native fixture is a real grant: replace metadata and
            # the child collector explicitly; ZERO actual science subprocess.
            with mock.patch.object(sys, 'argv', args), mock.patch.object(launcher, 'validate_evidence', return_value=fake), \
                 mock.patch.object(launcher, 'collect', side_effect=OSError('synthetic post-start custody failure')), \
                 mock.patch.object(launcher, 'SCIENCE_ATTEMPTED', False), contextlib.redirect_stdout(output):
                with self.assertRaises(SystemExit) as stopped:
                    launcher.entrypoint()
                self.assertEqual(stopped.exception.code, 70)
            value = json.loads(output.getvalue())
            self.assertTrue(value['worker_may_have_started'])
            self.assertIn('OUTCOME_UNKNOWN', value['state'])
            self.assertTrue((launcher.attempt_path(root)/'PREPARED.json').is_file())

    def test_codec_exact_worstcase_ascii_roundtrip(self):
        with tempfile.TemporaryDirectory(dir=BASE) as temp:
            root = Path(temp)
            data = b'x' * codec.RAW_CAP  # Synthetic bytes, no scientific JSON.
            (root/'raw').write_bytes(data)
            index = codec.pack(root/'raw', root/'carrier', report_started_monotonic=time.monotonic())
            self.assertEqual(len(index['parts']), 32)
            self.assertEqual(codec.unpack(root/'carrier'), data)
            self.assertLessEqual(sum(p.stat().st_size for p in (root/'carrier').iterdir()), codec.ENCODED_CAP)
            with self.assertRaises(FileExistsError):
                codec.pack(root/'raw', root/'carrier', report_started_monotonic=time.monotonic())

    def test_codec_corruption_and_expiry(self):
        with tempfile.TemporaryDirectory(dir=BASE) as temp:
            root = Path(temp)
            (root/'raw').write_bytes(b'synthetic')
            with self.assertRaises(ValueError):
                codec.pack(root/'raw', root/'expired', report_started_monotonic=time.monotonic()-301)
            codec.pack(root/'raw', root/'carrier', report_started_monotonic=time.monotonic())
            (root/'carrier/part-00.txt').write_bytes(b'corrupted')
            with self.assertRaises(ValueError):
                codec.unpack(root/'carrier')

if __name__ == '__main__':
    unittest.main(verbosity=2)
