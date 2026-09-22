#!/usr/bin/env python3
"""Run an unchanged retained M18 module; do not weaken any expectation."""
from __future__ import annotations
import importlib.util,json,sys,unittest,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
name=sys.argv[1];spec=importlib.util.spec_from_file_location('m20_retained_'+name,ROOT/'tools/nollm_visual_toolkit/tests'/f'{name}.py')
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
expected=[]
if name=='test_phase32_lab' and not (ROOT/'tools/nollm_visual_toolkit/nollm_visual_toolkit/phase32_lab.html').exists():
    for n in ('test_deterministic_html_and_config','test_site_three_pages_and_manifest'):
        setattr(m.Tests,n,unittest.skip('unchanged production Phase32 HTML absent from source slice')(getattr(m.Tests,n)));expected.append(n)
start=time.monotonic()
r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(m))
rec=dict(module=name,tests=r.testsRun,passed=r.testsRun-len(r.failures)-len(r.errors)-len(r.skipped),failures=len(r.failures),errors=len(r.errors),skips=len(r.skipped),expected_template_skips=expected)
out=ROOT/'evidence/migration20/retained';out.mkdir(parents=True,exist_ok=True)
(out/f'{name}.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec))
raise SystemExit(0 if r.wasSuccessful() and len(r.skipped)==len(expected) else 1)
