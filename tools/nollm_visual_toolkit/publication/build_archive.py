"""Generate the complete lab archive locally; remote publication is separate."""
from __future__ import annotations
import argparse, hashlib, io, json, os, shutil, subprocess, sys, unittest, zipfile
from pathlib import Path

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p, obj):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def build(source, out, browser=True, wheel=True):
    source,out=source.resolve(),out.resolve()
    if out==source or source.is_relative_to(out) or (out.exists() and any(out.iterdir())):
        raise ValueError('Use an empty output directory that cannot replace the source')
    out.mkdir(parents=True,exist_ok=True); evidence=out/'verification';evidence.mkdir()
    sys.path.insert(0,str(source))
    from nollm_visual_toolkit import core
    from nollm_visual_toolkit import multiplication_lab as lab
    log=io.StringIO(); suite=unittest.TestLoader().discover(str(source/'tests'),pattern='test_multiplication_lab.py')
    result=unittest.TextTestRunner(stream=log,verbosity=2).run(suite)
    (evidence/'unit.log').write_text(log.getvalue(),encoding='utf-8')
    if not result.wasSuccessful() or not result.testsRun: raise RuntimeError('Tests failed/not discovered')
    data=core.demo_hex();core.write_data(data,out/'data/source-v2.json');lab.build_lab_site(out/'site')
    expected={'index.html':'65916996de2dbe388cd886a67b916876aa782567228c36fefe73ad30a311bab3',
              'multiplication.html':'f304cdebbc6c5a2f894a3d4d4bed683ad97cab3b6c39cc2af80570a7284bf552',
              'manifest.json':'968e1ba8d078c90553970a92d106a5034968f698414ec430c5e562d66ebf4ce6'}
    parity={name:sha(out/'site'/name)==digest for name,digest in expected.items()}
    if not all(parity.values()): raise RuntimeError('Supplied original pages differ: inspect before publishing')
    spf=lab.smallest_factors(65536)
    comparisons={m:lab.diagnostics(lab.phases(spf,lab.prime_phases(spf,m))) for m in ('golden','rank','zero')}
    dump(evidence/'phase_comparison.json',comparisons)
    excluded={'published','__pycache__','.git','.pytest_cache','build','dist','site'}
    for p in sorted(source.rglob('*')):
        rel=p.relative_to(source)
        if any(x in excluded or x.endswith('.egg-info') for x in rel.parts): continue
        if p.is_file() and p.suffix!='.pyc':
            dest=out/'source'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
    if wheel:
        run=subprocess.run([sys.executable,'-m','pip','wheel',str(source),'--no-deps','--no-build-isolation','-w',str(out/'install')],capture_output=True,text=True,timeout=180)
        (evidence/'wheel.log').write_text(run.stdout+run.stderr,encoding='utf-8')
        if run.returncode: raise RuntimeError('Wheel build failed')
    checks=[]
    if browser:
        from playwright.sync_api import sync_playwright
        errors=[];requests=[]
        def check(name, value):
            if not value: raise AssertionError(name)
            checks.append(name)
        with sync_playwright() as pw:
            options={'headless':True}
            if os.environ.get('CHROMIUM_PATH'): options['executable_path']=os.environ['CHROMIUM_PATH']
            b=pw.chromium.launch(**options);page=b.new_page(viewport={'width':1560,'height':1100})
            page.on('pageerror',lambda e:errors.append(str(e)));page.on('request',lambda r:requests.append(r.url))
            page.set_content((out/'site/index.html').read_text(encoding='utf-8'))
            f=page.frame(name='lab');f.wait_for_function('NumberFieldLab.status().drawn===65536',timeout=90000)
            check('all_65536_records',f.evaluate('NumberFieldLab.status().drawn')==65536)
            check('raw_data_equal',f.evaluate('NumberFieldLab.rawData()')==data)
            check('all_65536_phases',f.evaluate('Array.from({length:65536},(_,i)=>NumberFieldLab.phase(i))')==lab.phases(spf,lab.prime_phases(spf)))
            check('occupancy_equal',f.evaluate('NumberFieldLab.status().occupied_cells')==comparisons['golden']['occupied_cells'])
            for preset in ('golden','legacy','zero','layers'):
                f.evaluate('(p)=>NumberFieldLab.preset(p)',preset)
                check('preset_'+preset,f.evaluate('NumberFieldLab.status().drawn')==65536)
                page.screenshot(path=str(out/'site'/(preset+'.png')))
            f.evaluate('NumberFieldLab.configure({limit:1023,selected:3,k:5,overrides:{5:12345}})')
            state=f.evaluate('NumberFieldLab.snapshot()');saved=f.evaluate('NumberFieldLab.exportHTML()')
            (out/'site/saved-session-demo.html').write_text(saved,encoding='utf-8')
            page.close();page=b.new_page(viewport={'width':1560,'height':1100})
            page.on('pageerror',lambda e:errors.append(str(e)));page.on('request',lambda r:requests.append(r.url))
            page.set_content(saved);page.wait_for_function('NumberFieldLab.status().drawn===1024')
            check('saved_state_equal',page.evaluate('NumberFieldLab.snapshot()')==state)
            check('saved_data_equal',page.evaluate('NumberFieldLab.rawData()')==data)
            page.set_viewport_size({'width':390,'height':844});page.wait_for_timeout(150)
            check('mobile_no_overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'))
            page.screenshot(path=str(out/'site/mobile.png'),full_page=True)
            check('no_errors',not errors);check('no_external_requests',not any(x.startswith(('http:','https:')) for x in requests))
            dump(evidence/'browser.json',{'checks':checks,'checks_passed':len(checks),'browser':b.version,'errors':errors,'external_requests':[],'method':'Chromium supplied HTML + srcdoc; not native iOS certification'})
            b.close()
    audit=source/'publication/scale_audit.py'
    if audit.exists():
        run=subprocess.run([sys.executable,str(audit),'--out',str(out/'scale-audit')],capture_output=True,text=True,timeout=180)
        (evidence/'scale_audit.log').write_text(run.stdout+run.stderr,encoding='utf-8')
        if run.returncode: raise RuntimeError('Scale audit failed')
    (out/'OPEN_FIRST.md').write_text('# 完整数场归档\n\n打开 `site/index.html`；原始数据见 `data/source-v2.json`；源码见 `source/`；安装包见 `install/`。尺度审计见 `scale-audit/index.html`（若存在）。本目录不会自动部署公网。\n',encoding='utf-8')
    manifest={'schema':'NOLLM_FULL_ARCHIVE_V1','source_commit':os.environ.get('GITHUB_SHA'),
      'activity_id':'RA-nollm-web-preview-20260910-c6c82','population':65536,'data_sha256':core.fingerprint(data),
      'legacy_page_byte_parity':parity,'unit_tests':{'run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skipped':len(result.skipped)},
      'new_browser_checks':len(checks),'wheel_built':wheel,
      'limits':['Not a public deployment or mathematical admission.','Not a byte copy of the old conversation ZIP: screenshots/logs are freshly generated and historical evidence remains identified in source.','No Nollm runtime change.'],
      'files':[{'path':p.relative_to(out).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(out.rglob('*')) if p.is_file()]}
    dump(out/'MANIFEST.json',manifest)
    archive=out/'complete-toolkit.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(out.rglob('*')):
            if p.is_file() and p!=archive:
                i=zipfile.ZipInfo(p.relative_to(out).as_posix(),date_time=(1980,1,1,0,0,0));i.compress_type=zipfile.ZIP_DEFLATED;i.external_attr=0o644<<16
                z.writestr(i,p.read_bytes())
    dump(out/'ARCHIVE_SHA256.json',{'file':archive.name,'bytes':archive.stat().st_size,'sha256':sha(archive)})
    return manifest

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--out',type=Path,required=True);p.add_argument('--skip-browser',action='store_true');p.add_argument('--skip-wheel',action='store_true');a=p.parse_args()
    m=build(a.source,a.out,not a.skip_browser,not a.skip_wheel)
    print(json.dumps({'out':str(a.out),'files':len(m['files']),'tests':m['unit_tests'],'browser_checks':m['new_browser_checks']}))
if __name__=='__main__':main()
