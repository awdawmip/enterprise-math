#!/usr/bin/env python3
"""Installed nollm-viz machine-report gate; fixtures are explicitly non-production."""
from __future__ import annotations
import email,json,re,shutil,subprocess,sys,tempfile,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; PKGROOT=ROOT/'tools/nollm_visual_toolkit'; REPORT=ROOT/'evidence/migration12/example_exact_report.json'
BLOBS={'core.py':'cdb8ace10e4cc8bba13b70f4da306313efb24819','division.py':'bf0b1a6b6aeccc94578d11509c5bcd12ff930cb5','exact_arithmetic.py':'35ea95b0916494b83a92386e3e313928362dd79e'}
WORKBENCH='507d39ea055942ab777d09b562c0f6c17152c4d6'
def run(c): return subprocess.run(c,text=True,capture_output=True)
def ok(c):
 r=run(c)
 if r.returncode: raise AssertionError(f'{c}\n{r.stdout}\n{r.stderr}')
 return r
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def main():
 checks=[]
 def ck(n,x):
  if not x: raise AssertionError(n)
  checks.append(n);print('PASS',n,flush=True)
 for n,h in BLOBS.items(): ck('blob_'+n,blob(ROOT/'src/enterprise_math'/n)==h)
 with tempfile.TemporaryDirectory(prefix='m14-') as d:
  d=Path(d);pkg=d/'toolkit';shutil.copytree(PKGROOT,pkg)
  if not (pkg/'README.md').exists():(pkg/'README.md').write_text('M14 metadata fixture\n')
  w=pkg/'nollm_visual_toolkit/workbench.html';prod=w.exists() and blob(w)==WORKBENCH
  if not w.exists():w.write_text('<script id="dataset" type="application/json">__PAYLOAD__</script>__FINGERPRINT__')
  wheels=d/'w';wheels.mkdir();ok([sys.executable,'-m','pip','wheel','--no-deps','--no-build-isolation',str(pkg),'-w',str(wheels)])
  tw=next(wheels.glob('nollm_visual_toolkit-*.whl'))
  with zipfile.ZipFile(tw) as z: meta=email.message_from_bytes(z.read(next(x for x in z.namelist() if x.endswith('.dist-info/METADATA'))))
  req=meta.get_all('Requires-Dist') or [];ck('exact_extra',any('enterprise-math==0.1.0' in x and 'extra == "exact"' in x for x in req));ck('not_base_dep',not any(x.startswith('enterprise-math==0.1.0') and 'extra ==' not in x for x in req))
  em=d/'em';src=em/'src/enterprise_math';src.mkdir(parents=True)
  for n in BLOBS:shutil.copy2(ROOT/'src/enterprise_math'/n,src/n)
  (src/'__init__.py').write_text('"""test fixture, not production"""\nfrom . import exact_arithmetic\n')
  (em/'pyproject.toml').write_text('[build-system]\nrequires=["setuptools>=68"]\nbuild-backend="setuptools.build_meta"\n[project]\nname="enterprise-math"\nversion="0.1.0"\n[tool.setuptools.packages.find]\nwhere=["src"]\n')
  ok([sys.executable,'-m','pip','wheel','--no-deps','--no-build-isolation',str(em),'-w',str(wheels)]);ew=next(wheels.glob('enterprise_math-*.whl'))
  v=d/'v';ok([sys.executable,'-m','venv',str(v)]);pip=v/'bin/pip';cli=v/'bin/nollm-viz';py=v/'bin/python';ok([str(pip),'install','--no-deps',str(tw)])
  out=d/'out';out.mkdir();ok([str(cli),'demo','--kind','hex','--count','16','--out',str(out/'demo.html'),'--data',str(out/'demo.json')]);ok([str(cli),'validate',str(out/'demo.json')]);ck('standalone_legacy',True)
  miss=run([str(cli),'validate',str(REPORT)]);ck('missing_exact_exit2',miss.returncode==2);ck('missing_exact_clear','requires Enterprise Math BRC' in miss.stderr and 'no approximate fallback' in miss.stderr and 'Traceback' not in miss.stderr)
  ok([str(pip),'install','--no-deps',str(ew)]);val=ok([str(cli),'validate',str(REPORT)]);ok([str(cli),'convert',str(REPORT),'--out',str(out/'cells.json')]);ok([str(cli),'convert',str(REPORT),'--out',str(out/'cells.csv')]);csvv=ok([str(cli),'validate',str(out/'cells.csv')]);ok([str(cli),'profile',str(REPORT),'--axis','s','--out',str(out/'profile.json')]);ok([str(cli),'render',str(REPORT),'--out',str(out/'view.html')]);ok([str(cli),'site',str(REPORT),'--out',str(out/'site'),'--title','M14'])
  V=json.loads(val.stdout);D=json.loads((out/'cells.json').read_text());P=json.loads((out/'profile.json').read_text());H=(out/'view.html').read_text();M=re.search(r'<script id="dataset" type="application/json">(.*?)</script>',H,re.S);S=json.loads((out/'site/manifest.json').read_text());Q=(out/'site'/S['pages'][0]['href']).read_text();N=re.search(r'<script id="dataset" type="application/json">(.*?)</script>',Q,re.S)
  ck('validate_report',V['records']==256);ck('profile_population',sum(x['count'] for x in P)==256);ck('all_identities',len(D['records'])==256);ck('no_ideal_pixels',not any(any(k.startswith('ideal') for k in x.get('fields',{})) for x in D['records']));ck('render_equal',M and json.loads(M.group(1))==D);ck('site_equal',N and json.loads(N.group(1))==D);ck('fingerprints',S['pages'][0]['sha256']==V['sha256']==json.loads(csvv.stdout)['sha256']);ck('not_auth',D['metadata']['machine_report_import']['validation']=='DETERMINISTIC_REPLAY_NOT_AUTHENTICITY')
  http=ok([str(py),'-c',"from nollm_visual_toolkit.web import preview_server;import urllib.request,sys\nwith preview_server(sys.argv[1],quiet=True) as h:\n r=urllib.request.urlopen(h.url,timeout=3);print(r.status,r.headers.get('Cache-Control'),'dataset' in r.read().decode())",str(out/'view.html')]);ck('http_readback',http.stdout.strip()=='200 no-store True')
  rec={'schema':'M14_INSTALLED_CONSOLE_GATE_V1','checks':len(checks),'passed':checks,'production_workbench_template':prod,'package_data_mode':'PRODUCTION_REMOTE_BLOB' if prod else 'EXPLICIT_TEST_FIXTURE_NOT_PRODUCTION_TEMPLATE_ACCEPTANCE','enterprise_math_runtime':'TEST_ONLY_EXACT_RUNTIME_FIXTURE_FROM_BYTE_IDENTICAL_BRC_FILES','machine_report_records':256,'machine_data_fingerprint':V['sha256'],'native_browser_navigation':'NOT_TESTED','full_enterprise_math_package':'NOT_TESTED'}
  e=ROOT/'evidence/migration14';e.mkdir(parents=True,exist_ok=True);(e/'installed_console.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2))
 return 0
if __name__=='__main__':raise SystemExit(main())
