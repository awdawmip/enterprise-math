"""M18 real machine CLI tests; legacy render stubs test routing, not browsers."""
from __future__ import annotations
import ast
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from nollm_visual_toolkit import phase32_lab as m, core

ROOT=Path(__file__).resolve().parents[3]
COUNTS={'invalid_cli_inputs':0,'replayed_reports':0,'legacy_object_cases':0}


def call(*args):
    stdout,stderr=io.StringIO(),io.StringIO()
    with patch.object(sys,'argv',['phase32_lab',*map(str,args)]),contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):
        try: code=m.main()
        except SystemExit as e: code=e.code
    return code,stdout.getvalue(),stderr.getvalue()


def no_floats(obj):
    if type(obj) is float:return False
    if isinstance(obj,dict):return all(no_floats(v) for v in obj.values())
    if isinstance(obj,(list,tuple)):return all(no_floats(v) for v in obj)
    return True


def frozen():
    path=ROOT/'evidence/migration18/frozen_m17_phase32_lab.py'
    spec=importlib.util.spec_from_file_location('m18_frozen_m17',path)
    mod=importlib.util.module_from_spec(spec);mod.__package__='nollm_visual_toolkit';spec.loader.exec_module(mod);return mod


class Phase32CliExactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.old=frozen()

    def test_machine_source_strict_typed_config_and_copy(self):
        cfg=m.machine_config(128,'hash',seed=12,overrides={'3':m.DEN-1},sectors=31,rings=7,a=2,b=3)
        before=copy.deepcopy(cfg);model=m.build(cfg,cell_pitch=(50,100),include_display=False)
        self.assertEqual(cfg,before);self.assertTrue(no_floats(model))
        self.assertEqual(set(cfg),{'schema','count','mode','seed','overrides','sectors','rings','a','b'})
        self.assertEqual(model['display_role'],m.NO_DISPLAY)
        model['config']['overrides']['3']=0;self.assertEqual(cfg,before)

    def test_machine_source_refuses_display_config_even_integer_fields(self):
        for key,value in [('pitch',1),('yaw',0),('zoom',1),('view','hex'),('field','phase')]:
            cfg=m.machine_config(16);cfg[key]=value
            with self.assertRaises(ValueError):m.build(cfg,cell_pitch=(1,1),include_display=False)
        with self.assertRaises(ValueError):m.build({'count':16},cell_pitch=(1,1),include_display=False)
        with self.assertRaises(ValueError):m.build(m.machine_config(16),include_display=False)
        with self.assertRaises(ValueError):m.build(m.machine_config(16),cell_pitch=(1,1),include_display=0)

    def test_invalid_machine_config_fields(self):
        for key,value in [('count',True),('count',2.0),('count',1),('seed',m.DEN),('seed',-1),
                          ('sectors',True),('sectors',5),('rings',0),('a',16),('b',False),
                          ('mode','other'),('overrides',[]),('overrides',{'04':4}),
                          ('overrides',{'4':7}),('overrides',{'17':0}),('overrides',{'3':True}),
                          ('overrides',{'3':m.DEN}),('schema',m.SCHEMA)]:
            cfg=m.machine_config(16);cfg[key]=value
            with self.subTest(key=key,value=value),self.assertRaises(ValueError):m.checked_machine_config(cfg)
        self.assertEqual(m.machine_config(2)['a'],1)
        with self.assertRaises(ValueError):m.machine_config(True)

    def test_text_integer_fraction_decimal_and_inverse_pitch(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'report.json'
            for text,pair in [('2',(2,1)),('1/2',(1,2)),('0.50',(50,100)),('2/2',(2,2)),('1.00',(100,100))]:
                code,out,err=call('--machine-only','--count',32,'--cell-pitch',text,'--report',p)
                self.assertEqual(code,0,err);r=json.loads(p.read_text())
                self.assertEqual(r['cell_pitch_source']['text'],text)
                self.assertEqual((r['cell_pitch_source']['numerator'],r['cell_pitch_source']['denominator']),tuple(map(str,pair)))
                self.assertEqual(r['cell_membership_exact']['certifier_scale'],{'numerator':str(pair[1]),'denominator':str(pair[0])})
                self.assertEqual(r['phase_modulus'],str(1<<32));self.assertTrue(no_floats(r))

    def test_invalid_pitch_text_fails_before_outputs(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'report.json'
            for value in ('','0','0.00','-1','+1',' 1','1 ','01','1/02','1/0','.5','1.','1e-2','nan','Infinity','1_000','0.'+'1'*257):
                code,out,err=call('--machine-only','--count',16,'--cell-pitch',value,'--report',p)
                self.assertEqual(code,2,(value,err));self.assertFalse(p.exists());COUNTS['invalid_cli_inputs']+=1

    def test_exact_cli_never_executes_display_helpers_or_float_conversion(self):
        def forbidden(*a,**k):raise AssertionError('display/float executed')
        with tempfile.TemporaryDirectory() as td,contextlib.ExitStack() as stack:
            p=Path(td)/'report.json';d=Path(td)/'cells.csv'
            for name in ('render','build_site','position','quantize','validate_config'):
                stack.enter_context(patch.object(m,name,forbidden))
            for name in ('float','complex'):stack.enter_context(patch.object(m,name,forbidden,create=True))
            for name in ('sqrt','sin','cos','floor','isfinite'):stack.enter_context(patch.object(m.math,name,forbidden))
            code,out,err=call('--machine-only','--count',64,'--cell-pitch','1','--report',p,'--hex-data',d)
            self.assertEqual(code,0,err);self.assertTrue(no_floats(json.loads(p.read_text())))
            self.assertEqual(len(core.read_data(d)['records']),64)

    def test_exact_flags_require_machine_mode_and_meaningful_outputs(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);report=root/'report.json';out=root/'page.html'
            bad=[['--cell-pitch','1'],['--cell-bits','64'],['--readout-scale','1000000'],
                 ['--machine-only'],['--machine-only','--cell-pitch','1'],
                 ['--machine-only','--report',report],
                 ['--machine-only','--cell-pitch','1','--report',report,'--out',out],
                 ['--machine-only','--cell-pitch','1','--report',report,'--preview'],
                 ['--machine-only','--cell-pitch','1','--report',report,'--site']]
            with patch.object(m,'render',side_effect=AssertionError('render must not execute')):
                for args in bad:
                    code,_,err=call(*args);self.assertEqual(code,2,err);COUNTS['invalid_cli_inputs']+=1
                    self.assertFalse(report.exists());self.assertFalse(out.exists())

    def test_bad_precision_is_rejected_before_build(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'r.json'
            for initial,maximum in [(7,192),(64,513),(128,64),(0,8)]:
                code,_,err=call('--machine-only','--count',16,'--cell-pitch','1','--cell-bits',initial,'--cell-max-bits',maximum,'--report',p)
                self.assertEqual(code,2,err);self.assertFalse(p.exists())
            for value in (True,64.0):
                with self.assertRaises(ValueError):m.build(m.machine_config(16),cell_pitch=(1,1),cell_bits=value,include_display=False)

    def test_low_budget_is_persisted_and_replay_matches(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'report.json'
            code,out,err=call('--machine-only','--count',512,'--mode','hash','--cell-pitch','1','--cell-bits',8,'--cell-max-bits',8,'--report',p)
            self.assertEqual(code,0,err);r=json.loads(p.read_text())
            self.assertEqual(r['cell_precision'],{'initial_bits':8,'max_bits':8})
            self.assertEqual(r['cell_membership_exact']['status'],'UNRESOLVED_BOUNDARY')
            self.assertTrue(r['cell_membership_exact']['unresolved_identities'])
            self.assertIsNone(r['metrics']['occupied_cells'])
            model=m.build(r['config'],cell_pitch=(1,1),cell_bits=8,cell_max_bits=8,include_display=False)
            model['cell_pitch_source']=r['cell_pitch_source']
            self.assertEqual(m.machine_report(model),r);COUNTS['replayed_reports']+=1

    def test_unresolved_hex_refuses_all_requested_writes(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);p=root/'r.json';d=root/'d.csv'
            code,_,err=call('--machine-only','--count',512,'--mode','hash','--cell-pitch','1','--cell-bits',8,'--cell-max-bits',8,'--report',p,'--hex-data',d)
            self.assertEqual(code,2,err);self.assertIn('unresolved',err)
            self.assertFalse(p.exists());self.assertFalse(d.exists())

    def test_source_domain_broader_than_visual_carrier(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);p=root/'r.json';d=root/'d.json'
            args=['--machine-only','--count',16,'--cell-pitch','0.0000001','--report',p]
            code,_,err=call(*args);self.assertEqual(code,0,err)
            r=json.loads(p.read_text());self.assertEqual(r['cell_pitch_source']['denominator'],'10000000')
            p.unlink();code,_,err=call(*args,'--hex-data',d)
            self.assertEqual(code,2,err);self.assertIn('exact browser range',err)
            self.assertFalse(p.exists());self.assertFalse(d.exists())

    def test_machine_config_preserves_seed_overrides_and_readout_observation(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);cfg=root/'cfg.json';p=root/'r.json'
            config=m.machine_config(128,'hash',seed=123,overrides={'3':123456789},sectors=31,rings=7,a=2,b=2)
            cfg.write_text(json.dumps(config))
            code,_,err=call('--machine-only','--config',cfg,'--cell-pitch','2/2','--readout-scale',10**12+7,'--report',p)
            self.assertEqual(code,0,err);r=json.loads(p.read_text());self.assertEqual(r['config'],config)
            model=m.build(config,cell_pitch=(2,2),include_display=False);model['cell_pitch_source']=r['cell_pitch_source']
            self.assertEqual(r,m.machine_report(model,readout_scale=10**12+7));COUNTS['replayed_reports']+=1
            self.assertEqual(r['metrics']['angular_cv_squared_exact']['readout']['scale'],str(10**12+7))

    def test_null_readout_and_zero_product(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);cfg=root/'c.json';p=root/'r.json'
            cfg.write_text(json.dumps(m.machine_config(16,a=0,b=7)))
            code,_,err=call('--machine-only','--config',cfg,'--cell-pitch','1','--readout-scale','none','--report',p)
            self.assertEqual(code,0,err);r=json.loads(p.read_text())
            self.assertIsNone(r['metrics']['angular_cv_squared_exact']['readout'])
            self.assertIsNone(r['multiplication']['phase_defect_uint32'])
            self.assertIsNone(r['multiplication']['continuous_relative_error'])
            self.assertIn('absorbing',r['multiplication']['zero_rule'])

    def test_spiral_counterexample_is_not_erased(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);cfg=root/'c.json';p=root/'r.json'
            cfg.write_text(json.dumps(m.machine_config(16,'spiral',a=2,b=2)))
            code,_,err=call('--machine-only','--config',cfg,'--cell-pitch','1','--report',p)
            self.assertEqual(code,0,err);r=json.loads(p.read_text())
            self.assertEqual(r['multiplication']['phase_defect_uint32'],m.GOLDEN)

    def test_true_tie_policy_full_certificate_not_changed(self):
        config=m.machine_config(16,overrides={'2':m.DEN//8})
        model=m.build(config,cell_pitch=(2,1),include_display=False)
        cert=model['cell_membership_exact']['certificates'][4]
        self.assertEqual(cert['cell'],['-1','1']);self.assertEqual(cert['base_certificate']['cell'],['0','1'])
        self.assertEqual(cert['status'],'CERTIFIED_TIE')

    def test_config_duplicate_float_boolean_and_legacy_schema_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            cfg=Path(td)/'c.json';p=Path(td)/'r.json';good=json.dumps(m.machine_config(16))
            texts=[good.replace('"count": 16','"count": 16,"count":16'),
                   good.replace('"count": 16','"count": 16.0'),good.replace('"count": 16','"count": true'),
                   good.replace('"seed": 0','"seed": NaN'),json.dumps(m.DEFAULT),
                   json.dumps({'schema':m.SCHEMA,'version':m.VERSION,'config':dict(count=16)}),
                   '['*1200+'0'+']'*1200,' ' * 65537]
            for text in texts:
                cfg.write_text(text);code,_,err=call('--machine-only','--config',cfg,'--cell-pitch','1','--report',p)
                self.assertEqual(code,2,err);self.assertFalse(p.exists());COUNTS['invalid_cli_inputs']+=1

    def test_explicit_config_not_silently_overridden(self):
        with tempfile.TemporaryDirectory() as td:
            cfg=Path(td)/'c.json';p=Path(td)/'r.json';cfg.write_text(json.dumps(m.machine_config(16)))
            for extra in [('--count',16),('--mode','golden')]:
                code,_,err=call('--machine-only','--config',cfg,'--cell-pitch','1','--report',p,*extra)
                self.assertEqual(code,2,err);self.assertFalse(p.exists())

    def test_output_aliases_and_hardlinks_preserve_input(self):
        with tempfile.TemporaryDirectory() as td:
            cfg=Path(td)/'c.json';alias=Path(td)/'a.json';cfg.write_text(json.dumps(m.machine_config(16)));before=cfg.read_bytes()
            os.link(cfg,alias)
            for dest in (cfg,alias):
                code,_,err=call('--machine-only','--config',cfg,'--cell-pitch','1','--report',dest)
                self.assertEqual(code,2,err);self.assertEqual(cfg.read_bytes(),before)
            p=Path(td)/'r.json';code,_,err=call('--machine-only','--count',16,'--cell-pitch','1','--report',p,'--hex-data',p)
            self.assertEqual(code,2,err);self.assertFalse(p.exists())

    def test_json_csv_exports_are_lossless_and_detached(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);reports=[];data=[]
            for ext in ('json','csv'):
                p=root/(ext+'report.json');d=root/('data.'+ext)
                code,_,err=call('--machine-only','--count',128,'--cell-pitch','0.50','--report',p,'--hex-data',d)
                self.assertEqual(code,0,err);reports.append(json.loads(p.read_text()));data.append(core.read_data(d))
            self.assertEqual(data[0],data[1]);self.assertEqual(reports[0],reports[1])
            self.assertEqual([r['id'] for r in data[0]['records']],[str(i) for i in range(128)])
            self.assertTrue(no_floats(data[0]));self.assertIsNone(data[0]['records'][0]['fields']['phase_numerator'])
            self.assertFalse(any(k.startswith('ideal') for r in data[0]['records'] for k in r['fields']))

    def test_report_does_not_alias_model(self):
        model=m.build(m.machine_config(32),cell_pitch=(1,1),include_display=False)
        before=copy.deepcopy(model);r=m.machine_report(model)
        r['config']['overrides']['3']=12;r['cell_precision']['initial_bits']=8
        r['cell_membership_exact']['unresolved_identities'].append('1')
        self.assertEqual(model,before)
        with self.assertRaises(ValueError):m.machine_report(m.build(dict(count=16),cell_pitch=(1,1)))

    def test_old_full_objects_and_exact_observations_unchanged(self):
        for mode in ('golden','hash','spiral'):
            for count in (16,128):
                cfg=dict(count=count,mode=mode,pitch=2)
                for pitch in (None,(1,2),(3,2)):
                    before=self.old.build(cfg,cell_pitch=pitch);now=m.build(cfg,cell_pitch=pitch)
                    self.assertEqual(json.dumps(before),json.dumps(now))
                    self.assertEqual(json.dumps(self.old.metrics(before)),json.dumps(m.metrics(now)))
                    self.assertEqual(self.old.hex_data(before),m.hex_data(now));COUNTS['legacy_object_cases']+=1

    def test_only_build_and_main_existing_asts_change(self):
        def functions(text):
            return {n.name:ast.dump(n,include_attributes=False) for n in ast.parse(text).body if isinstance(n,ast.FunctionDef)}
        old=functions(Path(self.old.__file__).read_text());new=functions(Path(m.__file__).read_text())
        self.assertEqual({k for k in old if new[k]!=old[k]},{'build','main'})

    def test_real_subprocess_cli_entrypoint(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'r.json'
            env=dict(os.environ,PYTHONPATH=str(ROOT/'src')+os.pathsep+str(ROOT/'tools/nollm_visual_toolkit'))
            result=subprocess.run([sys.executable,'-m','nollm_visual_toolkit.phase32_lab','--machine-only','--count','32','--cell-pitch','0.50','--report',str(p)],
                                  cwd=td,env=env,capture_output=True,text=True,timeout=30)
            self.assertEqual(result.returncode,0,result.stderr);self.assertTrue(p.exists())
            self.assertEqual(json.loads(result.stdout)['status'],'CERTIFIED_ALL')
            self.assertFalse((Path(td)/'multiplicative-field.html').exists())

    def test_legacy_cli_payload_retained_with_explicit_render_stub(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);p=root/'r.json';d=root/'d.json';out=root/'page.html'
            with patch.object(m,'render',return_value=out):
                code,_,err=call('--count',32,'--mode','hash','--report',p,'--hex-data',d,'--out',out)
            self.assertEqual(code,0,err);old=self.old.build(dict(count=32,mode='hash',a=5,b=7))
            expected=dict(schema=m.SCHEMA,config=old['config'],metrics=self.old.metrics(old),multiplication=self.old.multiplication(old,5,7))
            self.assertEqual(json.loads(p.read_text()),expected);self.assertEqual(json.loads(d.read_text()),self.old.hex_data(old))

    def test_invalid_readout_scale_does_not_write(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'r.json'
            for scale in ('0','01','-1','1.0','1e6','NONE','',str(10**256)):
                code,_,err=call('--machine-only','--count',16,'--cell-pitch','1','--readout-scale',scale,'--report',p)
                self.assertEqual(code,2,err);self.assertFalse(p.exists());COUNTS['invalid_cli_inputs']+=1

    def test_missing_brc_explicit_no_fallback(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'r.json'
            with patch.object(m,'_lexicographic_cells',side_effect=RuntimeError('Certified cells require Enterprise Math BRC. No approximate fallback.')):
                code,_,err=call('--machine-only','--count',16,'--cell-pitch','1','--report',p)
            self.assertEqual(code,2,err);self.assertIn('no approximate fallback',err);self.assertFalse(p.exists())


if __name__=='__main__':unittest.main(verbosity=2)
