"""M13 actual reader and explicit projection checks; no simulated browser receipt."""
from __future__ import annotations
import ast
import contextlib
import copy
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from nollm_visual_toolkit import core, multiplicative as m, multiplicative_report as r

ROOT = Path(__file__).resolve().parents[3]
COUNTS = {}


def report_for(count=64, scheme='valuation', text='0.50', bits=64, max_bits=192,
               rings=8, sectors=32, readout=1000000, overrides=None):
    pair, source = m.parse_cell_scale_text(text)
    f = m.build_field(m.machine_config(count, scheme, overrides), cell_scale=pair,
                      cell_bits=bits, cell_max_bits=max_bits, include_display=False)
    f['cell_scale_source'] = source
    report = {
        'schema': m.MACHINE_REPORT_SCHEMA, 'lab_version': m.LAB_VERSION,
        'config': f['config'], 'statistics': m.statistics(f, rings, sectors, readout_scale=readout),
        'all_pairs': m.all_pair_audit(f), 'cell_engine': f['cell_engine'],
        'cell_scale_source': source, 'cell_membership_exact': m.cell_membership_summary(f),
        'browser_startup': None, 'html_observer_boundary': 'NOT_GENERATED_MACHINE_ONLY',
        'display_role': m.NO_DISPLAY, 'cell_precision': f['cell_precision'],
    }
    return report, f


def no_float(obj):
    if type(obj) is float:
        raise AssertionError('float in exact import')
    for v in (obj.values() if type(obj) is dict else obj if type(obj) is list else ()):
        no_float(v)


def cli(args):
    out, err = io.StringIO(), io.StringIO()
    with patch.object(sys, 'argv', ['report', *map(str, args)]), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            status = r.main()
        except SystemExit as exc:
            status = exc.code
    return status, out.getvalue(), err.getvalue()


class MachineReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report, cls.field = report_for()
        cls.low, cls.low_field = report_for(512, 'mixed', '1', 8, 8)

    def test_01_core_read_data_actual_dispatch(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td)/'report.json';path.write_text(json.dumps(self.report))
            with patch.object(r, 'replay_machine_report', wraps=r.replay_machine_report) as run:
                data = core.read_data(path)
            run.assert_called_once()
        self.assertEqual(data['records'], m.hex_data(self.field)['records'])
        self.assertEqual(data['metadata']['cell_precision'], {'initial_bits':64,'max_bits':192})
        self.assertEqual(core.collision_groups(data), core.collision_groups(m.hex_data(self.field)))
        self.assertEqual(core.neighborhood(data, '3'), core.neighborhood(m.hex_data(self.field), '3'))
        no_float(data)

    def test_02_original_report_replay_and_source_unmodified(self):
        before = copy.deepcopy(self.report)
        field = r.replay_machine_report(self.report)
        self.assertEqual(field, self.field);self.assertEqual(self.report, before)
        field['cell_scale_source']['numerator'] = '7'
        self.assertEqual(self.report, before)

    def test_03_unresolved_budget_replays_without_promotion(self):
        restored = r.replay_machine_report(self.low)
        self.assertEqual(restored, self.low_field)
        self.assertEqual(restored['cell_membership_exact']['status'], 'UNRESOLVED_BOUNDARY')
        self.assertTrue(restored['cell_membership_exact']['unresolved_identities'])
        for key in ('occupied_cells','collision_groups','excess_identities_if_collapsed','max_cell_load'):
            self.assertIsNone(restored['cell_membership_exact'][key])
        with self.assertRaises(ValueError):r.machine_report_to_data(self.low)

    def test_04_missing_budget_or_changed_observation_rejected(self):
        bad = copy.deepcopy(self.low);del bad['cell_precision']
        with self.assertRaises(ValueError):r.replay_machine_report(bad)
        bad = copy.deepcopy(self.low);bad['cell_precision']={'initial_bits':64,'max_bits':192}
        with self.assertRaisesRegex(ValueError,'replay mismatch'):r.replay_machine_report(bad)

    def test_05_lexical_unreduced_sources_survive(self):
        for text in ('0.50','2/2','1.00'):
            report, field = report_for(text=text)
            got = r.machine_report_to_data(report)
            self.assertEqual(got['metadata']['cell_scale_source'], report['cell_scale_source'])
            self.assertEqual(got['metadata']['cell_membership_exact']['scale'], field['cell_membership_exact']['scale'])

    def test_06_tampered_source_fields_fail_before_build(self):
        for key, value in [('numerator','1'),('denominator','2'),('syntax','INTEGER'),('unreduced',1)]:
            bad = copy.deepcopy(self.report);bad['cell_scale_source'][key]=value
            with self.subTest(key=key), patch.object(m,'build_field') as build, self.assertRaises(ValueError):
                r.replay_machine_report(bad)
            build.assert_not_called()

    def test_07_tampered_readouts_counts_and_hashes_rejected(self):
        variants=[]
        for key,value in [('population',True),('collision_groups',999),('angular_cv',0)]:
            bad=copy.deepcopy(self.report);bad['statistics'][key]=value;variants.append(bad)
        bad=copy.deepcopy(self.report);bad['statistics']['grid'][0][0]+=1;variants.append(bad)
        bad=copy.deepcopy(self.report);bad['cell_membership_exact']['phase_source_sha256']='0'*64;variants.append(bad)
        bad=copy.deepcopy(self.report);bad['cell_membership_exact']['tie_rule']='OTHER';variants.append(bad)
        bad=copy.deepcopy(self.report);bad['all_pairs']['phase_failures']=1;variants.append(bad)
        bad=copy.deepcopy(self.report);bad['statistics']['angular_cv_squared_exact']['readout']['integer']='999';variants.append(bad)
        for bad in variants:
            with self.assertRaises(ValueError):r.replay_machine_report(bad)
        COUNTS['tampered_outputs_rejected']=len(variants)

    def test_08_duplicate_keys_floats_and_nan_rejected(self):
        text=json.dumps(self.report)
        variants=[text.replace('"count": 64','"count": 64, "count": 64'),
                  text.replace('"count": 64','"count": 64.0'),
                  text.replace('"count": 64','"count": 6.4e1'),
                  text.replace('"browser_startup": null','"browser_startup": NaN'),
                  text.replace('"browser_startup": null','"browser_startup": Infinity')]
        for value in variants:
            with self.assertRaises(ValueError):r.parse_machine_report(value)
        bad=copy.deepcopy(self.report);bad['config']['count']=64.0
        with self.assertRaises(ValueError):r.replay_machine_report(bad)

    def test_09_reordered_keys_are_equal_but_boolean_is_not_integer(self):
        reordered=json.loads(json.dumps(self.report,sort_keys=True))
        self.assertEqual(r.replay_machine_report(reordered),self.field)
        bad=copy.deepcopy(self.report);bad['all_pairs']['phase_failures']=False
        with self.assertRaises(ValueError):r.replay_machine_report(bad)

    def test_10_no_approximate_work_during_read_and_projection(self):
        with contextlib.ExitStack() as stack:
            for name in ('sqrt','cos','sin','hypot','atan2','isfinite'):
                stack.enter_context(patch('math.'+name,side_effect=AssertionError(name)))
            for name in ('float','complex','_display_point','lattice_point'):
                stack.enter_context(patch.object(m,name,side_effect=AssertionError(name),create=True))
            got=r.machine_report_to_data(r.parse_machine_report(json.dumps(self.report)))
        no_float(got)

    def test_11_exact_statistics_custom_dimensions_and_scales(self):
        n=0
        for rings,sectors in ((1,1),(1,3),(3,1),(3,7)):
            for scale in (None,1,10**30):
                report,field=report_for(rings=rings,sectors=sectors,readout=scale)
                restored=r.replay_machine_report(report)
                self.assertEqual(restored,field)
                data=r.machine_report_to_data(report)
                self.assertEqual(data['metadata']['machine_report_import']['source_statistics'],report['statistics'])
                n+=1
        COUNTS['custom_observation_cases']=n

    def test_12_reader_resource_limits_fail_before_allocation(self):
        bad=copy.deepcopy(self.report);bad['statistics']['rings']=r.MAX_HISTOGRAM_CELLS+1
        with patch.object(m,'build_field') as build,self.assertRaisesRegex(ValueError,'allocation budget'):
            r.replay_machine_report(bad)
        build.assert_not_called()
        with patch.object(r,'MAX_REPORT_BYTES',10),self.assertRaises(ValueError):
            r.parse_machine_report(json.dumps(self.report))
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'large';p.write_text(json.dumps(self.report))
            with patch.object(r,'MAX_REPORT_BYTES',10),self.assertRaises(ValueError):r.load_machine_report(p)

    def test_13_display_projection_requires_explicit_scale(self):
        with self.assertRaises(TypeError):r.machine_report_startup(self.report)
        before=copy.deepcopy(self.report)
        seed=r.machine_report_startup(self.report,display_scale=2)
        self.assertEqual(seed,m.browser_startup(m.config(64,'valuation',2),cell_scale_text='0.50'))
        self.assertEqual(self.report,before)
        self.assertEqual(seed['cell_options']['scale'],'0.50')
        self.assertEqual(seed['config']['scale'],2.0)
        for invalid in (True,0,5,float('nan'),'1'):
            with self.assertRaises(ValueError):r.machine_report_startup(self.report,display_scale=invalid)

    def test_14_display_projection_preserves_low_budget_and_rejects_custom_readout(self):
        seed=r.machine_report_startup(self.low,display_scale=1)
        self.assertEqual(seed['cell_options']['initialBits'],8)
        self.assertEqual(seed['cell_options']['maxBits'],8)
        other,_=report_for(rings=3,sectors=7,readout=10**12)
        with self.assertRaisesRegex(ValueError,'fixed 8/32/1000000'):
            r.machine_report_startup(other,display_scale=1)

    def test_15_browser_or_visual_domain_is_not_source_rejection(self):
        report,_=report_for(count=16,text='5')
        r.replay_machine_report(report)
        with self.assertRaisesRegex(ValueError,'browser exact scale'):r.machine_report_startup(report,display_scale=1)
        huge,_=report_for(count=16,text='10000000')
        r.replay_machine_report(huge)
        with self.assertRaisesRegex(ValueError,'exact browser range'):r.machine_report_to_data(huge)

    def test_16_visual_data_and_csv_roundtrip_detach_all_sources(self):
        before=copy.deepcopy(self.report);data=r.machine_report_to_data(self.report)
        with tempfile.TemporaryDirectory() as td:
            for ext in ('json','csv'):
                path=Path(td)/('cells.'+ext);core.write_data(data,path)
                self.assertEqual(core.read_data(path),data)
        data['metadata']['machine_report_import']['source_statistics']['grid'][0][0]=999
        data['records'][0]['coord'][0]=5
        self.assertEqual(self.report,before)

    def test_17_legacy_data_loaders_and_unchanged_core_functions(self):
        p=ROOT/'evidence/migration13/frozen_m12_core.py'
        spec=importlib.util.spec_from_file_location('frozen_m12_core',p);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
        def defs(source):
            return {n.name:ast.dump(n,include_attributes=False) for n in ast.parse(source).body if isinstance(n,ast.FunctionDef)}
        previous,current=defs(p.read_text()),defs(Path(core.__file__).read_text())
        self.assertEqual(set(previous),set(current))
        self.assertEqual({k for k in previous if previous[k]!=current[k]},{'read_data'})
        with tempfile.TemporaryDirectory() as td:
            for d in (core.demo_hex(64),core.demo_x6()):
                for ext in ('json','csv'):
                    path=Path(td)/('old.'+ext);core.write_data(d,path)
                    self.assertEqual(core.read_data(path),old.read_data(path))

    def test_18_cli_actual_machine_replay_exports_and_budget(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);source=root/'in.json';source.write_text(json.dumps(self.report))
            verified,hexfile,seedfile=(root/name for name in ('checked.json','cells.csv','seed.json'))
            status,out,err=cli([source,'--verified-report',verified,'--hex-data',hexfile,'--startup',seedfile,'--display-scale','2'])
            self.assertEqual(status,0,err);self.assertEqual(json.loads(out)['status'],'REPLAY_MATCHED')
            self.assertEqual(json.loads(verified.read_text()),self.report)
            self.assertEqual(core.read_data(hexfile)['records'],m.hex_data(self.field)['records'])
            self.assertEqual(json.loads(seedfile.read_text())['cell_options']['scale'],'0.50')

    def test_19_cli_unresolved_report_retained_hex_preflight_rejects(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);source=root/'in.json';source.write_text(json.dumps(self.low))
            saved,cells=root/'saved.json',root/'cells.json'
            status,out,err=cli([source,'--verified-report',saved]);self.assertEqual(status,0,err)
            self.assertEqual(json.loads(saved.read_text()),self.low)
            saved.unlink()
            status,out,err=cli([source,'--verified-report',saved,'--hex-data',cells]);self.assertEqual(status,2)
            self.assertFalse(saved.exists());self.assertFalse(cells.exists())

    def test_20_cli_projection_failure_writes_nothing_and_never_guesses(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);source=root/'in.json';source.write_text(json.dumps(self.report))
            saved,seed=root/'saved.json',root/'seed.json'
            for args in ([source,'--startup',seed], [source,'--display-scale','1'],
                         [source,'--verified-report',saved,'--startup',seed,'--display-scale','nan']):
                status,out,err=cli(args);self.assertEqual(status,2);self.assertFalse(saved.exists());self.assertFalse(seed.exists())

    def test_21_input_output_aliases_and_hardlinks_are_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);source=root/'source.json';source.write_text(json.dumps(self.report));old=source.read_bytes()
            alias=root/'alias.json';os.link(source,alias)
            for dest in (source,alias):
                status,out,err=cli([source,'--verified-report',dest]);self.assertEqual(status,2);self.assertEqual(source.read_bytes(),old)

    def test_22_zero_phase_and_spiral_nonclosure_remain_visible(self):
        report,_=report_for(count=128,scheme='spiral')
        f=r.replay_machine_report(report)
        self.assertIsNone(f['records'][0]['phase'])
        self.assertNotEqual(m.multiplication(f,5,7)['phase_defect'],0)
        self.assertGreater(report['all_pairs']['phase_failures'],0)

    def test_23_invalid_or_display_schema_never_laundered(self):
        for key,value in [('schema',m.EXACT_REPORT_SCHEMA),('lab_version','unknown'),
                          ('browser_startup',{}),('display_role','DISPLAY'),('cell_engine','LEGACY_FLOAT')]:
            bad=copy.deepcopy(self.report);bad[key]=value
            with self.assertRaises(ValueError):r.replay_machine_report(bad)
        bad=copy.deepcopy(self.report);bad['config']['scale']=1
        with self.assertRaises(ValueError):r.replay_machine_report(bad)

    def test_24_core_loader_rejects_duplicate_machine_input(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'bad.json';p.write_text(json.dumps(self.report).replace('"count": 64','"count": 64,"count": 64'))
            with self.assertRaisesRegex(ValueError,'duplicate'):core.read_data(p)

    def test_25_real_module_subprocess_entrypoint(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'source.json';p.write_text(json.dumps(self.report))
            env=dict(os.environ,PYTHONPATH=str(ROOT/'src')+os.pathsep+str(ROOT/'tools/nollm_visual_toolkit'))
            proc=subprocess.run([sys.executable,'-m','nollm_visual_toolkit.multiplicative_report',str(p)],env=env,capture_output=True,text=True,timeout=30)
            self.assertEqual(proc.returncode,0,proc.stderr)
            self.assertEqual(json.loads(proc.stdout)['cell_status'],'CERTIFIED_ALL')


if __name__=='__main__':unittest.main(verbosity=2)
