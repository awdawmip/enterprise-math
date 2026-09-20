#!/usr/bin/env python3
"""Finite full-population Python/Node record comparison; timings are telemetry."""
from __future__ import annotations
import importlib.util,json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit.multiplication_lab import smallest_factors,prime_phases,phases
from nollm_visual_toolkit.certified_hex import certified_population
spec=importlib.util.spec_from_file_location('browser_tests',ROOT/'tools/nollm_visual_toolkit/tests/test_certified_hex_browser.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
rows=[]
for count,scales in [(4096,[(1,2),(1,1),(3,2)]),(65536,[(1,1)])]:
 spf=smallest_factors(count)
 for mode in ['golden','rank','zero']:
  phi=phases(spf,prime_phases(spf,mode))
  for sn,sd in scales:
   started=time.perf_counter();js=m.results([{'op':'population','args':[phi,sn,sd]}])[0];js_elapsed=time.perf_counter()-started
   started=time.perf_counter();py=certified_population(phi,sn,sd);py_elapsed=time.perf_counter()-started
   if js!=py:raise AssertionError((count,mode,sn,sd,'full-record mismatch'))
   row={'count':count,'mode':mode,'scale':[sn,sd],'all_fields_match':True,'node_seconds_telemetry':js_elapsed,'python_seconds_telemetry':py_elapsed,'record':js};rows.append(row)
   print(count,mode,sn,sd,js['status'],js['occupied_cells'],round(js_elapsed,3),flush=True)
out=ROOT/'evidence/migration04/population_matrix.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps({'schema':'M04_FINITE_FULL_RECORD_MATRIX_V1','runs':rows,'scope':'finite population only; no asymptotic theorem; timing is not a decision input'},ensure_ascii=False,indent=2)+'\n')
