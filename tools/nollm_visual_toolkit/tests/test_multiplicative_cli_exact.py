from __future__ import annotations
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from nollm_visual_toolkit import multiplicative as m


class MultiplicativeCliExactTests(unittest.TestCase):
    def test_parse_integer_fraction_decimal_without_float(self):
        cases = {
            '2': ((2, 1), {'text':'2','syntax':'INTEGER','numerator':'2','denominator':'1','unreduced':True}),
            '1/2': ((1, 2), {'text':'1/2','syntax':'FRACTION','numerator':'1','denominator':'2','unreduced':True}),
            '2/2': ((2, 2), {'text':'2/2','syntax':'FRACTION','numerator':'2','denominator':'2','unreduced':True}),
            '0.50': ((50, 100), {'text':'0.50','syntax':'DECIMAL','numerator':'50','denominator':'100','unreduced':True}),
            '2.0': ((20, 10), {'text':'2.0','syntax':'DECIMAL','numerator':'20','denominator':'10','unreduced':True}),
        }
        for text, expected in cases.items():
            self.assertEqual(m.parse_cell_scale_text(text), expected)

    def test_parse_rejects_ambiguous_noncanonical_or_nonpositive_text(self):
        bad = ('', '0', '0.0', '-1', '+1', ' 1/2', '1/2 ', '01/2', '1/02', '.5', '1.',
               '1e-3', '1//2', '1/0', 'nan', 'inf', '1_000', '0.' + '1' * 257)
        for value in bad:
            with self.subTest(value=value), self.assertRaises(ValueError):
                m.parse_cell_scale_text(value)
        for value in (None, 0.5, (1,2)):
            with self.subTest(value=value), self.assertRaises(ValueError):
                m.parse_cell_scale_text(value)

    def test_precision_budget_validation(self):
        self.assertEqual(m._cell_precision(8, 512), (8, 512))
        for pair in ((7,64),(64,513),(128,64),(64.0,192),(True,192)):
            with self.subTest(pair=pair), self.assertRaises(ValueError):
                m._cell_precision(*pair)

    def test_exact_cli_report_and_hex_keep_display_and_cell_scales_separate(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);out=root/'lab.html';report=root/'report.json';data=root/'data.json'
            def fake_render(path, settings):
                Path(path).write_text('<!doctype html><title>legacy display stub</title>', encoding='utf-8')
                return Path(path)
            argv=['multiplicative','--count','64','--scale','2','--cell-scale','0.50',
                  '--cell-bits','64','--cell-max-bits','192','--out',str(out),
                  '--report',str(report),'--hex-data',str(data)]
            stderr=io.StringIO()
            with mock.patch.object(sys,'argv',argv), mock.patch.object(m,'render',side_effect=fake_render), contextlib.redirect_stderr(stderr):
                self.assertEqual(m.main(),0)
            r=json.loads(report.read_text())
            d=json.loads(data.read_text())
            self.assertEqual(r['schema'],m.EXACT_REPORT_SCHEMA)
            self.assertEqual(r['config']['scale'],2.0)
            self.assertEqual(r['cell_scale_source']['text'],'0.50')
            self.assertEqual(r['cell_scale_source']['numerator'],'50')
            self.assertEqual(r['cell_scale_source']['denominator'],'100')
            self.assertEqual(r['cell_membership_exact']['scale'],{'numerator':'50','denominator':'100'})
            self.assertEqual(r['cell_membership_exact']['status'],'CERTIFIED_ALL')
            self.assertIn('legacy floating observer',r['html_observer_boundary'])
            self.assertEqual(d['metadata']['config']['scale'],2.0)
            self.assertEqual(d['metadata']['cell_scale_source']['text'],'0.50')
            self.assertEqual(d['metadata']['cell_scale_source']['numerator'],'50')
            self.assertIn('report/hex-data only',stderr.getvalue())

    def test_legacy_cli_report_schema_and_payload_remain_v1(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);out=root/'lab.html';report=root/'report.json'
            def fake_render(path, settings):
                Path(path).write_text('legacy', encoding='utf-8');return Path(path)
            argv=['multiplicative','--count','64','--scale','1.5','--out',str(out),'--report',str(report)]
            with mock.patch.object(sys,'argv',argv), mock.patch.object(m,'render',side_effect=fake_render):
                self.assertEqual(m.main(),0)
            r=json.loads(report.read_text())
            expected_field=m.build_field(m.config(64,'valuation',1.5))
            expected={'schema':m.REPORT_SCHEMA,'lab_version':m.LAB_VERSION,'config':expected_field['config'],
                      'statistics':m.statistics(expected_field),'all_pairs':m.all_pair_audit(expected_field)}
            self.assertEqual(r,expected)

    def test_exact_cli_requires_a_machine_output_and_disables_preview(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);out=root/'lab.html'
            for extra in ([], ['--preview']):
                argv=['multiplicative','--count','16','--cell-scale','1/2','--out',str(out),*extra]
                render=mock.Mock()
                with mock.patch.object(sys,'argv',argv), mock.patch.object(m,'render',render), self.assertRaises(SystemExit) as cm:
                    m.main()
                self.assertEqual(cm.exception.code,2)
                render.assert_not_called()

    def test_precision_flags_require_cell_scale_and_fail_before_render(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);out=root/'lab.html';report=root/'report.json'
            bad_argvs=[
                ['multiplicative','--count','16','--cell-bits','32','--out',str(out),'--report',str(report)],
                ['multiplicative','--count','16','--cell-scale','1/2','--cell-bits','7','--out',str(out),'--report',str(report)],
                ['multiplicative','--count','16','--cell-scale','1/2','--cell-bits','128','--cell-max-bits','64','--out',str(out),'--report',str(report)],
            ]
            for argv in bad_argvs:
                render=mock.Mock()
                with self.subTest(argv=argv), mock.patch.object(sys,'argv',argv), mock.patch.object(m,'render',render), self.assertRaises(SystemExit) as cm:
                    m.main()
                self.assertEqual(cm.exception.code,2)
                render.assert_not_called()

    def test_low_budget_report_surfaces_unresolved_but_hex_request_fails_before_writes(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);out=root/'lab.html';report=root/'report.json';data=root/'data.json'
            def fake_render(path, settings): Path(path).write_text('legacy');return Path(path)
            report_only=['multiplicative','--count','512','--scheme','mixed','--cell-scale','1',
                         '--cell-bits','8','--cell-max-bits','8','--out',str(out),'--report',str(report)]
            with mock.patch.object(sys,'argv',report_only), mock.patch.object(m,'render',side_effect=fake_render), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(m.main(),0)
            r=json.loads(report.read_text())
            self.assertEqual(r['cell_membership_exact']['status'],'UNRESOLVED_BOUNDARY')
            self.assertTrue(r['cell_membership_exact']['unresolved_identities'])
            out.unlink();report.unlink()
            both=['multiplicative','--count','512','--scheme','mixed','--cell-scale','1',
                  '--cell-bits','8','--cell-max-bits','8','--out',str(out),'--report',str(report),'--hex-data',str(data)]
            render=mock.Mock(side_effect=fake_render)
            with mock.patch.object(sys,'argv',both), mock.patch.object(m,'render',render), self.assertRaises(SystemExit) as cm:
                m.main()
            self.assertEqual(cm.exception.code,2)
            render.assert_not_called()
            self.assertFalse(out.exists());self.assertFalse(report.exists());self.assertFalse(data.exists())

    def test_help_exposes_exact_scale_as_separate_from_display_scale(self):
        out=io.StringIO()
        with mock.patch.object(sys,'argv',['multiplicative','--help']), contextlib.redirect_stdout(out), self.assertRaises(SystemExit) as cm:
            m.main()
        self.assertEqual(cm.exception.code,0)
        text=out.getvalue()
        self.assertIn('--scale',text);self.assertIn('legacy/display scale only',text)
        self.assertIn('--cell-scale',text);self.assertIn('--cell-bits',text);self.assertIn('--cell-max-bits',text)

    def test_cli_fraction_preserves_unreduced_source(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);out=root/'lab.html';report=root/'report.json'
            def fake_render(path, settings): Path(path).write_text('legacy');return Path(path)
            argv=['multiplicative','--count','32','--cell-scale','2/2','--out',str(out),'--report',str(report)]
            with mock.patch.object(sys,'argv',argv), mock.patch.object(m,'render',side_effect=fake_render), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(m.main(),0)
            r=json.loads(report.read_text())
            self.assertEqual(r['cell_scale_source']['text'],'2/2')
            self.assertEqual(r['cell_membership_exact']['scale'],{'numerator':'2','denominator':'2'})


if __name__=='__main__':
    unittest.main(verbosity=2)
