#!/usr/bin/env python3
"""Reproduce the EC49FAD 591 fixed-schedule certificates from frozen ranked native-X6 inputs."""
import argparse, json, sys, importlib.util, subprocess, hashlib
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--ranked',required=True,help='EC49EXZ_ARCHIVE/ranked_exz.json from prior evidence')
p.add_argument('--generator',required=True,help='EC49EXZ_ARCHIVE/SCREEN_H5_EC49EXJ.py')
p.add_argument('--solver',required=True,help='compiled EXACT_OR_MASK_DP.cpp executable')
p.add_argument('--manifest',default=str(Path(__file__).with_name('RANGES_EC49FAD.json')))
p.add_argument('--log',default='EC49FAD_REPLAY.jsonl')
a=p.parse_args()
s=json.loads(Path(a.manifest).read_text()); rr=json.loads(Path(a.ranked).read_text())['cases']
ranks=[r for lo,hi in s['selected_ranks_expanded_from_inclusive_ranges'] for r in range(lo,hi+1)]
assert len(ranks)==len(set(ranks))==591 and len(rr)==12356
spec=importlib.util.spec_from_file_location('frozen_native',a.generator)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
log=Path(a.log)
with log.open('w') as out:
 for idx in ranks:
  z=rr[idx];assert z['bounds'][0]<76
  pre=tuple((tuple(key),typ) for h,key,typ in z['pairs'])
  assert sum(typ for key,typ in pre) in (18,20)
  data,nodes,words=mod.build_input(pre)
  digest=hashlib.sha256(data.encode()).hexdigest()
  res=subprocess.run([a.solver,'76'],input=data,text=True,capture_output=True,check=True)
  value=res.stdout.strip()
  if not value.startswith('BOUND_PASS minimum_total_at_least=76'):raise ValueError((idx,value))
  out.write(json.dumps({'rank':idx,'source_schedule':z['raw'],'native_input_sha256':digest,'native_words':words,'signed_prefix_nodes':nodes,'observations':sum(t for _,t in pre),'solver_stdout':value},sort_keys=True)+'\n')
print('PASS exact signed-X6 BRC cutoff 76:',len(ranks),'different schedules, remaining:',s['remaining_unexcluded'])
