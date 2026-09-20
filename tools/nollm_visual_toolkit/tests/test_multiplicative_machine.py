"""M12: real machine field/CLI with optional display disabled before float work."""
from __future__ import annotations
import ast
import contextlib
import copy
import hashlib
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
from nollm_visual_toolkit import multiplicative as m
from nollm_visual_toolkit import core

ROOT = Path(__file__).resolve().parents[3]
BASELINE = ROOT/'evidence/migration12/frozen_m11_multiplicative.py'
COUNTS = {}


def baseline():
    spec = importlib.util.spec_from_file_location('nollm_visual_toolkit._m11_machine_baseline', BASELINE)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


def poison():
    stack = contextlib.ExitStack()
    for name in ('sqrt','sin','cos','hypot','atan2','isfinite'):
        stack.enter_context(patch('math.'+name, side_effect=AssertionError('display math: '+name)))
    for name in ('float','complex','_display_point','lattice_point'):
        stack.enter_context(patch.object(m,name,side_effect=AssertionError('display call: '+name),create=True))
    return stack


def no_float(value):
    if isinstance(value, float):
        raise AssertionError('unexpected float in machine state: '+repr(value))
    for child in (value.values() if isinstance(value,dict) else value if isinstance(value,(tuple,list)) else ()):
        no_float(child)


def run_cli(argv):
    with patch.object(sys,'argv',['multiplicative',*map(str,argv)]), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        return m.main()


class MachineFieldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old = baseline()
        cls.machine = m.build_field(m.machine_config(257,'mixed'),cell_scale=(1,1),include_display=False)

    def test_01_source_and_all_unmodified_mathematical_functions(self):
        raw = BASELINE.read_bytes()
        self.assertEqual(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),
                         '95dd6aad2c2597c9f25fd2a7b7aadcbe27f9b838')
        defs = lambda text:{f.name:ast.dump(f,include_attributes=False) for f in ast.parse(text).body
                           if isinstance(f,ast.FunctionDef)}
        old,new=defs(raw),defs(Path(m.__file__).read_text())
        self.assertEqual(set(new)-set(old),{'_phase_options','machine_config','checked_machine_config','_display_point'})
        self.assertEqual({k for k in old if old[k]!=new[k]}, {'config','build_field','hex_data','main'})
        self.assertTrue(set(old)<=set(new))

    def test_02_shared_integer_phase_validation(self):
        cases = 0
        for scheme in ('valuation','mixed','spiral','radial'):
            for count in (16,257):
                for overrides in (None,{'2':8192,'3':16384}):
                    exact=m.machine_config(count,scheme,overrides)
                    old=self.old.config(count,scheme,overrides=overrides)
                    self.assertEqual({k:exact[k] for k in ('count','scheme','overrides')},
                                     {k:old[k] for k in ('count','scheme','overrides')})
                    no_float(exact);cases+=1
        COUNTS['phase_config_cases']=cases

    def test_03_entire_machine_construction_readout_export_with_float_poison(self):
        with poison():
            f=m.build_field(m.machine_config(64),cell_scale=(50,100),include_display=False)
            result=[f,m.statistics(f),m.multiplication(f,5,7),m.hex_data(f),m.all_pair_audit(f)]
        for obj in result:no_float(obj)
        self.assertNotIn('scale',f['config']);self.assertEqual(f['display_role'],m.NO_DISPLAY)
        self.assertTrue(all('ideal' not in r for r in f['records']))

    def test_04_legacy_full_objects_and_json_stay_identical(self):
        for mode in ('valuation','mixed','spiral','radial'):
            cfg=m.config(129,mode,1.5);f=m.build_field(cfg);old=self.old.build_field(cfg)
            self.assertEqual(json.dumps(f),json.dumps(old))
            self.assertEqual(json.dumps(m.hex_data(f)),json.dumps(self.old.hex_data(old)))
            self.assertEqual(m.statistics(f),self.old.statistics(old))
            self.assertEqual(m.multiplication(f,5,7),self.old.multiplication(old,5,7))

    def test_05_opt_in_display_exact_field_unchanged(self):
        cfg=m.config(129,'mixed',.5)
        self.assertEqual(json.dumps(m.build_field(cfg,cell_scale=(50,100))),
                         json.dumps(self.old.build_field(cfg,cell_scale=(50,100))))

    def test_06_full_certificates_and_counts_match_displayed_reference(self):
        cases=0
        for scheme in ('valuation','mixed','spiral','radial'):
            for scale in ((1,2),(1,1),(3,2)):
                old=self.old.build_field(self.old.config(128,scheme),cell_scale=scale)
                with poison():new=m.build_field(m.machine_config(128,scheme),cell_scale=scale,include_display=False)
                self.assertEqual(new['cell_membership_exact'],old['cell_membership_exact'])
                self.assertEqual(new['records'],[{k:v for k,v in r.items() if k!='ideal'} for r in old['records']])
                self.assertEqual(m.statistics(new),self.old.statistics(old));cases+=1
        COUNTS['full_certificate_cases_128']=cases

    def test_07_unreduced_source_and_lexicographic_tie_retained(self):
        with poison():
            f=m.build_field(m.machine_config(16,overrides={'2':8192,'3':16384}),cell_scale=(50,100),include_display=False)
        self.assertEqual(f['cell_scale_source'],{'numerator':'50','denominator':'100','unreduced':True})
        self.assertEqual(f['records'][3]['coord'],[-1,1]);self.assertEqual(f['records'][4]['coord'],[-1,1])
        self.assertEqual(f['cell_membership_exact']['certificates'][4]['base_certificate']['cell'],['0','1'])

    def test_08_no_silent_loss_of_legacy_display_configuration(self):
        legacy=m.config(16,scale=1.5)
        with poison(),self.assertRaisesRegex(ValueError,'machine_config'):
            m.build_field(legacy,cell_scale=(1,1),include_display=False)
        with self.assertRaises(ValueError):m.build_field(m.machine_config(16),cell_scale=(1,1))

    def test_09_boolean_flag_and_required_scale(self):
        for flag in (0,1,'false',None,[],{}):
            with self.subTest(flag=flag),self.assertRaises(ValueError):
                m.build_field(m.machine_config(16),cell_scale=(1,1),include_display=flag)
        with self.assertRaises(ValueError):m.build_field(m.machine_config(16),include_display=False)

    def test_10_checked_machine_configuration_is_strict_and_copied(self):
        c=m.machine_config(16,overrides={'3':123});v=m.checked_machine_config(c)
        c['overrides']['3']=8;self.assertEqual(v['overrides']['3'],123)
        for change in ({'scale':1},{'scale':1.0},{'schema':'wrong'},{'extra':None}):
            bad=dict(v,**change)
            with self.assertRaises(ValueError):m.checked_machine_config(bad)
        for key in ('schema','count','scheme','overrides'):
            bad=copy.deepcopy(v);bad.pop(key)
            with self.assertRaises(ValueError):m.checked_machine_config(bad)

    def test_11_invalid_machine_phase_inputs_rejected(self):
        for count in (0,15,65537,True,16.0,'16'):
            with self.assertRaises(ValueError):m.machine_config(count)
        for overrides in ({'4':2},{'03':2},{'3':.5},{'3':True},{'3':65536},[],{'٣':7}):
            with self.assertRaises(ValueError):m.machine_config(16,overrides=overrides)
        with self.assertRaises(ValueError):m.machine_config(16,scheme='unknown')

    def test_12_low_budget_retains_partial_state_not_guessed_pixels(self):
        with poison():f=m.build_field(m.machine_config(512,'mixed'),cell_scale=(1,1),include_display=False,cell_bits=8,cell_max_bits=8)
        ids=f['cell_membership_exact']['unresolved_identities'];self.assertTrue(ids)
        self.assertTrue(all(f['records'][int(i)]['coord'] is None for i in ids))
        self.assertEqual(len(f['records']),512);s=m.statistics(f)
        for k in ('occupied_hex_centers','collision_groups','extra_identities_at_shared_centers','largest_fiber'):
            self.assertIsNone(s[k])
        self.assertEqual(sum(map(sum,s['grid'])),511)
        with self.assertRaises(ValueError):m.hex_data(f)
        no_float(f)

    def test_13_large_exact_scale_is_not_restricted_to_visual_carrier(self):
        with poison():f=m.build_field(m.machine_config(16,'radial'),cell_scale=(10**40,7),include_display=False)
        self.assertEqual(f['cell_membership_exact']['status'],'CERTIFIED_ALL')
        self.assertGreater(abs(f['records'][1]['coord'][0]),core.MAX_COORD)
        no_float(m.statistics(f))
        with self.assertRaisesRegex(ValueError,'coordinate'):m.hex_data(f)

    def test_14_machine_json_and_csv_roundtrip(self):
        with poison():d=m.hex_data(self.machine)
        with tempfile.TemporaryDirectory() as td:
            for suffix in ('json','csv'):
                path=Path(td)/('data.'+suffix)
                with poison():core.write_data(d,path);read=core.read_data(path)
                self.assertEqual(d,read);no_float(read)

    def test_15_public_hex_export_does_not_alias_provenance(self):
        old=copy.deepcopy(self.machine);d=m.hex_data(self.machine)
        d['records'][0]['coord'][0]=999
        d['metadata']['config']['overrides']['3']=6
        d['metadata']['cell_membership_exact']['scale']['numerator']='99'
        self.assertEqual(self.machine,old)

    def test_16_machine_only_cli_subprocess_produces_no_float_report(self):
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/'report.json'
            env=dict(os.environ,PYTHONPATH=str(ROOT/'src')+os.pathsep+str(ROOT/'tools/nollm_visual_toolkit'))
            subprocess.run([sys.executable,'-m','nollm_visual_toolkit.multiplicative',
                '--count','64','--machine-only','--cell-scale','0.50','--report',str(out)],
                check=True,capture_output=True,text=True,env=env,timeout=30)
            r=json.loads(out.read_text());no_float(r)
            self.assertEqual(r['schema'],m.MACHINE_REPORT_SCHEMA)
            self.assertEqual(r['config']['schema'],m.MACHINE_CONFIG_SCHEMA)
            self.assertNotIn('scale',r['config']);self.assertEqual(r['display_role'],m.NO_DISPLAY)
            self.assertEqual(r['cell_scale_source']['text'],'0.50')
            self.assertEqual(r['cell_membership_exact']['scale'],{'numerator':'50','denominator':'100'})
            self.assertIsNone(r['browser_startup'])

    def test_17_actual_cli_report_and_hex_export_under_poison(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);out=root/'report.json';data=root/'cells.json'
            with poison():self.assertEqual(run_cli(['--count',64,'--machine-only','--cell-scale','2/2','--report',out,'--hex-data',data]),0)
            r,d=json.loads(out.read_text()),core.read_data(data)
            no_float(r);no_float(d)
            self.assertEqual(r['cell_scale_source']['text'],'2/2')
            self.assertTrue(all('ideal_x' not in x['fields'] and 'ideal_y' not in x['fields'] for x in d['records']))
            self.assertEqual(r['cell_membership_exact'],d['metadata']['cell_membership_exact'])
            self.assertEqual(r['cell_precision'],d['metadata']['cell_precision'])
            self.assertEqual({p.name for p in root.iterdir()},{'report.json','cells.json'})

    def test_18_explicit_display_scale_never_silently_ignored_by_machine_cli(self):
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'r.json'
            for scale in ('1','1.5','nan','not-a-number'):
                with poison(),self.assertRaises(SystemExit) as err:
                    run_cli(['--count',16,'--machine-only','--cell-scale','1','--scale',scale,'--report',path])
                self.assertEqual(err.exception.code,2);self.assertFalse(path.exists())

    def test_19_unresolved_and_carrier_overflow_fail_before_replacing_outputs(self):
        with tempfile.TemporaryDirectory() as td:
            report=Path(td)/'report.json';data=Path(td)/'data.json'
            for args in (['--count',512,'--scheme','mixed','--cell-scale','1','--cell-bits',8,'--cell-max-bits',8],
                         ['--count',16,'--cell-scale',str(10**40)]):
                report.write_text('previous report');data.write_text('previous data')
                with poison(),self.assertRaises(SystemExit):
                    run_cli(['--machine-only','--report',report,'--hex-data',data,*args])
                self.assertEqual(report.read_text(),'previous report');self.assertEqual(data.read_text(),'previous data')

    def test_20_partial_machine_report_still_exportable(self):
        with tempfile.TemporaryDirectory() as td:
            report=Path(td)/'r.json'
            with poison():run_cli(['--machine-only','--report',report,'--count',512,'--scheme','mixed',
                                    '--cell-scale','1','--cell-bits',8,'--cell-max-bits',8])
            r=json.loads(report.read_text());no_float(r)
            self.assertEqual(r['cell_membership_exact']['status'],'UNRESOLVED_BOUNDARY')

    def test_21_report_source_rebuild_is_lossless_for_exact_observer(self):
        with tempfile.TemporaryDirectory() as td:
            report=Path(td)/'r.json'
            run_cli(['--machine-only','--report',report,'--count',64,'--cell-scale','0.50'])
            r=json.loads(report.read_text())
            pair,source=m.parse_cell_scale_text(r['cell_scale_source']['text'])
            with poison():f=m.build_field(m.checked_machine_config(r['config']),cell_scale=pair,include_display=False,
                                           cell_bits=r['cell_precision']['initial_bits'],
                                           cell_max_bits=r['cell_precision']['max_bits'])
            self.assertEqual(source,r['cell_scale_source'])
            self.assertEqual(m.cell_membership_summary(f),r['cell_membership_exact'])
            self.assertEqual(m.statistics(f),r['statistics'])

    def test_27_report_retains_budget_and_replays_unresolved_outcome(self):
        with tempfile.TemporaryDirectory() as td:
            report=Path(td)/'r.json'
            run_cli(['--machine-only','--report',report,'--count',512,'--scheme','mixed',
                     '--cell-scale','1','--cell-bits',8,'--cell-max-bits',8])
            r=json.loads(report.read_text())
            self.assertEqual(r['cell_precision'],{'initial_bits':8,'max_bits':8})
            scale,source=m.parse_cell_scale_text(r['cell_scale_source']['text'])
            with poison():
                f=m.build_field(m.checked_machine_config(r['config']),cell_scale=scale,include_display=False,
                                cell_bits=r['cell_precision']['initial_bits'],cell_max_bits=r['cell_precision']['max_bits'])
            self.assertEqual(m.cell_membership_summary(f),r['cell_membership_exact'])
            self.assertEqual(r['cell_membership_exact']['status'],'UNRESOLVED_BOUNDARY')

    def test_22_zero_and_spiral_nonclosure_survive_no_display(self):
        with poison():
            f=m.build_field(m.machine_config(64,'spiral'),cell_scale=(1,1),include_display=False)
            a=m.multiplication(f,0,7);b=m.multiplication(f,5,7)
        self.assertIsNone(a['phase_defect']);self.assertIsNone(a['ideal_relative_error'])
        self.assertNotEqual(b['phase_defect'],0)
        self.assertEqual(b['omega_defect'],0)

    def test_23_normal_cli_keeps_legacy_and_exact_display_reports(self):
        # Only render is stubbed: this checks machine/display routing and V1/V2,
        # not the absent full-M10 HTML template or browser execution.
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            for exact in (False,True):
                out=root/'lab.html';report=root/'r.json'
                def render(path,*args,**kwargs):Path(path).write_text('DISPLAY_TEST_STUB');return path
                args=['--count',32,'--out',out,'--scale','1.5','--report',report]
                if exact:args+=['--cell-scale','1/2']
                with patch.object(m,'render',side_effect=render):run_cli(args)
                r=json.loads(report.read_text())
                self.assertEqual(r['schema'],m.EXACT_REPORT_SCHEMA if exact else m.REPORT_SCHEMA)
                self.assertEqual(r['config'],self.old.config(32,scale=1.5))
                self.assertNotIn('display_role',r)
                if exact:self.assertEqual(r['browser_startup'],self.old.browser_startup(r['config'],cell_scale_text='1/2'))

    def test_24_legacy_error_priority_and_messages_unchanged(self):
        cases=[{'count':True},{'scheme':'bad'},{'scale':False},{'scale':float('nan')},
               {'scale':0,'overrides':{'4':2}},{'overrides':{'4':2}},{'count':15,'scale':0}]
        for kwargs in cases:
            with self.assertRaises(ValueError) as a:self.old.config(**kwargs)
            with self.assertRaises(ValueError) as b:m.config(**kwargs)
            self.assertEqual(str(a.exception),str(b.exception))

    def test_25_machine_export_rejects_inconsistent_mode_marker(self):
        f=copy.deepcopy(self.machine);f.pop('cell_engine')
        with self.assertRaises(ValueError):m.hex_data(f)

    def test_26_unmodified_brc_source_and_existing_integer_root(self):
        raw=(ROOT/'src/enterprise_math/exact_arithmetic.py').read_bytes()
        self.assertEqual(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),
                         '35ea95b0916494b83a92386e3e313928362dd79e')


if __name__=='__main__':unittest.main(verbosity=2)
