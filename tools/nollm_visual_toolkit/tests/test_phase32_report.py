from __future__ import annotations

import ast
import contextlib
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from nollm_visual_toolkit import phase32_lab as p, phase32_report as r, core
from nollm_visual_toolkit import multiplicative as m, multiplicative_report as old_reader

ROOT = Path(__file__).resolve().parents[3]
COUNTS = {'replay_cases': 0, 'rejected_cases': 0, 'subprocesses': 0}


def example(count=64, mode='golden', pitch='1', bits=64, maximum=192, scale=10**6, **kwargs):
    pair, source = m.parse_cell_scale_text(pitch)
    model = p.build(p.machine_config(count, mode, **kwargs), cell_pitch=pair,
                    cell_bits=bits, cell_max_bits=maximum, include_display=False)
    model['cell_pitch_source'] = source
    return p.machine_report(model, readout_scale=scale), model


def call(*args):
    out, err = io.StringIO(), io.StringIO()
    with patch.object(sys, 'argv', ['phase32_report', *map(str, args)]), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            code = r.main()
        except SystemExit as exc:
            code = exc.code
    return code, out.getvalue(), err.getvalue()


def no_float(value):
    if type(value) is float:
        return False
    if type(value) is dict:
        return all(no_float(x) for x in value.values())
    if type(value) is list:
        return all(no_float(x) for x in value)
    return True


class Phase32ReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report, cls.model = example()

    def reject(self, value):
        with self.assertRaises(ValueError):
            r.replay_machine_report(value)
        COUNTS['rejected_cases'] += 1

    def check_replay(self, report, model):
        got = r.replay_machine_report(report)
        self.assertEqual(got, model)
        COUNTS['replay_cases'] += 1
        return got

    def test_complete_model_replayed_not_only_aggregate(self):
        got = self.check_replay(self.report, self.model)
        self.assertIsNot(got, self.model)
        self.assertEqual(got['cell_membership_exact']['certificates'], self.model['cell_membership_exact']['certificates'])

    def test_lexical_sources_unreduced(self):
        for pitch in ('0.50', '2/2', '2.0', '3/2'):
            record, model = example(pitch=pitch)
            self.check_replay(record, model)
            self.assertEqual(record['cell_pitch_source']['text'], pitch)
            self.assertEqual(model['cell_membership_exact']['certifier_scale']['numerator'], record['cell_pitch_source']['denominator'])

    def test_direct_integer_ratio_source_does_not_gain_spelling(self):
        model = p.build(p.machine_config(32), cell_pitch=(50, 100), include_display=False)
        report = p.machine_report(model)
        got = self.check_replay(report, model)
        self.assertNotIn('text', got['cell_pitch_source'])
        self.assertEqual(got['cell_pitch_source']['denominator'], '100')

    def test_modes_and_custom_observations(self):
        for mode in ('golden', 'hash', 'spiral'):
            for pitch in ('0.50', '1', '3/2'):
                report, model = example(128, mode, pitch, scale=10**12+7, sectors=31, rings=7, seed=23)
                self.check_replay(report, model)
                self.assertEqual(len(report['metrics']['equal_area_counts']), 31*7)

    def test_zero_and_nonclosure_are_preserved(self):
        report, model = example(32, a=0, b=7)
        self.check_replay(report, model)
        self.assertIsNone(report['multiplication']['phase_defect_uint32'])
        report, model = example(32, 'spiral', a=2, b=2)
        self.check_replay(report, model)
        self.assertEqual(report['multiplication']['phase_defect_uint32'], p.GOLDEN)

    def test_true_lexicographic_tie_and_base_certificate_survive(self):
        report, model = example(16, pitch='2', overrides={'2': p.DEN//8})
        got = self.check_replay(report, model)
        cert = got['cell_membership_exact']['certificates'][4]
        self.assertEqual(cert['cell'], ['-1', '1'])
        self.assertEqual(cert['base_certificate']['cell'], ['0', '1'])

    def test_unresolved_budget_is_not_refined(self):
        report, model = example(128, 'hash', bits=8, maximum=8)
        got = self.check_replay(report, model)
        self.assertEqual(got['cell_membership_exact']['status'], 'UNRESOLVED_BOUNDARY')
        self.assertEqual(got['cell_precision'], {'initial_bits': 8, 'max_bits': 8})
        with self.assertRaisesRegex(ValueError, 'unresolved'):
            r.machine_report_to_data(report)

    def test_null_readout_is_not_replaced_with_default(self):
        report, model = example(scale=None)
        self.check_replay(report, model)
        self.assertIsNone(report['metrics']['angular_cv_squared_exact']['readout'])
        self.assertIsNone(report['metrics']['equal_area_cv_squared_exact']['readout'])

    def test_every_top_level_result_group_checked(self):
        for key in r.REPORT_KEYS:
            value = copy.deepcopy(self.report)
            value[key] = {} if value[key] is None else None
            self.reject(value)
        bad = copy.deepcopy(self.report)
        bad['metrics']['angular_counts'][0] += 1
        self.reject(bad)
        bad = copy.deepcopy(self.report)
        bad['cell_membership_exact']['phase_source_sha256'] = '0'*64
        self.reject(bad)

    def test_inexact_json_tokens_rejected(self):
        text = json.dumps(self.report)
        for token in ('0.0', '0e0', 'NaN', 'Infinity', '-Infinity', '1e999'):
            with self.assertRaises(ValueError):
                r.parse_machine_report(text.replace('"seed": 0', '"seed": ' + token, 1))
            COUNTS['rejected_cases'] += 1

    def test_duplicate_top_and_nested_keys_rejected(self):
        text = json.dumps(self.report)
        for bad in (text.replace('"seed": 0', '"seed": 0, "seed": 0', 1),
                    text.replace('"schema":', '"schema": "x", "schema":', 1),
                    text.replace('"numerator": "1"', '"numerator": "1", "numerator": "1"', 1)):
            with self.assertRaisesRegex(ValueError, 'duplicate'):
                r.parse_machine_report(bad)
            COUNTS['rejected_cases'] += 1

    def test_direct_api_non_json_types_rejected(self):
        for val in (0.0, object(), (1, 2), {1: 2}):
            bad = copy.deepcopy(self.report); bad['metrics'] = val
            self.reject(bad)

    def test_bool_and_integer_are_not_interchangeable(self):
        for key in ('count', 'seed', 'rings', 'sectors', 'a', 'b'):
            bad = copy.deepcopy(self.report); bad['config'][key] = True
            self.reject(bad)
        bad = copy.deepcopy(self.report)
        bad['metrics']['empty_bins_not_missing_ids'] = 1
        self.reject(bad)
        bad = copy.deepcopy(self.report); bad['cell_pitch_source']['unreduced'] = 1
        self.reject(bad)

    def test_pitch_sources_reject_spelling_mismatch_and_invalid_ratios(self):
        for source in ({'numerator': '0', 'denominator': '1', 'unreduced': True},
                       {'numerator': '1', 'denominator': '0', 'unreduced': True},
                       {'numerator': '01', 'denominator': '1', 'unreduced': True},
                       {'numerator': 1, 'denominator': '1', 'unreduced': True},
                       {**self.report['cell_pitch_source'], 'text': '2/2'},
                       {**self.report['cell_pitch_source'], 'unreduced': False}):
            bad = copy.deepcopy(self.report); bad['cell_pitch_source'] = source
            self.reject(bad)

    def test_consistently_changed_source_is_another_valid_observation(self):
        report, model = example(seed=1)
        self.assertNotEqual(report, self.report)
        self.check_replay(report, model)
        self.assertIn('NO_SOURCE_AUTHENTICATION', report['observation_scope'])

    def test_parse_is_not_mathematical_verification(self):
        bad = copy.deepcopy(self.report); bad['metrics']['collision_excess'] += 1
        parsed = r.parse_machine_report(json.dumps(bad))
        self.assertEqual(parsed, bad)
        self.reject(parsed)

    def test_missing_and_inconsistent_readout_scales_rejected(self):
        for scale in ('0', '01', '-1', '1e6', 1000000, True, '', '1'*257):
            bad = copy.deepcopy(self.report)
            bad['metrics']['angular_cv_squared_exact']['readout']['scale'] = scale
            self.reject(bad)
        bad = copy.deepcopy(self.report); del bad['metrics']['angular_cv_squared_exact']['readout']
        self.reject(bad)
        bad = copy.deepcopy(self.report); bad['metrics']['angular_cv_squared_exact']['readout'] = None
        self.reject(bad)

    def test_original_precision_and_histogram_dimensions_required(self):
        for budget in ({}, {'initial_bits': 8}, {'initial_bits': True, 'max_bits': 192},
                       {'initial_bits': 128, 'max_bits': 64}, {'initial_bits': 64, 'max_bits': 513}):
            bad = copy.deepcopy(self.report); bad['cell_precision'] = budget
            self.reject(bad)
        for key in ('pitch', 'yaw', 'zoom'):
            bad = copy.deepcopy(self.report); bad['config'][key] = 1
            self.reject(bad)

    def test_report_schemas_remain_separate(self):
        with self.assertRaises(ValueError):
            old_reader.parse_machine_report(json.dumps(self.report))
        old = json.loads((ROOT/'evidence/migration12/example_exact_report.json').read_text())
        with self.assertRaises(ValueError):
            r.parse_machine_report(json.dumps(old))

    def test_all_ids_and_full_source_report_retained(self):
        data = r.machine_report_to_data(self.report)
        self.assertEqual([x['id'] for x in data['records']], [str(n) for n in range(64)])
        self.assertEqual(data['metadata']['source_machine_report'], self.report)
        digest = hashlib.sha256(r._canonical(self.report).encode()).hexdigest()
        self.assertEqual(data['metadata']['machine_report_import']['canonical_report_sha256'], digest)
        self.assertEqual(data['records'], p.hex_data(self.model)['records'])
        self.assertIsNone(data['records'][0]['fields']['phase_numerator'])

    def test_large_readout_remains_exact_and_has_no_pixels(self):
        report, _ = example(scale=2**200)
        data = r.machine_report_to_data(report)
        self.assertTrue(no_float(data))
        self.assertFalse(any(k.startswith('ideal') for x in data['records'] for k in x['fields']))
        self.assertEqual(data['metadata']['source_machine_report']['metrics']['angular_cv_squared_exact']['readout']['scale'], str(2**200))

    def test_exports_and_models_are_detached(self):
        before = copy.deepcopy(self.report)
        model = r.replay_machine_report(self.report)
        model['cell_pitch_source']['numerator'] = '999'
        data = r.machine_report_to_data(self.report)
        data['metadata']['source_machine_report']['config']['count'] = 2
        self.assertEqual(self.report, before)

    def test_adapter_uses_verified_snapshot_during_caller_mutation(self):
        report = copy.deepcopy(self.report); before = copy.deepcopy(report); original = p.build
        def changing(*args, **kwargs):
            report['config']['seed'] = 123
            return original(*args, **kwargs)
        with patch.object(p, 'build', side_effect=changing):
            data = r.machine_report_to_data(report)
        self.assertEqual(data['metadata']['source_machine_report'], before)

    def test_file_bom_and_invalid_encoding(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td)/'r.json'; path.write_bytes(b'\xef\xbb\xbf' + json.dumps(self.report).encode())
            self.assertEqual(r.load_machine_report(path), self.report)
            path.write_bytes(b'\xff\xfe')
            with self.assertRaises(UnicodeError): r.load_machine_report(path)

    def test_reader_nesting_and_byte_budgets(self):
        for text in ('['*70+'0'+']'*70, '['*1500+'0'+']'*1500):
            with self.assertRaises(ValueError): r.parse_machine_report(text)
        with patch.object(r, 'MAX_REPORT_BYTES', 128):
            with self.assertRaisesRegex(ValueError, 'byte budget'): r.parse_machine_report(' '*129)
            with tempfile.TemporaryDirectory() as td:
                path = Path(td)/'r.json'; path.write_bytes(b' '*129)
                with self.assertRaisesRegex(ValueError, 'byte budget'): r.load_machine_report(path)

    def test_ordinary_visual_data_unchanged(self):
        with tempfile.TemporaryDirectory() as td:
            for suffix in ('json', 'csv'):
                path = Path(td)/('d.'+suffix); data = core.demo_hex(64)
                core.write_data(data, path)
                self.assertEqual(core.read_data(path), data)

    def test_original_multiplicative_report_route_unchanged(self):
        path = ROOT/'evidence/migration12/example_exact_report.json'
        report = old_reader.load_machine_report(path)
        self.assertEqual(core.read_data(path), old_reader.machine_report_to_data(report))

    def test_core_routes_phase32_through_strict_replay(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td)/'r.json'; text = json.dumps(self.report); path.write_text(text)
            self.assertEqual(core.read_data(path), r.machine_report_to_data(self.report))
            path.write_text(text.replace('"seed": 0', '"seed": 0.0', 1))
            with self.assertRaises(ValueError): core.read_data(path)

    def test_cli_real_subprocess_json_and_csv(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); src = root/'r.json'; verified = root/'v.json'; data_path = root/'d.csv'
            src.write_text(json.dumps(self.report)); env = dict(os.environ)
            env['PYTHONPATH'] = str(ROOT/'src')+os.pathsep+str(ROOT/'tools/nollm_visual_toolkit')
            result = subprocess.run([sys.executable, '-m', 'nollm_visual_toolkit.phase32_report', str(src),
                                     '--verified-report', str(verified), '--hex-data', str(data_path)],
                                    cwd=root, env=env, capture_output=True, text=True, timeout=30)
            COUNTS['subprocesses'] += 1
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)['status'], 'REPLAY_MATCHED')
            self.assertEqual(json.loads(verified.read_text()), self.report)
            self.assertEqual(core.read_data(data_path), r.machine_report_to_data(self.report))

    def test_cli_verify_only_does_not_write(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); path = root/'r.json'; path.write_text(json.dumps(self.report))
            code, out, err = call(path)
            self.assertEqual(code, 0, err); self.assertEqual(json.loads(out)['population'], 64)
            self.assertEqual(list(root.iterdir()), [path])

    def test_cli_unresolved_report_and_export_preflight(self):
        report, _ = example(128, 'hash', bits=8, maximum=8)
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); src=root/'r.json'; dst=root/'v.json'; data=root/'d.json'
            src.write_text(json.dumps(report)); code, _, err = call(src, '--verified-report', dst)
            self.assertEqual(code, 0, err); self.assertEqual(json.loads(dst.read_text()), report)
            dst.write_text('preserve'); data.write_text('preserve')
            code, _, err = call(src, '--verified-report', dst, '--hex-data', data)
            self.assertEqual(code, 2); self.assertIn('unresolved', err)
            self.assertEqual(dst.read_text(), 'preserve'); self.assertEqual(data.read_text(), 'preserve')

    def test_cli_out_of_carrier_does_not_reject_source_report(self):
        report, _ = example(16, pitch='0.0000001')
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); src=root/'r.json'; dst=root/'v.json'; data=root/'d.json'; src.write_text(json.dumps(report))
            code, _, err=call(src, '--verified-report', dst); self.assertEqual(code, 0, err)
            dst.unlink(); code, _, err=call(src, '--verified-report', dst, '--hex-data', data)
            self.assertEqual(code, 2); self.assertIn('exact browser range', err)
            self.assertFalse(dst.exists()); self.assertFalse(data.exists())

    def test_aliases_and_hardlinks_preserve_input(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); src=root/'r.json'; src.write_text(json.dumps(self.report)); before=src.read_bytes()
            link=root/'link.json'; os.link(src, link)
            symbolic=root/'sym.json'; symbolic.symlink_to(src)
            for target in (src, link, symbolic):
                code, _, _=call(src, '--verified-report', target)
                self.assertEqual(code, 2); self.assertEqual(src.read_bytes(), before)
            out=root/'out.json'; code, _, _=call(src, '--verified-report', out, '--hex-data', out)
            self.assertEqual(code, 2); self.assertFalse(out.exists())

    def test_invalid_cli_input_has_no_outputs_or_traceback(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); src=root/'r.json'; dst=root/'v.json'
            for raw in (b'bad', b'\xff', b'[]'):
                src.write_bytes(raw); code, _, err=call(src, '--verified-report', dst)
                self.assertEqual(code, 2); self.assertNotIn('Traceback', err); self.assertFalse(dst.exists())

    def test_reader_has_no_implicit_precision_or_display_override(self):
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'r.json'; path.write_text(json.dumps(self.report))
            for args in (('--cell-bits', '128'), ('--display-scale', '1'), ('--preview',)):
                code, _, _=call(path, *args); self.assertEqual(code, 2)

    def test_exact_replay_does_not_call_display_geometry(self):
        def forbidden(*args, **kwargs): raise AssertionError('display path was executed')
        with contextlib.ExitStack() as stack:
            for name in ('position', 'quantize', 'render', 'validate_config'):
                stack.enter_context(patch.object(p, name, side_effect=forbidden))
            for name in ('sqrt', 'sin', 'cos', 'isfinite'):
                stack.enter_context(patch.object(p.math, name, side_effect=forbidden))
            self.check_replay(self.report, self.model)
            self.assertTrue(no_float(r.machine_report_to_data(self.report)))

    def test_absent_brc_never_falls_back(self):
        from nollm_visual_toolkit import certified_hex as c
        with patch.object(c, '_brc', side_effect=RuntimeError('Certified cells require Enterprise Math BRC. No approximate fallback.')):
            with self.assertRaisesRegex(ValueError, 'no approximate fallback'):
                r.replay_machine_report(self.report)
            with tempfile.TemporaryDirectory() as td:
                path=Path(td)/'r.json'; path.write_text(json.dumps(self.report))
                code, _, err=call(path); self.assertEqual(code, 2); self.assertNotIn('Traceback', err)

    def test_existing_exact_consumers_get_identical_centers(self):
        data=r.machine_report_to_data(self.report); original=p.hex_data(self.model)
        self.assertEqual(core.collision_groups(data), core.collision_groups(original))
        self.assertEqual(core.neighborhood(data, '3', 2), core.neighborhood(original, '3', 2))
        self.assertEqual(core.trajectory(data, 3, 2), core.trajectory(original, 3, 2))
        self.assertEqual(core.profile(data, 's'), core.profile(original, 's'))

    def test_existing_arithmetic_sources_unchanged(self):
        files={'phase32_lab.py':'92ae69d0d3d2b9223ed7209db7e4b0949bfa9b6e',
               'certified_hex.py':'f7f3425636f8913cf36a41ad1dcbabfb6803890e',
               'multiplicative.py':'4edda0928d9a5275cce93576c3430ec6eef426ed',
               'multiplicative_report.py':'b15c73d205f89558df45c75867ffd38180bf6a5a'}
        for name, expected in files.items():
            raw=(ROOT/'tools/nollm_visual_toolkit/nollm_visual_toolkit'/name).read_bytes()
            self.assertEqual(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
