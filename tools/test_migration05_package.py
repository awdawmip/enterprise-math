#!/usr/bin/env python3
"""M05 reconstructed-package import and preview-server checks.

The source slice omits some unchanged package files. This test reconstructs only
those unchanged files from connector-read blobs recorded under evidence/migration05,
verifies their Git blob identities, and executes the real top-level import/CLI import.
It does not claim a full wheel or whole-repository regression.
"""
from __future__ import annotations
import hashlib, json, os, shutil, subprocess, sys, tempfile, tomllib, urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLICE=ROOT/'tools/nollm_visual_toolkit/nollm_visual_toolkit'
FIXTURE=ROOT/'evidence/migration05/remote_package'
ACTUAL_ROOT=ROOT/'tools/nollm_visual_toolkit'
EXPECTED={
 '__init__.py':'145a2ae4e8dae0b7ff5dc5101502385d3942cfb9',
 '__main__.py':'f80885ff53d1a377e5706cda81e21a93eea24c5e',
 'web.py':'331007287f69b8b1411a92acdf449f4321129a87',
 'pyproject.toml':'5bb34f73970387d680673c409ccf2ea8d8365eb5',
}

def git_blob(data:bytes)->str:
 return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def main()->int:
 checks=[]
 def check(name,truth):
  if not truth: raise AssertionError(name)
  checks.append(name); print('PASS',name,flush=True)
 actual={'__init__.py':SLICE/'__init__.py','__main__.py':SLICE/'__main__.py','web.py':SLICE/'web.py','pyproject.toml':ACTUAL_ROOT/'pyproject.toml'}
 use_actual=all(p.exists() for p in actual.values())
 source=actual if use_actual else {name:FIXTURE/name for name in EXPECTED}
 for name,sha in EXPECTED.items():
  check('remote_blob_'+name,git_blob(source[name].read_bytes())==sha)
 project=tomllib.loads(source['pyproject.toml'].read_text())
 check('pyproject_cli_entrypoint',project['project']['scripts']['nollm-viz']=='nollm_visual_toolkit.__main__:main')
 check('pyproject_version',project['project']['version']=='0.3.0')
 with tempfile.TemporaryDirectory() as d:
  root=Path(d);pkg=root/'nollm_visual_toolkit';shutil.copytree(SLICE,pkg)
  if not use_actual:
   for name in ('__init__.py','__main__.py','web.py'): shutil.copy2(source[name],pkg/name)
  env=dict(os.environ);env['PYTHONPATH']=str(root)
  probe=subprocess.run([sys.executable,'-c',
   'import json,nollm_visual_toolkit as n; import nollm_visual_toolkit.__main__ as m; '
   'import nollm_visual_toolkit.multiplication_lab as lab; '
   'print(json.dumps({"version":n.__version__,"site":n.SITE_SCHEMA,"main":callable(m.main),"lab":lab.LAB_VERSION}))'],
   env=env,text=True,capture_output=True,check=True)
  data=json.loads(probe.stdout)
  check('top_level_import',data['version']=='0.3.0' and data['site']=='NOLLM_VISUAL_SITE_V1')
  check('cli_and_lab_import',data['main'] and data['lab']=='0.1.0')
  help_run=subprocess.run([sys.executable,'-m','nollm_visual_toolkit','--help'],env=env,text=True,capture_output=True)
  check('module_cli_help',help_run.returncode==0 and 'Nollm Visual Toolkit' in help_run.stdout)
  preview=root/'preview.html';preview.write_text('<!doctype html><title>M05 preview</title><p>ok</p>',encoding='utf-8')
  code='''from nollm_visual_toolkit.web import preview_server\nimport urllib.request,sys\np=sys.argv[1]\nwith preview_server(p,quiet=True) as h:\n r=urllib.request.urlopen(h.url,timeout=3)\n b=r.read().decode()\n print(r.status, r.headers.get("Cache-Control"), "M05 preview" in b)\n'''
  served=subprocess.run([sys.executable,'-c',code,str(preview)],env=env,text=True,capture_output=True,check=True)
  check('preview_server_http_readback',served.stdout.strip()=='200 no-store True')
 result={'schema':'M05_RECONSTRUCTED_PACKAGE_CHECK_V1','checks':len(checks),'passed':checks,'package_context':'ACTUAL_FULL_CHECKOUT' if use_actual else 'SOURCE_SLICE_WITH_EXACT_REMOTE_FIXTURES',
  'scope':'top-level package + __main__ import and local HTTP server using exact unchanged init/main/web blobs; not full wheel, package-data, whole repository or browser navigation'}
 out=ROOT/'evidence/migration05/package_validation.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
