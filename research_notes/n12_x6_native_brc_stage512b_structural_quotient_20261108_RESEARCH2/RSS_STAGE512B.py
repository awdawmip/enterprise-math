#!/usr/bin/env python3
"""Stage512-B process-isolated peak resident set measurement (Linux ru_maxrss KiB).
Run next to REPRO_STAGE512B_COMPACT.py; no dependencies outside Python stdlib.
"""
import subprocess, sys, json, statistics, os
case={
 'n19':(19,3,[2,11],[1,3],[0,3,6,12,15,18]),
 'n28':(28,2,[2,12],[1,2],[0,20,24,26,27]),
 'n28_h5':(28,5,[2,12],[1,3],[0,5,10,17,20,24,26,27]),
 'n100_h5':(100,5,[2,61],[1,3],list(range(0,100,7)))
}
code='''import sys,resource,time,json,REPRO_STAGE512B_COMPACT as m
c=json.loads(sys.argv[1]);n,h,R,S,P=c
T=tuple(i in P for i in range(n))
f=m.fast if sys.argv[2]=='quotient' else m.old
start=time.perf_counter_ns();mask,states=f(T,h,R,S)
elapsed=(time.perf_counter_ns()-start)/1e6
print(json.dumps(dict(states=states,mask=sorted(mask),rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,wall_ms=elapsed)))'''
def main():
 result={}
 for name,c in case.items():
  methods={}
  for mode in ('reference','quotient'):
   samples=[]
   for _ in range(5):
    p=subprocess.run([sys.executable,'-c',code,json.dumps(c),mode],capture_output=True,text=True,check=True,cwd=os.path.dirname(__file__))
    samples.append(json.loads(p.stdout))
   assert all(x['mask']==samples[0]['mask'] for x in samples)
   methods[mode]={'states':samples[0]['states'],'mask':samples[0]['mask'],
      'peak_rss_KiB_samples':[s['rss_KiB'] for s in samples],
      'rss_KiB_median':statistics.median(s['rss_KiB'] for s in samples),
      'wall_ms_median':round(statistics.median(s['wall_ms'] for s in samples),4)}
  assert methods['reference']['mask']==methods['quotient']['mask']
  result[name]=methods
 return dict(schema='EM_STAGE512B_PROCESS_ISOLATED_RSS_V1',source='REPRO_STAGE512B_COMPACT.py',
    platform='Linux getrusage(RUSAGE_SELF).ru_maxrss in KiB, fresh subprocess per run',
    cases=result,assertions='PASS')
if __name__=='__main__':print(json.dumps(main(),indent=2))
