"""M09 actual rendered-engine tests. Node uses native Web Crypto, not a mock."""
from __future__ import annotations
import contextlib
import hashlib
import io
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from nollm_visual_toolkit import multiplicative as m
from nollm_visual_toolkit.multiplicative_browser import prepare_template
from nollm_visual_toolkit.angular_dispersion import AngularDispersion

ROOT=Path(__file__).resolve().parents[3]
PKG=Path(m.__file__).parent
TEMPLATE=PKG/'multiplicative_lab.html'

def engine_script() -> str:
    text=prepare_template(TEMPLATE.read_text())
    return '\n'.join(re.search(r'<script id="'+id+r'">(.*?)</script>',text,re.S).group(1)
                     for id in ['lab-engine','mul-exact-engine'])

def node(body, payload=None, *, poison_round=False):
    script=engine_script()
    if poison_round:script=script.replace('function round(x,y){', "function round(x,y){throw Error('legacy quantizer executed');")
    script+='\nconst input=JSON.parse(require("fs").readFileSync(0,"utf8"));\n'
    script+='(async()=>{'+body+'})().then(x=>process.stdout.write(JSON.stringify(x))).catch(e=>{console.error(e.stack);process.exitCode=1;});'
    with tempfile.TemporaryDirectory() as d:
        f=Path(d)/'test.cjs';f.write_text(script)
        r=subprocess.run(['node',str(f)],input=json.dumps(payload),text=True,capture_output=True,timeout=90)
        if r.returncode:raise AssertionError(r.stderr)
        return json.loads(r.stdout)

def options(scale='1',initial=64,maximum=192):
    return dict(engine='certified',scale=scale,initialBits=initial,maxBits=maximum)

class BrowserMigrationTests(unittest.TestCase):
    def test_original_template_exact_blob_and_m07_python_reuse(self):
        b=TEMPLATE.read_bytes()
        self.assertEqual(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'6619c5da7ad03f38766bfc383d60b5505cb863e0')
        frozen=(ROOT/'evidence/migration09/frozen_m07_multiplicative.py').read_text()
        now=Path(m.__file__).read_text().replace('    from .multiplicative_browser import prepare_template\n    template = prepare_template(template)\n','')
        self.assertEqual(now,frozen)
    def test_real_render_is_deterministic_and_embeds_existing_engines(self):
        with tempfile.TemporaryDirectory() as d:
            a=m.render(Path(d)/'a.html',m.config(16));b=m.render(Path(d)/'b.html',m.config(16))
            self.assertEqual(a.read_bytes(),b.read_bytes())
            for s in ['populationLexicographic','id="cellScale"','id="cellEngine"','MulExact.build']:
                self.assertIn(s,a.read_text())
            self.assertNotIn('__LAB_SEED__',a.read_text())
            self.assertNotRegex(a.read_text(),r'<script[^>]+src=')
    def test_unknown_template_not_silently_rewritten(self):
        with self.assertRaises(ValueError):prepare_template(TEMPLATE.read_text()+'\n')
    def test_scale_parser_matches_python_for_lexical_sources(self):
        texts=['0.50','2/2','2.0','1','9007199254740993/9007199254740992']
        texts += [f'{n}/{d}' for n in range(1,13) for d in range(1,13)]
        got=node('return input.map(MulExact.source);',texts)
        self.assertEqual(got,[m.parse_cell_scale_text(t)[1] for t in texts])
    def test_whitespace_newline_unicode_and_numeric_inputs_rejected(self):
        bad=['1\n','1/2\r\n','1\t',' 1','１','1e0','01','1.','.5','0','0.0','1/0','1/02',0.5,None,True,'0.'+'1'*256]
        got=node('return input.map(v=>{try{MulExact.source(v);return false;}catch(e){return true;}});',bad)
        self.assertTrue(all(got))
    def test_browser_scale_range_and_precision_guard(self):
        good=[options('1/4',8,512),options('4'),options('4.0'),options('2/2')]
        self.assertEqual(node('return input.map(MulExact.options);',good),good)
        bad=[options('1/5'),options('5'),options('1',7,64),options('1',128,64),options('1',64,513),{**options(),'extra':True}]
        self.assertTrue(all(node('return input.map(v=>{try{MulExact.options(v);return false;}catch(e){return true;}});',bad)))
    def test_all_four_schemes_complete_certificates_match_python(self):
        for scheme in ('valuation','mixed','spiral','radial'):
            cfg=m.config(256,scheme)
            out=node('const f=await MulExact.build(input.c,input.o);return {p:f.cell_membership_exact,rows:f.records.map(({ideal,...r})=>r),source:f.cell_scale_source};',{'c':cfg,'o':options('0.50')})
            py=m.build_field(cfg,cell_scale=(50,100))
            self.assertEqual(out['p'],py['cell_membership_exact'])
            self.assertEqual(out['rows'],[{k:v for k,v in r.items() if k!='ideal'} for r in py['records']])
            self.assertEqual(out['source'],m.parse_cell_scale_text('0.50')[1])
    def test_shared_radical_and_declared_tie_rule_reused(self):
        for n,overrides in [(3,{'3':16384}),(4,{'2':8192})]:
            cfg=m.config(16,overrides=overrides)
            out=node('const f=await MulExact.build(input.c,input.o);return f.cell_membership_exact.certificates[input.n];',{'c':cfg,'o':options('1/2'),'n':n})
            self.assertEqual(out,m.build_field(cfg,cell_scale=(1,2))['cell_membership_exact']['certificates'][n])
            self.assertEqual(out['cell'],['-1','1'])
    def test_old_quantizer_cannot_execute_in_exact_build(self):
        got=node('return (await MulExact.build(input, {engine:"certified",scale:"1",initialBits:64,maxBits:192})).cell_membership_exact.status;',m.config(128,'mixed'),poison_round=True)
        self.assertEqual(got,'CERTIFIED_ALL')
    def test_display_trigonometry_cannot_change_certificates(self):
        got=node('const o={engine:"certified",scale:"1/2",initialBits:64,maxBits:192};const a=await MulExact.build(input,o);Math.sin=()=>17;Math.cos=()=>19;Math.sqrt=()=>23;const b=await MulExact.build(input,o);return JSON.stringify(a.cell_membership_exact)===JSON.stringify(b.cell_membership_exact);',m.config(128))
        self.assertTrue(got)
    def test_histogram_readouts_match_brc_full_record(self):
        got=node('const f=await MulExact.build(input.c,input.o);return MulExact.stats(f);',{'c':m.config(512,'mixed'),'o':options('1')})
        grid=got['grid'];angular=[sum(row[j] for row in grid) for j in range(32)]
        self.assertEqual(got['angular_cv_squared_exact'],AngularDispersion.from_counts(angular).as_record(scale=10**6))
        self.assertEqual(got['area_sector_cv_squared_exact'],AngularDispersion.from_counts([v for row in grid for v in row]).as_record(scale=10**6))
        self.assertIsNone(got['area_sector_cv']);self.assertIsNone(got['iid_cv_scale'])
    def test_unresolved_population_no_guessed_hex_output(self):
        got=node('const f=await MulExact.build(input.c,input.o);let rejected=false;try{MulExact.hexData(f);}catch(e){rejected=true;}return {p:MulExact.summary(f),s:MulExact.stats(f),rejected};',{'c':m.config(512,'mixed'),'o':options('1',8,8)})
        self.assertEqual(got['p']['status'],'UNRESOLVED_BOUNDARY');self.assertTrue(got['rejected'])
        for key in ['occupied_hex_centers','collision_groups','extra_identities_at_shared_centers','largest_fiber']:
            self.assertIsNone(got['s'][key])
    def test_export_is_detached_from_live_provenance(self):
        got=node('const f=await MulExact.build(input, {engine:"certified",scale:"2/2",initialBits:64,maxBits:192});const d=MulExact.hexData(f);d.metadata.config.scale=3;d.metadata.cell_scale_source.text="3";d.records[0].coord[0]=100;return {scale:f.config.scale,text:f.cell_scale_source.text,cell:f.records[0].coord};',m.config(64))
        self.assertEqual(got,{'scale':1,'text':'2/2','cell':[0,0]})
    def test_input_snapshot_survives_caller_mutation(self):
        got=node('const o={engine:"certified",scale:"1/2",initialBits:64,maxBits:192};const p=MulExact.build(input,o);input.overrides["3"]=1;o.scale="3";const f=await p;return {o:f.config.overrides,s:f.cell_scale_source.text};',m.config(512,overrides={'3':16384}))
        self.assertEqual(got,{'o':{'3':16384},'s':'1/2'})
    def test_legacy_rendered_engine_payload_remains_unchanged(self):
        original=re.search(r'<script id="lab-engine">(.*?)</script>',TEMPLATE.read_text(),re.S).group(1).replace('const MulMath=', 'const OriginalMath=')
        got=node(original+'\nreturn input.every(c=>JSON.stringify(MulMath.build(c))===JSON.stringify(OriginalMath.build(c)));',[m.config(257,k,scale=1.5) for k in ['valuation','mixed','spiral','radial']])
        self.assertTrue(got)
    def test_exact_product_does_not_misreport_geometric_zero_error(self):
        got=node('const f=await MulExact.build(input,{engine:"certified",scale:"1",initialBits:64,maxBits:192});return [MulExact.multiply(f,5,7),MulExact.multiply(f,0,7)];',m.config(64))
        self.assertEqual(got[0]['phase_defect'],0);self.assertIsNone(got[0]['ideal_relative_error']);self.assertIsNone(got[0]['rounded_relative_error'])
        self.assertIsNone(got[1]['phase_defect'])
    def test_real_cli_keeps_m07_machine_scope_and_generates_actual_page(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);argv=['multiplicative','--count','64','--cell-scale','0.50','--out',str(p/'lab.html'),'--report',str(p/'report.json')]
            with patch.object(sys,'argv',argv),contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):self.assertEqual(m.main(),0)
            self.assertIn('id="cellEngine"',(p/'lab.html').read_text())
            report=json.loads((p/'report.json').read_text());self.assertEqual(report['cell_scale_source']['text'],'0.50')
            self.assertEqual(report['schema'],'NOLLM_MULTIPLICATIVE_REPORT_V2')
            self.assertIn('legacy',(report['html_observer_boundary']))

if __name__=='__main__':unittest.main(verbosity=2)
