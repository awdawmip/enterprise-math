"""M10 actual CLI/render -> exact browser startup; no fake render outputs."""
from __future__ import annotations
import contextlib,copy,io,json,re,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from nollm_visual_toolkit import multiplicative as m
from test_multiplicative_browser import node

def seed_of(path):
    return json.loads(re.search(r'<script id="lab-seed" type="application/json">(.*?)</script>',Path(path).read_text(),re.S).group(1))

def cli(*args):
    out,err=io.StringIO(),io.StringIO()
    with patch.object(sys,'argv',['multiplicative',*map(str,args)]),contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
        try: code=m.main()
        except SystemExit as e: code=e.code
    return code,out.getvalue(),err.getvalue()

class StartupMigrationTests(unittest.TestCase):
    def test_lexical_options_and_display_scale_are_separate(self):
        for text in ('0.50','2/2','1/4','4.0','9007199254740993/9007199254740992'):
            seed=m.browser_startup(m.config(64,scale=2),cell_scale_text=text,cell_bits=32,cell_max_bits=128)
            self.assertEqual(seed,{'schema':m.STARTUP_SCHEMA,'config':m.config(64,scale=2),'cell_options':{'engine':'certified','scale':text,'initialBits':32,'maxBits':128}})
    def test_legacy_seed_shape_is_unchanged(self):
        self.assertEqual(m.browser_startup(m.config(32)),{'config':m.config(32)})
    def test_invalid_text_never_enters_browser_seed(self):
        for text in (0.5,True,'1\n',' 1','01','1e0','１','0','-1','1/0','1.','.5'):
            with self.subTest(text=text),self.assertRaises(ValueError):m.browser_startup(m.config(16),cell_scale_text=text)
    def test_integer_range_resolves_near_float_boundaries(self):
        d=10**40
        for text in ('1/4','4',f'{d+1}/{4*d}',f'{4*d-1}/{d}'):
            m.browser_startup(m.config(16),cell_scale_text=text)
        for text in (f'{d-1}/{4*d}',f'{4*d+1}/{d}','1/5','5'):
            with self.subTest(text=text),self.assertRaises(ValueError):m.browser_startup(m.config(16),cell_scale_text=text)
    def test_precision_budget_types_are_not_coerced(self):
        for initial,maximum in ((True,64),(64.0,192),(7,64),(64,513),(128,64)):
            with self.subTest(bits=(initial,maximum)),self.assertRaises(ValueError):m.browser_startup(m.config(16),cell_scale_text='1',cell_bits=initial,cell_max_bits=maximum)
        with self.assertRaises(ValueError):m.browser_startup(m.config(16),cell_bits=32)
    def test_seed_detaches_input_config(self):
        cfg=m.config(16,overrides={'3':16384});seed=m.browser_startup(cfg,cell_scale_text='1/2');cfg['overrides']['3']=1
        self.assertEqual(seed['config']['overrides'],{'3':16384})
    def test_python_seed_matches_real_browser_validation(self):
        inputs=[m.browser_startup(m.config(64,k,scale=2),cell_scale_text=t,cell_bits=32,cell_max_bits=128) for k in ('valuation','mixed','spiral','radial') for t in ('0.50','2/2','4','1/4')]
        self.assertEqual(node('return input.map(MulExact.startup);',inputs),[{'config':v['config'],'cell_options':v['cell_options'],'session':None} for v in inputs])
    def test_browser_rejects_bad_or_downgraded_seed(self):
        good=m.browser_startup(m.config(16),cell_scale_text='1/2')
        bad=[None,True,[],{},dict(good,extra=1),dict(good,schema='OLD'),dict(good,session={}),{'config':good['config'],'cell_options':good['cell_options']},dict(good,cell_options=None)]
        for change in ({'engine':'legacy-float'},{'scale':.5},{'scale':'1/5'},{'initialBits':False}):bad.append(dict(good,cell_options={**good['cell_options'],**change}))
        self.assertTrue(all(node('return input.map(s=>{try{MulExact.startup(s);return false;}catch(e){return true;}});',bad)))
    def test_saved_seed_cannot_mix_config_sources(self):
        cfg=m.config(32,overrides={'3':16384,'5':0});session={'schema':'NOLLM_MULTIPLICATIVE_SESSION_V2','config':copy.deepcopy(cfg),'cell_options':{'engine':'certified','scale':'1/2','initialBits':64,'maxBits':192},'view_state':{}}
        good={'config':cfg,'session':session}
        self.assertEqual(node('return MulExact.startup(input).session;',good),session)
        bad=copy.deepcopy(good);bad['session']['config']['overrides']['3']=1
        self.assertTrue(node('try{MulExact.startup(input);return false;}catch(e){return true;}',bad))
        good['session']['config']['overrides']={'5':0,'3':16384}
        self.assertEqual(node('return MulExact.startup(input).config;',good),cfg)
    def test_real_cli_seed_report_and_hex_agree(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);h=p/'lab.html';j=p/'report.json';x=p/'hex.json'
            code,_,err=cli('--count','64','--scale','2','--cell-scale','0.50','--out',h,'--report',j,'--hex-data',x)
            self.assertEqual(code,0,err);r=json.loads(j.read_text());seed=seed_of(h)
            self.assertEqual(seed,r['browser_startup']);self.assertEqual(seed['config']['scale'],2.0)
            self.assertEqual(r['cell_scale_source'],m.parse_cell_scale_text('0.50')[1])
            self.assertEqual(json.loads(x.read_text())['metadata']['cell_scale_source'],r['cell_scale_source'])
            got=node('const s=MulExact.startup(input);const f=await MulExact.build(s.config,s.cell_options);return MulExact.summary(f);',seed,poison_round=True)
            self.assertEqual(got,r['cell_membership_exact'])
    def test_html_only_exact_start_needs_no_backend_compute(self):
        with tempfile.TemporaryDirectory() as d,patch.object(m,'build_field',side_effect=AssertionError('HTML-only must not run Python population')):
            h=Path(d)/'exact.html';code,_,err=cli('--count','16','--cell-scale','2/2','--out',h)
            self.assertEqual(code,0,err);self.assertEqual(seed_of(h)['cell_options']['scale'],'2/2')
    def test_legacy_cli_report_is_still_v1(self):
        with tempfile.TemporaryDirectory() as d:
            h=Path(d)/'lab.html';j=Path(d)/'report.json';code,_,err=cli('--count','32','--scale','1.5','--out',h,'--report',j)
            self.assertEqual(code,0,err);cfg=m.config(32,scale=1.5);f=m.build_field(cfg)
            self.assertEqual(seed_of(h),{'config':cfg})
            self.assertEqual(json.loads(j.read_text()),{'schema':m.REPORT_SCHEMA,'lab_version':m.LAB_VERSION,'config':cfg,'statistics':m.statistics(f),'all_pairs':m.all_pair_audit(f)})
    def test_machine_only_preserves_broader_scale(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            for i,text in enumerate(('1/8','5','5/5')):
                j=p/f'{i}.json';code,_,err=cli('--count','16','--cell-scale',text,'--machine-only','--report',j)
                self.assertEqual(code,0,err);r=json.loads(j.read_text())
                self.assertEqual(r['cell_scale_source']['text'],text);self.assertIsNone(r['browser_startup']);self.assertEqual(r['html_observer_boundary'],'NOT_GENERATED_MACHINE_ONLY')
            self.assertFalse(list(p.glob('*.html')))
    def test_invalid_machine_only_flags_fail_before_outputs(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            for args in (['--machine-only','--cell-scale','1','--out',p/'x.html','--report',p/'x.json'],['--machine-only','--cell-scale','1','--preview','--report',p/'x.json'],['--machine-only','--report',p/'x.json'],['--machine-only','--cell-scale','1'],['--report',p/'x.json']):
                self.assertEqual(cli('--count','16',*args)[0],2);self.assertFalse(list(p.iterdir()))
    def test_out_of_range_never_overwrites_existing_artifacts(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);h=p/'lab.html';j=p/'report.json';h.write_text('old html');j.write_text('old report')
            code,_,err=cli('--count','16','--cell-scale','5','--out',h,'--report',j)
            self.assertEqual(code,2);self.assertIn('--machine-only',err);self.assertEqual(h.read_text(),'old html');self.assertEqual(j.read_text(),'old report')
    def test_output_alias_does_not_overwrite_page_with_report(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);h=p/'out';h.write_text('preserve');alias=p/'link';alias.symlink_to(h)
            for other in (h,alias):
                self.assertEqual(cli('--count','16','--cell-scale','1','--out',h,'--report',other)[0],2);self.assertEqual(h.read_text(),'preserve')
    def test_unresolved_startup_matches_report_hex_preflight(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);h=p/'lab.html';j=p/'report.json';x=p/'hex.json'
            args=['--count','512','--scheme','mixed','--cell-scale','1','--cell-bits','8','--cell-max-bits','8','--out',h,'--report',j]
            code,_,err=cli(*args);self.assertEqual(code,0,err)
            r=json.loads(j.read_text());self.assertEqual(r['cell_membership_exact']['status'],'UNRESOLVED_BOUNDARY')
            got=node('const s=MulExact.startup(input);return MulExact.summary(await MulExact.build(s.config,s.cell_options));',seed_of(h))
            self.assertEqual(got,r['cell_membership_exact']);before=(h.read_bytes(),j.read_bytes())
            self.assertEqual(cli(*args,'--hex-data',x)[0],2);self.assertFalse(x.exists());self.assertEqual((h.read_bytes(),j.read_bytes()),before)
    def test_exact_preview_remains_explicit_unpassed_gate(self):
        with tempfile.TemporaryDirectory() as d:
            h=Path(d)/'lab.html';code,_,err=cli('--count','16','--cell-scale','1','--out',h,'--preview')
            self.assertEqual(code,2);self.assertIn('native-browser acceptance',err);self.assertFalse(h.exists())
    def test_invalid_render_creates_no_parent_directory(self):
        with tempfile.TemporaryDirectory() as d:
            h=Path(d)/'new'/'lab.html'
            with self.assertRaises(ValueError):m.render(h,m.config(16),cell_scale_text='1/5')
            self.assertFalse(h.parent.exists())
    def test_seed_does_not_claim_browser_execution(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);h=p/'lab.html';j=p/'report.json';code,_,err=cli('--count','16','--cell-scale','1','--out',h,'--report',j)
            self.assertEqual(code,0,err);self.assertEqual(json.loads(j.read_text())['html_observer_boundary'],'GENERATED_WITH_CERTIFIED_STARTUP_NOT_BROWSER_EXECUTION_RECEIPT')

if __name__=='__main__':unittest.main(verbosity=2)
